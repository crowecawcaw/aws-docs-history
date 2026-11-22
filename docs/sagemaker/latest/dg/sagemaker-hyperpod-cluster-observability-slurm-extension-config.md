

# Observability extension configuration

You configure the observability extension with a JSON object that you pass in the `ConfigurationValues` parameter of `CreateClusterExtension` and `UpdateClusterExtension`. All settings are optional. If you pass `{}`, the extension uses the default values and sends metrics to Amazon CloudWatch.

Setting names are case sensitive and use camel case. Unknown settings are rejected at every level, so a misspelled setting is reported instead of ignored. HyperPod writes the default values into the stored configuration, so `DescribeClusterExtension` shows every setting. If a later version changes a default value, your extension keeps the value that it has.

The following example shows every setting with its default value. Without `prometheus`, metrics go to Amazon CloudWatch.

```
{
  "prometheus": {
    "remoteWriteUrl": "https://aps-workspaces.us-west-2.amazonaws.com/workspaces/ws-11111111-2222-3333-4444-555555555555/api/v1/remote_write"
  },
  "metricsProvider": {
    "nodeMetrics":               { "level": "BASIC",    "collectionIntervalSeconds": 30 },
    "acceleratedComputeMetrics": { "level": "BASIC",    "collectionIntervalSeconds": 30 },
    "networkMetrics":            { "level": "ENABLED",  "collectionIntervalSeconds": 30 },
    "jobMetrics":                { "level": "ENABLED",  "collectionIntervalSeconds": 30 },
    "clusterMetrics":            { "level": "ENABLED",  "collectionIntervalSeconds": 30 },
    "ncclMetrics":               { "level": "DISABLED", "collectionIntervalSeconds": 30 }
  },
  "profilesProvider": {
    "hostProfiling": { "enabled": false }
  },
  "grafana": {
    "workspaceId": "g-0123456789"
  }
}
```

## prometheus
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-config-prometheus"></a>

The `prometheus` setting sends metrics to an Amazon Managed Service for Prometheus workspace. If you omit it, metrics go to Amazon CloudWatch. To switch back to Amazon CloudWatch, update the extension with `{"prometheus": null}`. Sending `{}` doesn't change the metric store. Before you switch, make sure that the execution role has the Amazon CloudWatch permission in [Permissions for the observability extension](sagemaker-hyperpod-cluster-observability-slurm-extension.md#sagemaker-hyperpod-cluster-observability-slurm-extension-iam).


| Setting | Type | Required | Description | 
| --- | --- | --- | --- | 
| remoteWriteUrl | String, up to 200 characters | Yes, if prometheus is present | The remote write URL of your workspace, in the format https://aps-workspaces.region.amazonaws.com/workspaces/workspace-id/api/v1/remote\_write. The workspace must be in the cluster's AWS Region, and the execution role needs aps:RemoteWrite on it. | 

## metricsProvider
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-config-metricsprovider"></a>

Each metric family has a `level` and a `collectionIntervalSeconds`.

For the metrics that each family collects, see [Collected metrics](sagemaker-hyperpod-cluster-observability-slurm-extension.md#sagemaker-hyperpod-cluster-observability-slurm-extension-collected-metrics).


| Setting | Valid values | Default | Description | 
| --- | --- | --- | --- | 
| nodeMetrics.level | BASIC, ADVANCED, DISABLED | BASIC | Host CPU, memory, disk, file system, network, and load metrics on every node. ADVANCED adds cgroup, non-uniform memory access (NUMA) memory, network interface (ethtool), Network File System (NFS) and Lustre mount, route, process, and TCP connection metrics. | 
| acceleratedComputeMetrics.level | BASIC, ADVANCED, DISABLED | BASIC | NVIDIA GPU metrics on compute nodes with GPUs. BASIC collects 23 NVIDIA Data Center GPU Manager (DCGM) fields. ADVANCED collects 47, adding ECC errors, retired pages, NVLink errors and bandwidth, and throttling counters. | 
| networkMetrics.level | ENABLED, DISABLED | ENABLED | EFA device counters on compute nodes with EFA devices. | 
| jobMetrics.level | ENABLED, DISABLED | ENABLED | Per-Slurm-job resource usage on compute nodes. | 
| clusterMetrics.level | ENABLED, DISABLED | ENABLED | Slurm node, job, partition, and scheduler metrics from the Slurm controller. | 
| ncclMetrics.level | ENABLED, DISABLED | DISABLED | NCCL collective communication metrics from the jobs on compute nodes. | 
| family.collectionIntervalSeconds | Integer, 30–300 | 30 | How often, in seconds, the metric family is collected. For ncclMetrics, how often each job process sends its NCCL metrics. | 

When `ncclMetrics` is `ENABLED`, `nodeMetrics` can't be `DISABLED`.

### NCCL metrics
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-config-nccl-metrics"></a>

When `ncclMetrics.level` is `ENABLED`, every Slurm job step on compute nodes loads the HyperPod NCCL profiler plugin. The following list describes what this means for your jobs.
+ The plugin replaces any `NCCL_PROFILER_PLUGIN` value that you set yourself. When you set `ncclMetrics.level` back to `DISABLED`, your own value applies again.
+ The change applies to job steps that start after the update. Running jobs aren't affected.
+ Containers that you run with Enroot and Pyxis get the plugin automatically.

**Note**  
NCCL metrics require the GNU C Library (glibc) version 2.34 or later on the compute nodes.

## profilesProvider
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-config-profilesprovider"></a>


| Setting | Valid values | Default | Description | 
| --- | --- | --- | --- | 
| hostProfiling.enabled | true, false | false | Turns on ongoing CPU profiling of Slurm worker nodes. Controller, login, and restricted instance groups are excluded. Requires Linux kernel 5.9 or later, and cloudwatch:PutOtelProfiles on the execution role. | 

## grafana
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-config-grafana"></a>


| Setting | Valid values | Description | 
| --- | --- | --- | 
| workspaceId | g- followed by 10 lowercase hexadecimal characters, or an empty string | The ID of an existing Amazon Managed Grafana workspace that you use to view the metrics. When you choose a workspace in the console, the console sets this value and sets up the data source and dashboards in that workspace. It doesn't change what the extension collects. | 

## Reserved names
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-config-reserved-names"></a>

Don't include `region`, `clusterArn`, `clusterName`, or `previousVersion` in your configuration. HyperPod sets these values itself, and rejects them if you supply them.

## Example configurations
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-config-example-configurations"></a>

**Standard metrics in Amazon CloudWatch.** Pass `{}`. This collects basic node metrics on every node, basic GPU metrics on GPU compute nodes, EFA metrics on EFA nodes, job metrics on compute nodes, and Slurm cluster metrics from the controller, every 30 seconds.

The following configuration sets up a GPU training cluster that sends metrics to Amazon Managed Service for Prometheus, with all GPU metrics and NCCL metrics:

```
{
  "prometheus": {
    "remoteWriteUrl": "https://aps-workspaces.us-west-2.amazonaws.com/workspaces/ws-11111111-2222-3333-4444-555555555555/api/v1/remote_write"
  },
  "grafana": { "workspaceId": "g-0123456789" },
  "metricsProvider": {
    "acceleratedComputeMetrics": { "level": "ADVANCED" },
    "ncclMetrics": { "level": "ENABLED" }
  }
}
```

The following configuration sets up a CPU cluster that collects node, job, and Slurm cluster metrics every 60 seconds and turns off GPU and network metrics:

```
{
  "metricsProvider": {
    "nodeMetrics":               { "level": "BASIC", "collectionIntervalSeconds": 60 },
    "acceleratedComputeMetrics": { "level": "DISABLED" },
    "networkMetrics":            { "level": "DISABLED" },
    "jobMetrics":                { "level": "ENABLED", "collectionIntervalSeconds": 60 },
    "clusterMetrics":            { "level": "ENABLED", "collectionIntervalSeconds": 60 }
  }
}
```

**Slurm cluster metrics only.** The controller collects Slurm cluster metrics, and the other nodes collect nothing.

```
{
  "metricsProvider": {
    "nodeMetrics":               { "level": "DISABLED" },
    "acceleratedComputeMetrics": { "level": "DISABLED" },
    "networkMetrics":            { "level": "DISABLED" },
    "jobMetrics":                { "level": "DISABLED" }
  }
}
```

**Temporary advanced node metrics.** Turn on advanced node metrics during an investigation, and then return to the default. Only the node exporter restarts, and the other components keep collecting.

```
--configuration-values '{"metricsProvider":{"nodeMetrics":{"level":"ADVANCED"}}}'
--configuration-values '{"metricsProvider":{"nodeMetrics":null}}'
```

## Validation errors
<a name="sagemaker-hyperpod-cluster-observability-slurm-extension-config-validation-errors"></a>

If the configuration isn't valid, `CreateClusterExtension` and `UpdateClusterExtension` return a `ValidationException` that lists up to five problems, each with the path to the setting, and the extension doesn't change. For example:

```
ConfigurationValues does not match the schema for extension sagemaker-observability version 1.0.0: /metricsProvider/nodeMetrics/level: must be one of "BASIC", "ADVANCED", "DISABLED"
```


| Mistake | Message detail | 
| --- | --- | 
| Unknown setting, for example nodeMetric | /metricsProvider: has properties the schema does not permit | 
| Invalid level, for example HIGH | /metricsProvider/nodeMetrics/level: must be one of "BASIC", "ADVANCED", "DISABLED" | 
| BASIC on a family that is only on or off | /metricsProvider/jobMetrics/level: must be one of "ENABLED", "DISABLED" | 
| Interval out of range | …/collectionIntervalSeconds: must be at least 30 (or must be at most 300) | 
| Interval as a string, for example "30" | …/collectionIntervalSeconds: must be of type integer | 
| prometheus without a URL | /prometheus: is missing required property "remoteWriteUrl" | 
| A workspace in another AWS Region | /prometheus/remoteWriteUrl: is in region 'us-east-1' but the cluster's region is 'us-west-2' | 