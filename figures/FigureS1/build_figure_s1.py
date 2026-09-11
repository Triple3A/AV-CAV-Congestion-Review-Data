"""Generate descriptive counts without recoding the source matrix.

Run with Python, numpy, and matplotlib installed:
  python build_figure_s1.py /path/to/retained_corpus.csv
"""
import csv
import hashlib
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

SOURCE_URL = 'https://github.com/Triple3A/AV-CAV-Congestion-Review-Data/blob/main/data/retained_corpus.csv'
APPLICATIONS = [
    'Traffic smoothing / mobile-actuator control',
    'Speed harmonization / dynamic headway / bottleneck-inflow regulation',
    'Lane assignment / lane-use control',
    'Cooperative merging / coordinated gap creation / ramp coordination',
    'Integrated longitudinal–lateral bottleneck control',
    'Platooning',
    'Routing / dynamic traffic assignment / managed-lane operation',
    'Perimeter/corridor control / fleet rebalancing',
]
SETTINGS = ['Analytical/theoretical', 'Simulation', 'Test-track experiment',
            'Field experiment', 'Observational/open-road data', 'Network/demand model']
ROLES = {'Included as direct evidence': '[D]',
         'Included as mechanism-supporting evidence': '[M]',
         'Included only as system context': '[C]'}
CAPTION = ('Figure S1. Evidence settings across AV/CAV congestion-control application families. '
           'Cells report numbers of retained studies coded to each application–evidence-setting combination. '
           'Application and evidence-setting fields are multi-label, so counts are non-exclusive '
           'and should not be summed as independent study totals.')

def labels(record, field):
    return {value.strip() for value in record[field].split(';') if value.strip()}

source = Path(sys.argv[1])
out = Path(__file__).resolve().parent
records = list(csv.DictReader(source.open(encoding='utf-8-sig', newline='')))
assert len(records) == 96
assert len({r['corpus_id'] for r in records}) == 96
application_sets = [labels(r, 'operational_application') for r in records]
setting_sets = [labels(r, 'evidence_setting') for r in records]
matrix = np.array([[sum(a in aa and e in ee for aa, ee in zip(application_sets, setting_sets))
                    for e in SETTINGS] for a in APPLICATIONS], dtype=int)
with (out / 'Figure_S1_matrix.csv').open('w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['operational_application'] + SETTINGS)
    writer.writerows([[a] + row.tolist() for a, row in zip(APPLICATIONS, matrix)])

with (out / 'corpus_profile_counts.csv').open('w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['dimension', 'category', 'study_count', 'percent_of_96'])
    for role, label in ROLES.items():
        n = sum(r['review_role'] == role for r in records)
        writer.writerow(['review_role', label, n, f'{n/96*100:.1f}'])
    for setting in SETTINGS:
        n = sum(setting in ss for ss in setting_sets)
        writer.writerow(['evidence_setting', setting, n, f'{n/96*100:.1f}'])
    for application in APPLICATIONS:
        n = sum(application in aa for aa in application_sets)
        writer.writerow(['operational_application', application, n, ''])
    writer.writerow(['coverage', 'At least one operational-application family',
                     sum(bool(set(APPLICATIONS) & aa) for aa in application_sets), ''])
    writer.writerow(['coverage', 'No controlled evidence-setting label',
                     sum(not (set(SETTINGS) & ss) for ss in setting_sets), ''])

# Study identifiers make each plotted count independently traceable.
with (out / 'Figure_S1_cell_membership.csv').open('w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['operational_application', 'evidence_setting', 'study_count', 'corpus_ids'])
    for a in APPLICATIONS:
        for e in SETTINGS:
            ids = [r['corpus_id'] for r, aa, ee in zip(records, application_sets, setting_sets)
                   if a in aa and e in ee]
            writer.writerow([a, e, len(ids), '; '.join(ids)])

unmapped = [{'corpus_id': r['corpus_id'], 'citation_key': r['citation_key'],
             'evidence_setting': r['evidence_setting']}
            for r, ss in zip(records, setting_sets) if not set(SETTINGS) & ss]
(out / 'source_provenance.json').write_text(json.dumps({
    'source_url': SOURCE_URL,
    'retrieved_date_utc': '2026-09-11',
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'retained_record_count': len(records),
    'counting_rule': 'Split existing semicolon-delimited labels; count each corpus_id once per combination. No recoding.',
    'unmapped_evidence_records': unmapped,
}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

row_labels = [
    'Traffic smoothing /\nmobile-actuator control',
    'Speed harmonization / dynamic headway /\nbottleneck-inflow regulation',
    'Lane assignment /\nlane-use control',
    'Cooperative merging / coordinated gap\ncreation / ramp coordination',
    'Integrated longitudinal–lateral\nbottleneck control',
    'Platooning',
    'Routing / dynamic traffic assignment /\nmanaged-lane operation',
    'Perimeter/corridor control /\nfleet rebalancing',
]
column_labels = ['Analytical/\ntheoretical', 'Simulation', 'Test-track\nexperiment',
                 'Field\nexperiment', 'Observational/\nopen-road data', 'Network/\ndemand model']
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12, 'svg.fonttype': 'none'})
fig = plt.figure(figsize=(13.5, 8.4), facecolor='white')
ax = fig.add_axes([0.38, 0.22, 0.54, 0.61])
im = ax.imshow(matrix, cmap='Blues', vmin=0, vmax=36, aspect='auto', interpolation='nearest')
ax.set_xticks(range(6), labels=column_labels, fontsize=11)
ax.set_yticks(range(8), labels=row_labels, fontsize=11.5)
ax.xaxis.tick_top()
ax.tick_params(axis='both', length=0, pad=10)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_xticks(np.arange(-0.5, 6, 1), minor=True)
ax.set_yticks(np.arange(-0.5, 8, 1), minor=True)
ax.grid(which='minor', color='white', linewidth=2)
ax.tick_params(which='minor', bottom=False, left=False)
for i in range(8):
    for j in range(6):
        n = matrix[i, j]
        ax.text(j, i, str(n), ha='center', va='center', fontsize=14,
                color='white' if n >= 20 else '#122532')
cax = fig.add_axes([0.94, 0.22, 0.015, 0.61])
bar = fig.colorbar(im, cax=cax, ticks=[0, 6, 12, 18, 24, 30, 36])
bar.outline.set_visible(False)
bar.ax.tick_params(length=0, labelsize=10)
bar.set_label('Study count', labelpad=10, fontsize=11)
fig.text(0.04, 0.96, 'Figure S1. Evidence settings across AV/CAV congestion-control application families',
         fontsize=15, fontweight='bold', va='top')
fig.text(0.04, 0.12,
         'Cells report numbers of retained studies coded to each application–evidence-setting combination.\n'
         'Application and evidence-setting fields are multi-label, so counts are non-exclusive and should not be\n'
         'summed as independent study totals.', fontsize=11, linespacing=1.5, va='top')
fig.savefig(out / 'Figure_S1.svg', facecolor='white')
fig.savefig(out / 'Figure_S1.png', dpi=400, facecolor='white')
plt.close(fig)
(out / 'README.md').write_text(
    '# Supplementary Figure S1\n\n' + CAPTION + '\n\n'
    'Place Figure S1 in the supplementary material, with the figure and derived CSVs in the review repository. '
    'It is not an additional main-text figure.\n\n'
    'Source: ' + SOURCE_URL + '\n\n'
    'The eight application labels and six evidence-setting labels are matched exactly after splitting '
    'the existing fields on semicolons and trimming whitespace. Each study is counted once per cell. '
    'Eighty of 96 records have at least one listed application. Five records have no label matching '
    'the six controlled evidence settings; their original values are recorded in source_provenance.json. '
    'A zero is a zero coded combination, not a statement that no evidence exists outside this corpus. '
    'No facility bins, role changes, or quality/maturity scores are introduced.\n\n'
    'Figure_S1_matrix.csv contains the plotted counts. Figure_S1_cell_membership.csv lists contributing '
    'corpus IDs for each cell. corpus_profile_counts.csv contains the marginal counts used in Section 2. '
    'source_provenance.json identifies the downloaded source by SHA-256.\n\n'
    'Reproduce with Python, numpy, and matplotlib: `python build_figure_s1.py /path/to/retained_corpus.csv`.\n',
    encoding='utf-8')
print(json.dumps({'records': len(records), 'matrix': matrix.tolist(), 'output_directory': str(out)}))
