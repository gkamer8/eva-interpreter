import __tests__.test_util as tu

def test(eva):
    # Math

    tu.test(eva, '(+ 1 5)', 5)
    tu.test(eva, '(+ (+ 2 3) 5', 10)
    tu.test(eva, '(+ (* 2 3) 5', 11)

    # Comparison

    tu.test(eva, '(> 1 5)', False)
    tu.test(eva, '(< 1 5)', True)

    tu.test(eva, '(>= 5 5)', True)
    tu.test(eva, '(<= 5 5)', True)
    tu.test(eva, '(= 5 5)', True)
