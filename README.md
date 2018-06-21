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

### Write new problems

You can write new problems for the Coding Bee via the following two steps. NOTE: in the top of the Jupyter Notebook it runs `administer.validate_all()` to verify that all functions and tests are working properly.

#### 1. Add function to problems/

Inside easy.py, medium.py, or hard.py, add a function with the same prefix as the other ones in that file with both a meaningful docstring (this is where the challenge definition comes from) and also a valid implementation.

For example in `problems/easy.py`:

```python3
def easy_len3(a):
    """Takes a list of integers and return True if its length is 3, otherwise False"""
    return len(a) == 3
```

#### 2. Add test cases to tests.json

Inside tests.json add an entry with the function name and an array of tests. A test is an array of length 2 containing an array of function arguments and the expected result.

For example:

```json
{
  "easy_len5": [
    [[], false],
    [[1, 2], false],
    [[5, 5, 5], true],
    [[1, 2, 3, 4], false]
  ]
}
```

### Credits

- Original project, problems, and test cases by [Brian Lee](https://github.com/brilee)
- Updates and additional problems for Spring 2018 by [Peter Coles](https://github.com/mrcoles)
- Made possible by the [Recurse Center community](https://www.recurse.com/)
