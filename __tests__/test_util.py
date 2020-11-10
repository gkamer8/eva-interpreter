import importlib.util
spec = importlib.util.spec_from_file_location("evaParser", "./parser/evaParser.py")
evaParser = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evaParser)

def test(eva, code, expected):
    exp = evaParser.parse(code)
    assert eva.eval(exp) == expected

