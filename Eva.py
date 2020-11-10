from Environment import Environment
import re
import collections

default_env = {
    'VERSION': '0.1'
}

class Eva:

    def __init__(self, glob=GlobalEnvironment):
        self.glob = glob

    def eval(self, exp, env=None):
        if env is None:
            env = self.glob

        if self._isNumber(exp):  # Ints and floats
            return exp
        if self._isString(exp):  # Strings
            return exp[1:-1]

        # Block

        if exp[0] == 'begin':
            blockEnv = Environment({}, env)
            return self._evalBlock(exp, blockEnv)

        # Variable declaration
        if exp[0] == 'var':
            _, name, value = exp
            return env.define(name, self.eval(value, env))

        # Variable update
        if exp[0] == 'set':
            _, name, value = exp
            return env.assign(name, self.eval(value, env))

        # Variable access
        if self._isVariableName(exp):
            return env.lookup(exp)

        # If expression
        if exp[0] == 'if':
            _tag, condition, consequent, alternate = exp
            if self.eval(condition):
                return self.eval(consequent, env)
            return self.eval(alternate, env)
        
        # while expression
        if exp[0] == 'while':
            _tag, condition, body = exp
            while self.eval(condition, env):
                result = self.eval(body, env)
            return result

        # Function calls
        if type(exp) is list:
            fn = self.eval(exp[0])
            args = list(map(lambda x: self.eval(x, env), exp[1:]))

            # Native function
            # If the function is an actual Python callable (function)
            if isinstance(fn, collections.Callable):
                pass

            # user defined function


        raise NotImplementedError

    def _evalBlock(self, block, env):
        _tag, *expressions = block
        for exp in expressions:
            result = self.eval(exp, env)
        return result


    def _isNumber(self, exp):
        return type(exp) is int or type(exp) is float

    def _isString(self, exp):
        return type(exp) is str and exp[0] == '"' and exp[-1] == '"'

    def _isVariableName(self, exp):
        return type(exp) == str and re.search('^[+\-*/<>=a-zA-Z0-9_]*$', exp) is not None

GlobalEnvironment = Environment({
    'null': None,
    'true': True,
    'false': False,
    'VERSION': '0.1',
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '-': lambda x, y=None: -x if y is None else x - y,
    '/': lambda x, y: x / y,
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
    '>=': lambda x, y: x >= y,
    '<=': lambda x, y: x <= y,
    '=': lambda x, y: x == y
})