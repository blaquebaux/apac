#!/usr/bin/env julia
# ============================================================================
# apac_live.jl — BLAQUE BAUX APAC live driver (cross-country relative strength).
#
# Runs on the engine (engine/ submodule) — same governed order path + Layer-3 safety gate as the spine.
# SIGNAL (research keeper, qualified): directional APAC exposure is US beta + a severe FX drag, so the
# ONLY viable expression is RELATIVE STRENGTH, not beta — long the top-third / short the bottom-third of
# the APAC country ETFs by trailing 126-day momentum (dollar-neutral). Genuine country dispersion (Japan/
# Taiwan/Korea/India diverge) earns +0.30 as a long-short; the cross-country long/short is also roughly
# neutral to the common USD factor. Held at ~1x gross.
#
# CAVEATS (honest): the country ETFs are USD-priced (unhedged FX — the -229% Japan drag is the warning),
# so this is a RELATIVE-strength trade, not a currency-hedged one; and it is still below SPY on absolute
# risk-adjusted return. Best used as a rotation INPUT to a global book, not a standalone return sleeve.
#
# MODES: dry-run by default via the wrapper (BB_DRYRUN=1). Real money needs BB_LIVE_CONFIRM. Kill
# switch: ~/.config/blaquebaux/HALT.  Run: julia --project=engine live/apac_live.jl.  Not validated to the spine's bar.
# ============================================================================
using Dates, Printf, Statistics

const REPO   = normpath(joinpath(@__DIR__, ".."))
const ENGINE = joinpath(REPO, "engine")
for m in ("module_7_execution/module_7_execution.jl","module_10_feedback/module_10_feedback.jl",
          "module_13_portfolio/module_13_portfolio.jl","module_1_data/equity_panel.jl",
          "module_1_data/alpaca_panel.jl","module_8_governance/safety_gate.jl")
    include(joinpath(ENGINE, "src", m))
end
using .ExecutionLayer, .FeedbackLayer, .PortfolioOptModule, .EquityPanel, .AlpacaPanel, .SafetyGate
include(joinpath(ENGINE, "scripts/live_execution.jl"))
include(joinpath(@__DIR__, "_sleeve_main.jl"))

const APAC = ["EWJ","EWY","EWT","MCHI","EWA","EWH","EWS","INDA","EIDO","THD","EWM","EPHE"]
const UNIVERSE = APAC
const LIVE_SENTINEL = "I_UNDERSTAND_THIS_IS_REAL_MONEY"
const LOOK = 126

function apac_target(panel, cap)
    syms = panel.symbols; R = panel.returns; T = size(R, 1); N = length(APAC)
    col(s) = R[:, findfirst(==(s), syms)]; px(s) = panel.prices[findfirst(==(s), syms)]
    mom = [prod(1 .+ col(s)[T-LOOK+1:T]) - 1 for s in APAC]
    o = sortperm(mom); nt = max(1, round(Int, N / 3)); w = zeros(N)
    for j in o[end-nt+1:end]; w[j] = 1.0/nt; end          # long the top-third by momentum
    for j in o[1:nt]; w[j] = -1.0/nt; end                 # short the bottom-third
    w ./= max(sum(abs, w), 1e-9); net = Dict(APAC[i] => w[i] for i in 1:N)  # gross 1 (dollar-neutral)
    price = Dict(s => px(s) for s in APAC)
    (targets = Dict(s => round(Float64, net[s] * cap / price[s]) for s in APAC), prices = price, net = net)
end

if abspath(PROGRAM_FILE) == @__FILE__
    sleeve_main(apac_target; label = "apac", signal_id = "apac", regime = "cross-country-rs",
        lookback = 200, LIVE_SENTINEL = LIVE_SENTINEL, UNIVERSE = UNIVERSE, REPO = REPO)
end
