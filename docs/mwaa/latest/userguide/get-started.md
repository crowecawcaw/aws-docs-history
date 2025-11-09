# Get started with Amazon Managed Workflows for Apache Airflow

Amazon Managed Workflows for Apache Airflow uses the Amazon VPC, DAG files and supporting files in your Amazon S3 storage bucket to create an environment. This chapter describes the prerequisites and AWS resources needed to get started with Amazon MWAA.

###### Topics

- [Prerequisites](#prerequisites "#prerequisites")
- [About this guide](#prerequisites-infra "#prerequisites-infra")
- [Before you begin](#prerequisites-before "#prerequisites-before")
- [Available regions](#regions "#regions")
- [Create an Amazon S3 bucket for Amazon MWAA](mwaa-s3-bucket.md "mwaa-s3-bucket.md")
- [Create the VPC network](vpc-create.md "vpc-create.md")
- [Create an Amazon MWAA environment](create-environment.md "create-environment.md")
- [What's next?](#mwaa-s3-bucket-next-up "#mwaa-s3-bucket-next-up")

## Prerequisites

To create an Amazon MWAA environment, ensure you have permission to the AWS resources you need to create.

- **AWS account** – An AWS account with permission to use Amazon MWAA and the AWS services and resources used by your environment.

## About this guide

This guide covers the AWS infrastructure and resources you'll create.

- **Amazon VPC** – The Amazon VPC networking components required by an Amazon MWAA environment. You can configure an existing VPC that meets these requirements (advanced) as found in [About networking on Amazon MWAA](networking-about.md "networking-about.md"), or create the VPC and networking components, as defined in [Create the VPC network](vpc-create.md "vpc-create.md").
- **Amazon S3 bucket** – An Amazon S3 bucket to store your DAGs and associated files, such as `plugins.zip` and `requirements.txt`. Your Amazon S3 bucket must be configured to **Block all public access**, with **Bucket Versioning** enabled, as defined in [Create an Amazon S3 bucket for Amazon MWAA](mwaa-s3-bucket.md "mwaa-s3-bucket.md").
- **Amazon MWAA environment** – An Amazon MWAA environment configured with the location of your Amazon S3 bucket, the path to your DAG code and any custom plugins or Python dependencies, and your Amazon VPC and its security group, as defined in [Create an Amazon MWAA environment](create-environment.md "create-environment.md").

## Before you begin

To create an Amazon MWAA environment, you can take additional steps to create and configure other AWS resources before you create your environment.

To create an environment, you need the following:

- **AWS KMS key** – An AWS KMS key for data encryption on your environment. You can choose the default option on the Amazon MWAA console to create an [AWS-owned key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") when you create an environment, or specify an existing [Customer-managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") with permissions to other AWS services used by your environment configured (advanced). To learn more, refer to [Using customer-managed keys for encryption](custom-keys-certs.md "custom-keys-certs.md").
- **Execution role** – An execution role that allows Amazon MWAA to access AWS resources in your environment. You can choose the default option on the Amazon MWAA console to create an execution role when you create an environment. To learn more, refer to [Amazon MWAA execution role](mwaa-create-role.md "mwaa-create-role.md").
- **VPC security group** – A VPC security group that allows Amazon MWAA to access other AWS resources in your VPC network. You can choose the default option on the Amazon MWAA console to create a security group when you create an environment, or provide a security group with the appropriate inbound and outbound rules (advanced). To learn more, refer to [Security in your VPC on Amazon MWAA](vpc-security.md "vpc-security.md").

## Available regions

Amazon MWAA is available in the following AWS Regions. To learn more about each region, such as which are enabled or disabled by default, refer to [AWS Regions](../../../global-infrastructure/latest/regions/aws-regions.md "../../../global-infrastructure/latest/regions/aws-regions.md").

| Code           | Name                      |
| -------------- | ------------------------- |
| us-east-1      | US East (N. Virginia)     |
| us-east-2      | US East (Ohio)            |
| us-west-1      | US West (N. California)   |
| us-west-2      | US West (Oregon)          |
| af-south-1     | Africa (Cape Town)        |
| ap-east-1      | Asia Pacific (Hong Kong)  |
| ap-south-2     | Asia Pacific (Hyderabad)  |
| ap-southeast-3 | Asia Pacific (Jakarta)    |
| ap-southeast-5 | Asia Pacific (Malaysia)   |
| ap-southeast-4 | Asia Pacific (Melbourne)  |
| ap-south-1     | Asia Pacific (Mumbai)     |
| ap-northeast-3 | Asia Pacific (Osaka)      |
| ap-northeast-2 | Asia Pacific (Seoul)      |
| ap-southeast-1 | Asia Pacific (Singapore)  |
| ap-southeast-2 | Asia Pacific (Sydney)     |
| ap-northeast-1 | Asia Pacific (Tokyo)      |
| ca-central-1   | Canada (Central)          |
| ca-west-1      | Canada West (Calgary)     |
| eu-central-1   | Europe (Frankfurt)        |
| eu-west-1      | Europe (Ireland)          |
| eu-west-2      | Europe (London)           |
| eu-south-1     | Europe (Milan)            |
| eu-west-3      | Europe (Paris)            |
| eu-south-2     | Europe (Spain)            |
| eu-north-1     | Europe (Stockholm)        |
| eu-central-2   | Europe (Zurich)           |
| il-central-1   | Israel (Tel Aviv)         |
| me-south-1     | Middle East (Bahrain)     |
| me-central-1   | Middle East (UAE)         |
| sa-east-1      | South America (São Paulo) |

## What's next?

- Learn how to create an Amazon S3 bucket in [Create an Amazon S3 bucket for Amazon MWAA](mwaa-s3-bucket.md "mwaa-s3-bucket.md").
