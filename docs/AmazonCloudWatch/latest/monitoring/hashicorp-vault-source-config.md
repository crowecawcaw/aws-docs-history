# Source configuration for HashiCorp Vault

## Integrating with HashiCorp Vault

HashiCorp Vault integration uses Amazon S3 and Amazon SQS to ingest log data into CloudWatch pipelines. Vault produces two log types: audit logs (detailed JSON records of all API requests and responses) and operational logs (server health and performance). Fluent Bit collects both log types from the Vault host and delivers them to an Amazon S3 bucket. Amazon SQS notifications alert the pipeline when new log objects arrive.

## Prerequisites

- An AWS account with permissions to create Amazon S3 buckets, Amazon SQS queues, and IAM roles
- A HashiCorp Vault server (self-managed) with administrative access
- A Linux host with Fluent Bit installed (can be the same host as Vault)
- Network connectivity between the Vault host and AWS

## Log forwarding setup

HashiCorp Vault audit logs can be forwarded to Amazon S3 using the Vault file audit device combined with Fluent Bit. Vault supports three audit device types: **file**, **socket**, and **syslog**. We recommend the **file** audit device for highest reliability.

## Instructions to setup Amazon S3 and Amazon SQS

Complete the following steps to configure the Amazon S3 and Amazon SQS infrastructure for HashiCorp Vault log ingestion.

### Step 1: Create Amazon S3 bucket

Create an Amazon S3 bucket to store HashiCorp Vault logs. The bucket must reside in the same AWS Region where you plan to create the CloudWatch pipeline.

### Step 2: Create Amazon SQS queue

Create an Amazon SQS queue in the same AWS Region as your Amazon S3 bucket. This queue receives notifications when new log files are added to the bucket.

### Step 3: Connect Amazon S3 to Amazon SQS

Configure the Amazon S3 bucket to send event notifications for `s3:ObjectCreated:*` events to the Amazon SQS queue.

### Step 4: Configure Amazon SQS queue policy

Configure the Amazon SQS queue policy to allow the Amazon S3 bucket to send messages to the queue. Apply the following policy to your Amazon SQS queue:

```
{
  "Version": "2012-10-17",
  "Id": "AllowS3ToSQS",
  "Statement": [
    {
      "Sid": "AllowS3BucketNotification",
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "arn:aws:sqs:<region>:<account-id>:<queue-name>",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:s3:::<YOUR-BUCKET>"
        },
        "StringEquals": {
          "aws:SourceAccount": "<account-id>"
        }
      }
    }
  ]
}
```

### Step 5: Configure Vault log export and Fluent Bit

Enable the Vault file audit device to write audit logs:

```
vault audit enable file file_path=/var/log/vault/audit.log
```

Configure JSON operational logs in the Vault server configuration file (`vault.hcl`):

```
log_level = "info"
log_format = "json"
```

Configure Fluent Bit to collect both audit and operational logs and deliver them to Amazon S3:

```
########################################
# SERVICE SECTION
########################################
[SERVICE]
    Flush        5
    Daemon       Off
    Log_Level    info
    storage.path /etc/fluent-bit/db/storage
    storage.sync normal
    storage.checksum off
    storage.backlog.mem_limit 10M

########################################
# INPUT SECTION
########################################
[INPUT]
    Name             tail
    Path             /var/log/vault/audit.log
    Tag              vault.audit
    Parser           json
    Read_from_Head   False
    DB               /etc/fluent-bit/db/vault-audit.db
    DB.Sync          Normal
    storage.type     filesystem
    Rotate_Wait      30
    Refresh_Interval 60

[INPUT]
    Name             tail
    Path             /var/log/vault/vault.log
    Tag              vault.operational
    Parser           json
    Read_from_Head   False
    DB               /etc/fluent-bit/db/vault-operational.db
    DB.Sync          Normal
    storage.type     filesystem
    Rotate_Wait      30
    Refresh_Interval 60

########################################
# OUTPUT SECTION
########################################
[OUTPUT]
    Name                 s3
    Match                vault.*
    bucket               <YOUR-BUCKET>
    region               <region>
    s3_key_format        /hashicorp-vault/%Y/%m/%d/%H/%M/%S.log.gz
    compression          gzip
    use_put_object       On
    store_dir            /etc/fluent-bit/db/s3
    total_file_size      1M
    log_key              log
    upload_timeout       60
```

### Step 6: IAM permissions

Create an IAM policy with the following permissions for the Fluent Bit host to write objects to the Amazon S3 bucket:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FluentBitS3Write",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetBucketLocation",
        "s3:ListBucket",
        "s3:ListMultipartUploadParts",
        "s3:AbortMultipartUpload",
        "s3:CreateMultipartUpload",
        "s3:CompleteMultipartUpload"
      ],
      "Resource": [
        "arn:aws:s3:::<YOUR-BUCKET>",
        "arn:aws:s3:::<YOUR-BUCKET>/hashicorp-vault/*"
      ]
    }
  ]
}
```

### Step 7: Verify

Verify the setup by confirming that log files appear in the Amazon S3 bucket and that Amazon SQS notifications are being generated. Check the Amazon SQS queue for messages indicating new object creation events.

## Configuring the CloudWatch pipeline

- Choose HashiCorp Vault as the data source when creating the pipeline.
- Provide the Amazon SQS queue URL and IAM role ARN.
- Select the destination CloudWatch Logs log group.
- After you create the pipeline, data will be available in the selected log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0. The following table shows the mapping between HashiCorp Vault log types and OCSF event classes. Events that are not mapped are forwarded as raw logs.

| Event name  | OCSF event class       |
| ----------- | ---------------------- |
| Audit       | API Activity [6003]    |
| Operational | N/A (raw pass-through) |
