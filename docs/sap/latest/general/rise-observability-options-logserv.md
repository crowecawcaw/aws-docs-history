

# SAP LogServ
<a name="rise-observability-options-logserv"></a>

SAP LogServ gives you visibility into the operating system, database, and SAP application layers of your RISE with SAP landscape. SAP manages these layers, and you cannot access them directly. With LogServ, you can collect these logs and observe your landscape from within your own AWS account. This addresses the observability gap in the RISE with SAP shared responsibility model by making SAP-managed infrastructure logs available to your own security and operations teams.

## Overview
<a name="_overview"></a>

SAP LogServ is an SAP-managed service, part of SAP Enterprise Cloud Services, that collects, stores, forwards, and provides access to logs from across a RISE with SAP landscape.

SAP LogServ has two zones. A Data Landing Zone (DLZ) collects and pre-processes logs from across the SAP-managed landscape. The DLZ then feeds a per-customer Customer Landing Zone (CLZ), an isolated data lake in the SAP RISE managed account that holds your logs. The CLZ provides an Amazon Simple Storage Service (Amazon S3) object store and Amazon Simple Queue Service (Amazon SQS) event notifications. SAP retains logs in the CLZ for 365 days by default.

The logs cover three high-level families:
+  **Operating system logs**: for example, Linux system messages, authentication and `sudo` logs, cron, and (on Windows hosts) Windows Event Log entries.
+  **Database logs and traces**: for example, SAP HANA audit logs and trace files.
+  **SAP application logs**: from SAP NetWeaver Application Server for ABAP, SAP HANA, SAP NetWeaver Application Server for Java, and SAP Web Dispatcher (for example, work process, dispatcher, ICM, and message server traces).

These log families map to the categories and subcategories you filter on when you deploy the forwarder (see [Prerequisites](#rise-observability-options-logserv-prerequisites) and the forwarder guidance for the full category list).

The ** AWS SAP LogServ log forwarder** is a customer-deployed reference solution, published by AWS, that brings this log data out of the SAP-managed CLZ and into a destination Amazon S3 bucket in your own AWS account. The rest of this section describes that forwarder solution.

## How the log forwarder works
<a name="_how_the_log_forwarder_works"></a>

The log forwarder is an AWS Lambda function that runs in your own AWS account. When SAP writes a new object to the CLZ Amazon S3 bucket, the forwarder receives an Amazon SQS notification, reads the file, and applies optional category filtering. It then decompresses the gzip-compressed newline-delimited JSON (`.json.gz`) and copies the result to a destination Amazon S3 bucket in your account, organized by category and date.

From there, you query the logs with Amazon Athena, Amazon OpenSearch Service, or Amazon CloudWatch, or forward them to a third-party security information and event management (SIEM) system.

Each decompressed line is a JSON record with a consistent envelope: `_raw` (the original log line, exactly as written by the source), `_time` (Unix epoch timestamp), `source` (original log file path), `host`, `clz_dir` (log category), `clz_subdir` (log subcategory), and `clzfilename` (original filename). The format of the `_raw` field itself varies by log type. Use this schema when you build Athena tables or SIEM parsing rules; the forwarder guidance documents it in full.

## Architecture
<a name="_architecture"></a>

The solution spans two AWS accounts. The SAP RISE managed account holds the CLZ source Amazon S3 bucket and the Amazon SQS notification queue. Your own (self-managed) AWS account hosts the forwarder and the destination Amazon S3 bucket. This account is distinct from the SAP-managed AWS accounts in your RISE landscape. A cross-account trust boundary separates the two accounts, and that boundary is enforced by AWS Identity and Access Management (IAM) and Transport Layer Security (TLS) 1.2 or later.

SAP grants your account access through resource policies on the SAP RISE side. A bucket policy on the CLZ bucket grants your account read access, and a queue policy on the notification queue grants your account receive, delete, and get-attributes permissions. The queue triggers the forwarder Lambda function. The function validates and filters each qualifying file, decompresses it, and copies it to your destination bucket for your downstream consumers to read.

The following diagram shows how the log forwarder moves data from the SAP RISE managed account to your own AWS account.

![CLZ source bucket and queue in the SAP RISE account feed the forwarder Lambda and destination bucket in your own account](https://docs.aws.amazon.com/sap/latest/general/images/rise-observability-logserv.png)


## Prerequisites
<a name="rise-observability-options-logserv-prerequisites"></a>

Before you can deploy the forwarder, you must obtain the LogServ entitlement and cross-account access from SAP:

1. Work with your SAP account team to add the LogServ SKU to your RISE with SAP entitlement.

1. After SAP confirms the SKU is added, raise the SAP Service Request titled **"Manage security LogServ & Raven"** to obtain cross-account access. Provide SAP with the AWS account IDs that need access to the CLZ source Amazon S3 bucket and the Amazon SQS notification queue.

1. SAP then provides the values you need to configure the forwarder: the source Amazon S3 bucket name, the Amazon SQS queue name, and the SAP RISE AWS account ID (the account ID is typically embedded in the bucket and queue names).

You also need the [AWS Serverless Application Model (AWS SAM) CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) installed and AWS CLI credentials configured for your target account.

## Deployment
<a name="_deployment"></a>

You deploy the forwarder with AWS SAM. The forwarder’s SAM template defines a set of CloudFormation parameters, so you tailor its behavior without changing code. The following table shows the four required connection inputs; the forwarder guidance documents every parameter.


| Input | Description | 
| --- | --- | 
|  `DestBucketName`  | The destination Amazon S3 bucket in your account where the forwarder writes processed logs. | 
|  `SourceBucketName`  | The CLZ source Amazon S3 bucket provided by SAP. Also acts as an allowlist: events naming a different bucket are rejected before the object is read. | 
|  `SourceSqsQueueName`  | The CLZ notification queue name provided by SAP. | 
|  `SourceAwsAccountId`  | The AWS account ID of the SAP RISE managed account that owns the source bucket and queue. | 

The remaining parameters are optional and fall into three groups:
+  **Content and filtering**: control which logs you keep and how they are stored: `IncludeCategories`, `ExcludeSubcategories`, `ForwardAWSLogs`, `Decompress`, `DestPrefix`, and `RetentionDays`.
+  **Performance**: tune throughput: `BatchSize`, `BatchWindow`, `ReservedConcurrency`, `MaxFileSizeMB`, and `EmitMetrics` (see [Cost](#rise-observability-options-logserv-cost) for the cost impact of enabling metrics).
+  **Security and access**: scope who can read the data and how it is monitored: `AllowedPrincipalArns`, `AlarmNotificationTopicArn`, and `AccessLogBucketName`.

The two filtering parameters are the first things most customers configure:
+  `IncludeCategories` is an allowlist. Set it to forward only the categories you need. For example, `hana,linux,abap`. Leave it blank to forward all categories. Valid values are `abap`, `dns`, `hana`, `linux`, `sap`, `scc`, `webdispatcher`, `bobj_bi`, `bobj_bods`, `bobj_sacagent`, `sybase`, `java`, and `windows`.
+  `ExcludeSubcategories` is a denylist applied regardless of category. For example, `audit,proxy,slapd`.

For more information about deployment steps and the complete parameter reference, see [Guidance for SAP Log ingestion to AWS Services](https://github.com/aws-for-sap/Guidance-for-SAP-Log-ingestion-to-AWS-Services/tree/main/aws-sap-logserv-forwarder) on GitHub.

## Cost
<a name="rise-observability-options-logserv-cost"></a>

As of mid-2026, a typical single-SID landscape costs roughly USD 25 to 40 per month with metrics off, or roughly USD 40 to 60 per month with metrics on. Amazon S3 storage dominates the run cost. Cost scales roughly linearly with log volume, so multiply by the number of active SIDs for a multi-SID landscape. For precise, Region-specific estimates, use the [AWS Pricing Calculator](https://calculator.aws/).

To manage cost:
+ Filter early with `IncludeCategories` and `ExcludeSubcategories` so you forward only the logs you need.
+ Right-size `RetentionDays` to your compliance requirement. Note that the SAP CLZ retains source logs for only 365 days, so setting a shorter destination retention means logs cannot be re-forwarded from source after they expire locally.
+ Choose an appropriate Amazon S3 storage class. By default the destination bucket transitions objects to S3 Intelligent-Tiering after 30 days; for write-once, rarely-read logs you can instead transition to S3 Standard-Infrequent Access (S3 Standard-IA), which can reduce storage cost by roughly 40%. The forwarder guidance describes how to customize the lifecycle policy.
+ Leave `EmitMetrics` off unless you need the CloudWatch metrics, because they add roughly USD 15 to 20 per month.

## Security
<a name="_security"></a>
+  **Encryption at rest**: The destination Amazon S3 bucket uses SSE-S3 (AES-256), and the dead-letter queue uses the AWS managed SSE-SQS key.
+  **Encryption in transit**: All access uses TLS 1.2 or later, and the destination bucket policy denies non-TLS requests.
+  **Amazon S3 hardening**: All four public access block settings are enabled, and object versioning is enabled.
+  **Least-privilege access**: The AWS Lambda execution role is scoped to only the actions and resources it needs (`s3:PutObject` on the destination, `s3:GetObject` on the source, and the specific queue ARN). Cross-account read access to the destination is granted to specific IAM principals through `AllowedPrincipalArns` (not to account-root) and is conditional on secure transport.
+  **Input validation and hardening**: The forwarder validates Amazon S3 keys, pins the source bucket, enforces file-size limits against the object’s real size, protects against decompression bombs, and sanitizes log output.
+  **Auditability**: Optional Amazon S3 server access logging and Amazon CloudWatch alarms provide monitoring and audit evidence.

You are responsible for validating that these controls meet your organization’s requirements before you deploy to production.

 **Key management (SSE-KMS).** The reference solution encrypts the destination bucket with SSE-S3 and does not currently expose a parameter for SSE-KMS with a customer managed key. If your compliance framework requires a customer managed key, treat this as a known limitation of the reference template. You can either modify the template to set the bucket encryption to `aws:kms` with your key, or point the forwarder at an existing SSE-KMS bucket by setting `CreateDestBucket` to `false`. In both cases you must also extend the AWS Lambda execution role with `kms:GenerateDataKey` and `kms:Decrypt` on your key, which the reference role does not grant by default.

 **Network (VPC).** The forwarder Lambda function runs outside a VPC and reaches the cross-account Amazon SQS queue and Amazon S3 buckets over public AWS service endpoints, secured with TLS 1.2 or later. It needs no access to private VPC resources, and running outside a VPC avoids elastic network interface (ENI) cold-start latency and subnet IP-address consumption. If your security posture requires AWS API traffic to stay on private networking, attach the function to a VPC and add Amazon S3 and Amazon SQS VPC endpoints, along with the associated networking permissions. The reference template does not configure VPC networking today.

## Performance and scaling
<a name="_performance_and_scaling"></a>

 AWS Lambda suits this workload because log forwarding is event-driven, bursty, short-lived, and stateless. Lambda scales automatically up to `ReservedConcurrency` and costs nothing when idle.

A single landscape typically produces around 100 to 200 files per minute, well within the operating range of Lambda. If you need more throughput, increase `BatchSize` before you scale out concurrency. An always-on model, such as AWS Fargate or Lambda provisioned concurrency, only becomes cost-effective at sustained high volume around the clock, typically only when many landscapes feed one forwarder. If you enable `EmitMetrics`, the forwarder publishes a files-per-minute metric you can use to judge when that crossover applies.

## Monitoring and troubleshooting
<a name="_monitoring_and_troubleshooting"></a>

The forwarder ships with operational monitoring so you can run it day to day:
+  **Alarms**: When you provide an Amazon SNS topic through `AlarmNotificationTopicArn`, the solution notifies you on three Amazon CloudWatch alarms: any message landing in the dead-letter queue (DLQ), Lambda errors above 10 per 5-minute window, and Lambda throttles above 5 per 5-minute window.
+  **Dead-letter queue**: The DLQ preserves messages that fail processing, with 14-day retention. Because the SAP CLZ retains source logs for 365 days, you have ample time to investigate and reprocess. The forwarder retries transient failures automatically. It logs and skips permanent failures (for example, an oversized object or corrupt gzip) rather than retrying them indefinitely.
+  **Metrics and dashboards**: With `EmitMetrics` enabled, the forwarder emits per-file and per-batch CloudWatch metrics (files processed, filtered, and failed; processing time; batch size) under the `SAP/LogServ` namespace. Useful widgets include files per minute (throughput and cost-crossover signal), average and p99 processing time, batch utilization, and an error rate derived from files failed over files processed.

For the full list of alarms, metrics, dimensions, and recommended dashboard widgets, see the forwarder guidance.