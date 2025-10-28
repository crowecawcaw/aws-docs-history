# Scheduler logs in AWS PCS

You can configure AWS PCS to send detailed logging data from your cluster scheduler to
Amazon CloudWatch Logs, Amazon Simple Storage Service (Amazon S3), and Amazon Data Firehose. This can assist with monitoring and
troubleshooting.

###### Contents

- [Prerequisites](monitoring_scheduler-logs.md#monitoring_scheduler-logs_prereqs "monitoring_scheduler-logs.md#monitoring_scheduler-logs_prereqs")
- [Set up scheduler logs](monitoring_scheduler-logs.md#monitoring_scheduler-logs_setup "monitoring_scheduler-logs.md#monitoring_scheduler-logs_setup")
- [Scheduler log stream paths and
  names](monitoring_scheduler-logs.md#monitoring_scheduler-logs_paths "monitoring_scheduler-logs.md#monitoring_scheduler-logs_paths")
- [Example scheduler log
  record](monitoring_scheduler-logs.md#monitoring_scheduler-logs_record "monitoring_scheduler-logs.md#monitoring_scheduler-logs_record")

## Prerequisites

The IAM principal that manages the AWS PCS cluster must allow the
`pcs:AllowVendedLogDeliveryForResource` action.

The following example IAM policy grants the required permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PcsAllowVendedLogsDelivery",
 "Effect": "Allow",
 "Action": ["pcs:AllowVendedLogDeliveryForResource"],
 "Resource": [
 "arn:aws:pcs:*::cluster/*"
 ]
 }
 ]
}`

```

## Set up scheduler logs

You can set up scheduler logs for your AWS PCS cluster with the AWS Management Console or
AWS CLI.

AWS Management Console

###### To set up scheduler logs with the console

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs "https://console.aws.amazon.com/pcs").
2. In the navigation pane, choose **Clusters**.
3. Choose the cluster where you want to add scheduler logs.
4. On the cluster details page, choose the **Logs** tab.
5. Under **Scheduler Logs**, choose **Add** to add
   up to 3 log delivery destinations from among CloudWatch Logs, Amazon S3, and Firehose.
6. Choose **Update log deliveries**.

AWS CLI

###### To set up scheduler logs with the AWS CLI

1. Create a log delivery destination:

```
aws logs put-delivery-destination --region `region` \
  --name `pcs-logs-destination` \
  --delivery-destination-configuration \
  destinationResourceArn=`resource-arn`
```

Replace:

    * `region` — The AWS Region where you want to create
     the destination, such as `us-east-1`
    * `pcs-logs-destination` — A name for the
     destination
    * `resource-arn` — The Amazon Resource Name (ARN) of a
     CloudWatch Logs log group, S3 bucket, or Firehose delivery stream.

For more information, see [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md") in the _Amazon CloudWatch Logs API Reference_. 2. Set the PCS cluster as a log delivery source:

```
aws logs put-delivery-source --region `region` \
  --name `cluster-logs-source-name` \
  --resource-arn `cluster-arn` \
  --log-type PCS_SCHEDULER_LOGS
```

Replace:

    * `region` — The AWS Region of your cluster, such as
     `us-east-1`
    * `cluster-logs-source-name` — A name for the
     source
    * `cluster-arn` — the ARN of your AWS PCS cluster

For more information, see [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md") in the _Amazon CloudWatch Logs API Reference_. 3. Connect the delivery source to the delivery destination:

```
aws logs create-delivery --region `region` \
  --delivery-source-name `cluster-logs-source` \
  --delivery-destination-arn `destination-arn`
```

Replace:

    * `region` — The AWS Region, such as
     `us-east-1`
    * `cluster-logs-source` — The name of your delivery
     source
    * `destination-arn` — The ARN of your delivery
     destination

For more information, see [CreateDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md") in the _Amazon CloudWatch Logs API Reference_.

## Scheduler log stream paths and

names

The path and name for AWS PCS scheduler logs depend on the destination type.

- **CloudWatch Logs**
  - A CloudWatch Logs stream follows this naming convention.

  ```
  AWSLogs/PCS/${cluster_id}/${log_name}_${scheduler_major_version}.log
  ```

  ###### Example

  ```
  AWSLogs/PCS/abcdef0123/slurmctld_24.05.log
  ```

- **S3 bucket**
  - An S3 bucket output path follows this naming convention:

  ```
  AWSLogs/${account-id}/PCS/${region}/${cluster_id}/${log_name}/${scheduler_major_version}/yyyy/MM/dd/HH/
  ```

  ###### Example

  ```
  AWSLogs/111111111111/PCS/us-east-2/abcdef0123/slurmctld/24.05/2024/09/01/00.
  ```

  - An S3 object name follows this convention:

  ```
  PCS_${log_name}_${scheduler_major_version}_#{expr date 'event_timestamp', format: "yyyy-MM-dd-HH"}_${cluster_id}_${hash}.log
  ```

  ###### Example

  ```
  PCS_slurmctld_24.05_2024-09-01-00_abcdef0123_0123abcdef.log
  ```

## Example scheduler log

record

AWS PCS scheduler logs are structured. They include fields such as the cluster
identifier, scheduler type, major and patch versions, in addition to the log message
emitted from the Slurm controller process. Here is an example.

```
{
    "resource_id": "s3431v9rx2",
    "resource_type": "PCS_CLUSTER",
    "event_timestamp": 1721230979,
    "log_level": "info",
    "log_name": "slurmctld",
    "scheduler_type": "slurm",
    "scheduler_major_version": "25.05",
    "scheduler_patch_version": "3",
    "node_type": "controller_primary",
    "message": "[2024-07-17T15:42:58.614+00:00] Running as primary controller\n"
}
```
