

# Deep health checks
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks"></a>

SageMaker HyperPod performs *deep health checks* on Slurm-orchestrated cluster instances to ensure the reliability and stability of the underlying hardware and infrastructure. Deep health checks can run automatically when instances are created or added to a cluster (*on-start*), or you can trigger them manually at any time (*on-demand*) using the [StartClusterHealthCheck](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartClusterHealthCheck.html) API. This proactive approach helps identify and mitigate potential issues throughout the cluster lifecycle.

During deep health checks, affected nodes are placed in a Slurm maintenance reservation to prevent jobs from being scheduled on them. Once all checks pass, the nodes are released from the reservation and become available for workloads.

**Important**  
To use deep health checks, you must update to the latest AMI version. Run [UpdateClusterSoftware](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html) to update to the latest version of the AMI. If you are running on an older AMI version, deep health checks may not function as expected.

## Deep health check types
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-types"></a>

SageMaker HyperPod supports two categories of deep health checks for Slurm clusters:
+ **InstanceStress** — Runs instance-level tests including hardware stress testing (CPU, memory, disk, GPU/PCI verification), DCGM GPU diagnostics, and EFA loopback connectivity. This validates the health of individual node hardware.
+ **InstanceConnectivity** — Runs cluster-level NCCL (NVIDIA Collective Communications Library) tests across multiple nodes to verify inter-node GPU communication performance. This check is only supported on instances with multi-node GPU communication capabilities.

## List of deep health checks done by SageMaker HyperPod
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-list"></a>

SageMaker HyperPod runs the following deep health checks.

**Instance-level deep health checks (InstanceStress)**


| Category | Utility name | Instance type compatibility | Description | 
| --- | --- | --- | --- | 
| Accelerator | GPU/NVLink count | GPU | Verifies GPU/NVLink counts. | 
| Accelerator | [DCGM diagnostics](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html) level 4 | GPU | Assesses the health and functionality of NVIDIA GPUs by running DCGM (NVIDIA Data Center GPU Manager) diagnostics at level 4, including additional memory tests. Typical duration: \~45-90 minutes depending on GPU count. | 
| Network | EFA | GPU | Runs EFA loopback bandwidth and latency tests on the attached EFA device. Typical duration: \~2-5 minutes. | 

**Cluster-level deep health checks (InstanceConnectivity)**


| Category | Utility name | Instance type compatibility | Description | 
| --- | --- | --- | --- | 
| Accelerator | NCCL test | GPU | Runs NCCL all\_reduce performance tests across multiple nodes to verify inter-node GPU communication bandwidth. Typical duration: \~5-15 minutes depending on node count. | 

## On-start deep health checks
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-on-start"></a>

On-start deep health checks run automatically when instances are first provisioned — during cluster creation or when new instances are added via [UpdateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html). This ensures every node passes hardware validation before accepting workloads.

### Enabling on-start deep health checks
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-on-start-enabling"></a>

To enable on-start deep health checks, specify the `OnStartDeepHealthChecks` parameter in the instance group configuration when creating or updating a cluster.

**Example: Create a cluster with on-start deep health checks**

```
aws sagemaker create-cluster \
  --cluster-name {{my-slurm-cluster}} \
  --instance-groups '[
    {
      "InstanceGroupName": "controller-group",
      "InstanceType": "ml.m5.xlarge",
      "InstanceCount": 1,
      "LifeCycleConfig": {
        "SourceS3Uri": "s3://{{my-bucket}}/lifecycle-scripts/",
        "OnCreate": "on_create.sh"
      },
      "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/{{my-role}}",
      "ThreadsPerCore": 1
    },
    {
      "InstanceGroupName": "worker-group",
      "InstanceType": "ml.p4d.24xlarge",
      "InstanceCount": 4,
      "LifeCycleConfig": {
        "SourceS3Uri": "s3://{{my-bucket}}/lifecycle-scripts/",
        "OnCreate": "on_create.sh"
      },
      "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/{{my-role}}",
      "ThreadsPerCore": 1,
      "OnStartDeepHealthChecks": ["InstanceStress", "InstanceConnectivity"]
    }
  ]' \
  --vpc-config '{"SecurityGroupIds":["{{sg-12345678}}"],"Subnets":["{{subnet-12345678}}"]}'
```

### What happens during on-start deep health checks
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-on-start-process"></a>

When on-start deep health checks are enabled, the following process occurs:

1. **Node provisioning**: New instances are launched and lifecycle scripts execute.

1. **Node isolation**: The HyperPod cluster agent places new nodes in a Slurm maintenance reservation (`hyperpod-deep-health-check`) and adds them to the `hyperpod-system-maintenance` partition. Nodes are marked with the Slurm feature `SageMakerDeepHealthCheck:InProgress`. This prevents jobs from being scheduled on these nodes during testing.

1. **Test execution**: The following tests run on each node as part of the `InstanceStress` check:
   + **HARDWARE\_CHECK**: Runs `stress-ng` for CPU, memory, and disk stress testing, followed by GPU and PCI device count verification. Typical duration: \~1-2 minutes.
   + **DCGM**: Runs NVIDIA DCGM diagnostics at level 4, including GPU memory tests. Typical duration: \~45-90 minutes depending on GPU count.
   + **EFA**: Runs EFA loopback bandwidth and latency tests. Typical duration: \~2-5 minutes.

   If `InstanceConnectivity` is also enabled, the following additional test is executed:
   + **NCCL**: Runs NCCL `all_reduce` performance tests across multiple nodes to verify inter-node GPU communication bandwidth. Typical duration: \~5-15 minutes depending on node count.

1. **Result handling**:
   + **Pass**: The node is removed from the maintenance reservation, the deep health check feature is cleared, and the node becomes available for jobs in its assigned partition.
   + **Fail**: The node remains isolated. SageMaker HyperPod automatically replaces the failed node and runs deep health checks on the replacement.

The cluster transitions to `InService` once at least the controller node is running. Worker nodes show `DeepHealthCheckInProgress` status during testing and transition to `Running` after passing.

### Monitoring on-start deep health checks
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-on-start-monitoring"></a>

You can monitor the status of on-start deep health checks using the Amazon SageMaker AI API or Slurm commands.

**Check node status using the AWS Command Line Interface**

```
aws sagemaker list-cluster-nodes \
  --cluster-name {{my-slurm-cluster}}
```

Nodes undergoing deep health checks show `InstanceStatus.Status` as `DeepHealthCheckInProgress`.

**Check Slurm state via SSM on the controller node**

```
# View node states
sinfo -a -N -l

# View maintenance reservation
scontrol show reservations

# View running DHC jobs
squeue -a
```

Nodes under deep health check appear in the `hyperpod-deep-health-check` reservation and the `hyperpod-system-maintenance` partition.

### Adding nodes to a cluster with on-start deep health checks enabled
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-on-start-add-nodes"></a>

When you scale up a cluster that has `OnStartDeepHealthChecks` configured, new nodes automatically go through deep health checks before accepting workloads. Existing nodes and running jobs are not affected.

```
aws sagemaker update-cluster \
  --cluster-name {{my-slurm-cluster}} \
  --instance-groups '[
    {
      "InstanceGroupName": "controller-group",
      "InstanceType": "ml.m5.xlarge",
      "InstanceCount": 1,
      "LifeCycleConfig": {
        "SourceS3Uri": "s3://{{my-bucket}}/lifecycle-scripts/",
        "OnCreate": "on_create.sh"
      },
      "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/{{my-role}}",
      "ThreadsPerCore": 1
    },
    {
      "InstanceGroupName": "worker-group",
      "InstanceType": "ml.p4d.24xlarge",
      "InstanceCount": 8,
      "LifeCycleConfig": {
        "SourceS3Uri": "s3://{{my-bucket}}/lifecycle-scripts/",
        "OnCreate": "on_create.sh"
      },
      "ExecutionRole": "arn:aws:iam::{{111122223333}}:role/{{my-role}}",
      "ThreadsPerCore": 1,
      "OnStartDeepHealthChecks": ["InstanceStress", "InstanceConnectivity"]
    }
  ]'
```

The new nodes are isolated in the maintenance reservation while deep health checks run. Jobs that require the additional capacity from the new nodes wait until those nodes pass deep health checks and become available. Jobs that can be satisfied by existing available nodes are not affected.

## On-demand deep health checks
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-on-demand"></a>

On-demand deep health checks let you trigger hardware validation on existing cluster nodes at any time using the [StartClusterHealthCheck](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartClusterHealthCheck.html) API. This is useful for periodic health validation or after suspected hardware issues.

### Running on-demand deep health checks from the console
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-on-demand-console"></a>

You can run deep health checks on HyperPod cluster instances directly from the SageMaker AI console.

**To run on-demand deep health checks from the console**

1. Open the SageMaker AI console at [SageMaker AI console](https://console.aws.amazon.com/sagemaker).

1. In the navigation pane, under **HyperPod**, choose **Clusters**.

1. Choose the name of your cluster to open the cluster detail page.

1. In the **Instances** table, select one or more instances that you want to run deep health checks on.
**Note**  
Supported instance families include g5, p4, and p5. Non-accelerated instances are automatically skipped.

1. Choose **Actions**, then choose **Run deep health checks**.

1. Select **Stress check**, **Connectivity check**, or both:
   + **Stress check** — Validates accelerator hardware under load (corresponds to `InstanceStress`).
   + **Connectivity check** — Validates inter-node network communication (corresponds to `InstanceConnectivity`).

1. Choose **Run health checks**.

A success banner confirms that the checks were initiated. Instances are unavailable for workloads during checks, which may take over an hour. Monitor instance status in the **Instances** table — it shows **Deep health check in progress** while running. When issues are found and automatic recovery is enabled, SageMaker HyperPod automatically reboots or replaces faulty instances.

### Triggering on-demand deep health checks using the AWS Command Line Interface
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-on-demand-triggering"></a>

You can specify which instance groups and which checks to run. Only one on-demand deep health check request can be active per cluster at a time.

```
aws sagemaker start-cluster-health-check \
  --cluster-name {{my-slurm-cluster}} \
  --deep-health-check-configurations '[
    {
      "InstanceGroupName": "worker-group",
      "DeepHealthChecks": ["InstanceStress", "InstanceConnectivity"]
    }
  ]'
```

### Behavior with running workloads
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-on-demand-behavior"></a>

When on-demand deep health checks are triggered on nodes that are running jobs:
+ Running jobs are **not** interrupted or terminated.
+ The deep health check is queued and waits for the current job to complete. If the running job does not complete within 10 minutes, the node is skipped from the deep health check.
+ Nodes are placed in the maintenance reservation to prevent new jobs from being scheduled during testing.

## Logs from the deep health checks
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-logs"></a>

The following are example logs from the SageMaker HyperPod deep health checks.

**Cluster-level logs**

The cluster-level deep health check logs are stored in your CloudWatch log group at `/aws/sagemaker/Clusters/<cluster_name>/<cluster_id>`.

The log streams are logged at `DeepHealthCheckResults/<log_stream_id>`.

**Instance-level logs**

On each node, deep health check logs are stored at `/var/log/aws/clusters/sagemaker-deep-health-check.log`.

You can access the log via SSM:

```
aws ssm start-session \
  --target "sagemaker-cluster:{{<cluster_id>}}_{{<instance_group>}}-{{<instance_id>}}"
```

Then view the log:

```
cat /var/log/aws/clusters/sagemaker-deep-health-check.log
```

**Example HARDWARE\_CHECK output**

```
2026-03-29T18:03:14Z  info  Executing Hardware stress check with command: stress-ng
2026-03-29T18:04:20Z  info  stress-ng success
2026-03-29T18:04:20Z  info  GpuPci Count check success
```

**Example DCGM output**

```
2026-03-29T18:35:02Z  info  DCGM diagnostic health summary: dcgmCheckLevel: 4
  dcgmVersion: 3.3.7 gpuDriverVersion: 535.183.01
  gpuDeviceIds: [2237] replacementRequired: false rebootRequired: false
```

**Example EFA output**

```
2026-03-29T18:36:28Z  info  EFA Loopback check passed for device: rdmap0s29
  MaxBw: 58.59, AvgBw: 32.42, MaxTypicalLat: 30.87, AvgLat: 21.63
```

**Example deep health check failure output**

```
{
    "level": "error",
    "ts": "2026-03-29T19:15:22Z",
    "msg": "Encountered FaultyInstance. Replace the Instance. Region: us-west-2, InstanceType: ml.g5.8xlarge. ERROR: Bandwidth has less than threshold: Expected minimum threshold: 80, NCCL Test output Bw: 30"
}
```

## Auto-resume behavior with deep health checks
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-auto-resume"></a>

Without deep health checks enabled, when a node is replaced during auto-resume, the replacement node is immediately added to the cluster and the auto-resumed job can be scheduled on it right away.

With deep health checks enabled, the replacement node must pass all configured deep health checks before it becomes available. However, the auto-resumed job does not have to wait for the replacement node — it can be scheduled on any other available node in the cluster. The job only waits if no other nodes are available.

## Additional considerations
<a name="sagemaker-hyperpod-resiliency-slurm-deep-health-checks-limitations"></a>
+ Deep health checks require the latest AMI version. Run [UpdateClusterSoftware](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html) to update your cluster before enabling deep health checks.
+ Deep health checks run on worker nodes only. Controller and login nodes are not subject to deep health checks.
+ Only one on-demand deep health check request can be active per cluster at a time.
+ If an on-demand check triggers a node reboot or replacement, the replacement node only runs deep health checks if `OnStartDeepHealthChecks` is enabled on the instance group. Otherwise, the node rejoins without re-running deep health checks.