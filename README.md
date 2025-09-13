# NotePilot
## _Your Smart Note Management Companion_


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/pavitra-04/NotePilot)

NotePilot is a FastAPI-powered backend service designed to manage your personal notes efficiently.
It supports reading, creating, and organizing notes through easy HTTP APIs.

## Features
- Create, read, and organize your notes easily.

- Secure your API endpoints with simple token-based authentication.

- Fast, lightweight, and developer-friendly design.


## Tech
- [FastAPI] – Super fast Python web framework

- [Uvicorn] – Lightning-fast ASGI server

- [Pytest] – Testing framework for ensuring app correctness

NotePilot itself is open source with a [public repository][NotePilot]
 on GitHub.

## Installation
Make sure you have Python 3.10+ installed.

Clone the repository:

```sh
git clone https://github.com/yourusername/notepilot.git
cd NotePilot
```

Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install dependencies:
```sh
pip install fastapi uvicorn pytest
```
Run the app:
```sh
uvicorn main:app --reload
```
## ⚙️ API Endpoints
> **Get Root Message**
>> GET / \
>> Returns a welcome message.

> **Get Notes**
>> GET /notes \
Returns a list of predefined notes.

> **Read an Item**
>> GET /items/{item_id} \
Requires header X-Token: coneofsilence. \
Returns the item details or errors for invalid tokens/nonexistent items.

> **Create an Item**
>> POST /items/ \
>>Requires header X-Token: coneofsilence. \
Creates a new note item with fields: id, title, description.

## Running Tests

Make sure the virtual environment is activated, then run:
```sh
pytest
```
This will run all the automated tests to ensure your app works perfectly.





## License

MIT

## Summary

NotePilot helps you easily manage your notes using clean HTTP APIs.
It supports token-based authentication and simple CRUD operations, making it perfect for building your personal note-taking backend.



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

