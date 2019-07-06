#!/bin/bash

# grep the environment variables from .env
export $(egrep -v '^#' .env | xargs)

~/Programs/cloud_sql_proxy -dir=/cloudsql --instances=$CLOUD_SQL_CONNECTION_NAME --credential_file=$GOOGLE_APPLICATION_CREDENTIALS
