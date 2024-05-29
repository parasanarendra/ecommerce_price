import pytest
@pytest.mark.smoke
@pytest.mark.skip

def test_firstcase():
    msg = "Hi"
    assert msg == "Hi", "Test case Failed"

def test_secondcase():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"

