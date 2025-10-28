# Using a startup script with Amazon MWAA

A startup script is a shell (`.sh`) script you host in your environment's Amazon S3 bucket similar to your DAGs, requirements, and plugins. Amazon MWAA runs this script during startup on every individual Apache Airflow component (worker, scheduler, and web server) before installing requirements and initializing the Apache Airflow process. Use a startup script to do the following:

- **Install runtimes** – Install Linux runtimes required by your workflows and connections.
- **Configure environment variables** – Set environment variables for each Apache Airflow component. Overwrite common variables such as `PATH`, `PYTHONPATH`, and `LD_LIBRARY_PATH`.
- **Manage keys and tokens** – Pass access tokens for custom repositories to `requirements.txt` and configure security keys.
  The following topics describe how to configure a startup script to install Linux runtimes, set environment variables, and troubleshoot related issues using CloudWatch Logs.

###### Topics

- [Configure a startup script](#create-startup-script "#create-startup-script")
- [Install Linux runtimes using a startup script](#install-dependencies-using-startup-script "#install-dependencies-using-startup-script")
- [Set environment variables using a startup script](#set-variables-using-startup-script "#set-variables-using-startup-script")

## Configure a startup script

To use a startup script with your existing Amazon MWAA environment, upload a `.sh` file to your environment's Amazon S3 bucket. Then, to associate the script with the environment, specify the following in your environment details:

- **The Amazon S3 URL path to the script** – The relative path to the script hosted in your bucket, for example, `s3://mwaa-environment/`startup.sh``
- **The Amazon S3 version ID of the script** – The version of the startup shell script in your Amazon S3 bucket. You must specify the [version ID](../../../AmazonS3/latest/userguide/versioning-workflows.md "../../../AmazonS3/latest/userguide/versioning-workflows.md") that Amazon S3 assigns to the file every time you update the script. Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long, for example, `3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo`.

To complete the steps in this section, use the following sample script. The script outputs the value assigned to `MWAA_AIRFLOW_COMPONENT`. This environment variable identifies each Apache Airflow component that the script runs on.

Copy the code and save it locally as `startup.sh`.

```
#!/bin/sh
			​
echo "Printing Apache Airflow component"
echo $MWAA_AIRFLOW_COMPONENT
```

Next, upload the script to your Amazon S3 bucket.

AWS Management Console

###### To upload a shell script (console)

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. From the **Buckets** list, choose the name of the bucket associated with your environment.
3. On the **Objects** tab, choose **Upload**.
4. On the **Upload** page, drag and drop the shell script you created.
5. Choose **Upload**.

The script is listed in the list of **Objects**. Amazon S3 creates a new version ID for the file. If you update the script and upload it again using the same file name, a new version ID is assigned to the file.

AWS CLI

###### To create and upload a shell script (CLI)

1. Open a new command prompt, and run the Amazon S3 `ls` command to list and identify the bucket associated with your environment.

```
`aws s3 ls`
```

2. Navigate to the folder where you saved the shell script. Use `cp` in a new prompt window to upload the script to your bucket. Replace `amzn-s3-demo-bucket` with your information.

```
`aws s3 cp startup.sh s3://`amzn-s3-demo-bucket`/startup.sh`
```

If successful, Amazon S3 outputs the URL path to the object:

```
upload: ./startup.sh to s3://amzn-s3-demo-bucket/startup.sh
```

3. Use the following command to retrieve the latest version ID for the script.

```
`aws s3api list-object-versions --bucket `amzn-s3-demo-bucket` --prefix startup --query 'Versions[?IsLatest].[VersionId]' --output text`
```

```
BbdVMmBRjtestta1EsVnbybZp1Wqh1J4
```

You specify this version ID when you associate the script with an environment.

Now, associate the script with your environment.

AWS Management Console

###### To associate the script with an environment (console)

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Select the row for the environment you want to update, then choose **Edit**.
3. On the **Specify details** page, for **Startup script file - _optional_**, enter the Amazon S3 URL for the script, for example: `s3://`amzn-s3-demo-bucket`/startup-sh.`.
4. Choose the latest version from the drop down list, or **Browse S3** to find the script.
5. Choose **Next**, then proceed to the **Review and save** page.
6. Review changes, then choose **Save**.

Environment updates can take between 10 to 30 minutes. Amazon MWAA runs the startup script as each component in your environment restarts.

AWS CLI

###### To associate the script with an environment (CLI)

- Open a command prompt and use `update-environment` to specify the Amazon S3 URL and version ID for the script.

```
`aws mwaa update-environment \
--name `your-mwaa-environment` \
--startup-script-s3-path `startup.sh` \
--startup-script-s3-object-version `BbdVMmBRjtestta1EsVnbybZp1Wqh1J4``
```

If successful, Amazon MWAA returns the Amazon Resource Name (ARN) for the environment:

```
arn:aws:airflow:us-west-2:123456789012:environment/your-mwaa-environment
```

Environment update can take between 10 to 30 minutes. Amazon MWAA runs the startup script as each component in your environment restarts.

Finally, retrieve log events to verify that the script is working as expected. When you activate logging for an each Apache Airflow component, Amazon MWAA creates a new log group and log stream. For more information, refer to [Apache Airflow log types](monitoring-airflow.md#monitoring-airflow-log-groups "monitoring-airflow.md#monitoring-airflow-log-groups").

AWS Management Console

###### To get the Apache Airflow log stream (console)

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose your environment.
3. In the **Monitoring** pane, choose the log group for which you want to access logs, for example, **Airflow scheduler log group** .
4. In the CloudWatch console, from the **Log streams** list, choose a stream with the following prefix: `startup_script_execution_ip`.
5. On the **Log events** pane, you will refer to the output of the command printing the value for `MWAA_AIRFLOW_COMPONENT`. For example, for scheduler logs, you will the following:

```
Printing Apache Airflow component
								**scheduler**
								Finished running startup script. Execution time: 0.004s.
								Running verification
								Verification completed
```

You can repeat the previous steps to access worker and webserver logs.

## Install Linux runtimes using a startup script

Use a startup script to update the operating system of an Apache Airflow component, and install additional runtime libraries to use with your workflows. For example, the following script runs `yum update` to update the operating system.

When running `yum update` in a startup script, you must exclude Python using `--exclude=python*` as listed in the example. For your environment to run, Amazon MWAA installs a specific version of Python compatible with your environment. Therefore, you can't update the environment's Python version using a startup script.

```
#!/bin/sh

echo "Updating operating system"
sudo yum update -y --exclude=python*
```

To install runtimes on specific Apache Airflow component, use `MWAA_AIRFLOW_COMPONENT` and `if` and `fi` conditional statements. This example runs a single command to install the `libaio` library on the scheduler and worker, but not on the webserver.

###### Important

- If you have configured a [private webserver](configuring-networking.md#access-overview-private "configuring-networking.md#access-overview-private"), you must either use the following condition or provide all installation files locally to avoid installation timeouts.
- Use `sudo` to run operations that require administrative privileges.

```
#!/bin/sh

if [[ "${MWAA_AIRFLOW_COMPONENT}" != "webserver" ]]
  then
    sudo yum -y install libaio

fi
```

You can use a startup script to get the Python version.

```
#!/bin/sh

export PYTHON_VERSION_CHECK=`python -c 'import sys; version=sys.version_info[:3]; print("{0}.{1}.{2}".format(*version))'`
echo "Python version is $PYTHON_VERSION_CHECK"
```

Amazon MWAA does not support overriding the default Python version, as this might lead to incompatibilities with the installed Apache Airflow libraries.

## Set environment variables using a startup script

Use startup scripts to set environment variables and modify Apache Airflow configurations. The following defines a new variable, `ENVIRONMENT_STAGE`. You can reference this variable in a DAG or in your custom modules.

```
#!/bin/sh

export ENVIRONMENT_STAGE="development"
echo "$ENVIRONMENT_STAGE"
```

Use startup scripts to overwrite common Apache Airflow or system variables. For example, you set `LD_LIBRARY_PATH` to instruct Python to search for binaries in the path you specify. This lets you provide custom binaries for your workflows using [plugins](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/plugins.html "https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/plugins.html"):

```
#!/bin/sh

export LD_LIBRARY_PATH=/usr/local/airflow/plugins/`your-custom-binary`
```

### Reserved environment variables

Amazon MWAA reserves a set of critical environment variables. If you overwrite a _reserved_ variable, Amazon MWAA restores it to its default. The following lists the reserved variables:

- `MWAA__AIRFLOW__COMPONENT` – Used to identify the Apache Airflow component with one of the following values: `scheduler`, `worker`, or `webserver`.
- `AIRFLOW__WEBSERVER__SECRET_KEY` – The secret key used for securely signing session cookies in the Apache Airflow web server.
- `AIRFLOW__CORE__FERNET_KEY` – The key used for encryption and decryption of sensitive data stored in the metadata database, for example, connection passwords.
- `AIRFLOW_HOME` – The path to the Apache Airflow home directory where configuration files and DAG files are stored locally.
- `AIRFLOW__CELERY__BROKER_URL` – The URL of the message broker used for communication between the Apache Airflow scheduler and the Celery worker nodes.
- `AIRFLOW__CELERY__RESULT_BACKEND` – The URL of the database used to store the results of Celery tasks.
- `AIRFLOW__CORE__EXECUTOR` – The executor class that Apache Airflow must use. In Amazon MWAA this is a `CeleryExecutor`
- `AIRFLOW__CORE__LOAD_EXAMPLES` – Used to activate, or deactivate, the loading of example DAGs.
- `AIRFLOW__METRICS__METRICS_BLOCK_LIST` – Used to manage which Apache Airflow metrics are emitted and captured by Amazon MWAA in CloudWatch.
- `SQL_ALCHEMY_CONN` – The connection string for the RDS for PostgreSQL database used to store Apache Airflow metadata in Amazon MWAA.
- `AIRFLOW__CORE__SQL_ALCHEMY_CONN` – Used for the same purpose as `SQL_ALCHEMY_CONN`, but following the new
  Apache Airflow naming convention.
- `AIRFLOW__CELERY__DEFAULT_QUEUE` – The default queue for Celery tasks in Apache Airflow.
- `AIRFLOW__OPERATORS__DEFAULT_QUEUE` – The default queue for tasks using specific Apache Airflow operators.
- `AIRFLOW_VERSION` – The Apache Airflow version installed in the Amazon MWAA environment.
- `AIRFLOW_CONN_AWS_DEFAULT` – The default AWS credentials used to integrate with other AWS services in.
- `AWS_DEFAULT_REGION` – Sets the default AWS Region used with default credentials to integrate with other AWS services.
- `AWS_REGION` – If defined, this environment variable overrides the values in the environment variable `AWS_DEFAULT_REGION`
  and the profile setting region.
- `PYTHONUNBUFFERED` – Used to send `stdout` and `stderr` streams to container logs.
- `AIRFLOW__METRICS__STATSD_ALLOW_LIST` – Used to configure an allow list of comma-separated prefixes to send the metrics that start with the elements of the list.
- `AIRFLOW__METRICS__STATSD_ON` – Activates sending metrics to `StatsD`.
- `AIRFLOW__METRICS__STATSD_HOST` – Used to connect to the `StatSD` daemon.
- `AIRFLOW__METRICS__STATSD_PORT` – Used to connect to the `StatSD` daemon.
- `AIRFLOW__METRICS__STATSD_PREFIX` – Used to connect to the `StatSD` daemon.
- `AIRFLOW__CELERY__WORKER_AUTOSCALE` – Sets the maximum and minimum concurrency.
- `AIRFLOW__CORE__DAG_CONCURRENCY` – Sets the number of task instances that can run concurrently by the scheduler in one DAG.
- `AIRFLOW__CORE__MAX_ACTIVE_TASKS_PER_DAG` – Sets the maximum number of active tasks per DAG.
- `AIRFLOW__CORE__PARALLELISM` – Defines the maximum number of task instances that can simultaneously.
- `AIRFLOW__SCHEDULER__PARSING_PROCESSES` – Sets the maximum number of processes parsed by the scheduler to schedule DAGs.
- `AIRFLOW__CELERY_BROKER_TRANSPORT_OPTIONS__VISIBILITY_TIMEOUT` – Defines the number of seconds a worker waits to acknowledge the task before the message is redelivered to another worker.
- `AIRFLOW__CELERY_BROKER_TRANSPORT_OPTIONS__REGION` – Sets the AWS Region for the underlying Celery transport.
- `AIRFLOW__CELERY_BROKER_TRANSPORT_OPTIONS__PREDEFINED_QUEUES` – Sets the queue for the underlying Celery transport.
- `AIRFLOW_SCHEDULER_ALLOWED_RUN_ID_PATTERN` – Used to verify the validity of your input for the `run_id` parameter when triggering a DAG.
- `AIRFLOW__WEBSERVER__BASE_URL` – The URL of the web server used to host the Apache Airflow UI.
- `PYTHONPATH` (only for Apache Airflow v2.9 and later) – Reserved by Amazon MWAA to ensure that all basic environment functionalities operate correctly.

###### Note

For Apache Airflow versions earlier than v2.9, `PYTHONPATH` is an _unreserved_ environment variable.

### Unreserved environment variables

You can use a startup script to overwrite _unreserved_ environment variables. The following lists some of these common variables:

- `PATH` – Specifies a list of directories where the operating system searches for executable files and scripts. When a command runs in the command line, the system checks the directories in `PATH` to find and execute the command. When you create custom operators or tasks in Apache Airflow, you might need to rely on external scripts or executables. If the directories containing these files are not in the specified in the `PATH` variable, the tasks fail to run when the system is unable to locate them. By adding the appropriate directories to `PATH`, Apache Airflow tasks can find and run the required executables.
- `PYTHONPATH` – Used by the Python interpreter to determine which directories to search for imported modules and packages. It is a list of directories that you can add to the default search path. This lets the interpreter find and load Python libraries not included in the standard library, or installed in system directories. Use this variable to add your modules and custom Python packages and use them with your DAGs.

###### Note

For Apache Airflow v2.9 and later, `PYTHONPATH` is a _reserved_ environment variable.

- `LD_LIBRARY_PATH` – An environment variable used by the dynamic linker and loader in Linux to find and load shared libraries. It specifies a list of directories containing shared libraries, which are searched before the default system library directories. Use this variable to specify your custom binaries.
- `CLASSPATH` – Used by the Java Runtime Environment (JRE) and Java Development Kit (JDK) to locate and load Java classes, libraries, and resources at runtime. It is a list of directories, JAR files, and ZIP archives that contain compiled Java code.
