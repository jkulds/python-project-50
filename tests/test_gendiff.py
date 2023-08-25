import json

import pytest

from gendiff.gendiff import generate_diff

FIXTURES_PATH = './tests/fixtures/'
BIG1_JSON_PATH = FIXTURES_PATH + 'big1.json'
BIG2_JSON_PATH = FIXTURES_PATH + 'big2.json'
FIRST_JSON_PATH = FIXTURES_PATH + 'file1.json'
SECOND_JSON_PATH = FIXTURES_PATH + 'file2.json'
EMPTY_JSON_PATH = FIXTURES_PATH + 'empty.json'

FIRST_YAML_PATH = FIXTURES_PATH + 'data1.yaml'
SECOND_YAML_PATH = FIXTURES_PATH + 'data2.yaml'
BIG1_YML_PATH = FIXTURES_PATH + 'big1.yml'
BIG2_YML_PATH = FIXTURES_PATH + 'big2.yml'
FIRST_YML_PATH = FIXTURES_PATH + 'data1.yml'
SECOND_YML_PATH = FIXTURES_PATH + 'data2.yml'

EXPECTED_STYLISH_SMALL_FILE_PATH = FIXTURES_PATH + 'expected_stylish_small'
EXPECTED_STYLISH_BIG_FILE_PATH = FIXTURES_PATH + 'expected_stylish_big'
EXPECTED_STYLISH_EMPTY_FILE_PATH = FIXTURES_PATH + 'expected_stylish_empty'

EXPECTED_PLAIN_FILE_PATH = FIXTURES_PATH + 'expected_plain'
EXPECTED_PLAIN_BIG_FILE_PATH = FIXTURES_PATH + 'expected_plain_big'

EXPECTED_JSON_SMALL_FILE_PATH = FIXTURES_PATH + 'expected_json_small'
EXPECTED_JSON_BIG_FILE_PATH = FIXTURES_PATH + 'expected_big_small'


@pytest.mark.parametrize("path1, path2, path_expected, out_format", [
    pytest.param(FIRST_JSON_PATH, SECOND_JSON_PATH, EXPECTED_STYLISH_SMALL_FILE_PATH, "stylish"),
    pytest.param(BIG1_JSON_PATH, BIG2_JSON_PATH, EXPECTED_STYLISH_BIG_FILE_PATH, "stylish"),
    pytest.param(FIRST_JSON_PATH, EMPTY_JSON_PATH, EXPECTED_STYLISH_EMPTY_FILE_PATH, "stylish"),
    pytest.param(FIRST_YAML_PATH, SECOND_YAML_PATH, EXPECTED_STYLISH_SMALL_FILE_PATH, "stylish"),
    pytest.param(FIRST_YML_PATH, SECOND_YML_PATH, EXPECTED_STYLISH_SMALL_FILE_PATH, "stylish"),
    pytest.param(BIG1_YML_PATH, BIG2_YML_PATH, EXPECTED_STYLISH_BIG_FILE_PATH, "stylish"),
    pytest.param(FIRST_JSON_PATH, SECOND_JSON_PATH, EXPECTED_PLAIN_FILE_PATH, "plain"),
    pytest.param(BIG1_JSON_PATH, BIG2_JSON_PATH, EXPECTED_PLAIN_BIG_FILE_PATH, "plain"),
    pytest.param(BIG1_YML_PATH, BIG2_YML_PATH, EXPECTED_PLAIN_BIG_FILE_PATH, "plain"),
    pytest.param(FIRST_YML_PATH, SECOND_YML_PATH, EXPECTED_PLAIN_FILE_PATH, "plain"),
    pytest.param(FIRST_YAML_PATH, SECOND_YAML_PATH, EXPECTED_PLAIN_FILE_PATH, "plain")
])
def test_gendiff(path1: str, path2: str, path_expected: str, out_format: str):
    diffs = generate_diff(path1, path2, out_format)

    expected_file = open(path_expected)
    expected = expected_file.read()

    assert diffs == expected


def test_gendiff_json():
    diffs = generate_diff(FIRST_JSON_PATH, EMPTY_JSON_PATH, 'json')

    assert isinstance(diffs, str)
    assert len(diffs) > 0
    assert isinstance(json.loads(diffs), dict)