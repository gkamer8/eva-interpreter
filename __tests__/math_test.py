def test(eva):
    assert eva.eval(['+', 1, 5]) == 6
    assert eva.eval(['+', ['+', 2, 3], 5]) == 10
    assert eva.eval(['/', ['-', 10, 4], ['*', 2, 1]]) == 3