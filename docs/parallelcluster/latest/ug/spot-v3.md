# Working with Spot Instances

AWS ParallelCluster uses Spot Instances if you have set [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") /
[CapacityType](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-CapacityType "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-CapacityType") or [AwsBatchQueues](Scheduling-v3.md#Scheduling-v3-AwsBatchQueues "Scheduling-v3.md#Scheduling-v3-AwsBatchQueues") / [CapacityType](Scheduling-v3.md#yaml-Scheduling-AwsBatchQueues-CapacityType "Scheduling-v3.md#yaml-Scheduling-AwsBatchQueues-CapacityType") to `SPOT`
in the cluster configuration file. Spot Instances are more cost effective than On-Demand Instances, but they might be interrupted. It might help to
take advantage of _Spot Instance interruption notices_, which provide a two minute warning before Amazon EC2 must stop or terminate
your Spot Instance. For more information, see [Spot Instance interruptions](../../../AWSEC2/latest/UserGuide/spot-interruptions.md "../../../AWSEC2/latest/UserGuide/spot-interruptions.md") in
_Amazon EC2 User Guide_. To learn how [AwsBatchQueues](Scheduling-v3.md#Scheduling-v3-AwsBatchQueues "Scheduling-v3.md#Scheduling-v3-AwsBatchQueues") works with Spot Instances, see [Compute Resources](../../../batch/latest/userguide/compute_environment_parameters.md#compute_environment_compute_resources "../../../batch/latest/userguide/compute_environment_parameters.md#compute_environment_compute_resources")
in the _AWS Batch User Guide_.

The AWS ParallelCluster configured scheduler assigns jobs to compute resources in queues with spot instances in the same way it assigns jobs to
compute resources in queues with on-demand instances.

When using Spot Instances, an AWSServiceRoleForEC2Spot service-linked role must exist in your account. To create this role in your account using
the AWS CLI, run the following command:

```
`$` `aws iam create-service-linked-role --aws-service-name spot.amazonaws.com`
```

For more information, see [Service-linked role for Spot Instance requests](../../../AWSEC2/latest/UserGuide/spot-requests.md#service-linked-roles-spot-instance-requests "../../../AWSEC2/latest/UserGuide/spot-requests.md#service-linked-roles-spot-instance-requests")
in the _Amazon EC2 User Guide_.

The following sections describe three scenarios in which Spot Instances can be
interrupted when using [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues").

For more information about Spot Instances, see [Spot Instances](../../../AWSEC2/latest/UserGuide/using-spot-instances.md "../../../AWSEC2/latest/UserGuide/using-spot-instances.md") in the
_Amazon EC2 User Guide_.
