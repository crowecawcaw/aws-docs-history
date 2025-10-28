# Update an Amazon MWAA environment

###### Note

Amazon MWAA graceful updates are not yet supported in the Canada West (Calgary) and Asia Pacific (Malaysia) regions.

Amazon MWAA environment updates apply the latest changes and security patches. You can also edit existing configurations and upgrade
the Apache Airflow version. This guide describes the steps to update an Amazon MWAA environment.

###### Contents

- [Before you begin](update-environment.md#update-environment-before "update-environment.md#update-environment-before")
- [Worker replacement strategy](update-environment.md#worker-replacement-strategy "update-environment.md#worker-replacement-strategy")
- [Update environment resources](update-environment.md#update-environment-resources "update-environment.md#update-environment-resources")
- [Update an environment](update-environment.md#update-environment-start "update-environment.md#update-environment-start")
  - [Step one: Specify details](update-environment.md#update-environment-start-details "update-environment.md#update-environment-start-details")
  - [Step two: Configure advanced settings](update-environment.md#update-environment-start-advanced "update-environment.md#update-environment-start-advanced")
  - [Step three: Review and update](update-environment.md#update-environment-start-review "update-environment.md#update-environment-start-review")

## Before you begin

- The [VPC network](vpc-create.md "vpc-create.md") you specified for your environment cannot be modified after the environment is created.
- You need an Amazon S3 bucket configured to **Block all public access**, with **Bucket Versioning** enabled.
- You need an AWS account with [permissions to use Amazon MWAA](manage-access.md "manage-access.md"), and permission in AWS Identity and Access Management (IAM) to create IAM roles.
  If you choose the **Private network** access mode for the Apache Airflow webserver, which limits Apache Airflow access
  within your Amazon VPC, you'll need permission in IAM to create Amazon VPC endpoints.
- To enable Graceful environment updates, you need to upgrade To Apache Airflow version 2.4.3 or higher. To upgrade the Airflow version, refer to [Changing the Apache Airflow version](upgrading-environment.md "upgrading-environment.md").

## Worker replacement strategy

You can choose a worker replacement strategy to control how Amazon MWAA handles active workers during an environment update.
You can select one of the following strategies:

**Forced updates**

Forced update is the default worker replacement strategy. Forced updates immediately stop all active workers,
causing running tasks to fail during the update.

**Graceful updates**

Graceful updates allow workers to continue running tasks for up to 12 hours before shutting down.
It prevents tasks failing due to update interruptions, as long as they finish under 12 hours. New tasks are
routed to updated workers.

To enable Graceful updates on an existing environment, you must complete one **Forced update** and ensure the environment is on
Apache Airflow version 2.4.3 or higher.

###### Note

If you perform an update while your environment is in `MAINTENANCE` status, the worker replacement strategy for any ongoing environment update switches from `GRACEFUL` to `FORCED`. Your update is performed after maintenance is complete.

## Update environment resources

Amazon MWAA environment updates use the existing environment configuration by default. To update the environment without changing your current configuration:

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. From the **Environments** list, choose the environment that you want to update.
3. On the environment page, choose **Edit** to edit the environment.
4. Choose **Next** until you are on the **Review and save** page.
5. On the **Review and save** page, review your changes, then choose **Save**.

## Update an environment

The following section describes the steps to update an Amazon MWAA environment.

### Step one: Specify details

###### To specify details for the environment

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. From the **Environments** list, choose the environment that you want to update.
3. On the environment page, choose **Edit** to edit the environment.
4. In the Environment details section, for Airflow version, choose the new Apache Airflow version number that you want to
   upgrade the environment to from the dropdown list.

###### Note

Before you upgrade, make sure that your DAGs and other workflow resources are compatible with the new
Apache Airflow version. For more information, refer to [Changing the Apache Airflow version](upgrading-environment.md "upgrading-environment.md"). 5. Under **DAG code in Amazon S3** specify the following:

    1. **S3 Bucket**. Choose **Browse S3** and select your Amazon S3 bucket, or enter the Amazon S3 URI.
    2. **DAGs folder**. Choose **Browse S3** and select the `dags` folder in your Amazon S3 bucket, or enter the Amazon S3 URI.
    3. **Plugins file - *optional***. Choose **Browse S3** and select the `plugins.zip` file on your Amazon S3 bucket, or enter the Amazon S3 URI.
    4. **Requirements file - *optional***. Choose **Browse S3** and select the `requirements.txt` file on your Amazon S3 bucket, or enter the Amazon S3 URI.
    5. **Startup script file - *optional***, Choose **Browse S3** and select the script file on your Amazon S3 bucket, or enter the Amazon S3 URI.

6. Choose **Next**.

### Step two: Configure advanced settings

###### To configure advanced settings

1. Under **webserver access**, select your preferred [Apache Airflow access mode](configuring-networking.md "configuring-networking.md"):
   1. **Private network**. This limits access of the Apache Airflow UI to users _within your Amazon VPC_ that have been granted access to the [IAM policy for your environment](access-policies.md "access-policies.md"). You need permission to create Amazon VPC endpoints for this step.

   ###### Note

   Choose the **Private network** option if your Apache Airflow UI is only accessed within a corporate network, and you do not require access to public repositories for webserver requirements installation. If you choose this access mode option, you need to create a mechanism to access your Apache Airflow webserver in your Amazon VPC. For more information, refer to [Accessing the VPC endpoint for your Apache Airflow webserver (private network access)](vpc-vpe-access.md#vpc-vpe-access-endpoints "vpc-vpe-access.md#vpc-vpe-access-endpoints"). 2. **Public network**. This allows the Apache Airflow UI to be accessed over the internet by users granted access to the [IAM policy for your environment](access-policies.md "access-policies.md").

2. Under **Security groups**, choose the security group used to secure your [Amazon VPC](vpc-create.md "vpc-create.md"):
   1. By default, Amazon MWAA creates a security group in your Amazon VPC with specific inbound and outbound rules in **Create new security group**.
   2. **Optional**. Deselect the check box in **Create new security group** to select up to 5 security groups.

   ###### Note

   An existing Amazon VPC security group must be configured with specific inbound and outbound rules to allow network traffic. To learn more, refer to [Security in your VPC on Amazon MWAA](vpc-security.md "vpc-security.md").

3. Under **Environment class**, choose an [environment class](environment-class.md "environment-class.md").

We recommend choosing the smallest size necessary to support your workload. You can change the environment class at any time. 4. For **Maximum worker count**, specify the maximum number of Apache Airflow workers to run in the environment.

For more information, refer to [Example high performance use case](mwaa-autoscaling.md#mwaa-autoscaling-high-volume "mwaa-autoscaling.md#mwaa-autoscaling-high-volume"). 5. Specify the **Maximum web server count** and **Minimum webserver count**
to configure how Amazon MWAA scales the Apache Airflow web servers in your environment.

For more information about web server automatic scaling, refer to [Configuring Amazon MWAA webserver automatic scaling](mwaa-web-server-autoscaling.md "mwaa-web-server-autoscaling.md"). 6. Under **Encryption**, choose a data encryption option:

    1. By default, Amazon MWAA uses an AWS-owned key to encrypt your data.
    2. **Optional**. Choose **Customize encryption settings (advanced)** to choose a different AWS KMS key. If you choose to specify a [Customer-managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in this step, you must specify an AWS KMS key ID or ARN. [AWS KMS aliases and multi-region keys are not supported by Amazon MWAA](custom-keys-certs.md "custom-keys-certs.md"). If you specified an Amazon S3 key for server-side encryption on your Amazon S3 bucket, you must specify the same key for your Amazon MWAA environment.


    ###### Note

    You must have permissions to the key to select it on the Amazon MWAA console. You must also grant permissions for Amazon MWAA to use the key by attaching the policy described in [Attach key policy](custom-keys-certs.md#custom-keys-certs-grant-policies-attach "custom-keys-certs.md#custom-keys-certs-grant-policies-attach").

7. **Recommended**. Under **Monitoring**, choose one or more log categories for **Airflow logging configuration** to send Apache Airflow logs to CloudWatch Logs:
   1. **Airflow task logs**. Choose the type of Apache Airflow task logs to send to CloudWatch Logs in **Log level**.
   2. **Airflow webserver logs**. Choose the type of Apache Airflow webserver logs to send to CloudWatch Logs in **Log level**.
   3. **Airflow scheduler logs**. Choose the type of Apache Airflow scheduler logs to send to CloudWatch Logs in **Log level**.
   4. **Airflow worker logs**. Choose the type of Apache Airflow worker logs to send to CloudWatch Logs in **Log level**.
   5. **Airflow DAG processing logs**. Choose the type of Apache Airflow DAG processing logs to send to CloudWatch Logs in **Log level**.

8. **Optional**. For **Airflow configuration options**, choose **Add custom configuration option**.

You can choose from the suggested dropdown list of [Apache Airflow configuration options](configuring-env-variables.md "configuring-env-variables.md") for your Apache Airflow version, or specify custom configuration options. For example, `core.default_task_retries` : `3`. 9. Under **Permissions**, choose an execution role:

    1. By default, Amazon MWAA creates an [execution role](mwaa-create-role.md "mwaa-create-role.md") in **Create a new role**. You must have permission to create IAM roles to use this option.
    2. **Optional**. Choose **Enter role ARN** to enter the Amazon Resource Name (ARN) of an existing execution role.

10. Under **Update specifications**, choose a [Worker replacement strategy](#worker-replacement-strategy "#worker-replacement-strategy") to control how active workers are handled during an update.
11. Choose **Next**.

### Step three: Review and update

###### To review an environment summary

- Review the environment summary, choose **Save**.

###### Note

It takes about twenty to thirty minutes to update an environment using forced updates. Graceful environment updates might take
up to twelve hours to complete, as it waits for your ongoing tasks to finish.
