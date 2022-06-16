# API Starter

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This started with [Cookiecutter Django][cookiecutter-django] is a framework for
jumpstarting production-ready Django projects quickly.

We've taken some liberties though. For example we've swapped out django-allauth
for djoser for REST api authentication.

- [API Starter](#api-starter)
  - [Coding Rules](#coding-rules)
  - [Commit Message Guidelines](#commit-message-guidelines)
    - [Commit Message Format](#commit-message-format)
    - [Example:](#example)
  - [Running](#running)
    - [Environment Requirements](#environment-requirements)
    - [Set up environment and run](#set-up-environment-and-run)
    - [Set up cloud tasks locally](#set-up-cloud-tasks-locally)
  - [Type checks](#type-checks)
  - [Testing](#testing)
    - [Test coverage](#test-coverage)
    - [Running tests with py.test](#running-tests-with-pytest)
  - [Task Management](#task-management)
    - [Set up cloud tasks locally](#set-up-cloud-tasks-locally-1)
  - [Deployment](#deployment)
    - [Docker](#docker)
    - [Google App Engine Standard](#google-app-engine-standard)
    - [Google Cloud Run](#google-cloud-run)
    - [Google Kubernetes Enegine](#google-kubernetes-enegine)

## Coding Rules

To ensure consistency throughout the source code, keep these rules in mind as you are working:

- All new functionality **must be tested**.
- All features or bug fixes **must be tested** by one or more tests.
- We follow [The Elements of Python Style][py-style-guide], but wrap all code at
  **120 characters** max. An automated formatter is available and pre-commit is set up to ensure
  this.

## Commit Message Guidelines

[Conventional Commits][conventional-commits] are the way to go here.

An example of this is seen in the way the [Angular Team][angular] manages commit messages.

This project follows similar precise rules as well to **make messages more readable** when looking at the history.

### Commit Message Format

Each commit message consists of a **header**, a **body** and a **footer**. The header has a special format that includes a **type**, an optional **scope** and a **subject**:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

### Example:

```
fix: prevent data migration (#1)

Eshop data migration was creating an extra plan category for tests.
Tests were failing. So prevent data migration from running during testing.

PR Close #3
```

The **header** is mandatory and the **scope** of the header is optional.

Any line of the commit message cannot be longer than 100 characters! This allows the message to be easier to read on GitHub as well as in various git tools.

The footer should contain a [closing reference to an issue](https://help.github.com/articles/closing-issues-via-commit-messages/) if any.

## Running

### Environment Requirements

- python 3
- postgres db
- postgres client
- [virtualenv][venv]

### Set up environment and run

1.  Make sure Python 3.9 and virtualenv are already installed.
2.  Clone the repo and configure the virtual environment and run [pre-commit][pre-commit] for the first time:

```
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements/local.txt
$ pre-commit install
$ pre-commit run --all-files
```

3. Set up environment variables. Examples exist in `.env.sample`:

```
cp .env.sample .env
```

4. Edit `.env` to reflect your local environment settings and export them to your terminal

```
(env) $ source .env
```

5.  Run the initial migrations, build the database, create user and run project

```
(env) $ python manage.py migrate
(env) $ python manage.py createsuperuser
(env) $ python manage.py runserver
```

### Set up cloud tasks locally

1. Clone https://github.com/aertje/cloud-tasks-emulator. More instructions out there to run this

2. Run locally with the `default-notification` cloud task queue

```
export APP_ENGINE_EMULATOR_HOST=http://localhost:8000
go run ./ -queue projects/dev/locations/here/queues/default-notification
```

## Type checks

Running type checks with mypy:

    $ mypy api_project

## Testing

As mentioned in the [coding rules], all features or bug fixes **must be tested** by one or more tests.

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Or to run all above commands in one fell swoop simply run:

    $ make test

### Running tests with py.test

    $ pytest

## Task Management

This has an optional feature to schedule long running / expensive activities in the
background with google cloud tasks.

### Set up cloud tasks locally

1. Clone https://github.com/aertje/cloud-tasks-emulator. More instructions out there to
   run this

2. Run locally with the `default-notification` cloud task queue

```
export APP_ENGINE_EMULATOR_HOST=http://localhost:8000
go run ./ -queue projects/sample-project/locations/local/queues/default-queue
```

## Deployment

You wouldn't have to worry about deployment. Will be handled automatically by Google Cloud Build.

The following details how to deploy this application outside of setting up google cloud build.

### Docker

Detailed docker instructions found on [cookiecutter-django docker
documentation][cookiecutter-django-docker].

### Google App Engine Standard

Instructions to deploy django apps on [App Engine][gae].

### Google Cloud Run

Instructions to deploy dockerized apps with [Cloud Run][cloud-run].

### Google Kubernetes Enegine

Instructions to deploy django with [GKE][gke].

[conventional-commits]: https://conventionalcommits.org/
[pre-commit]: https://pre-commit.com/#3-install-the-git-hook-scripts
[angular]: https://github.com/angular/angular/blob/master/CONTRIBUTING.md
[py-style-guide]: https://github.com/amontalenti/elements-of-python-style
[gae]: https://cloud.google.com/appengine/docs/standard/python3/runtime
[cloud-run]: https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python
[gke]: https://cloud.google.com/python/django/kubernetes-engine
[cookiecutter-django]: http://cookiecutter-django.readthedocs.io/en/latest/
[cookiecutter-django-docker]: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html
[venv]: https://virtualenv.pypa.io/en/latest/
