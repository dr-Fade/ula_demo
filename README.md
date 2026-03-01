# ULA demo

This project contains implementation of a simple 1D ULA and allows the user to interactively adjust signal's direction of arrival, its SNR level, and the baseband signal frequency.

## Python

It is recommended that the Python notebook is ran inside of VSCode because the Jupyter Lab server requires non-trivial configuration to support the interactive widgets properly.

1. Navigate to the `python` directory and open a terminal window.
2. Create a virtual environment and install the dependencies:
```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
3. Open the project in VSCode:
```
$ code .
```
4. Install the Jupyter extension to be able to run the Jupyter notebooks inside VSCode.
5. Open the `ula_demo.ipynb` and run all cells.

Alternatively, you can run the notebook using the Jupyter Lab server:

1. Navigate to the `python` directory and open a terminal window.
2. Create a virtual environment and install the dependencies:
```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
3. Run the `start.sh` script:
4. Open the link provided in the server start logs.
5. Upon opening the notebook file, select the "ULA demo" kernel to make Jupyter use the project's virtual environment.


## Julia

Julia offers a smoother experience thanks to `Pluto.jl`, which is a notebook environment that is focused on reproducibility, offers reactive workflows that run chains of interdependent cells automatically, and provides native support for interactive widgets as well as full HTML/Markdown support.

To run the Julia version of the demo:

1. Install Julia - https://julialang.org/downloads/.
2. Navigate to the `julia` directory and open a terminal window.
3. Run the `start.sh` script
4. Once Julia has initialized and downloaded Pluto, a browser link will open and load the notebook.
5. Wait for Pluto to download the missing dependencies and start interacting with the notebook using the available widgets.
