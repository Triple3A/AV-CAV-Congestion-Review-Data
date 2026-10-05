# Application-Family–Mechanism Evidence Map

The application–mechanism map summarizes how the operational applications reviewed in the paper relate to the congestion mechanisms used in the synthesis.

The map is intended as a qualitative evidence summary, not a meta-analysis.

## Corpus role and cell-level directness

Corpus-level evidence role ([D], [M], [C] in Table S2) and application–mechanism support directness (DIRECT, INDIRECT, NONE in Table S5) are distinct coding constructs. An [M] or [C] study can provide direct support for a coded application–mechanism relationship only when that relationship meets the cell-level criteria below. A [D] study does not provide direct support for every mechanism it discusses.

In the final audit, the 106 direct study–cell links come from [D] studies (102), [M] studies (3: Hung and Zhang, 2022; Öncü et al., 2014; Qin and Wang, 2023, all platooning × string instability) and one [C] study (Chakraborty et al., 2021, routing/managed-lane operation × shifted/redistributed congestion, coded mixed).

## Direct support

Direct support is cell-specific. A study contributes to `direct_supporting_study_count` only when all of the following hold:

1. It is coded to the relevant application family.
2. AVs/CAVs execute the controlled action (execution rule below).
3. It directly evaluates or reports the relevant congestion mechanism or a mechanism-specific outcome.
4. It provides a traffic-flow or congestion outcome supporting that relationship.

**Execution rule.**

| Type | What executes the action | Coding |
|---|---|---|
| A | AVs/CAVs execute the action, including commands computed by infrastructure that AVs/CAVs execute automatically. | Can be direct. |
| B | Guidance that depends on human-driver compliance. | Indirect only. |
| C | Infrastructure executes the control (for example, variable speed limits or signals), including designs that use connected vehicles only as data sources. | Indirect only. |

When a study evaluates both a type A scenario and a type B or C scenario, only the type A evidence can be direct.

**Mechanism-specific requirements.** Direct capacity-drop support requires a stated sustainable or reference pre-breakdown flow or capacity estimate compared with sustained post-breakdown or queue discharge under comparable conditions. Higher throughput, outflow, travel-time improvement or lane balancing alone is not coded as capacity or capacity-drop mitigation. Physical spillback requires a queue boundary relative to finite storage and is kept separate from shifted/redistributed congestion.

## Finding pattern

A finding pattern is recorded for direct relationships only:

- `consistent_positive`: the intervention moves the coded mechanism in the mitigating direction under the tested conditions. Examples are less capacity drop, less physical spillback, or less shifted/redistributed congestion. A result showing that congestion merely moved elsewhere is not positive for the shifted/redistributed-congestion cell.
- `mixed`: benefits and harms are both reported for the mechanism.
- `negative`: the intervention worsens the mechanism.
- `strongly_conditional`: the direction depends on demand, penetration, comparator or another tested condition.

The same study may be coded differently across mechanisms. When it is, the rationale in Table S5 explains why.

## Marker assignment

**● Repeated, consistently positive direct support**

Requires `direct_supporting_study_count >= 2` with every direct study coded `consistent_positive`.

**○ Limited or mixed direct support**

Requires `direct_supporting_study_count >= 1` and either `direct_supporting_study_count = 1` or at least one direct finding coded mixed, negative or strongly conditional.

**□ Indirect influence only**

Requires `direct_supporting_study_count = 0` and `indirect_supporting_study_count >= 1`.

**— No substantive relationship identified**

Requires `direct_supporting_study_count = 0` and `indirect_supporting_study_count = 0`.

Marker categories describe the pattern of support in the retained coded set. They do not measure methodological quality, field validation, causal certainty across settings, deployment readiness or treatment-effect magnitude. Several consistent simulation studies may therefore yield ● while the evidence setting remains simulation. A dash indicates only that no substantive relationship was identified in the retained corpus.

## Source data and aggregation

The map is aggregated mechanically from the study-level audit in `data/Table_S5_Study_Application_Mechanism_Audit.csv` by `scripts/build_evidence_map.py`. That file has one row per study × application family × congestion mechanism, coded DIRECT, INDIRECT or NONE. No study-level field is reinterpreted during aggregation. `data/Table_S7_Taxonomy_Figure2_Crosswalk.csv` documents how the granular taxonomy categories map to the nine mechanism columns and eight application families.

The cell-level result is `data/Table_S4_Application_Mechanism_Evidence_Map.csv`. For each of the 72 cells it records:

- the final marker and its meaning;
- the direct and indirect supporting-study counts, IDs and citations;
- counts of direct findings by pattern (consistently positive, mixed, negative, strongly conditional);
- the evidence roles and evidence settings of the supporting studies;
- representative supporting metrics;
- a short cell rationale.

The final map contains 106 direct and 76 indirect study–cell links, giving 4 ●, 34 ○, 7 □ and 27 — cells. The filled cells are:

- lane assignment/lane-use control × queue formation/discharge;
- lane assignment/lane-use control × lane-changing friction;
- integrated longitudinal–lateral bottleneck control × lane-changing friction;
- integrated longitudinal–lateral bottleneck control × merging turbulence (Hu and Sun, 2019; Cai et al., 2024).

Cai et al. (2024) is placed in integrated longitudinal–lateral control because one controller sets both acceleration and lane changes at the merge, as in the combined case of Hu and Sun (2019). If it were placed in cooperative merging instead, the integrated × merging-turbulence cell would become open and the cooperative-merging × merging-turbulence cell would stay open, leaving three filled cells.

`figures/Figure2/build_figure_2.py` draws Figure 2 from the `final_marker` column without recomputing any marker.

An internal robustness check removed four high-leverage studies together (Nagalur Subraveti et al., 2021; Kim et al., 2023; Yang et al., 2018; Xiao et al., 2022). Three filled cells remain: lane-use × queue formation/discharge, integrated control × lane-changing friction and integrated control × merging turbulence. Removing either Nagalur Subraveti et al. or Kim et al. alone leaves all four filled cells. The integrated × merging-turbulence cell rests on two studies and becomes open if either is removed.

Study count is descriptive. It is not interpreted as an effect-size estimate or an evidence-quality score.

The map should therefore be read together with the study context, evidence setting, congestion metric and limitations reported elsewhere in the review.
