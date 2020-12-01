from functions import *
import pytest
import os

# tests for strip_parent_directory
def test_strip_parent_dir():
    input='one/two/three'
    output='two/three'
    result = strip_parent_directory(input)
    assert result == output, f"Expected {output}, Got {result}"
    
def test_strip_parent_dir_one_level():
    input='one'
    output=None
    result = strip_parent_directory('one')
    assert result == output, f"Expected {output}, Got {result}"
    
# test makedir
def test_make_directorytree_if_not_exists():
    path = 'test1/test2'
    make_directorytree_if_not_exists(path)
    assert os.path.exists(path), f"Failed to create path {path}"
    