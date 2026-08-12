# Blaque Baux APAC

**Asia-Pacific.**

APAC is a member of the Blaque Baux family. The [core repo](https://github.com/Carter-Warrens/blaquebaux)
is the **engine and blueprint** — a governed, systematic platform (Julia) with a venue-agnostic
execution controller and a Layer-3 live-money safety gate. APAC points that engine in its own
direction and inherits the governance wholesale.

> **Not investment advice.** Educational/research software. Nothing here is validated. See [LICENSE](LICENSE).

```bash
git clone --recursive https://github.com/Carter-Warrens/blaquebaux-apac.git
julia --project=engine -e 'using Pkg; Pkg.instantiate()'   # one-time engine setup
```

## The thesis

Regional exposure (EWJ, EWY, EWT, FXI/ASHR, EWA, INDA and peers). The base's Blunt #3 already found the Asia-to-US 'cascade' is priced instantly (no next-day edge), so APAC's edge, if any, is regional rotation and trend, not lead-lag into the US.

## Research — first pass done

Full detail in [`research/README.md`](research/README.md). The scorecard:

| # | Question | Verdict |
|---|----------|---------|
| 1 | Distinct exposure or US beta? | ❌ US beta — 12 ETFs → **2.5 bets**, corr-SPY 0.79; +0.52/+8%/−39% vs SPY +0.88/+15%/−34% |
| 1 | What does the unhedged FX cost? | 🔴 huge — Japan EWJ +138% vs hedged DXJ **+367%** = **−229% FX drag** |
| 2 | Does country rotation add alpha? | ⚠️ APAC alone has a pulse — long-short country momentum **+0.30** (EMEA −0.23, LATAM −0.04) |
| 2 | Does anything beat SPY? | ❌ no — pooled long +0.59, cross-region rotate +0.60, all < SPY +0.88 |

**The synthesis:** APAC is US beta wearing a flag (12 ETFs → **2.5 bets**, underperforms SPY), and it
carries the family's most brutal FX drag — currency-hedged Japan (DXJ +367%) *tripled* unhedged Japan
(EWJ +138%), a **−229%** currency tax as the yen collapsed. But APAC is also the **one** region with a
real cross-country dispersion pulse: long-short country relative strength earns **+0.30** (Japan /
Taiwan / Korea / India genuinely diverge), where EMEA and LATAM have none. Not a standalone sleeve, but
the family's best candidate for a **currency-hedged, cross-country relative-strength input** — with two
firm rules: hedge the FX, and trade it as relative strength, not directional beta.

## Status
**Research: first pass complete — a qualified null (US beta + severe FX drag; the one region with a
rotation pulse); standalone driver built** (`research/` + `live/`). `live/apac_live.jl` runs the one
viable expression standalone through the engine's order path + Layer-3 safety gate: long top-third /
short bottom-third of the APAC country ETFs by 126-day momentum (dollar-neutral cross-country relative
strength — RS, not beta). **Dry-run by default**; graduates to paper with its own isolated keys. Best
as a rotation input, not a standalone return sleeve; not validated to the spine's bar.
```bash
BB_DRYRUN=1 julia --project=engine live/apac_live.jl
```

## About Blaque Baux

**Blaque Baux** is a quantitative research initiative and a subsidiary of **[Carter Warrens](https://carterwarrens.com)**.
[**BlaqueBaux.com**](https://blaquebaux.com) is the home for the work; the code lives here on GitHub — open to
study, test, and build bespoke strategies on top of.

Anyone can point an AI at a market. The edge is **understanding what the data actually says — and turning it
into something you can act on.** We test relentlessly and put most of it *on the record as rejected, with the
reason*; what survives is built, governed, and validated before it is ever called real. That combination —
honest research, reproducible evidence, and execution you can trust — is why Carter Warrens leads on
**strategy and implementation**, not merely uses the tools everyone now has.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/Carter-Warrens/blaquebaux) is the
base/blueprint and holds the [full family roster](https://github.com/Carter-Warrens/blaquebaux#the-blaque-baux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule -> Carter-Warrens/blaquebaux)
research/   two Path-A sketches (regional beta + FX drag, country/region rotation) + scorecard
live/       governed live drivers (once a sleeve graduates to paper A/B)
```

## License
[MIT](LICENSE). (c) 2026 Carter Warrens.
