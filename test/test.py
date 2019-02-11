# basic tests

import sys
import os
import pytest
from src.articles import Articles

FIXTURE = 'test_data.fixture.json'


@pytest.fixture
def test_data():
    fixture = os.path.join(os.path.dirname(__file__), FIXTURE)
    return Articles(fixture)


def test_list_query_returns_full_lists(test_data):
    assert len(test_data.get_filtered_view()) == 4


def test_list_query_returns_no_body(test_data):
    articles = test_data.get_filtered_view()
    for article in articles:
        assert "body" not in article["fulltext"]


def test_api_returns_detail_on_id(test_data):
    article = test_data.get_filtered_detail('4')
    assert article[0]['metadata']['newid'] == '4'


def test_api_returns_body_in_detail(test_data):
    article = test_data.get_filtered_detail('4')
    assert "body" in article[0]["fulltext"]


def test_api_returns_fulltext(test_data):
    article = test_data.get_filtered_detail('4')


def test_filter_places_returns_value(test_data):
    articles = test_data.get_filtered_view({'places': 'usa'})
    for article in articles:
        assert 'usa' in article['places']


def test_filter_places_and_topics_returns_values(test_data):
    articles = test_data.get_filtered_view(
            {'topics': 'cocoa', 'places': 'usa'}
            )
    for article in articles:
        assert 'usa' in article['places']
        assert 'cocoa' == article['topics'][0]
