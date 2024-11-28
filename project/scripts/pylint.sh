#!/bin/bash

poetry run pylint --load-plugins pylint_django --ignore=migrations,.venv --ignore-patterns='migrations/.*\.py' --disable=too-many-ancestors .
