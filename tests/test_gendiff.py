import json

from gendiff.scripts.gendiff import get_sorted_dict_from_json, generate_diff

FIRST_FILE_PATH = './tests/fixtures/file1.json'
SECOND_FILE_PATH = './tests/fixtures/file2.json'


def test_gendiff_correct():
    d1 = get_sorted_dict_from_json(FIRST_FILE_PATH)
    d2 = get_sorted_dict_from_json(SECOND_FILE_PATH)
    diffs = generate_diff(d1, d2)

    assert diffs == '''- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true'''


def test_sorted_dict():
    d = json.load(open(FIRST_FILE_PATH))

    d1 = get_sorted_dict_from_json(FIRST_FILE_PATH)

    assert d1 == dict(sorted(d.items(), key=lambda x: x[0]))