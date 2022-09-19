import pytest


@pytest.mark.parametrize("hdl_val, expected",
                         [(85, "Normal"),
                          (50, "Borderline Low"),
                          (20, "Low")])
def test_check_HDL(hdl_val, expected):
    from blood_calculate import check_HDL
    answer = check_HDL(hdl_val)
    assert answer == expected


@pytest.mark.parametrize("ldl_val, expected",
                         [(200, "Very High"),
                          (170, "High"),
                          (150, "Borderline High"),
                          (100, "Normal")])
def test_check_LDL(ldl_val, expected):
    from blood_calculate import check_LDL
    answer = check_LDL(ldl_val)
    assert answer == expected


@pytest.mark.parametrize("total_val, expected",
                         [(250, "High"),
                          (220, "Borderline High"),
                          (180, "Normal")])
def test_check_total_cholesterol(total_val, expected):
    from blood_calculate import check_total_cholesterol
    answer = check_total_cholesterol(total_val)
    assert answer == expected
