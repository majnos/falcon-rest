# Using falcon as it is much faster and flexible solution

import falcon
from os.path import join, isfile, dirname
import os
from articles import Articles
import json
from urllib import parse

DEFAULT_FILE = join(dirname(__file__), '../json-data/reut2-000.json')
pwd = os.path.dirname(__file__)
template_dir = os.path.join(pwd)

articles = Articles(DEFAULT_FILE)


class Healthy(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'status': 'ok'})


class ListArticles(object):
    def on_get(self, req, resp):
        try:
            """Handles GET requests"""
            query = dict(parse.parse_qsl(req.query_string))
            resp.status = falcon.HTTP_200  # This is the default status
            resp.body = json.dumps(
                articles.get_filtered_view(query),
                ensure_ascii=False
                )
        except KeyError:
            raise falcon.HTTPError(falcon.HTTP_404, 'Key Not Found')


class SearchFullText(object):
    def on_get(self, req, resp):
        try:
            """Handles GET requests"""
            print(req.query_string)
            query = dict(parse.parse_qsl(req.query_string))
            resp.status = falcon.HTTP_200  # This is the default status
            resp.body = json.dumps(
                articles.get_fulltext_detail(query),
                ensure_ascii=False
                )
        except KeyError:
            raise falcon.HTTPError(falcon.HTTP_404, 'Key Not Found')


class GetDetailById(object):
    def on_get(self, req, resp, id):
        try:
            query = dict(parse.parse_qsl(req.query_string))
            resp.status = falcon.HTTP_200  # This is the default status
            resp.body = json.dumps(
                articles.get_filtered_detail(id),
                ensure_ascii=False
                )
        except KeyError:
            raise falcon.HTTPError(falcon.HTTP_404, 'Key Not Found')


app = falcon.API()

list_articles = ListArticles()
search_full_text = SearchFullText()
get_detail_by_id = GetDetailById()
healthy = Healthy()

app.add_route('/reuters/health', healthy)
app.add_route('/reuters/articles', list_articles)
app.add_route('/reuters/search', search_full_text)
app.add_route('/reuters/articles/{id}', get_detail_by_id)


# @app.route('/reuters/articles', methods=['GET'])
# def return_overview():
#     return jsonify(articles.get_filtered_view(request.args))

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
