# Using topology-aware scheduling in Amazon SageMaker HyperPod

Data transfer efficiency is a critical factor in high-performance computing (HPC) and machine learning workloads. When using UltraServers with Amazon SageMaker HyperPod, SageMaker HyperPod automatically applies topology labels to your resources. Topology-aware scheduling
helps allocate resources to minimize data transfer overheads by considering both instance topology
(how resources are connected within an instance) and network topology (how instances are connected with each other).
For more information about instance topology, see
[Amazon EC2 instance topology](../../../AWSEC2/latest/UserGuide/ec2-instance-topology.md "../../../AWSEC2/latest/UserGuide/ec2-instance-topology.md").

Topology-aware scheduling works with both clusters on Slurm and Amazon EKS. For general information about
how topology works with Slurm, see the [Topology
guide in the Slurm documentation](https://slurm.schedmd.com/topology.html "https://slurm.schedmd.com/topology.html").

In Amazon SageMaker HyperPod, data transfer overheads typically come from three main sources:

- **GPU-to-GPU data transfer**: Modern technologies like NVLink and NVLink switches allow high-throughput data transfer between GPUs without involving other compute resources. This is extremely efficient but usually limited to a single instance.
- **GPU-to-CPU data transfer**: Non-uniform memory access (NUMA) systems have multiple system buses on a single motherboard. In a typical EC2 instance architecture like p5.48xlarge, there are two different system buses, each with a CPU and 4 GPUs. For optimal performance, processes that load or read data to/from GPUs should execute on a CPU connected to the same system bus as the GPU.
- **Network communications between instances**: Instances transfer
  data through a chain of network switches. The shortest path typically corresponds to the lowest latency.

## UltraServer architecture

SageMaker HyperPod supports UltraServer architecture with p6e-gb200.36xlarge instances. An UltraServer contains up to 18 p6e-gb200.36xlarge instances,
with 4 GPUs on each instance. All GPUs across all nodes are interconnected through NVLink switches, enabling data transfer between any two GPUs without using network interfaces.

This architecture provides a significant performance boost compared to individual instances. To leverage this architecture effectively,
jobs should be submitted to compute nodes from a single UltraServer.

## EKS topology label

In accordance with EC2 instance topology, HyperPod automatically labels your nodes with the following labels:

- **topology.kubernetes.io/region** - the AWS Region that the node resides in.
- **topology.kubernetes.io/zone** - the Availability Zone that the node resides in.
- **topology.k8s.aws/network-node-layer** - NetworkNodes describes the network node set of an instance.
  In each network node set, the network nodes are listed in a hierarchical order from top to bottom. The network node that is connected
  to the instance is the last network node in the list. There are up to four network node layers, and each node is tagged with a label.
  Available layers are `topology.k8s.aws/network-node-layer-1`, `topology.k8s.aws/network-node-layer-2`,
  `topology.k8s.aws/network-node-layer-3`.
- **topology.k8s.aws/ultraserver-id** - An identifier used to label each of
  the instances belonging to the same NVLink domain in an Ultraserver. To learn more about using
  UltraServers with SageMaker HyperPod, see [Using UltraServers in Amazon SageMaker HyperPod](sagemaker-hyperpod-ultraserver.md "sagemaker-hyperpod-ultraserver.md").

Using these labels, you can use topology-aware scheduling in HyperPod task governance to apply topology labels and
annotations to optimize training efficiency of your workloads. For more information, see
[Using topology-aware scheduling in Amazon SageMaker HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance-tasks-scheduling.md "sagemaker-hyperpod-eks-operate-console-ui-governance-tasks-scheduling.md").

## Slurm network topology plugins

Slurm provides built-in plugins for network topology awareness. UltraServer architecture in SageMaker HyperPod
supports the block plugin.

### Using the topology/block Plugin

NVIDIA developed a topology/block plugin that provides hierarchical scheduling across blocks of nodes with the following characteristics:

- A block is a consecutive range of nodes
- Blocks cannot overlap with each other
- All nodes in a block are allocated to a job before the next block is used
- The planning block size is the smallest block size configured
- Every higher block level size is a power of two than the previous one

This plugin allocates nodes based on the defined network topology.

#### Configuration

To configure topology-aware scheduling with the topology/block plugin,

- SageMaker HyperPod automatically configures the topology/block plugin.
  If you want to configure the plugin, specify the following in the topology.conf file in your Slurm configuration directory:

```
BlockName=us1 Nodes=ultraserver1-[0-17]

BlockName=us2 Nodes=ultraserver2-[0-17]

BlockSizes=18
```

- Ensure your `slurm.conf` includes:

```
TopologyPlugin=topology/block
```

#### Usage

When submitting jobs, you can use the following additional arguments with `sbatch` and `srun` commands:

- `--segment=N`: Specify the number of nodes to group together. The size of the segment must be less than or equal to the planning block size.
- `--exclusive=topo`: Request that no other jobs be placed on the same block. This is useful for benchmarking and performance-sensitive applications.

The following are sample scenarios you might consider when thinking about allocating blocks.

**Allocate a whole block of nodes on an empty system**

```
sbatch -N18
```

**Allocate two blocks of nodes on an empty system**

```
sbatch -N36
```

**Allocate 18 nodes on one block + 6 nodes on another block**

```
sbatch -N24
```

**Allocate 12 nodes on one block and 12 nodes on another block**

```
sbatch -N24 —segment=12
```

**With —exclusive=topo, job must be placed on block with no other jobs**

```
sbatch -N12 —exclusive=topo
```

## Best practices for UltraServer topology

For optimal performance with UltraServer architecture in SageMaker HyperPod:

- **Set appropriate block sizes**: Configure `BlockSizes=18` (or 17 if one node is spare) to match the UltraServer architecture.
- **Use segments for better availability**: Use `--segment=16`, `--segment=8`, or `--segment=9` with `srun` and `sbatch` commands to improve job scheduling flexibility.
- **Consider job size and segment size**:
  - If `BlockSizes=18`, jobs with up to 18 instances will always run on a single UltraServer.
  - If `BlockSizes=16`, jobs with fewer than 16 instances will always run on a single UltraServer, while jobs with 18 instances may run on one or two UltraServers.

When thinking about segmenting, consider the following

- With `--segment=1`, each instance can run on a separate UltraServer.
- With `-N 18 --segment 9`, 9 nodes will be placed on one UltraServer, and another 9 nodes can be placed on the same or another UltraServer.
- With `-N 24 --segment 8`, the job can run on 2 or 3 UltraServers, with every 8 nodes placed together on the same server.

## Limitations in SageMaker HyperPod topology aware scheduling

The `topology/block` plugin has limitations with heterogeneous clusters (clusters with different instance types):

- Only nodes listed in blocks are schedulable by Slurm
- Every block must have at least `BlockSizes[0]` nodes

For heterogeneous clusters, consider these alternatives:

- Do not use the block plugin with heterogeneous clusters. Instead, isolate UltraServer nodes in a different partition.
- Create a separate cluster with UltraServers only in the same VPC and use Slurm's multicluster setup.
