

# Setting up observability with the SageMaker HyperPod observability extension

The SageMaker HyperPod observability extension, `sagemaker-observability`, installs metrics exporters and collectors on the instances of your Slurm cluster. The extension gives you visibility into cluster health, job performance, and GPU utilization.

The extension supports the following features:
+ Metrics in Amazon CloudWatch. Amazon CloudWatch is the default metric store. With Amazon CloudWatch, you don't create an Amazon Managed Service for Prometheus workspace or give the execution roles access to it.
+ Metrics in Amazon Managed Service for Prometheus, when you specify the remote write URL of an Amazon Managed Service for Prometheus workspace.

The extension sends metrics to one metric store. It can't send metrics to both Amazon CloudWatch and Amazon Managed Service for Prometheus at the same time.

## Quick start
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-quick-start"></a>

1. Make sure that your cluster meets the [Prerequisites for the observability extension](#sagemaker-hyperpod-cluster-observability-slurm-extension-prerequisites).

1. Install the extension with the default settings, which send metrics to Amazon CloudWatch:

   ```
   aws sagemaker create-cluster-extension \
      --cluster-arn {{arn:aws:sagemaker:us-west-2:111122223333:cluster/abcde1234567}} \
      --extension-name sagemaker-observability \
      --configuration-values '{}'
   ```

1. Wait until the status is `Active` and `ActiveCount` equals `TotalCount`:

   ```
   aws sagemaker describe-cluster-extension \
      --cluster-arn {{arn:aws:sagemaker:us-west-2:111122223333:cluster/abcde1234567}} \
      --extension-arn {{extension-arn}}
   ```

1. [Viewing the metrics of the observability extension](#sagemaker-hyperpod-cluster-observability-slurm-extension-view-metrics).

## Prerequisites for the observability extension
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-prerequisites"></a>
+ Your cluster uses continuous provisioning. SageMaker HyperPod supports cluster extensions only on clusters that have `NodeProvisioningMode` set to `Continuous`. For more information, see [Continuous provisioning for enhanced cluster operations with Slurm](sagemaker-hyperpod-scaling-slurm.md).
+ The execution role of each instance group has the permissions in [Permissions for the observability extension](#sagemaker-hyperpod-cluster-observability-slurm-extension-iam).
+ To view Amazon CloudWatch metrics in Amazon Managed Grafana, use a workspace that runs Grafana version 12 or later.
+ No other process uses the ports of the extension's exporters. The extension uses port 9100 for the node exporter on every node, port 9400 for the NVIDIA Data Center GPU Manager (DCGM) exporter on GPU compute nodes, and port 9109 for the Elastic Fabric Adapter (EFA) exporter on compute nodes with EFA. If another process uses one of these ports, the installation fails. The error message names the port and the metric type that you can turn off.

  If you set up observability with the lifecycle scripts (`enable_observability=True`), the exporter containers of the lifecycle scripts use these ports. For more information, see [Migrating from lifecycle scripts](#sagemaker-hyperpod-cluster-observability-slurm-extension-migrating-from-lifecycle-scripts). Before you install the extension, do one of the following:
  + Replace the lifecycle-script exporters with the extension. In the `config.py` file of your lifecycle scripts, set `enable_observability = False`, and upload the file to the Amazon S3 location of your lifecycle scripts. New and replaced nodes then don't start the containers. Then remove the containers on each node. The current lifecycle scripts name them `node-exporter`, `dcgm-exporter`, `efa-exporter`, and `otel-collector`.

    ```sh
    $ sudo docker rm -f node-exporter dcgm-exporter efa-exporter otel-collector
    ```

    A node that doesn't have one of these containers reports an error for that name. If your lifecycle scripts are older, run `sudo docker ps` to find the container names. After you remove the containers, the metrics of the lifecycle scripts stop, and the extension collects the metrics.
  + Set `metricsProvider.nodeMetrics.level`, `metricsProvider.acceleratedComputeMetrics.level`, and `metricsProvider.networkMetrics.level` to `DISABLED`. The extension then doesn't use ports 9100, 9400, and 9109, and it doesn't collect these metric types. When `ncclMetrics` is `ENABLED`, `nodeMetrics` can't be `DISABLED`.

## Components on each node type
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-components-on-each-node-type"></a>

The following table shows the components that the extension runs with the default settings, and the setting that controls each one. On nodes without GPUs or EFA devices, the extension skips those exporters without an error, so you can use the same configuration on clusters with mixed instance types.


| Component | Port | Setting | Controller | Login | Compute | 
| --- | --- | --- | --- | --- | --- | 
| Node exporter | 9100 | nodeMetrics | Yes | Yes | Yes | 
| NVIDIA Data Center GPU Manager (DCGM) exporter | 9400 | acceleratedComputeMetrics | — | — | Nodes with NVIDIA GPUs | 
| EFA exporter | 9109 | networkMetrics | — | — | Nodes with EFA | 
| Slurm job exporter | 9110 | jobMetrics | — | — | Yes | 
| Slurm cluster metrics, from the Slurm controller | — | clusterMetrics | Yes | — | — | 
| NCCL profiler plugin | 4327 | ncclMetrics | — | — | When enabled | 
| OpenTelemetry Collector | 13133, 8889 | Always | Yes | Yes | Yes | 

The exporters listen only on the node's loopback interface, except the OpenTelemetry Collector's health port, 13133, which listens on every address. To keep it private, block port 13133 from other hosts in your security groups.

## Installing the observability extension with the console
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-console"></a>

**To install the observability extension**

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. Go to your cluster's details page.

1. Choose the **Extensions** tab.

1. On the **Amazon SageMaker HyperPod observability** card, choose **Actions**, and then choose **Install**.

1. On the **Install HyperPod observability** page, under **Observability metrics**, configure which metrics the extension collects from your cluster instances.

1. Under **Metric store**, choose **Amazon CloudWatch** or **Amazon Managed Service for Prometheus**. **Amazon CloudWatch** is the default, unless the setup stack of the cluster sends metrics to Amazon Managed Service for Prometheus. If you choose Amazon Managed Service for Prometheus, under **Prometheus workspace**, choose **Create a new workspace** or **Choose an existing workspace**.

1. Under **Grafana workspace**, choose **Create a new workspace**, **Choose an existing workspace**, or **None**. If the setup stack of the cluster set up a Grafana workspace, that workspace is the default. If the setup stack set up no Grafana workspace, **None** is the default. Otherwise, **Create a new workspace** is the default in the AWS Regions where Amazon Managed Grafana is available. In other AWS Regions, the page doesn't show **Create a new workspace**, and **None** is the default. Choose **None** if you plan to connect the metrics to your own observability stack.

1. Submit the page.

When you choose Amazon Managed Service for Prometheus, the console tries to give the execution roles of the cluster the `aps:RemoteWrite` permission on the workspace. If the console can't add the permission, it shows a warning. Add the permission to each execution role yourself.

To change the configuration later, on the **Amazon SageMaker HyperPod observability** card, choose **Actions**, and then choose **Edit**. The **Edit HyperPod observability** page has the same settings.

When you create a cluster with **Quick setup**, the console installs the observability extension with **Amazon CloudWatch** as the metric store.

## Installing the observability extension with the API
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-api"></a>

To install the extension, use the `CreateClusterExtension` API operation. To change the configuration of an installed extension, use the `UpdateClusterExtension` API operation. Pass the configuration of the extension as a JSON string in `ConfigurationValues`.

The following example is a `CreateClusterExtension` request that installs the extension with Amazon CloudWatch as the metric store.

```json
{
    "ClusterArn": "{{arn:aws:sagemaker:us-west-2:111122223333:cluster/abcde1234567}}",
    "ExtensionName": "sagemaker-observability",
    "ExtensionVersion": "1.0.0",
    "ConfigurationValues": "{}"
}
```

The following AWS CLI command sends the same request.

```
aws sagemaker create-cluster-extension \
    --cluster-arn {{arn:aws:sagemaker:us-west-2:111122223333:cluster/abcde1234567}} \
    --extension-name sagemaker-observability \
    --extension-version 1.0.0 \
    --configuration-values '{}'
```

To change the configuration, use the `aws sagemaker update-cluster-extension` command.

`UpdateClusterExtension` applies `ConfigurationValues` to the stored configuration as a JSON merge patch (RFC 7396). Keys that you don't specify keep their stored values. A key with the value `null` is deleted. SageMaker HyperPod then validates the merged configuration against the schema of the extension. For example, to send metrics to Amazon CloudWatch instead of Amazon Managed Service for Prometheus, delete the `prometheus` key with the following command. Replace {{extension-arn}} with the ARN of the installed extension. To get the ARN, use the `ListClusterExtensions` API operation.

```
aws sagemaker update-cluster-extension \
    --cluster-arn {{arn:aws:sagemaker:us-west-2:111122223333:cluster/abcde1234567}} \
    --extension-arn {{extension-arn}} \
    --configuration-values '{"prometheus":null}'
```

To change back to Amazon Managed Service for Prometheus, specify `prometheus.remoteWriteUrl` again. The execution role of each instance group needs `aps:RemoteWrite` on the workspace.

After you change the metric store, the extension sends new metrics only to the new metric store. It doesn't copy the metrics that are already in the old metric store. Metrics in an Amazon Managed Service for Prometheus workspace stay there for the retention period of the workspace.

If the extension has a Grafana workspace, the console replaces the SageMaker HyperPod Slurm dashboards in that workspace with the dashboards for the new metric store the next time that you view the cluster in the console. If other SageMaker HyperPod clusters use the workspace, the console asks you before it replaces the dashboards.

To check the status of the extension, use the `DescribeClusterExtension` API operation. When the installation is complete, the status is `Active`.

The extension accepts the following configuration values.


**Configuration values for the observability extension**  

| Key | Description | 
| --- | --- | 
| prometheus.remoteWriteUrl | The remote write URL of your Amazon Managed Service for Prometheus workspace, for example `https://aps-workspaces.{{us-west-2}}.amazonaws.com/workspaces/{{ws-11111111-2222-3333-4444-555555555555}}/api/v1/remote_write`. The workspace must be in the same AWS Region as the cluster.<br />If you don't specify `prometheus` when you install the extension, the extension sends metrics to Amazon CloudWatch. To change an installed extension to Amazon CloudWatch, set `prometheus` to `null`. | 
| metricsProvider.{{type}}.level | The collection level for a metric type:+  `nodeMetrics` and `acceleratedComputeMetrics`—`BASIC` (default), `ADVANCED`, or `DISABLED`. <br />+  `clusterMetrics`, `networkMetrics`, and `jobMetrics`—`ENABLED` (default) or `DISABLED`. <br />+  `ncclMetrics`—`ENABLED` or `DISABLED` (default). When `ncclMetrics` is `ENABLED`, `nodeMetrics` can't be `DISABLED`.  | 
| metricsProvider.{{type}}.collectionIntervalSeconds | The collection interval for a metric type, from 30 to 300 seconds. The default is 30. | 

The following configuration values install the extension with Amazon CloudWatch as the metric store.

```json
{}
```

The following configuration values send metrics to an Amazon Managed Service for Prometheus workspace.

```json
{
    "prometheus": {
        "remoteWriteUrl": "https://aps-workspaces.{{us-west-2}}.amazonaws.com/workspaces/{{ws-11111111-2222-3333-4444-555555555555}}/api/v1/remote_write"
    }
}
```

## Updating the extension
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-updating-the-extension"></a>

To change the configuration, run `update-cluster-extension` with only the settings that you want to change. HyperPod applies `ConfigurationValues` to the stored configuration as a JSON merge patch (RFC 7396): keys that you don't specify keep their stored values, and a key with the value `null` is removed and returns to its default. HyperPod validates the merged configuration before it applies it. An update restarts only the components whose settings change, and the other components keep collecting.

For example, the following command sends metrics to Amazon CloudWatch instead of Amazon Managed Service for Prometheus:

```
aws sagemaker update-cluster-extension \
    --cluster-arn {{arn:aws:sagemaker:us-west-2:111122223333:cluster/abcde1234567}} \
    --extension-arn {{extension-arn}} \
    --configuration-values '{"prometheus":null}'
```

Replace {{extension-arn}} with the ARN of the installed extension. To get the ARN, use the `ListClusterExtensions` API operation.

To change back to Amazon Managed Service for Prometheus, specify `prometheus.remoteWriteUrl` again. After you change the metric store, the extension sends new metrics only to the new metric store. It doesn't copy metrics that are already in the old one. Metrics in an Amazon Managed Service for Prometheus workspace stay there for the retention period of the workspace.

To move to a later version, add `--extension-version`.

## Permissions for the observability extension
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-iam"></a>

The extension runs with the execution role of each instance group. The role needs the following actions for the features that you use:
+ Metrics in Amazon CloudWatch—`cloudwatch:PutMetricData`
+ Metrics in Amazon Managed Service for Prometheus—`aps:RemoteWrite` on the workspace

When the console creates the execution role, the role allows `cloudwatch:PutMetricData`.

The AWS managed policy [AmazonSageMakerClusterInstanceRolePolicy](security-iam-awsmanpol-AmazonSageMakerClusterInstanceRolePolicy.md) allows `cloudwatch:PutMetricData`. If your execution role has this policy, the role needs no other permissions for Amazon CloudWatch metrics. The policy doesn't allow `aps:RemoteWrite`. To send metrics to Amazon Managed Service for Prometheus, add a statement like the following to the execution role.

```json
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "aps:RemoteWrite",
            "Resource": "arn:aws:aps:{{us-west-2}}:{{111122223333}}:workspace/{{workspace-ID}}"
        }
    ]
}
```

## Viewing the metrics of the observability extension
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-view-metrics"></a>

When Amazon CloudWatch is the metric store, the extension sends the metrics to the CloudWatch OpenTelemetry Protocol (OTLP) endpoint. You can query the metrics with the Prometheus Query Language (PromQL) in Query Studio in the CloudWatch console, with the Prometheus-compatible query API, or in Amazon Managed Grafana. To query the metrics, you need the `cloudwatch:GetMetricData` and `cloudwatch:ListMetrics` permissions. For more information, see [Query metrics with PromQL](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-PromQL.html) in the *Amazon CloudWatch User Guide*.

The extension adds the resource attributes `aws.sagemaker.hyperpod.cluster.name`, `aws.sagemaker.hyperpod.cluster.arn`, `aws.sagemaker.hyperpod.cluster.id`, `aws.sagemaker.hyperpod.instance_group.name`, `cloud.resource_id`, and `host.name` to each metric. In PromQL, add the prefix `@resource.` to a resource attribute and put the label name in quotation marks, for example `{"@resource.aws.sagemaker.hyperpod.cluster.name"="{{my-cluster}}"}`.

When you choose an Amazon Managed Grafana workspace in the console, the console sets up a data source for the metric store and the SageMaker HyperPod dashboards in the workspace. The **Grafana dashboards** row on the **Amazon SageMaker HyperPod observability** card shows the status of this setup. For Amazon CloudWatch, the workspace must run Grafana version 12 or later, because the dashboards need the Amazon Managed Service for Prometheus data source plugin.

```
avg by ("@resource.host.name") (DCGM_FI_DEV_GPU_UTIL{"@resource.aws.sagemaker.hyperpod.cluster.name"="my-cluster"})
```

**Amazon Managed Service for Prometheus.** The same attributes are labels, with each `.` replaced by `_`, for example `aws_sagemaker_hyperpod_cluster_name`.

**Amazon Managed Grafana.** Dashboards are optional. An Amazon Managed Grafana workspace needs AWS IAM Identity Center or SAML for user authentication; for more information, see [Authenticate users in Amazon Managed Grafana workspaces](https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html) in the *Amazon Managed Grafana User Guide*. When you choose a Grafana workspace in the console, the console sets up a data source for the metric store and the SageMaker HyperPod dashboards in the workspace. The **Grafana dashboards** row on the **Amazon SageMaker HyperPod observability** card shows the status of this setup. For Amazon CloudWatch, the workspace must run Grafana version 12 or later. If you change the metric store, the console replaces the HyperPod Slurm dashboards in that workspace the next time that you view the cluster. If other HyperPod clusters use the workspace, the console asks you first.

An Amazon Managed Grafana workspace needs AWS IAM Identity Center or SAML for user authentication. For more information, see [Authenticate users in Amazon Managed Grafana workspaces](https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html) in the *Amazon Managed Grafana User Guide*.

## Collected metrics
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-collected-metrics"></a>


| Setting | What it collects | 
| --- | --- | 
| nodeMetrics | Prometheus node exporter metrics (node\_\*): CPU, memory, disk, file system, network, and load. ADVANCED adds the cgroups, ksmd, meminfo\_numa, ethtool, mountstats, network\_route, processes, and tcpstat collectors. | 
| acceleratedComputeMetrics | NVIDIA DCGM fields (DCGM\_FI\_\*). BASIC collects 23 fields: clocks, temperatures, power and energy, utilization, frame buffer memory, XID errors, PCIe replays, row remapping, and graphics engine, tensor pipe, DRAM, and PCIe activity. ADVANCED collects 47, adding error-correcting code (ECC) errors, retired pages, NVLink errors and bandwidth, and throttling counters. | 
| networkMetrics | EFA device counters. | 
| jobMetrics | Per-job resource usage on compute nodes, which attributes GPU usage to Slurm jobs. | 
| clusterMetrics | Slurm node, job, partition, and scheduler metrics from the Slurm controller's built-in metrics endpoints. To list the names, query for metrics that start with slurm\_. | 
| ncclMetrics | Metrics for the NCCL collective operations of your jobs, while the jobs run. | 

## Health
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-health"></a>

Each node reports the health of the extension and each of its components. For how health appears in `DescribeClusterExtension` and in the health metrics, see [Monitoring cluster extension health](sagemaker-hyperpod-slurm-extensions-health.md). When you fix the cause on the node, the health issue clears on its own, and you don't call an API.

The following example is a health record from a compute node without GPUs or EFA devices.

```
{
    "InstanceId": "i-0123456789abcdef0",
    "ExtensionName": "sagemaker-observability",
    "ExtensionVersion": "1.0.0",
    "Status": "HEALTHY",
    "Code": "ALL_COMPONENTS_HEALTHY",
    "Message": "All observability components are healthy",
    "EvaluatedAt": "2026-11-20T04:34:44Z",
    "Components": [
        { "Name": "node-exporter",        "Status": "HEALTHY", "Code": "SERVICE_RUNNING",    "Message": "prometheus-node-exporter is active" },
        { "Name": "slurm-job-exporter",   "Status": "HEALTHY", "Code": "SERVICE_RUNNING",    "Message": "hyperpod-slurm-job-exporter is active" },
        { "Name": "otel-collector",       "Status": "HEALTHY", "Code": "SERVICE_RUNNING",    "Message": "hyperpod-otel-collector is active" },
        { "Name": "otel-exporter-health", "Status": "HEALTHY", "Code": "HEALTH_ENDPOINT_OK", "Message": "OK" }
    ],
    "Time": "2026-11-20T04:35:30Z"
}
```

**Extension health codes**


| Status | Code | Meaning | 
| --- | --- | --- | 
| HEALTHY | ALL\_COMPONENTS\_HEALTHY | Every component on the node is healthy. | 
| UNHEALTHY | ExtensionUnhealthy | A component is unhealthy. The message names the component and what to check (see the next table). | 
| UNKNOWN | COMPONENT\_STATUS\_UNKNOWN | A component couldn't be checked. | 
| UNKNOWN | NO\_COMPONENTS | No component was checked on the node. | 

When more than one component is unhealthy, the message names the first one in the following order, because the components lower in the list depend on the ones above them.


| Component | Message | 
| --- | --- | 
| otel-collector | The OpenTelemetry collector (hyperpod-otel-collector) is not running, so this node sends no metrics. Check /var/log/aws/clusters/sagemaker-observability-otel-collector.log on the node. | 
| otel-exporter-health | The collector has not sent metrics to the destination within its stale interval. Check that the execution role allows cloudwatch:PutMetricData or aps:RemoteWrite on the destination, and that the node can reach the destination endpoint. | 
| node-exporter | node-exporter (prometheus-node-exporter) is not running, so node metrics are missing. Check /var/log/aws/clusters/sagemaker-observability-node-exporter.log on the node. | 
| dcgm-exporter | dcgm-exporter (nvidia-dcgm-exporter) is not running, so GPU metrics are missing. Check /var/log/aws/clusters/sagemaker-observability-dcgm-exporter.log on the node. | 
| efa-exporter | efa-exporter (hyperpod-efa-exporter) is not running, so EFA network metrics are missing. Check /var/log/aws/clusters/sagemaker-observability-efa-exporter.log on the node. | 
| slurm-job-exporter | slurm-job-exporter (hyperpod-slurm-job-exporter) is not running, so Slurm job metrics are missing. Check /var/log/aws/clusters/sagemaker-observability-slurm-job-exporter.log on the node. | 

**Component health codes**


| Status | Code | Meaning | 
| --- | --- | --- | 
| HEALTHY | SERVICE\_RUNNING | The component's service is running. | 
| UNHEALTHY | SERVICE\_NOT\_RUNNING | The component's service isn't running. | 
| UNKNOWN | SYSTEMD\_CHECK\_FAILED | The service status couldn't be read. | 
| HEALTHY | HEALTH\_ENDPOINT\_OK | otel-exporter-health: the collector is delivering metrics. | 
| UNHEALTHY | HEALTH\_ENDPOINT\_UNHEALTHY | otel-exporter-health: the collector hasn't delivered metrics recently. | 
| UNKNOWN | HEALTH\_ENDPOINT\_UNREACHABLE | otel-exporter-health: the collector's health endpoint didn't respond. | 

## Logs
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-logs"></a>

The extension's components write logs to your cluster's log group, `/aws/sagemaker/Clusters/cluster-name/cluster-id`, in the following log streams.


| Component | Log stream | 
| --- | --- | 
| OpenTelemetry Collector | SageMakerObservabilityOtelCollector/instance-group/instance-id | 
| Node exporter | SageMakerObservabilityNodeExporter/instance-group/instance-id | 
| DCGM exporter | SageMakerObservabilityDcgmExporter/instance-group/instance-id | 
| EFA exporter | SageMakerObservabilityEfaExporter/instance-group/instance-id | 
| Slurm job exporter | SageMakerObservabilitySlurmJobExporter/instance-group/instance-id | 

To find nodes where the extension isn't healthy, run the following query in Amazon CloudWatch Logs Insights on the cluster's log group:

```
fields @timestamp, InstanceId, Status, Code, Message
| filter @logStream like /^SageMakerExtensionHealth\// and ExtensionName = "sagemaker-observability" and Status != "HEALTHY"
| sort @timestamp desc
```

## Troubleshooting
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-troubleshooting"></a>


| Symptom | Cause and fix | 
| --- | --- | 
| Install fails with ConfigurationConflict: "Port port, which component needs, is in use by another process." | Another process, often a lifecycle-script exporter, holds the port. Stop that process, or turn off the setting that the message names. Then [Retrying failed nodes](sagemaker-hyperpod-slurm-extensions.md#sagemaker-hyperpod-slurm-extensions-retrying-failed-nodes). | 
| Install fails with ConfigurationConflict and the message names glibc or task\_prolog.sh | NCCL metrics need glibc 2.34 or later and the Slurm task prolog of the HyperPod AMI. Use a supported AMI, or set ncclMetrics.level to DISABLED. | 
| Install fails with ConfigurationConflict and the message names the beta hyperpod-observability-reconciler-agent service | Your account used the earlier observability preview on the AMI. Contact AWS Support to move off it. | 
| otel-exporter-health is UNHEALTHY | The collector can't deliver metrics. For Amazon CloudWatch, check that the execution role allows cloudwatch:PutMetricData with StringEqualsIfExists. For Amazon Managed Service for Prometheus, check aps:RemoteWrite on the workspace. For private subnets, check the VPC endpoints. Look for AccessDenied in the SageMakerObservabilityOtelCollector log stream. | 
| A component reports SERVICE\_NOT\_RUNNING | Check the log file that the message names. | 

## Migrating from lifecycle scripts
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-migrating-from-lifecycle-scripts"></a>

If you collect metrics with the base lifecycle scripts (`enable_observability = True`), move to the extension as follows. Install the extension last: its install fails on any node where a lifecycle-script exporter still holds a port.

1. Make sure that your cluster meets the [Prerequisites for the observability extension](#sagemaker-hyperpod-cluster-observability-slurm-extension-prerequisites).

1. In the `config.py` file of your lifecycle scripts, set `enable_observability = False`, and upload the file to the Amazon Simple Storage Service (Amazon S3) location of your lifecycle scripts. New and replaced nodes then don't start the lifecycle-script exporters.

1. On each existing node, remove the exporter containers. The lifecycle scripts run them with `--restart always`, so stopping them isn't enough. The current lifecycle scripts name them `node-exporter`, `dcgm-exporter`, `efa-exporter`, and `otel-collector`:

   ```
   sudo docker rm -f node-exporter dcgm-exporter efa-exporter otel-collector
   ```

   A node that doesn't run one of these containers reports an error for that name. If your lifecycle scripts are older, run `sudo docker ps` to find the names. Run it on the controller and login nodes too, because the node exporter container runs there.

1. Install the extension. To keep your existing dashboards, set `prometheus.remoteWriteUrl` to the same Amazon Managed Service for Prometheus workspace.

1. Update your Grafana Slurm panels. Slurm metrics now come from the Slurm controller's built-in metrics (`slurm_*`) instead of the community Slurm exporter.

## Deleting the extension
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-deleting-the-extension"></a>

Deleting the extension stops and removes its components from every node. Metrics already in Amazon CloudWatch or Amazon Managed Service for Prometheus aren't deleted.