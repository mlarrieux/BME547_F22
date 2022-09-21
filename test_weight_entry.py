import pytest


@pytest.mark.parametrize("input, expected", [
    ("22 lb", 10),
    ("50 kg", 50),
    ("35.6 kg", 36),
    ("-22 lb", -10),
    ("22 LB", 10),
    ("22 pound", 10),
    ("22 lb, 50 kg", None),
    ("22", None),
    ])
def test_parse_weight_input(input, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(input)
    assert answer == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (.1, .2, .3)
])
def test_add(a, b, expected):
    from weight_entry import add
    answer = add(a,b)
    # print(pytest.approx(expected))
    assert answer == pytest.approx(expected)
