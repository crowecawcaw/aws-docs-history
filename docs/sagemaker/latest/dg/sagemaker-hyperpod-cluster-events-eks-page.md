

# SageMaker HyperPod EKS cluster events
<a name="sagemaker-hyperpod-cluster-events-eks-page"></a>

Amazon SageMaker HyperPod emits structured cluster events that provide visibility into operational changes at the cluster, instance group, and instance level. You can use these events to monitor provisioning activity, track scaling operations, detect failures, and build automated alerting pipelines.

Cluster events are available for HyperPod EKS clusters with `NodeProvisioningMode` set to `Continuous`. Events are accessible through the `ListClusterEvents` and `DescribeClusterEvent` APIs, the SageMaker AI console, and Amazon EventBridge.

For the complete event schema, severity levels, full event catalog, and EventBridge integration details, see [SageMaker HyperPod cluster events reference](sagemaker-hyperpod-cluster-events-reference.md).

## Prerequisites
<a name="sagemaker-hyperpod-cluster-events-eks-prereqs"></a>
+ Your HyperPod EKS cluster must have `NodeProvisioningMode` set to `Continuous`. Clusters using the legacy provisioning mode do not emit structured events.
+ To use the API, you need `sagemaker:ListClusterEvents` and `sagemaker:DescribeClusterEvent` permissions in your IAM policy.

## Event types
<a name="sagemaker-hyperpod-cluster-events-eks-types"></a>

HyperPod emits two categories of events for EKS clusters on continuous provisioning: common events that apply to all orchestrators, and EKS-specific events.

**Common events** cover core infrastructure operations such as instance provisioning and termination, instance group scaling, capacity reservation handling, lifecycle script execution, ENI management, FSx filesystem lifecycle, and patching workflows. For the complete list, see [Common events (EKS and Slurm)](sagemaker-hyperpod-cluster-events-reference.md#sagemaker-hyperpod-cluster-events-common) in the HyperPod cluster events reference.

**EKS-specific events** cover orchestrator-specific operations such as EKS access entry management, Kubernetes configuration updates (labels and taints), Karpenter autoscaling lifecycle, pod eviction and cordon/uncordon during patching, and bake time alarm monitoring with auto-rollback. These events provide visibility into EKS-specific lifecycle stages that were previously only observable through CloudWatch logs. For the complete list, see [EKS-specific events](sagemaker-hyperpod-cluster-events-reference.md#sagemaker-hyperpod-cluster-events-eks) in the HyperPod cluster events reference.

## Viewing events in the console
<a name="sagemaker-hyperpod-cluster-events-eks-console"></a>

1. Open the [SageMaker AI console](https://console.aws.amazon.com/sagemaker).

1. In the left navigation pane, choose **HyperPod clusters**.

1. Choose your cluster name.

1. Choose the **Events** tab.

The **Events** tab displays a paginated list of events with columns for event level, event ID, resource name, resource type, description, and event time. You can filter events by attribute using the search box, sort by event time, and choose an event ID to see full event details including the event metadata and the complete event record.

## Listing events using the AWS CLI
<a name="sagemaker-hyperpod-cluster-events-eks-cli"></a>

Use the `list-cluster-events` command to retrieve events for your cluster:

```
aws sagemaker list-cluster-events \
    --cluster-name my-eks-cluster \
    --sort-by EventTime \
    --sort-order Descending \
    --max-results 20
```

You can narrow results using the following filters:
+ `--resource-type` — filter by `Cluster`, `InstanceGroup`, or `Instance`.
+ `--instance-group-name` — filter to events for a specific instance group.
+ `--node-id` — filter to events for a specific EC2 instance.
+ `--event-time-after` and `--event-time-before` — filter to a specific time window.

For example, to see only instance-group-level events for a specific instance group:

```
aws sagemaker list-cluster-events \
    --cluster-name my-eks-cluster \
    --resource-type InstanceGroup \
    --instance-group-name gpu-workers
```

## Describing a specific event
<a name="sagemaker-hyperpod-cluster-events-eks-describe"></a>

Use the `describe-cluster-event` command with an event ID from the list output to retrieve full event details, including the `EventLevel`, `Description`, and `EventMetadata`:

```
aws sagemaker describe-cluster-event \
    --cluster-name my-eks-cluster \
    --event-id 83ea0bb5-be77-45e8-a458-0a87f778a205
```

For the structure of the returned event record and a description of each field, see [Cluster event record](sagemaker-hyperpod-cluster-events-reference.md#sagemaker-hyperpod-cluster-events-record) in the HyperPod cluster events reference.

## Automating responses with Amazon EventBridge
<a name="sagemaker-hyperpod-cluster-events-eks-eventbridge"></a>

HyperPod cluster events are automatically sent to Amazon EventBridge under the detail type `SageMaker HyperPod Cluster Event`, enabling you to route events to targets such as Lambda, Amazon SNS, Step Functions, or Amazon SQS. You can filter on the `EventLevel` field to trigger alerts only for `Error` events, or filter by cluster ARN to scope rules to a specific cluster.

For EventBridge event patterns, payload examples, and the related `SageMaker HyperPod Cluster State Change` and `SageMaker HyperPod Cluster Node Health Event` detail types, see [EventBridge integration](sagemaker-hyperpod-cluster-events-reference.md#sagemaker-hyperpod-cluster-events-eventbridge) in the HyperPod cluster events reference.

## Related topics
<a name="sagemaker-hyperpod-cluster-events-eks-related"></a>
+ [SageMaker HyperPod cluster events reference](sagemaker-hyperpod-cluster-events-reference.md)
+ [Events that Amazon SageMaker AI sends to Amazon EventBridge](https://docs.aws.amazon.com/sagemaker/latest/dg/automating-sagemaker-with-eventbridge.html)