# StreamingHttpResponse in Django
<p>
    A StreamingHttpResponse is a response whose body is sent to the client in multiple pieces, or “chunks.” <br>
    On the other hand, HttpResponse is used to return a complete HTTP response with a fixed content or single piece.
</p>

## Features of the project
* Saved data in database in every 10 seconds
* The updated data will be presented in home page without loading ===> StreamingHttpResponse


# Setup
The first thing to do is to clone the repository:
```sh
$ https://github.com/MahmudJewel/StreamingHttpResponse
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ cd StreamingHttpResponse
$ python -m venv venv
$ source venv/bin/activate
```
Then install the dependencies:
```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Then run
```sh
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
```

### Happy Coding
Developed by **Mahmud**