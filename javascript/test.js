const assert = require("assert");
const equal = require("deep-equal");

const testConfigs = require("../tests.json");

const runTest = (testName, fn) => {
  console.log(`Testing: ${testName}`);
  const tests = testConfigs[testName];
  assert(tests !== undefined, `Test name not found: ${testName}`);

  const success = tests.every(([args, expected]) => {
    const actual = fn.apply(global, args);
    if (!equal(actual, expected)) {
      console.error("Not equal", actual, expected);
      return false;
    }
    return true;
  });

  console.log(success ? "SUCCESS" : "FAIL");
};

///////////////////////////

// hard_merge_dicts

function f(a, b) {
  return Object.assign(a, b);
}

runTest("hard_merge_dicts", f);
