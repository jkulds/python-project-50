import json

from gendiff.cli import generate_diff
from gendiff.parser import get_sorted_dict_from_path

FIXTURES_PATH = './tests/fixtures/'
FIRST_JSON_PATH = FIXTURES_PATH + 'file1.json'
SECOND_JSON_PATH = FIXTURES_PATH + 'file2.json'
THIRD_JSON_PATH = FIXTURES_PATH + 'file3.json'
FOURTH_JSON_PATH = FIXTURES_PATH + 'file4.json'
FIRST_YAML_PATH = FIXTURES_PATH + 'data1.yaml'
SECOND_YAML_PATH = FIXTURES_PATH + 'data2.yaml'
FIRST_YML_PATH = FIXTURES_PATH + 'data1.yml'
SECOND_YML_PATH = FIXTURES_PATH + 'data2.yml'
EXPECTED1_FILE_PATH = FIXTURES_PATH + 'expected1.txt'
EXPECTED2_FILE_PATH = FIXTURES_PATH + 'expected2.txt'
EXPECTED3_FILE_PATH = FIXTURES_PATH + 'expected3.txt'


def test_gendiff_correct_json():
    diffs = generate_diff(FIRST_JSON_PATH, SECOND_JSON_PATH)

    expected_file = open(EXPECTED1_FILE_PATH)
    expected = expected_file.read()

    assert diffs == expected


def test_gendiff_one_empty_json():
    diffs = generate_diff(FIRST_JSON_PATH, FOURTH_JSON_PATH)

    expected_file = open(EXPECTED3_FILE_PATH)
    expected = expected_file.read()

    assert diffs == expected


def test_gendiff_correct_yaml():
    diffs = generate_diff(FIRST_YAML_PATH, SECOND_YAML_PATH)

    expected_file = open(EXPECTED1_FILE_PATH)
    expected = expected_file.read()

    assert diffs == expected


def test_gendiff_correct_yml():
    diffs = generate_diff(FIRST_YML_PATH, SECOND_YML_PATH)

    expected_file = open(EXPECTED1_FILE_PATH)
    expected = expected_file.read()

    assert diffs == expected


def test_sorted_dict():
    d = json.load(open(FIRST_JSON_PATH))

    d1 = get_sorted_dict_from_path(FIRST_JSON_PATH)

    assert d1 == dict(sorted(d.items(), key=lambda x: x[0]))