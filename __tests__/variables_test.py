def test(eva):
    assert eva.eval(['var', 'x', 10]) == 10
    assert eva.eval(['var', 'x', ['*', 2, 2]]) == 4
    assert eva.eval('x') == 4