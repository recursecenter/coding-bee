import random

from IPython.display import display, Markdown

from problems import *
from test import run_test, validate_official_solutions

def choose(problems):
    title, desc = random.choice(list(problems.items()))
    return display(Markdown(f'\n### {title}\n\n{desc}\n'))

def check(challenge_name, submission):
    display(Markdown(f'### Testing: {challenge_name}'))
    success, passed, failed = run_test(challenge_name, submission)
    for args, expected, actual in failed:
        print('Input: {}'.format(copy_args))
        print('Expected: {!r}' % expected)
        print('Got back: {!r}' % actual)

    _display('SUCCESS' if success else 'FAIL', success)

def validate_all():
    is_ok, errors = validate_official_solutions()
    if errors:
        for error in errors:
            print(error)

    msg = 'READY TO GO!' if is_ok else 'PLEASE FIX THE ABOVE ISSUES BEFORE PROCEEDING!'
    _display(msg, is_ok)

#

def _display(msg, success):
    emoji = '🙂' if success else '🙃'
    color = 'green' if success else '#ba2425'
    display(Markdown(f'<font color="{color}">**_{msg}_** {emoji}</font>'))
