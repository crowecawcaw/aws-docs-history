

# Nitro Sandboxes on instances with multiple NUMA nodes

Some instance types have more than one non-uniform memory access (NUMA) node. Each node has its own vCPUs and memory, and a vCPU reaches the memory of its own node faster than the memory of another node.

On an instance with more than one node, the parent instance keeps the memory pool, the CPU pool, and the Nitro Sandbox slots separately for each node. Each Nitro Sandbox runs on one node, unless you place it on more than one. On an instance with one node, these differences don't apply.

**Topics**
+ [Check the number of NUMA nodes](#nitro-sandboxes-numa-check)
+ [How Nitro Sandboxes use NUMA nodes](#nitro-sandboxes-numa-behavior)
+ [Reserve memory on each node](#nitro-sandboxes-numa-mempool)
+ [Choose the node of a Nitro Sandbox](#nitro-sandboxes-numa-placement)
+ [Check the capacity of each node](#nitro-sandboxes-numa-slots)
+ [Troubleshoot launches on instances with multiple nodes](#nitro-sandboxes-numa-troubleshoot)
+ [Run workloads on instances with multiple nodes](#nitro-sandboxes-numa-runtime)

## Check the number of NUMA nodes
<a name="nitro-sandboxes-numa-check"></a>

Run the following command on the parent instance.

```bash
lscpu | grep NUMA
```

The following is example output for an `m8a.48xlarge` instance, which has two nodes.

```
NUMA node(s):                         2
NUMA node0 CPU(s):                    0-95
NUMA node1 CPU(s):                    96-191
```

You can also list the nodes in `/sys/devices/system/node`. Check the instance type that you plan to use, because the number of nodes depends on the instance type and size.

## How Nitro Sandboxes use NUMA nodes
<a name="nitro-sandboxes-numa-behavior"></a>
+ By default, Firecracker places all vCPUs and all memory of a Nitro Sandbox on node 0.
+ The memory of a Nitro Sandbox comes only from the memory pool on its node. If that pool does not have enough free memory, the launch fails with an out-of-memory error, even when the pool on another node has free memory.
+ The vCPUs and the memory of a Nitro Sandbox are always on the same node. A launch that would place them on different nodes fails.
+ Without CPU overcommit, each vCPU takes a hardware thread of its node. Node 0 has one core fewer in the CPU pool than the other nodes, because the Nitro Enclaves driver keeps the first core of the parent instance for the parent.
+ With CPU overcommit, the vCPUs of a Nitro Sandbox run on the vCPUs that the parent instance has on the same node. A Nitro Sandbox can have at most as many vCPUs on a node as the parent instance has on that node. To give a Nitro Sandbox more vCPUs, place it on more than one node.
+ In confidential mode, the buffers of the virtual devices come from the pool of the lowest-numbered node of the Nitro Sandbox.
+ The guest sees one NUMA node, unless you place the Nitro Sandbox on more than one node.
+ A running Nitro Sandbox stays on its nodes. To move it, stop it and launch it again on another node.

## Reserve memory on each node
<a name="nitro-sandboxes-numa-mempool"></a>

The `nitro_enclaves.mempool` kernel parameter takes a comma-separated list of entries. Each entry reserves memory on one node or on every node. Use one of the following forms for each entry.

`{{size}}@{{node}}`  
Reserves {{size}} on node {{node}}, for example `8G@1`.

`{{percent}}%`  
Reserves {{percent}} percent of the memory that each node has available at boot, on every node.

`{{percent}}%-{{size}}`  
Reserves {{percent}} percent of each node, minus {{size}} on each node. Use this form to keep a fixed amount of memory for the parent instance on every node.

`{{percent}}%+{{size}}`  
Reserves {{percent}} percent of each node, plus {{size}} on each node.

To apply a percentage form to one node only, add `@{{node}}`, for example `50%@1`. An entry can subtract or add a size, but not both.

An entry with a size and no node does not control which node gets the memory. On an instance with more than one node, give every entry a node or use a percentage form. On Graviton-based instances, the pool can have at most three entries, and a percentage entry without a node counts once for each node.

The following examples are for an instance with two nodes.


| Parameter | Result | 
| --- | --- | 
| nitro\_enclaves.mempool=8G@0,8G@1 | 8 GiB on each node. | 
| nitro\_enclaves.mempool=16G@0 | 16 GiB on node 0 and no pool on node 1. You can't launch Nitro Sandboxes on node 1. | 
| nitro\_enclaves.mempool=50% | Half of the available memory of each node. | 
| nitro\_enclaves.mempool=90%-16G | 90 percent of each node, minus 16 GiB on each node. | 
| nitro\_enclaves.mempool=95%-1G@0,4G@1 | 95 percent of node 0 minus 1 GiB, and 4 GiB on node 1. | 

Size the pool of each node for the Nitro Sandboxes that you plan to run on that node and their overhead. Also add 128 MiB for each step of 8 slots that the node provides, as described in [Check the capacity of each node](#nitro-sandboxes-numa-slots). If a node can't provide the requested size, the parent instance reserves less on that node, and the reserved size in the kernel log is lower than the requested size.

To add the parameter, follow the steps in [Prepare the parent instance](nitro-sandboxes-run-firecracker.md#nitro-sandboxes-prepare-parent). After the reboot, check the pool of each node, in bytes.

```bash
sudo dmesg | grep "nitro_enclaves: CMA pool"
grep . /sys/class/misc/nitro_enclaves/mem_pool/node*/total
```

The following is example output for `nitro_enclaves.mempool=64G@0,64G@1`.

```
nitro_enclaves: CMA pool: 131072 MiB reserved in 16 region(s), 131072 MiB requested
/sys/class/misc/nitro_enclaves/mem_pool/node0/total:68719476736
/sys/class/misc/nitro_enclaves/mem_pool/node1/total:68719476736
```

## Choose the node of a Nitro Sandbox
<a name="nitro-sandboxes-numa-placement"></a>

To place a Nitro Sandbox on a node other than node 0, add `numa_nodes` to the `enclave` object of the configuration in [Launch a Nitro Sandbox](nitro-sandboxes-run-firecracker.md#nitro-sandboxes-launch). The following example places all vCPUs and all memory on node 1.

```json
"machine-config": {
"vcpu_count": {{2}},
"mem_size_mib": {{2048}}
},
"enclave": {
"cpu_overcommit": true,
"numa_nodes": [
    { "parent_numa": {{1}}, "vcpu_count": {{2}}, "mem_size_mib": {{2048}} }
]
}
```

To place one Nitro Sandbox on more than one node, add an entry for each node. The following example puts 2 vCPUs and 2 GiB on each of nodes 0 and 1.

```json
"machine-config": {
"vcpu_count": 4,
"mem_size_mib": 4096
},
"enclave": {
"cpu_overcommit": true,
"numa_nodes": [
    { "parent_numa": 0, "vcpu_count": 2, "mem_size_mib": 2048 },
    { "parent_numa": 1, "vcpu_count": 2, "mem_size_mib": 2048 }
]
}
```

The entries must follow these rules:
+ The `vcpu_count` and `mem_size_mib` values of all entries add up to the values in `machine-config`.
+ Each entry names a different node and has at least one vCPU and some memory.
+ The entries appear in ascending order of node number.
+ The memory of every entry except the one with the highest node number is a multiple of 128 MiB.

A Nitro Sandbox with more than one entry sees one NUMA node for each entry. Its guest node 0 is the entry with the lowest node number, and the other guest nodes follow in order. The measured image records that the Nitro Sandbox spans more than one node, so its PCR0 differs from the same Nitro Sandbox on one node, as described in [Nitro Sandbox measurements](nitro-sandboxes-attestation.md#nitro-sandboxes-attestation-pcrs). If you build the image in advance, build it with the same settings that you launch with.

If you also set `cpu_ids`, choose CPUs on the node that holds the memory of the Nitro Sandbox. Otherwise, the launch fails.

## Check the capacity of each node
<a name="nitro-sandboxes-numa-slots"></a>

The parent instance reports the free capacity of each node in the `/sys/class/misc/nitro_enclaves` directory. The `mem_pool/node{{N}}` directories hold `total`, `in_use`, and `free` in bytes. The `cpu_pool/node{{N}}` directories hold the same files as vCPU counts, and count only Nitro Sandboxes without CPU overcommit.

```bash
grep . /sys/class/misc/nitro_enclaves/mem_pool/node*/free /sys/class/misc/nitro_enclaves/cpu_pool/node*/free
```

The parent instance also counts slots per node. Each node can run 4 Nitro Sandboxes, plus 8 for each step of 8 slots whose memory came from that node. When you raise `pcie_slots`, the parent instance takes the memory for each step from the nodes one after another. For example, with `pcie_slots` set to 20 on an instance with two nodes, each node can run up to 12 Nitro Sandboxes, and the instance up to 20 in total.

A launch on a node that has no slot left fails, even when `pcie_slots_in_use` is lower than `pcie_slots`. To run more Nitro Sandboxes on one node, raise `pcie_slots` further, or spread the Nitro Sandboxes across nodes.

## Troubleshoot launches on instances with multiple nodes
<a name="nitro-sandboxes-numa-troubleshoot"></a>

The launch fails with an out-of-memory error, and Firecracker reports `CMA allocation failed`  
The pool on the node of the Nitro Sandbox is full or empty. Check `mem_pool/node{{N}}/free`. Launch the Nitro Sandbox on a node with free memory, or reserve more memory on that node and reboot.

Firecracker reports `Failed to add a vCPU on parent NUMA node {{N}}`  
Without CPU overcommit, node {{N}} has no free core left. Check `cpu_pool/node{{N}}/free`. With CPU overcommit, the Nitro Sandbox asks for more vCPUs on node {{N}} than the parent instance has there. If the error is `Invalid argument`, the parent instance has no node {{N}}.

The launch fails while `pcie_slots_in_use` is lower than `pcie_slots`  
The node has no slot left. Raise `pcie_slots`, or launch on another node.

Launches without CPU overcommit fail after you configured Nitro Enclaves  
A fixed CPU pool for Nitro Enclaves, for example from the Nitro Enclaves allocator service, can hold cores of one node only. Nitro Sandboxes without CPU overcommit take their cores from that pool. Add cores of the node that you launch on to the pool, or use CPU overcommit.

## Run workloads on instances with multiple nodes
<a name="nitro-sandboxes-numa-runtime"></a>
+ Spread Nitro Sandboxes across nodes so that no single node runs out of pool memory, cores, or slots first. Before each launch, pick a node with enough free capacity.
+ Keep each Nitro Sandbox on one node when it fits. Its vCPUs then reach all of its memory on the same node. Place a Nitro Sandbox on more than one node when it needs more vCPUs or memory than one node has, and run a guest kernel and applications that use the NUMA topology.
+ With CPU overcommit, the Nitro Sandboxes on a node share the vCPUs of that node with the processes of the parent instance on the same node. Account for both when you decide how many Nitro Sandboxes a node runs.