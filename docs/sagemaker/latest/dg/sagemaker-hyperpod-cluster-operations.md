

# Tracking requests with SageMaker HyperPod cluster operations

A cluster operation is a record of a single scaling or on-demand deep health check request on a SageMaker HyperPod cluster. HyperPod creates the operation when it receives your request and tracks it until HyperPod finishes working on it. Each operation has a unique ID, a status, and a record of what the request changed on each instance group. Tracking a request helps you follow it to completion and find the reason if it doesn't finish, without manually correlating cluster events.

With continuous provisioning, requests such as `UpdateCluster` return as soon as HyperPod accepts them. HyperPod then brings each instance group to the requested size in the background, retries failed nodes, and can work on several requests against the same cluster at the same time. With cluster operations, you can follow each of those requests:
+ **Track a request to completion.** See whether HyperPod is still working on your request or has finished.
+ **Tell concurrent requests apart.** The instance and instance group events that HyperPod records while working on a request carry the operation's ID, so you can list only the events for one request.
+ **Find the errors behind a request.** Filter a request's events to find the failure reason when, for example, a scale-up doesn't reach its target.
+ **Review recent changes.** List the requests made on a cluster in the last 14 days and see what each one asked for.

Cluster operations are available for HyperPod clusters orchestrated by Amazon EKS or Slurm with `NodeProvisioningMode` set to `Continuous`. There is no additional cost.

**Topics**
+ [Prerequisites](#sagemaker-hyperpod-cluster-operations-prereqs)
+ [Requests that create an operation](#sagemaker-hyperpod-cluster-operations-requests)
+ [Operation record](#sagemaker-hyperpod-cluster-operations-record)
+ [Operation status](#sagemaker-hyperpod-cluster-operations-status)
+ [Viewing operations in the console](#sagemaker-hyperpod-cluster-operations-console)
+ [Listing operations using the AWS CLI](#sagemaker-hyperpod-cluster-operations-list)
+ [Describing an operation](#sagemaker-hyperpod-cluster-operations-describe)
+ [Viewing an operation's events](#sagemaker-hyperpod-cluster-operations-events)
+ [Find the errors behind an operation](#sagemaker-hyperpod-cluster-operations-errors)
+ [Retention](#sagemaker-hyperpod-cluster-operations-retention)
+ [Related topics](#sagemaker-hyperpod-cluster-operations-related)

## Prerequisites
<a name="sagemaker-hyperpod-cluster-operations-prereqs"></a>
+ Your cluster must have `NodeProvisioningMode` set to `Continuous`.

To use the APIs, your IAM policy must grant the following permissions:
+ `sagemaker:ListClusterOperations`
+ `sagemaker:DescribeClusterOperation`
+ `sagemaker:ListClusterEvents`, to view an operation's events
+ `sagemaker:DescribeClusterEvent`, to view an operation's events

## Requests that create an operation
<a name="sagemaker-hyperpod-cluster-operations-requests"></a>

The following requests create a cluster operation.


| Request | Operation type | 
| --- | --- | 
| CreateCluster | Scaling | 
| UpdateCluster that changes the instance count of one or more instance groups, or adds or removes an instance group | Scaling | 
| BatchAddClusterNodes | Scaling | 
| BatchDeleteClusterNodes | Scaling | 
| DeleteCluster | Scaling | 
| StartClusterHealthCheck (on-demand deep health check) | DeepHealthCheck | 

Requests made by an autoscaler on your behalf, such as Karpenter calling `BatchAddClusterNodes` or `BatchDeleteClusterNodes`, also create operations.

The following activity doesn't create an operation, and its events don't carry an operation ID:
+ Automatic node recovery and node replacement, including `BatchReplaceClusterNodes`
+ Node reboots, including `BatchRebootClusterNodes`
+ Software updates with `UpdateClusterSoftware`
+ Deep health checks that run when nodes start (`OnStartDeepHealthChecks`)

Cluster operations work together with cluster events. For more information, see [SageMaker HyperPod cluster events reference](sagemaker-hyperpod-cluster-events-reference.md). An operation gives you a way to follow a request through the events it produces, and the activity listed here appears in the same events, without an operation ID.

## Operation record
<a name="sagemaker-hyperpod-cluster-operations-record"></a>


| Field | Description | 
| --- | --- | 
| OperationId | Universally unique identifier (UUID) of the operation. | 
| ClusterArn | ARN of the cluster. | 
| Type | Scaling or DeepHealthCheck. | 
| Status | The operation's status. See [Operation status](#sagemaker-hyperpod-cluster-operations-status). | 
| CreationTime | When HyperPod received the request. | 
| ScalingDetails | For Scaling operations. One entry for each instance group the request changed, with that instance group's Status, its Original counts (before the request: CurrentCount, TargetCount, MinCount), and its Desired counts (what the request asked for: TargetCount, MinCount). | 
| DeepHealthCheckDetails | For DeepHealthCheck operations. One entry for each instance group checked, with the InstanceIds checked (empty means every instance in the group) and the DeepHealthChecks run (InstanceStress, InstanceConnectivity, MultiNodeTrainingValidation). | 

An operation records what you asked for and whether HyperPod is still working on it. It doesn't record the outcome of each step, such as which nodes failed or why. That detail is in the operation's events.

## Operation status
<a name="sagemaker-hyperpod-cluster-operations-status"></a>


| Status | Meaning | 
| --- | --- | 
| InProgress | HyperPod is working on the request. | 
| Done | HyperPod has finished working on the request. For a scale-up, the new nodes have run your lifecycle scripts and joined the orchestrator (Slurm or Kubernetes). ListClusterNodes can take a few more minutes to show them as Running. For a scale-down or BatchDeleteClusterNodes, the removed nodes are gone. A DeleteCluster operation stays InProgress while the cluster is being deleted. Once the cluster is gone, you can no longer describe the operation. | 
| Superseded | A newer request took over an instance group this operation was changing, so HyperPod now works toward the newer request's target for that instance group. | 

Each instance group in `ScalingDetails` also has its own status. When an operation changes more than one instance group, a newer request can take over one instance group while the operation continues on the others. Check the status of each instance group to see where the operation stands.

Keep the following in mind:
+ **There is no `Failed` status.** With continuous provisioning, HyperPod keeps retrying until it reaches the target. An operation that can't make progress, for example because a lifecycle script fails on every new node, stays `InProgress` until it expires after 14 days. To find out why an operation isn't finishing, list its `Error` events. For more information, see [Find the errors behind an operation](#sagemaker-hyperpod-cluster-operations-errors).
+ **A failed cluster creation shows `Done`.** If `CreateCluster` fails, its operation reads `Done`. Check the cluster's status with `DescribeCluster`.
+ **A `DeepHealthCheck` operation doesn't record the check result.** When the operation reaches `Done`, the check has finished. To see whether it passed, read the operation's events.
+ **Events can arrive after an operation ends.** Work that was already under way when a newer request took over, such as an instance that was launching, can continue, and its events still carry the superseded operation's ID.
+ **Work after an operation is `Done` isn't part of the operation.** If HyperPod later retries or replaces a node that the operation brought up, those events have no operation ID.

## Viewing operations in the console
<a name="sagemaker-hyperpod-cluster-operations-console"></a>

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker).

1. In the left navigation pane, choose **HyperPod clusters**.

1. Choose your cluster name.

1. Choose the **Events** tab.

The **Events** tab shows the operations on your cluster alongside its events. To see only the events for one operation, filter the **Events** tab by operation ID. In the **Instance groups** table, the **Operation ID** column shows the operation currently working on each instance group. Use this ID to filter the **Events** tab to that operation's events. When an operation that is in progress has `Error` events, the console shows an alert with a link to that operation's error events.

## Listing operations using the AWS CLI
<a name="sagemaker-hyperpod-cluster-operations-list"></a>

Use the `list-cluster-operations` command to list operations newest first:

```bash
aws sagemaker list-cluster-operations \
    --cluster-name my-cluster \
    --sort-by CreationTime \
    --sort-order Descending
```

Narrow results with filters:
+ `--status` (`InProgress`, `Done`, or `Superseded`)
+ `--type` (`Scaling` or `DeepHealthCheck`)
+ `--creation-time-after` and `--creation-time-before` (a time window)

For example, to list scaling operations still in progress:

```bash
aws sagemaker list-cluster-operations \
    --cluster-name my-cluster \
    --status InProgress \
    --type Scaling
```

The following is example output.

```json
{
    "ClusterOperationSummaries": [
        {
            "OperationId": "4c078808-1f2e-4a6b-9c3d-8e5f7a2b1c0d",
            "ClusterArn": "arn:aws:sagemaker:us-west-2:111122223333:cluster/abcd1234efgh",
            "Type": "Scaling",
            "Status": "InProgress",
            "CreationTime": "2026-11-20T13:45:02.118000-08:00"
        }
    ]
}
```

To find the operation for a request you just made, list the operations on the cluster sorted by `CreationTime` and look for the operation created at the time of your request.

## Describing an operation
<a name="sagemaker-hyperpod-cluster-operations-describe"></a>

Use the `describe-cluster-operation` command:

```bash
aws sagemaker describe-cluster-operation \
    --cluster-name my-cluster \
    --operation-id 4c078808-1f2e-4a6b-9c3d-8e5f7a2b1c0d
```

The following is example output for a scale-up of the `gpu-workers` instance group from 4 to 8 nodes.

```json
{
    "OperationId": "4c078808-1f2e-4a6b-9c3d-8e5f7a2b1c0d",
    "ClusterArn": "arn:aws:sagemaker:us-west-2:111122223333:cluster/abcd1234efgh",
    "Type": "Scaling",
    "Status": "InProgress",
    "CreationTime": "2026-11-20T13:45:02.118000-08:00",
    "ScalingDetails": [
        {
            "InstanceGroupName": "gpu-workers",
            "Status": "InProgress",
            "Original": {
                "CurrentCount": 4,
                "TargetCount": 4,
                "MinCount": 0
            },
            "Desired": {
                "TargetCount": 8,
                "MinCount": 0
            }
        }
    ]
}
```

To wait for a request to finish, call `describe-cluster-operation` periodically until `Status` is `Done` or `Superseded`. Because there is no `Failed` status, set a timeout and check the operation's `Error` events if the operation stays `InProgress` longer than expected. For `DeleteCluster`, wait until `DescribeCluster` returns `ResourceNotFound`. Once the cluster is gone, `describe-cluster-operation` returns `ResourceNotFound` too.

## Viewing an operation's events
<a name="sagemaker-hyperpod-cluster-operations-events"></a>

Use the `--operation-id` filter on `list-cluster-events`:

```bash
aws sagemaker list-cluster-events \
    --cluster-name my-cluster \
    --operation-id 4c078808-1f2e-4a6b-9c3d-8e5f7a2b1c0d
```

You can combine `--operation-id` with the other `list-cluster-events` filters. For example, add `--node-id` to trace one node's events within an operation. To go the other way, from an event to the request that caused it, read the event's `OperationId` field. Events that don't belong to any operation, such as cluster-level events and node replacement events, have no `OperationId`.

## Find the errors behind an operation
<a name="sagemaker-hyperpod-cluster-operations-errors"></a>

If an operation stays `InProgress` or an instance group doesn't reach its target:

1. List the operation's events with `--operation-id`.

1. Look for events with `EventLevel` set to `Error`.

1. Call `describe-cluster-event` on an error event to read its `FailureMessage`, for example an insufficient-capacity error or a lifecycle script failure with a link to its CloudWatch log group.

In the console, choose the link in the error alert, or filter the **Events** tab by the operation's ID and look for `Error` events.

## Retention
<a name="sagemaker-hyperpod-cluster-operations-retention"></a>

Operations are available for 14 days, the same as cluster events. Operations aren't an audit log. To keep a permanent record of the API calls made on your cluster, use CloudTrail. In rare cases, a request might not have an operation, for example if HyperPod couldn't record it. The request itself isn't affected.

## Related topics
<a name="sagemaker-hyperpod-cluster-operations-related"></a>
+ [SageMaker HyperPod EKS cluster events](sagemaker-hyperpod-cluster-events-eks-page.md)
+ [SageMaker HyperPod Slurm cluster events](sagemaker-hyperpod-cluster-events-slurm-page.md)
+ [SageMaker HyperPod cluster events reference](sagemaker-hyperpod-cluster-events-reference.md)
+ [ListClusterOperations](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterOperations.html) and [DescribeClusterOperation](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterOperation.html) in the Amazon SageMaker AI API Reference