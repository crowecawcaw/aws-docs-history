

# Scheduler logs in AWS PCS
<a name="monitoring_scheduler-logs"></a>

You can configure AWS PCS to send detailed logging data from your cluster scheduler to Amazon CloudWatch Logs, Amazon Simple Storage Service (Amazon S3), and Amazon Data Firehose. This can assist with monitoring and troubleshooting.

AWS PCS delivers logs from the following Slurm daemons through the `PCS_SCHEDULER_LOGS` log type:
+ **`slurmctld`** — The Slurm controller daemon. Available for all supported Slurm versions.
+ **`slurmdbd`** — The Slurm database daemon. Available for Slurm 24.11 and later.
+ **`slurmrestd`** — The Slurm REST API daemon. Available for Slurm 25.05 and later.

Clusters that already have `PCS_SCHEDULER_LOGS` delivery configured automatically start receiving `slurmdbd` and `slurmrestd` logs when they run a supported Slurm version. No additional configuration is required.

**Contents**
+ [Prerequisites](#monitoring_scheduler-logs_prereqs)
+ [Set up scheduler logs](#monitoring_scheduler-logs_setup)
+ [Scheduler log stream paths and names](#monitoring_scheduler-logs_paths)
+ [Example scheduler log records](#monitoring_scheduler-logs_record)

## Prerequisites
<a name="monitoring_scheduler-logs_prereqs"></a>

The IAM principal that manages the AWS PCS cluster must allow the `pcs:AllowVendedLogDeliveryForResource` action.

The following example IAM policy grants the required permissions.

------
#### [ JSON ]

****  

```
{
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
}
```

------

## Set up scheduler logs
<a name="monitoring_scheduler-logs_setup"></a>

You can set up scheduler logs for your AWS PCS cluster with the AWS Management Console or AWS CLI.

------
#### [ AWS Management Console ]

**To set up scheduler logs with the console**

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs).

1. In the navigation pane, choose **Clusters**.

1. Choose the cluster where you want to add scheduler logs.

1. On the cluster details page, choose the **Logs** tab.

1. Under **Scheduler Logs**, choose **Add** to add up to 3 log delivery destinations from among CloudWatch Logs, Amazon S3, and Firehose.

1. Choose **Update log deliveries**.

------
#### [ AWS CLI ]

**To set up scheduler logs with the AWS CLI**

1. Create a log delivery destination:

   ```
   aws logs put-delivery-destination --region {{region}} \
     --name {{pcs-logs-destination}} \
     --delivery-destination-configuration \
     destinationResourceArn={{resource-arn}}
   ```

   Replace:
   + {{region}} — The AWS Region where you want to create the destination, such as `us-east-1`
   + {{pcs-logs-destination}} — A name for the destination
   + {{resource-arn}} — The Amazon Resource Name (ARN) of a CloudWatch Logs log group, S3 bucket, or Firehose delivery stream.

   For more information, see [PutDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html) in the *Amazon CloudWatch Logs API Reference*.

1. Set the PCS cluster as a log delivery source:

   ```
   aws logs put-delivery-source --region {{region}} \
     --name {{cluster-logs-source-name}} \
     --resource-arn {{cluster-arn}} \
     --log-type PCS_SCHEDULER_LOGS
   ```

   Replace:
   + {{region}} — The AWS Region of your cluster, such as `us-east-1`
   + {{cluster-logs-source-name}} — A name for the source
   + {{cluster-arn}} — the ARN of your AWS PCS cluster

   For more information, see [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html) in the *Amazon CloudWatch Logs API Reference*.

1. Connect the delivery source to the delivery destination:

   ```
   aws logs create-delivery --region {{region}} \
     --delivery-source-name {{cluster-logs-source}} \
     --delivery-destination-arn {{destination-arn}}
   ```

   Replace:
   + {{region}} — The AWS Region, such as `us-east-1`
   + {{cluster-logs-source}} — The name of your delivery source
   + {{destination-arn}} — The ARN of your delivery destination

   For more information, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) in the *Amazon CloudWatch Logs API Reference*.

------

## Scheduler log stream paths and names
<a name="monitoring_scheduler-logs_paths"></a>

 The path and name for AWS PCS scheduler logs depend on the destination type. 

The `${log_name}` value in the paths below is `slurmctld`, `slurmdbd`, or `slurmrestd`, depending on the daemon that produced the log.
+ **CloudWatch Logs**
  + A CloudWatch Logs stream follows this naming convention.

    ```
    AWSLogs/PCS/${cluster_id}/${log_name}_${scheduler_major_version}.log
    ```  
**Example**  

    ```
    AWSLogs/PCS/abcdef0123/slurmctld_25.11.log
    AWSLogs/PCS/abcdef0123/slurmdbd_24.11.log
    AWSLogs/PCS/abcdef0123/slurmrestd_25.05.log
    ```
+ **S3 bucket**
  + An S3 bucket output path follows this naming convention:

    ```
    AWSLogs/${account-id}/PCS/${region}/${cluster_id}/${log_name}/${scheduler_major_version}/yyyy/MM/dd/HH/
    ```  
**Example**  

    ```
    AWSLogs/111111111111/PCS/us-east-2/abcdef0123/slurmctld/25.11/2024/09/01/00/
    AWSLogs/111111111111/PCS/us-east-2/abcdef0123/slurmdbd/24.11/2024/09/01/00/
    AWSLogs/111111111111/PCS/us-east-2/abcdef0123/slurmrestd/25.05/2024/09/01/00/
    ```
  + An S3 object name follows this convention:

    ```
    PCS_${log_name}_${scheduler_major_version}_#{expr date 'event_timestamp', format: "yyyy-MM-dd-HH"}_${cluster_id}_${hash}.log
    ```  
**Example**  

    ```
    PCS_slurmctld_25.11_2024-09-01-00_abcdef0123_0123abcdef.log
    ```

## Example scheduler log records
<a name="monitoring_scheduler-logs_record"></a>

AWS PCS scheduler logs are structured. They include fields such as the cluster identifier, scheduler type, major and patch versions, in addition to the log message emitted from the Slurm daemon process. The `log_name` and `node_type` fields identify which daemon produced the log.

The following example shows a `slurmctld` log record.

```
{
    "resource_id": "s3431v9rx2",
    "resource_type": "PCS_CLUSTER",
    "event_timestamp": 1721230979,
    "log_level": "info",
    "log_name": "slurmctld",
    "scheduler_type": "slurm",
    "scheduler_major_version": "25.11",
    "scheduler_patch_version": "2",
    "node_type": "controller_primary",
    "message": "[2024-07-17T15:42:58.614+00:00] Running as primary controller\n"
}
```

The following example shows a `slurmdbd` log record (Slurm 24.11 and later).

```
{
    "resource_id": "pcs_bu93qsds2j",
    "resource_type": "PCS_CLUSTER",
    "event_timestamp": 1774485082772,
    "log_level": "info",
    "log_name": "slurmdbd",
    "scheduler_type": "slurm",
    "scheduler_major_version": "25.11",
    "scheduler_patch_version": "2",
    "node_type": "slurmdbd_primary",
    "message": "[2026-03-26T00:31:22.772+00:00] mysql_common: storage token refreshed"
}
```

The following example shows a `slurmrestd` log record (Slurm 25.05 and later).

```
{
    "resource_id": "pcs_bu93qsds2j",
    "resource_type": "PCS_CLUSTER",
    "event_timestamp": 1774485082772,
    "log_level": "info",
    "log_name": "slurmrestd",
    "scheduler_type": "slurm",
    "scheduler_major_version": "25.05",
    "scheduler_patch_version": "3",
    "node_type": "slurmrestd_primary",
    "message": "[2026-03-26T00:31:22.772+00:00] slurmrestd: Listening on port 6820\n"
}
```