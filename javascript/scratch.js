var runTest = require("./test");

function f(a, b) {
  return Object.assign(a, b);
}

runTest("hard_merge_dicts", f);
