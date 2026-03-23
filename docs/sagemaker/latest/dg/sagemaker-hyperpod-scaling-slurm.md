# Continuous provisioning for enhanced cluster operations with Slurm

Amazon SageMaker HyperPod clusters created with Slurm orchestration now support continuous
provisioning, a capability that enables greater flexibility and efficiency when running
large-scale AI/ML workloads. Continuous provisioning lets you start training quickly, scale
seamlessly, perform maintenance without disrupting operations, and have granular visibility
into cluster operations.

###### Note

Continuous provisioning is available as an optional configuration for new
HyperPod clusters created with Slurm orchestration. Existing clusters using the
previous scaling model cannot be migrated to continuous provisioning at this time.

## How it works

The continuous provisioning system introduces a desired-state architecture that
replaces the traditional all-or-nothing scaling model. In the previous model, if any
instance group could not be fully provisioned, the entire cluster creation or update
operation failed and rolled back. With continuous provisioning, the system accepts
partial capacity and continues to provision remaining instances asynchronously.

The continuous provisioning system:

- **Accepts the request**: Records the target
  instance count for each instance group.
- **Initiates provisioning**: Begins launching
  instances for all instance groups in parallel.
- **Provisions priority nodes first**: The cluster
  transitions to `InService` after at least one controller node (and
  one login node, if a login instance group is specified) is successfully
  provisioned.
- **Tracks progress**: Monitors each instance
  launch attempt and records the status.
- **Handles failures**: Automatically retries
  failed launches for worker nodes asynchronously.

Continuous provisioning is disabled by default. To use this feature, set
`NodeProvisioningMode` to `Continuous` in your
`CreateCluster` request.

With continuous provisioning enabled, you can initiate multiple scaling operations
simultaneously without waiting for previous operations to complete. This lets you scale
different instance groups in the same cluster concurrently and submit multiple scaling
requests to the same instance group.

## Priority-based provisioning

Slurm clusters require a controller node to be operational before worker nodes can
register and accept jobs. Continuous provisioning handles this automatically through
priority-based provisioning:

1. The controller instance group is provisioned first.
2. Once one controller node is healthy, login nodes and worker nodes begin
   provisioning in parallel.
3. The cluster transitions to `InService` when one controller node is
   up and one login node is up (if a login instance group is specified). If no login
   instance group is specified, the cluster transitions to `InService` as
   soon as the controller node is provisioned.
4. Worker nodes that cannot be immediately provisioned due to capacity constraints
   enter an asynchronous retry loop and are added to the Slurm cluster automatically
   as they become available.

## Controller failure handling

During cluster creation, if the controller node fails to provision, the behavior
depends on whether the error is retryable or non-retryable.

**Retryable errors** (for example, unhealthy instance or
transient failures):

- HyperPod continuously replaces the instance and retries provisioning
  until the controller comes up.
- Worker and login nodes that have already been provisioned remain available, but
  the cluster does not transition to `InService` until the controller is
  healthy.

**Non-retryable errors** (for example, no capacity
available for the controller instance type or lifecycle script failure):

- The cluster is marked as `Failed`.
- You are notified of the failure reason and must take corrective action, such as
  choosing a different instance type, fixing lifecycle scripts, or retrying in a
  different Availability Zone.

## Prerequisites

Continuous provisioning requires that Slurm provisioning parameters (node types,
partition names) are provided via the API payload in each instance group's
`SlurmConfig` field. Clusters that rely on the legacy
`provisioning_parameters.json` file in Amazon S3 are not compatible with
continuous provisioning.

###### Note

The following features are not currently supported with continuous provisioning on
Slurm clusters: migration of existing clusters, multi-head node configuration via
API-based Slurm topology, and `SlurmConfigStrategy`. Continuous
provisioning operates exclusively in merge mode for `slurm.conf`
management.

## Usage metering

HyperPod clusters with continuous provisioning use instance-level metering to
provide accurate billing that reflects actual resource usage. This metering approach
differs from traditional cluster-level billing by tracking each instance
independently.

**Instance-level billing**

With continuous provisioning, billing starts and stops at the individual instance level
rather than waiting for cluster-level state changes. This approach provides the following
benefits:

- **Precise billing accuracy**: Billing starts when
  the lifecycle script execution begins. If the lifecycle script fails, the
  instance provision will be retried and you are charged for the duration of the
  lifecycle script runtime.
- **Independent metering**: Each instance's billing
  lifecycle is managed separately, preventing cascading billing errors.
- **Real-time billing updates**: Billing starts
  when an instance begins executing its lifecycle configuration script and stops
  when the instance enters a terminating state.

**Billing lifecycle**

Each instance in your HyperPod cluster follows this billing lifecycle:

- **Billing starts**: When the instance
  successfully launches and begins executing its lifecycle configuration
  script.
- **Billing continues**: Throughout the instance's
  operational lifetime.
- **Billing stops**: When the instance enters a
  terminating state, regardless of the reason for termination.

###### Note

Billing does not start for instances that fail to launch. If an instance launch
fails due to insufficient capacity or other issues, you are not charged for that
failed attempt. Billing is calculated at the instance level and costs are aggregated
and reported under your cluster's Amazon Resource Name (ARN).

## Create a cluster with continuous provisioning enabled

###### Note

Prepare a lifecycle configuration script and upload it to an Amazon S3 bucket that your
execution role can access. For more information, see [SageMaker HyperPod Slurm cluster operations](sagemaker-hyperpod-operate-slurm.md "sagemaker-hyperpod-operate-slurm.md").

Prepare a `CreateCluster` API request file in JSON format. Set
`NodeProvisioningMode` to `Continuous` and provide Slurm
topology information in each instance group's `SlurmConfig` field.

```
// create_cluster.json
{
    "ClusterName": "my-training-cluster",
    "NodeProvisioningMode": "Continuous",
    "Orchestrator": {
        "Slurm": {}
    },
    "InstanceGroups": [
        {
            "InstanceGroupName": "controller-group",
            "InstanceType": "ml.m5.xlarge",
            "InstanceCount": 1,
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://amzn-s3-demo-bucket/lifecycle-scripts/src/",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/iam-role-for-cluster",
            "SlurmConfig": {
                "NodeType": "Controller"
            }
        },
        {
            "InstanceGroupName": "login-group",
            "InstanceType": "ml.m5.xlarge",
            "InstanceCount": 1,
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://amzn-s3-demo-bucket/lifecycle-scripts/src/",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/iam-role-for-cluster",
            "SlurmConfig": {
                "NodeType": "Login"
            }
        },
        {
            "InstanceGroupName": "worker-gpu-a",
            "InstanceType": "ml.p5.48xlarge",
            "InstanceCount": 16,
            "LifeCycleConfig": {
                "SourceS3Uri": "s3://amzn-s3-demo-bucket/lifecycle-scripts/src/",
                "OnCreate": "on_create.sh"
            },
            "ExecutionRole": "arn:aws:iam::111122223333:role/iam-role-for-cluster",
            "SlurmConfig": {
                "NodeType": "Compute",
                "PartitionNames": ["gpu-training"]
            }
        }
    ],
    "VpcConfig": {
        "SecurityGroupIds": ["sg-12345678"],
        "Subnets": ["subnet-12345678"]
    }
}
```

Run the `create-cluster` command to submit the request.

```
aws sagemaker create-cluster \
    --cli-input-json file://complete/path/to/create_cluster.json
```

This returns the ARN of the new cluster.

```
{
    "ClusterArn": "arn:aws:sagemaker:us-west-2:111122223333:cluster/abcde12345"
}
```

## Slurm configuration management

Continuous provisioning operates exclusively in merge mode for
`slurm.conf` partition management. In merge mode, HyperPod
applies its partition configuration changes additively on top of whatever you have
modified in `slurm.conf`. HyperPod only updates the
partition-related sections of `slurm.conf` (such as
partition name and node name entries); other Slurm
configuration parameters are not modified. This means:

- Your manual edits to `slurm.conf` are preserved.
- There is no automated drift detection or resolution of conflicts between your
  modifications and HyperPod's expected state.

The `SlurmConfigStrategy` parameter (`Managed`,
`Merge`, `Overwrite`) is not supported with continuous
provisioning. Passing any `SlurmConfigStrategy` value results in an
API error.
