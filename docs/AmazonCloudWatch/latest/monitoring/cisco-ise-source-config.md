

# Source configuration for Cisco ISE
<a name="cisco-ise-source-config"></a>

## Integrating with Cisco ISE
<a name="cisco-ise-integration"></a>

CloudWatch Pipeline ingests Cisco ISE log data from Amazon S3. You configure ISE to forward syslog to a Fluent Bit host, which compresses and uploads the logs to Amazon S3. The pipeline then reads from Amazon S3 using Amazon SQS notifications.

To integrate CloudWatch Pipelines with Cisco ISE, complete the following high-level steps:
+ Configure ISE Remote Logging Target to forward syslog to a Fluent Bit host.
+ Assign the Remote Target to the desired Logging Categories.
+ Install and configure Fluent Bit to receive syslog and upload to Amazon S3.
+ Create an Amazon S3 bucket and Amazon SQS queue with event notifications.
+ Create a CloudWatch pipeline with Cisco ISE as the data source.
+ Verify that data is flowing into the pipeline.

## Prerequisites
<a name="cisco-ise-prerequisites"></a>

Before you begin, make sure you have the following:
+ Active Cisco ISE deployment (version 2.x or 3.x) with administrative access to configure Remote Logging Targets and Logging Categories
+ Network connectivity from ISE nodes to the Fluent Bit host (TCP port configurable, default 1514)
+ Fluent Bit installed on a host reachable from all ISE nodes generating logs
+ AWS credentials configured for Fluent Bit to write to Amazon S3
+ An AWS account with [permissions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/pipeline-iam-reference.html#api-caller-permissions) to create and manage CloudWatch Pipelines
+ An AWS account with permissions to create and manage CloudWatch Logs log groups

## Instructions to set up Cisco ISE, Fluent Bit, Amazon S3 and Amazon SQS
<a name="cisco-ise-s3-sqs-setup"></a>

1. **Configure ISE Remote Logging Target**

   In the ISE Admin Console, navigate to **Administration > System > Logging > Remote Logging Targets > Add**. Configure the following settings:
   + **Name:** Descriptive name (for example, `FluentBit_S3_Collector`)
   + **Target Type:** `TCP Syslog` or `Secure Syslog` (TCP\+TLS) recommended for reliability
   + **Status:** Enabled
   + **Host/IP Address:** Fluent Bit host IP or FQDN
   + **Port:** Must match Fluent Bit listener port (for example, 1514)
   + **Maximum Length:** Set to **8192** (default 1024 will truncate messages)
   + **Comply to RFC 3164:** Check this box

1. **Assign Remote Target to Logging Categories**

   Navigate to **Administration > System > Logging > Logging Categories**. For each desired category, move the remote target from "Available" to "Selected".
   + **Categories from PSN nodes only:** AAA Audit, AAA Diagnostics, Accounting, Profiler, Posture, External MDM, Passive ID
   + **Categories from all nodes:** Administrative and Operational Audit, System Diagnostics, System Statistics

   Ensure Fluent Bit is reachable from all ISE nodes that generate the selected categories.

1. **Install and configure Fluent Bit**

   Install Fluent Bit on the designated log collection host. Configure Fluent Bit with a TCP input to receive syslog from ISE and an Amazon S3 output plugin:

   ```
   [SERVICE]
       Flush        5
       Log_Level    info
   
   [INPUT]
       Name         tcp
       Tag          cisco.ise
       Listen       0.0.0.0
       Port         1514
       Format       none
       Separator    \n
   
   [OUTPUT]
       Name         s3
       Match        cisco.ise
       bucket       <your-bucket-name>
       region       <your-region>
       s3_key_format /cisco-ise-logs/$TAG/%Y/%m/%d/%H/%M/$UUID.gz
       total_file_size 5M
       upload_timeout 60s
       use_put_object On
       compression  gzip
       content_type application/gzip
       store_dir    /tmp/fluent-bit-s3
       log_key      log
   ```
**Note**  
Maximum message length in ISE MUST be set to 8192 to avoid truncation of verbose ISE syslog messages. Fluent Bit uses TCP input (not the built-in syslog input) because ISE's syslog format is not fully RFC 3164 compliant. The `log_key` parameter ensures only the raw log line is written to Amazon S3 (without Fluent Bit metadata).

1. **Create Amazon S3 bucket and Amazon SQS queue**

   Create an Amazon S3 bucket in your desired AWS region to receive Cisco ISE logs. Create an Amazon SQS queue in the same region and configure the Amazon S3 bucket to send "Object Create" event notifications to the Amazon SQS queue.

1. **Verify log delivery**

   Use ISE TCP Dump (**Operations > Troubleshoot > TCP Dump**) filtered by Fluent Bit IP to confirm log delivery from ISE. Verify objects appear in the Amazon S3 bucket under the configured prefix.

## Configuring the CloudWatch Pipeline
<a name="cisco-ise-pipeline-config"></a>

When configuring the pipeline, choose **Cisco ISE** as the data source. Configure the Amazon S3 bucket and Amazon SQS queue details and select the destination log group. After you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Data flow
<a name="cisco-ise-data-flow"></a>

```
Cisco ISE -> Fluent Bit (TCP Syslog) -> Amazon S3 -> Amazon SQS Notification -> CloudWatch Pipeline -> CloudWatch Logs
```

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="cisco-ise-ocsf-support"></a>

This integration supports **OCSF schema version v1.5.0**. Cisco ISE syslog events are parsed using a custom ISE syslog parser and mapped to OCSF classes based on the ISE logging category and message code.


| ISE Event Type | OCSF Event Class | Description | 
| --- | --- | --- | 
| Failed Attempts | Authentication (3002) | Failed RADIUS authentication and authorization attempts | 
| Passed Authentication | Authentication (3002) | Successful RADIUS authentication and authorization events | 
| Radius Accounting | Network Activity (4001), Tunnel Activity (4014) | RADIUS accounting start, stop, and interim update events (codes 3000-3004). RADIUS tunnel-related accounting events (codes 3005-3010). | 
| Policy Diagnostics | Authentication (3002) | Policy evaluation and matching diagnostic events | 
| Identity Store Diagnostics | Authentication (3002) | Identity store lookup and validation diagnostic events | 
| Authentication Flow Diagnostics | Authentication (3002) | Authentication flow processing diagnostic events | 
| Administrative and Operational Audit | Authentication (3002), Account Change (3001), Entity Management (3004), Application Lifecycle (6002), Application Error (6008), API Activity (6003), Network Activity (4001), Detection Finding (2004) | Administrative actions, system operations, and configuration changes mapped by message code | 
| Guest | Web Resources Activity (6004) | Guest portal access and lifecycle events (codes 86001, 86005, 86012, 86021-86023, 86030-86031) | 

The following event types are ingested but not currently mapped to OCSF classes (forwarded as raw logs):
+ Radius Diagnostics
+ Administrator Authentication and Authorization
+ Posture and Client Provisioning Audit
+ Posture and Client Provisioning Diagnostics
+ Profiler
+ System Diagnostics
+ Distributed Management
+ Internal Operations Diagnostics
+ System Statistics

Events that do not match any OCSF mapping transformation are automatically passed through and sent directly to the configured sink without additional processing.