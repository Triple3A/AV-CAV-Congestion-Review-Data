# Codebook

This version documents the 97-publication retained corpus after the TRID update, Comments 5-6, and the targeted Wu et al. (2026) review addition in Comments 7-10. The screening matrix contains 222 verified records from 260 candidates; 125 verified records are excluded.

## General conventions

Multiple applicable values are separated with semicolons. Values are study-specific and are not inferred from technology labels or keywords. `Not applicable` means a field does not conceptually apply. `Not clearly specified` denotes unresolved taxonomy coding. The comparator field uses the exact missing-value label `Not clearly reported`. Existing source-availability labels are preserved in other fields where appropriate.

Figure 2 groups related operational applications into eight application families for synthesis. Application family is a display grouping, not an additional taxonomy dimension.

## Review role

[D] direct congestion evidence, [M] mechanism-supporting evidence, and [C] contextual/system evidence remain the three retained review roles. [F] identifies foundational theory as a subtype of [M], not a fourth eligibility category or taxonomy dimension. Role and evidence setting remain distinct from inferential scope and methodological quality.

## Taxonomy dimensions and active fields

The taxonomy has exactly nine dimensions. Operating context has two subfields; these do not add a tenth dimension.

| Dimension | Active CSV field(s) |
| --- | --- |
| Congestion mechanism | `congestion_mechanism` |
| AV/CAV decision lever | `av_cav_decision_lever` |
| Design method | `design_method` |
| Coordination/implementation mode | `coordination_implementation_mode` |
| Operational application | `operational_application` |
| Operating context | `facility_context`; `spatial_system_scale` |
| Mixed-traffic and deployment conditions | `mixed_traffic_deployment_conditions` |
| Evidence setting | `evidence_setting` |
| Congestion metric | `congestion_metric` |

### Congestion mechanism

Traffic-flow process or system-level congestion consequence that the study seeks to explain or influence. Categories include congestion onset/breakdown, capacity drop, queue formation/discharge, stop-and-go waves, string instability, lane-changing friction, merging turbulence, physical spillback, and shifted/redistributed congestion. Physical spillback and redistribution remain separate.

### AV/CAV decision lever

Primitive executable continuous actions, setpoints or discrete choices: acceleration/deceleration; desired speed; desired time headway/spacing gap; lane choice; lane-change timing/execution; merge/yield/gap-acceptance decision; route choice; entry/access/release decision.

### Design method

Method used to compute, optimize, or learn the executable control decision. Categories include rule-based/control law, optimal control, MPC, game-theoretic control, RL/MARL, and heuristic control. Design method is separate from coordination/implementation mode and evidence setting.

### Coordination/implementation mode

Architecture through which actors, information, and control authority are organized. Categories include individual/onboard, cooperative V2V, infrastructure-assisted V2I/I2V, centralized, distributed/decentralized, and hybrid vehicle-infrastructure.

### Operational application

Operational traffic-management function in which decision levers and a design method are applied. The existing eight grouped families are retained: traffic smoothing/mobile-actuator control; speed harmonization/dynamic headway/bottleneck-inflow regulation; lane assignment/lane-use control; cooperative merging/coordinated gap creation/ramp coordination; integrated longitudinal-lateral bottleneck control; platooning; routing/DTA/managed-lane operation; perimeter/corridor control/fleet rebalancing.

Application-family membership describes review coverage, including contextual reviews where previously coded. It does not make a review an operational intervention or a Figure 2 supporting study. Wu et al. (2026) belongs to the managed-lane review family, but is not added to S5 or Figure 2 support.

### Operating context

Physical facility/geometry and spatial or system scale at which the strategy and traffic effect are evaluated.

- `facility_context`: physical or geometric traffic environment in which the control or mechanism is evaluated. Categories include ring-road/single-lane testbed, basic freeway or motorway segment, on-ramp merge, lane drop, weaving section, work zone/lane closure, sag curve, other explicitly defined geometry, and not facility-specific. Corridor and network are not facility types. Urban intersections, diverge/off-ramp bottlenecks, tunnel bottlenecks, and moving bottlenecks are retained when supported by the study context.
- `spatial_system_scale`: level at which the traffic effect or control outcome is evaluated. Categories are vehicle string/platoon, local road segment, bottleneck/local facility, corridor, and network/system. Mere mention of routes, downstream traffic or a simulation network does not establish network-scale evaluation. Reviews and books without an original evaluation receive `Not applicable` for this subfield.

The split was made record by record using existing coded study context and available original sources. Ambiguous subfields are `Not clearly specified` and appear in `author_verification_queue.csv`. `legacy_facility_system_scale` preserves the previous composite value for traceability only; it is not an active taxonomy field. The legacy value is never used to normalize facility-based counts.

### Mixed-traffic and deployment conditions

Assumptions governing traffic composition, effective control authority, human response, controller heterogeneity, connectivity/communication, and other deployment conditions that can alter the realized control effect.

Components may include AV/CAV market penetration; controllable share; connected but human-driven share; HDV car-following behavior/calibration; HDV lane-changing and cut-in response; controller heterogeneity; compliance; heavy-vehicle share; communication reliability/latency where modeled; sensing/state-estimation limitations where modeled; and fallback or operational-design-domain limits where reported. These are components of one dimension, not separate dimensions. Renaming the field preserves its previously coded values and does not imply that every component was extracted for every study.

### Evidence setting

Methodological or empirical setting in which the reported claim is evaluated. Controlled categories remain analytical/theoretical, simulation, test-track experiment, field experiment, observational/open-road data, and network/demand model. These are non-exclusive. A review's coverage of simulated or network studies does not make that review a new simulation or network-model experiment. Wu et al. (2026) is coded `Not applicable (review/context study)` and contributes no heatmap cell. Existing coding for earlier records is unchanged in this targeted revision.

### Congestion metric

Outcome used to evaluate the congestion claim. Examples include onset time, breakdown probability, pre-breakdown flow, post-breakdown discharge, bottleneck outflow, capacity drop, queue length/discharge, speed variance, delay, travel time, throughput, storage occupation, blocked upstream movements, spillback duration, system travel time, and VMT/VKT. Throughput, discharge and capacity are not interchangeable. RL reward remains distinct from independently measured traffic-flow outcomes. Person-based managed-lane and safety/deployment reporting requirements are unchanged.

## Descriptive extraction fields

- `key_finding`: main result relevant to the review.
- `main_limitation`: primary caveat or limitation.
- `comparator_reference_condition`: Study-specific traffic, control, policy, or algorithmic reference condition against which the reported intervention or congestion outcome is evaluated.

Key finding, main limitation, and comparator/reference condition were recorded as descriptive extraction fields for synthesis and audit rather than as taxonomy dimensions.

### Comparator coding rule

Extract the actual reference condition from the original study material. Record multiple substantive comparators separated by semicolons, and distinguish intervention baselines from references used to calculate a metric or validate a model. Do not infer an all-HDV or uncontrolled baseline merely from an improvement percentage. Use `Not applicable` when no comparator applies to the retained synthesis role, and `Not clearly reported` when a relevant comparator cannot be established confidently from available original material, including inaccessible or insufficient full text. This latter code is not a claim that the original publication itself omitted a comparator.

`retained_corpus.csv` is authoritative across all 97 retained publications, including the original 96. S5 copies the comparator and both context subfields by stable `corpus_id`; it never independently recodes them. The screening matrix has no comparator extraction column.

Source access, evidence basis and verification tasks are recorded in `comparator_context_source_audit.csv`. The original 96 contain 71 source-supported explicit comparators, 17 `Not applicable`, and 8 `Not clearly reported`. Adding Wu increases only `Not applicable`, producing final counts of 71, 18, and 8. Only the eight `Not clearly reported` records require author verification of the comparator; the audit does not invent a baseline for them.

## Dataset-specific notes

- `retained_corpus.csv`: 97 records; exactly nine taxonomy dimensions plus descriptive and audit fields.
- `verified_screening_matrix.csv`: 222 verified records; the new review's [C] disposition is recorded in its audit note. No comparator field is added.
- `study_application_mechanism_audit.csv` (Table S5): 71 operational-study records. `corpus_id` links to the master; comparator and context values are exact copies. Previous `facility_tags` values are retained only as `legacy_facility_tags`.
- `application_mechanism_evidence_map.csv` (Table S4): marker assignments and supporting-study membership remain unchanged. The two context subfields aggregate linked S5/master values; `legacy_typical_facilities` preserves old broad tags for audit only.
- `manuscript_reference_match_audit.csv`: matches all 96 supplied bibliography entries and documents the proposed Wu insertion as the 97th retained reference. The supplied DOCX is not represented as already edited.
- `comparator_context_source_audit.csv`: one row per retained publication with evidence basis, access level and verification flags.
- `author_verification_queue.csv`: eight unresolved comparators and eight ambiguous operating-context splits; because one record appears in both groups, the queue contains 15 distinct publications.
- Figure S1: keep the finalized application-by-evidence-setting heatmap. Counts are regenerated from the revised master; review/no-setting records are reported separately. No maturity scores are used.
