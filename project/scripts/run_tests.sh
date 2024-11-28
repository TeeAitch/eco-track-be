#!/bin/bash

# Run the tests
python3 manage.py test users.tests
python3 manage.py test core.tests
