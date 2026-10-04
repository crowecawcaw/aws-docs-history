

# Scaling logs in AWS PCS
<a name="monitoring_scaling-logs"></a>

Scaling logs give you a record of how AWS Parallel Computing Service scales the compute node groups in your cluster. Each log entry records one state transition for one compute node: for example, an instance launch, a node registration, a scale-down, or a launch failure with its reason. You can use scaling logs to answer questions such as why a node group did not reach its target size, which launches failed for capacity reasons, and when a specific node started or stopped.

You can send scaling logs to Amazon CloudWatch, Amazon Simple Storage Service (Amazon S3), and Amazon Data Firehose. For each transition, AWS PCS records the following data:
+ Cluster and compute node group identifiers
+ The node name
+ The new status
+ A reason code and a human-readable description
+ The EC2 instance ID, when an instance is associated with the transition
+ Launch context, such as instance type and subnet, when relevant

AWS PCS delivers scaling logs through the `PCS_SCALING_LOGS` log type. Scaling log delivery is opt-in. AWS PCS does not deliver scaling logs for a cluster until you configure a delivery for it.

**Contents**
+ [Prerequisites](#monitoring_scaling-logs_prereqs)
+ [Set up scaling logs](#monitoring_scaling-logs_setup)
+ [Finding scaling logs](#monitoring_scaling-logs_access)
  + [CloudWatch Logs](#monitoring_scaling-logs_access_cloudwatch)
  + [Amazon S3](#monitoring_scaling-logs_access_s3)
+ [Scaling log fields](#monitoring_scaling-logs_fields)
+ [Status codes and reason codes](#monitoring_scaling_logs-status-codes-and-reason-codes)
+ [Example scaling logs](#monitoring_scaling-logs_example)

## Prerequisites
<a name="monitoring_scaling-logs_prereqs"></a>

The IAM principal that manages the AWS PCS cluster must allow the `pcs:AllowVendedLogDeliveryForResource` action.

The following example IAM policy grants the required permissions.

```
{
    "Version": "2012-10-17",
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

## Set up scaling logs
<a name="monitoring_scaling-logs_setup"></a>

You can set up scaling logs for your AWS PCS cluster with the AWS Management Console or AWS CLI.

------
#### [ AWS Management Console ]

**To set up scaling logs with the console**

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs).

1. In the navigation pane, choose **Clusters**.

1. Choose the cluster where you want to add scaling logs.

1. On the cluster details page, choose the **Logs** tab.

1. Under **Scaling Logs**, choose **Add** to add up to 3 log delivery destinations from among CloudWatch Logs, Amazon S3, and Firehose.

1. Choose **Update log deliveries**.

------
#### [ AWS CLI ]

**To set up scaling logs with the AWS CLI**

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
     --log-type PCS_SCALING_LOGS
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

## Finding scaling logs
<a name="monitoring_scaling-logs_access"></a>

You can configure log destinations in CloudWatch Logs and Amazon S3. AWS PCS uses the following structured path names and file names.

### CloudWatch Logs
<a name="monitoring_scaling-logs_access_cloudwatch"></a>

AWS PCS uses the following name format for the CloudWatch Logs stream:

```
AWSLogs/PCS/{{cluster-id}}/node_lifecycle.log
```

For example: `AWSLogs/PCS/pcs_abc123de45/node_lifecycle.log`

### Amazon S3
<a name="monitoring_scaling-logs_access_s3"></a>

AWS PCS uses the following name format for the S3 path:

```
AWSLogs/{{account-id}}/PCS/{{region}}/{{cluster-id}}/node_lifecycle/{{year}}/{{month}}/{{day}}/{{hour}}/
```

For example: `AWSLogs/111122223333/PCS/us-east-1/pcs_abc123de45/node_lifecycle/2026/09/03/11/`

AWS PCS uses the following name format for the log files:

```
PCS_{{cluster-id}}_node_lifecycle_{{year}}-{{month}}-{{day}}-{{hour}}_{{random-id}}.log.gz
```

For example: `PCS_pcs_abc123de45_node_lifecycle_2026-09-03-11_04be080b.log.gz`

## Scaling log fields
<a name="monitoring_scaling-logs_fields"></a>

AWS PCS writes scaling log data as JSON objects. Each log entry contains top-level metadata fields and a `details` object. The top-level fields identify the cluster, event time, and compute node group and scheduler node ids. The `details` object holds the transition details.

The following table describes the top-level fields in each log entry.


**Top-level fields**  

| Name | Example value | Required | Notes | 
| --- | --- | --- | --- | 
| resource\_id | "pcs\_22l8nzr3t9" | Yes | The AWS PCS cluster ID | 
| resource\_type | "PCS\_CLUSTER" | Yes | Always "PCS\_CLUSTER" | 
| event\_timestamp | 1789179816460 | Yes | Unix epoch milliseconds when the event occurred | 
| compute\_node\_group\_id | "pcs\_56zr33g8" | Yes | The compute node group the node belongs to | 
| scheduler\_node\_id | "compute-1" | Yes | The scheduler node id | 
| status\_code | "LAUNCH\_FAILED" | Yes | The new status of the node. See [Status codes and reason codes](#monitoring_scaling_logs-status-codes-and-reason-codes) | 
| reason\_code | "INSUFFICIENT\_CAPACITY" | Yes | Why the transition happened | 
| description | "The launch failed because EC2 did not have enough capacity" | Yes | A human-readable summary derived from the status and reason codes | 
| details | {...} | No | Additional context for the transition. Keys depend on the transition type | 

The following table describes the keys that can appear inside the `details` object.


**Fields inside the `details` object**  

| Name | Example value | Required | Notes | 
| --- | --- | --- | --- | 
| instance\_id | "i-0abcdef01234567a" | No | The EC2 instance associated with the node. Absent when no instance is associated, such as after a launch failure | 
| ec2\_error\_code | "InsufficientInstanceCapacity" | No | The EC2 error code for a failed launch. The same code appears in the CloudTrail record of the CreateFleet call in your account | 
| instance\_type | "t4g.micro" | No | The instance type launched | 
| subnet\_id | "subnet-0abc123" | No | The subnet targeted by the launch | 

## Status codes and reason codes
<a name="monitoring_scaling_logs-status-codes-and-reason-codes"></a>

The `status_code` field tells you the state the node entered. The `reason_code` field tells you why. For example, a `LAUNCH_FAILED` status with an `INSUFFICIENT_CAPACITY` reason means Amazon EC2 could not provide capacity for the requested instance type in the targeted subnet. A `LIMIT_EXCEEDED` means an Amazon EC2 quota blocked the launch.


**Status codes and reason codes**  

| Status code | Reason code | Description | 
| --- | --- | --- | 
| LAUNCHED | SCHEDULER\_REQUESTED | Instance launched to satisfy a scheduler scale-up request | 
| LAUNCHED | MAINTAIN\_MIN\_CAPACITY | Instance launched to maintain the node group's minimum capacity | 
| REGISTERED | REGISTER\_SUCCESS | Node registered successfully via the PCS agent | 
| ACTIVE | BOOTSTRAP\_SUCCESS | Node bootstrap completed; slurmd is running and accepting jobs | 
| PENDING\_REPLACEMENT | NODE\_GROUP\_UPDATE | Node is draining ahead of being powered down for a node group update | 
| PENDING\_REPLACEMENT | EC2\_HEALTH\_CHECK\_FAILED | Node is draining because a health check on the node or its instance failed | 
| PENDING\_REPLACEMENT | EC2\_SCHEDULED\_EVENT | Node is draining because its instance has a scheduled EC2 maintenance event | 
| LAUNCH\_FAILED | INSUFFICIENT\_CAPACITY | Node did not get an instance because there was not enough capacity available | 
| LAUNCH\_FAILED | LIMIT\_EXCEEDED | Instance launch failed because an account quota was exceeded | 
| LAUNCH\_FAILED | LAUNCH\_ERROR | Node failed to launch its instance | 
| TERMINATED | SCHEDULER\_REQUESTED | Instance terminated after the scheduler released the node (idle timeout or power-down) | 
| TERMINATED | UNHEALTHY\_NODE | Instance terminated because the scheduler reported the node as unhealthy | 
| TERMINATED | BOOTSTRAP\_FAILED | Instance terminated because the node failed to bootstrap | 
| TERMINATED | EXTERNALLY\_TERMINATED | Instance was terminated outside of PCS; the node was released so it can be replaced | 
| TERMINATED | REPLACEMENT\_REQUESTED | Instance was terminated because the node was drained for replacement | 
| TERMINATED | NODE\_GROUP\_DELETION | Instance terminated as part of compute node group deletion | 
| TERMINATE\_FAILED | EC2\_OPERATION\_NOT\_PERMITTED | Instance termination failed. Ensure termination protection is not enabled on the instance | 
| TERMINATE\_FAILED | EC2\_ERROR | Instance termination failed | 

## Example scaling logs
<a name="monitoring_scaling-logs_example"></a>

The following example shows a successful instance launch:

```
{
    "resource_id": "pcs_abc123de45",
    "resource_type": "PCS_CLUSTER",
    "event_timestamp": 1789179816460,
    "compute_node_group_id": "pcs_abcdef01",
    "scheduler_node_id": "compute-1",
    "status_code": "LAUNCHED",
    "reason_code": "SCHEDULER_REQUESTED",
    "description": "Instance launched to satisfy a scheduler scale-up request.",
    "details": {
        "instance_id": "i-0abc12345def67890",
        "instance_type": "c6i.xlarge",
        "subnet_id": "subnet-0123456789abcdef0"
    }
}
```

The following example shows a launch failure caused by insufficient EC2 capacity. No `instance_id` is present because no instance was launched.

```
{
    "resource_id": "pcs_abc123de45",
    "resource_type": "PCS_CLUSTER",
    "event_timestamp": 1789179816460,
    "compute_node_group_id": "pcs_abcdef01",
    "scheduler_node_id": "compute-2",
    "status_code": "LAUNCH_FAILED",
    "reason_code": "INSUFFICIENT_CAPACITY",
    "description": "Node did not get an instance because there was not enough capacity available.",
    "details": {
        "ec2_error_code": "InsufficientInstanceCapacity"
    }
}
```