### Hexlet tests and linter status:
[![Actions Status](https://github.com/jkulds/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/jkulds/python-project-50/actions)
<a href="https://codeclimate.com/github/jkulds/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/d67890b9dc584ca5b5e9/maintainability" /></a>
<a href="https://codeclimate.com/github/jkulds/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/d67890b9dc584ca5b5e9/test_coverage" /></a>

### Gendiff json files
[Screencast demo](https://asciinema.org/a/Yxo0fK24JeD6MIehz3KK6sw55)
#### Extended Demo
[Json files with formatters](https://asciinema.org/a/OyaweWPRtdZyerfMX1MajWvlo/edit)<br/>
[YML/YAML files with formatters](https://asciinema.org/a/ER7MDLBzDyYfWpINCibqxgr7c)



#### Example
<i>Json</i> <br/>
stylish - gendiff tests/fixtures/file1.json tests/fixtures/file2.json <br/>
stylish - gendiff tests/fixtures/big1.json tests/fixtures/big2.json <br/>
plain - gendiff tests/fixtures/big1.json tests/fixtures/big2.json -f plain<br/> 
json - gendiff tests/fixtures/big1.json tests/fixtures/big2.json -f json<br/>

<i>YML, YAML</i> <br/>
stylish - gendiff tests/fixtures/data1.yml tests/fixtures/data2.yml <br/>
stylish - gendiff tests/fixtures/big1.yml tests/fixtures/big2.yml <br/>
stylish - gendiff tests/fixtures/data1.yaml tests/fixtures/data2.yaml <br/>
plain - gendiff tests/fixtures/big1.yml tests/fixtures/big2.yml -f plain<br/> 
json - gendiff tests/fixtures/big1.yml tests/fixtures/big2.yml -f json<br/>
