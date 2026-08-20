# Codebook

This file describes the main fields used in the repository datasets.

## General conventions

Multiple applicable values are separated with semicolons.

- **Not applicable** means that a field does not conceptually apply to a study.
- **Not clearly specified** means that the field is relevant but could not be determined reliably.
- **Not recoded without full text** is used where a retained source could not be checked in full during the final reconciliation.

## Review role

The retained literature is classified by its role in the review:

- **Included as direct evidence** — evaluates an AV/CAV-executed or coordinated action with a congestion-relevant collective traffic-flow outcome.
- **Included as mechanism-supporting evidence** — explains a relevant congestion mechanism, interaction, or feasible control action without directly establishing AV/CAV congestion mitigation.
- **Included only as system context** — informs deployment boundaries, network feedback, demand response, or broader system consequences.

## AV/CAV decision lever

Primitive executable actions or choices:

- Acceleration/deceleration
- Desired speed
- Desired time headway/spacing gap
- Lane choice
- Lane-change timing/execution
- Merge/yield/gap-acceptance decision
- Route choice
- Entry/access/release decision

## Design method

Typical categories include:

- Rule-based/control law
- Optimal control
- Model predictive control (MPC)
- Game-theoretic control
- Reinforcement learning / multi-agent reinforcement learning (RL/MARL)
- Heuristic control
- Other / not clearly specified

## Coordination / implementation mode

Typical categories include:

- Individual/onboard
- Cooperative V2V
- Infrastructure-assisted V2I/I2V
- Centralized
- Distributed/decentralized
- Hybrid vehicle–infrastructure

## Operational application

The application–mechanism map uses grouped operational applications including:

- Traffic smoothing / mobile-actuator control
- Speed harmonization / dynamic headway / bottleneck-inflow regulation
- Lane assignment / lane-use control
- Cooperative merging / coordinated gap creation / ramp coordination
- Integrated longitudinal–lateral bottleneck control
- Platooning
- Routing / dynamic traffic assignment / managed-lane operation
- Perimeter/corridor control / fleet rebalancing

## Facility / system scale

Examples include ring road/single lane, freeway bottleneck, on-ramp merge, lane drop, weaving section, work zone, sag curve, corridor, and network.

## Mixed-traffic condition

This field records assumptions about traffic composition and implementation, such as:

- AV/CAV penetration or controllable share
- HDV behavior
- Controller or driver heterogeneity
- Compliance
- Communication reliability
- Truck share

## Evidence setting

The setting in which the reported claim is evaluated:

- Analytical/theoretical
- Simulation
- Test-track experiment
- Field experiment
- Observational/open-road data
- Network/demand model

Design method and evidence setting are coded separately. For example, an RL controller tested in SUMO is coded as `RL/MARL` for design method and `Simulation` for evidence setting.

## Congestion mechanism

Main mechanism categories include:

- Stop-and-go waves / oscillations
- String instability
- Congestion onset / breakdown
- Capacity drop
- Queue formation / discharge
- Lane-changing friction
- Merging turbulence
- Physical spillback
- Shifted / redistributed congestion

Physical spillback and shifted/redistributed congestion are treated separately.

## Congestion metric

Examples include onset time, breakdown probability, pre-breakdown flow, post-breakdown discharge, bottleneck outflow, capacity drop, queue length, queue discharge, speed variance, delay, travel time, throughput, spillback occurrence/duration, network travel time, and VMT/VKT.

## Descriptive synthesis fields

- `key_finding` — main result relevant to the review.
- `main_limitation` — primary caveat or limitation.

## Baseline/comparator

Baseline/comparator is not a corpus-wide coding field. Where a study-specific comparator is important for interpretation, it is reported in the relevant synthesis table rather than treated as a formal taxonomy dimension.

## Dataset-specific notes

`verified_screening_matrix.csv` contains the 216 verified records considered during eligibility screening.

`retained_corpus.csv` contains the 91 publications retained in the current manuscript.

`application_mechanism_evidence_map.csv` and `application_mechanism_figure_matrix.csv` support the application–mechanism synthesis figure.

`study_application_mechanism_audit.csv` is an audit layer used to trace figure assignments back to study-level coding.

`manuscript_reference_match_audit.csv` records how the current manuscript references were reconciled with the screening matrix.
