import json

import pytest

from gendiff.gendiff import generate_diff

FIXTURES_PATH = './tests/fixtures/'
BIG1_JSON_PATH = FIXTURES_PATH + 'big1.json'
BIG2_JSON_PATH = FIXTURES_PATH + 'big2.json'
JSON1_PATH = FIXTURES_PATH + 'file1.json'
JSON2_PATH = FIXTURES_PATH + 'file2.json'
EMPTY_JSON_PATH = FIXTURES_PATH + 'empty.json'

YAML1_PATH = FIXTURES_PATH + 'data1.yaml'
YAML2_PATH = FIXTURES_PATH + 'data2.yaml'
BIG1_YML_PATH = FIXTURES_PATH + 'big1.yml'
BIG2_YML_PATH = FIXTURES_PATH + 'big2.yml'
YML1_PATH = FIXTURES_PATH + 'data1.yml'
YML2_PATH = FIXTURES_PATH + 'data2.yml'

EXP_STYLISH_SMALL = FIXTURES_PATH + 'expected_stylish_small'
EXP_STYLISH_BIG = FIXTURES_PATH + 'expected_stylish_big'
EXP_STYLISH_EMPTY = FIXTURES_PATH + 'expected_stylish_empty'

EXP_PLAIN = FIXTURES_PATH + 'expected_plain'
EXPECTED_PLAIN_BIG = FIXTURES_PATH + 'expected_plain_big'

EXPECTED_JSON_SMALL = FIXTURES_PATH + 'expected_json_small'
EXPECTED_JSON_BIG = FIXTURES_PATH + 'expected_big_small'

CI_TEST_DATA_PATH = FIXTURES_PATH + 'ci_test_data/'
CI_TEST_JSON1 = CI_TEST_DATA_PATH + "file1.json"
CI_TEST_JSON2 = CI_TEST_DATA_PATH + "file2.json"
CI_TEST_YML1 = CI_TEST_DATA_PATH + "file1.yml"
CI_TEST_YML2 = CI_TEST_DATA_PATH + "file2.yml"
CI_TEST_RESULT_PLAIN = CI_TEST_DATA_PATH + "result_plain"
CI_TEST_EXP_STYLISH = CI_TEST_DATA_PATH + "result_stylish"


@pytest.mark.parametrize("path1, path2, path_expected, out_format", [
    pytest.param(JSON1_PATH, JSON2_PATH, EXP_STYLISH_SMALL, "stylish"),
    pytest.param(BIG1_JSON_PATH, BIG2_JSON_PATH, EXP_STYLISH_BIG, "stylish"),
    pytest.param(JSON1_PATH, EMPTY_JSON_PATH, EXP_STYLISH_EMPTY, "stylish"),
    pytest.param(YAML1_PATH, YAML2_PATH, EXP_STYLISH_SMALL, "stylish"),
    pytest.param(YML1_PATH, YML2_PATH, EXP_STYLISH_SMALL, "stylish"),
    pytest.param(BIG1_YML_PATH, BIG2_YML_PATH, EXP_STYLISH_BIG, "stylish"),
    pytest.param(JSON1_PATH, JSON2_PATH, EXP_PLAIN, "plain"),
    pytest.param(BIG1_JSON_PATH, BIG2_JSON_PATH, EXPECTED_PLAIN_BIG, "plain"),
    pytest.param(BIG1_YML_PATH, BIG2_YML_PATH, EXPECTED_PLAIN_BIG, "plain"),
    pytest.param(YML1_PATH, YML2_PATH, EXP_PLAIN, "plain"),
    pytest.param(YAML1_PATH, YAML2_PATH, EXP_PLAIN, "plain"),
    pytest.param(CI_TEST_JSON1, CI_TEST_JSON2, CI_TEST_RESULT_PLAIN, "plain"),
    pytest.param(CI_TEST_YML1, CI_TEST_YML2, CI_TEST_RESULT_PLAIN, "plain"),
    pytest.param(CI_TEST_JSON1, CI_TEST_JSON2, CI_TEST_EXP_STYLISH, "stylish"),
    pytest.param(CI_TEST_YML1, CI_TEST_YML2, CI_TEST_EXP_STYLISH, "stylish"),
])
def test_gendiff(path1: str, path2: str, path_expected: str, out_format: str):
    diffs = generate_diff(path1, path2, out_format)

    expected_file = open(path_expected)
    expected = expected_file.read()

    assert diffs == expected


def test_gendiff_json():
    diffs = generate_diff(JSON1_PATH, EMPTY_JSON_PATH, 'json')

    assert isinstance(diffs, str)
    assert len(diffs) > 0
    assert isinstance(json.loads(diffs), dict)
