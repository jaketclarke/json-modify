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

# test read json
def test_load_json():
    input = f'test-data-input{os.sep}dir-one{os.sep}four.json'
    result = load_json(input)
    expected = {"id":4,"name":"Patricia Lebsack","username":"Karianne","email":"Julianne.OConner@kory.org","address":{"street":"Hoeger Mall","suite":"Apt. 692","city":"South Elvis","zipcode":"53919-4257","geo":{"lat":"29.4572","lng":"-164.2990"}},"phone":"493-170-9623 x156","website":"kale.biz","company":{"name":"Robel-Corkery","catchPhrase":"Multi-tiered zero tolerance productivity","bs":"transition cutting-edge web services"}}
    assert result == expected, f"Expected {expected}, Got {result}"
