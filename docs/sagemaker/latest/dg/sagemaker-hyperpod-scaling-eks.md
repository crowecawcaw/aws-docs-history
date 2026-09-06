

# Continuous provisioning for enhanced cluster operations on Amazon EKS
<a name="sagemaker-hyperpod-scaling-eks"></a>

Amazon SageMaker HyperPod clusters created with Amazon EKS orchestration now supports continuous provisioning, a new capability that enables greater flexibility and efficiency running large-scale AI/ML workloads. Continuous provisioning lets you start training quickly, scale seamlessly, perform maintenance without disrupting operations, and have granular visibility into cluster operations. 

**Note**  
Continuous provisioning is available as an optional configuration for HyperPod clusters created with EKS orchestration. HyperPod clusters created with Slurm orchestration also support continuous provisioning. For details, see [Continuous provisioning for enhanced cluster operations with Slurm](sagemaker-hyperpod-scaling-slurm.md).

## How it works
<a name="sagemaker-hyperpod-scaling-eks-how"></a>

The continuous provisioning system introduces a desired-state architecture that replaces the traditional request-based model. This new architecture enables parallel, non-blocking operations across different resource levels while maintaining system stability and performance. The continuous provisioning system:
+ **Accepts the request**: Records the target instance count for each instance group
+ **Initiates provisioning**: Begins launching instances to meet the target count

  **Tracks progress**: Monitors each instance launch attempt and records the status
+ **Handles failures**: Automatically retries failed launches

Continuous provisioning is disabled by default. To use this feature, set `--node-provisioning-mode` to `Continuous`.

With continuous provisioning enabled, you can initiate multiple scaling operations simultaneously without waiting for previous operations to complete. This lets you scale different instance groups in the same cluster concurrently and submit multiple scaling requests to the same instance group. 

Continuous provisioning also gives you access to [DescribeClusterEvent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterEvent.html) and [ListClusterEvent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterEvents.html) for detailed event monitoring and operational visibility. 

## Usage metering
<a name="sagemaker-hyperpod-scaling-eks-metering"></a>

HyperPod clusters with continuous provisioning use instance-level metering to provide accurate billing that reflects actual resource usage. This metering approach differs from traditional cluster-level billing by tracking each instance independently.

**Instance-level billing**

With continuous provisioning, billing starts and stops at the individual instance level rather than waiting for cluster-level state changes. This approach provides the following benefits:
+ **Precise billing accuracy**: Billing starts when the lifecycle script execution begins. If the lifecycle script fails, the instance provision will be retried and you will be charged for the duration of the lifecycle script runtime.
+ **Independent metering**: Each instance's billing lifecycle is managed separately, preventing cascading billing errors
+ **Real-time billing updates**: Billing starts when an instance begins executing its lifecycle script and stops when the instance enters a terminating state

**Billing lifecycle**

Each instance in your HyperPod cluster follows this billing lifecycle:
+ **Billing starts**: When the instance successfully launches and begins executing its lifecycle configuration script
+ **Billing continues**: Throughout the instance's operational lifetime
+ **Billing stops**: When the instance enters a terminating state, regardless of the reason for termination

**Note**  
Billing does not start for instances that fail to launch. If an instance launch fails due to insufficient capacity or other issues, you are not charged for that failed attempt. Billing is calculated at the instance level and costs are aggregated and reported under your cluster's Amazon Resource Name (ARN). 

## Create a cluster with continuous provisioning enabled
<a name="sagemaker-hyperpod-scaling-eks-create"></a>

**Note**  
You must have an existing Amazon EKS cluster configured with VPC networking and the required Helm chart installed. Additionally, prepare a lifecycle configuration script and upload it to an Amazon S3 bucket that your execution role can access. For more information, see [Managing SageMaker HyperPod clusters orchestrated by Amazon EKS](sagemaker-hyperpod-eks-operate.md).

The following AWS CLI operation creates a HyperPod cluster with one instance group and continuous provisioning enabled.

```
aws sagemaker create-cluster \ 
--cluster-name $HP_CLUSTER_NAME \
--orchestrator 'Eks={ClusterArn='$EKS_CLUSTER_ARN'}' \
--vpc-config '{
   "SecurityGroupIds": ["'$SECURITY_GROUP'"],
   "Subnets": ["'$SUBNET'"]
}' \
--instance-groups '{
   "InstanceGroupName": "ig-1",
   "InstanceType": "ml.c5.2xlarge",
   "InstanceCount": 2,
   "LifeCycleConfig": {
      "SourceS3Uri": "s3://'$BUCKET_NAME'",
      "OnCreate": "on_create_noop.sh"
   },
   "ExecutionRole": "'$EXECUTION_ROLE'",
   "ThreadsPerCore": 1,
   "TrainingPlanArn": ""
}' \
--node-provisioning-mode Continuous


// Expected Output:
{
    "ClusterArn": "arn:aws:sagemaker:us-west-2:<account-id>:cluster/<cluster-id>"
}
```

After you’ve created your cluster, you can use [ListClusterNodes](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterNodes.html) or [DescribeClusterNode](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterNode.html) to find out more information about the nodes in the cluster. 

Calling these operations will return a [ClusterInstanceStatusDetails](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterInstanceStatusDetails.html) object with one of the following values: 
+  **Running**: The node is healthy and registered with the cluster orchestrator (EKS). 
+  **Failure**: The node provisioning failed but the system will automatically retry provisioning with a new EC2 instance. 
+  **Pending**: The node is being provisioned or rebooted. 
+  **ShuttingDown**: The node termination is in progress. The node will either transition to Failure status if termination encounters issues, or will be successfully removed from the cluster. 
+  **SystemUpdating**: The node is undergoing AMI patching, either triggered manually or as part of patching cronjobs. 
+  **DeepHealthCheckInProgress**: [Deep health checks (DHCs)](sagemaker-hyperpod-eks-resiliency-deep-health-checks.md) are being conducted. This could take anywhere between a few mins to several hours depending on the nature of tests. Bad nodes are replaced and healthy nodes switch to Running. 
+  **NotFound** : Used in [BatchAddClusterNodes](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchAddClusterNodes.html) response to indicate a node has been deleted during idempotent replay. 

## Minimum capacity requirements (MinCount)
<a name="sagemaker-hyperpod-scaling-eks-mincount"></a>

The MinCount feature allows you to specify the minimum number of instances that must be successfully provisioned before an instance group transitions to the `InService` status. This feature provides better control over scaling operations and helps prevent scenarios where partially provisioned instance groups cannot be used effectively for training workloads.

**Important**  
MinCount is not a permanent guarantee of minimum capacity. It only ensures that the specified minimum number of instances are available when the instance group first becomes `InService`. Brief dips below MinCount may occur during normal operations such as unhealthy instance replacements or maintenance activities.

### How MinCount works
<a name="sagemaker-hyperpod-scaling-eks-mincount-how"></a>

When you create or update an instance group with MinCount enabled, the following behavior occurs:
+ **New instance groups**: The instance group remains in `Creating` status until at least MinCount instances are successfully provisioned and ready. Once this threshold is met, the instance group transitions to `InService`.
+ **Existing instance groups**: When updating MinCount on an existing instance group, the status changes to `Updating` until the new MinCount requirement is satisfied.
+ **Continuous scaling**: If TargetCount is greater than MinCount, the continuous scaling system continues attempting to launch additional instances until TargetCount is reached.
+ **Timeout and rollback**: If MinCount cannot be satisfied within 3 hours, the system automatically rolls back the instance group to its last known good state. For more information about rollback behavior, see [Automatic rollback behavior](#sagemaker-hyperpod-scaling-eks-mincount-rollback).

### Instance group status during MinCount operations
<a name="sagemaker-hyperpod-scaling-eks-mincount-status"></a>

Instance groups with MinCount configured exhibit the following status behavior:

Creating  
For new instance groups when CurrentCount < MinCount. The instance group remains in this status until the minimum capacity requirement is met.

Updating  
For existing instance groups when MinCount is modified and CurrentCount < MinCount. The instance group remains in this status until the new minimum capacity requirement is satisfied.

InService  
When MinCount ≤ CurrentCount ≤ TargetCount. The instance group is ready for use and all mutating operations are unblocked.

During `Creating` or `Updating` status, the following restrictions apply:
+ Mutating operations such as `BatchAddClusterNodes`, `BatchDeleteClusterNodes`, or `UpdateClusterSoftware` are blocked
+ You can still modify MinCount and TargetCount values to correct configuration errors
+ Cluster and Instance group deletion is always permitted

### Automatic rollback behavior
<a name="sagemaker-hyperpod-scaling-eks-mincount-rollback"></a>

If an instance group cannot reach its MinCount within 3 hours, the system automatically initiates a rollback to prevent indefinite waiting:
+ **New instance groups**: MinCount and TargetCount are reset to (0, 0)
+ **Existing instance groups**: MinCount and TargetCount are restored to their values from the last `InService` state
+ **Instance selection for termination**: If instances need to be terminated during rollback, the system selects the unhealthy instances first, then those that were most recently provisioned.
+ **Status transition**: The instance group immediately transitions to `InService` status after rollback initiation, allowing the continuous scaling system to manage capacity according to the rollback settings

The 3-hour timeout resets each time MinCount is updated. For example, if you update MinCount multiple times, the timeout period starts fresh from the most recent update.

### MinCount events
<a name="sagemaker-hyperpod-scaling-eks-mincount-events"></a>

The system emits specific events to help you track MinCount operations:
+ **Minimum capacity reached**: Emitted when an instance group successfully reaches its MinCount and transitions to `InService`
+ **Rollback initiated**: Emitted when the 3-hour timeout expires and automatic rollback begins

You can monitor these events using [ListClusterEvents](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterEvents.html) to track the progress of your MinCount operations.

### API usage
<a name="sagemaker-hyperpod-scaling-eks-mincount-api"></a>

MinCount is specified using the `MinInstanceCount` parameter in instance group configurations:

```
aws sagemaker create-cluster \
--cluster-name $HP_CLUSTER_NAME \
--orchestrator 'Eks={ClusterArn='$EKS_CLUSTER_ARN'}' \
--vpc-config '{
   "SecurityGroupIds": ["'$SECURITY_GROUP'"],
   "Subnets": ["'$SUBNET'"]
}' \
--instance-groups '{
   "InstanceGroupName": "worker-group",
   "InstanceType": "ml.p4d.24xlarge",
   "InstanceCount": 64,
   "MinInstanceCount": 50,
   "LifeCycleConfig": {
      "SourceS3Uri": "s3://'$BUCKET_NAME'",
      "OnCreate": "on_create.sh"
   },
   "ExecutionRole": "'$EXECUTION_ROLE'"
}' \
--node-provisioning-mode Continuous
```

Key considerations for MinCount usage:
+ `MinInstanceCount` must be between 0 and `InstanceCount` (inclusive) value of the instance group specified in [CreateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCluster.html) or [UpdateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html) request
+ Setting `MinInstanceCount` to 0 (default) preserves standard continuous scaling behavior
+ Setting `MinInstanceCount` equal to `InstanceCount` provides all-or-nothing scaling behavior
+ MinCount is only available for clusters with `NodeProvisioningMode` set to `Continuous`

## Flexible instance groups
<a name="sagemaker-hyperpod-scaling-eks-flexible-ig"></a>

Flexible instance groups allow you to specify multiple instance types within a single instance group. This simplifies cluster management by reducing the number of instance groups you need to create and manage, especially for inference workloads that use autoscaling.

With flexible instance groups, HyperPod:
+ Attempts to provision instances using the first instance type in your list
+ Falls back to subsequent instance types if capacity is unavailable
+ Terminates instances of the lowest-priority instance type first during scale-down

**Note**  
Flexible instance groups are only available for clusters with `NodeProvisioningMode` set to `Continuous`. The `InstanceType` and `InstanceRequirements` properties are mutually exclusive—you can specify one or the other, but not both.

### Create a cluster with a flexible instance group
<a name="sagemaker-hyperpod-scaling-eks-flexible-ig-create"></a>

Use `InstanceRequirements` instead of `InstanceType` to create a flexible instance group. The order of instance types in the list determines the priority for provisioning.

```
aws sagemaker create-cluster \
--cluster-name $HP_CLUSTER_NAME \
--orchestrator 'Eks={ClusterArn='$EKS_CLUSTER_ARN'}' \
--vpc-config '{
   "SecurityGroupIds": ["'$SECURITY_GROUP'"],
   "Subnets": ["'$SUBNET_AZ1'", "'$SUBNET_AZ2'"]
}' \
--instance-groups '[{
   "InstanceGroupName": "flexible-ig",
   "InstanceRequirements": {
      "InstanceTypes": ["ml.p5.48xlarge", "ml.p4d.24xlarge", "ml.g6.48xlarge"]
   },
   "InstanceCount": 10,
   "LifeCycleConfig": {
      "SourceS3Uri": "s3://'$BUCKET_NAME'",
      "OnCreate": "on_create.sh"
   },
   "ExecutionRole": "'$EXECUTION_ROLE'"
}]' \
--node-provisioning-mode Continuous
```

### Targeted scaling with BatchAddClusterNodes
<a name="sagemaker-hyperpod-scaling-eks-flexible-ig-targeted"></a>

When using flexible instance groups, you can use [BatchAddClusterNodes](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchAddClusterNodes.html) to add nodes with specific instance types and availability zones. This is particularly useful when Karpenter autoscaling determines the optimal instance type and availability zone for your workload.

```
aws sagemaker batch-add-cluster-nodes \
--cluster-name $HP_CLUSTER_NAME \
--nodes-to-add '[
   {
      "InstanceGroupName": "flexible-ig",
      "IncrementTargetCountBy": 1,
      "InstanceTypes": ["ml.p5.48xlarge"],
      "AvailabilityZones": ["us-west-2a"]
   }
]'
```

### View flexible instance group details
<a name="sagemaker-hyperpod-scaling-eks-flexible-ig-describe"></a>

Use [DescribeCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCluster.html) to view the instance types and per-type breakdown of your flexible instance group. The response includes:
+ `InstanceRequirements` — The current and desired instance types for the instance group
+ `InstanceTypeDetails` — A per-instance-type breakdown showing the count and configuration of each instance type in the group

### Using flexible instance groups with Karpenter autoscaling
<a name="sagemaker-hyperpod-scaling-eks-flexible-ig-autoscaling"></a>

Flexible instance groups integrate with HyperPod's managed Karpenter autoscaling. For more information about setting up Karpenter, see [Autoscaling on SageMaker HyperPod EKS](sagemaker-hyperpod-eks-autoscaling.md). When you reference a flexible instance group in a `HyperPodNodeClass` configuration, Karpenter automatically:
+ Detects the supported instance types from the flexible instance group
+ Selects the optimal instance type and availability zone based on pod requirements and pricing
+ Scales the flexible instance group using targeted `BatchAddClusterNodes` calls with the selected instance type and availability zone

**Note**  
When Karpenter manages scaling, it uses its own selection logic based on pod requirements and pricing to determine which instance type to provision. This differs from the list-order priority used by HyperPod's native provisioning (such as `CreateCluster` and `UpdateCluster`), where the first instance type in the list is always attempted first.

This eliminates the need to create separate instance groups for each instance type and manually configure Karpenter to reference multiple groups.