

# Using topology-aware scheduling in Amazon SageMaker HyperPod
<a name="sagemaker-hyperpod-topology"></a>

Data transfer efficiency is a critical factor in high-performance computing (HPC) and machine learning workloads. When using UltraServers with Amazon SageMaker HyperPod, SageMaker HyperPod automatically applies topology labels to your resources. Topology-aware scheduling helps allocate resources to minimize data transfer overheads by considering both instance topology (how resources are connected within an instance) and network topology (how instances are connected with each other). For more information about instance topology, see [ Amazon EC2 instance topology](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology.html).

Topology-aware scheduling works with both clusters on Slurm and Amazon EKS. For general information about how topology works with Slurm, see the [Topology guide in the Slurm documentation](https://slurm.schedmd.com/topology.html).

In Amazon SageMaker HyperPod, data transfer overheads typically come from three main sources:
+ **GPU-to-GPU data transfer**: Modern technologies like NVLink and NVLink switches allow high-throughput data transfer between GPUs without involving other compute resources. This is extremely efficient but usually limited to a single instance.
+ **GPU-to-CPU data transfer**: Non-uniform memory access (NUMA) systems have multiple system buses on a single motherboard. In a typical EC2 instance architecture like p5.48xlarge, there are two different system buses, each with a CPU and 4 GPUs. For optimal performance, processes that load or read data to/from GPUs should execute on a CPU connected to the same system bus as the GPU.
+ **Network communications between instances**: Instances transfer data through a chain of network switches. The shortest path typically corresponds to the lowest latency.

## UltraServer architecture
<a name="sagemaker-hyperpod-topology-ultraserver-architecture"></a>

SageMaker HyperPod supports UltraServer architecture with p6e-gb200.36xlarge instances. An UltraServer contains up to 18 p6e-gb200.36xlarge instances, with 4 GPUs on each instance. All GPUs across all nodes are interconnected through NVLink switches, enabling data transfer between any two GPUs without using network interfaces.

This architecture provides a significant performance boost compared to individual instances. To leverage this architecture effectively, jobs should be submitted to compute nodes from a single UltraServer.

### EKS topology label
<a name="sagemaker-hyperpod-topology-eks-scheduling"></a>

In accordance with EC2 instance topology, HyperPod automatically labels your nodes with the following labels:
+ **topology.kubernetes.io/region** - the AWS Region that the node resides in.
+ **topology.kubernetes.io/zone** - the Availability Zone that the node resides in.
+ **topology.k8s.aws/network-node-layer** - NetworkNodes describes the network node set of an instance. In each network node set, the network nodes are listed in a hierarchical order from top to bottom. The network node that is connected to the instance is the last network node in the list. There are up to four network node layers, and each node is tagged with a label. Available layers are `topology.k8s.aws/network-node-layer-1`, `topology.k8s.aws/network-node-layer-2`, `topology.k8s.aws/network-node-layer-3`.
+ **topology.k8s.aws/ultraserver-id** - An identifier used to label each of the instances belonging to the same NVLink domain in an Ultraserver. To learn more about using UltraServers with SageMaker HyperPod, see [Using UltraServers in Amazon SageMaker HyperPod](sagemaker-hyperpod-ultraserver.md).

Using these labels, you can use topology-aware scheduling in HyperPod task governance to apply topology labels and annotations to optimize training efficiency of your workloads. For more information, see [Using topology-aware scheduling in Amazon SageMaker HyperPod task governance](sagemaker-hyperpod-eks-operate-console-ui-governance-tasks-scheduling.md).

## Slurm network topology plugins
<a name="sagemaker-hyperpod-topology-slurm-plugins"></a>

Slurm provides built-in plugins for network topology awareness. SageMaker HyperPod automatically selects and configures the appropriate topology plugin based on the instance types in your cluster.

### Automatic topology selection
<a name="sagemaker-hyperpod-topology-auto-selection"></a>

When you create a HyperPod Slurm cluster, the system inspects all instance groups and their associated instance types, identifies the GPU communication characteristics of each instance type, and configures Slurm with the appropriate topology plugin. This process runs automatically and does not require any configuration.

HyperPod manages topology through dynamically generated configuration files. On Slurm 25.11 and later, topology is defined in a `topology.yaml` file, which is the source of truth and supports multiple topology definitions and per-partition assignment. On Slurm 24.x, topology is defined in a `topology.conf` file with a single cluster-wide topology. As the cluster evolves through scaling operations or node replacements, HyperPod continuously reconciles the topology configuration to reflect the current cluster state. For more information, see [Dynamic topology updates](#sagemaker-hyperpod-topology-dynamic-updates).

### Instance types that support network topology
<a name="sagemaker-hyperpod-topology-supported-instances"></a>

HyperPod configures tree or block topology for instance types that support Amazon EC2 instance topology. For the authoritative, up-to-date list of supported instance types, see [Prerequisites for Amazon EC2 topology](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology-prerequisites.html#inst-net-topology-prereqs-instance-types) in the *Amazon EC2 User Guide*.

Supported instance types include accelerated computing families such as G6e, G7e, P4d, P4de, P5, P5e, P5en, and P6e-GB200, as well as AWS Trainium families such as Trn1, Trn1n, and Trn2. UltraServer instance types (for example, `ml.p6e-gb200.36xlarge`) use block topology, and other topology-capable instance types use tree topology.

### Using the topology/tree plugin
<a name="sagemaker-hyperpod-topology-tree"></a>

The `topology/tree` plugin models hierarchical communication structures with multiple bandwidth tiers. Tree topology enables Slurm to place jobs in a way that minimizes cross-tier communication and maximizes locality.

Tree topology is used for instance types with hierarchical interconnects, where distributed training workloads benefit from locality-aware placement. This includes instance types such as `ml.p5.48xlarge`, `ml.p5e.48xlarge`, and `ml.p5en.48xlarge`.

SageMaker HyperPod automatically configures the `topology/tree` plugin when your cluster uses these instance types. The generated topology configuration maps nodes into a switch hierarchy that reflects the communication tiers of your hardware.

Ensure your `slurm.conf` includes:

```
TopologyPlugin=topology/tree
```

#### Configuration
<a name="sagemaker-hyperpod-topology-tree-config"></a>

SageMaker HyperPod automatically configures tree topology based on information provided by Amazon EC2. For more details about Amazon EC2 topology, see [Amazon EC2 instance topology](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology.html).

On Slurm 25.11 and later, HyperPod defines topology in `topology.yaml`, which is the source of truth. A tree topology entry maps nodes into a switch hierarchy that reflects the communication tiers of your hardware:

```
- topology: tree
  cluster_default: true
  tree:
    switches:
      - switch: root
        children: leaf-0,leaf-1
      - switch: leaf-0
        nodes: compute-1,compute-2
      - switch: leaf-1
        nodes: compute-3,compute-4
```

On Slurm 24.x, tree topology is defined in `topology.conf` instead, which uses the following format:

```
SwitchName=nn-6fe9d8a965d34d181 Switches=nn-0b53107754517bf0e

SwitchName=nn-0b53107754517bf0e Switches=nn-424c855d4ad825aa4,nn-95acd7c656329fc30

SwitchName=nn-424c855d4ad825aa4 Nodes=ip-10-1-111-198
SwitchName=nn-95acd7c656329fc30 Nodes=ip-10-1-53-231
```

#### Usage
<a name="sagemaker-hyperpod-topology-tree-usage"></a>

When the `topology/tree` plugin is configured, Slurm tries to allocate machines that are close to each other. You can force Slurm to allocate machines on a single switch by passing the `--switch` command line parameter to `sbatch` or `srun`:

```
sbatch --switch=1 ....
```

### Using the topology/block plugin
<a name="sagemaker-hyperpod-topology-block"></a>

NVIDIA developed a `topology/block` plugin that provides hierarchical scheduling across blocks of nodes with the following characteristics:
+ A block is a consecutive range of nodes
+ Blocks cannot overlap with each other
+ All nodes in a block are allocated to a job before the next block is used
+ The planning block size is the smallest block size configured
+ Every higher block level size is a power of two than the previous one

This plugin allocates nodes based on the defined network topology.

Block topology models uniform, high-bandwidth communication domains where all GPUs participate in a single high-speed domain with near-uniform latency. Block topology treats all nodes as part of a single cohesive communication unit. UltraServer architecture in SageMaker HyperPod supports the block plugin.

Block topology is used for UltraServer instance types such as `ml.p6e-gb200.36xlarge`.

Ensure your `slurm.conf` includes:

```
TopologyPlugin=topology/block
```

#### Configuration
<a name="sagemaker-hyperpod-topology-block-config"></a>

SageMaker HyperPod automatically configures block topology. On Slurm 25.11 and later, block topology is defined in `topology.yaml`, which is the source of truth. Block and tree topologies for a cluster are defined together in the same file. The following example shows a cluster with a P5 partition (tree) and an UltraServer partition (block):

```
- topology: tree
  cluster_default: true
  tree:
    switches:
      - switch: root
        children: leaf-0,leaf-1
      - switch: leaf-0
        nodes: compute-p5-1,compute-p5-2
      - switch: leaf-1
        nodes: compute-p5-3,compute-p5-4
- topology: block
  cluster_default: false
  block:
    block_sizes:
      - 18
    blocks:
      - block: cb-001
        nodes: ultraserver-1-[1-18]
```

On Slurm 24.x, block topology is defined in `topology.conf` instead, which uses the following format:

```
BlockName=us1 Nodes=ultraserver1-[0-17]
BlockName=us2 Nodes=ultraserver2-[0-17]
BlockSizes=18
```

#### Usage
<a name="sagemaker-hyperpod-topology-block-usage"></a>

When submitting jobs, you can use the following additional arguments with `sbatch` and `srun` commands:
+ `--segment=N`: Specify the number of nodes to group together. The size of the segment must be less than or equal to the planning block size.
+ `--exclusive=topo`: Request that no other jobs be placed on the same block. This is useful for benchmarking and performance-sensitive applications.

The following are sample scenarios you might consider when thinking about allocating blocks.

**Allocate a whole block of nodes on an empty system**

```
sbatch -N18
```

**Allocate two blocks of nodes on an empty system**

```
sbatch -N36
```

**Allocate 18 nodes on one block \+ 6 nodes on another block**

```
sbatch -N24
```

**Allocate 12 nodes on one block and 12 nodes on another block**

```
sbatch -N24 --segment=12
```

**With --exclusive=topo, job must be placed on block with no other jobs**

```
sbatch -N12 --exclusive=topo
```

### Partition-level topology selection
<a name="sagemaker-hyperpod-topology-partition-level"></a>

Starting with Slurm 25.11, HyperPod supports topology configuration at the partition level. Each partition is assigned a topology based on the instance types of its compute instance groups, so a single cluster can run tree topology in one partition and block topology in another. Partitions that contain instance types without network topology support inherit a cluster-wide `flat` default, which keeps their nodes schedulable.

HyperPod resolves the topology for each partition as follows:
+ If every compute instance group in the partition is an UltraServer instance type, the partition uses `block` topology.
+ If every compute instance group in the partition supports network topology (and the partition is not all UltraServer), the partition uses `tree` topology.
+ If a partition contains both UltraServer and other topology-capable instance types, the partition uses `tree` topology.
+ If any compute instance group in the partition uses an instance type that does not support network topology, the partition has no topology assignment and inherits the cluster-wide `flat` default.

The cluster-wide default topology is selected based on the topologies present across the cluster: if only one topology type is present, that type is the default; if both block and tree are present with no non-topology groups, tree is the default; and if any non-topology compute group is present, `flat` is the default so that those nodes remain schedulable.

The following table shows an example of how HyperPod resolves topology for a cluster with mixed instance types.


| Instance group | Instance type | Applied topology | 
| --- | --- | --- | 
| IG-1 | ml.p5.48xlarge | Tree | 
| IG-2 | ml.p6e-gb200.36xlarge | Block | 

In this example, the P5 partition uses tree topology and the UltraServer partition uses block topology. With partition-level topology, each partition uses its optimal topology within the same cluster, so you no longer need to create separate clusters to give each instance type its ideal topology model.

**Note**  
On clusters running Slurm 24.x, only a single cluster-wide topology configuration is supported. Per-partition topology requires Slurm 25.11 or later.

### Flat topology default
<a name="sagemaker-hyperpod-topology-flat-default"></a>

When a cluster contains a mix of topology-capable and non-topology instance types, HyperPod applies `topology/flat` as the cluster default. Topology-aware partitions are pointed at their tree or block topology through per-partition `Topology=` directives in `slurm.conf` (Slurm 25.11 and later), while partitions with non-topology nodes have no `Topology=` directive and inherit the flat default. This ensures every node remains schedulable.

### Disable or change topology plugin
<a name="sagemaker-hyperpod-topology-disable-change"></a>

When a Slurm cluster is created, HyperPod automatically selects the optimal topology plugin. To manually change the topology plugin, update the `TopologyPlugin` value in `slurm.conf` on the controller node.

To disable topology-aware placement, set the plugin to `topology/flat` (or `topology/default`):

```
# Set this value to disable topology-aware placement
TopologyPlugin=topology/flat
```

### Dynamic topology updates
<a name="sagemaker-hyperpod-topology-dynamic-updates"></a>

Topology-aware scheduling continuously maintains topology correctness as your cluster changes. The topology is automatically recalculated and the topology configuration file is regenerated when any of the following events occur:
+ **Scale-up**: New nodes are added to the cluster.
+ **Scale-down**: Nodes are removed from the cluster.
+ **Node replacement**: Failed or unhealthy nodes are replaced, or nodes are manually replaced using the [BatchReplaceClusterNodes](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchReplaceClusterNodes.html) API.

When the topology is updated, new nodes are incorporated into the correct topology structure, removed nodes are pruned, and the Slurm configuration is updated without requiring manual intervention. This ensures that the topology always reflects the actual cluster state.

**Note**  
Advanced users can override the topology behavior by logging into the Slurm controller node and manually modifying `slurm.conf` and the applicable topology file (`topology.yaml` on Slurm 25.11 and later, or `topology.conf` on Slurm 24.x). However, manual changes may be overwritten by HyperPod during subsequent cluster updates, including scaling operations, node replacements, and other cluster lifecycle events. If you modify these files manually, verify your changes after any cluster update.

## Best practices for UltraServer topology
<a name="sagemaker-hyperpod-topology-best-practices"></a>

For optimal performance with UltraServer architecture in SageMaker HyperPod:
+ **Set appropriate block sizes**: Configure `BlockSizes=18` (or 17 if one node is spare) to match the UltraServer architecture.
+ **Use segments for better availability**: Use `--segment=16`, `--segment=8`, or `--segment=9` with `srun` and `sbatch` commands to improve job scheduling flexibility.
+ **Consider job size and segment size**:
  + If `BlockSizes=18`, jobs with up to 18 instances will always run on a single UltraServer.
  + If `BlockSizes=16`, jobs with fewer than 16 instances will always run on a single UltraServer, while jobs with 18 instances may run on one or two UltraServers.

When thinking about segmenting, consider the following:
+ With `--segment=1`, each instance can run on a separate UltraServer.
+ With `-N 18 --segment 9`, 9 nodes will be placed on one UltraServer, and another 9 nodes can be placed on the same or another UltraServer.
+ With `-N 24 --segment 8`, the job can run on 2 or 3 UltraServers, with every 8 nodes placed together on the same server.

## Limitations in SageMaker HyperPod topology aware scheduling
<a name="sagemaker-hyperpod-topology-limitations"></a>

With Slurm 25.11 and later, heterogeneous clusters (clusters with different instance types) are supported through partition-level topology and the `flat` cluster default. Each partition receives the topology best suited to its instance types, and non-topology and UltraServer nodes remain schedulable within the same cluster. For more information, see [Partition-level topology selection](#sagemaker-hyperpod-topology-partition-level).

On clusters running Slurm 24.x, a single cluster-wide topology applies, and the `topology/block` plugin has the following limitations with heterogeneous clusters:
+ Only nodes listed in blocks are schedulable by Slurm.
+ Every block must have at least `BlockSizes[0]` nodes.

For heterogeneous clusters on Slurm 24.x, consider these alternatives:
+ Do not use the block plugin with heterogeneous clusters. Instead, isolate UltraServer nodes in a different partition.
+ Create a separate cluster with UltraServers only in the same VPC and use Slurm's multicluster setup.