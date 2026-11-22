

# Monitoring cluster extension health

You don't need to turn on health reporting. It needs only the CloudWatch Logs permissions in the `AmazonSageMakerClusterInstanceRolePolicy` AWS managed policy. Health can take a few minutes to update after a change or a fix.

A node reports each extension as one of the following:
+ **`HEALTHY`** – All of the extension's components on the node are working.
+ **`UNHEALTHY`** – At least one component isn't working.
+ **`UNKNOWN`** – The node couldn't determine the extension's health, such as right after installation. `UNKNOWN` never makes an extension `Degraded`.

When any node reports an extension as `UNHEALTHY`, the extension's status is `Degraded`, and the node isn't counted in `ActiveCount`. Fix the cause on the node. The status returns to `Active` after every node is healthy again, and you don't need to reinstall the extension. For what each extension checks, see its page.

`Health` in the `describe-cluster-extension` response is a summary for the whole cluster. CloudWatch metrics and logs give per-node detail and history, and you can alarm on them.

## Health metrics
<a name="sagemaker-hyperpod-slurm-extensions-health-health-metrics"></a>

HyperPod publishes the following metrics in the `/aws/sagemaker/Clusters` namespace.


**Extension health metrics**  

| Metric | Description | Dimensions | 
| --- | --- | --- | 
| extension\_healthy\_count | The number of nodes that reported the extension as healthy | ClusterId; ClusterId, ExtensionName | 
| extension\_unhealthy\_count | The number of nodes that reported the extension as unhealthy | ClusterId; ClusterId, ExtensionName | 
| extension\_unknown\_count | The number of nodes that couldn't determine the extension's health | ClusterId; ClusterId, ExtensionName | 

To get the node counts for one extension, use the `Sum` statistic, a 5-minute period, and both the `ClusterId` and `ExtensionName` dimensions. A shorter period shows gaps.

**To create an alarm for an unhealthy extension by using the AWS Command Line Interface (AWS CLI)**

In the following command, replace {{abcd1234efgh}} with your cluster ID, and `sagemaker-observability` with the extension name. Create one alarm for each extension.

Run the following `put-metric-alarm` command to create an alarm on `extension_unhealthy_count`:

```
aws cloudwatch put-metric-alarm \
    --alarm-name hyperpod-{{abcd1234efgh}}-observability-unhealthy \
    --namespace /aws/sagemaker/Clusters \
    --metric-name extension_unhealthy_count \
    --dimensions Name=ClusterId,Value={{abcd1234efgh}} Name=ExtensionName,Value=sagemaker-observability \
    --statistic Sum --period 300 --evaluation-periods 2 \
    --threshold 1 --comparison-operator GreaterThanOrEqualToThreshold \
    --treat-missing-data notBreaching
```

## Health logs
<a name="sagemaker-hyperpod-slurm-extensions-health-health-logs"></a>

Each node writes a JSON health record for each extension to your cluster's log group, the same log group that holds the lifecycle script logs.
+ Log group: `/aws/sagemaker/Clusters/{{cluster-name}}/{{cluster-id}}`
+ Log stream: `SageMakerExtensionHealth/{{instance-group-name}}/{{instance-id}}`

The following example is a health record from the observability extension on a node where the node exporter stopped:

```
{
    "InstanceId": "i-1234567890abcdef0",
    "ExtensionName": "sagemaker-observability",
    "ExtensionVersion": "1.0.0",
    "Status": "UNHEALTHY",
    "Code": "ExtensionUnhealthy",
    "Message": "node-exporter (prometheus-node-exporter) is not running, so node metrics are missing. Check /var/log/aws/clusters/sagemaker-observability-node-exporter.log on the node.",
    "EvaluatedAt": "2026-11-12T09:15:03Z",
    "Components": [
        { "Name": "node-exporter", "Status": "UNHEALTHY", "Code": "SERVICE_NOT_RUNNING", "Message": "prometheus-node-exporter is not active" },
        { "Name": "slurm-job-exporter", "Status": "HEALTHY", "Code": "SERVICE_RUNNING", "Message": "hyperpod-slurm-job-exporter is active" },
        { "Name": "otel-collector", "Status": "HEALTHY", "Code": "SERVICE_RUNNING", "Message": "hyperpod-otel-collector is active" },
        { "Name": "otel-exporter-health", "Status": "HEALTHY", "Code": "HEALTH_ENDPOINT_OK", "Message": "OK" }
    ],
    "Time": "2026-11-12T09:15:30Z"
}
```

`Code` and `Message` give the reason for the status, and `Components` gives the status of each component on the node. Each extension's page lists its codes. When a node can't get a health result from the extension, the record's status is `UNKNOWN` with one of the following codes.


**Codes when a node can't get a health result**  

| Code | Meaning | 
| --- | --- | 
| ReportAbsent | No health result yet. This is normal for a few minutes after installation. | 
| ReportStale | The extension hasn't refreshed its health result recently. | 
| ReportMalformed, SchemaUnsupported, AccessDenied | The health result couldn't be read. If this continues, contact AWS Support. | 

### Querying health records
<a name="sagemaker-hyperpod-slurm-extensions-health-querying-health-records"></a>

You can use the following Amazon CloudWatch Logs Insights query on your cluster's log group. It lists the nodes that weren't healthy in the selected time range, with their instance group and the failing check:

```
fields @timestamp, @logStream
| filter @logStream like /^SageMakerExtensionHealth\// and Status != "HEALTHY"
| parse @logStream "SageMakerExtensionHealth/*/*" as instanceGroup, instance
| stats latest(Status) as status, latest(Code) as code, latest(Message) as message, count(*) as reports by instanceGroup, InstanceId, ExtensionName
| sort reports desc
```

To see the components of the failing records, run the following query:

```
fields Time, InstanceId, @message
| filter @logStream like /^SageMakerExtensionHealth\// and Status = "UNHEALTHY"
| sort Time desc
| limit 50
```

**Note**  
The log group also contains `SageMakerExtensionHealthMetrics/…` streams, which hold the records that the health metrics are built from. To match only health records, use the regular expression `/^SageMakerExtensionHealth\//` exactly as shown.

### Extension run logs
<a name="sagemaker-hyperpod-slurm-extensions-health-extension-run-logs"></a>

Some extensions also write a log each time they apply their configuration on a node. The user management extension writes to `/var/log/aws/clusters/sagemaker-user-management.log` on the node, which is shipped to the log stream `SageMakerUserManagement/instance-group-name/instance-id`. The observability extension's components each write to their own `SageMakerObservability…` log stream.

## Troubleshooting extension health
<a name="sagemaker-hyperpod-slurm-extensions-health-troubleshooting"></a>

### The extension status is Degraded
<a name="sagemaker-hyperpod-slurm-extensions-health-the-extension-status-is-degraded"></a>

At least one node failed the operation, or reports the extension as unhealthy.

1. Run `describe-cluster-extension`. `Health` lists the problems by cause. For what each code means, see [Health issues](sagemaker-hyperpod-slurm-extensions.md#sagemaker-hyperpod-slurm-extensions-health-issues).

1. To find the nodes and the failing component, run the queries in [Querying health records](#sagemaker-hyperpod-slurm-extensions-health-querying-health-records).

1. Fix the cause, and then retry as described in [Retrying failed nodes](sagemaker-hyperpod-slurm-extensions.md#sagemaker-hyperpod-slurm-extensions-retrying-failed-nodes).

For extension-specific checks, see the troubleshooting section of the [Setting up observability with the SageMaker HyperPod observability extension](sagemaker-hyperpod-cluster-observability-slurm-extension.md) or the [Troubleshooting](sagemaker-hyperpod-slurm-user-management-manage.md#sagemaker-hyperpod-slurm-user-management-manage-troubleshooting).

### The extension status is CreateFailed or UpdateFailed
<a name="sagemaker-hyperpod-slurm-extensions-health-the-extension-status-is-createfailed-or-updatefailed"></a>

The operation failed on every node, usually because the nodes can't apply the configuration.

1. Run `describe-cluster-extension`. `Health` shows the cause, with a code and a message that names the setting to fix.

1. Retry the operation in one of the following ways:
   + If you correct the configuration, send it with `update-cluster-extension`.
   + If you fixed the cause on the nodes or in IAM instead, run `update-cluster-extension` without changing the version or configuration.

   HyperPod retries the operation on the nodes where it failed.

### ActiveCount stays lower than TotalCount
<a name="sagemaker-hyperpod-slurm-extensions-health-activecount-stays-lower-than-totalcount"></a>

Some nodes haven't finished the operation, failed it, or report the extension as unhealthy. New nodes are counted in `TotalCount` as soon as they start, and finish within a few minutes.

1. Run `describe-cluster-extension`, and check `Health` to see why nodes aren't counted.

1. If nodes failed the operation or report the extension as unhealthy, follow the steps in [The extension status is Degraded](#sagemaker-hyperpod-slurm-extensions-health-the-extension-status-is-degraded).

1. If nodes are still being installed or updated, wait a few minutes, and then check again.

### No health metrics or health logs
<a name="sagemaker-hyperpod-slurm-extensions-health-no-health-metrics-or-health-logs"></a>

Only nodes that run a supported AMI publish extension health. For more information, see [Prerequisites and IAM permissions for cluster extensions](sagemaker-hyperpod-slurm-extensions-prerequisites.md). Also make sure that the execution role can write to the `/aws/sagemaker/Clusters/*` log groups. The `AmazonSageMakerClusterInstanceRolePolicy` managed policy includes this permission.