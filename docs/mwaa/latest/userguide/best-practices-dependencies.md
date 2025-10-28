# Managing Python dependencies in requirements.txt

This topic describes how to install and manage Python dependencies in a
`requirements.txt` file for an Amazon Managed Workflows for Apache Airflow environment.

###### Contents

- [Testing DAGs using the Amazon MWAA CLI utility](best-practices-dependencies.md#best-practices-dependencies-cli-utility "best-practices-dependencies.md#best-practices-dependencies-cli-utility")
- [Installing Python dependencies using PyPi.org Requirements File Format](best-practices-dependencies.md#best-practices-dependencies-different-ways "best-practices-dependencies.md#best-practices-dependencies-different-ways")
  - [Option one: Python dependencies from the Python Package Index](best-practices-dependencies.md#best-practices-dependencies-pip-extras "best-practices-dependencies.md#best-practices-dependencies-pip-extras")
  - [Option two: Python wheels (.whl)](best-practices-dependencies.md#best-practices-dependencies-python-wheels "best-practices-dependencies.md#best-practices-dependencies-python-wheels")
    - [Using the plugins.zip file on an Amazon S3 bucket](best-practices-dependencies.md#best-practices-dependencies-python-wheels-s3 "best-practices-dependencies.md#best-practices-dependencies-python-wheels-s3")
    - [Using a WHL file hosted on a URL](best-practices-dependencies.md#best-practices-dependencies-python-wheels-url "best-practices-dependencies.md#best-practices-dependencies-python-wheels-url")
    - [Creating a WHL files from a DAG](best-practices-dependencies.md#best-practices-dependencies-python-wheels-dag "best-practices-dependencies.md#best-practices-dependencies-python-wheels-dag")

  - [Option three: Python dependencies hosted on a private PyPi/PEP-503 Compliant Repo](best-practices-dependencies.md#best-practices-dependencies-custom-auth-url "best-practices-dependencies.md#best-practices-dependencies-custom-auth-url")

- [Enabling logs on the Amazon MWAA console](best-practices-dependencies.md#best-practices-dependencies-troubleshooting-enable "best-practices-dependencies.md#best-practices-dependencies-troubleshooting-enable")
- [Accessing logs on the CloudWatch Logs console](best-practices-dependencies.md#best-practices-dependencies-troubleshooting-view "best-practices-dependencies.md#best-practices-dependencies-troubleshooting-view")
- [Accessing errors in the Apache Airflow UI](best-practices-dependencies.md#best-practices-dependencies-troubleshooting-aa "best-practices-dependencies.md#best-practices-dependencies-troubleshooting-aa")
  - [Log in to Apache Airflow](best-practices-dependencies.md#airflow-access-and-login "best-practices-dependencies.md#airflow-access-and-login")

- [Example requirements.txt scenarios](best-practices-dependencies.md#best-practices-dependencies-ex-mix-match "best-practices-dependencies.md#best-practices-dependencies-ex-mix-match")

## Testing DAGs using the Amazon MWAA CLI utility

- The command line interface (CLI) utility replicates an Amazon Managed Workflows for Apache Airflow environment locally.
- The CLI builds a Docker container image locally that’s similar to an Amazon MWAA production image. You can use this to run a local Apache Airflow environment to develop and test DAGs, custom plugins, and dependencies before deploying to Amazon MWAA.
- To run the CLI, refer to [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") on GitHub.

## Installing Python dependencies using PyPi.org Requirements File Format

The following section describes the different ways to install Python dependencies according to the PyPi.org [Requirements File Format](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format "https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format").

### Option one: Python dependencies from the Python Package Index

The following section describes how to specify Python dependencies from the [Python Package Index](https://pypi.org/ "https://pypi.org/") in a `requirements.txt` file.

Apache Airflow v3

1. **Test locally**. Add additional libraries iteratively to find the right combination of packages and their versions, before creating a `requirements.txt` file. To run the Amazon MWAA CLI utility, refer to [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") on GitHub.
2. **Review the Apache Airflow package extras**. To access a list of the packages installed for Apache Airflow v3 on Amazon MWAA, refer to [aws-mwaa-docker-images `requirements.txt`](https://github.com/aws/amazon-mwaa-docker-images/blob/main/requirements.txt "https://github.com/aws/amazon-mwaa-docker-images/blob/main/requirements.txt") on the GitHub website.
3. **Add a constraints statement**. Add the constraints file for your Apache Airflow v3 environment at the top of your `requirements.txt` file. Apache Airflow constraints files specify the provider versions available at the time of a Apache Airflow release.

In the following example, replace `{environment-version}` with your environment's version number, and `{Python-version}` with the version of Python that's compatible with your environment.

For information about the version of Python compatible with your Apache Airflow environment, refer to [Apache Airflow Versions](airflow-versions.md#airflow-versions-official "airflow-versions.md#airflow-versions-official").

```
--constraint "https://raw.githubusercontent.com/apache/airflow/constraints-`{Airflow-version}`/constraints-`{Python-version}`.txt"
```

If the constraints file determines that `xyz==1.0` package is not compatible with other packages in your environment, `pip3 install` fails to
prevent incompatible libraries from being installed to your environment. If installation fails for any packages, you can access error logs for each Apache Airflow component (the scheduler, worker, and webserver) in the corresponding log stream on CloudWatch Logs. For more information about log types, refer to [Accessing Airflow logs in Amazon CloudWatch](monitoring-airflow.md "monitoring-airflow.md"). 4. **Apache Airflow packages**. Add the [package extras](http://airflow.apache.org/docs/apache-airflow/2.5.1/extra-packages-ref.html "http://airflow.apache.org/docs/apache-airflow/2.5.1/extra-packages-ref.html") and the version (`==`). This helps to prevent packages of the same name, but different version, from being installed on your environment.

```
apache-airflow[`package-extra`]==2.5.1
```

5. **Python libraries**. Add the package name and the version (`==`) in your `requirements.txt` file. This helps to prevent a future breaking update from [PyPi.org](https://pypi.org "https://pypi.org") from being automatically applied.

```
`library` == `version`
```

###### Example Boto3 and psycopg2-binary

This example is provided for demonstration purposes. The boto and psycopg2-binary libraries are included with the base install for Apache Airflow v3 and don't need to be specified in a `requirements.txt` file.

```
boto3==1.17.54
boto==2.49.0
botocore==1.20.54
psycopg2-binary==2.8.6
```

If a package is specified without a version, Amazon MWAA installs the latest version of the package from [PyPi.org](https://pypi.org "https://pypi.org"). This version can conflict with other packages in your `requirements.txt`.

Apache Airflow v2

1. **Test locally**. Add additional libraries iteratively to find the right combination of packages and their versions, before creating a `requirements.txt` file. To run the Amazon MWAA CLI utility, refer to [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") on GitHub.
2. **Review the Apache Airflow package extras**. To access a list of the packages installed for Apache Airflow v2 on Amazon MWAA, access
   [aws-mwaa-docker-images `requirements.txt`](https://github.com/aws/amazon-mwaa-docker-images/blob/main/requirements.txt "https://github.com/aws/amazon-mwaa-docker-images/blob/main/requirements.txt")
   on the GitHub website.
3. **Add a constraints statement**. Add the constraints file for your Apache Airflow v2 environment at the top of your
   `requirements.txt` file. Apache Airflow constraints files specify the provider versions available at the time of a Apache Airflow release.

Beginning with Apache Airflow v2.7.2, your requirements file must include a `--constraint` statement. If you do not provide a constraint, Amazon MWAA will specify
one for you to ensure the packages listed in your requirements are compatible with the version of Apache Airflow you are using.

In the following example, replace `{environment-version}` with your environment's version number, and `{Python-version}`
with the version of Python that's compatible with your environment.

For information about the version of Python compatible with your Apache Airflow environment, refer to [Apache Airflow Versions](airflow-versions.md#airflow-versions-official "airflow-versions.md#airflow-versions-official").

```
--constraint "https://raw.githubusercontent.com/apache/airflow/constraints-`{Airflow-version}`/constraints-`{Python-version}`.txt"
```

If the constraints file determines that `xyz==1.0` package is
not compatible with other packages in your environment, `pip3
 install` fails to prevent incompatible libraries
from being installed to your environment. If installation fails for any
packages, you can access error logs for each Apache Airflow component (the
scheduler, worker, and webserver) in the corresponding log stream on
CloudWatch Logs. For more information about log types, refer to [Accessing Airflow logs in Amazon CloudWatch](monitoring-airflow.md "monitoring-airflow.md"). 4. **Apache Airflow packages**. Add the [package extras](http://airflow.apache.org/docs/apache-airflow/2.5.1/extra-packages-ref.html "http://airflow.apache.org/docs/apache-airflow/2.5.1/extra-packages-ref.html")
and the version (`==`). This helps to prevent packages of the same name, but different version, from being installed on your environment.

```
apache-airflow[`package-extra`]==2.5.1
```

5. **Python libraries**. Add the package name and the version (`==`) in your `requirements.txt` file. This helps to prevent a future breaking update from [PyPi.org](https://pypi.org "https://pypi.org") from being automatically applied.

```
`library` == `version`
```

###### Example Boto3 and psycopg2-binary

This example is provided for demonstration purposes. The boto and psycopg2-binary libraries are included with the Apache Airflow v2 base install and don't need to be specified in a `requirements.txt` file.

```
boto3==1.17.54
boto==2.49.0
botocore==1.20.54
psycopg2-binary==2.8.6
```

If a package is specified without a version, Amazon MWAA installs the latest version of the package from [PyPi.org](https://pypi.org "https://pypi.org"). This version can conflict with other packages in your `requirements.txt`.

### Option two: Python wheels (.whl)

A Python wheel is a package format designed to ship libraries with compiled artifacts. There are several benefits to wheel packages as a method to install dependencies in Amazon MWAA:

- **Faster installation** – the WHL files are copied to the container as a single ZIP, and then installed locally, without having to download each one.
- **Fewer conflicts** – You can determine version compatibility for your packages in advance. As a result, there is no need for
  `pip` to recursively work out compatible versions.
- **More resilience** – With externally hosted libraries, downstream requirements can change, resulting in version incompatibility between containers on a Amazon MWAA environment.
  By not depending on an external source for dependencies, every container on has have the same libraries regardless of when the each container is instantiated.

We recommend the following methods to install Python dependencies from a Python wheel archive (`.whl`)
in your `requirements.txt`.

###### Methods

- [Using the plugins.zip file on an Amazon S3 bucket](#best-practices-dependencies-python-wheels-s3 "#best-practices-dependencies-python-wheels-s3")
- [Using a WHL file hosted on a URL](#best-practices-dependencies-python-wheels-url "#best-practices-dependencies-python-wheels-url")
- [Creating a WHL files from a DAG](#best-practices-dependencies-python-wheels-dag "#best-practices-dependencies-python-wheels-dag")

#### Using the `plugins.zip` file on an Amazon S3 bucket

The Apache Airflow scheduler, workers, and webserver (for Apache Airflow v2.2.2 and later) search for custom plugins during startup on the AWS-managed Fargate container for your environment at
`/usr/local/airflow/plugins/`\*``. This process begins prior to Amazon MWAA's `pip3 install -r requirements.txt`for Python dependencies and Apache Airflow service startup.
 A`plugins.zip` file can be used for any files that you don't want continuously changed during environment execution, or that you do not want to grant access to users that write DAGs.
For example, Python library wheel files, certificate PEM files, and configuration YAML files.

The following section describes how to install a wheel that's in the `plugins.zip` file on your Amazon S3 bucket.

1. **Download the necessary WHL files** You can use [`pip download`](https://pip.pypa.io/en/stable/cli/pip_download/ "https://pip.pypa.io/en/stable/cli/pip_download/") with your existing
   `requirements.txt` on the Amazon MWAA [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") or another [Amazon Linux 2](https://aws.amazon.com/amazon-linux-2 "https://aws.amazon.com/amazon-linux-2")
   container to resolve and download the necessary Python wheel files.

```
`pip3 download -r "$AIRFLOW_HOME/dags/requirements.txt" -d "$AIRFLOW_HOME/plugins"`
`cd "`$AIRFLOW_HOME`/plugins"`
`zip "`$AIRFLOW_HOME`/plugins.zip" *`
```

2. **Specify the path in your `requirements.txt`**. Specify the plugins directory at the top of your requirements.txt using
   [`--find-links`](https://pip.pypa.io/en/stable/cli/pip_install/#install-find-links "https://pip.pypa.io/en/stable/cli/pip_install/#install-find-links") and instruct `pip` not to install from other sources using
   [`--no-index`](https://pip.pypa.io/en/stable/cli/pip_install/#install-no-index "https://pip.pypa.io/en/stable/cli/pip_install/#install-no-index"), as listed in the following code:

```
--find-links /usr/local/airflow/plugins
--no-index

```

###### Example wheel in requirements.txt

The following example assumes you've uploaded the wheel in a `plugins.zip` file at the root of your Amazon S3 bucket. For example:

```
--find-links /usr/local/airflow/plugins
--no-index

numpy
```

Amazon MWAA fetches the `numpy-1.20.1-cp37-cp37m-manylinux1_x86_64.whl` wheel from the `plugins` folder and installs it on your environment.

#### Using a WHL file hosted on a URL

The following section describes how to install a wheel that's hosted on a URL. The URL must either be publicly accessible, or accessible from within the custom Amazon VPC you specified for your Amazon MWAA environment.

- **Provide a URL**. Provide the URL to a wheel in your `requirements.txt`.

###### Example wheel archive on a public URL

The following example downloads a wheel from a public site.

```
--find-links https://files.pythonhosted.org/packages/
--no-index
```

Amazon MWAA fetches the wheel from the URL you specified and installs them on your environment.

###### Note

URLs are not accessible from private webservers installing requirements in Amazon MWAA v2.2.2 and later.

#### Creating a WHL files from a DAG

If you have a private webserver using Apache Airflow v2.2.2 or later and you're unable to install requirements because your environment does not have access to external repositories, you
can use the following DAG to take your existing Amazon MWAA requirements and package them on Amazon S3:

```
from airflow import DAG
 from airflow.operators.bash_operator import BashOperator
 from airflow.utils.dates import days_ago

 S3_BUCKET = 'my-s3-bucket'
 S3_KEY = 'backup/plugins_whl.zip'

 with DAG(dag_id="create_whl_file", schedule_interval=None, catchup=False, start_date=days_ago(1)) as dag:
 cli_command = BashOperator(
 task_id="bash_command",
 bash_command=f"mkdir /tmp/whls;pip3 download -r /usr/local/airflow/requirements/requirements.txt -d /tmp/whls;zip -j /tmp/plugins.zip /tmp/whls/*;aws s3 cp /tmp/plugins.zip s3://`amzn-s3-demo-bucket`/`{S3_KEY}`"
)
```

After running the DAG, use this new file as your Amazon MWAA `plugins.zip`, optionally, packaged with other plugins. Then, update your `requirements.txt` preceded by
`--find-links /usr/local/airflow/plugins` and `--no-index` without adding `--constraint`.

This method you can use to use the same libraries offline.

### Option three: Python dependencies hosted on a private PyPi/PEP-503 Compliant Repo

The following section describes how to install an Apache Airflow extra that's hosted on a private URL with authentication.

1. Add your user name and password as [Apache Airflow configuration options](configuring-env-variables.md "configuring-env-variables.md"). For example:
   - `foo.user` : `YOUR_USER_NAME`
   - `foo.pass` : `YOUR_PASSWORD`

2. Create your `requirements.txt` file. Substitute the placeholders in the following example with your private URL, and the username and password you've added as [Apache Airflow configuration options](configuring-env-variables.md "configuring-env-variables.md"). For example:

```
--index-url https://${AIRFLOW__FOO__USER}:${AIRFLOW__FOO__PASS}@my.privatepypi.com
```

3. Add any additional libraries to your `requirements.txt` file. For example:

```
--index-url https://${AIRFLOW__FOO__USER}:${AIRFLOW__FOO__PASS}@my.privatepypi.com
my-private-package==1.2.3
```

## Enabling logs on the Amazon MWAA console

The [execution role](mwaa-create-role.md "mwaa-create-role.md") for your Amazon MWAA environment needs permission to send logs to CloudWatch Logs. To update the permissions of an execution role, refer to [Amazon MWAA execution role](mwaa-create-role.md "mwaa-create-role.md").

You can enable Apache Airflow logs at the `INFO`, `WARNING`, `ERROR`, or `CRITICAL` level. When you choose a log level, Amazon MWAA sends logs for that level and all higher levels of severity. For example, if you enable logs at the `INFO` level, Amazon MWAA sends `INFO` logs and `WARNING`, `ERROR`, and `CRITICAL` log levels to CloudWatch Logs. We recommend enabling Apache Airflow logs at the `INFO` level for the scheduler to access logs received for the `requirements.txt`.

![This image depicts how to enable logs at the INFO level.](images/mwaa-console-logs-info.png)

## Accessing logs on the CloudWatch Logs console

You can access Apache Airflow logs for the scheduler scheduling your workflows and parsing your `dags` folder. The following steps describe how to open the log group for the scheduler on the Amazon MWAA console, and access Apache Airflow logs on the CloudWatch Logs console.

###### To access logs for a `requirements.txt`

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. Choose the **Airflow scheduler log group** on the **Monitoring** pane.
4. Choose the `requirements_install_ip` log in **Log streams**.
5. Refer to the list of packages that were installed on the environment at `/usr/local/airflow/.local/bin`. For example:

```
Collecting appdirs==1.4.4 (from -r /usr/local/airflow/.local/bin (line 1))
Downloading https://files.pythonhosted.org/packages/3b/00/2344469e2084fb28kjdsfiuyweb47389789vxbmnbjhsdgf5463acd6cf5e3db69324/appdirs-1.4.4-py2.py3-none-any.whl
Collecting astroid==2.4.2 (from -r /usr/local/airflow/.local/bin (line 2))
```

6. Review the list of packages and whether any of these encountered an error during installation. If something went wrong, you can get an error similar to the following:

```
2021-03-05T14:34:42.731-07:00
No matching distribution found for LibraryName==1.0.0 (from -r /usr/local/airflow/.local/bin (line 4))
No matching distribution found for LibraryName==1.0.0 (from -r /usr/local/airflow/.local/bin (line 4))
```

## Accessing errors in the Apache Airflow UI

You can also check your Apache Airflow UI to identify whether an error is related to another issue. The most common error you can encounter with Apache Airflow on Amazon MWAA is:

```
Broken DAG: No module named `x`
```

If you find this error in your Apache Airflow UI, you're likely missing a required dependency in your `requirements.txt` file.

### Log in to Apache Airflow

You need [Apache Airflow UI access policy: AmazonMWAAWebServerAccess](access-policies.md#web-ui-access "access-policies.md#web-ui-access") permissions for your AWS account in AWS Identity and Access Management (IAM) to access your Apache Airflow UI.

###### To access your Apache Airflow UI

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. Choose **Open Airflow UI**.

## Example `requirements.txt` scenarios

You can mix and match different formats in your `requirements.txt`. The following example uses a combination of the different ways to install extras.

###### Example Extras on PyPi.org and a public URL

You need to use the `--index-url` option when specifying packages from PyPi.org, in addition to packages on a public URL, such as custom PEP 503 compliant repo URLs.

```
aws-batch == 0.6
				phoenix-letter >= 0.3

				--index-url http://dist.repoze.org/zope2/2.10/simple
				zopelib
```
