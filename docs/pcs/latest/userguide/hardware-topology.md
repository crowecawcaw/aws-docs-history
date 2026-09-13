

# Configuring hardware topology in AWS PCS
<a name="hardware-topology"></a>

Slurm makes better placement decisions when it knows the internal hardware layout of a compute node: how cores group into sockets and Non-Uniform Memory Access (NUMA) domains, how L3 caches map to cores, and which cores each GPU is attached to. This topic describes how Slurm models that layout, and how AWS PCS configures it on each supported Slurm version.

## CPU topology
<a name="hardware-topology-cpu"></a>

The cores of a compute node are not interchangeable. They are grouped into physical packages (sockets) and NUMA domains, and each group shares resources such as memory controllers and L3 cache. Two tasks placed in the same group communicate faster and share cache; tasks placed across groups compete less for those shared resources.

Slurm describes this grouping per node with the `Sockets`, `CoresPerSocket`, and `ThreadsPerCore` settings in `slurm.conf`. What Slurm treats as a *socket* is configurable with the per-node [Parameters](https://slurm.schedmd.com/slurm.conf.html#OPT_Parameters) setting:
+ `numa_node_as_socket` – each NUMA domain is a socket.
+ `l3cache_as_socket` – each L3 cache domain is a socket. This can be useful on certain processors where the socket level is too coarse, and the L3 cache may provide better task distribution.

With CPU topology configured, socket-aware scheduling options work as intended: job options such as `--ntasks-per-socket` and `--sockets-per-node`, and socket-based allocation with the `CR_Socket` or `CR_Socket_Memory` values of the cluster-level `SelectTypeParameters` setting. For more information about how Slurm allocates sockets, cores, and threads, see [Support for Multi-core/Multi-thread Architectures](https://slurm.schedmd.com/mc_support.html) in the Slurm documentation.

AWS PCS doesn't configure CPU topology on Slurm versions before 25.11, so nodes on those versions advertise one core per socket and these options have no effect.

## GPU affinity
<a name="hardware-topology-gpu"></a>

Each GPU in a node is closest to one NUMA domain, so a subset of the node's cores is local to it. A task that runs on cores local to its GPU transfers data over a shorter path than a task on the other socket. Slurm records this GPU-to-core affinity per device (the `Cores` attribute of a `gres.conf` record), along with the GPU-to-GPU interconnect layout (`Links`).

On AWS PCS compute nodes this information can't be configured statically ahead of time, because device enumeration depends on the individual instance and the devices only become visible when the node boots. Slurm's [AutoDetect](https://slurm.schedmd.com/gres.conf.html#OPT_AutoDetect) mechanism solves this: when a node boots, `slurmd` queries the NVIDIA Management Library (NVML) and reports the detected affinity to the controller at registration.

**Note**  
While a node is powered down, Slurm doesn't know its GPU-to-CPU affinity. The affinity only becomes available when the node boots and registers, so scheduling decisions for powered-down nodes are made without it.

Autodetected GPU affinity is expressed in terms of sockets, so it requires correct CPU topology. If a node registers GPU affinity that doesn't fit the node's configured socket boundaries, Slurm sets the node to `INVALID_REG` and drains it. For more information, see [Troubleshoot invalid node registrations (INVALID\_REG) in AWS PCS](troubleshooting-invalid-registration.md).

With GPU affinity available, Slurm can place tasks on cores local to their allocated GPUs. Generic Resource (GRES) affinity is handled at socket granularity. Placement depends on the job options; combinations that use the detected affinity include `--ntasks-per-socket` with `--gpus-per-task`, and `--gpus` with `--ntasks-per-gpu`.

## Topology behavior by Slurm version
<a name="hardware-topology-versions"></a>

What AWS PCS configures for you, and what you can configure yourself, depends on the Slurm version of the cluster.

### From Slurm 25.11
<a name="hardware-topology-versions-2511"></a>

#### CPU topology through custom settings
<a name="hardware-topology-versions-manual-cpu"></a>

You can configure CPU topology yourself with the `Sockets` and `Parameters` custom Slurm settings for a compute node group. For more information, see [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md).
+ Set `Sockets` to the number of domains you want Slurm to treat as sockets. AWS PCS computes and sets the matching `CoresPerSocket` for you. The value must divide the node's core count evenly.
+ Set `Parameters` to `numa_node_as_socket` or `l3cache_as_socket` to declare what the domains are.

With `l3cache_as_socket`, `Sockets` is required: AWS PCS can't determine the L3 cache layout of an instance type, so you supply the number of L3 cache domains. This applies on every Slurm version, including 26.05 and later.

**Example – L3 cache domains as sockets on an hpc7a.96xlarge compute node group (24 L3 cache domains, 8 cores each)**  

```
aws pcs update-compute-node-group \
      --cluster-identifier {{my-cluster}} \
      --compute-node-group-identifier {{my-cng-1}} \
      --slurm-configuration \
      'slurmCustomSettings=[{parameterName=Sockets,parameterValue=24},{parameterName=Parameters,parameterValue=l3cache_as_socket}]'
```

**Note**  
AWS PCS validates the structure of a `Sockets` value, not its correctness against the hardware. A value that doesn't match the node's real layout leads to suboptimal placement, or to `INVALID_REG` when GPU autodetection is active.

#### GPU topology with AutoDetect (opt-in)
<a name="hardware-topology-versions-2511-gpu"></a>

On Slurm 25.11, GPU autodetection is off by default. You opt in by adding `AutoDetect` to the GPU record of the compute node group in `gresCustomSettings`. For more information, see [Configuring custom GRES settings in AWS PCS](gres-custom-settings.md).

AutoDetect requires the node's CPU topology to be configured. On 25.11, that means setting `Sockets` for the compute node group as described in the previous section. Without it, nodes register GPU affinity that doesn't fit the default one-core-per-socket layout, and Slurm sets them to `INVALID_REG`.

### From Slurm 26.05
<a name="hardware-topology-versions-2605"></a>

#### Default CPU topology
<a name="hardware-topology-versions-2605-cpu"></a>

From Slurm 26.05, AWS PCS configures NUMA-based CPU topology by default. AWS PCS determines the number of NUMA domains from the instance type of the compute node group, and sets `Sockets`, `CoresPerSocket`, and `Parameters=numa_node_as_socket` on each node.

The following rules apply:
+ If a compute node group uses multiple instance types, AWS PCS applies the default topology only when all of them have the same number of NUMA domains. Otherwise, AWS PCS leaves the topology unset, matching the behavior of earlier versions.
+ If you set `Sockets` in the custom Slurm settings of the compute node group, your value takes precedence and AWS PCS doesn't add `Parameters`. Use this to override the default, for example to use L3 cache domains as sockets with `Parameters=l3cache_as_socket`, which still requires your `Sockets` value.

**Note**  
The automatic topology applies to clusters created with Slurm 26.05 or later, and to clusters when you update them to 26.05 or later.

#### GPU autodetection by default
<a name="hardware-topology-versions-2605-gpu"></a>

From Slurm 26.05, AWS PCS enables GPU autodetection by default. AWS PCS adds `AutoDetect=full` to the GPU record it generates for a GPU compute node group when the node's socket layout is known, either because AWS PCS configured the CPU topology automatically, or because you set `Sockets` yourself. When the socket layout is not available, AWS PCS emits its GPU record without `AutoDetect`, matching the behavior of earlier versions. For more information about the GPU record that AWS PCS generates and how it reconciles that record with your own, see [How AWS PCS applies your gres.conf records](gres-custom-settings.md#gres-custom-settings-merge).