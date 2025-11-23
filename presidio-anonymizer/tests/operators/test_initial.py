import pytest

from presidio_anonymizer.operators import Initial

def test_correct_name():
    assert Initial().operator_name() == "initial"

@pytest.mark.parametrize(
    "input_text, initials",
    [
        ("     Eastern    Michigan   University ","E. M. U."),
        ("John Smith", "J. S."),
        ("@abc", "@A."),
        ("@843A", "@8."),
        ("--**abc", "--**A.")
    ],
)
def test_given_value_for_initial(input_text, initials):
    text = Initial().operate(input_text) 
    assert text == initials