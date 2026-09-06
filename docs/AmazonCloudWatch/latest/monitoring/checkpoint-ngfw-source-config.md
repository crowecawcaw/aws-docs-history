

# Source configuration for Check Point NGFW
<a name="checkpoint-ngfw-source-config"></a>

## Integrating with Check Point NGFW
<a name="checkpoint-ngfw-integration"></a>

Check Point NGFW integration uses Amazon S3 and Amazon SQS to ingest log data into CloudWatch pipelines. Log data is forwarded from the Check Point appliance using the `cp_log_export` utility to a syslog receiver, then collected by Fluent Bit and delivered to an Amazon S3 bucket. Amazon SQS notifications alert the pipeline when new log objects arrive.

## Prerequisites
<a name="checkpoint-ngfw-prerequisites"></a>
+ An AWS account with permissions to create Amazon S3 buckets, Amazon SQS queues, and IAM roles
+ A Check Point NGFW appliance with access to the `cp_log_export` utility
+ A Linux host with Fluent Bit installed (for log collection and delivery to Amazon S3)
+ Network connectivity between the Check Point appliance, syslog receiver, and AWS

## Log forwarding setup
<a name="checkpoint-ngfw-log-forwarding"></a>

Check Point NGFW exports logs using the `cp_log_export` utility, which forwards log data in syslog format to a designated receiver. Fluent Bit running on the syslog receiver host collects these logs and delivers them to Amazon S3 in NDJSON format.

## Instructions to setup Amazon S3 and Amazon SQS
<a name="checkpoint-ngfw-s3-sqs-setup"></a>

Complete the following steps to configure the Amazon S3 and Amazon SQS infrastructure for Check Point NGFW log ingestion.

### Step 1: Create Amazon S3 bucket
<a name="checkpoint-ngfw-step1"></a>

Create an Amazon S3 bucket to store Check Point NGFW logs. The bucket must reside in the same AWS Region where you plan to create the CloudWatch pipeline.

### Step 2: Create Amazon SQS queue
<a name="checkpoint-ngfw-step2"></a>

Create an Amazon SQS queue in the same AWS Region as your Amazon S3 bucket. This queue receives notifications when new log files are added to the bucket.

### Step 3: Connect Amazon S3 to Amazon SQS
<a name="checkpoint-ngfw-step3"></a>

Configure the Amazon S3 bucket to send event notifications for `s3:ObjectCreated:*` events to the Amazon SQS queue.

### Step 4: Configure Amazon SQS queue policy
<a name="checkpoint-ngfw-step4"></a>

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

### Step 5: Configure Check Point log export and Fluent Bit
<a name="checkpoint-ngfw-step5"></a>

On the Check Point appliance, configure `cp_log_export` to forward logs to your syslog receiver:

```
cp_log_export add name my_export target-server <syslog-host> target-port 514 protocol udp format syslog
```

On the syslog receiver host, install Fluent Bit and configure it to tail the Check Point NGFW log files and upload them to Amazon S3. Use the following example configuration:

```
########################################
# SERVICE SECTION
########################################
[SERVICE]
    Flush                        5
    Daemon                       Off
    Log_Level                    info
    storage.path                 /etc/fluent-bit/db/storage
    storage.sync                 normal
    storage.checksum             off
    storage.backlog.mem_limit    10M

########################################
# INPUT SECTION
########################################
[INPUT]
    Name                         tail
    Path                         /var/logs/<checkpoint_ip_address>/*.log
    Tag                          checkpoint.*
    Read_from_Head               True
    DB                           /etc/fluent-bit/db/checkpoint.db
    DB.Sync                      Normal
    storage.type                 filesystem
    Rotate_Wait                  30
    Refresh_Interval             60

########################################
# OUTPUT SECTION
########################################
[OUTPUT]
    Name                         s3
    Match                        checkpoint.*
    Bucket                       <<Bucket name>>
    Region                       <region>
    S3_Key_Format                /checkpoint-ngfw/%Y/%m/%d/%H/%M/%S.log.gz
    compression                  gzip
    use_put_object               On
    store_dir                    /etc/fluent-bit/db/s3
    total_file_size              1M
    log_key                      log
    upload_timeout               60
```

**Note**  
Logs from `cp_log_export` arrive in JSON format through syslog to the receiver host.
`log_key log` sends only the value of the `log` key to Amazon S3.
`storage.path` and `store_dir` provide local buffering.
The `DB` parameter tracks file read positions to prevent duplicate ingestion.
Replace `<checkpoint_ip_address>` with the actual IP address.
Replace `<<Bucket name>>` with your actual Amazon S3 bucket name.

### Step 6: IAM permissions
<a name="checkpoint-ngfw-step6"></a>

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
        "arn:aws:s3:::<YOUR-BUCKET>/checkpoint-ngfw/*"
      ]
    }
  ]
}
```

### Step 7: Verify
<a name="checkpoint-ngfw-step7"></a>

Verify the setup by confirming that log files appear in the Amazon S3 bucket and that Amazon SQS notifications are being generated. Check the Amazon SQS queue for messages indicating new object creation events.

## Configuring the CloudWatch pipeline
<a name="checkpoint-ngfw-pipeline-config"></a>
+ Choose Check Point NGFW as the data source when creating the pipeline.
+ Provide the Amazon SQS queue URL and IAM role ARN.
+ Select the destination CloudWatch Logs log group.
+ After you create the pipeline, data will be available in the selected log group.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="checkpoint-ngfw-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0. The following table shows the mapping between Check Point NGFW event types and OCSF event classes.


| Event name | OCSF event class | 
| --- | --- | 
| Firewall | Network Activity [4001] | 
| URL Filtering | Network Activity [4001] | 
| HTTPS Inspection | Network Activity [4001] | 
| Application Control | Network Activity [4001] | 
| Identity Awareness | Network Activity [4001] | 
| Anti Virus | Detection Finding [2004] | 
| Anti Spam | Detection Finding [2004] | 
| IPS | Detection Finding [2004] | 
| Anti Bot | Detection Finding [2004] | 
| Threat Emulation | Detection Finding [2004] | 
| Audit | Entity Management [3004] | 
| DLP | Data Security Finding [2006] | 