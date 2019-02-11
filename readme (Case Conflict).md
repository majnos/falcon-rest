Task:
=====

https://archive.ics.uci.edu/ml/datasets/Reuters-21578+Text+Categorization+Collection
Problem: Create a REST api that allows you to explore the data set above. You can use any one of the .sgm files in the data set, you may import the data into a data store if you want to. You are expected to use Java or Python and REST and any other technology of your choice
Expected APIs
1. API to list content 
2. API to search content
3. API get a specific content by id/any identifier
 
Please share code git repo and be ready to demonstrate and discuss on a call.



Prerequisites:
===============
`pyenv install 3.7.1`

`pyenv local 3.7.1`

How to work with repo:
======================

Install dependencies:
`make install`

Run server:
`make start`

Test functionality:
`make verify`

TBD:
* list articles according to time <DATETIME1>.....<DATETIME2>
* increase debugability
* streamline js like features for python
* increase readability of the cooe
* be able to debug tests also in vscode (PYTHONPATH)
* add regex search for fulltext
* add test for sgml=>json parser (verification of the elements)
* fix linting issues and automatic linting before commit
* create better documentation for api (swagger)


How to start:
=============

import:
`h2o.postman_collection` to your postman and playaround with the rest api

APIs:
1) `localhost:5000/reuters/articles/<int:newid>`  
returns detail view of the article with body for display of the article to readers
2) `localhost:5000/retures/articles?`
returns list of articles
you can use querystring to filter out the articles
e.g.
`http://localhost:5000/reuters/articles?metadata.topics=YES&places=usa`
 * metadata.newid
 * metadtaa.oldid
 * metadta.cgisplit
 * metaddata.lewissplit
 * metadata.topics
 * places
 * people
 * orgs
 * exchanges
 * companies
 * topics
 
3) `http://localhost:5002/reuters/search?fulltext.body=businessmen`
returns the fulltext search 
you can query these by fulltext:
fulltext.title
fulltext.dataline
fulltext.body


Notes:
======
* trying out node like tools for python
* sgml data do not have unique keys that is why I am using dot based selectors, imo fastest approach