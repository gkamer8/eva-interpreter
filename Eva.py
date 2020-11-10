from Environment import Environment
import re

default_env = {
    'VERSION': '0.1'
}

class Eva:

    def __init__(self, glob=Environment(default_env)):
        self.glob = glob

    def eval(self, exp, env=None):
        if env is None:
            env = self.glob

        if isNumber(exp):  # Ints and floats
            return exp
        if isString(exp):  # Strings
            return exp[1:-1]

        # Math operations

        if exp[0] == '+':  # Addition
            return self.eval(exp[1], env) + self.eval(exp[2], env)
        if exp[0] == '*':  # Multiplication
            return self.eval(exp[1], env) * self.eval(exp[2], env)
        if exp[0] == '-':  # Subtraction
            return self.eval(exp[1], env) - self.eval(exp[2], env)
        if exp[0] == '/':  # Division
            return self.eval(exp[1], env) / self.eval(exp[2], env)

        # Comparison operators
        if exp[0] == '>':
            return self.eval(exp[1], env) > self.eval(exp[2], env)
        if exp[0] == '<':
            return self.eval(exp[1], env) < self.eval(exp[2], env)
        if exp[0] == '>=':
            return self.eval(exp[1], env) >= self.eval(exp[2], env)
        if exp[0] == '<=':
            return self.eval(exp[1], env) <= self.eval(exp[2], env)

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
        if isVariableName(exp):
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

        raise NotImplementedError

    def _evalBlock(self, block, env):
        _tag, *expressions = block
        for exp in expressions:
            result = self.eval(exp, env)
        return result


    def _isNumber(exp):
        return type(exp) is int or type(exp) is float

    def _isString(exp):
        return type(exp) is str and exp[0] == '"' and exp[-1] == '"'

    def _isVariableName(exp):
        return type(exp) == str and re.search('^[a-zA-Z][a-zA-Z0-9]*$', exp) is not None

