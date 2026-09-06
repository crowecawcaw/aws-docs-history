

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Decrease latency for applications with long boot times using warm pools with managed node groups
<a name="warm-pools-managed-node-groups"></a>

When your applications have long initialization or boot times, scale-out events can cause delays—new nodes must fully boot and join the cluster before Pods can be scheduled on them. This latency can impact application availability during traffic spikes or rapid scaling events. Warm pools solve this problem by maintaining a pool of pre-initialized EC2 instances that have already completed the bootup process. During a scale-out event, instances move from the warm pool directly to your cluster, bypassing the time-consuming initialization steps and significantly reducing the time it takes for new capacity to become available. For more information, see [Decrease latency for applications that have long boot times using warm pools](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html) in the *Amazon EC2 Auto Scaling User Guide*.

Amazon EKS managed node groups support Amazon EC2 Auto Scaling warm pools. A warm pool maintains pre-initialized EC2 instances alongside your Auto Scaling group that can quickly join your cluster during scale-out events. Instances in the warm pool have already completed the bootup initialization process and can be kept in a `Stopped`, `Running`, or `Hibernated` state.

Amazon EKS manages warm pools throughout the node group lifecycle using the `AWSServiceRoleForAmazonEKSNodegroup` service-linked role to create, update, and delete warm pool resources.

## How it works
<a name="warm-pools-how-it-works"></a>

When you configure a warm pool, Amazon EKS creates an EC2 Auto Scaling warm pool attached to your node group’s Auto Scaling group. Instances launch into the warm pool, complete the bootup initialization process, and remain in the configured state (`Running`, `Stopped`, or `Hibernated`) until needed. During scale-out events, instances move from the warm pool to the Auto Scaling group, complete the Amazon EKS initialization process to join the cluster, and become available for pod scheduling. With instance reuse enabled, instances can return to the warm pool during scale-in events.

**Important**  
Always configure warm pools through the Amazon EKS API using `create-nodegroup` or `update-nodegroup-config`. Don’t manually modify warm pool settings using the EC2 Auto Scaling API, as this can cause conflicts with Amazon EKS management of the resources.

## Considerations
<a name="warm-pools-considerations"></a>

**Important**  
Before configuring warm pools, review the prerequisites and limitations in [Warm pools for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html) in the *Amazon EC2 Auto Scaling User Guide*. Not all instance types, AMIs, or configurations are supported.
+  **IAM permissions** – The `AWSServiceRoleForAmazonEKSNodegroup` service-linked role (created automatically with your first managed node group) includes the necessary warm pool management permissions.
+  **AMI limitations** – Warm pools don’t support custom AMIs. You must use Amazon EKS optimized AMIs.
+  **Bottlerocket limitations** – If using Bottlerocket AMIs, the `Hibernated` pool state isn’t supported. Use `Stopped` or `Running` pool states only. Additionally, the `reuseOnScaleIn` feature isn’t supported with Bottlerocket AMIs.
+  **Hibernation support** – The `Hibernated` pool state is only supported on specific instance types. See [Hibernation prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html) in the *Amazon EC2 User Guide* for supported instance types.
+  **Cost impact** – Creating a warm pool when it’s not required can lead to unnecessary costs.
+  **Capacity planning** – Size your warm pool based on scaling patterns to balance cost and availability. Start with 10-20% of expected peak capacity.
+  **VPC networking** – Ensure sufficient IP addresses for both Auto Scaling group and warm pool instances.

## Configure warm pools
<a name="warm-pools-configuration"></a>

You can configure warm pools when creating a new managed node group or update an existing managed node group to add warm pool support.

### Configuration parameters
<a name="warm-pools-parameters"></a>
+  **enabled** – (boolean) Indicates your intent to attach a warm pool to the managed node group. Required to enable warm pool support.
+  **maxGroupPreparedCapacity** – (integer) Maximum total instances across warm pool and Auto Scaling group combined.
+  **minSize** – (integer) Minimum number of instances to maintain in the warm pool. Default: `0`.
+  **poolState** – (string) State for warm pool instances. Default: `Stopped`.
+  **reuseOnScaleIn** – (boolean) Whether instances return to the warm pool during scale-in events instead of terminating them. Default: `false`. Not supported with Bottlerocket AMIs.

### Using the AWS CLI
<a name="warm-pools-create-cli"></a>

You can configure a warm pool when creating a managed node group or add one to an existing node group.

 **Create a node group with a warm pool** 

```
aws eks create-nodegroup \
  --cluster-name my-cluster \
  --nodegroup-name my-nodegroup \
  --node-role arn:aws:iam::111122223333:role/AmazonEKSNodeRole \
  --subnets subnet-12345678 subnet-87654321 \
  --region us-east-1 \
  --scaling-config minSize=2,maxSize=10,desiredSize=3 \
  --warm-pool-config enabled=true,maxGroupPreparedCapacity=8,minSize=2,poolState=Stopped,reuseOnScaleIn=true
```

 **Add a warm pool to an existing node group** 

```
aws eks update-nodegroup-config \
  --cluster-name my-cluster \
  --nodegroup-name my-nodegroup \
  --region us-east-1 \
  --warm-pool-config enabled=true,maxGroupPreparedCapacity=8,minSize=2,poolState=Stopped,reuseOnScaleIn=true
```

## Update configuration
<a name="warm-pools-update"></a>

Update warm pool settings at any time using `update-nodegroup-config`. Existing warm pool instances aren’t immediately affected; new settings apply to instances entering the warm pool after the update.

```
aws eks update-nodegroup-config \
  --cluster-name my-cluster \
  --nodegroup-name my-nodegroup \
  --region us-east-1 \
  --warm-pool-config enabled=true,maxGroupPreparedCapacity=10,minSize=3,poolState=Running,reuseOnScaleIn=true
```

To disable the warm pool attached to your nodegroup, set `enabled=false`:

```
aws eks update-nodegroup-config \
  --cluster-name my-cluster \
  --nodegroup-name my-nodegroup \
  --region us-east-1 \
  --warm-pool-config enabled=false
```

## Additional resources
<a name="warm-pools-additional-resources"></a>
+  [Warm pools for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html) in the *Amazon EC2 Auto Scaling User Guide* 
+  [Simplify node lifecycle with managed node groups](managed-node-groups.md) 