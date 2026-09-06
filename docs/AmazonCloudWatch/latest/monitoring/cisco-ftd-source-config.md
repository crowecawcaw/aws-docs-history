

# Source configuration for Cisco FTD
<a name="cisco-ftd-source-config"></a>

## Integrating with Cisco FTD
<a name="cisco-ftd-integration"></a>

Cisco FTD exports logs using the syslog protocol. These logs are collected by a syslog server, processed using Fluent Bit, and delivered to a customer-managed Amazon S3 bucket. CloudWatch pipelines read from this bucket using Amazon SQS notifications for new object events.

To integrate Cisco FTD with CloudWatch Logs, you must configure both the source and the pipeline. First, set up the syslog server, Fluent Bit, Amazon S3, and Amazon SQS to receive and store data from Cisco FTD. Then, configure the CloudWatch pipeline to ingest the data from your source into CloudWatch Logs.

## Prerequisites
<a name="cisco-ftd-prerequisites"></a>

Before you begin, make sure you have the following:
+ Access to Cisco FTD with permissions to configure syslog export (through Firepower Management Center or CLI)
+ A Linux-based syslog server (Amazon Linux 2 or Amazon Linux 2023 recommended) with network connectivity to your Cisco FTD appliance
+ An AWS account with permissions to create and manage CloudWatch pipelines
+ An AWS account with permissions to create and manage Amazon S3 buckets, Amazon SQS queues, and IAM roles

## Instructions to set up Syslog Server, Fluent Bit, Amazon S3 and Amazon SQS
<a name="cisco-ftd-s3-sqs-setup"></a>

1. **Create an Amazon S3 Bucket**

   Create an Amazon S3 bucket in the same AWS region where you plan to run the pipeline. Enable server-side encryption and block public access. Reference: [Creating a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)

1. **Create an IAM User with Programmatic Access for Fluent Bit**

   In IAM, create a user with programmatic (CLI) access for Fluent Bit to write logs to Amazon S3. Attach a policy scoped to the target bucket:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "s3:PutObject",
                   "s3:AbortMultipartUpload",
                   "s3:ListBucket"
               ],
               "Resource": [
                   "arn:aws:s3:::<bucket-name>",
                   "arn:aws:s3:::<bucket-name>/*"
               ]
           }
       ]
   }
   ```

1. **Create an Amazon SQS Queue**

   Create a standard Amazon SQS queue in the same AWS region as the Amazon S3 bucket. Note the Queue URL and Queue ARN. Reference: [Creating an Amazon SQS queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/creating-sqs-standard-queues.html)

1. **Configure Amazon SQS Queue Policy**

   Add a resource policy to the Amazon SQS queue allowing Amazon S3 to send event notifications:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [{
           "Effect": "Allow",
           "Principal": {"Service": "s3.amazonaws.com"},
           "Action": "sqs:SendMessage",
           "Resource": "arn:aws:sqs:<region>:<account-id>:<queue-name>",
           "Condition": {
               "ArnEquals": {"aws:SourceArn": "arn:aws:s3:::<bucket-name>"}
           }
       }]
   }
   ```

1. **Enable Amazon S3 Event Notifications**

   Navigate to the Amazon S3 bucket > Properties > Event notifications. Create a notification for `s3:ObjectCreated:*` events. Select the Amazon SQS queue created in Step 3 as the destination. Reference: [Enabling event notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)

1. **Configure Cisco FTD, the Syslog Server, and Fluent Bit**

   Configure Cisco FTD to forward logs over syslog (UDP 514/5514) to the syslog server, set up the syslog server (for example, rsyslog on Amazon Linux) to receive them, and install Fluent Bit to compress (gzip) and upload the logs to the Amazon S3 bucket created in Step 1.

   Use the following Fluent Bit configuration as a reference:

   ```
   [SERVICE]
       Flush             1
       Daemon            Off
       Log_Level         info
       Parsers_File      /etc/fluent-bit/parsers.conf
       storage.path      /tmp/fluent-bit/storage
   
   [INPUT]
       Name              tail
       Path              /var/log/cisco-ftd.log,/var/log/messages
       Tag               cisco.ftd
       Read_from_Head    True
       Refresh_Interval  5
       Mem_Buf_Limit     50MB
       Skip_Long_Lines   On
       DB                /tmp/fluent-bit/flb.db
   
   [OUTPUT]
       Name              s3
       Match             cisco.ftd
       bucket            <bucket-name>
       region            <region>
       total_file_size   5M
       upload_timeout    1m
       store_dir         /tmp/fluent-bit/s3
       s3_key_format     /cisco-ftd/%Y/%m/%d/%H/%M/%S-$UUID.gz
       compression       gzip
       log_key           log
   ```

   Replace `<bucket-name>` and `<region>` with the values from Step 1. Ensure Fluent Bit has AWS credentials (the IAM user from Step 2, or an instance role) with permission to write to the bucket.

## Configuring the CloudWatch Pipeline
<a name="cisco-ftd-pipeline-config"></a>

When configuring the pipeline to read data from Cisco FTD, choose Cisco FTD as the data source. Provide the Amazon SQS queue URL and IAM role ARN. After you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="cisco-ftd-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0 and transforms the following events that map to [Authentication (3002)](https://schema.ocsf.io/1.5.0/), [Tunnel Activity (4014)](https://schema.ocsf.io/1.5.0/), [Network Activity (4001)](https://schema.ocsf.io/1.5.0/), [Detection Finding (2004)](https://schema.ocsf.io/1.5.0/), and [Authorize Session (3003)](https://schema.ocsf.io/1.5.0/). Events that are not listed but pulled are not mapped to OCSF and will be forwarded to the sink as raw logs.

**Authentication** contains the following [Syslog IDs](https://www.cisco.com/c/en/us/td/docs/security/firepower/Syslogs/fptd_syslog_guide/syslogs1.html):

109011, 109012, 109013, 109026, 109027, 109039, 109201, 109202, 109203, 109204, 109205, 109206, 109207, 109208, 109209, 109210, 109211, 109212, 109213, 113001, 113004, 113005, 113006, 113007, 113008, 113009, 113010, 113012, 113013, 113014, 113016, 113017, 113019, 113020, 113021, 113022, 113023, 113024, 113025, 113026, 113027, 113028, 113029, 113033, 113035, 113037, 113038, 113039, 113040, 214001, 308001, 320001, 324302, 324303, 333001, 333002, 333003, 333004, 333005, 333006, 333007, 333008, 333009, 333010, 334001, 334002, 334003, 334004, 334005, 334006, 334007, 334008, 334009, 611101, 611102, 611103, 611104, 611316, 611317, 611318, 611319, 716036, 716038, 716039, 716040, 716160, 717001, 717009, 717010, 717012, 717013, 717014, 717015, 717016, 717017, 717018, 717021, 717022, 717024, 717025, 717026, 717027, 717028, 717029, 717030, 717031, 717032, 717033, 717034, 717035, 717036, 717037, 717038, 717053, 772002, 772003, 772004, 772005, 772006

**Tunnel Activity** contains the following [Syslog IDs](https://www.cisco.com/c/en/us/td/docs/security/firepower/Syslogs/fptd_syslog_guide/syslogs1.html):

316001, 316002, 602303, 602304, 602305, 602306, 603110, 611309, 611315, 702307, 713041, 713049, 713050, 713056, 713060, 713061, 713073, 713074, 713075, 713076, 713092, 713099, 713113, 713120, 713123, 713136, 713169, 713187, 713194, 713195, 713196, 713206, 713207, 713218, 713227, 713239, 713259, 713262, 713276, 715009, 715013, 715080, 716001, 716002, 716006, 716007, 716009, 716023, 716057, 716058, 716059, 716060, 716166, 718048, 718049, 718050, 718051, 722020, 722029, 722030, 722031, 722032, 722033, 722034, 722037, 722038, 722041, 722045, 722046, 722047, 722048, 722049, 722050, 722054, 724001, 724002, 750001, 750002, 750003, 750004, 750005, 750006, 750007, 750008, 750009, 750010, 750011, 750012, 750013, 750014, 751001, 751002, 751003, 751004, 751005, 751006, 751007, 751008, 751009, 751010, 751011, 751012, 751013, 751014, 751015, 751016, 751017, 751018, 751019, 751020, 751021, 751022, 751023, 751024, 751025, 751026, 751027, 751031, 752002, 752012, 752015, 752016, 752017, 840001

**Network Activity** contains the following [Syslog IDs](https://www.cisco.com/c/en/us/td/docs/security/firepower/Syslogs/fptd_syslog_guide/syslogs1.html):

430002, 430003, 106029, 302003, 302004, 302012, 302013, 302015, 302017, 302020, 302022, 302024, 302026, 302033, 302037, 302303, 305009, 305011, 609001, 302014, 302016, 302018, 302021, 302023, 302025, 302027, 302038, 302304, 305010, 305012, 419006, 507001, 609002, 500005, 110002, 110003, 201005, 201006, 302034, 302311, 305006, 305016, 305021, 305023, 106001, 106002, 106006, 106007, 106010, 106011, 106012, 106013, 106014, 106015, 106016, 106017, 106018, 106020, 106021, 106022, 106023, 106027, 106103, 201002, 201003, 201004, 201008, 201009, 201010, 201011, 201012, 201013, 209003, 209004, 209005, 209006, 302302, 313001, 313004, 313005, 313008, 313009, 322001, 407001, 407002, 407003, 418001, 419001, 421001, 424001, 424002, 446003, 448001, 500003, 500004, 509001, 710003, 710004, 710005, 710006, 767001, 815002, 106100, 106102, 302010, 302310, 305013, 419002, 419003, 419004, 419005, 421007, 507003, 775002, 805001, 805002, 805003, 815004, 852001, 852002

**Detection Finding** contains the following [Syslog IDs](https://www.cisco.com/c/en/us/td/docs/security/firepower/Syslogs/fptd_syslog_guide/syslogs4.html):

430001, 430004, 430005

**Authorize Session** contains the following [Syslog IDs](https://www.cisco.com/c/en/us/td/docs/security/firepower/Syslogs/fptd_syslog_guide/syslogs1.html):

109100, 109101, 109102, 109103, 109104, 113003, 113011, 113034, 113036, 501101, 634001, 734001, 734003, 113015, 113018, 113030, 113031, 113032, 113041, 113042, 730002, 734002, 109016, 109018, 109019, 109020, 109029, 109030, 109032, 109033, 109034, 109035, 109036, 109037, 109038, 610101, 734004