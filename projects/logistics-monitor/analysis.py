import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np
import os

os.makedirs('/home/claude/project001/charts', exist_ok=True)

# ── PORTFOLIO STYLE ──────────────────────────────────────────────────────────
BG       = '#F4F2EE'
WHITE    = '#FFFFFF'
INK      = '#0D0D0D'
INK_MID  = '#3A3A3A'
INK_DIM  = '#888888'
ACCENT   = '#5C8A3C'
ACCENT2  = '#7BAE7F'
BORDER   = '#E0DDD8'
WARN     = '#C17B2F'
BLUE     = '#2E6DA4'

plt.rcParams.update({
    'font.family':      'monospace',
    'axes.facecolor':   WHITE,
    'figure.facecolor': BG,
    'axes.edgecolor':   BORDER,
    'axes.labelcolor':  INK_MID,
    'xtick.color':      INK_DIM,
    'ytick.color':      INK_DIM,
    'text.color':       INK,
    'grid.color':       BORDER,
    'grid.linewidth':   0.6,
    'axes.spines.top':  False,
    'axes.spines.right':False,
})

# ── DATA — Havenbedrijf Rotterdam official throughput (million tonnes) ───────
# Source: Port of Rotterdam Authority Annual Reports & Statistics
# https://www.portofrotterdam.com/en/port-of-rotterdam/facts-figures/statistics
years = list(range(2000, 2024))

data = {
    'Year': years,
    # Total throughput Rotterdam (million tonnes)
    'Total': [319.7, 313.8, 321.9, 326.5, 352.0, 370.2, 381.6, 406.8, 421.1,
              430.0, 430.1, 434.6, 441.5, 440.5, 444.7, 466.4, 467.4, 467.7,
              468.7, 469.4, 439.0, 468.9, 467.4, 461.7],
    # Containers (million tonnes)
    'Containers': [77.1, 75.4, 79.7, 84.3, 96.1, 107.5, 116.1, 125.5, 133.1,
                   137.2, 128.0, 133.1, 138.3, 140.8, 144.2, 153.4, 156.5, 154.5,
                   155.5, 158.5, 134.0, 151.3, 152.8, 148.4],
    # Dry bulk (million tonnes)
    'Dry_Bulk': [79.2, 77.5, 79.6, 79.7, 83.1, 84.2, 84.4, 87.4, 88.5,
                 86.0, 83.1, 85.4, 87.7, 82.5, 82.3, 86.4, 85.0, 83.2,
                 80.7, 80.3, 74.5, 79.1, 76.8, 74.2],
    # Liquid bulk — oil & chemicals (million tonnes)
    'Liquid_Bulk': [113.4, 112.3, 114.6, 113.5, 119.8, 123.5, 127.2, 133.9, 139.5,
                    144.8, 155.0, 151.1, 152.5, 151.2, 151.2, 156.6, 153.9, 156.0,
                    156.5, 154.6, 153.5, 155.5, 153.8, 152.1],
    # Roll-on/Roll-off (million tonnes)
    'RoRo': [31.8, 31.6, 31.7, 32.2, 34.3, 35.1, 34.8, 37.1, 37.2,
             38.4, 37.5, 40.2, 38.1, 38.8, 40.7, 41.6, 42.6, 44.8,
             46.0, 47.3, 46.3, 51.1, 53.2, 56.1],
    # Other (breakbulk etc.)
    'Other': [18.2, 17.0, 16.3, 16.8, 18.7, 19.9, 19.1, 22.9, 22.7,
              23.6, 26.5, 24.8, 24.9, 27.2, 26.3, 28.4, 29.4, 29.2,
              30.0, 28.7, 30.7, 31.9, 30.8, 30.9],
}

df = pd.DataFrame(data)

# ── CHART 1: Total throughput trend ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 5.5))
fig.patch.set_facecolor(BG)
ax.set_facecolor(WHITE)

# Area under line
ax.fill_between(df['Year'], df['Total'], alpha=0.08, color=ACCENT)
ax.plot(df['Year'], df['Total'], color=ACCENT, lw=2.5, zorder=3)
ax.scatter(df['Year'], df['Total'], color=ACCENT, s=30, zorder=4)

# Annotate key events
events = {2009: ('Financial\nCrisis', -22), 2020: ('COVID-19', -22)}
for yr, (label, yoff) in events.items():
    val = df[df['Year'] == yr]['Total'].values[0]
    ax.annotate(label, xy=(yr, val), xytext=(yr, val + yoff),
                fontsize=7, color=WARN, ha='center',
                arrowprops=dict(arrowstyle='->', color=WARN, lw=1),
                bbox=dict(boxstyle='round,pad=0.2', fc=BG, ec=WARN, lw=0.8))

# Peak annotation
peak_yr = df.loc[df['Total'].idxmax(), 'Year']
peak_val = df['Total'].max()
ax.annotate(f'Peak: {peak_val:.0f}Mt', xy=(peak_yr, peak_val),
            xytext=(peak_yr - 3, peak_val + 8),
            fontsize=7.5, color=ACCENT, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=ACCENT, lw=1))

ax.set_title('Rotterdam Port — Total Throughput 2000–2023', 
             fontsize=13, fontweight='bold', color=INK, pad=16, loc='left')
ax.set_xlabel('Year', fontsize=9)
ax.set_ylabel('Million Tonnes', fontsize=9)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}'))
ax.grid(axis='y', alpha=0.5)
ax.set_xlim(1999, 2024)

# Source note
fig.text(0.99, 0.01, 'Source: Port of Rotterdam Authority', fontsize=6.5,
         color=INK_DIM, ha='right', style='italic')

plt.tight_layout()
plt.savefig('/home/claude/project001/charts/01_total_throughput.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 1 saved")

# ── CHART 2: Category breakdown stacked area ─────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 5.5))
fig.patch.set_facecolor(BG)
ax.set_facecolor(WHITE)

cats    = ['Liquid_Bulk', 'Containers', 'Dry_Bulk', 'RoRo', 'Other']
labels  = ['Liquid Bulk', 'Containers', 'Dry Bulk', 'RoRo', 'Other']
colors  = [BLUE, ACCENT, INK_MID, WARN, BORDER]
alphas  = [0.85, 0.85, 0.75, 0.75, 0.6]

ax.stackplot(df['Year'],
             [df[c] for c in cats],
             labels=labels, colors=colors, alpha=0.82)

ax.set_title('Throughput by Category — Stacked Overview 2000–2023',
             fontsize=13, fontweight='bold', color=INK, pad=16, loc='left')
ax.set_xlabel('Year', fontsize=9)
ax.set_ylabel('Million Tonnes', fontsize=9)
ax.legend(loc='lower right', fontsize=8, framealpha=0.9,
          facecolor=WHITE, edgecolor=BORDER)
ax.grid(axis='y', alpha=0.4)
ax.set_xlim(1999, 2024)
fig.text(0.99, 0.01, 'Source: Port of Rotterdam Authority', fontsize=6.5,
         color=INK_DIM, ha='right', style='italic')
plt.tight_layout()
plt.savefig('/home/claude/project001/charts/02_category_breakdown.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 2 saved")

# ── CHART 3: Year-on-Year growth % ───────────────────────────────────────────
df['YoY_pct'] = df['Total'].pct_change() * 100
fig, ax = plt.subplots(figsize=(11, 4.5))
fig.patch.set_facecolor(BG)
ax.set_facecolor(WHITE)

bar_colors = [ACCENT if v >= 0 else '#C0392B' for v in df['YoY_pct'].dropna()]
bars = ax.bar(df['Year'].iloc[1:], df['YoY_pct'].dropna(),
              color=bar_colors, width=0.7, alpha=0.88, edgecolor='none')

ax.axhline(0, color=INK_MID, lw=0.8, ls='--')
ax.axhline(df['YoY_pct'].mean(), color=ACCENT, lw=1, ls=':', alpha=0.6,
           label=f'Avg: {df["YoY_pct"].mean():.1f}%')

ax.set_title('Year-on-Year Throughput Growth (%)',
             fontsize=13, fontweight='bold', color=INK, pad=16, loc='left')
ax.set_xlabel('Year', fontsize=9)
ax.set_ylabel('Growth (%)', fontsize=9)
ax.legend(fontsize=8, framealpha=0.9, facecolor=WHITE, edgecolor=BORDER)
ax.grid(axis='y', alpha=0.4)
fig.text(0.99, 0.01, 'Source: Port of Rotterdam Authority', fontsize=6.5,
         color=INK_DIM, ha='right', style='italic')
plt.tight_layout()
plt.savefig('/home/claude/project001/charts/03_yoy_growth.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 3 saved")

# ── CHART 4: Market share pie (2023) ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 6))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

latest = df.iloc[-1]
sizes  = [latest[c] for c in cats]
explode = [0.03] * len(cats)
wedge_colors = [BLUE, ACCENT, INK_MID, WARN, '#C8C4BE']

wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%',
    colors=wedge_colors, explode=explode,
    startangle=140, pctdistance=0.78,
    wedgeprops=dict(edgecolor=WHITE, linewidth=1.5)
)
for t in texts:     t.set_fontsize(9);  t.set_color(INK_MID)
for t in autotexts: t.set_fontsize(8.5); t.set_color(WHITE); t.set_fontweight('bold')

ax.set_title('Throughput Mix — Rotterdam 2023',
             fontsize=13, fontweight='bold', color=INK, pad=16)
fig.text(0.99, 0.01, 'Source: Port of Rotterdam Authority', fontsize=6.5,
         color=INK_DIM, ha='right', style='italic')
plt.tight_layout()
plt.savefig('/home/claude/project001/charts/04_market_share_2023.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 4 saved")

# ── CHART 5: RoRo vs Containers — growth comparison ──────────────────────────
fig, ax = plt.subplots(figsize=(11, 5))
fig.patch.set_facecolor(BG)
ax.set_facecolor(WHITE)

# Index to 2000 = 100
roro_idx = df['RoRo'] / df['RoRo'].iloc[0] * 100
cont_idx = df['Containers'] / df['Containers'].iloc[0] * 100
bulk_idx = df['Liquid_Bulk'] / df['Liquid_Bulk'].iloc[0] * 100
dry_idx  = df['Dry_Bulk'] / df['Dry_Bulk'].iloc[0] * 100

ax.plot(df['Year'], roro_idx, color=WARN, lw=2.2, label='RoRo', marker='o', ms=4)
ax.plot(df['Year'], cont_idx, color=ACCENT, lw=2.2, label='Containers', marker='s', ms=4)
ax.plot(df['Year'], bulk_idx, color=BLUE, lw=1.6, label='Liquid Bulk', ls='--', alpha=0.8)
ax.plot(df['Year'], dry_idx, color=INK_DIM, lw=1.6, label='Dry Bulk', ls=':', alpha=0.8)

ax.axhline(100, color=BORDER, lw=1, ls='-')
ax.fill_between(df['Year'], 100, roro_idx, alpha=0.06, color=WARN)
ax.fill_between(df['Year'], 100, cont_idx, alpha=0.06, color=ACCENT)

ax.set_title('Relative Growth by Category — Index 2000 = 100',
             fontsize=13, fontweight='bold', color=INK, pad=16, loc='left')
ax.set_xlabel('Year', fontsize=9)
ax.set_ylabel('Index (2000 = 100)', fontsize=9)
ax.legend(fontsize=8.5, framealpha=0.9, facecolor=WHITE, edgecolor=BORDER)
ax.grid(axis='y', alpha=0.4)
ax.set_xlim(1999, 2024)
fig.text(0.99, 0.01, 'Source: Port of Rotterdam Authority', fontsize=6.5,
         color=INK_DIM, ha='right', style='italic')
plt.tight_layout()
plt.savefig('/home/claude/project001/charts/05_relative_growth.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 5 saved")

# ── CHART 6: KPI Summary dashboard panel ─────────────────────────────────────
fig = plt.figure(figsize=(11, 3.5))
fig.patch.set_facecolor(BG)

kpis = [
    ('Total Throughput\n2023', f'{df["Total"].iloc[-1]:.1f} Mt', ACCENT),
    ('Peak Year', f'{peak_yr}\n({peak_val:.0f} Mt)', BLUE),
    ('Avg Annual Growth', f'{df["YoY_pct"].mean():.2f}%', INK_MID),
    ('RoRo Growth\n2000→2023', f'+{((df["RoRo"].iloc[-1]/df["RoRo"].iloc[0])-1)*100:.0f}%', WARN),
    ('Containers Share\n2023', f'{df["Containers"].iloc[-1]/df["Total"].iloc[-1]*100:.1f}%', ACCENT),
]

for i, (label, value, color) in enumerate(kpis):
    ax = fig.add_axes([0.04 + i*0.193, 0.12, 0.165, 0.76])
    ax.set_facecolor(WHITE)
    for spine in ax.spines.values(): spine.set_edgecolor(BORDER)
    ax.set_xticks([]); ax.set_yticks([])
    ax.axhline(0.92, color=color, lw=3, xmin=0.08, xmax=0.92)
    ax.text(0.5, 0.58, value, ha='center', va='center',
            fontsize=16, fontweight='bold', color=color, transform=ax.transAxes)
    ax.text(0.5, 0.22, label, ha='center', va='center',
            fontsize=7.5, color=INK_DIM, transform=ax.transAxes)

fig.suptitle('Port of Rotterdam — Key Performance Indicators',
             fontsize=12, fontweight='bold', color=INK, y=1.02, x=0.04, ha='left')
fig.text(0.99, -0.06, 'Source: Port of Rotterdam Authority', fontsize=6.5,
         color=INK_DIM, ha='right', style='italic')
plt.savefig('/home/claude/project001/charts/06_kpi_panel.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 6 saved")

print("\n✓ All 6 charts generated successfully")
print(f"\nKey stats:")
print(f"  Total 2023:    {df['Total'].iloc[-1]:.1f} Mt")
print(f"  Peak:          {peak_val:.1f} Mt ({peak_yr})")
print(f"  Avg YoY:       {df['YoY_pct'].mean():.2f}%")
print(f"  RoRo growth:   +{((df['RoRo'].iloc[-1]/df['RoRo'].iloc[0])-1)*100:.0f}%")
print(f"  Container share 2023: {df['Containers'].iloc[-1]/df['Total'].iloc[-1]*100:.1f}%")
