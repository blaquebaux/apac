#!/usr/bin/python3
# =============================================================================
# apac_3_dollar_overlay.py — should APAC consume brics' DOLLAR regime?  (Mostly no.)
#
# The honest answer depends on WHICH apac book. apac's LIVE driver is the dollar-NEUTRAL cross-country
# long/short (long top-third momentum, short bottom-third) — by construction ~neutral to the common
# USD factor. So the dollar overlay is the WRONG signal for what apac actually trades, exactly as a
# market-neutral book declines the bonds overlay. We MEASURE that (L/S beta to UUP ~ 0), then, for
# completeness, test the overlay on the DIRECTIONAL apac basket (the rejected book, which IS
# dollar-exposed) so the contrast is explicit. Read-only. (emea/latam are directional -> see their #3.)
# =============================================================================
import os, sys, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _apac_common import load, REGIONS

REGION = "APAC"; MA = 100; LOOK = 126; REB = 21
B = load(); g = REGIONS[REGION]

# ---- (a) the LIVE driver: dollar-neutral cross-country long/short -> measure its UUP exposure ----
idx = [B.i[s] for s in g]; n = len(idx); k = max(1, n // 3); Rl = B.R[:, idx]
wp = np.zeros(n); ls = []; lsidx = []
for t in range(LOOK, B.T - 1):
    if (t - LOOK) % REB == 0:
        tr = B.M[t, idx] / B.M[t - LOOK, idx] - 1; o = np.argsort(tr); w = np.zeros(n)
        w[o[-k:]] = 1.0 / k; w[o[:k]] = -1.0 / k
    else:
        w = wp
    ls.append(float(np.nansum(w * Rl[t + 1]))); lsidx.append(t + 1); wp = w
ls = np.array(ls); uup_al = B.col("UUP")[lsidx]
shL, cgL, ddL = B.met(ls)
print("=" * 80, "\nAPAC — should it consume the dollar regime? (the live L/S book is dollar-neutral)\n" + "=" * 80)
print(f"  LIVE driver (cross-country long/short): Sharpe {shL:+.2f}  corr-to-UUP {B.corr(ls, uup_al):+.2f}  beta-to-UUP {B.beta(ls, uup_al):+.2f}")
print("    -> ~dollar-NEUTRAL by construction; the dollar overlay is the wrong signal for it (declined,")
print("       same reason a market-neutral book declines the bonds overlay).")

# ---- (b) for contrast: the DIRECTIONAL apac basket (rejected) IS dollar-exposed -> test the overlay ----
basket = B.basket(g); uup = B.M[:, B.i["UUP"]]
strong = np.zeros(B.T, bool)
for t in range(MA, B.T): strong[t] = uup[t] > uup[t-MA:t].mean()
overlay = lambda d: np.where(strong, d, 1.0) * basket
sh0, cg0, dd0 = B.met(basket)
print(f"\n  DIRECTIONAL apac basket (the rejected book): corr-to-UUP {B.corr(basket, B.col('UUP')):+.2f}  Sharpe {sh0:+.2f}  maxDD {dd0*100:+.0f}%")
print(f"  {'  overlay':<20}{'Sharpe':>8}{'CAGR':>8}{'maxDD':>8}")
res = []
for d in (0.75, 0.50, 0.0):
    sh, cg, dd = B.met(overlay(d)); res.append((d, sh, dd))
    print(f"  {('  x'+str(d) if d else '  to cash'):<20}{sh:>+8.2f}{cg*100:>+7.0f}%{dd*100:>+7.0f}%")
bd, bsh, bdd = max(res, key=lambda x: x[1]); ddcut = 1 - abs(bdd)/abs(dd0)
print(f"  best: {'x'+str(bd) if bd else 'to cash'} -> Sharpe {sh0:+.2f}->{bsh:+.2f}, maxDD {dd0*100:+.0f}%->{bdd*100:+.0f}% ({ddcut*100:.0f}% cut)")

print("\nVERDICT: apac's LIVE book is the dollar-NEUTRAL long/short, so it correctly DOES NOT consume the")
print("dollar overlay — its UUP beta is ~0; de-risking a neutral book on a dollar signal adds nothing.")
print("Only the DIRECTIONAL apac basket is dollar-exposed, and that book was already rejected (US beta +")
print("FX drag). So the honest answer to 'consume the dollar regime in apac' is: not in the live driver —")
print("match the signal to the sleeve. (apac still PUBLISHES nothing; brics is the dollar-regime source.)")
