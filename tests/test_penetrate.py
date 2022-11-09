import pytest
from src.team13LoremIpsum import penetrate
from unittest.mock import patch, mock_open


class TestPenetrate:
    def test_unsupported_language(self):
        with pytest.raises(NotImplementedError) as fnfe:
            penetrate.penetrate('invalid_language')

            expected_val = "invalid_language is not currently supported"
            actual_val = fnfe.value

            assert expected_val == actual_val

    def test_color_error(self):
        with pytest.raises(ValueError) as ve:
            penetrate.penetrate(
                'python', notification_style="unsupported style 1", emphasis_style="unsupported style 2")

            expected_val = "style of unsupported style 1 and/or unsupported style 2 is not supported"
            actual_val = ve.value

            assert expected_val == actual_val

    def test_banner_length_warning(self):
        with pytest.raises(UserWarning) as uw:
            penetrate.penetrate(
                'python', text="TextLongerThanMax")

            expected_val = "Incorrect Dispaly: Text length should be less than 8."
            actual_val = uw.value

            assert expected_val == actual_val
