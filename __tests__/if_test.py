def test(eva):
    eva.eval(
        ['begin',
            ['var', 'x', 10],
            ['var', 'y', 0],

            ['if', ['>', 'x', 10],
                ['set', 'y', 20],
                ['set', 'y', 30]
            ]
        ]
    )