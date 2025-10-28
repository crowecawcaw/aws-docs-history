# Installing Python dependencies

A Python dependency is any package or distribution not included in the Apache Airflow base install for your Apache Airflow version on your Amazon Managed Workflows for Apache Airflow environment.
This topic describes the steps to install Apache Airflow Python dependencies on your Amazon MWAA environment using a `requirements.txt` file in your Amazon S3 bucket.

###### Contents

- [Prerequisites](working-dags-dependencies.md#working-dags-dependencies-prereqs "working-dags-dependencies.md#working-dags-dependencies-prereqs")
- [How it works](working-dags-dependencies.md#working-dags-dependencies-how "working-dags-dependencies.md#working-dags-dependencies-how")
- [Python dependencies overview](working-dags-dependencies.md#working-dags-dependencies-overview "working-dags-dependencies.md#working-dags-dependencies-overview")
  - [Python dependencies location and size limits](working-dags-dependencies.md#working-dags-dependencies-quota "working-dags-dependencies.md#working-dags-dependencies-quota")

- [Creating a requirements.txt file](working-dags-dependencies.md#working-dags-dependencies-test-create "working-dags-dependencies.md#working-dags-dependencies-test-create")
  - [Step one: Test Python dependencies using the Amazon MWAA CLI utility](working-dags-dependencies.md#working-dags-dependencies-cli-utility "working-dags-dependencies.md#working-dags-dependencies-cli-utility")
  - [Step two: Create the requirements.txt](working-dags-dependencies.md#working-dags-dependencies-syntax-create "working-dags-dependencies.md#working-dags-dependencies-syntax-create")

- [Uploading requirements.txt to Amazon S3](working-dags-dependencies.md#configuring-dag-dependencies-upload "working-dags-dependencies.md#configuring-dag-dependencies-upload")
  - [Using the AWS CLI](working-dags-dependencies.md#configuring-dag-dependencies-upload-cli "working-dags-dependencies.md#configuring-dag-dependencies-upload-cli")
  - [Using the Amazon S3 console](working-dags-dependencies.md#configuring-dag-dependencies-upload-console "working-dags-dependencies.md#configuring-dag-dependencies-upload-console")

- [Installing Python dependencies on your environment](working-dags-dependencies.md#configuring-dag-dependencies-installing "working-dags-dependencies.md#configuring-dag-dependencies-installing")
  - [Specifying the path to requirements.txt on the Amazon MWAA console (the first time)](working-dags-dependencies.md#configuring-dag-dependencies-first "working-dags-dependencies.md#configuring-dag-dependencies-first")
  - [Specifying the requirements.txt version on the Amazon MWAA console](working-dags-dependencies.md#working-dags-dependencies-mwaaconsole-version "working-dags-dependencies.md#working-dags-dependencies-mwaaconsole-version")

- [Accessing logs for your requirements.txt](working-dags-dependencies.md#working-dags-dependencies-logs "working-dags-dependencies.md#working-dags-dependencies-logs")
- [What's next?](working-dags-dependencies.md#working-dags-dependencies-next-up "working-dags-dependencies.md#working-dags-dependencies-next-up")

## Prerequisites

You'll need the following before you can complete the steps on this page.

- **Permissions** — Your AWS account must have been granted access by your administrator to the [AmazonMWAAFullConsoleAccess](access-policies.md#console-full-access "access-policies.md#console-full-access")
  access control policy for your environment. In addition, your Amazon MWAA environment must be permitted by your [execution role](mwaa-create-role.md "mwaa-create-role.md") to access the AWS resources used by your environment.
- **Access** — If you require access to public repositories to install dependencies directly on the webserver, your environment must be configured with
  **public network** webserver access. For more information, refer to [Apache Airflow access modes](configuring-networking.md "configuring-networking.md").
- **Amazon S3 configuration** — The [Amazon S3 bucket](mwaa-s3-bucket.md "mwaa-s3-bucket.md") used to store your DAGs, custom plugins in `plugins.zip`,
  and Python dependencies in `requirements.txt` must be configured with _Public Access Blocked_ and _Versioning Enabled_.

## How it works

On Amazon MWAA, you install all Python dependencies by uploading a `requirements.txt` file to your Amazon S3 bucket, then specifying the version of the file on the Amazon MWAA console each time you update the file. Amazon MWAA runs `pip3 install -r requirements.txt` to install the Python dependencies on the Apache Airflow scheduler and each of the workers.

To run Python dependencies on your environment, you must do three things:

1. Create a `requirements.txt` file locally.
2. Upload the local `requirements.txt` to your Amazon S3 bucket.
3. Specify the version of this file in the **Requirements file** field on the Amazon MWAA console.

###### Note

If this is the first time you're creating and uploading a `requirements.txt` to your Amazon S3 bucket, you also need to specify the path to the file on the Amazon MWAA console. You only need to complete this step once.

## Python dependencies overview

You can install Apache Airflow extras and other Python dependencies from the Python Package Index (PyPi.org), Python wheels (`.whl`), or Python dependencies hosted on a private PyPi/PEP-503 Compliant Repo on your environment.

### Python dependencies location and size limits

The Apache Airflow scheduler and the workers search for
the packages in the `requirements.txt` file and the packages are
installed on the environment at `/usr/local/airflow/.local/bin`.

- **Size limit**. We recommend a `requirements.txt` file that references libraries whose combined size is less than than 1 GB. The more libraries Amazon MWAA needs to install, the longer the _startup_ time on an environment. Although Amazon MWAA doesn't limit the size of installed libraries explicitly, if dependencies can't be installed within ten minutes, the Fargate service will time-out and attempt to rollback the environment to a stable state.

## Creating a requirements.txt file

The following steps describe the steps we recommend to create a requirements.txt file locally.

### Step one: Test Python dependencies using the Amazon MWAA CLI utility

- The command line interface (CLI) utility replicates an Amazon Managed Workflows for Apache Airflow environment locally.
- The CLI builds a Docker container image locally that’s similar to an Amazon MWAA production image. You can use this to run a local Apache Airflow environment to develop and test DAGs, custom plugins, and dependencies before deploying to Amazon MWAA.
- To run the CLI, refer to [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") on GitHub.

### Step two: Create the `requirements.txt`

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

If the constraints file determines that `xyz==1.0` package is not compatible with other packages in your environment, `pip3 install` will fail to
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

If a package is specified without a version, Amazon MWAA installs the latest version of the package from [PyPi.org](https://pypi.org "https://pypi.org"). This version might conflict with other packages in your `requirements.txt`.

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
 install` will fail to prevent incompatible libraries
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

If a package is specified without a version, Amazon MWAA installs the latest version of the package from [PyPi.org](https://pypi.org "https://pypi.org"). This version might conflict with other packages in your `requirements.txt`.

## Uploading `requirements.txt` to Amazon S3

You can use the Amazon S3 console or the AWS Command Line Interface (AWS CLI) to upload a `requirements.txt` file to your Amazon S3 bucket.

### Using the AWS CLI

The AWS Command Line Interface (AWS CLI) is an open source tool that you can use to interact with AWS services using commands in your command-line shell. To complete the steps on this page, you need the following:

- [AWS CLI – Install version 2](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md").
- [AWS CLI – Quick configuration with `aws configure`](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").

###### To upload using the AWS CLI

1. Use the following command to list all of your Amazon S3 buckets.

```
aws s3 ls
```

2. Use the following command to list the files and folders in the Amazon S3 bucket for your environment.

```
aws s3 ls s3://`YOUR_S3_BUCKET_NAME`
```

3. The following command uploads a `requirements.txt` file to an Amazon S3 bucket.

```
aws s3 cp requirements.txt s3://`amzn-s3-demo-bucket`/requirements.txt
```

### Using the Amazon S3 console

The Amazon S3 console is a web-based user interface that you can use to create and manage the resources in your Amazon S3 bucket.

###### To upload using the Amazon S3 console

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. Select the **S3 bucket** link in the **DAG code in S3** pane to open your storage bucket in the console.
4. Choose **Upload**.
5. Choose **Add file**.
6. Select the local copy of your `requirements.txt`, choose **Upload**.

## Installing Python dependencies on your environment

This section describes how to install the dependencies you uploaded to your Amazon S3 bucket by specifying the path to the requirements.txt file, and specifying the version of the requirements.txt file each time it's updated.

### Specifying the path to `requirements.txt` on the Amazon MWAA console (the first time)

If this is the first time you're creating and uploading a `requirements.txt` to your Amazon S3 bucket, you also need to specify the path to the file on the Amazon MWAA console. You only need to complete this step once.

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. Choose **Edit**.
4. On the **DAG code in Amazon S3** pane, choose **Browse S3** adjacent to the **Requirements file - optional** field.
5. Select the `requirements.txt` file on your Amazon S3 bucket.
6. Choose **Choose**.
7. Choose **Next**, **Update environment**.

You can begin using the new packages immediately after your environment finishes updating.

### Specifying the `requirements.txt` version on the Amazon MWAA console

You need to specify the version of your `requirements.txt` file on the Amazon MWAA console each time you upload a new version of your `requirements.txt` in your Amazon S3 bucket.

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. Choose **Edit**.
4. On the **DAG code in Amazon S3** pane, choose a `requirements.txt` version in the dropdown list.
5. Choose **Next**, **Update environment**.

You can begin using the new packages immediately after your environment finishes updating.

## Accessing logs for your `requirements.txt`

You can view Apache Airflow logs for the scheduler scheduling your workflows and parsing your `dags` folder. The following steps describe how to open the log group for the scheduler on the Amazon MWAA console, and access Apache Airflow logs on the CloudWatch Logs console.

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

6. Review the list of packages and whether any of these encountered an error during installation. If something went wrong, you get an error similar to the following:

```
2021-03-05T14:34:42.731-07:00
No matching distribution found for LibraryName==1.0.0 (from -r /usr/local/airflow/.local/bin (line 4))
No matching distribution found for LibraryName==1.0.0 (from -r /usr/local/airflow/.local/bin (line 4))
```

## What's next?

Test your DAGs, custom plugins, and Python dependencies locally using [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") on GitHub.
