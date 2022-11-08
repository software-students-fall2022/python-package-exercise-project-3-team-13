import pytest
from src.team13LoremIpsum import penetrate
from unittest.mock import patch, mock_open
from rich.console import Console
import pyfiglet


class TestConsole:
    @pytest.fixture
    def console(self):
        con = Console()
        return con

    def test_console_init(self, console):
        expected_val = True
        assert isinstance(console, Console) == expected_val

    def test_console_print_color(self, console, capsys):
        console.print("123")
        captured = capsys.readouterr()
        assert captured.out == "123\n"


class TestPyfiglet:
    def test_pyfiglet(self):
        banner = pyfiglet.figlet_format("DARKWEB", font="banner3-D")
        assert isinstance(banner, pyfiglet.FigletString) == True
        assert len(banner) > 0


class TestPenetrate:
    def test_unsupported_language(self):
        with pytest.raises(NotImplementedError) as fnfe:
            penetrate.penetrate('invalid_language')

            expected_val = "invalid_language is not currently supported"
            actual_val = fnfe.value

            assert expected_val == actual_val
