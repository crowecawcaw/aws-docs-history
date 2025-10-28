# Using dbt with Amazon MWAA

This topic demonstrates how you can use dbt and Postgres with Amazon MWAA. In the following steps, you'll add the required dependencies to your `requirements.txt`, and upload a sample dbt project to your environment's Amazon S3 bucket.
Then, you'll use a sample DAG to verify that Amazon MWAA has installed the dependencies, and finally use the `BashOperator` to run the dbt project.

###### Topics

- [Version](#samples-dbt-version "#samples-dbt-version")
- [Prerequisites](#samples-dbt-prereqs "#samples-dbt-prereqs")
- [Dependencies](#samples-dbt-dependencies "#samples-dbt-dependencies")
- [Upload a dbt project to Amazon S3](#samples-dbt-upload-project "#samples-dbt-upload-project")
- [Use a DAG to verify dbt dependency
  installation](#samples-dbt-test-dependencies "#samples-dbt-test-dependencies")
- [Use a DAG to run a dbt project](#samples-dbt-run-project "#samples-dbt-run-project")

## Version

You can use the code example on this page with **Apache Airflow v2** in [Python 3.10](https://peps.python.org/pep-0619/ "https://peps.python.org/pep-0619/") and **Apache Airflow v3** in [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/").

## Prerequisites

Before you can complete the following steps, you'll need the following:

- An [Amazon MWAA environment](get-started.md "get-started.md") using Apache Airflow v2.2.2. This sample was written, and tested with v2.2.2. You might need to modify the sample to use
  with other Apache Airflow versions.
- A sample dbt project. To get started using dbt with Amazon MWAA, you can create a fork and clone the [dbt starter project](https://github.com/dbt-labs/dbt-starter-project "https://github.com/dbt-labs/dbt-starter-project") from the dbt-labs GitHub repository.

## Dependencies

To use Amazon MWAA with dbt, add the following startup script to your environment. To learn more, refer to [Using a startup script with Amazon MWAA](using-startup-script.md "using-startup-script.md").

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
  sudo mkdir python3-virtualenv
  cd python3-virtualenv
  sudo python3 -m venv dbt-env
  sudo chmod -R 777 *

  echo "------------------------------"
  echo "Activating venv in"
  $DBT_ENV_PATH
	  		echo "------------------------------"

  source dbt-env/bin/activate
  pip3 list

  echo "------------------------------"
  echo "Installing libraries..."
  echo "------------------------------"

  # do not use sudo, as it will install outside the venv
  pip3 install dbt-redshift==1.6.1 dbt-postgres==1.6.1

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

In the following sections, you'll upload your dbt project directory to Amazon S3 and
run a DAG that validates whether Amazon MWAA has successfully installed the required dbt
dependencies.

## Upload a dbt project to Amazon S3

To be able to use a dbt project with your Amazon MWAA environment, you can upload the entire project directory to your environment's `dags` folder.
When the environment updates, Amazon MWAA downloads the dbt directory to the local `usr/local/airflow/dags/` folder.

###### To upload a dbt project to Amazon S3

1. Navigate to the directory where you cloned the dbt starter project.
2. Run the following Amazon S3 AWS CLI command to recursively copy the content of the project to your environment's `dags` folder using the `--recursive` parameter.
   The command creates a sub-directory called `dbt` that you can use for all of your dbt projects. If the sub-directory already exists, the project files are copied into the existing directory, and a new directory is not created. The command also creates a sub-directory within the `dbt`
   directory for this specific starter project.

```
`aws s3 cp `dbt-starter-project` s3://`amzn-s3-demo-bucket`/dags/dbt/`dbt-starter-project` --recursive`
```

You can use different names for project sub-directories to organize multiple dbt projects within the parent `dbt` directory.

## Use a DAG to verify dbt dependency

installation

The following DAG uses a `BashOperator` and a bash command to
verify whether Amazon MWAA has successfully installed the dbt dependencies specified in
`requirements.txt`.

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

Do the following to access task logs and verify that dbt and its dependencies have been
installed.

1. Navigate to the Amazon MWAA console, then choose **Open Airflow
   UI** from the list of available environments.
2. On the Apache Airflow UI, find the `dbt-installation-test` DAG from the
   list, then choose the date in the `Last Run` column to open the
   last successful task.
3. Using **Graph View**, choose the `bash_command`
   task to open the task instance details.
4. Choose **Log** to open the task logs, then verify that the
   logs successfully list the dbt version we specified in
   `requirements.txt`.

## Use a DAG to run a dbt project

The following DAG uses a `BashOperator` to copy the dbt projects you
uploaded to Amazon S3 from the local `usr/local/airflow/dags/` directory to the
write-accessible `/tmp` directory, then runs the dbt project. The bash
commands assume a starter dbt project titled `dbt-starter-project`. Modify
the directory name according to the name of your project directory.

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
			cd /tmp/dbt/mwaa_dbt_test_project;\
			/usr/local/airflow/python3-virtualenv/dbt-env/bin/dbt run --project-dir /tmp/dbt/mwaa_dbt_test_project --profiles-dir ..;\
			cat /tmp/dbt_logs/dbt.log;\
			rm -rf /tmp/dbt/mwaa_dbt_test_project"
			)
```
