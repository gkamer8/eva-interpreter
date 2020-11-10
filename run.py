from __tests__ import self_eval_test, math_test, block_test, variables_test
from __tests__ import if_test, while_test, built_in_function_test

from Eva import Eva

eva = Eva()

self_eval_test.test(eva)
math_test.test(eva)
block_test.test(eva)
variables_test.test(eva)
if_test.test(eva)
while_test.test(eva)
built_in_function_test.test(eva)

print("All assertions passed.")