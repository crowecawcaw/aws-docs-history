# Elastic Fabric Adapter

Elastic Fabric Adapter (EFA) is a network device that has OS-bypass capabilities for low-latency network communications with other instances on
the same subnet. EFA is exposed by using Libfabric, and can be used by applications using the Messaging Passing Interface (MPI).

To use EFA with AWS ParallelCluster and a Slurm scheduler, set [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") / [ComputeResources](Scheduling-v3.md#Scheduling-v3-SlurmQueues-ComputeResources "Scheduling-v3.md#Scheduling-v3-SlurmQueues-ComputeResources") / [Efa](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-Efa "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-Efa") / [Enabled](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-Efa-Enabled "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-Efa-Enabled") to `true`.

To view the list of Amazon EC2 instances that support EFA, see [Supported instance types](../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types "../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types")
in the _Amazon EC2 User Guide for Linux Instances_.

We recommend that you run your EFA-enabled instances in a placement group. This way the instances are launched into a
low-latency group in a single Availability Zone. For more information on how to configure placement groups with
AWS ParallelCluster, see [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") / [Networking](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking "Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking") / [PlacementGroup](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup").

For more information, see [Elastic Fabric
Adapter](../../../AWSEC2/latest/UserGuide/efa.md "../../../AWSEC2/latest/UserGuide/efa.md") in the _Amazon EC2 User Guide_ and [Scale HPC workloads with elastic fabric adapter and AWS ParallelCluster](https://aws.amazon.com/blogs/opensource/scale-hpc-workloads-elastic-fabric-adapter-and-aws-parallelcluster/ "https://aws.amazon.com/blogs/opensource/scale-hpc-workloads-elastic-fabric-adapter-and-aws-parallelcluster/") in the _AWS Open Source
Blog_.

###### Note

Elastic Fabric Adapter (EFA) isn't supported over different availability zones. For more information, see
[Scheduling](Scheduling-v3.md "Scheduling-v3.md") / [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") /
[Networking](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking "Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking") / [SubnetIds](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SubnetIds "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SubnetIds").

###### Note

By default, Ubuntu distributions enable ptrace (process trace) protection. ptrace protection is disabled so that Libfabric works properly. For more
information, see [Disable
ptrace protection](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-ptrace "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-ptrace") in the _Amazon EC2 User Guide_.
