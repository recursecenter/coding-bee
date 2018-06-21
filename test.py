import copy
from IPython.display import display, Markdown
import json

with open('./tests.json') as f:
    ALL_TESTS = json.load(f)

def run_test(func_name, func):
    test_cases = ALL_TESTS[func_name]
    failed = []
    passed = []

    for args, expected in test_cases:
        copy_args = copy.deepcopy(args) # defensive copying in case func mutates the value
        actual = func(*copy_args)
        result = (copy_args, expected, actual)
        if not actual == expected:
            # test failed
            failed.append(result)
        # elif not copy_args == args:
        #     # input args got mutated
        #     failed.append(result)
        else:
            passed.append(result)

    success = len(failed) == 0
    return success, passed, failed

def validate_official_solutions():
    from problems import NAME_TO_FN
    is_ok = True
    errors = []

    test_names = set(ALL_TESTS.keys())
    fn_names = set(NAME_TO_FN.keys())

    extra_test_names = ', '.join(test_names.difference(fn_names))
    extra_fn_names = ', '.join(fn_names.difference(test_names))

    if extra_test_names or extra_fn_names:
        is_ok = False
        if extra_test_names:
            errors.append(f'Extra tests found: {extra_test_names}')
        if extra_fn_names:
            errors.append(f'Extra functions found: {extra_fn_names}')
        return is_ok, errors

    challenges = ALL_TESTS.keys()
    for challenge in challenges:
        official_solution = NAME_TO_FN[challenge]
        success, passed, failed = run_test(challenge, official_solution)
        if failed:
            is_ok = False
            errors.append((f'### {challenge}', failed))

    return is_ok, errors
