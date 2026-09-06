

# Elastic Fabric Adapter
<a name="efa-v3"></a>

Elastic Fabric Adapter (EFA) is a network device that has OS-bypass capabilities for low-latency network communications with other instances on the same subnet. EFA is exposed by using Libfabric, and can be used by applications using the Messaging Passing Interface (MPI).

To use EFA with AWS ParallelCluster and a Slurm scheduler, set [`SlurmQueues`](Scheduling-v3.md#Scheduling-v3-SlurmQueues) / [`ComputeResources`](Scheduling-v3.md#Scheduling-v3-SlurmQueues-ComputeResources) / [`Efa`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-Efa) / [`Enabled`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-Efa-Enabled) to `true`.

To view the list of Amazon EC2 instances that support EFA, see [Supported instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types) in the *Amazon EC2 User Guide for Linux Instances*.

We recommend that you run your EFA-enabled instances in a placement group. This way the instances are launched into a low-latency group in a single Availability Zone. For more information on how to configure placement groups with AWS ParallelCluster, see [`SlurmQueues`](Scheduling-v3.md#Scheduling-v3-SlurmQueues) / [`Networking`](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking) / [`PlacementGroup`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup).

**Note**  
Elastic Fabric Adapter (EFA) isn't supported over different availability zones. For more information, see [Scheduling](Scheduling-v3.md) / [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues) / [Networking](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking) / [SubnetIds](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-SubnetIds).

**Note**  
By default, Ubuntu distributions enable ptrace (process trace) protection. ptrace protection is disabled so that Libfabric works properly. For more information, see [Disable ptrace protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html#efa-start-ptrace) in the *Amazon EC2 User Guide*.

## Default EFA network configuration
<a name="efa-v3-default-config"></a>

Starting in AWS ParallelCluster 3.15.0, when EFA is enabled, AWS ParallelCluster automatically configures EFA-only network interfaces to separate EFA traffic from IP traffic. This maximizes EFA bandwidth while minimizing IP address consumption. AWS ParallelCluster determines the optimal configuration based on the capabilities of the instance type. Therefore, EFA-enabled compute nodes are launched with more than one network interface, even when they use a single-network-card instance type, provided that instance type supports more than one network interface.

This default configuration is recommended for most workloads, including tightly-coupled HPC and distributed AI/ML training.

**Note**  
Amazon EC2 does not auto-assign a public IP address to an instance launched with more than one network interface. EFA-enabled compute nodes launch with multiple network interfaces. These compute nodes fail to bootstrap if they rely on an auto-assigned public IP for internet access (a public subnet with no NAT gateway). Place these compute nodes in a private subnet with a [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) and set [AssignPublicIp](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-AssignPublicIp) to `false`. This requirement previously applied only to instance types with multiple network cards.

## Customizing EFA network interfaces
<a name="efa-v3-custom-interfaces"></a>

If your workload requires a different network configuration, such as maximizing ENA bandwidth on secondary network cards or configuring a subset of available network cards, you can override the default settings using the [`SlurmQueues`](Scheduling-v3.md#Scheduling-v3-SlurmQueues) / [`ComputeResources`](Scheduling-v3.md#Scheduling-v3-SlurmQueues-ComputeResources) / [`LaunchTemplateOverrides`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-LaunchTemplateOverrides) parameter. This replaces the entire network interface configuration of the compute nodes with the configuration defined in your launch template.

For a step-by-step walkthrough, see [Customize compute node network interfaces with launch template overrides](tutorial-network-customization-v3.md).

**Warning**  
If you configure network interfaces in a way that is not supported by the instance type, instances will fail to launch. To verify the supported network configurations for your instance type, see [DescribeInstanceTypes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceTypes.html) in the *Amazon EC2 API Reference*.

For more information, see [Elastic Fabric Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) in the *Amazon EC2 User Guide* and [Scale HPC workloads with elastic fabric adapter and AWS ParallelCluster](https://aws.amazon.com/blogs/opensource/scale-hpc-workloads-elastic-fabric-adapter-and-aws-parallelcluster/) in the *AWS Open Source Blog*.