# TARA Protocol

**Coordinate an acceptable next step in an imperfect world.**

TARA does not assume that every interest can be described in advance or aligned once and for all. It helps people, AI agents and collective structures choose a feasible, authorized next step while keeping unknowns, disagreements, commitments and the possibility of revision visible.

This is the public development repository of TARA Protocol, supported by [TARA — Institute for Consciousness & Agency](https://opentara.org/). It contains a conceptual draft and experimental practice materials. It is not a released normative specification, executable language, runtime or certification system.

## Start with your agent

1. Download [the starter skill](skills/tara-next-step/SKILL.md), or [its Russian version](translations/ru/skills/tara-next-step/SKILL.md).
2. Attach it to a new conversation with your agent and ask it to apply the principles to one task. The file supplies instructions; attaching it does not install a persistent skill or change the model.
3. Use the [personal-agent trial](examples/personal-agent-trial.md). Check whether the agent preserves unknowns and different interests, stays within authority and proposes a review point.

The skill is experimental v0.1. A correct-looking answer or an installed file is not evidence of reliable behavior. Compare several situations, failures and the additional cost of coordination.

## Read and use

| Material | Purpose |
|---|---|
| [Protocol overview](docs/protocol.en.md) · [По-русски](docs/protocol.ru.md) | Nine conditions of the real world, the next-step cycle, agents and governance |
| [Working concepts](model/concepts.json) | Candidate vocabulary; no normative grammar or ODE object equivalence |
| [Conditions](model/conditions.json) | The bilingual nine-condition starting set, with implications for action |
| [Situation worksheet](worksheets/next-step.en.txt) · [RU](worksheets/next-step.ru.txt) | Prepare one bounded step with affected participants |
| [Governance questions](governance/questions.en.txt) · [RU](governance/questions.ru.txt) | Decision rights, enforceable limits, handoffs and admission of changes |
| [ODE review, 23 October 2026](docs/ode-review-2026-10-23.md) · [RU](docs/ode-review-2026-10-23.ru.md) | What ODE 0.4 already describes, what stays open, and why TARA's core does not need revision |
| [Source record](sources/review.json) | Exact upstream version and file hashes used for this review |

## Relationship to Open Digital Employee

TARA supplies general concepts for cooperation. [Open Digital Employee](https://github.com/opendigitalemployee/specification) gives digital employees their own versioned description contracts, procedures and structural checks. Domain methods supply professional judgment; execution environments enforce permissions, budgets and stopping.

Reviewed baseline: **ODE v0.4.0-draft.2**, core format **0.4.0-draft**, decision extension **0.2.0**. The latest ODE work supports TARA's existing principles; it does not require a new TARA core. Earlier ODE 0.2 gap assessments are historical, not the current integration status. See the [review](docs/ode-review-2026-10-23.md).

Neither repository automatically changes the other. ODE's six operating-condition groups and TARA's nine starting conditions have different granularity. They are not competing version numbers or a one-to-one taxonomy.

## Development and evidence

Keep conceptual proposals, description contracts, structural validation, observed behavior and real-world effects separate. Unknowns and missing evidence are valid results. Improving a metric does not grant permission; a new version does not establish an improvement.

Contributions can bring a concrete situation, a proposed distinction, an implementation or a bounded comparison. State whose interests and authority are involved, what evidence supports the proposal and what remains unknown. Do not submit private agent memories, personal profiles or credentials. Use English for public issues and pull requests; the Russian guides remain available for reading.

Check the repository's structure and publication boundary with:

```sh
python3 tools/check.py
```

That check does not evaluate agent behavior. No automatic installer, runtime adapter or formal conformance claim is included.

**License:** a project-wide license has not yet been selected. Linked upstream projects retain their own licenses; this repository does not inherit ODE's licensing by reference.
