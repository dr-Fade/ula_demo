#!/bin/bash

if ! command -v julia &>/dev/null; then
    echo "Please install Julia: https://julialang.org/downloads/"
    return 1
fi

julia -e 'using Pkg; Pkg.add("Pluto"); using Pluto; Pluto.run(notebook="ula_demo.jl")'
