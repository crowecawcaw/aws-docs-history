

# Using dbt with Amazon MWAA
<a name="samples-dbt"></a>

With Amazon MWAA, you can use dbt (data build tool) and PostgreSQL to build and run data transformation workflows. In the following steps, add the required dependencies using a startup script, and upload a sample dbt project to your environment's Amazon S3 bucket. Then, use a sample DAG to verify that Amazon MWAA has installed the dependencies. Finally, use the `BashOperator` to run the dbt project.

**Topics**
+ [Version](#samples-dbt-version)
+ [Prerequisites](#samples-dbt-prereqs)
+ [Dependencies](#samples-dbt-dependencies)
+ [Upload a dbt project to Amazon S3](#samples-dbt-upload-project)
+ [Use a DAG to verify dbt dependency installation](#samples-dbt-test-dependencies)
+ [Create and upload a dbt profiles.yml](#samples-dbt-profiles)
+ [Use a DAG to run a dbt project](#samples-dbt-run-project)

## Version
<a name="samples-dbt-version"></a>

You can use the code example on this page with **Apache Airflow v2** in [Python 3.12](https://peps.python.org/pep-0693/) on the Python website and **Apache Airflow v3** in [Python 3.12](https://peps.python.org/pep-0693/) on the Python website.

## Prerequisites
<a name="samples-dbt-prereqs"></a>

Before you can complete the following steps, you need the following:
+ An [Amazon MWAA environment](get-started.md) using Apache Airflow v2.11.2. This sample was written, and tested with v2.11.2. You might need to modify the sample to use with other Apache Airflow versions.
+ A sample dbt project. To get started using dbt with Amazon MWAA, you can create a fork and clone the [dbt starter project](https://github.com/dbt-labs/dbt-starter-project) from the dbt-labs GitHub repository.

## Dependencies
<a name="samples-dbt-dependencies"></a>

To use Amazon MWAA with dbt, add the following startup script to your environment. To learn more, refer to [Using a startup script with Amazon MWAA](using-startup-script.md).

```
#!/bin/bash

if [[ "${MWAA_AIRFLOW_COMPONENT}" != "worker" ]]
  then
    exit 0
fi

echo "------------------------------"
echo "Installing virtual Python env"
echo "------------------------------"

pip3 install --upgrade pip

echo "Current Python version:"
python3 --version
echo "..."

sudo pip3 install --user virtualenv
sudo mkdir -p /usr/local/airflow/python3-virtualenv
cd /usr/local/airflow/python3-virtualenv
sudo python3 -m venv dbt-env
sudo chmod -R 777 *

echo "------------------------------"
echo "Activating venv in $DBT_ENV_PATH"
echo "------------------------------"

source dbt-env/bin/activate
pip3 list

echo "------------------------------"
echo "Installing libraries..."
echo "------------------------------"

# do not use sudo, as it will install outside the venv
pip3 install dbt-core==1.9.4 dbt-redshift==1.9.1 dbt-postgres==1.9.0

echo "------------------------------"
echo "Venv libraries..."
echo "------------------------------"

pip3 list
dbt --version

echo "------------------------------"
echo "Deactivating venv..."
echo "------------------------------"

deactivate
```

**Setting the DBT\_ENV\_PATH variable**  
You can set `$DBT_ENV_PATH` in the startup script or set it as an Airflow configuration in your Amazon MWAA environment.

In the following sections, upload your dbt project directory to Amazon S3 and run a DAG that validates whether Amazon MWAA has successfully installed the required dbt dependencies.

## Upload a dbt project to Amazon S3
<a name="samples-dbt-upload-project"></a>

To be able to use a dbt project with your Amazon MWAA environment, you can upload the entire project directory to your environment's `dags` folder. When the environment updates, Amazon MWAA downloads the dbt directory to the local `usr/local/airflow/dags/` folder.

**To upload a dbt project to Amazon S3**

1. Navigate to the directory where you cloned the dbt starter project.

1. Run the following Amazon S3 AWS CLI command to recursively copy the content of the project to your environment's `dags` folder using the `--recursive` parameter. The command creates a sub-directory called `dbt` that you can use for all of your dbt projects. If the sub-directory already exists, the project files are copied into the existing directory, and a new directory is not created. The command also creates a sub-directory within the `dbt` directory for this specific starter project.

   ```
   aws s3 cp {{dbt-starter-project}} s3://{{amzn-s3-demo-bucket}}/dags/dbt/{{dbt-starter-project}} --recursive
   ```

   You can use different names for project sub-directories to organize multiple dbt projects within the parent `dbt` directory.

## Use a DAG to verify dbt dependency installation
<a name="samples-dbt-test-dependencies"></a>

The following DAG uses a `BashOperator` and a bash command to verify whether Amazon MWAA has successfully installed the dbt dependencies specified in the startup script.

```
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

with DAG(dag_id="dbt-installation-test", schedule_interval=None, catchup=False, start_date=days_ago(1)) as dag:
    cli_command = BashOperator(
        task_id="bash_command",
        bash_command="/usr/local/airflow/python3-virtualenv/dbt-env/bin/dbt --version"
    )
```

Do the following to access task logs and verify that dbt and its dependencies have been installed.

1. Navigate to the Amazon MWAA console, then choose **Open Airflow UI** from the list of available environments.

1. On the Apache Airflow UI, find the `dbt-installation-test` DAG from the list, then choose the date in the `Last Run` column to open the last successful task.

1. Using **Graph View**, choose the `bash_command` task to open the task instance details.

1. Choose **Log** to open the task logs, then verify that the logs successfully list the dbt version specified in the startup script.

## Create and upload a dbt profiles.yml
<a name="samples-dbt-profiles"></a>

To connect to your target database, dbt requires a `profiles.yml` file. The DAG in the next section passes `--profiles-dir /tmp/dbt`, so dbt looks for `profiles.yml` directly inside the `/tmp/dbt` directory. This is the `dbt` folder you uploaded to Amazon S3.

The profile name in `profiles.yml` must match the `profile:` value defined in the starter project's `dbt_project.yml`. The dbt starter project uses `default`.

**To create and upload a profiles.yml**

1. In the directory where you cloned the starter project, create a file named `profiles.yml` with your database connection details.

   ```
   default:
     target: dev
     outputs:
       dev:
         type: postgres
         host: {{your-db-endpoint}}.{{region}}.rds.amazonaws.com
         port: 5432
         user: {{your_db_user}}
         password: {{your_db_password}}
         dbname: {{your_database}}
         schema: {{your_schema}}
         threads: 4
   ```

1. Upload the file to the `dbt` sub-directory in your environment's DAGs folder.

   ```
   aws s3 cp profiles.yml s3://{{amzn-s3-demo-bucket}}/dags/dbt/profiles.yml
   ```

**Protecting database credentials**  
To avoid storing plaintext credentials, reference secrets using the dbt `env_var()` function. Supply the values through Amazon MWAA environment variables or AWS Secrets Manager—for example, `password: "{{ env_var('DBT_PASSWORD') }}"`. Also make sure your Amazon MWAA VPC security groups allow your workers to reach your database on the configured port.

## Use a DAG to run a dbt project
<a name="samples-dbt-run-project"></a>

The following DAG uses a `BashOperator` to copy the dbt projects you uploaded to Amazon S3 from the local `usr/local/airflow/dags/` directory to the write-accessible `/tmp` directory, then runs the dbt project. The bash commands assume a starter dbt project titled `dbt-starter-project`. Modify the directory name according to the name of your project directory.

```
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

import os

DAG_ID = os.path.basename(__file__).replace(".py", "")

# assumes all files are in a subfolder of DAGs called dbt

with DAG(dag_id=DAG_ID, schedule_interval=None, catchup=False, start_date=days_ago(1)) as dag:
    cli_command = BashOperator(
        task_id="bash_command",
        bash_command="source /usr/local/airflow/python3-virtualenv/dbt-env/bin/activate;\
        cp -R /usr/local/airflow/dags/dbt /tmp;\
        echo 'listing project files:';\
        ls -R /tmp;\
        cd /tmp/dbt/dbt-starter-project;\
        /usr/local/airflow/python3-virtualenv/dbt-env/bin/dbt run --project-dir /tmp/dbt/dbt-starter-project --profiles-dir /tmp/dbt;\
        cat /tmp/dbt/dbt-starter-project/logs/dbt.log;\
        rm -rf /tmp/dbt/dbt-starter-project"
    )
```