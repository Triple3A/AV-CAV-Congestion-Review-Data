# Codebook

This version documents the 99-publication retained corpus after the TRID update, Comments 5-6, the targeted Wu et al. (2026) review addition in Comments 7-10, the final second-author coding check and adjudication (September 2026), the final pre-submission check (October 2026), and the October 2026 coverage update, which added Jang et al. (2025) and Wang et al. (2025) and extended the application–mechanism audit to six more studies (changes listed in `data/qa_final_coding_changes.csv`). The screening matrix contains 228 verified records from 266 candidates; 129 verified records are excluded.

## General conventions

Multiple applicable values are separated with semicolons. Values are study-specific and are not inferred from technology labels or keywords. `Not applicable` means a field does not conceptually apply. `Not clearly specified` denotes unresolved taxonomy coding. The comparator field uses the exact missing-value label `Not clearly reported`. Existing source-availability labels are preserved in other fields where appropriate.

Figure 2 groups related operational applications into eight application families for synthesis. Application family is a display grouping, not an additional taxonomy dimension.

## Review role

[D] direct congestion evidence, [M] mechanism-supporting evidence, and [C] contextual/system evidence remain the three retained review roles. [F] identifies foundational theory as a subtype of [M], not a fourth eligibility category or taxonomy dimension. Role and evidence setting remain distinct from inferential scope and methodological quality.

Corpus-level role and cell-level support directness (Table S5) are distinct constructs: an [M] or [C] study can supply direct support for a coded application–mechanism relationship only when that relationship meets the cell-level criteria in `docs/evidence_map_method.md`, and a [D] study does not supply direct support for every mechanism it discusses.

**Execution rule.** [D] requires an AV/CAV-executed or coordinated action. The same rule governs cell-level directness:

- **Type A:** AVs/CAVs execute the action, including commands computed by infrastructure that AVs/CAVs execute automatically. Eligible for [D] and for direct support.
- **Type B:** guidance that depends on human-driver compliance.
- **Type C:** infrastructure-executed control, including designs that use connected vehicles only as data sources.

Types B and C give indirect support only. A type C study is [M] when it tests a congestion mechanism or an action AVs/CAVs could execute (for example, infrastructure variable speed limits or perimeter signal control), and [C] when it serves only as deployment or network context. When both type A and type B/C scenarios are evaluated, only the type A evidence counts as direct.

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

Traffic-flow process or system-level congestion consequence that the study seeks to explain or influence. Categories include congestion onset/breakdown, capacity drop, queue formation/discharge, stop-and-go waves, string instability, lane-changing friction, merging turbulence, physical spillback, and shifted/redistributed congestion. Physical spillback and redistribution remain separate. The coded data also use four further labels where a study supports them: bottleneck activation/throughput loss, shockwave propagation, network congestion distribution, and induced demand/VMT. Figure 2 and Table S4 use the nine mechanisms listed first. The corpus-level mechanism field in Table S2 retains some legacy wording from coding done before the codebook was finalized; it is not used for any reported count, and `Table_S7_Taxonomy_Figure2_Crosswalk.csv` maps its labels to the nine Figure 2 columns.

### AV/CAV decision lever

Primitive executable continuous actions, setpoints or discrete choices: acceleration/deceleration; desired speed; desired time headway/spacing gap; lane choice; lane-change timing/execution; merge/yield/gap-acceptance decision; route choice; entry/access/release decision.

### Design method

Method used to compute, optimize, or learn the executable control decision. Categories include rule-based/control law, optimal control, MPC, game-theoretic control, RL/MARL, and heuristic control. Design method is separate from coordination/implementation mode and evidence setting.

### Coordination/implementation mode

Architecture through which actors, information, and control authority are organized. Categories include individual/onboard, cooperative V2V, infrastructure-assisted V2I/I2V, centralized, distributed/decentralized, and hybrid vehicle-infrastructure.

### Operational application

Operational traffic-management function in which decision levers and a design method are applied. Table S2 records it with the eight family labels used in Figure 2: traffic smoothing/mobile-actuator control; speed harmonization/dynamic headway/bottleneck-inflow regulation; lane assignment/lane-use control; cooperative merging/coordinated gap creation/ramp coordination; integrated longitudinal–lateral bottleneck control (joint speed/headway and lane-change or merge control at one bottleneck); platooning; routing/DTA/managed-lane operation; perimeter/corridor control/fleet rebalancing. Placement follows the application objective, not the coordination mode: deployed (commercial) ACC studies that test whether onboard controllers damp or amplify disturbances are traffic smoothing, platoon formation or string-level CACC coordination is platooning, and dedicated or reserved AV/CACC lanes are managed-lane operation. `Table_S7_Taxonomy_Figure2_Crosswalk.csv` lists the granular Appendix B categories in each family. Every family in which the final audit codes direct support for a study is included in that study's Table S2 code; a study can contribute indirect support in a family it does not implement.

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

Methodological or empirical setting in which the reported claim is evaluated. Controlled categories remain analytical/theoretical, simulation, test-track experiment, field experiment, observational/open-road data, and network/demand model. These are non-exclusive.

- A closed track, ring road or test facility with recruited drivers is a test-track experiment. A field experiment runs in operational traffic on public roads.
- Data taken from an earlier field test and used as model input do not make a simulation study a field experiment.
- A review's coverage of simulated or network studies does not make that review a new simulation or network-model experiment. All seven retained reviews (Adam 2025; Li 2023; Li 2025; Mahmassani 2016, not recoded without full text; Pan 2024; Wu 2026; Zhu 2022) carry no empirical setting. Neither do the Daganzo et al. (2002) conceptual report and the Treiber and Kesting (2013) book.

Final counts (non-exclusive, 99 studies): simulation 71, analytical/theoretical 56, network/demand model 7, field experiment 3 (Gunter et al., 2021; Jang et al., 2025; Wang et al., 2025), test-track experiment 2 (Öncü et al., 2014; Stern et al., 2018), observational/open-road data 1 (Cassidy and Bertini, 1999); 9 records carry no setting.

Among the 62 [D] studies the counts are: simulation 60, analytical/theoretical 37, network/demand model 3, field 3, test-track 1, observational 0.

### Congestion metric

Outcome used to evaluate the congestion claim. Examples include onset time, breakdown probability, pre-breakdown flow, post-breakdown discharge, bottleneck outflow, capacity drop, queue length/discharge, speed variance, delay, travel time, throughput, storage occupation, blocked upstream movements, spillback duration, system travel time, and VMT/VKT. Throughput, discharge and capacity are not interchangeable. RL reward remains distinct from traffic-flow outcomes: a retained RL/MARL study must report an independently interpretable traffic-flow or congestion outcome rather than reward or cumulative return alone. The outcome may use the same traffic quantity as a reward component, provided it is reported and interpreted separately as an evaluation result. Person-based managed-lane and safety/deployment reporting requirements are unchanged.

## Descriptive extraction fields

- `key_finding`: main result relevant to the review.
- `main_limitation`: primary caveat or limitation.
- `comparator_reference_condition`: Study-specific traffic, control, policy, or algorithmic reference condition against which the reported intervention or congestion outcome is evaluated.

Key finding, main limitation, and comparator/reference condition were recorded as descriptive extraction fields for synthesis and audit rather than as taxonomy dimensions.

### Comparator coding rule

Extract the actual reference condition from the original study material. Record multiple substantive comparators separated by semicolons, and distinguish intervention baselines from references used to calculate a metric or validate a model. Do not infer an all-HDV or uncontrolled baseline merely from an improvement percentage. Use `Not applicable` when no comparator applies to the retained synthesis role, and `Not clearly reported` when a relevant comparator cannot be established confidently from available original material, including inaccessible or insufficient full text. This latter code is not a claim that the original publication itself omitted a comparator.

`Table_S2_Retained_Corpus.csv` is authoritative for the comparator field across all 99 retained publications. The screening matrix has no comparator extraction column.

Final comparator counts are 73 source-supported explicit comparators, 18 `Not applicable`, and 8 `Not clearly reported`. Only the eight `Not clearly reported` records require author verification of the comparator; no baseline is invented for them.

## Dataset-specific notes

- `Table_S1_Verified_Screening_Matrix.csv`: 228 verified records with record-level screening dispositions. The six records from the targeted coverage check carry their disposition in `Row audit notes`. No comparator field.
- `Table_S2_Retained_Corpus.csv`: 99 records, with review roles (62 [D], 27 [M], 10 [C]), exactly nine taxonomy dimensions, and descriptive and audit fields. Records changed by the final adjudication or the final pre-submission check say so in `audit_note`. Reference strings, years and venues follow the version-of-record metadata (Crossref/publisher).
- `Table_S3_Screening_Flow.csv`: the counts shown in Figure 1 (266 candidates, 228 verified, 99 retained). The 38 records removed at verification include duplicates, overlapping versions and unverifiable records; counts by removal reason, and by category for the 129 eligibility exclusions, were not recorded (the five exclusions from the targeted coverage check have recorded reasons in Table S1).
- `Table_S5_Study_Application_Mechanism_Audit.csv`: the study-level application–mechanism audit of 77 retained studies. It has one row per study × application family × congestion mechanism, coded DIRECT, INDIRECT or NONE. A finding pattern (`consistent_positive`, `mixed`, `negative`, `strongly_conditional`) is recorded for direct relationships only, together with the supporting metric, evidence setting, full-text rationale and source location. Rows changed at adjudication or in the final pre-submission check are marked in `full_text_rationale`. Six operational-application-coded studies are not in the audit; all six are reviews. Cai et al. (2024), Stern et al. (2018), Vishnoi et al. (2024) and Wu et al. (2022) were added to the audit in the coverage update, together with the two new studies. Two system-context studies without an operational application (Perrine et al., 2020; Zhao and Kockelman, 2018) are in it; Perrine et al. (2020) is kept as a NONE record.
- `Table_S4_Application_Mechanism_Evidence_Map.csv`: the mechanical aggregation of Table S5 into the 8 × 9 map (106 direct and 76 indirect links; 4 ●, 34 ○, 7 □, 27 —). Marker rules are in `docs/evidence_map_method.md`.
- `Table_S7_Taxonomy_Figure2_Crosswalk.csv`: crosswalk from study-level mechanism and application codes to the Figure 2 columns and families.
- `qa_final_coding_changes.csv`: every change made in the final pre-submission check and in the coverage update, with its basis.
- `Table_S6_Independent_Coding_Agreement.csv`, `Table_S6_legacy_label_review.csv`, `independent_coding_check_adjudication.csv` and `evidence_role_reconciliation.csv`: the second-author coding check of 19 studies (exact-set agreement for multi-label fields; mean Jaccard similarity as a secondary diagnostic), the treatment of legacy lead-coding labels, the record-level adjudication of all 105 disagreements, and the re-check of the evidence-role reassessments. Hung and Zhang (2022) was changed from [D] to [M] by author decision after the adjudication; this is recorded in its Table S2 audit note and Table S5 rationale.
- Figure S1: application families from Table S5 against study-level evidence settings from Table S2, as unique-study counts. No maturity scores are used.
