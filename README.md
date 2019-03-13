PY2LUNCH
=========
> It's like go2lunch, but in python

An application, that suggests where do we want to go for a lunch today.
## Goals
1. Eliminate _"Where we're going to eat today?"_ problem
2. Vote for restaurants and make a decision about that
3. Automatically add new restaurants
4. Implement several suggestion models
5. Learn how to create flexible, maintainable and scalable app using Django's best practices.
6. Have fun!

_more to come, stay tuned._

## Run local dev server.

1. Create python virtual environment and activate it:
  ```!bash
  virtualenv env
  source env/bin/activate
  ```
2. Download into project directory GAE SDK and install python packages:
  ```!bash
  ./install_deps
  ```
3. Run local devserver:
  ```!bash
  ./manage.py runserver
  ```
4. Open in the browser django dev server `http://127.0.0.1:8000` and GAE devserver admin `http://127.0.0.1:8014`.
5. Login into django admin with your Google account email (make sure you don't have any saved cookies).

Walkthrough video with running local dev server env https://youtu.be/DdKy2cwOaq8.
