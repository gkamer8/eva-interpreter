def test(eva):
    assert eva.eval(1) == 1
    assert eva.eval('"hello"') == "hello"