# Aurora PostgreSQL database cleanup on an Amazon MWAA environment

Amazon Managed Workflows for Apache Airflow uses an Aurora PostgreSQL database as the Apache Airflow metadata database, where DAG runs and task instances are stored.
The following sample code periodically clears out entries from the dedicated Aurora PostgreSQL database for your Amazon MWAA
environment.

###### Topics

- [Version](#samples-database-cleanup-version "#samples-database-cleanup-version")
- [Prerequisites](#samples-database-cleanup-prereqs "#samples-database-cleanup-prereqs")
- [Dependencies](#samples-sql-server-dependencies "#samples-sql-server-dependencies")
- [Code sample](#samples-database-cleanup-code "#samples-database-cleanup-code")

## Version

The code samples on this page are specific to Apache Airflow v2 and v3 supported on Amazon MWAA. Refer to the [supported Apache Airflow versions](airflow-versions.md "airflow-versions.md").

## Prerequisites

To use the sample code on this page, you'll need the following:

- An [Amazon MWAA environment](get-started.md "get-started.md").

## Dependencies

To use this code example with Apache Airflow v2, no additional dependencies are required. Use
[aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") to install Apache Airflow.

## Code sample

The following DAG cleans the metadata database for the tables specified in
`TABLES_TO_CLEAN`. The example deletes data from the specified tables that is
older than 30 days. To adjust how far back the entries are deleted, set
`MAX_AGE_IN_DAYS` to a different value.

Apache Airflow v3.0.6 to 3.2.1

```
from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

# Note: Database commands might time out if running longer than 5 minutes. If this occurs, please increase the MAX_AGE_IN_DAYS (or change
# timestamp parameter to an earlier date) for initial runs, then reduce on subsequent runs until the desired retention is met.

MAX_AGE_IN_DAYS = 30

# To clean specific tables, please provide a comma-separated list per
# https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#clean

# A value of None will clean all tables
TABLES_TO_CLEAN = None

with DAG(
    dag_id="clean_db_dag",
    schedule=None,
    catchup=False,
    start_date=datetime(2026, 1, 1),
) as dag:
    tables_flag = f"--tables '{TABLES_TO_CLEAN}' " if TABLES_TO_CLEAN else ""

    bash_command = (
        f"TIMESTAMP=$(date -u -d '{MAX_AGE_IN_DAYS} days ago' '+%Y-%m-%d %H:%M:%S' 2>/dev/null "
        f"|| date -u -v-{MAX_AGE_IN_DAYS}d '+%Y-%m-%d %H:%M:%S') && "
        "echo \"Cleaning records before: $TIMESTAMP\" && "
        "airflow db clean "
        "--clean-before-timestamp \"$TIMESTAMP\" "
        f"{tables_flag}"
        "--skip-archive --yes"
    )

    cli_command = BashOperator(
        task_id="bash_command",
        bash_command=bash_command,
    )

```

Apache Airflow v2.7.2 to 2.11.2

```
from airflow import DAG
from airflow.models.param import Param
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta

# Note: Database commands might time out if running longer than 5 minutes. If this occurs, please increase the MAX_AGE_IN_DAYS (or change
# timestamp parameter to an earlier date) for initial runs, then reduce on subsequent runs until the desired retention is met.

MAX_AGE_IN_DAYS = 30

# To clean specific tables, please provide a comma-separated list per
# https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#clean
# A value of None will clean all tables

TABLES_TO_CLEAN = None

with DAG(
    dag_id="clean_db_dag",
    schedule_interval=None,
    catchup=False,
    start_date=days_ago(1),
    params={
        "timestamp": Param(
            default=(datetime.now()-timedelta(days=MAX_AGE_IN_DAYS)).strftime("%Y-%m-%d %H:%M:%S"),
            type="string",
            minLength=1,
            maxLength=255,
        ),
    }
) as dag:
    if TABLES_TO_CLEAN:
        bash_command="airflow db clean --clean-before-timestamp '{{ params.timestamp }}' --tables '"+TABLES_TO_CLEAN+"' --skip-archive --yes"
    else:
        bash_command="airflow db clean --clean-before-timestamp '{{ params.timestamp }}' --skip-archive --yes"

    cli_command = BashOperator(
        task_id="bash_command",
        bash_command=bash_command
    )
```
