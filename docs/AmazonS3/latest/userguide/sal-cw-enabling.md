

# Delivering server access logs to CloudWatch Logs
<a name="sal-cw-enabling"></a>

You can deliver Amazon S3 server access logs to a CloudWatch Logs log group using Amazon CloudWatch Logs vended log delivery. Once logs are in CloudWatch Logs, you can query them with CloudWatch Logs Insights, aggregate them across accounts and Regions, encrypt them with AWS Key Management Service (AWS KMS), and optionally deliver them to Amazon S3 Tables in Apache Iceberg format for SQL analytics. You can also deliver logs to Amazon S3 in JSON or Apache Parquet format or route them through Amazon Data Firehose.

You configure delivery using CloudWatch Logs APIs, not Amazon S3 APIs. You specify a log group for each source bucket. Multiple buckets can share the same log group, or each bucket can deliver to its own.

**Tip**  
You can set up multiple destinations for the same bucket. For example, deliver to a CloudWatch Logs log group for interactive querying and simultaneously deliver to Amazon S3 in Parquet format for long-term retention at lower cost.

**Note**  
CloudWatch Logs vended log delivery also supports Amazon Data Firehose and Amazon S3 as delivery destinations, including Apache Parquet output format. This page covers the CloudWatch Logs log group destination, which also supports the S3 Tables integration for SQL analytics. For information about Firehose and Amazon S3 destinations, see [Enable logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) in the *Amazon CloudWatch Logs User Guide*.

**Note**  
For information about delivering server access logs to an Amazon S3 general purpose bucket instead, see [Enabling Amazon S3 server access logging](enable-server-access-logging.md).

## Prerequisites
<a name="sal-cw-prerequisites"></a>

Before you set up delivery, you need the following:
+ An Amazon S3 general purpose bucket (the source bucket you want to log).
+ A CloudWatch Logs log group in the same AWS Region as the source bucket.
+ IAM permissions for the caller. At a minimum, you need the following permissions:
  + `logs:PutDeliverySource`
  + `logs:PutDeliveryDestination`
  + `logs:CreateDelivery`
  + `s3:AllowVendedLogDeliveryForResource` (on the source bucket)

  If you plan to enable the S3 Tables integration, you also need:
  + `observabilityadmin:CreateS3TableIntegration`
  + `logs:AssociateSourceToS3TableIntegration`
  + `s3tables:CreateTableBucket`
  + `s3tables:PutTableBucketEncryption`
  + `s3tables:PutTableBucketPolicy`

## Setting up delivery (AWS CLI)
<a name="sal-cw-setup-cli"></a>

To set up server access log delivery to CloudWatch Logs using the AWS Command Line Interface, complete the following three steps.

1. **Create a delivery source.** This registers your Amazon S3 bucket as a log source with CloudWatch Logs.

   ```
   aws logs put-delivery-source \
     --name {{my-sal-source}} \
     --resource-arn arn:aws:s3:::{{my-bucket}} \
     --log-type S3_SERVER_ACCESS_LOGS
   ```

1. **Create a delivery destination.** This specifies the CloudWatch Logs log group where logs will be delivered.

   ```
   aws logs put-delivery-destination \
     --name {{my-sal-destination}} \
     --delivery-destination-configuration '{"destinationResourceArn": "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:{{my-sal-logs}}"}'
   ```

1. **Create a delivery.** This links the source to the destination and starts log delivery.

   ```
   aws logs create-delivery \
     --delivery-source-name {{my-sal-source}} \
     --delivery-destination-arn arn:aws:logs:{{us-east-1}}:{{123456789012}}:delivery-destination:{{my-sal-destination}}
   ```

After you complete these steps, Amazon S3 begins delivering server access logs to your CloudWatch Logs log group. The configuration takes 15–20 minutes to propagate. After propagation, log delivery typically begins within a few hours. Only new requests are logged – there is no backfill of historical data.

## Setting up delivery (Amazon S3 console)
<a name="sal-cw-setup-console"></a>

1. Sign in to the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Buckets**.

1. Choose the name of the source bucket that you want to enable logging for.

1. Choose the **Properties** tab.

1. In the **Server access log delivery to CloudWatch Logs** section, choose **Edit**.

1. Choose **Enable**.

1. Select or create a CloudWatch Logs log group as the delivery destination.

1. (Optional) To deliver logs to S3 Tables in Apache Iceberg format, select **Enable S3 Tables integration**.

1. Choose **Save changes**.

After you save, the **Server access log delivery to CloudWatch Logs** section displays the enabled log group.

## Setting up delivery (CloudFormation)
<a name="sal-cw-setup-cfn"></a>

You can use AWS CloudFormation to automate the setup of server access log delivery to CloudWatch Logs. The following template creates the required resources: an IAM role, a CloudWatch Logs log group, a delivery source, a delivery destination, and a delivery.

```
AWSTemplateFormatVersion: '2010-09-09'
Description: S3 Access Logs delivery to CloudWatch Logs

Parameters:
  SourceBucketArn:
    Type: String
    Description: ARN of the S3 bucket to enable access logging
  LogGroupName:
    Type: String
    Default: /aws/s3/access-logs
    Description: CloudWatch Log Group name for SAL delivery

Resources:
  SALLogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: !Ref LogGroupName
      RetentionInDays: 180

  SALDeliverySource:
    Type: AWS::Logs::DeliverySource
    Properties:
      Name: !Sub '${AWS::StackName}-sal-source'
      ResourceArn: !Ref SourceBucketArn
      LogType: S3_SERVER_ACCESS_LOGS

  SALDeliveryDestination:
    Type: AWS::Logs::DeliveryDestination
    Properties:
      Name: !Sub '${AWS::StackName}-sal-destination'
      DestinationResourceArn: !GetAtt SALLogGroup.Arn

  SALDelivery:
    Type: AWS::Logs::Delivery
    Properties:
      DeliverySourceName: !Ref SALDeliverySource
      DeliveryDestinationArn: !GetAtt SALDeliveryDestination.Arn
```

## Enabling the S3 Tables integration (optional)
<a name="sal-cw-tables-integration"></a>

When you enable the S3 Tables integration, CloudWatch Logs automatically delivers your server access logs in Apache Iceberg format to the `aws-cloudwatch` managed table bucket in your account. You can then query this data using Amazon Athena, Amazon Redshift, or any Iceberg-compatible tool.

There is no additional charge for storage or table maintenance in the S3 Tables integration. You pay only for CloudWatch Logs ingestion and for query requests at S3 Tables pricing.

1. **Create the S3 Tables integration** (once per account per Region).

   ```
   aws observabilityadmin create-s3-table-integration \
     --role-arn arn:aws:iam::{{123456789012}}:role/{{CWLogsS3TableIntegrationRole}} \
     --encryption '{"SseAlgorithm": "AES256"}'
   ```

   The IAM role must trust the `logs.amazonaws.com` service principal and grant the `logs:integrateWithS3Table` permission. The following is an example trust policy:

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
             "aws:SourceAccount": "{{123456789012}}"
           },
           "ArnLike": {
             "aws:SourceArn": "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:{{log-group-name}}"
           }
         }
       }
     ]
   }
   ```

   The role also needs the following permission policy:

   ```
   		 	 	 {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "logs:integrateWithS3Table",
         "Resource": "arn:aws:logs:{{us-east-1}}:{{123456789012}}:log-group:{{log-group-name}}",
         "Condition": {
           "StringEquals": {
             "aws:ResourceAccount": "{{123456789012}}"
           }
         }
       }
     ]
   }
   ```

1. **Associate your delivery source to the integration.**

   ```
   aws logs associate-source-to-s3-table-integration \
     --integration-arn {{integration-arn}} \
     --data-source '{"name":"amazon_s3","type":"server_access"}'
   ```

After these steps, CloudWatch Logs creates the `aws-cloudwatch` managed table bucket and begins delivering logs in Iceberg format. Data typically appears within an hour of the first delivery to CloudWatch Logs.

For information about querying the S3 Tables integration, see [Querying access logs in S3 Tables](sal-cw-querying-s3tables.md).

## Cross-account and cross-Region aggregation
<a name="sal-cw-cross-account"></a>

The CloudWatch Logs delivery path supports cross-account and cross-Region log aggregation with two options:
+ **CloudWatch cross-account observability** allows you to query logs in place across accounts without copying data.
+ **CloudWatch Logs centralization** allows you to consolidate logs from multiple accounts and Regions into a central log group, optionally using subscription filters for selective forwarding.

For multi-account setups, administrators can use CloudWatch Telemetry Config enablement rules with AWS Organizations to automatically enable server access log delivery across member accounts.

**Note**  
Enablement rules do not currently support automatic enablement of the S3 Tables integration. You must enable the integration separately in each account.

## Encryption
<a name="sal-cw-encryption"></a>

You can encrypt server access logs delivered to CloudWatch Logs by configuring AWS KMS encryption on your log group. When server access logs are delivered to that log group, they are encrypted with your AWS KMS key. This addresses a key limitation of the Amazon S3 general purpose bucket delivery path, which supports only SSE-S3 encryption.

If you enable the S3 Tables integration with a AWS KMS-encrypted log group, you must grant additional permissions in your AWS KMS key policy to the following service principals:

```
		 	 	 {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EnableCWSystemTablesKeyUsage",
      "Effect": "Allow",
      "Principal": {
        "Service": "systemtables.cloudwatch.amazonaws.com"
      },
      "Action": [
        "kms:DescribeKey",
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": "arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{key-id}}",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{123456789012}}"
        }
      }
    },
    {
      "Sid": "EnableS3TablesMaintenanceKeyUsage",
      "Effect": "Allow",
      "Principal": {
        "Service": "maintenance.s3tables.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": "arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{key-id}}",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:s3:arn": "{{table-bucket-arn}}/*"
        }
      }
    }
  ]
}
```

The `systemtables.cloudwatch.amazonaws.com` principal is used by CloudWatch Logs to write logs to S3 Tables. The `maintenance.s3tables.amazonaws.com` principal is used by S3 Tables for Iceberg operations such as compaction.

## Disabling delivery
<a name="sal-cw-disabling"></a>

To stop delivering server access logs to CloudWatch Logs, you can delete the delivery or the delivery source:
+ **Delete the delivery** – stops log delivery but keeps the delivery source configuration intact. You can create a new delivery later without reconfiguring the source.

  ```
  aws logs delete-delivery \
    --id {{delivery-id}}
  ```
+ **Delete the delivery source** – removes the source configuration entirely. Use this if you no longer want the bucket associated with CloudWatch Logs delivery.

  ```
  aws logs delete-delivery-source \
    --name {{delivery-source-name}}
  ```

Previously delivered logs remain in the log group and in the S3 Tables integration (if enabled). Deleting the delivery does not remove existing log data.