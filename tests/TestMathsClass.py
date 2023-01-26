
from decimal import DivisionByZero
import conftest

from src.MathsClass import Maths_class
import pytest
import mock

class TestMathsClass:

    @pytest.fixtures("mock_maths_function_internal")
    def test_maths_function_success():
        expected_output  = 0.6400000000000001
        actual_output = Maths_class.maths_function(10)
        assert expected_output == actual_output

    def test_maths_function_failure_inline():
        with mock.path.object("Maths_class","maths_function_internal", side_effect=DivisionByZero, return_value=41) as maths_function_mock:
            with pytest.raises(DivisionByZero):
                actual_output = Maths_class.maths_function(5)
                maths_function_mock.assert_called_once()
                maths_function_mock.assert_called_once_with(5)

    def test_maths_function_success_inline():
        with mock.path.object("Maths_class","maths_function_internal",return_value=0.6400000000000001) as maths_function_mock:
            expected_output  = 0.6400000000000001
            actual_output = Maths_class.maths_function(10)
            maths_function_mock.assert_called_once()
            maths_function_mock.assert_called_once_with(10)
            assert expected_output == actual_output
