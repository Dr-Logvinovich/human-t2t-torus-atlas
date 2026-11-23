# Complete Zero-RNG Toric Disk Atlas of the Human T2T-CHM13v2.0 Genome

**Deterministic, Zero-Random-Number-Generator (Zero-RNG) Whole-Chromosome Structural Audit Across All 24 Human T2T-CHM13v2.0 Chromosomes (`3.117 Gb`, `NC_060925.1`–`NC_060948.1`)**

* **Authors:** Victor Logvinovich ([ORCID 0009-0007-2040-6955](https://orcid.org)) & Jean-Claude Perez ([ORCID 0000-0001-6446-2042](https://orcid.org))
* **Manuscript (PDF):** [`human_t2t_atlas.pdf`](human_t2t_atlas.pdf) (LaTeX source: [`human_t2t_atlas.tex`](human_t2t_atlas.tex))
* **Computational Engine:** [`human_t2t_atlas.py`](human_t2t_atlas.py) (`v1.5.3`, MIT License)
* **Companion Series (Papers 1–3):** [Dr-Logvinovich/codon-torus-syntax](https://github.com)

---

## Overview & Key Discoveries

Treating each complete telomere-to-telomere human chromosome (`GCF_009914755.1`) as a continuous physical medium on the discrete codon torus $\mathbb{T}_4^3 = (\mathbb{Z}/4\mathbb{Z})^3$, this engine computes exact closed-form algebraic observables on the $64\times 64$ triplet-pair transition tensor $B^{(d)}$ across all 24 RefSeq sequences **without Monte Carlo simulations, random seeds, or external genome annotations**.

| # | Discovery | Key Metric | Core Result |
|---|---|---|---|
| **1** | **Euchromatin PR2 Lock** | `99.9995%` (`2.08e5 : 1`) | Data-driven KI-BIC satellite stripping collapses chiral flow $\|W_{--}\|^2_{\mathrm{unb}}$ by $2.26\times 10^5$-fold below the $1/(4N)$ pooling floor (`0.66x`). |
| **2** | **Inter-Chr Coherence** | $\kappa_{\mathrm{euch}}(-+) = 95.82\%$ | All 24 chromosomes align along a single 1024-D directional arrow, while chiral PR2 defects cancel $94.4\times$ ($\kappa = 1.06\%$). |
| **3** | **1D Arrow Manifold** | `PC1 = 87.97%`, `PR = 1.29` | Autosomal 1024-D euchromatic arrows collapse onto a 1D GC/Alu manifold; `chrY` is the sole orthogonal PC2 excursion. |
| **4** | **Palindromic Escape** | $32 \oplus 0 \oplus 32 \oplus 0$; $\ge 9/16$ | Spaced palindromes $(u, \rho(u))$ lock algebraically into $W_{-+}$ with $87.89\%$ single-mode and $\ge 56.25\%$ universal 3600-D non-envelope escape. |
| **5** | **$1/d$ Decay & Alu Dipole** | $\|W_{-+}\|^2 \propto d^{-0.998}$ | Stripping $\bmod\,5$ HSat2/3 `(GGAAT)n` aliasing exposes scale-free $1/d$ decay ($R^2 = 0.940$) and condenses $d = 171\text{ bp}$ onto the canonical Alu `CTCTACT -> AAA` dipole (`25.36%`). |
| **6** | **Anti-Gradient Lock** | $\rho = -0.9821$ ($p = 1.9\text{e-}17$) | Strongest arrows (`chr19`, `chr17`, `chr22`) exhibit the lowest D15 compositional-current alignment ($\cos = 0.02\text{--}0.09$) and `100%` residual energy. |
| **7** | **Karyotype Regimes** | `5/5` vs. `0/17`; `24/24` chr | Zero-overlap $10.4\text{ nt}$ / $154^\circ\text{--}161^\circ$ WW–SS antiphase switch at $\mathrm{WW} < 31\%$; strict $24/24$ Hurst ordering $H(\mathrm{GC}) > H(I_{\mathrm{nonbr}}^{\mathrm{MM}}) > H(\Omega_{\mathrm{cond}})$. |

---

## Visual Highlights

### Alignment-Free $24 \times 24$ Directed Toric Distance (Before vs. After Satellite Stripping)
![Similarity Heatmaps](results_human_t2t_atlas_v1_5_3/figures/fig3_human24_similarity_heatmaps.png)

### Unbiased Toric Karyotype Ideogram Across All 24 Chromosomes
![Karyotype Ideogram](results_human_t2t_atlas_v1_5_3/figures/fig2_human24_karyotype_ideogram.png)

---

## Quick Start & Reproducibility

### 1. Run the Automated Zero-RNG Algebraic Self-Test Gate (23 Checks)
```bash
python3 human_t2t_atlas.py --self-test
```

### 2. Re-Audit & Regenerate All Figures from Archived JSON Results (No FASTA Download Needed)
```bash
python3 human_t2t_atlas.py --replot-only results_human_t2t_atlas_v1_5_3/human_t2t_atlas_v1.json --out-dir results_human_t2t_atlas_v1_5_3
```

### 3. Full From-Scratch 24-Chromosome RefSeq Run (Auto-Downloads `NC_060925.1`–`NC_060948.1`)
```bash
python3 human_t2t_atlas.py --all-24 --auto-download --resume --chr-dir chr_cache --out-dir results_human_t2t_atlas_v1_5_3
```

---

## Repository Structure

* `human_t2t_atlas.py` — Standalone Zero-RNG mathematical engine implementing Theorems D1–D19.
* `human_t2t_atlas.pdf` & `human_t2t_atlas.tex` — Complete research paper and LaTeX source.
* `results_human_t2t_atlas_v1_5_3/human_t2t_atlas_v1.md` — Full human-readable 24-chromosome audit tables.
* `results_human_t2t_atlas_v1_5_3/human_t2t_atlas_v1.json` — Machine-readable audit payload (`39.6 MB`) & startup self-test verification matrix.
* `results_human_t2t_atlas_v1_5_3/figures/` — High-resolution publication figures (`fig1`–`fig6`) and all 24 individual chromosome hard-drive maps (`diskmaps/`).
