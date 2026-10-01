# Codebook

This version documents the 97-publication retained corpus after the TRID update, Comments 5-6, and the targeted Wu et al. (2026) review addition in Comments 7-10, and the final second-author coding check and adjudication (September 2026). The screening matrix contains 222 verified records from 260 candidates; 125 verified records are excluded.

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

Traffic-flow process or system-level congestion consequence that the study seeks to explain or influence. Categories include congestion onset/breakdown, capacity drop, queue formation/discharge, stop-and-go waves, string instability, lane-changing friction, merging turbulence, physical spillback, and shifted/redistributed congestion. Physical spillback and redistribution remain separate. The coded data also use four further labels where a study supports them: bottleneck activation/throughput loss, shockwave propagation, network congestion distribution, and induced demand/VMT. Figure 2 and Table S4 use the nine mechanisms listed first.

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

The split was made record by record using existing coded study context and available original sources. Ambiguous subfields are coded `Not clearly specified`. `legacy_facility_system_scale` preserves the previous composite value for traceability only; it is not an active taxonomy field. The legacy value is never used to normalize facility-based counts.

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

`Table_S2_Retained_Corpus.csv` is authoritative for the comparator field across all 97 retained publications. The screening matrix has no comparator extraction column.

Final comparator counts are 71 source-supported explicit comparators, 18 `Not applicable`, and 8 `Not clearly reported`. Only the eight `Not clearly reported` records require author verification of the comparator; no baseline is invented for them.

## Dataset-specific notes

- `Table_S1_Verified_Screening_Matrix.csv`: 222 verified records with record-level screening dispositions. No comparator field.
- `Table_S2_Retained_Corpus.csv`: 97 records, with review roles (61 [D], 26 [M], 10 [C]), exactly nine taxonomy dimensions, and descriptive and audit fields. Records changed by the final adjudication say so in `audit_note`.
- `Table_S3_Screening_Flow.csv`: the counts shown in Figure 1 (260 candidates, 222 verified, 97 retained).
- `Table_S5_Study_Application_Mechanism_Audit.csv`: the study-level application–mechanism audit of 71 retained studies. It has one row per study × application family × congestion mechanism, coded DIRECT, INDIRECT or NONE. A finding pattern (`consistent_positive`, `mixed`, `negative`, `strongly_conditional`) is recorded for direct relationships only, together with the supporting metric, evidence setting, full-text rationale and source location. Rows changed at adjudication are marked in `full_text_rationale`.
- `Table_S4_Application_Mechanism_Evidence_Map.csv`: the mechanical aggregation of Table S5 into the 8 × 9 map. Marker rules are in `docs/evidence_map_method.md`.
- `Table_S6_Independent_Coding_Agreement.csv`, `Table_S6_legacy_label_review.csv`, `independent_coding_check_adjudication.csv` and `evidence_role_reconciliation.csv`: the second-author coding check of 19 studies (exact-set agreement for multi-label fields; mean Jaccard similarity as a secondary diagnostic), the treatment of legacy lead-coding labels, the record-level adjudication of all 105 disagreements, and the re-check of the evidence-role reassessments. Hung and Zhang (2022) was changed from [D] to [M] by author decision after the adjudication; this is recorded in its Table S2 audit note and Table S5 rationale.
- Figure S1: application families from Table S5 against study-level evidence settings from Table S2, as unique-study counts. No maturity scores are used.
