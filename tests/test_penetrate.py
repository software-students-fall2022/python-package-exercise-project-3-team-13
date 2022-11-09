import pytest
from src.team13hackertype import penetrate
from unittest.mock import patch


class TestPenetrate:
    def test_successful_output(self, capsys):
        with patch('src.team13hackertype.penetrate.hackertype.hackertype'):
            penetrate.penetrate('python')
            captured = capsys.readouterr()

            actual_val = captured.out
            assert "Admin privileges acquired... Ready to implant virus code..." in actual_val
            assert "Logged Out... Successfully implanted" in actual_val

    def test_unsupported_language(self):
        with pytest.raises(NotImplementedError) as fnfe:
            penetrate.penetrate('invalid_language')

        expected_val = "Language invalid_language is not currently supported"
        actual_val = str(fnfe.value)

        assert expected_val == actual_val

    def test_color_error(self):
        with pytest.raises(ValueError) as ve:
            penetrate.penetrate(
                'python', notification_style="unsupported style 1", emphasis_style="unsupported style 2")

        expected_val = "style of unsupported style 1 and/or unsupported style 2 is not supported"
        actual_val = str(ve.value)

        assert expected_val == actual_val

    def test_banner_length_warning(self):
        with pytest.raises(UserWarning) as uw:
            penetrate.penetrate(
                'python', text="TextLongerThanMax")

        expected_val = "Incorrect Display: Text length should be less than 8."
        actual_val = str(uw.value)

        assert expected_val == actual_val
