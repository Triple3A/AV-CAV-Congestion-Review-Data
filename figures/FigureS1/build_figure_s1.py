"""Supplementary Figure S1: application family x evidence setting (non-exclusive unique-study counts).

Rows    : application families from Table S5 (final study-level application-mechanism audit). A study counts
          once in a family when it has at least one DIRECT or INDIRECT relationship coded to that family.
Columns : the six controlled evidence settings, taken from each study's `evidence_setting` in Table S2
          (final retained corpus).
Families and settings are both non-exclusive, so rows and columns do not sum to the corpus or audit totals.

Usage:
    python build_figure_s1.py data/study_application_mechanism_audit.csv data/retained_corpus.csv [output_dir]

Outputs: Figure_S1.png (600 dpi), Figure_S1.svg, Figure_S1.pdf, Figure_S1_matrix.csv,
         Figure_S1_cell_membership.csv, corpus_profile_counts.csv, source_provenance.json
"""
import csv
import hashlib
import json
import os
import re
import sys
from collections import defaultdict

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle

AUDIT = sys.argv[1] if len(sys.argv) > 1 else 'data/study_application_mechanism_audit.csv'
CORPUS = sys.argv[2] if len(sys.argv) > 2 else 'data/retained_corpus.csv'
OUT_DIR = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(os.path.abspath(__file__))
STEM = 'Figure_S1'

FAMILIES = [
    'Traffic smoothing / mobile actuator',
    'Speed harmonization / dynamic headway / bottleneck-inflow regulation',
    'Lane assignment / lane-use control',
    'Cooperative merging / coordinated gap creation / ramp coordination',
    'Integrated longitudinal–lateral bottleneck control',
    'Platooning',
    'Routing / dynamic traffic assignment / managed-lane operation',
    'Perimeter / corridor / fleet rebalancing',
]
ROW_LABELS = [
    'Traffic smoothing /\nmobile actuator',
    'Speed harmonization /\ndynamic headway /\nbottleneck-inflow regulation',
    'Lane assignment /\nlane-use control',
    'Cooperative merging /\ncoordinated gap creation /\nramp coordination',
    'Integrated longitudinal–\nlateral bottleneck control',
    'Platooning',
    'Routing / dynamic traffic\nassignment / managed-lane\noperation',
    'Perimeter / corridor /\nfleet rebalancing',
]
SETTINGS = ['Simulation', 'Analytical/theoretical', 'Network/demand model', 'Field experiment',
            'Test-track experiment', 'Observational/open-road data']
COL_LABELS = ['Simulation', 'Analytical/\ntheoretical', 'Network/\ndemand\nmodel', 'Field\nexperiment',
              'Test-track\nexperiment', 'Observational/\nopen-road\ndata']

FONT = 'Liberation Sans'
ROW_FS, COL_FS, CELL_FS, NOTE_FS = 8.5, 8.5, 9.0, 8.0
GRID_COLOR = '#2B5F8A'
CMAP = LinearSegmentedColormap.from_list('s1', ['#FFFFFF', '#2F6FAE'])
MM = 72 / 25.4
FIG_W = 180 * MM


def read(path):
    with open(path, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def settings_of(value):
    """Map a study-level evidence_setting string to the six controlled settings."""
    parts = {p.strip().lower() for p in re.split(r'[;|]', value or '') if p.strip()}
    return [s for s in SETTINGS if s.lower() in parts]


def count(audit, corpus):
    by_title = {r['title'].strip().lower(): r for r in corpus}
    by_doi = {r['doi_or_stable_url'].strip().lower(): r for r in corpus if r['doi_or_stable_url'].strip()}
    members = defaultdict(set)
    study_settings, unassigned, cid = {}, set(), {}
    for r in audit:
        if r['support_directness'] not in ('DIRECT', 'INDIRECT'):
            continue
        members[r['application_family']].add(r['study_id'])
        if r['study_id'] not in study_settings:
            c = by_doi.get(r['doi_or_stable_identifier'].strip().lower()) or by_title.get(r['title'].strip().lower())
            if c is None:
                raise SystemExit(f"{r['study_id']} not found in Table S2")
            study_settings[r['study_id']] = settings_of(c['evidence_setting'])
            cid[r['study_id']] = c['corpus_id']
            if not study_settings[r['study_id']]:
                unassigned.add(f"{r['study_id']} ({r['citation_key']})")
    unknown = set(members) - set(FAMILIES)
    if unknown:
        raise SystemExit(f'Unknown families in audit: {unknown}')
    matrix = [[sum(s in study_settings[sid] for sid in members[f]) for s in SETTINGS] for f in FAMILIES]
    totals = [len(members[f]) for f in FAMILIES]
    return matrix, totals, sorted(unassigned), members, study_settings, cid


def draw(matrix, totals):
    plt.rcParams.update({'font.family': FONT, 'svg.fonttype': 'none', 'pdf.fonttype': 42, 'axes.linewidth': 0})
    label_w, cell_w, n_gap, n_w = 50 * MM, 17.5 * MM, 4 * MM, 15 * MM
    cell_h, head_h, pad = 12.5 * MM, 15 * MM, 2 * MM
    grid_w = cell_w * len(SETTINGS)
    fig_h = head_h + cell_h * len(FAMILIES) + 2 * pad
    fig = plt.figure(figsize=(FIG_W / 72, fig_h / 72))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, FIG_W)
    ax.set_ylim(fig_h, 0)
    ax.axis('off')
    x0 = FIG_W - pad - n_w - n_gap - grid_w
    y0 = pad + head_h
    vmax = max(max(row) for row in matrix)
    for i, row in enumerate(matrix):
        y = y0 + i * cell_h
        ax.text(x0 - 2.5 * MM, y + cell_h / 2, ROW_LABELS[i], ha='right', va='center', fontsize=ROW_FS, linespacing=1.1)
        for j, v in enumerate(row):
            x = x0 + j * cell_w
            face = CMAP(v / vmax) if v else '#FFFFFF'
            ax.add_patch(Rectangle((x, y), cell_w, cell_h, facecolor=face, edgecolor=GRID_COLOR, linewidth=0.6,
                                   gid=f'cell_r{i}_c{j}'))
            ax.text(x + cell_w / 2, y + cell_h / 2, str(v), ha='center', va='center', fontsize=CELL_FS,
                    color='white' if v / vmax > 0.6 else ('#9A9A9A' if v == 0 else 'black'))
        nx = x0 + grid_w + n_gap
        ax.add_patch(Rectangle((nx, y), n_w, cell_h, facecolor='#F2F2F2', edgecolor=GRID_COLOR, linewidth=0.6))
        ax.text(nx + n_w / 2, y + cell_h / 2, str(totals[i]), ha='center', va='center', fontsize=CELL_FS,
                fontweight='bold')
    ax.add_patch(Rectangle((x0, y0), grid_w, cell_h * len(FAMILIES), facecolor='none', edgecolor=GRID_COLOR,
                           linewidth=1.1))
    for j, lab in enumerate(COL_LABELS):
        ax.text(x0 + (j + 0.5) * cell_w, y0 - 2 * MM, lab, ha='center', va='bottom', fontsize=COL_FS, linespacing=1.1)
    ax.text(x0 + grid_w + n_gap + n_w / 2, y0 - 2 * MM, 'Studies\nin family', ha='center', va='bottom',
            fontsize=COL_FS, linespacing=1.1, fontweight='bold')
    return fig


ROLES = {'Included as direct evidence': '[D]', 'Included as mechanism-supporting evidence': '[M]',
         'Included only as system context': '[C]'}
CODEBOOK_FAMILIES = [
    'Traffic smoothing / mobile-actuator control',
    'Speed harmonization / dynamic headway / bottleneck-inflow regulation',
    'Lane assignment / lane-use control',
    'Cooperative merging / coordinated gap creation / ramp coordination',
    'Integrated longitudinal–lateral bottleneck control',
    'Platooning',
    'Routing / dynamic traffic assignment / managed-lane operation',
    'Perimeter/corridor control / fleet rebalancing',
]


def write_csv(path, header, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def profile(corpus):
    """Corpus-level marginal counts reported in Section 2.1 (from Table S2)."""
    n = len(corpus)
    rows = []
    for role, lab in ROLES.items():
        k = sum(r['review_role'] == role for r in corpus)
        rows.append(['review_role', lab, k, f'{100 * k / n:.1f}'])
    sets = [settings_of(r['evidence_setting']) for r in corpus]
    for s in SETTINGS:
        k = sum(s in ss for ss in sets)
        rows.append(['evidence_setting', s, k, f'{100 * k / n:.1f}'])
    apps = [{p.strip() for p in r['operational_application'].split(';') if p.strip()} for r in corpus]
    for a in CODEBOOK_FAMILIES:
        rows.append(['operational_application', a, sum(a in aa for aa in apps), ''])
    rows.append(['coverage', 'At least one operational-application family',
                 sum(bool(set(CODEBOOK_FAMILIES) & aa) for aa in apps), ''])
    review = [r['evidence_setting'].strip().startswith('Not applicable') for r in corpus]
    rows.append(['coverage', 'Not applicable (review/context study)', sum(review), ''])
    rows.append(['coverage', 'Could not be assigned to the six controlled settings',
                 sum(not ss and not rv for ss, rv in zip(sets, review)), ''])
    return rows, n


def main():
    audit, corpus = read(AUDIT), read(CORPUS)
    matrix, totals, unassigned, members, study_settings, cid = count(audit, corpus)
    fig = draw(matrix, totals)
    os.makedirs(OUT_DIR, exist_ok=True)
    out = lambda name: os.path.join(OUT_DIR, name)
    fig.savefig(out(STEM + '.svg'))
    fig.savefig(out(STEM + '.pdf'))
    fig.savefig(out(STEM + '.png'), dpi=600)

    write_csv(out('Figure_S1_matrix.csv'), ['application_family', 'studies_in_family'] + SETTINGS,
              [[f, n] + row for f, n, row in zip(FAMILIES, totals, matrix)])
    cells = []
    for f in FAMILIES:
        for s in SETTINGS:
            ids = sorted(sid for sid in members[f] if s in study_settings[sid])
            cells.append([f, s, len(ids), '; '.join(ids), '; '.join(cid[i] for i in ids)])
    write_csv(out('Figure_S1_cell_membership.csv'),
              ['application_family', 'evidence_setting', 'study_count', 'audit_study_ids', 'corpus_ids'], cells)
    prof, n = profile(corpus)
    write_csv(out('corpus_profile_counts.csv'), ['dimension', 'category', 'study_count', f'percent_of_{n}'], prof)

    sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
    json.dump({
        'audit_source': os.path.basename(AUDIT), 'audit_sha256': sha(AUDIT),
        'corpus_source': os.path.basename(CORPUS), 'corpus_sha256': sha(CORPUS),
        'retained_record_count': n,
        'audit_studies_with_any_relationship': len({s for v in members.values() for s in v}),
        'counting_rule': ('Rows: a study counts once per family with any DIRECT or INDIRECT audit relationship. '
                          'Columns: study-level evidence_setting from the retained corpus, split on semicolons and '
                          'matched exactly to the six controlled settings. No recoding.'),
        'audit_studies_without_controlled_setting': unassigned,
    }, open(out('source_provenance.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    print('rows (family, n, counts):')
    for fam, k, row in zip(FAMILIES, totals, matrix):
        print(f'  {fam[:45]:45} n={k:2}  {row}')
    print('audit studies with no assigned setting:', unassigned or 'none')


if __name__ == '__main__':
    main()
