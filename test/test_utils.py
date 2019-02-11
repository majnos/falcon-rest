# tests for the parser
# when input data changes we are able to
# verify simply that our parser is working

import sys
import os
import json
import pytest
from src.utils.parsesgm import Parser

FIXTURE_INPUT = 'test_parser_input.fixture.sgm'
FIXTURE_OUTPUT = 'test_parser_output.fixture.json'


@pytest.fixture
def test_data():
    output = []
    parser = Parser()
    fp = os.path.join(os.path.dirname(__file__), FIXTURE_INPUT)
    with open(fp, encoding="utf8", errors='ignore') as fh:
        output = parser.convert_smg_to_json(fh)
        return output


def test_input_equals_output(test_data):
    fp = os.path.join(os.path.dirname(__file__), FIXTURE_OUTPUT)
    with open(fp, encoding="utf8", errors='ignore') as fh:
        loaded_template = json.load(fh)
        assert loaded_template == test_data
