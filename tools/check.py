#!/usr/bin/env python3
"""Check this public snapshot; no semantics, agent behavior or efficacy claim."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check():
    names = json.loads((ROOT / 'public-files.json').read_text())
    require(len(names) == len(set(names)), 'Duplicate publication entry')
    allowed = set(names)
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
              if p.is_file() and '.git' not in p.relative_to(ROOT).parts
              and '__pycache__' not in p.relative_to(ROOT).parts}
    require(actual == allowed, f'Publication inventory mismatch: missing={allowed-actual}, unexpected={actual-allowed}')
    for name in names:
        p = ROOT / name
        require(not p.is_symlink() and p.resolve().is_relative_to(ROOT), 'Unsafe publication path: '+name)
        text = p.read_text()
        local_roots = ['/'+'Users/', '/'+'private/', 'file:'+'///']
        require(not any(s in text for s in local_roots), 'Local path in public file: '+name)
        require(not re.search(r'(?:ghp_|github_pat_)[A-Za-z0-9_]{30,}', text), 'Possible credential: '+name)
        if p.suffix == '.json':
            json.loads(text)
        if p.suffix == '.md':
            for ref in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
                url = urlsplit(ref)
                if url.scheme or not url.path:
                    continue
                dest = (p.parent / unquote(url.path)).resolve()
                require(dest.is_relative_to(ROOT) and dest.is_file(), f'Broken local link: {name} -> {ref}')
    for filename, key, count in [('concepts.json','concepts',10), ('conditions.json','conditions',9)]:
        model = json.loads((ROOT / 'model' / filename).read_text())
        require(model['status'] == 'conceptual-draft', 'Model must retain draft status')
        items = model[key]
        require(len(items) == count and len({x['id'] for x in items}) == count, 'Invalid vocabulary inventory')
        for item in items:
            if key == 'concepts':
                require(set(item['label']) == set(item['meaning']) == {'en','ru'}, 'Missing concept translation')
            else:
                require(all(item[lang].get(field) for lang in ['en','ru'] for field in ['title','risk','response']), 'Incomplete condition')
    record = json.loads((ROOT / 'sources/review.json').read_text())
    require(re.fullmatch('[a-f0-9]{40}',record['ode']['commit']) is not None, 'Unpinned upstream commit')
    for item in record['ode']['files']:
        require(re.fullmatch('[a-f0-9]{64}',item['sha256']) is not None, 'Invalid source hash')
        require('/'+record['ode']['commit']+'/' in item['url'], 'Source URL must pin the reviewed commit')
    for item in record['tara']['practiceFiles']:
        require(hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest() == item['sha256'], 'Practice differs from reviewed snapshot: '+item['path'])
    print(f'PASS: {len(names)} public files, local links, JSON, 10 concepts, 9 conditions and source pins.')
    print('PASS: six practice files match the reviewed published snapshot.')
    print('No agent behavior, permissions, human agreement or efficacy verified.')


if __name__ == '__main__':
    try:
        check()
    except (ValueError, KeyError, OSError) as error:
        print('FAIL:',error,file=sys.stderr)
        raise SystemExit(1)
