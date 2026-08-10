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

## Research plan (Path A — not yet built)

- Regional trend / rotation across APAC country ETFs.
- Semis linkage — Taiwan/Korea vs the global chip cycle (cf. Blunt #3, the correlation study).
- Cross-region rotation with EMEA and LATAM.

Nothing above is implemented or validated. This is the map, not the territory.

## Status
**Scaffold.** Engine wired as a submodule; strategy research not yet conducted.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/Carter-Warrens/blaquebaux) is the
base/blueprint and holds the [full family roster](https://github.com/Carter-Warrens/blaquebaux#the-blaque-baux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule -> Carter-Warrens/blaquebaux)
research/   Path-A strategy sketches (to come)
live/       governed live drivers (once a sleeve graduates to paper A/B)
```

## License
[MIT](LICENSE). (c) 2026 Carter Warrens.
