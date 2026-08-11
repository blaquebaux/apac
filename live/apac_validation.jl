#!/usr/bin/env julia
# apac_validation.jl — validate-before-live gate for the APAC sleeve (walk-forward / OOS / net-of-cost).
# Reuses apac_target from apac_live.jl. Run:  julia --project=engine live/apac_validation.jl
include(joinpath(@__DIR__, "apac_live.jl"))
include(joinpath(@__DIR__, "_sleeve_validation.jl"))
validate_sleeve(apac_target; label = "APAC", universe = UNIVERSE, warmup = 180, kind = :neutral)
