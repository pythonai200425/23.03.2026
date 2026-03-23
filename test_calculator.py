from calculator import Calculator
import pytest


def test_power_returns_expected_value():
    calc = Calculator()
    a = 3
    b = 2
    expected = 9

    actual = calc.power(a, b)

    assert expected == actual

def test_power_returns_expected_value_bih():
    calc = Calculator()
    a = 30
    b = 3
    expected = 27000

    actual = calc.power(a, b)

    assert expected == actual


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 0, 1),
        (0, 3, 0),
        (-2, 3, -8),
        (-2, 2, 4),
        (2.5, 2, 6.25),
        (1, 99, 1),
    ],
)
def test_power_edge_and_sign_cases(a, b, expected):
    calc = Calculator()

    actual = calc.power(a, b)

    if isinstance(expected, float):
        assert actual == pytest.approx(expected)
    else:
        assert actual == expected


def test_power_negative_exponent():
    calc = Calculator()

    actual = calc.power(2, -2)

    assert actual == pytest.approx(0.25)

