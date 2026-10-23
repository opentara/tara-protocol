# TARA and ODE 0.4: review of the latest changes

**23 October 2026 · Documentation and integration review.** [Русский отчёт](ode-review-2026-10-23.ru.md).

## Decision

**No change to TARA's core principles is required by the reviewed ODE changes.** ODE now describes several mechanisms that the earlier TARA-to-ODE exploration had only proposed. Publish the current TARA conceptual draft and practice materials with an updated, pinned integration account. Do not publish the historical ODE 0.2 gap list as if it described today's standard.

This conclusion concerns compatibility of concepts and contracts. It does not establish successful agent behavior, calibrated forecasts, authentic consent or working runtime enforcement.

## Scope and evidence

Reviewed repository: [opendigitalemployee/specification](https://github.com/opendigitalemployee/specification), tag [v0.4.0-draft.2](https://github.com/opendigitalemployee/specification/releases/tag/v0.4.0-draft.2), commit [`2de920485fb2665eaf7298ac65452a4a79412a9a`](https://github.com/opendigitalemployee/specification/commit/2de920485fb2665eaf7298ac65452a4a79412a9a). It was the latest release and main head at review time. This release changes release-note language; the substantive 0.4 changes were introduced in draft.1.

Current layers: 38 normative object kinds in format 0.4.0-draft; experimental decision-making 0.2.0; SELF-01 0.6.0; assessment format 0.3.0. These versions describe different artifacts. The [status](https://github.com/opendigitalemployee/specification/blob/v0.4.0-draft.2/STATUS.md), relevant contracts, schema, examples and checkers were inspected. Runtime trials were not run. [Source hashes](../sources/review.json) identify the exact material.

TARA baseline: the public overview and starter practice of 21 October 2026, plus the earlier working concept map. The private historical archive was used for comparison and is not part of this public repository.

## What changed and what it means for TARA

| ODE update | Concrete meaning | TARA conclusion |
|---|---|---|
| [Decision-making](https://github.com/opendigitalemployee/specification/blob/v0.4.0-draft.2/spec/DECISION-MAKING.md), first added in ODE 0.2 draft.3 | Method logic, applicability, method context, condition assessment, one leading focus, forecast, authority and later review are explicit. | Supports the existing bounded-step approach. Retire the blanket claim that ODE has no decision contract; enforcement and effectiveness remain open. |
| [Space and stakeholders](https://github.com/opendigitalemployee/specification/blob/v0.4.0-draft.2/spec/CONTEXT.md), introduced in 0.3 | Concerns preserve stated, observed, inferred or disputed bases. Affected parties can be absent or unresolved. Membership, representation and authority are separate. | Gives concrete form to TARA's participant, interest and disagreement concepts. It does not require a complete interest model or consensus. |
| [SELF-01 response coverage](https://github.com/opendigitalemployee/specification/blob/v0.4.0-draft.2/docs/agents/imperfect-world.md), introduced in 0.3 draft.2 | Six condition records connect signals to sourced response claims, selected methods, permitted action, limits and evidence or a routed gap. | TARA's starter can be described as a method. Availability, selection, use and evidence must remain distinct. Installing the skill is not proof of ability. |
| [Agent / DigitalEmployee / Identity / Assignment](https://github.com/opendigitalemployee/specification/blob/v0.4.0-draft.2/spec/COMMUNICATION.md), 0.4 | Persistent subject, working configuration, addressable representation and contextual assignment are distinct. Directory and role routing retain uncertainty and temporal scope. | Use these distinctions in an ODE mapping. Do not import the object kinds as mandatory TARA primitives or infer permission from an address or role. |
| Independent requests, decision extension 0.2 | An information request to one person can coexist with an authorization request to another. Approval is bound to its request and action scope. | Reinforces the existing distinction between learning, agreement and authority. No TARA core revision is needed. |
| Scoped communication, 0.4 | Discovery, routing, initiative, disclosure and declared permission are distinct; revoked, stale or ambiguous records cannot silently authorize contact. | A concrete governance application of existing boundaries. A valid description is not message delivery or authenticated permission. |

The latest SELF-01 integration explicitly cites TARA's overview, starter and governance material as an input. This is a documented design connection, not independent adoption or evidence of effectiveness.

## Nine TARA conditions and six ODE groups

This is an editorial, many-to-many reading aid. It is not a normative crosswalk or a claim that the ODE catalog exhausts TARA's subject.

| TARA starting condition | Relevant ODE groups / cross-cutting concern |
|---|---|
| Incomplete knowledge | knowledge-limits; outcome-uncertainty remains distinct |
| Different pictures of the world | knowledge-limits; goal-interest-conflicts |
| Conflicting interests | goal-interest-conflicts |
| Errors in understanding and execution | knowledge-limits; capability-execution-limits |
| Changing world and participants | changing-conditions |
| Finite resources | resource-dependency-limits |
| Human inconsistency and provisional wishes | goal-interest-conflicts; changing-conditions |
| Unequal information and influence | knowledge-limits; representation and authority across groups |
| Wider consequences and competing assessments | outcome-uncertainty; goal-interest-conflicts; review across groups |

Better information cannot guarantee an outcome. TARA's limits on exposure, bounded experiments and review remain important even when a factual question has been answered. Unequal influence and absent representation must not disappear merely because they have no separate ODE catalog code.

## Current boundaries and unresolved work

- [Issue #24](https://github.com/opendigitalemployee/specification/issues/24) remains open at review time. The decision checker cannot represent every unauthorized or unexpected observed attempt as an episode. Preserve such facts through a separately linked incident record, such as Run/Evidence, with the gap visible. Do not rewrite a failure as an admissible plan. TARA's honest-history principle already applies; this is an ODE implementation/representation limitation.
- [Issue #22](https://github.com/opendigitalemployee/specification/issues/22) is closed by independent requests; [#26](https://github.com/opendigitalemployee/specification/issues/26) is closed by the response self-diagnosis integration. Do not present either as an outstanding TARA prerequisite.
- The response guide still mentions assessment 0.2.0 and describes #22 as a remaining limitation. The current collection contract uses 0.3.0 and the decision contract implements independent requests. The product example README also retains an old “ODE 0.2 package” label. These are upstream documentation inconsistencies, not a reason to change TARA. This review uses the current contracts and records the discrepancies.
- Live enforcement, authenticated authority, human agreement, professional quality, shared resource reservations, benefits and coordination costs need separate evidence. The upstream worked examples are synthetic.
- TARA's general model of living systems and plural interests is broader than ODE's human/collective stakeholder records. Do not claim ODE represents every kind of agency or subjective interest.

## Publication result intended by this review

Keep the accepted TARA thesis and six starter practices unchanged. Publish an English-first repository with a Russian overview, existing practice downloads, candidate concepts and this dated review. Preserve the old working corpus separately. No normative TARA version, runtime adapter, efficacy result, license grant or ODE release is created by this publication.
