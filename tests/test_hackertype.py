import pytest
from src.team13LoremIpsum import hackertype
from unittest.mock import patch, mock_open
import os


class TestLoopingString:

    @pytest.fixture
    def string(self):
        return '0123456789'

    def test_return_correct_substring(self, string):
        looping_string = hackertype.looping_string(string, 1)

        for i in range(10):
            actual_val = next(looping_string)
            expected_val = str(i)

            assert expected_val == actual_val

    def test_return_correct_substring_after_looping(self, string):
        looping_string = hackertype.looping_string(string, 6)
        next(looping_string)
        next(looping_string)

        actual_val = next(looping_string)
        expected_val = '234567'

        assert expected_val == actual_val

    def test_chunk_size_greater_than_string_length(self, string):
        looping_string = hackertype.looping_string(string, 15)

        actual_val = next(looping_string)
        expected_val = '012345678901234'

        assert expected_val == actual_val


class TestGetCodeSnippet:

    def test_file_read_success(self):
        expected_val = "print('Hello, world!')"

        __dirname = os.path.dirname(os.path.abspath(__file__))
        snippet_filename = os.path.normpath(
            os.path.join(__dirname, '../src/code_snippets/python.txt'))

        with patch('src.team13LoremIpsum.hackertype.open',
                   mock_open(read_data=expected_val), create=True) as m:
            actual_val = hackertype.get_code_snippet('python')
            m.assert_called_once_with(snippet_filename)
            assert expected_val == actual_val

    def test_unsupported_language(self):
        with pytest.raises(NotImplementedError) as fnfe:
            hackertype.get_code_snippet('invalid_language')

            expected_val = "invalid_language is not currently supported"
            actual_val = fnfe.value

            assert expected_val == actual_val

    def test_io_exception(self):
        with pytest.raises(IOError) as ioe:
            with patch('src.team13LoremIpsum.hackertype.open') as m:
                m.side_effect = IOError()
                hackertype.get_code_snippet('java')

                expected_val = "Unexpected I/O error"
                actual_val = ioe.value

                assert expected_val in actual_val


class TestHackertype:

    @pytest.fixture
    def mock_on_press_side_effect(self):
        # sets the side effect of on_press as just
        # running the callback of on_press

        def mock_keyboard_output(arg):
            # the only argument to on_press is a lambda function
            # that takes in one (unused) argument
            arg(None)

        return mock_keyboard_output

    def test_hackertype_default_output(self,
                                       mock_on_press_side_effect,
                                       capsys):
        with patch('src.team13LoremIpsum.hackertype.keyboard.on_press',
                   create=True) as on_press_mock,\
             patch('src.team13LoremIpsum.hackertype.keyboard.wait'):

            on_press_mock.side_effect = mock_on_press_side_effect
            hackertype.hackertype('python')
            captured = capsys.readouterr()

            expected_val = '"""Functional tests '
            actual_val = captured.out

            assert expected_val == actual_val

    def test_hackertype_modified_speed(self,
                                       mock_on_press_side_effect,
                                       capsys):
        with patch('src.team13LoremIpsum.hackertype.keyboard.on_press',
                   create=True) as on_press_mock,\
             patch('src.team13LoremIpsum.hackertype.keyboard.wait'):

            on_press_mock.side_effect = mock_on_press_side_effect
            hackertype.hackertype('python', 5)
            captured = capsys.readouterr()

            expected_val = '"""Fu'
            actual_val = captured.out

            assert expected_val == actual_val

    def test_hackertype_java(self,
                             mock_on_press_side_effect,
                             capsys):
        with patch('src.team13LoremIpsum.hackertype.keyboard.on_press',
                   create=True) as on_press_mock,\
             patch('src.team13LoremIpsum.hackertype.keyboard.wait'):

            on_press_mock.side_effect = mock_on_press_side_effect
            hackertype.hackertype('java')
            captured = capsys.readouterr()

            expected_val = 'package org.springfr'
            actual_val = captured.out

            assert expected_val == actual_val
