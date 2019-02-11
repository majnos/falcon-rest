# logic of the whole app

import json
from model import to_detail_view, to_list_view
from nested import getByDot
from flask import make_response, jsonify, abort


class Articles:
    def __init__(self, file_path):
        with open(file_path) as f:
            self.raw_data = json.load(f)

    def get_filtered_view(self, query={}):
        output = []
        for article in self.raw_data:
            if self.match_all(article, query):
                output.append(to_list_view(article))
            elif not(any(query)):
                output.append(to_list_view(article))
        return output

    def get_filtered_detail(self, query={}):
        try:
            output = []
            for article in self.raw_data:
                if self.match_single(article, query):
                    output.append(to_detail_view(article))
            return output
        except KeyError:
            abort(404)

    def get_fulltext_detail(self, query):
        try:
            output = []
            for article in self.raw_data:
                if self.match_fulltext(article, query):
                    output.append(to_detail_view(article))
            return output
        except KeyError:
            abort(404)

    def match_single(self, article, newid):
        matched_key = 'metadata.newid'
        if self.match_item2item(newid, getByDot(article, matched_key)):
            return True
        return False

    def match_all(self, article, query):
        for key in query:
            matching = False
            value = query[key]
            if isinstance(getByDot(article, key), list):
                if self.match_item2list(value, getByDot(article, key)):
                    matching = True
            elif isinstance(getByDot(article, key), str):
                if self.match_item2item(value, getByDot(article, key)):
                    matching = True
            if not matching:
                return False
            else:
                return True

    def match_fulltext(self, article, query):
        for key in query:
            matching = False
            value = query[key]
            if isinstance(getByDot(article, key), str):
                if self.match_item2list(value, getByDot(article, key)):
                    matching = True
            if not matching:
                return False
            else:
                return True

    def match_item2item(self, item1, item2):
        if (item1 == item2):
            return True
        else:
            return False

    def match_item2list(self, item, list):
        if (item in list):
            return True
        else:
            return False
