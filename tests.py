from functions import *
import pytest

def test_strip_parent_dir():
    result = strip_parent_directory('one/two/three')
    assert result == 'two/ssss'

def test_strip_parent_dir_one_level():
    result = strip_parent_directory('one')
    assert result is None