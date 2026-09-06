

# Source configuration for Zeek
<a name="zeek-source-setup"></a>

## Integrating with Zeek
<a name="zeek-integration"></a>

To integrate Zeek with CloudWatch Logs, you must configure both the source and the pipeline. First, set up your Zeek source by configuring Amazon S3 and Amazon SQS to receive data. Then, configure the CloudWatch pipeline to ingest the data from your source into CloudWatch Logs.

## Instructions to setup Amazon S3 and Amazon SQS
<a name="zeek-s3-sqs-setup"></a>

Configuring Zeek with Fluent Bit to send logs to an Amazon S3 bucket involves several steps, primarily focused on setting up the Amazon S3 bucket, Amazon SQS queue, IAM roles, and then configuring the CloudWatch Pipeline.

**Configuring Zeek logs using Fluent Bit**
+ Install Fluent Bit (a lightweight log collector that reads log files and forwards them to destinations such as Amazon S3) on the Zeek host and configure it to tail Zeek log files (for example, `/opt/zeek/logs/current/*.log`).
+ Configure AWS credentials (IAM role or `aws configure`) so Fluent Bit has permission to upload objects to the Amazon S3 bucket.
+ Update the Fluent Bit configuration to use the S3 output plugin, specifying the bucket name, Region, and S3 key path for Zeek logs.
+ Start and enable the Fluent Bit service to continuously collect Zeek logs and upload them to Amazon S3 for downstream ingestion.

**Amazon S3 and Amazon SQS configuration**
+ Amazon S3 bucket that stores the Zeek logs should reside in the same AWS Region.
+ Configure the Amazon S3 bucket to create event notifications, specifically for "Object Create" events. These notifications should be sent to an Amazon SQS queue.
+ Create an Amazon SQS queue in the same AWS Region as your Amazon S3 bucket. This queue will receive notifications when new log files are added to the Amazon S3 bucket.

## Configuring the CloudWatch Pipeline
<a name="zeek-pipeline-config"></a>

When configuring the pipeline to read data from Zeek, choose Zeek as the data source. After filling in the required information and you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="zeek-ocsf-support"></a>

This integration supports OCSF schema version v1.5.0 and events that map to multiple OCSF classes. The following table lists the supported event mappings.


| Event name | OCSF class | 
| --- | --- | 
| conn | Network Activity (4001) | 
| dns | DNS Activity (4003) | 
| http | HTTP Activity (4002) | 
| ssl | Network Activity (4001) | 
| ssh | SSH Activity (4007) | 
| kerberos | Authentication (3002) | 
| rdp | RDP Activity (4005) | 
| files | Network Activity (4001) | 
| notice | Detection Finding (2004) | 
| known\_hosts | Base Event (0) | 
| x509 | Network Activity (4001) | 
| ftp | FTP Activity (4008) | 
| smtp | Email Activity (4009) | 
| dhcp | DHCP Activity (4004) | 
| ntlm | Authentication (3002) | 
| smb\_files | SMB Activity (4006) | 
| smb | SMB Activity (4006) | 
| dce\_rpc | SMB Activity (4006) | 
| ldap | Authentication (3002) | 
| ldap\_search | Network Activity (4001) | 
| quic | Network Activity (4001) | 
| tunnel | Tunnel Activity (4014) | 
| pe | Base Event (0) | 
| weird | Base Event (0) | 
| known\_services | Base Event (0) | 
| software | Software Inventory Info (5020) | 
| reporter | Base Event (0) | 

Events that do not match any OCSF mapping transformation are automatically passed through and sent directly to the configured sink without additional processing.