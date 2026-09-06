

# Aurora PostgreSQL database cleanup on an Amazon MWAA environment
<a name="samples-database-cleanup"></a>

Amazon Managed Workflows for Apache Airflow uses an Aurora PostgreSQL database as the Apache Airflow metadata database, where DAG runs and task instances are stored. The following sample code periodically clears out entries from the dedicated Aurora PostgreSQL database for your Amazon MWAA environment.

**Important**  
Apache Airflow v3 restricts direct metadata database access from task code. Workers no longer connect to the metadata database, and DAG or task code can't import or use Apache Airflow database sessions or models directly. This change improves security and scalability. However, the DAG-based database cleanup approach that works in Apache Airflow v2 doesn't work in Apache Airflow v3 environments.  
Instead, use the `airflow db clean` CLI command through the Amazon MWAA CLI endpoint to perform metadata database cleanup.

**Note**  
Over time, the metadata database accumulates old records, XCom data, and stale task data. This growth uses database connections, slows your environment, and delays tasks. Run regular metadata cleanup to prevent these issues.

**Topics**
+ [Version](#samples-database-cleanup-version)
+ [Prerequisites](#samples-database-cleanup-prereqs)
+ [Dependencies](#samples-sql-server-dependencies)
+ [Code sample](#samples-database-cleanup-code)

## Version
<a name="samples-database-cleanup-version"></a>

The code samples on this page are specific to Apache Airflow v2 and v3 supported on Amazon MWAA. Refer to the [supported Apache Airflow versions](airflow-versions.md).

## Prerequisites
<a name="samples-database-cleanup-prereqs"></a>

To use the sample code on this page, you'll need the following:
+ An [Amazon MWAA environment](get-started.md).

## Dependencies
<a name="samples-sql-server-dependencies"></a>

To use this code example with Apache Airflow v2, no additional dependencies are required. Use [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images) to install Apache Airflow.

## Code sample
<a name="samples-database-cleanup-code"></a>

The following examples show how to clean the metadata database on your Amazon MWAA environment.

------
#### [ Apache Airflow v3.0.6 to 3.3.1 ]
+ You must specify `--clean-before-timestamp` to control how far back the cleanup reaches. Use an ISO 8601 formatted timestamp (for example, `2025-01-01T00:00:00+00:00`).
+ We recommend that you specify `--tables` to limit the cleanup to specific tables. If omitted, the command cleans all supported tables.
+ Start with a small scope — use an older `--clean-before-timestamp` value (closer to your environment creation date) and a single table first. This limits the cleanup to only the oldest records. Because the command deletes everything before the specified timestamp, using a more recent timestamp results in a larger deletion scope. Gradually move the timestamp forward as you gain confidence in the process.
+ Large-scale cleanup can impact database performance. Deleting a high volume of records puts pressure on the Aurora PostgreSQL database and might affect the responsiveness of your environment. Use the `--batch-size` parameter to control transaction size, and consider running cleanup during low-traffic periods. Exercise caution when running on production environments.

When you specify a table with `--tables`, the command automatically includes any dependent (child) tables that have foreign key relationships with the specified table. Child table records are deleted first, then the parent table records, to satisfy foreign key constraints. For example, specifying `--tables dag_run` also cleans `task_instance`, `task_instance_history`, `xcom`, `task_state_store`, and `deadline` because these tables reference `dag_run` through foreign keys.

The following table summarizes the dependency chains.


| Table specified | Additional tables cleaned (dependents) | 
| --- | --- | 
| dag\_run | task\_instance, task\_instance\_history, xcom, task\_state\_store, deadline | 
| dag | dag\_version, deadline | 
| task\_instance | task\_instance\_history, xcom | 
| trigger | task\_instance, task\_instance\_history, xcom | 
| dag\_version | task\_instance, task\_instance\_history, xcom, dag\_run | 

Tables without dependents (such as `log`, `job`, `import_error`, `sla_miss`) are cleaned in isolation when specified.

Use `--dry-run` to see exactly which tables and how many rows would be affected before committing to a cleanup.

The following table describes the available parameters for `airflow db clean`.


| Parameter | Description | Default | 
| --- | --- | --- | 
| --clean-before-timestamp | (Required) The date or timestamp before which data is purged. If no timezone is supplied, the Apache Airflow default timezone is assumed. Example: 2025-01-01T00:00:00\+00:00 | None | 
| --tables or -t | Table names to perform maintenance on (comma-separated). Options include: dag\_run, task\_instance, task\_instance\_history, log, job, xcom, import\_error, task\_reschedule, trigger, dag, dag\_version, sla\_miss, callback\_request, celery\_taskmeta, celery\_tasksetmeta, asset\_event, deadline, revoked\_token, task\_state\_store, connection\_test\_request, \_xcom\_archive | None | 
| --batch-size | Maximum number of rows to delete or archive in a single transaction. Lower values reduce long-running locks but increase the number of batches. | None | 
| --dry-run | Perform a dry run without actually deleting data. Recommended for initial testing. | False | 
| --skip-archive | Don't preserve purged records in an archive table. By default, db clean moves purged records into archive tables (named with a \_<table>\_archive convention, for example \_dag\_run\_archive) instead of permanently deleting them. This provides a safety net — you can inspect archived data, export it with airflow db export-archived, or drop it later with airflow db drop-archived. When --skip-archive is set, records are permanently deleted without this intermediate step. | False | 
| --dag-ids | Only cleanup data related to the given DAG IDs. | None | 
| --exclude-dag-ids | Avoid cleaning up data related to the given DAG IDs. | None | 
| -y, --yes | Skip the confirmation prompt. Required for non-interactive CLI execution through Amazon MWAA. | False | 
| -v, --verbose | Make logging output more verbose. | False | 

For more information about the available parameters, see [CLI and env variables reference](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#clean) on the Apache Airflow website.

The following examples show how to invoke `airflow db clean` through the Amazon MWAA CLI endpoint. For more information about creating CLI tokens, see [Creating an Apache Airflow CLI token](call-mwaa-apis-cli.md).

Using a Python script:

```
import boto3
import base64
import requests

# Replace with your environment name and AWS Region
mwaa_env_name = "YOUR_ENVIRONMENT_NAME"
region = "YOUR_REGION"

# Configure cleanup scope
clean_before_timestamp = "2025-06-01T00:00:00+00:00"
tables = "dag_run,task_instance,log,job,xcom"

# Build the Airflow CLI command
# -y flag is required to skip interactive confirmation prompt
airflow_cmd = f"db clean --clean-before-timestamp {clean_before_timestamp} --tables {tables} -y"

# Create a CLI token
client = boto3.client("mwaa", region_name=region)
cli_token_response = client.create_cli_token(Name=mwaa_env_name)

cli_token = cli_token_response["CliToken"]
web_server_hostname = cli_token_response["WebServerHostname"]

# Invoke the Airflow CLI through the MWAA endpoint
url = f"https://{web_server_hostname}/aws_mwaa/cli"
response = requests.post(
    url,
    headers={
        "Authorization": f"Bearer {cli_token}",
        "Content-Type": "text/plain",
    },
    data=airflow_cmd,
)

# Parse and display the results
stdout_message = base64.b64decode(response.json()["stdout"]).decode("utf-8")
stderr_message = base64.b64decode(response.json()["stderr"]).decode("utf-8")

print(f"Status code: {response.status_code}")
print(f"stdout:\n{stdout_message}")
print(f"stderr:\n{stderr_message}")
```

Before performing an actual cleanup, run with `--dry-run` to see what would be deleted:

```
AIRFLOW_CMD="db clean --clean-before-timestamp 2025-06-01T00:00:00+00:00 --tables dag_run,task_instance --dry-run -y"
```

------
#### [ Apache Airflow v2.7.2 to 2.11.2 ]

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

------