# Coding Bee

Jupyter notebook for MCing the [Recurse Center](https://www.recurse.com/) Coding Bee :bee:

Problems live inside problems/[easy|medium|hard].py. Test cases live in tests.json.

Questions are auto-generated from the docstrings of the problems and validated against tests.json.

### Install

```bash
python3 -m venv .venv # requires Python >= 3.6
. .venv/bin/activate.fish # or .sh or whatever your shell is
pip3 install -r requirements.txt

cd javascript
yarn install
```

### Run

Start the notebook locally via the following command and open "coding_bee.ipynb":

```bash
jupyter notebook
```

Run Python questions in a new cell below the notebook.

Run other languages in https://repl.it/

If you want to run JavaScript against test cases, you can paste the function into `javascript/scratch.js` and run it there. (TODO: this could benefit from something more slick!)

### Credits

- Original project, problems, and test cases by [Brian Lee](https://github.com/brilee)
- Updates and additional problems for Spring 2018 by [Peter Coles](https://github.com/mrcoles)
- Made possible by the [Recurse Center community](https://www.recurse.com/)
