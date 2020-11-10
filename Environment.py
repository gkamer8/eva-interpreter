class Environment:

    def __init__(self, record = dict(), parent=None):
        self.record = record
        self.parent = parent

    def define(self, name, value):
        self.record[name] = value
        return value

    def lookup(self, name):
        return self.resolve(name).record[name]
    
    def assign(self, name, value):
        self.resolve(name).record[name] = value
        return value
    
    def resolve(self, name):
        if name in self.record:
            return self
        if self.parent is None:
            raise ReferenceError(f'Variable {name} is not defined.')
        return self.parent.resolve(name)
