# Create an Amazon MWAA environment

Amazon Managed Workflows for Apache Airflow sets up Apache Airflow on an environment in your chosen version using the same open-source Apache Airflow and user interface available from Apache.
This guide describes the steps to create an Amazon MWAA environment.

###### Contents

- [Before you begin](create-environment.md#create-environment-before "create-environment.md#create-environment-before")
- [Apache Airflow versions](create-environment.md#create-environment-regions-aa-versions "create-environment.md#create-environment-regions-aa-versions")
- [Create an environment](create-environment.md#create-environment-start "create-environment.md#create-environment-start")
  - [Step one: Specify details](create-environment.md#create-environment-start-details "create-environment.md#create-environment-start-details")
  - [Step two: Configure advanced settings](create-environment.md#create-environment-start-advanced "create-environment.md#create-environment-start-advanced")
  - [Step three: Review and create](create-environment.md#create-environment-start-review "create-environment.md#create-environment-start-review")

## Before you begin

- The [VPC network](vpc-create.md "vpc-create.md") you specify for your environment cannot be modified after the environment is created.
- You need an Amazon S3 bucket configured to **Block all public access**, with **Bucket Versioning** enabled.
- You need an AWS account with [permissions to use Amazon MWAA](manage-access.md "manage-access.md"), and permission in AWS Identity and Access Management (IAM) to create IAM roles.
  If you choose the **Private network** access mode for the Apache Airflow webserver, which limits Apache Airflow access
  within your Amazon VPC, you'll need permission in IAM to create Amazon VPC endpoints.

###### Note

Amazon MWAA dynamically determines the network during creation. If you use IPv6 subnets, Amazon MWAA creates IPv6 private link connectivity to the database and webserver. Amazon MWAA does not support transitioning between network types and cannot upgrade existing environments to IPv6.

## Apache Airflow versions

The following Apache Airflow versions are supported on Amazon Managed Workflows for Apache Airflow.

###### Note

- Effective December 30, 2025, Amazon MWAA will end support for Apache Airflow versions v2.4.3, v2.5.1,
  and v2.6.3. For more information, refer to [Apache Airflow version support and FAQ](airflow-versions.md#airflow-versions-support "airflow-versions.md#airflow-versions-support").
- Beginning with Apache Airflow v2.2.2, Amazon MWAA supports installing Python requirements, provider
  packages, and custom plugins directly on the Apache Airflow webserver.
- Beginning with Apache Airflow v2.7.2, your requirements file must include a `--constraint` statement. If you don't provide a constraint, Amazon MWAA will specify
  one for you to ensure the packages listed in your requirements are compatible with the version of Apache Airflow you're using.

For more information about setting up constraints in your requirements file, refer to
[Installing Python dependencies](working-dags-dependencies.md#working-dags-dependencies-syntax-create "working-dags-dependencies.md#working-dags-dependencies-syntax-create").

| Apache Airflow version                                                                                                   | Apache Airflow release date                                                                                                                                                                                                  | Amazon MWAA availability date | Apache Airflow constraints                                                                                                                                                                                      | Python version                                                                       |
| ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [v3.0.6](https://airflow.apache.org/docs/apache-airflow/3.0.6 "https://airflow.apache.org/docs/apache-airflow/3.0.6")    | [August 29, 2025](https://airflow.apache.org/docs/apache-airflow/3.0.6/release_notes.html#airflow-3-0-6-2025-08-29 "https://airflow.apache.org/docs/apache-airflow/3.0.6/release_notes.html#airflow-3-0-6-2025-08-29")       | October 1, 2025               | [v3.0.6 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-3.0.6/constraints-3.12.txt "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.6/constraints-3.12.txt")    | [Python 3.12](https://peps.python.org/pep-0693/ "https://peps.python.org/pep-0693/") |
| [v2.10.3](https://airflow.apache.org/docs/apache-airflow/2.10.3 "https://airflow.apache.org/docs/apache-airflow/2.10.3") | [November 4, 2024](https://airflow.apache.org/docs/apache-airflow/2.10.3/release_notes.html#airflow-2-10-3-2024-11-04 "https://airflow.apache.org/docs/apache-airflow/2.10.3/release_notes.html#airflow-2-10-3-2024-11-04")  | December 18, 2024             | [v2.10.3 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.11.txt "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.11.txt") | [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/") |
| [v2.10.1](https://airflow.apache.org/docs/apache-airflow/2.10.1 "https://airflow.apache.org/docs/apache-airflow/2.10.1") | [September 5, 2024](https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-10-1-2024-09-05 "https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-10-1-2024-09-05") | September 26, 2024            | [v2.10.1 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.10.1/constraints-3.11.txt "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.1/constraints-3.11.txt") | [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/") |
| [v2.9.2](https://airflow.apache.org/docs/apache-airflow/2.9.2 "https://airflow.apache.org/docs/apache-airflow/2.9.2")    | [June 10, 2024](https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-9-2-2024-06-10 "https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-9-2-2024-06-10")       | July 9, 2024                  | [v2.9.2 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.9.2/constraints-3.11.txt "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.2/constraints-3.11.txt")    | [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/") |
| [v2.8.1](https://airflow.apache.org/docs/apache-airflow/2.8.1 "https://airflow.apache.org/docs/apache-airflow/2.8.1")    | [January 19, 2024](https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-8-1-2024-01-19 "https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-8-1-2024-01-19")    | February 23, 2024             | [v2.8.1 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.11.txt "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.11.txt")    | [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/") |
| [v2.7.2](https://airflow.apache.org/docs/apache-airflow/2.7.2 "https://airflow.apache.org/docs/apache-airflow/2.7.2")    | [October 12, 2023](https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-7-2-2023-10-12 "https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-7-2-2023-10-12")    | November 6, 2023              | [v2.7.2 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.7.2/constraints-3.11.txt "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.2/constraints-3.11.txt")    | [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/") |

For more information about migrating your self-managed Apache Airflow deployments, or migrating an existing Amazon MWAA environment, including instructions for backing up your metadata database, refer to the [Amazon MWAA Migration Guide](../migrationguide/index.md "../migrationguide/index.md").

## Create an environment

The following section describes the steps to create an Amazon MWAA environment.

### Step one: Specify details

###### To specify details for the environment

1. Open the [Amazon MWAA](https://console.aws.amazon.com/mwaa/home/ "https://console.aws.amazon.com/mwaa/home/") console.
2. Select your AWS Region.
3. Choose **Create environment**.
4. On the **Specify details** page, under **Environment details**:
   1. Enter a unique name for your environment in **Name**.
   2. Choose the Apache Airflow version in **Airflow version**.

   ###### Note

   If no value is specified, defaults to the latest Apache Airflow version. The latest available version is Apache Airflow v3.0.6.

5. Under **DAG code in Amazon S3** specify the following:
   1. **S3 Bucket**. Choose **Browse S3** and select your Amazon S3 bucket, or enter the Amazon S3 URI.
   2. **DAGs folder**. Choose **Browse S3** and select the `dags` folder in your Amazon S3 bucket, or enter the Amazon S3 URI.
   3. **Plugins file - _optional_**. Choose **Browse S3** and select the `plugins.zip` file on your Amazon S3 bucket, or enter the Amazon S3 URI.
   4. **Requirements file - _optional_**. Choose **Browse S3** and select the `requirements.txt` file on your Amazon S3 bucket, or enter the Amazon S3 URI.
   5. **Startup script file - _optional_**, Choose **Browse S3** and select the script file on your Amazon S3 bucket, or enter the Amazon S3 URI.

6. Choose **Next**.

### Step two: Configure advanced settings

###### To configure advanced settings

1. On the **Configure advanced settings** page, under **Networking**:
   1. Choose your [Amazon VPC](vpc-create.md "vpc-create.md").

   This step populates two of the private subnets in your Amazon VPC.

2. Under **webserver access**, select your preferred [Apache Airflow access mode](configuring-networking.md "configuring-networking.md"):
   1. **Private network**. This limits access of the Apache Airflow UI to users _within your Amazon VPC_ that have been granted access to the [IAM policy for your environment](access-policies.md "access-policies.md"). You need permission to create Amazon VPC endpoints for this step.

   ###### Note

   Choose the **Private network** option if your Apache Airflow UI is only accessed within a corporate network, and you do not require access to public repositories for webserver requirements installation.
   If you choose this access mode option, you need to create a mechanism to access your Apache Airflow webserver in your Amazon VPC. For more information, refer to
   [Accessing the VPC endpoint for your Apache Airflow webserver (private network access)](vpc-vpe-access.md#vpc-vpe-access-endpoints "vpc-vpe-access.md#vpc-vpe-access-endpoints"). 2. **Public network**. This allows the Apache Airflow UI to be accessed over the internet by users granted access to the [IAM policy for your environment](access-policies.md "access-policies.md").

3. Under **Security groups**, choose the security group used to secure your [Amazon VPC](vpc-create.md "vpc-create.md"):
   1. By default, Amazon MWAA creates a security group in your Amazon VPC with specific inbound and outbound rules in **Create new security group**.
   2. **Optional**. Deselect the check box in **Create new security group** to select up to 5 security groups.

   ###### Note

   An existing Amazon VPC security group must be configured with specific inbound and outbound rules to allow network traffic. To learn more, refer to [Security in your VPC on Amazon MWAA](vpc-security.md "vpc-security.md").

4. Under **Environment class**, choose an [environment class](environment-class.md "environment-class.md").

We recommend choosing the smallest size necessary to support your workload. You can change the environment class at any time. 5. For **Maximum worker count**, specify the maximum number of Apache Airflow workers to run in the environment.

For more information, refer to [Example high performance use case](mwaa-autoscaling.md#mwaa-autoscaling-high-volume "mwaa-autoscaling.md#mwaa-autoscaling-high-volume"). 6. Specify the **Maximum web server count** and **Minimum web server count**
to configure how Amazon MWAA scales the Apache Airflow web servers in your environment.

For more information about web server automatic scaling, refer to [Configuring Amazon MWAA webserver automatic scaling](mwaa-web-server-autoscaling.md "mwaa-web-server-autoscaling.md"). 7. Under **Encryption**, choose a data encryption option:

    1. By default, Amazon MWAA uses an AWS-owned key to encrypt your data.
    2. **Optional**. Choose **Customize encryption settings (advanced)** to choose a different AWS KMS key. If you choose to specify a [Customer-managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in this step, you must specify an AWS KMS key ID or ARN. [AWS KMS aliases and multi-region keys are not supported by Amazon MWAA](custom-keys-certs.md "custom-keys-certs.md"). If you specified an Amazon S3 key for server-side encryption on your Amazon S3 bucket, you must specify the same key for your Amazon MWAA environment.


    ###### Note

    You must have permissions to the key to select it on the Amazon MWAA console. You must also grant permissions for Amazon MWAA to use the key by attaching the policy described in [Attach key policy](custom-keys-certs.md#custom-keys-certs-grant-policies-attach "custom-keys-certs.md#custom-keys-certs-grant-policies-attach").

8. **Recommended**. Under **Monitoring**, choose one or more log categories for **Airflow logging configuration** to send Apache Airflow logs to CloudWatch Logs:
   1. **Airflow task logs**. Choose the type of Apache Airflow task logs to send to CloudWatch Logs in **Log level**.
   2. **Airflow webserver logs**. Choose the type of Apache Airflow webserver logs to send to CloudWatch Logs in **Log level**.
   3. **Airflow scheduler logs**. Choose the type of Apache Airflow scheduler logs to send to CloudWatch Logs in **Log level**.
   4. **Airflow worker logs**. Choose the type of Apache Airflow worker logs to send to CloudWatch Logs in **Log level**.
   5. **Airflow DAG processing logs**. Choose the type of Apache Airflow DAG processing logs to send to CloudWatch Logs in **Log level**.

9. **Optional**. For **Airflow configuration options**, choose **Add custom configuration option**.

You can choose from the suggested dropdown list of [Apache Airflow configuration options](configuring-env-variables.md "configuring-env-variables.md") for your Apache Airflow version, or specify custom configuration options. For example, `core.default_task_retries` : `3`. 10. **Optional**. Under **Tags**, choose **Add new tag** to associate tags to your environment. For example, `Environment`: `Staging`. 11. Under **Permissions**, choose an execution role:

    1. By default, Amazon MWAA creates an [execution role](mwaa-create-role.md "mwaa-create-role.md") in **Create a new role**. You must have permission to create IAM roles to use this option.
    2. **Optional**. Choose **Enter role ARN** to enter the Amazon Resource Name (ARN) of an existing execution role.

12. Choose **Next**.

### Step three: Review and create

###### To review an environment summary

- Review the environment summary, choose **Create environment**.

###### Note

It takes about twenty to thirty minutes to create an environment.
