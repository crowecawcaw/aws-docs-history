

# Working with Spot Instances
<a name="spot-v3"></a>

AWS ParallelCluster uses Spot Instances if you have set [`SlurmQueues`](Scheduling-v3.md#Scheduling-v3-SlurmQueues) / [`CapacityType`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-CapacityType) or [`AwsBatchQueues`](Scheduling-v3.md#Scheduling-v3-AwsBatchQueues) / [`CapacityType`](Scheduling-v3.md#yaml-Scheduling-AwsBatchQueues-CapacityType) to `SPOT` in the cluster configuration file. Spot Instances are more cost effective than On-Demand Instances, but they might be interrupted. It might help to take advantage of *Spot Instance interruption notices*, which provide a two minute warning before Amazon EC2 must stop or terminate your Spot Instance. For more information, see [Spot Instance interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html) in *Amazon EC2 User Guide*. To learn how [`AwsBatchQueues`](Scheduling-v3.md#Scheduling-v3-AwsBatchQueues) works with Spot Instances, see [Compute Resources](https://docs.aws.amazon.com/batch/latest/userguide/compute_environment_parameters.html#compute_environment_compute_resources) in the *AWS Batch User Guide*.

The AWS ParallelCluster configured scheduler assigns jobs to compute resources in queues with spot instances in the same way it assigns jobs to compute resources in queues with on-demand instances.

When using Spot Instances, an AWSServiceRoleForEC2Spot service-linked role must exist in your account. To create this role in your account using the AWS CLI, run the following command:

```
$ aws iam create-service-linked-role --aws-service-name spot.amazonaws.com
```

For more information, see [Service-linked role for Spot Instance requests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html#service-linked-roles-spot-instance-requests) in the *Amazon EC2 User Guide*.

The following sections describe three scenarios in which Spot Instances can be interrupted when using [`SlurmQueues`](Scheduling-v3.md#Scheduling-v3-SlurmQueues).

For more information about Spot Instances, see [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) in the *Amazon EC2 User Guide*.