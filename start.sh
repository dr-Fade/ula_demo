!#/bin/bash

source venv/bin/activate

python -m ipykernel install --user --name="ula_demo" --display-name="ULA demo"

jupyter lab
