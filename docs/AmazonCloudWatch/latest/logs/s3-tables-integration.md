# Access logs with S3 Tables Integration

The S3 Tables Integration with CloudWatch allows you to access log data ingested into CloudWatch using
analytics engines such as Amazon Athena, Amazon Redshift, and third-party tools that support connection
to Apache Iceberg-compatible stores. This integration enables you to perform comprehensive
log analysis using tools of your preference and correlate data in CloudWatch Logs with non-CloudWatch
data.

## Understanding S3 Tables

Integration

Amazon S3 Tables Integration is a fully managed solution that makes your logs in CloudWatch Logs
available as managed Amazon S3 tables. With this integration, you gain greater flexibility on
how you analyze your logs in addition to CloudWatch Logs features.

The integration works by creating a managed Amazon S3 table bucket
(`aws-cloudwatch`) and associating specific log sources with Amazon S3 Tables
based on data source name and type (that can be managed from the **Log
Management > Data Sources** tab in CloudWatch Logs Console). Once associated, CloudWatch Logs
data becomes accessible through Amazon S3 Tables using the Apache Iceberg format. This format
provides a standardized way for various analytics engines to query the data efficiently.

### Core Components

Data Source Association

The process of linking specific CloudWatch Logs sources to the S3 Tables
integration based on data source and type criteria.

Apache Iceberg Tables

The underlying table format used by S3 Tables that provides structured
data storage and enables compatibility with multiple analytics
engines.

### Data flow to S3 tables

Understanding how data flows between CloudWatch Logs and S3 Tables helps you plan your
integration and manage your log data effectively.

When you create an association, CloudWatch Logs automatically sends new log events that
match the associated data source name and type to a CloudWatch-managed S3 table bucket.
You can find these events in the logs namespace under the corresponding table for
that data source. The integration processes only log events added after you create
the association and does not backfill logs from before the association was
created.

Data retention in the S3 table bucket matches the retention policy set for the log
group. For example, if you set a log group to 1-day retention, CloudWatch Logs removes the
data from both CloudWatch Logs and the S3 Table after one day. When you delete a log group or
log stream, CloudWatch Logs also removes the data from the S3 table bucket.

## When to Use S3 Tables

Integration

Consider using S3 Tables integration to correlate log data with other external or
non-CloudWatch data or when you prefer using other analytics tools such as Amazon Athena to
perform analytics on CloudWatch Logs data. Use this integration when you need capabilities that go
beyond what's available in CloudWatch Logs. This integration is particularly valuable
when:

- You need to run complex SQL-like queries across large volumes of log
  data
- You want to integrate log analysis with existing analytics workflows and
  tools
- You require comprehensive log analysis capabilities that span multiple data
  sources

There are no additional storage or table maintenance charges for S3 tables created
through this integration, beyond existing CloudWatch ingestion and storage pricing.

## Prerequisites

Before implementing the integration, ensure you have the following:

- Existing CloudWatch Logs data
- Appropriate IAM permissions for cross-service access between CloudWatch Logs and S3
  Tables, as described in the following section

### IAM permissions

To integrate CloudWatch Logs with S3 Tables, you need to configure IAM permissions for two
separate entities: the user or role that sets up the integration, and the service
role that CloudWatch Logs assumes to write data to S3 Tables.

#### For the role or user creating the

integration

The user or role that sets up the integration requires the following
permissions:

- `observabilityadmin:CreateS3TableIntegration` to create the
  integration and `logs:AssociateSourceToS3TableIntegration` to
  add sources
- `s3tables:CreateTableBucket`,
  `s3tables:PutTableBucketEncryption`, and
  `s3tables:PutTableBucketPolicy` to configure the S3 table
  bucket

#### For the service role

Attach the following IAM policy to the IAM service role that CloudWatch Logs uses to
write data to the table bucket. This policy grants permission to write to the
tables. Replace `aws-region`,
`123456789012`, and
`log-group-name` with your AWS Region, account
ID, and log group name.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:integrateWithS3Table"
            ],
            "Resource": ["arn:aws:logs:`aws-region`:`123456789012`:log-group:`log-group-name`"],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "`123456789012`"
                }
            }
        }
    ]
}
```

Attach the following trust policy to the IAM service role that CloudWatch Logs will
assume to write log data to S3 Tables. You create or select this role during the
integration setup. The conditions restrict the role so that CloudWatch Logs can only
assume it for the specified account and log group. Replace `aws-region`,
`123456789012`, and
`log-group-name` with your AWS Region, account
ID, and log group name.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "logs.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "`123456789012`"
                },
                "ArnLike": {
                    "aws:SourceArn": ["arn:aws:logs:`aws-region`:`123456789012`:log-group:`log-group-name`"]
                }
            }
        }
    ]
}
```

### KMS key policy (for

encrypted data)

If you use a customer managed key to encrypt your log data, you must grant the
CloudWatch service principal and the S3 Tables maintenance service principal access to the
key. Add the following statements to your KMS key policy. Replace the placeholder
values with your AWS account ID, Region, KMS key ID, and S3 table or table bucket
ARN.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EnableSystemTablesKeyUsage",
            "Effect": "Allow",
            "Principal": {
                "Service": "systemtables.cloudwatch.amazonaws.com"
            },
            "Action": [
                "kms:DescribeKey",
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "arn:aws:kms:`aws-region`:`123456789012`:`key/key-id`",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "`123456789012`"
                }
            }
        },
        {
            "Sid": "EnableKeyUsage",
            "Effect": "Allow",
            "Principal": {
                "Service": "maintenance.s3tables.amazonaws.com"
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "arn:aws:kms:`aws-region`:`123456789012`:`key/key-id`",
            "Condition": {
                "StringLike": {
                    "kms:EncryptionContext:aws:s3:arn": "`<table-or-table-bucket-arn>`/*"
                }
            }
        }
    ]
}
```

## Getting Started

To get started with S3 Tables Integration, you need to set up the integration between
your CloudWatch Logs and S3 Tables. This process involves configuring data source associations and
setting up appropriate IAM permissions.

###### To create an S3 Tables Integration

1. Open the CloudWatch Logs console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch")".
2. Choose **Settings**, **Global**,
   **Create S3 Table Integration**.
3. Customize how logs will be encrypted in S3 Tables, and the role that CloudWatch Logs
   will use to write your logs into S3 Tables.
4. Choose **Create S3 Table Integration**.

###### To associate sources to an S3 Table Integration

1. Open the CloudWatch Logs console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch")".
2. Choose **Settings**, **Global**,
   **Manage S3 Table Integration**.
3. Choose **Associate data source**.
4. Select the data source name and data source type that you want to enable
   integration for.
5. Choose **Associate data source**.

###### To associate sources to an S3 Table Integration from the Log Management

Page

1. Open the CloudWatch Logs console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch")".
2. Choose **Log Management** in the navigation
   pane.
3. Select **Data Sources** tab.
4. Choose the data source name and data source type that you want to
   integrate.
5. Choose **Data source actions**.
6. Select **Associate with S3 Tables
   Integration**.
7. Review the data sources, and then choose **Associate Data
   source**.
