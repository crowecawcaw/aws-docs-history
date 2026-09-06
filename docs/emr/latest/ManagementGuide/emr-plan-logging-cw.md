

# Publish Amazon EMR logs to CloudWatch Logs
<a name="emr-plan-logging-cw"></a>

## Overview
<a name="emr-plan-logging-cw-overview"></a>

Amazon EMR on EC2 provides native integration with Amazon CloudWatch Logs, enabling you to send cluster logs directly to CloudWatch This feature simplifies log management and provides centralized access to your EMR cluster logs for monitoring, troubleshooting, and analysis.

With CloudWatch logging enabled, you can automatically capture and stream logs from your EMR clusters to CloudWatch log groups. This includes step execution logs, Spark driver logs, and Spark executor logs, giving you comprehensive visibility into your cluster operations and application behavior.

The CloudWatch logging feature is available starting with Amazon EMR release 7.11.0 and is configured through the `MonitoringConfiguration` parameter when creating your cluster. Once enabled, logs are automatically streamed to CloudWatch as they are generated, providing near real-time access to log data through the CloudWatch console or API.

## Prerequisites
<a name="emr-plan-logging-cw-prerequisites"></a>

Before enabling CloudWatch logging for your EMR cluster, ensure the following prerequisites are met:
+ **Amazon EMR Release:** Your cluster must use Amazon EMR release 7.11.0 or later.
+ **CloudWatch Agent Application:** The Amazon CloudWatch Agent must be installed on your cluster.
+ **IAM Permissions:** The EC2 instance profile for your cluster must have the required CloudWatch Logs permissions.
+ **VPC Endpoints (for private subnets):** If your cluster is in a private subnet, you must configure VPC endpoints for CloudWatch Logs.

## Permissions
<a name="emr-plan-logging-cw-permissions"></a>

The CloudWatch Agent requires specific AWS Identity and Access Management(IAM) permissions to create log groups, create log streams, and write log events to CloudWatch Logs. These permissions must be attached to the Amazon EC2 instance profile used by your EMR cluster.

### Required IAM policy
<a name="emr-plan-logging-cw-required-policy"></a>

Add the following policy to your [EC2 instance profile for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-role-for-ec2.html) to grant the necessary permissions:

```
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:PutLogEvents",
        "logs:PutRetentionPolicy",
        "logs:DescribeLogStreams",
        "logs:DescribeLogGroups",
        "logs:CreateLogStream",
        "logs:CreateLogGroup"
      ],
      "Resource": "*",
      "Sid": "AllowCWACloudWatchLogs"
    }
  ]
}
```

### Attaching the Policy
<a name="emr-plan-logging-cw-permissions-attaching"></a>

To attach this policy to your EC2 instance profile for EMR:

1. Navigate to the IAM console.

1. Locate the instance profile used by your EMR cluster. which is typically `EMR_EC2_DefaultRole`.

1. Create a new inline policy or attach a customer-managed policy with the permissions above.

1. Save the policy changes.

For more information about IAM roles for Amazon EMR, see [Configure IAM roles for Amazon EMR permissions to AWS services and resources](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-roles.html) in the Amazon EMR Management Guide.

## Configuring CloudWatch Logging
<a name="emr-plan-logging-cw-config"></a>

You can enable CloudWatch logging when creating a new EMR cluster through the AWS Management Console, AWS CLI, or AWS SDKs. The configuration is specified through the `MonitoringConfiguration` parameter.

### Using the AWS Management Console
<a name="emr-plan-logging-cw-config-console"></a>

To create a cluster with CloudWatch logging from the console:

1. Navigate to the [AWS EMR console](https://console.aws.amazon.com/emr/).

1. Choose **Create cluster**.

1. Under **Name and applications**, select an Amazon EMR release of 7.11.0 or higher.

1. Under **Application bundle**, select the applications you want to install and ensure Amazon CloudWatch Agent is included in your selections.

1. Under **Cluster logs**, select the option to **Publish cluster-specific logs to Amazon CloudWatch**.

1. (Optional) Configure the following settings:
   + **Log group name** - Custom log group name. The default is `/aws/emr/{cluster_id}`.
   + **Log stream prefix** - Prefix for log stream names The default is `empty`.
   + **CloudWatch KMS key** - KMS key ARN for log encryption (optional).
   + **Log types** - Select which log types to capture (default: step and Spark driver)

1. Complete the remaining cluster configuration settings.

1. Choose **Create cluster**.

After the cluster is created, you can access the CloudWatch Logs link from the **EMR Cluster Details** page under **Cluster management** → **Log destination** in Amazon CloudWatch.

### Using the AWS CLI
<a name="emr-plan-logging-cw-config-using-the-cli"></a>

You can enable CloudWatch logging using the AWS CLI with the `create-cluster` command. The CloudWatch Agent must be included in the `--applications` parameter, and logging is configured through the `--monitoring-configuration` parameter.

#### Example: Default Configuration
<a name="emr-plan-logging-cw-config-default-configuration"></a>

EMR will automatically capture step logs and Spark driver logs only and send them to the default log group.

```
aws emr create-cluster \
  --name "EMR cluster with CloudWatch Logs" \
  --release-label emr-7.11.0 \
  --applications Name=Spark Name=AmazonCloudWatchAgent \
  --instance-type m7g.2xlarge \
  --instance-count 3 \
  --use-default-roles \
  --monitoring-configuration '{
    "CloudWatchLogConfiguration": {
      "Enabled": true
    }
  }'
```

When using the default configuration:
+ **Log group name:** `/aws/emr/{cluster_id}` (where `{cluster_id}` is automatically replaced with your cluster ID).
+ **Log stream prefix:** Empty (no prefix).
+ **Log types:** `STEP_LOGS` and `SPARK_DRIVER` enabled, each capturing both `STDOUT` and `STDERR`.
+ **Encryption:** No customer managed keys (uses CloudWatch Server-Side Encryption by default)

#### Example: Custom Configuration
<a name="emr-plan-logging-cw-config-default-configuration-custom"></a>

This example demonstrates a custom configuration with specific log group names, KMS encryption, and selective log types.

```
aws emr create-cluster \
  --name "EMR cluster with custom CloudWatch Logs" \
  --release-label emr-7.11.0 \
  --applications Name=Spark Name=AmazonCloudWatchAgent \
  --instance-type m7g.2xlarge \
  --instance-count 3 \
  --use-default-roles \
  --monitoring-configuration '{
    "CloudWatchLogConfiguration": {
      "Enabled": true,
      "LogGroupName": "/my-company/emr/production",
      "LogStreamNamePrefix": "cluster-prod",
      "EncryptionKeyArn": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
      "LogTypes": {
        "STEP_LOGS": ["STDOUT", "STDERR"],
        "SPARK_DRIVER": ["STDOUT", "STDERR"],
        "SPARK_EXECUTOR": ["STDERR", "STDOUT"]
      }
    }
  }'
```

This configuration:
+ Creates logs in a custom log group `/my-company/emr/production`.
+ Prefixes all log stream names with `cluster-prod`.
+ Encrypts logs using the specified KMS key.
+ Captures all log types - step logs, Spark driver logs, and Spark executor logs.

For more information about using the AWS CLI with Amazon EMR, see the [AWS CLI Command Reference for EMR](https://docs.aws.amazon.com/cli/latest/reference/emr/).

### Configuration Reference
<a name="emr-plan-logging-cw-configuration-reference"></a>

#### CloudWatchLogConfiguration Parameters
<a name="emr-plan-logging-cw-configuration-parameters"></a>

The `CloudWatchLogConfigurationv` object supports the following parameters:


**CloudWatchLogConfiguration Parameters**  

| Parameter | Type | Required | Description | 
| --- | --- | --- | --- | 
| Enabled | Boolean | Yes | Set to true to enable CloudWatch logging. Set to false to disable. | 
| LogGroupName | String | No | The CloudWatch log group name. Default: /aws/emr/{cluster\_id} | 
| LogStreamNamePrefix | String | No | Prefix for log stream names. Default: Empty string | 
| EncryptionKeyArn | String | No | ARN of the KMS key for log encryption. If not specified, logs are encrypted by CloudWatch server-side encryption. | 
| LogTypes | Object | No | Specifies which log types to capture. Default: STEP\_LOGS and SPARK\_DRIVER types with STDOUT and STDERR. | 

#### Log types
<a name="emr-plan-logging-cw-configuration-log-types"></a>

Amazon EMR supports three log types, each capturing both standard output and standard error streams:


**Supported Log Types**  

| Log Type | Description | Available Streams | 
| --- | --- | --- | 
| STEP\_LOGS | EMR step execution logs, including step controller logs | STDOUT, STDERR | 
| SPARK\_DRIVER | Apache Spark driver logs from Spark applications | STDOUT, STDERR | 
| SPARK\_EXECUTOR | Apache Spark executor logs from worker nodes | STDOUT, STDERR | 

##### Default log types configuration
<a name="emr-plan-logging-cw-default-log-types"></a>

When you don't specify the `LogTypes` parameter, EMR uses the following default configuration:

```
"LogTypes": {
  "STEP_LOGS": ["STDOUT", "STDERR"],
  "SPARK_DRIVER": ["STDOUT", "STDERR"]
}
```

##### Custom log types configuration
<a name="emr-plan-logging-cw-default-log-types-configuration"></a>

You can customize which log types to capture by explicitly specifying the `LogTypes` parameter. For example, to capture only step logs:

```
"LogTypes": {
  "STEP_LOGS": ["STDOUT", "STDERR"]
}
```

Or to capture only standard error from Spark drivers:

```
"LogTypes": {
  "SPARK_DRIVER": ["STDERR"]
}
```

#### Log group and stream naming
<a name="emr-plan-logging-cw-log-group-and-stream-naming"></a>

CloudWatch organizes logs into log groups and log streams:
+ **Log Group:** A collection of log streams that share the same retention, monitoring, and access control settings.
  + **Default name:** `/aws/emr/{cluster_id}`
  + **Custom name:** Any valid CloudWatch log group name you specify.
+ **Log Stream:** A sequence of log events from a single source:
  + Naming patterns:
    + **Step logs:** `{prefix}/steps/{step_id}/{file_name}`.
    + **Spark driver and executor logs:** `{prefix}/applications/{application_id}/{container_id}/{file_name}`
  + Examples:
    + `/steps/s-ABCDEFG123456/stdout`
    + `cluster-prod/steps/s-ABCDEFG123456/stderr`
    + `/applications/application_1234567890_0001/container_1234567890_0001_01_000001/stdout`

### Encrypting Logs with AWS KMS
<a name="emr-plan-logging-cw-encrypting-logs-with-kms"></a>

You can encrypt your CloudWatch logs at rest using AWS Key Management Service (KMS). To enable encryption:

1. Create or identify a KMS key in the same AWS Region as your EMR cluster.

1. Ensure the KMS key policy allows the CloudWatch Logs service to use the key.

1. Add the `EncryptionKeyArn` parameter to your `CloudWatchLogConfiguration`.

For detailed information about encrypting CloudWatch Logs data, see [Encrypt log data in CloudWatch Logs using AWS Key Management Service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html).

#### Example with KMS Encryption
<a name="emr-plan-logging-cw-encrypting-logs-with-kms-example"></a>

```
{
  "CloudWatchLogConfiguration": {
    "Enabled": true,
    "EncryptionKeyArn": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
  }
}
```

### Viewing Logs in CloudWatch
<a name="emr-plan-logging-cw-viewing-logs"></a>

After your cluster is running with CloudWatch logging enabled, you can view and analyze your logs through the CloudWatch console or API.

#### Accessing Logs from the EMR Console
<a name="emr-plan-logging-cw-viewing-accessing"></a>

The fastest way to access your cluster logs is directly from the EMR console:

1. Navigate to the Amazon EMR console.

1. Select your cluster from the cluster list.

1. On the cluster details page, locate the **Cluster management** section.

1. Click the **Log destination in Amazon CloudWatch** link.

This link takes you directly to the CloudWatch Logs console filtered to your cluster's log group.

#### Accessing Logs from the CloudWatch console
<a name="emr-plan-logging-cw-viewing-accessing-console"></a>

To manually navigate to your logs in CloudWatch:

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Log groups**.

1. Find your log group (default: `/aws/emr/{cluster_id}` or your custom log group name)

1. Choose the log group to view available log streams.

1. Select a log stream to view its log events.

For more information about working with CloudWatch Logs, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/).

### Considerations
<a name="emr-plan-logging-cw-considerations"></a>

#### CloudWatch Agent Behavior
<a name="emr-plan-logging-cw-considerations-agent-behavior"></a>

The Amazon CloudWatch Agent provides both metrics and logging capabilities:
+ Enabling the CloudWatch Agent alone (without `MonitoringConfiguration`) publishes only CloudWatch metrics to CloudWatch. No logs are sent.
+ Enabling CloudWatch logging requires both the CloudWatch Agent application and the `MonitoringConfiguration` parameter with `CloudWatchLogConfiguration`. This enables metrics and logging together.

#### Enabling CloudWatch logging only (Disabling CloudWatch Metrics)
<a name="emr-plan-logging-cw-considerations-disabling"></a>

If you want to enable CloudWatch logging but disable the metrics collection feature, you can configure the CloudWatch Agent to stop exporting metrics. Add the following classification to your cluster configuration:

```
[
  {
    "Classification": "emr-metrics",
    "Properties": {},
    "Configurations": [
      {
        "Classification": "emr-system-metrics",
        "Properties": {},
        "Configurations": []
      }
    ]
  }
]
```

For more information about CloudWatch metrics, see [Monitor metrics with Amazon CloudWatch](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/AmazonCloudWatchAgent-metrics.html).

#### Known Limitations
<a name="emr-plan-logging-cw-considerations-disabling-known"></a>

Metrics Data Points During Log Uploads:  
When CloudWatch logging is active, you may observe occasional gaps in CloudWatch metrics data during periods of high log activity, particularly during step submissions. This occurs because the EMR instance controller restarts the CloudWatch Agent to apply new log configurations when steps are submitted, temporarily interrupting metrics collection. This does not affect log delivery or cluster functionality.

#### Private Subnet Requirements
<a name="emr-plan-logging-cw-considerations-disabling-known-private"></a>

To publish logs to CloudWatch Logs for an EMR cluster in a private subnet, create and associate the CloudWatch Logs VPC endpoint with your cluster's VPC.

For more information about CloudWatch Logs endpoints, see [Amazon CloudWatch Logs endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cwl_region.html) in the *AWS General Reference Guide*.

#### Cost Considerations
<a name="emr-plan-logging-cw-cost-considerations"></a>

CloudWatch Logs charges are based on:
+ **Data ingestion:** Volume of log data ingested into CloudWatch
+ **Storage:** Amount of log data stored, based on your retention settings
+ **Data analysis:** Queries run using CloudWatch Logs Insights

To optimize costs:
+ Set appropriate log retention periods for your log groups.
+ Use selective log types to capture only the logs you need.
+ Consider using Amazon S3 logging for long-term log storage at lower cost.

For current pricing information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

### Additional Resources
<a name="emr-plan-logging-cw-additional-resources"></a>
+ [Monitor metrics with Amazon CloudWatch](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/AmazonCloudWatchAgent-metrics.html) - Information about CloudWatch metrics collection
+ [Configure IAM roles for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-roles.html) - IAM role configuration for EMR clusters
+ [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/) - Complete guide to CloudWatch Logs features
+ [AWS CLI Command Reference for EMR](https://docs.aws.amazon.com/cli/latest/reference/emr/) - CLI reference documentation