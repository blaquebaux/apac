# Blaque Baux APAC — research

First-pass Path-A research on **Asia-Pacific via US-listed country ETFs.** The three regional sleeves
(EMEA / APAC / LATAM) are one research object — regional exposure bought through US wrappers — so they
share this module and its two sketches; this repo frames the joint result from APAC. All sketches read
Alpaca SIP daily bars (2016–2026), are read-only, print results.

APAC universe (12): `EWJ` Japan, `EWY` Korea, `EWT` Taiwan, `MCHI` China, `EWA` Australia, `EWH` Hong Kong, `EWS` Singapore, `INDA` India, `EIDO` Indonesia, `THD` Thailand, `EWM` Malaysia, `EPHE` Philippines.

```bash
export $(grep -v '^#' ~/.config/blaquebaux/alpaca.env | xargs)   # or source it
python research/apac_1_beta_and_fx.py   # is APAC just US beta + FX drag?
python research/apac_2_rotation.py       # does country / region rotation beat buy-and-hold?
```

## Scorecard

| # | Question | Result | Verdict |
|---|----------|--------|---------|
| 1 | Is APAC a distinct exposure or US beta? | 12 ETFs → **2.5 bets**, corr-SPY 0.79, beta 0.78; +0.52/+8%/−39% vs SPY +0.88/+15%/−34% | ❌ US beta, underperforms |
| 1 | What does the unhedged FX cost? | Japan EWJ +138% vs hedged DXJ **+367%** → **−229% FX drag** | 🔴 huge, uncompensated |
| 2 | Does country rotation add alpha? | long-short country momentum **+0.30** (only region with a pulse) | ⚠️ thin but real dispersion |
| 2 | Does anything beat SPY? | pooled long +0.59, cross-region rotate +0.60 — all < SPY +0.88 | ❌ no |

## The synthesis

- **APAC is US beta wearing a flag — but the most internally diverse region.** Twelve country ETFs
  collapse to **2.5 effective bets** (corr-SPY 0.79, beta 0.78 — the *lowest* market beta of the three
  regions), yet the basket still underperforms SPY (+0.52 / +8% / −39% vs +0.88 / +15% / −34%).

- **The FX drag is the family's most brutal.** Over 2016–2026 currency-hedged Japan (DXJ, +367%)
  *tripled* unhedged Japan (EWJ, +138%) — a **−229% FX drag** as the yen collapsed. This is the single
  loudest evidence for the whole regional caveat: bought unhedged through a US ETF, Japanese equities'
  huge local rally was almost entirely handed back in currency. **Hedge the yen or don't own it.**

- **APAC is the one region where country rotation has a pulse.** Long-short relative strength across
  APAC countries earns **+0.30** Sharpe — genuine dispersion (Japan / Taiwan / Korea / India diverge),
  where EMEA (−0.23) and LATAM (−0.04) have none. Long top-third (+0.58) edges EW-hold (+0.52). It is
  thin and still below SPY, but it is the family's best cross-country relative-strength candidate.

**Verdict:** not a standalone sleeve — APAC is concentrated US beta plus a **severe** FX tax. But it is
the **best candidate for a currency-hedged, cross-country relative-strength input** to a global rotation
book: real dispersion exists here, unlike EMEA/LATAM. Two firm rules for any live use: **hedge the FX**
(the −229% Japan drag is the proof) and **trade it as relative strength, not directional beta.**

## Files
- `_apac_common.py` — shared helpers + all three regional universes + benchmarks/FX pairs.
- `apac_1_beta_and_fx.py` — regional beta (all 3 regions vs SPY) + the hedged-vs-unhedged FX drag.
- `apac_2_rotation.py` — within-region country momentum + pooled & cross-region rotation vs SPY.
