# A Complete Zero-RNG Toric Disk Atlas of the Human T2T-CHM13v2.0 Genome

[![Zero-RNG](https://img.shields.io/badge/Methodology-100%25%20Zero--RNG-1f77b4.svg)](#quick-start--reproducibility)
[![Assembly](https://img.shields.io/badge/Assembly-T2T--CHM13v2.0%20(3.117%20Gb)-2ca02c.svg)](#overview--key-discoveries)
[![Engine](https://img.shields.io/badge/Engine-v1.5.3%20(47%20Self--Tests%20Passed)-blueviolet.svg)](#quick-start--reproducibility)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#license--provenance)
[![Series](https://img.shields.io/badge/Codon%20Torus%20Series-Paper%204-crimson.svg)](#companion-series-papers-14)
<!-- Uncomment after minting your Zenodo DOI:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
-->

**Deterministic, Zero-Random-Number-Generator (Zero-RNG) Whole-Chromosome Structural Audit Across All 24 Human T2T-CHM13v2.0 Chromosomes (`GCF_009914755.1` · `NC_060925.1`–`NC_060948.1` · `3,117,275,501 bp`)**

- **Authors:**
  - **Victor Logvinovich** — Master of Physical and Mathematical Sciences, Researcher in Pedagogical Sciences (Mathematics), Kobrin, Belarus · [ORCID 0009-0007-2040-6955](https://orcid.org/0009-0007-2040-6955) · `lomakez@icloud.com`
  - **Jean-Claude Perez** — PhD in Mathematics and Computer Science, Retired IBM AI European Research Centre (Montpellier); Luc Montagnier Foundation · [ORCID 0000-0001-6446-2042](https://orcid.org/0000-0001-6446-2042) · `jeanclaudeperez2@gmail.com`
- **Preprint Manuscript (19 pp.):** [`human_t2t_atlas.pdf`](human_t2t_atlas.pdf) · LaTeX source: [`human_t2t_atlas.tex`](human_t2t_atlas.tex)
- **Autonomous Engine:** [`human_t2t_atlas.py`](human_t2t_atlas.py) (`v1.5.3`, MIT License, `script_sha256=06d2b4278dd8ff53...`)
- **Full Audit Tables (Markdown):** [`results_human_t2t_atlas_v1_5_3/human_t2t_atlas_v1.md`](results_human_t2t_atlas_v1_5_3/human_t2t_atlas_v1.md)
- **Companion Series (Papers 1–3):** [`Dr-Logvinovich/codon-torus-syntax`](https://github.com/Dr-Logvinovich/codon-torus-syntax)

---

## Overview & Key Discoveries

Treating each complete telomere-to-telomere human chromosome as a continuous physical medium ("toric disk") on the discrete codon torus $\mathbb{T}_4^3 = (\mathbb{Z}/4\mathbb{Z})^3$, `human_t2t_atlas.py` computes exact closed-form algebraic observables on the $64 \times 64$ triplet-pair transition tensor $B^{(d)}$ across all 24 RefSeq chromosomes **without Monte Carlo simulations, random seeds, or external RepeatMasker / gene annotations**.

| # | Discovery | Key Metric | Core Result |
|---:|---|---|---|
| **1** | **Euchromatin PR2 Lock** | `99.9995%` (`2.08e5 : 1`) | Data-driven KI-BIC satellite stripping (`0.0%` clipping on `24/24` chr) collapses chiral flow $\Vert W_{--}\Vert^2_{\mathrm{unb}}$ by $2.26 \times 10^5$-fold below the $1/(4N)$ pooling floor (`0.66x`); $D_{5'\text{-lead}} = D_{3'\text{-wobble}} = 0.00804587\text{ nats}$ to 7 significant digits. |
| **2** | **Inter-Chr Coherence** | $\kappa_{\mathrm{euch}}(-+) = 95.82\%$ | All 24 chromosomes align along one universal 1024-D directional arrow, whereas whole-genome chiral PR2 defects cancel $94.4\times$ ($\kappa_{\mathrm{whole}}(--) = 1.06\%$; satellites $35.2\times$). |
| **3** | **1D Arrow Manifold** | `PC1 = 87.97%`, `PR = 1.29` | Autosomal 1024-D euchromatic arrows collapse onto a 1D GC/Alu manifold ($r = +0.9681$ vs. GC%, $p = 2.74 \times 10^{-9}$); `chrY` is the sole orthogonal PC2 excursion (`+0.2705`). |
| **4** | **Palindromic Escape** | $32 \oplus 0 \oplus 32 \oplus 0$; $\ge 9/16$ | Spaced palindromes $(u, \rho(u))$ lock algebraically into $W_{-+}$ with $(15/16)^2 = 87.89\%$ single-mode escape, $\ge 56.25\%$ universal escape, an 18-D dark kernel, and $66.3\times$ concentration at $d = 6\text{ bp}$ (`CCA-TGG`, `6.47%`). |
| **5** | **$1/d$ Decay & Alu Dipole** | $\Vert W_{-+}\Vert^2 \propto d^{-0.998}$ | Stripping $\bmod\,5$ HSat2/3 `(GGAAT)n` aliasing exposes scale-free $1/d$ decay ($R^2 = 0.940$, bridge $\Vert W_{-+}\Vert^2 \propto (I_{\mathrm{nonbr}}^{\mathrm{MM}})^{1.54}$, $R^2 = 0.985$) and condenses $d = 171\text{ bp}$ onto the canonical Alu `CTCTACT -> AAA` dipole (`25.36%`). |
| **6** | **Anti-Gradient Lock** | $\rho = -0.9821$ ($p = 1.9 \times 10^{-17}$) | All `24/24` chromosomes pass 1-Mb LOO Newey–West HAC ($t_{\mathrm{HAC}} \in [19.56, 112.73]$) and retain `100.00%` residual against $E_{\mathrm{loc}}$ ($M = 1000\text{ bp}$); strongest arrows (`chr19/17/22`) have the lowest drift alignment ($\cos = 0.02\text{--}0.09$). |
| **7** | **Karyotype Regimes** | `5/5` vs. `0/17`; `24/24` chr | Zero-overlap $10.4\text{ nt}$ / $154^\circ\text{--}161^\circ$ WW–SS antiphase switch at $\mathrm{WW} < 31\%$ ($p = 9.97 \times 10^{-4}$); strict `24/24` Hurst hierarchy $H(\mathrm{GC})\,0.928 > H(I_{\mathrm{nonbr}}^{\mathrm{MM}})\,0.831 > H(\Omega_{\mathrm{cond}})\,0.543$; sex-chr retention $\eta_{90/3}$ ranks 23–24/24. |

---

## Grand-Pooled 3.117-Gb Audit Summary ($d = 3\text{ bp}$)

| Partition | Triplet Pairs $N$ | $\Vert W_{++}\Vert^2$ | $\Vert W_{+-}\Vert^2$ | $\Vert W_{-+}\Vert^2_{\mathrm{unb}}$ | $\Vert W_{--}\Vert^2_{\mathrm{unb}}$ | PR2-ok (unb) | Non-Env 3600-D | CpG-Free | $I_{\mathrm{nonbr}}^{\mathrm{MM}}$ | 6-bp Pal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Whole Human Genome** | `3,117,275,381` | `3.99e-4` | `1.62e-7` | `1.65e-5` | `1.26e-7` | `99.24%` | `51.9%` | `89.6%` | `0.03153` | `1.544%` |
| **Euchromatin (KI-BIC)** | `2,812,997,330` | `3.98e-4` | `1.34e-9` | `1.22e-5` | `5.86e-11` | `99.9995%` | `37.0%` | `86.4%` | `0.02292` | `1.541%` |
| **Satellite / Tandem (KI-BIC)** | `303,097,395` | `9.88e-4` | `1.69e-5` | `6.02e-4` | `1.32e-5` | `97.85%` | `80.9%` | `96.5%` | `0.28328` | `1.575%` |

---

## Visual Highlights (All 6 Whole-Genome Figures)

### Fig. 1 — 24-Chromosome Executive Overview (PR2 Share, Screen Memory, 171-bp Resonance & WLS Hurst)
![Executive Overview](results_human_t2t_atlas_v1_5_3/figures/fig1_human24_overview.png)

### Fig. 2 — Unbiased Toric Karyotype Ideogram Across All 24 Chromosomes (`SNR >= 3` Masked)
![Karyotype Ideogram](results_human_t2t_atlas_v1_5_3/figures/fig2_human24_karyotype_ideogram.png)

### Fig. 3 — Alignment-Free $24 \times 24$ Directed Toric Distance (Full Disk vs. Satellite-Stripped Euchromatin)
![Similarity Heatmaps](results_human_t2t_atlas_v1_5_3/figures/fig3_human24_similarity_heatmaps.png)

### Fig. 6 — Multi-Lag Decay (Whole vs. Pure Euchromatin $\bmod\,5$ Aliasing), WW–SS Antiphase & Jackknife Hurst
![Multi-Lag WW Hurst](results_human_t2t_atlas_v1_5_3/figures/fig6_human24_D12_multilag_ww_hurst.png)

<details>
<summary><b>Click to expand Fig. 4 (Theorem D10 8-Strata Entropy Phase Diagram) & Fig. 5 (Theorem D11/D13 CpG-Free Top-15 Orbits)</b></summary>

#### Fig. 4 — Theorem D10: 8-Strata Entropy Phase Transition (`H = 5.65 bits`)
![Entropy Phase Diagram](results_human_t2t_atlas_v1_5_3/figures/fig4_human24_D10_entropy_phase_diagram.png)

#### Fig. 5 — Theorems D11 & D13: Non-Envelope 3600-D Syntax & Top-15 Strictly CpG-Free Directed 6-mer Orbits
![Arrow Anatomy Motifs](results_human_t2t_atlas_v1_5_3/figures/fig5_human24_D11_arrow_anatomy_motifs.png)

</details>

---

## 5-Track Per-Chromosome Toric Disk Maps (`chr1`–`chr22`, `chrX`, `chrY`)

Each chromosome is scanned at `100-kb` resolution across five independent physical tracks: (1) full-disk strand polarity walks, (1B) satellite-stripped euchromatin-only unit-SVD walks, (2) directed within-sector syntax ($W_{-+}$, $W_{--}$) & 3-mer entropy $H_3$, (3) blind 3-bp frame-phase lock $\Omega_{\mathrm{cond}}$, and (4) non-bridge $16 \times 16$ screen memory vs. GC isochores.

### Featured Archetypes: `chrY`, `chrX`, `chr19`, and `chr22`

#### `chrY` (`NC_060948.1`, `62.46 Mb`) — `58.2%` Satellite/Tandem Firmware & Periodic `Yq12` `DYZ1/2` Oscillations
![chrY Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chrY.png)

#### `chrX` (`NC_060947.1`, `154.26 Mb`) — Compact Centromere (`KI-BIC thr=0.130`) & Clean Euchromatic Polarity
![chrX Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chrX.png)

#### `chr19` (`NC_060943.1`, `61.71 Mb`) — Peak GC/Alu Euchromatic Arrow (`57.9%` Pure 3600-D Non-Envelope)
![chr19 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr19.png)

#### `chr22` (`NC_060946.1`, `51.32 Mb`) — Acrocentric rDNA Short Arm (`0–17 Mb`) & Peak PELT Concordance (`Jaccard = 0.77`)
![chr22 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr22.png)

<details>
<summary><b>Click to expand all remaining 20 chromosome 5-track disk maps (<code>chr1</code>–<code>chr18</code>, <code>chr20</code>, <code>chr21</code>)</b></summary>

#### `chr1` (`NC_060925.1`, `248.39 Mb`)
![chr1 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr1.png)

#### `chr2` (`NC_060926.1`, `242.70 Mb`)
![chr2 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr2.png)

#### `chr3` (`NC_060927.1`, `201.11 Mb`)
![chr3 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr3.png)

#### `chr4` (`NC_060928.1`, `193.57 Mb`)
![chr4 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr4.png)

#### `chr5` (`NC_060929.1`, `182.05 Mb`)
![chr5 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr5.png)

#### `chr6` (`NC_060930.1`, `172.13 Mb`)
![chr6 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr6.png)

#### `chr7` (`NC_060931.1`, `160.57 Mb`)
![chr7 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr7.png)

#### `chr8` (`NC_060932.1`, `146.26 Mb`)
![chr8 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr8.png)

#### `chr9` (`NC_060933.1`, `150.62 Mb`) — Balanced Head-to-Head `9q12` HSat3 Chiral Cancellation (`99.96%` PR2-ok)
![chr9 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr9.png)

#### `chr10` (`NC_060934.1`, `134.76 Mb`)
![chr10 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr10.png)

#### `chr11` (`NC_060935.1`, `135.13 Mb`)
![chr11 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr11.png)

#### `chr12` (`NC_060936.1`, `133.32 Mb`)
![chr12 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr12.png)

#### `chr13` (`NC_060937.1`, `113.57 Mb`)
![chr13 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr13.png)

#### `chr14` (`NC_060938.1`, `101.16 Mb`)
![chr14 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr14.png)

#### `chr15` (`NC_060939.1`, `99.75 Mb`)
![chr15 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr15.png)

#### `chr16` (`NC_060940.1`, `96.33 Mb`)
![chr16 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr16.png)

#### `chr17` (`NC_060941.1`, `84.28 Mb`) — Centromeric 3-bp Frame-Lock Burst (`KI-BIC thr=0.853`)
![chr17 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr17.png)

#### `chr18` (`NC_060942.1`, `80.54 Mb`) — Single Compact Centromeric Block (`KI-BIC thr=0.458`)
![chr18 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr18.png)

#### `chr20` (`NC_060944.1`, `66.21 Mb`) — Metacentric Satellite Core (`KI-BIC thr=0.242`)
![chr20 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr20.png)

#### `chr21` (`NC_060945.1`, `45.09 Mb`) — Acrocentric rDNA/Satellite Arm & 3-bp Phase-Lock Plateau (`KI-BIC thr=0.081`)
![chr21 Disk Map](results_human_t2t_atlas_v1_5_3/figures/diskmaps/fig_diskmap_Human_T2T_chr21.png)

</details>

---

## Mathematical Architecture (Theorems D1–D19)

| Module | Exact Mathematical Scope |
|---|---|
| **THM-D1 / D2 / D9** | Exact Klein $V_4 = \{I,T,R,S\}$ orthogonal splitting ($1056 \oplus 1024 \oplus 1024 \oplus 992$), exact heterogeneity annihilation $W_{-+}(E_{\mathrm{het}}) = W_{--}(E_{\mathrm{het}}) = 0$, and minimum-variance $U$-statistic debiasing (Theorem 6). |
| **THM-D3 / D11 / D13** | Exact 4-term two-sided $16 \times 16$ screen ($\mathrm{df} = 3969$), minimal $V_4$-closed 496-D screen envelope $\Pi_{\mathrm{env}}$ with 3600-D complement (zero quadrant leakage, `< 5e-16`), and palindromic anti-diagonal locking ($32 \oplus 0 \oplus 32 \oplus 0$, $\ge 9/16$ escape, Theorem 5). |
| **THM-D4 / D5 / D7** | Blind 3-bp frame-lock $\Omega_{\mathrm{phase}}$, intrinsic right-singular-vector SVD polarity walks, and constrained heteroscedastic Kittler–Illingworth BIC on $\log_{10}(I_{\mathrm{nonbr}}^{\mathrm{raw}})$ (`0.0%` clipping on `24/24` chromosomes). |
| **THM-D6 / D12 / D16 / D19** | Zero-padded FFT GC & WW/SS pitch with Hann ENBW-adjusted $F_{2,2M_{\mathrm{eff}}}$ testing, 10-lag euchromatin spectrum ($d = 3\text{--}171\text{ bp}$), and exact $\bmod\,p$ tandem-repeat aliasing proof (Theorem 4). |
| **THM-D8 / D14 / D15 / D17 / D18** | Delete-1 Jackknife WLS Hurst ($100\text{ kb} \to 6.4\text{ Mb}$), 1-Mb LOO Newey–West HAC inference + $1/(4N)$ pooling floor, memory-bounded compositional-current null $E_{\mathrm{loc}}$, FFT circular-shift Lévy area null (`0/24` FP), and LRV-calibrated delayed-pruning PELT $L_2$ segmentation (`0.0` error vs. exact $O(n^2)$ DP across 30 trials). |

---

## Quick Start & Reproducibility

### Requirements
```bash
pip install numpy scipy matplotlib
```
*(Verified on Python `3.12.1`, NumPy `2.3.2`, SciPy `1.16.2`, Matplotlib `3.10.6`; 100% deterministic, zero random seeds.)*

### 1. Run the Automated Zero-RNG Algebraic Self-Test Gate (47 Checks)
```bash
python3 human_t2t_atlas.py --self-test
```

### 2. Re-Audit & Regenerate All Figures from Archived JSON (No FASTA Download Needed)
```bash
python3 human_t2t_atlas.py \
  --replot-only results_human_t2t_atlas_v1_5_3/human_t2t_atlas_v1.json \
  --out-dir results_human_t2t_atlas_v1_5_3
```

### 3. Full From-Scratch 24-Chromosome RefSeq Run (Auto-Downloads `NC_060925.1`–`NC_060948.1`)
```bash
python3 human_t2t_atlas.py \
  --all-24 --auto-download --resume \
  --chr-dir chr_cache \
  --out-dir results_human_t2t_atlas_v1_5_3
```

---

## Repository Structure

```text
human-t2t-torus-atlas/
├── human_t2t_atlas.py                             # Standalone Zero-RNG engine v1.5.3 (Theorems D1–D19)
├── human_t2t_atlas.pdf                            # Complete 19-page audited preprint
├── human_t2t_atlas.tex                            # Full LaTeX source (6 theorems, 2 corollaries, 12 tables)
└── results_human_t2t_atlas_v1_5_3/
    ├── human_t2t_atlas_v1.md                      # Complete 24-chromosome Markdown audit tables
    ├── human_t2t_atlas_v1.json                    # Full machine-readable audit payload & 47 self-test results
    ├── atlas_b3_cache.npz                         # Cached exact 64x64 pair tensors across all 24 chr & 10 lags
    └── figures/
        ├── fig1_human24_overview.png              # 4-panel executive overview
        ├── fig2_human24_karyotype_ideogram.png    # 24-chr unbiased toric ideogram
        ├── fig3_human24_similarity_heatmaps.png   # 24x24 alignment-free cosine distance matrices
        ├── fig4_human24_D10_entropy_phase_diagram.png
        ├── fig5_human24_D11_arrow_anatomy_motifs.png
        ├── fig6_human24_D12_multilag_ww_hurst.png
        └── diskmaps/                              # 24 individual 5-track chromosome hard-drive maps
```

---

## Companion Series (Papers 1–4)

| Paper | Scope | Archive / Repository |
|---|---|---|
| **Papers 1–3** | Double-Stranded Codon Torus, 54-Taxon Biospheric Codon Memory Spectrum, Synthetic Genomes (`JCVI-syn1.0/3.0`) & mRNA Constructs (`BNT162b2`, `mRNA-1273`) | [GitHub `codon-torus-syntax`](https://github.com/Dr-Logvinovich/codon-torus-syntax) · [Zenodo `23287684`](https://doi.org/10.5281/zenodo.23287684) · [`23508080`](https://doi.org/10.5281/zenodo.23508080) · [`23695321`](https://doi.org/10.5281/zenodo.23695321) |
| **Paper 4 (This Repo)** | Complete 24-Chromosome Human T2T-CHM13v2.0 Toric Disk Atlas (`3.117 Gb`, Unannotated Whole-Chromosome Physical Medium) | [GitHub `human-t2t-torus-atlas`](https://github.com/Dr-Logvinovich/human-t2t-torus-atlas) · Complete offline FASTA cache (`chr_cache.zip`) archived on Zenodo |
| **Foundational Prior Work** | J.-C. Perez (2010), *Codon populations in single-stranded whole human genome DNA are fractal and fine-tuned by the Golden Ratio 1.618*, *Interdiscip. Sci.* **2**(3), 228–240 | [`doi:10.1007/s12539-010-0022-0`](https://doi.org/10.1007/s12539-010-0022-0) · PMID: `20658335` |

---

## Assembly Scope Note & Epistemic Firewall

- **Hybrid Reference Scope:** T2T-CHM13v2.0 combines the effectively haploid `46,XX` CHM13 cell line (`chr1`–`chr22`, `chrX`) with T2T-assembled `chrY` from HG002 (`46,XY`); acrocentric rDNA morph arrays include consensus-modeled copies in RefSeq v2.0.
- **Annotation-Blind Partition:** All euchromatin/satellite boundaries are derived purely from intrinsic sequence statistics (`THM-D7 KI-BIC`) without external RepeatMasker, gene, or epigenetic tracks.
- **No Unverified Mechanistic Overclaims:** All conclusions are restricted strictly to exact sequence-level algebraic and statistical invariants verified under Zero-RNG falsification gates (`0/24` HAC failures, `0/24` circular-shift Lévy false positives, `100.00%` D15 current-null residual).

---

## License & Provenance

- **Code & Data License:** MIT License (`human_t2t_atlas.py`, JSON/Markdown outputs, figures).
- **Cryptographic Provenance:** Primary full-genome run `script_sha256 = 06d2b4278dd8ff531e6b2b79ef6d9f1aa281c125270cb52ebb7b2470836adeb5`; individual SHA-256 digests for all 24 RefSeq FASTA files are archived in Table 11 of [`human_t2t_atlas.pdf`](human_t2t_atlas.pdf) and [`human_t2t_atlas_v1.json`](results_human_t2t_atlas_v1_5_3/human_t2t_atlas_v1.json).

### How to Cite

```bibtex
@misc{LogvinovichPerez2026T2TAtlas,
  author       = {Logvinovich, Victor and Perez, Jean-Claude},
  title        = {A Complete Zero-RNG Toric Disk Atlas of the Human T2T-CHM13v2.0 Genome: Klein V4 Irreversibility, Satellite Partitioning, and Multi-Lag Syntax Across All 24 Chromosomes},
  year         = {2026},
  month        = nov,
  version      = {1.5.3},
  publisher    = {Zenodo},
  url          = {https://github.com/Dr-Logvinovich/human-t2t-torus-atlas}
}
```
