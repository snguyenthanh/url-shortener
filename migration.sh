#!/bin/bash

export PYTHONPATH=.

alembic revision -m "Migrating..." --autogenerate --head head
alembic upgrade head
