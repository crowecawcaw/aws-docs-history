

# Adding or updating DAGs
<a name="configuring-dag-folder"></a>

Directed Acyclic Graphs (DAGs) are defined within a Python file that defines the DAG's structure as code. You can use the AWS CLI or the Amazon S3 console to upload DAGs to your environment. This topic describes the steps to add or update Apache Airflow DAGs on your Amazon Managed Workflows for Apache Airflow environment using the `dags` folder in your Amazon S3 bucket.

**Topics**
+ [Prerequisites](#configuring-dag-folder-prereqs)
+ [How it works](#configuring-dag-folder-how)
+ [What's changed?](#configuring-dag-folder-changed)
+ [Testing DAGs using the Amazon MWAA CLI utility](#working-dag-folder-cli-utility)
+ [Uploading DAG code to Amazon S3](#configuring-dag-folder-uploading)
+ [Specifying the path to your DAGs folder on the Amazon MWAA console (the first time)](#configuring-dag-folder-mwaaconsole)
+ [Accessing changes on your Apache Airflow UI](#configuring-dag-folder-mwaaconsole-view)
+ [What's next?](#configuring-dag-folder-next-up)

## Prerequisites
<a name="configuring-dag-folder-prereqs"></a>

You'll need the following before you can complete the steps on this page.
+ **Permissions** — Your AWS account must have been granted access by your administrator to the [AmazonMWAAFullConsoleAccess](access-policies.md#console-full-access) access control policy for your environment. In addition, your Amazon MWAA environment must be permitted by your [execution role](mwaa-create-role.md) to access the AWS resources used by your environment.
+ **Access** — If you require access to public repositories to install dependencies directly on the webserver, your environment must be configured with **public network** webserver access. For more information, refer to [Apache Airflow access modes](configuring-networking.md).
+ **Amazon S3 configuration** — The [Amazon S3 bucket](mwaa-s3-bucket.md) used to store your DAGs, custom plugins in `plugins.zip`, and Python dependencies in `requirements.txt` must be configured with *Public Access Blocked* and *Versioning Enabled*.

## How it works
<a name="configuring-dag-folder-how"></a>

A Directed Acyclic Graph (DAG) is defined within a single Python file that defines the DAG's structure as code. It consists of the following:
+ A [DAG](https://airflow.apache.org/docs/stable/concepts.html#dags) definition.
+ [Operators](https://airflow.apache.org/concepts.html#operators) that describe how to run the DAG and the [tasks](https://airflow.apache.org/docs/stable/concepts.html#tasks) to run.
+ [Operator relationships](https://airflow.apache.org/concepts.html#bitshift-composition) that describe the order in which to run the tasks.

To run an Apache Airflow platform on an Amazon MWAA environment, you need to copy your DAG definition to the `dags` folder in your storage bucket. For example, the DAG folder in your storage bucket should resemble:

**Example DAG folder**  

```
dags/
└ dag_def.py
```

Amazon MWAA automatically syncs new and changed objects from your Amazon S3 bucket to Amazon MWAA scheduler and worker containers’ `/usr/local/airflow/dags` folder every 30 seconds, preserving the Amazon S3 source’s file hierarchy, regardless of file type. The time that new DAGs take to be listed in your Apache Airflow UI is controlled by `scheduler.dag\_dir\_list\_interval`. Changes to existing DAGs will be picked up on the next [DAG processing loop](best-practices-tuning.md#best-practices-tuning-scheduler).

**Note**  
You do not need to include the `airflow.cfg` configuration file in your DAG folder. You can override the default Apache Airflow configurations from the Amazon MWAA console. For more information, refer to [Using Apache Airflow configuration options on Amazon MWAA](configuring-env-variables.md).

## What's changed?
<a name="configuring-dag-folder-changed"></a>

To review changes for a specific Apache Airflow release, refer to the [Release Notes](https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html#release-notes) page.
+ Apache Airflow v3 configurations: [Configuration Reference](https://airflow.apache.org/docs/apache-airflow/3.0.6/configurations-ref.html)
+ Apache Airflow v2 public interface information: [Public Interface of Airflow](https://airflow.apache.org/docs/apache-airflow/2.10.3/public-airflow-interface.html)

## Testing DAGs using the Amazon MWAA CLI utility
<a name="working-dag-folder-cli-utility"></a>
+ The command line interface (CLI) utility replicates an Amazon Managed Workflows for Apache Airflow environment locally.
+ The CLI builds a Docker container image locally that’s similar to an Amazon MWAA production image. You can use this to run a local Apache Airflow environment to develop and test DAGs, custom plugins, and dependencies before deploying to Amazon MWAA.
+ To run the CLI, refer to [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images) on GitHub.

## Uploading DAG code to Amazon S3
<a name="configuring-dag-folder-uploading"></a>

You can use the Amazon S3 console or the AWS Command Line Interface (AWS CLI) to upload DAG code to your Amazon S3 bucket. The following steps assume you are uploading code (`.py`) to a folder named `dags` in your Amazon S3 bucket.

### Using the AWS CLI
<a name="configuring-dag-folder-cli"></a>

The AWS Command Line Interface (AWS CLI) is an open source tool that you can use to interact with AWS services using commands in your command-line shell. To complete the steps on this page, you need the following:
+ [AWS CLI – Install version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
+ [AWS CLI – Quick configuration with `aws configure`](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).

**To upload using the AWS CLI**

1. Use the following command to list all of your Amazon S3 buckets.

   ```
   aws s3 ls
   ```

1. Use the following command to list the files and folders in the Amazon S3 bucket for your environment.

   ```
   aws s3 ls s3://{{YOUR_S3_BUCKET_NAME}}
   ```

1. The following command uploads a `dag_def.py` file to a `dags` folder. 

   ```
   aws s3 cp dag_def.py s3://{{amzn-s3-demo-bucket}}/dags/
   ```

   If a folder named `dags` does not already exist on your Amazon S3 bucket, this command creates the `dags` folder and uploads the file named `dag_def.py` to the new folder.

### Using the Amazon S3 console
<a name="configuring-dag-folder-console"></a>

The Amazon S3 console is a web-based user interface that you can use to create and manage the resources in your Amazon S3 bucket. The following steps assume you have a DAGs folder named `dags`.

**To upload using the Amazon S3 console**

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments) page on the Amazon MWAA console.

1. Choose an environment.

1. Select the **S3 bucket** link in the **DAG code in S3** pane to open your storage bucket in the console.

1. Choose the `dags` folder.

1. Choose **Upload**.

1. Choose **Add file**.

1. Select the local copy of your `dag_def.py`, choose **Upload**.

## Specifying the path to your DAGs folder on the Amazon MWAA console (the first time)
<a name="configuring-dag-folder-mwaaconsole"></a>

The following steps assume you are specifying the path to a folder on your Amazon S3 bucket named `dags`.

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments) page on the Amazon MWAA console.

1. Choose the environment where you want to run DAGs.

1. Choose **Edit**.

1. On the **DAG code in Amazon S3** pane, choose **Browse S3** adjacent to the **DAG folder** field.

1. Select your `dags` folder.

1. Choose **Choose**.

1. Choose **Next**, **Update environment**.

## Accessing changes on your Apache Airflow UI
<a name="configuring-dag-folder-mwaaconsole-view"></a>

You need [Apache Airflow UI access policy: AmazonMWAAWebServerAccess](access-policies.md#web-ui-access) permissions for your AWS account in AWS Identity and Access Management (IAM) to access your Apache Airflow UI.

**To access your Apache Airflow UI**

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments) page on the Amazon MWAA console.

1. Choose an environment.

1. Choose **Open Airflow UI**.

## What's next?
<a name="configuring-dag-folder-next-up"></a>

Test your DAGs, custom plugins, and Python dependencies locally using [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images) on GitHub.