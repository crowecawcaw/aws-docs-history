

# Scheduler audit logs in AWS PCS
<a name="monitoring_scheduler-audit-logs"></a>

Scheduler audit logs record Remote Procedure Call (RPC) operations processed by your cluster's Slurm controller (`slurmctld`) and database daemon (`slurmdbd`). The `AUDIT_RPCS:` prefix in the log message identifies these logs. They support security auditing and compliance use cases.

For clusters running Slurm 25.11 and later, AWS PCS delivers audit logs separately through the `PCS_SCHEDULER_AUDIT_LOGS` log type. This separation lets you control audit log ingestion and storage costs independently from your operational logs, because audit logs can make up to 90% of scheduler log volume.

**Note**  
For clusters running Slurm versions earlier than 25.11, audit logs remain in `PCS_SCHEDULER_LOGS` and the `PCS_SCHEDULER_AUDIT_LOGS` log type is not available. For more information about scheduler logs, see [Scheduler logs in AWS PCS](monitoring_scheduler-logs.md).

**Contents**
+ [Prerequisites](#monitoring_scheduler-audit-logs_prereqs)
+ [Set up scheduler audit logs](#monitoring_scheduler-audit-logs_setup)
+ [Scheduler audit log stream paths and names](#monitoring_scheduler-audit-logs_paths)
+ [Example scheduler audit log record](#monitoring_scheduler-audit-logs_record)
+ [Audit log behavior by Slurm version](#monitoring_scheduler-audit-logs_behavior)

## Prerequisites
<a name="monitoring_scheduler-audit-logs_prereqs"></a>

Before you can set up scheduler audit logs, you must meet the following requirements:
+ Your cluster must be running **Slurm 25.11 or later**.
+ The IAM principal that manages the AWS PCS cluster must allow the `pcs:AllowVendedLogDeliveryForResource` action.

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

## Set up scheduler audit logs
<a name="monitoring_scheduler-audit-logs_setup"></a>

You can set up scheduler audit logs for your AWS PCS cluster with the AWS Management Console or AWS CLI. Scheduler audit logs are opt-in. AWS PCS does not deliver them until you subscribe.

------
#### [ AWS Management Console ]

**To set up scheduler audit logs with the console**

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs).

1. In the navigation pane, choose **Clusters**.

1. Choose the cluster where you want to add scheduler audit logs.

1. On the cluster details page, choose the **Logs** tab.

1. Under **Scheduler Audit Logs**, choose **Add** to add up to 3 log delivery destinations from among CloudWatch Logs, Amazon S3, and Firehose.

1. Choose **Update log deliveries**.

------
#### [ AWS CLI ]

**To set up scheduler audit logs with the AWS CLI**

1. Create a log delivery destination:

   ```
   aws logs put-delivery-destination --region {{region}} \
     --name {{pcs-audit-logs-destination}} \
     --delivery-destination-configuration \
     destinationResourceArn={{resource-arn}}
   ```

   Replace:
   + {{region}} — The AWS Region where you want to create the destination, such as `us-east-1`
   + {{pcs-audit-logs-destination}} — A name for the destination
   + {{resource-arn}} — The Amazon Resource Name (ARN) of a CloudWatch Logs log group, S3 bucket, or Firehose delivery stream.

   For more information, see [PutDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html) in the *Amazon CloudWatch Logs API Reference*.

1. Set the PCS cluster as a log delivery source:

   ```
   aws logs put-delivery-source --region {{region}} \
     --name {{cluster-audit-logs-source-name}} \
     --resource-arn {{cluster-arn}} \
     --log-type PCS_SCHEDULER_AUDIT_LOGS
   ```

   Replace:
   + {{region}} — The AWS Region of your cluster, such as `us-east-1`
   + {{cluster-audit-logs-source-name}} — A name for the source
   + {{cluster-arn}} — the ARN of your AWS PCS cluster

   For more information, see [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html) in the *Amazon CloudWatch Logs API Reference*.

1. Connect the delivery source to the delivery destination:

   ```
   aws logs create-delivery --region {{region}} \
     --delivery-source-name {{cluster-audit-logs-source}} \
     --delivery-destination-arn {{destination-arn}}
   ```

   Replace:
   + {{region}} — The AWS Region, such as `us-east-1`
   + {{cluster-audit-logs-source}} — The name of your delivery source
   + {{destination-arn}} — The ARN of your delivery destination

   For more information, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) in the *Amazon CloudWatch Logs API Reference*.

------

## Scheduler audit log stream paths and names
<a name="monitoring_scheduler-audit-logs_paths"></a>

The path and name for AWS PCS scheduler audit logs depend on the destination type.
+ **CloudWatch Logs**
  + A CloudWatch Logs stream follows this naming convention.

    ```
    AWSLogs/PCS/${cluster_id}/${log_name}_${scheduler_major_version}_audit.log
    ```

    Where `${log_name}` is `slurmctld` or `slurmdbd`.  
**Example**  

    ```
    AWSLogs/PCS/abcdef0123/slurmctld_25.11_audit.log
    AWSLogs/PCS/abcdef0123/slurmdbd_25.11_audit.log
    ```
+ **S3 bucket**
  + An S3 bucket output path follows this naming convention:

    ```
    AWSLogs/${account-id}/PCS/${region}/${cluster_id}/scheduler_audit/${log_name}/yyyy/MM/dd/HH/
    ```  
**Example**  

    ```
    AWSLogs/111111111111/PCS/us-east-2/abcdef0123/scheduler_audit/slurmctld/2026/03/01/00/
    AWSLogs/111111111111/PCS/us-east-2/abcdef0123/scheduler_audit/slurmdbd/2026/03/01/00/
    ```

## Example scheduler audit log record
<a name="monitoring_scheduler-audit-logs_record"></a>

AWS PCS scheduler audit logs are structured. They use the same schema as scheduler logs, with the log message containing the `AUDIT_RPCS:` prefix. Here is an example from `slurmctld`.

```
{
    "resource_id": "pcs_bu93qsds2j",
    "resource_type": "PCS_CLUSTER",
    "event_timestamp": 1774481175953,
    "log_level": "info",
    "log_name": "slurmctld",
    "scheduler_type": "slurm",
    "scheduler_major_version": "25.11",
    "scheduler_patch_version": "2",
    "node_type": "controller_primary",
    "message": "[2026-01-21T08:19:26.692+00:00] AUDIT_RPCS: [slurmctld-primary:6817(fd:18)] msg_type=REQUEST_PARTITION_INFO uid=0 client=[10.0.76.95:56918]\n"
}
```

Here is an example from `slurmdbd`.

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
    "message": "[2026-01-21T08:19:26.692+00:00] AUDIT_RPCS: msg_type=DBD_GET_CLUSTERS uid=0 client=[28.5.0.18:36658] protocol=11008\n"
}
```

## Audit log behavior by Slurm version
<a name="monitoring_scheduler-audit-logs_behavior"></a>

The following table describes how audit logs are delivered depending on the Slurm version running on your cluster.


| Slurm version | `PCS_SCHEDULER_LOGS` contains | `PCS_SCHEDULER_AUDIT_LOGS` available | 
| --- | --- | --- | 
| Earlier than 25.11 | All logs, including audit logs | No | 
| 25.11 and later | Operational logs only (audit logs removed) | Yes (opt-in) | 