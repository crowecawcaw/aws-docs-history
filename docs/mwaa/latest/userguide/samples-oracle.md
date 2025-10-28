# Creating a custom plugin with Oracle

The following sample walks you through the steps to create a custom plugin using Oracle for Amazon MWAA and can be combined with other custom plugins and binaries in your plugins.zip file.

###### Contents

- [Version](samples-oracle.md#samples-oracle-version "samples-oracle.md#samples-oracle-version")
- [Prerequisites](samples-oracle.md#samples-oracle-prereqs "samples-oracle.md#samples-oracle-prereqs")
- [Permissions](samples-oracle.md#samples-oracle-permissions "samples-oracle.md#samples-oracle-permissions")
- [Requirements](samples-oracle.md#samples-oracle-dependencies "samples-oracle.md#samples-oracle-dependencies")
- [Code sample](samples-oracle.md#samples-oracle-code "samples-oracle.md#samples-oracle-code")
- [Create the custom plugin](samples-oracle.md#samples-oracle-create-pluginszip-steps "samples-oracle.md#samples-oracle-create-pluginszip-steps")
  - [Download dependencies](samples-oracle.md#samples-oracle-install "samples-oracle.md#samples-oracle-install")
  - [Custom plugin](samples-oracle.md#samples-oracle-plugins-code "samples-oracle.md#samples-oracle-plugins-code")
  - [Plugins.zip](samples-oracle.md#samples-oracle-pluginszip "samples-oracle.md#samples-oracle-pluginszip")

- [Airflow configuration options](samples-oracle.md#samples-oracle-airflow-config "samples-oracle.md#samples-oracle-airflow-config")
- [What's next?](samples-oracle.md#samples-oracle-next-up "samples-oracle.md#samples-oracle-next-up")

## Version

You can use the code example on this page with **Apache Airflow v2** in [Python 3.10](https://peps.python.org/pep-0619/ "https://peps.python.org/pep-0619/") and **Apache Airflow v3** in [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/").

## Prerequisites

To use the sample code on this page, you'll need the following:

- An [Amazon MWAA environment](get-started.md "get-started.md").
- Worker logging enabled at any log level, `CRITICAL` or in the previous section for your environment. For more information about Amazon MWAA log types and how to manage your log groups, refer to
  [Accessing Airflow logs in Amazon CloudWatch](monitoring-airflow.md "monitoring-airflow.md")

## Permissions

No additional permissions are required to use the code example on this page.

## Requirements

To use the sample code on this page, add the following dependencies to your `requirements.txt`. To learn more, refer to [Installing Python dependencies](working-dags-dependencies.md "working-dags-dependencies.md").

```
-c https://raw.githubusercontent.com/apache/airflow/constraints-2.0.2/constraints-3.7.txt
cx_Oracle
apache-airflow-providers-oracle
```

## Code sample

The following steps describe how to create the DAG code that will test the custom plugin.

1. In your command prompt, navigate to the directory where your DAG code is stored. For example:

```
cd dags
```

2. Copy the contents of the following code sample and save locally as `oracle.py`.

```
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import os
import cx_Oracle

DAG_ID = os.path.basename(__file__).replace(".py", "")

def testHook(**kwargs):
    cx_Oracle.init_oracle_client()
    version = cx_Oracle.clientversion()
    print("cx_Oracle.clientversion",version)
    return version

with DAG(dag_id=DAG_ID, schedule_interval=None, catchup=False, start_date=days_ago(1)) as dag:
    hook_test = PythonOperator(
        task_id="hook_test",
        python_callable=testHook,
        provide_context=True
    )
```

## Create the custom plugin

This section describes how to download the dependencies, create the custom plugin and the plugins.zip.

### Download dependencies

Amazon MWAA will extract the contents of plugins.zip into `/usr/local/airflow/plugins` on each Amazon MWAA scheduler and worker container. This is used to add binaries to your environment. The following steps describe how to assemble the files needed for the custom plugin.

###### Pull the Amazon Linux container image

1. In your command prompt, pull the Amazon Linux container image, and run the container locally. For example:

```
docker pull amazonlinux
						docker run -it amazonlinux:latest /bin/bash
```

Your command prompt can invoke a bash command line. For example:

```
bash-4.2#
```

2. Install the Linux-native asynchronous I/O facility (libaio).

```
yum -y install libaio
```

3. Keep this window open for subsequent steps. We'll be copying the following files locally: `lib64/libaio.so.1`, `lib64/libaio.so.1.0.0`, `lib64/libaio.so.1.0.1`.

###### Download client folder

1. Install the unzip package locally. For example:

```
sudo yum install unzip
```

2. Create an `oracle_plugin` directory. For example:

```
mkdir oracle_plugin
cd oracle_plugin
```

3. Use the following curl command to download the [instantclient-basic-linux.x64-18.5.0.0.0dbru.zip](https://download.oracle.com/otn_software/linux/instantclient/185000/instantclient-basic-linux.x64-18.5.0.0.0dbru.zip "https://download.oracle.com/otn_software/linux/instantclient/185000/instantclient-basic-linux.x64-18.5.0.0.0dbru.zip") from [Oracle Instant Client Downloads for Linux x86-64 (64-bit)](https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html "https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html").

```
curl https://download.oracle.com/otn_software/linux/instantclient/185000/instantclient-basic-linux.x64-18.5.0.0.0dbru.zip > client.zip
```

4. Unzip the `client.zip` file. For example:

```
unzip *.zip
```

###### Extract files from Docker

1. In a new command prompt, show and write down your Docker container ID. For example:

```
docker container ls
```

Your command prompt can return all containers and their IDs. For example:

```
debc16fd6970
```

2. In your `oracle_plugin` directory, extract the `lib64/libaio.so.1`, `lib64/libaio.so.1.0.0`, `lib64/libaio.so.1.0.1` files to the local `instantclient_18_5` folder. For example:

```
docker cp debc16fd6970:/lib64/libaio.so.1 instantclient_18_5/
docker cp debc16fd6970:/lib64/libaio.so.1.0.0 instantclient_18_5/
docker cp debc16fd6970:/lib64/libaio.so.1.0.1 instantclient_18_5/
```

### Custom plugin

Apache Airflow will execute the contents of Python files in the plugins folder at startup. This is used to set and modify environment variables. The following steps describe the sample code for the custom plugin.

- Copy the contents of the following code sample and save locally as `env_var_plugin_oracle.py`.

```
from airflow.plugins_manager import AirflowPlugin
import os

os.environ["LD_LIBRARY_PATH"]='/usr/local/airflow/plugins/instantclient_18_5'
os.environ["DPI_DEBUG_LEVEL"]="64"

class EnvVarPlugin(AirflowPlugin):
    name = 'env_var_plugin'
```

### Plugins.zip

The following steps explain how to create the `plugins.zip`. The contents of this example can be combined with your other plugins and binaries into a single `plugins.zip` file.

###### Zip the contents of the plugin directory

1. In your command prompt, navigate to the `oracle_plugin` directory. For example:

```
cd oracle_plugin
```

2. Zip the `instantclient_18_5` directory in plugins.zip. For example:

```
zip -r ../plugins.zip ./
```

Your command prompt displays:

```
oracle_plugin$ ls
client.zip		instantclient_18_5
```

3. Remove the `client.zip` file. For example:

```
rm client.zip
```

###### Zip the env_var_plugin_oracle.py file

1. Add the `env_var_plugin_oracle.py` file to the root of the plugins.zip. For example:

```
zip plugins.zip env_var_plugin_oracle.py
```

2. Your plugins.zip now includes the following:

```
env_var_plugin_oracle.py
instantclient_18_5/
```

## Airflow configuration options

If you're using Apache Airflow v2, add `core.lazy_load_plugins : False` as an Apache Airflow configuration option.
To learn more, refer to [Using configuration options to load plugins in 2](configuring-env-variables.md#configuring-2.0-airflow-override "configuring-env-variables.md#configuring-2.0-airflow-override").

## What's next?

- Learn how to upload the `requirements.txt` file in this example to your Amazon S3 bucket in [Installing Python dependencies](working-dags-dependencies.md "working-dags-dependencies.md").
- Learn how to upload the DAG code in this example to the `dags` folder in your Amazon S3 bucket in [Adding or updating DAGs](configuring-dag-folder.md "configuring-dag-folder.md").
- Learn more about how to upload the `plugins.zip` file in this example to your Amazon S3 bucket in [Installing custom plugins](configuring-dag-import-plugins.md "configuring-dag-import-plugins.md").
