# one time conversion of data

from bs4 import BeautifulSoup
import os
import json
from os.path import join, isfile, dirname
from os import listdir
from os import walk


sgm_data_dir_path = join(dirname(__file__), '../../sgm-data')
json_data_dir_path = join(dirname(__file__), '../../json-data')


class Parser:
    def xml_node_to_json(self, node):
        textNode = node.find('text')
        return {
            'metadata': {
                'topics': node.get('topics'),
                'lewissplit': node.get('lewissplit'),
                'cgisplit': node.get('cgisplit'),
                'oldid': node.get('oldid'),
                'newid': node.get('newid'),
            },
            'date': node.find('date').text,
            'unknown': node.find('unknown').text
            if node.find('unknown') else '',
            'fulltext': {
                'dateline': textNode.find('dateline').text
                if textNode.find('dateline') else '',
                'body': textNode.find('body').text
                if textNode.find('body') else '',
                'title': textNode.find('title').text
                if textNode.find('title') else '',
            },
            'topics': [elem.text for elem in node.find('topics').findAll('d')],
            'people': [
                elem.text for elem in node.find('people').findAll('d')
                ],
            'places': [
                elem.text for elem in node.find('places').findAll('d')
                ],
            'orgs': [
                elem.text for elem in node.find('orgs').findAll('d')
                ],
            'exchanges': [
                elem.text for elem in node.find('exchanges').findAll('d')
                ],
            'companies': [
                elem.text for elem in node.find('companies').findAll('d')
                ]
        }

    def convert_smg_to_json(self, sgm_file_handle):
        content = BeautifulSoup(sgm_file_handle, 'html.parser')
        jsonDocs = []
        for entry in content.findAll('reuters'):
            data = self.xml_node_to_json(entry)
            jsonDocs.append(data)
        return jsonDocs


if __name__ == '__main__':
    parser = Parser()
    sgm_data_files = [
        f for f in os.listdir(sgm_data_dir_path) if f.endswith('.sgm')
        ]
    for sgm_name in sgm_data_files:
        print("Starting with", sgm_name)
        json_path = join(
            json_data_dir_path,
            os.path.splitext(sgm_name)[0]+'.json')
        sgm_path = join(sgm_data_dir_path, sgm_name)
        with open(sgm_path, encoding="utf8", errors='ignore') as rf:
            with open(json_path, mode='w') as wf:
                jsonDocs = parser.convert_smg_to_json(rf)
                json.dump(jsonDocs, wf, indent=4, sort_keys=True)
