from pathlib import Path
import py_compile, shutil

p = Path("human_t2t_atlas.py")
shutil.copy2(p, p.with_suffix(".py.bak_v153"))
src = p.read_text(encoding="utf-8")

PATCHES = [
    (
        "    p_hyp = min(1.0, float(num) / float(denom)) if denom > 0 else 1.0",
        "    p_hyp = min(1.0, num / denom) if denom > 0 else 1.0",
    ),
    (
        '                        ("Euchromatin (THM-D7 Otsu-BIC)", gg["euchromatin_grand"]),\n'
        '                        ("Satellite/Tandem (THM-D7 Otsu-BIC)", gg["satellite_grand"])):',
        '                        ("Euchromatin (THM-D7 KI-BIC)", gg["euchromatin_grand"]),\n'
        '                        ("Satellite/Tandem (THM-D7 KI-BIC)", gg["satellite_grand"])):',
    ),
    (
        '          "| Chr | Otsu I_nonbr* | ΔBIC | Euch % | Sat % | Sat Blocks | Euch ‖W_-+‖² | Sat ‖W_--‖² | Euch K_nonbr^MM (d=3/90) | Sat 171-bp | Euch unitSVD1 W_+- |",',
        '          "| Chr | KI-BIC I_nonbr* | ΔBIC | Euch % | Sat % | Sat Blocks | Euch ‖W_-+‖² | Sat ‖W_--‖² | Euch K_nonbr^MM (d=3/90) | Sat 171-bp | Euch unitSVD1 W_+- |",',
    ),
    (
        '    ax.bar(x + 0.19, p_eu, 0.38, color="#1f77b4", label="Euchromatin Only (THM-D7 Otsu-BIC)")',
        '    ax.bar(x + 0.19, p_eu, 0.38, color="#1f77b4", label="Euchromatin Only (THM-D7 KI-BIC)")',
    ),
    (
        '    ax.set_xlabel("Physical Coordinate (Mb)  |  Magenta brackets = Data-Driven THM-D7 Satellite/Centromere/rDNA Blocks (Bin-Free log10(I_nonbr) Otsu-BIC + Entropy Inversion)", fontsize=10)',
        '    ax.set_xlabel("Physical Coordinate (Mb)  |  Magenta brackets = Data-Driven THM-D7 Satellite/Centromere/rDNA Blocks (Constrained Kittler–Illingworth BIC on log10(I_nonbr_raw))", fontsize=10)',
    ),
    (
        '                                 (axes[1], "dist_directed_euch", "B. Satellite-Stripped Euchromatin Only (THM-D7 Otsu-BIC)")):',
        '                                 (axes[1], "dist_directed_euch", "B. Satellite-Stripped Euchromatin Only (THM-D7 KI-BIC)")):',
    ),
    (
        '    all_h = [v for v in (h_gc + h_lo + h_hi) if _finite(v)]\n'
        '    ylo = min(0.42, min(all_h) - 0.04) if all_h else 0.42\n'
        '    yhi = max(1.06, max(all_h) + 0.04) if all_h else 1.06\n'
        '    ax.set_ylim(ylo, yhi); ax.set_xticks(x); ax.set_xticklabels(lbls, rotation=45, ha="right", fontsize=7.5)\n'
        '    ax.set_ylabel("WLS Hurst Exponent H"); ax.set_title("C. THM-D8/D9: Unified Euchromatin WLS Hurst (±95% Jackknife CI)")\n'
        '    ax.legend(fontsize=7.2, loc="lower right", framealpha=0.92); ax.grid(True, ls=":", alpha=0.35)',
        '    ylo, yhi = 0.22, 1.22\n'
        '    ax.set_ylim(ylo, yhi); ax.set_xticks(x); ax.set_xticklabels(lbls, rotation=45, ha="right", fontsize=7.5)\n'
        '    for xi_, hv_, lo_, hi_, lb_ in zip(x, h_u, h_lo, h_hi, lbls):\n'
        '        if _finite(hv_) and hv_ < ylo:\n'
        '            ax.plot(xi_, ylo + 0.025, marker="v", ms=6.5, color="#d62728", zorder=6)\n'
        '            ax.annotate(f"{lb_}: H={hv_:.2f} [{lo_:.2f},{hi_:.2f}]", xy=(xi_, ylo + 0.025),\n'
        '                        xytext=(max(0.5, xi_ - 10.5), ylo + 0.055), fontsize=6.8, color="#b2182b",\n'
        '                        bbox=dict(boxstyle="round,pad=0.22", fc="white", ec="#d62728", alpha=0.92),\n'
        '                        arrowprops=dict(arrowstyle="->", color="#d62728", lw=0.9))\n'
        '    ax.set_ylabel("WLS Hurst Exponent H"); ax.set_title("C. THM-D8/D9: Unified Euchromatin WLS Hurst (±95% Jackknife CI)")\n'
        '    ax.legend(fontsize=7.0, loc="lower left", bbox_to_anchor=(0.05, 0.02), framealpha=0.92); ax.grid(True, ls=":", alpha=0.35)',
    ),
    (
        '            axe.set_title(f"1B. Satellite-Stripped Euchromatin-Only Toric Walk (THM-D7 Otsu-BIC; r_GCsk={fnum(ew[\'corr_W_pm_vs_gc_skew\'],3,True)})", fontsize=10)',
        '            axe.set_title(f"1B. Satellite-Stripped Euchromatin-Only Toric Walk (THM-D7 KI-BIC; r_GCsk={fnum(ew[\'corr_W_pm_vs_gc_skew\'],3,True)})", fontsize=10)',
    ),
    (
        '        ax = at[2]; _shade(ax)\n'
        '        ax.plot(pos, tr["I_nonbr_MM"], color="#17becf", lw=1.1, label="I_nonbridge^MM (non-bridge screen memory)")\n'
        '        if _finite(d7.get("inb_threshold_otsu")):\n'
        '            ax.axhline(float(d7["inb_threshold_otsu"]), color="crimson", ls=":", lw=1.0, alpha=0.8)',
        '        ax = at[2]; _shade(ax)\n'
        '        use_raw_dm = ("D_5lead" in tr) and ("raw" in str(d7.get("partition_method", "")))\n'
        '        inb_dm = (np.asarray(tr["D_5lead"], dtype=np.float64) + np.asarray(tr["D_3wob"], dtype=np.float64)\n'
        '                  + np.asarray(tr["D_1_3"], dtype=np.float64)) if use_raw_dm else tr["I_nonbr_MM"]\n'
        '        ax.plot(pos, inb_dm, color="#17becf", lw=1.1,\n'
        '                label="I_nonbridge_raw (screen memory)" if use_raw_dm else "I_nonbridge^MM (non-bridge screen memory)")\n'
        '        if _finite(d7.get("inb_threshold_otsu")):\n'
        '            thr_dm = float(d7["inb_threshold_otsu"])\n'
        '            ax.axhline(thr_dm, color="crimson", ls=":", lw=1.1, alpha=0.85, label=f"KI-BIC thr={thr_dm:.3f}")',
    ),
]

for idx, (old, new) in enumerate(PATCHES, 1):
    assert src.count(old) == 1, f"Patch #{idx} anchor count = {src.count(old)}"
    src = src.replace(old, new, 1)

p.write_text(src, encoding="utf-8")
py_compile.compile(str(p), doraise=True)
print(f"OK: applied {len(PATCHES)} patches cleanly.")