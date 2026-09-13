

# Troubleshoot invalid node registrations (INVALID\_REG) in AWS PCS
<a name="troubleshooting-invalid-registration"></a>

When a node registers with hardware that conflicts with its configuration, Slurm sets the node state to `INVALID_REG` and drains it. The node's `Reason` field in the `scontrol show node` output reports the cause. The most common causes are a configured CPU topology that doesn't match the hardware, and, with GPU autodetection active, a socket layout that doesn't fit the detected GPU affinity. For additional information on how AWS PCS configures topology on each Slurm version, see [Configuring hardware topology in AWS PCS](hardware-topology.md).

## CPU topology doesn't match the hardware
<a name="troubleshooting-invalid-registration-cpu"></a>

A configured socket layout that declares more resources than the node reports makes the node register with the following reason:

```
NodeName=my-cng-1-1 ... State=DOWN+CLOUD+DRAIN+INVALID_REG
   Reason=Low socket*core*thread count [slurm@2026-09-07T11:45:03]
```

The reason text is verbatim; the compared counts appear only in the `slurmctld` log at debug log level, as `Node my-cng-1-1 has low socket*core*thread count (48 < 96)`. This means the configured `Sockets` and `CoresPerSocket` combination exceeds the node's real core count. For example, a `Sockets` custom setting greater than the actual number of NUMA or L3 cache domains produces a total that the hardware can't satisfy.

## GPU affinity doesn't fit the socket boundaries
<a name="troubleshooting-invalid-registration-gpu"></a>

With GPU autodetection active, a socket layout that doesn't match the hardware makes the node register with the following reason:

```
Reason=gres/gpu GRES autodetected core affinity 0-23 on node my-cng-1-1 doesn't match socket
boundaries. (Socket 0 is cores 0-0). Consider setting Parameters=l3cache_as_socket ...
```

This means the GPU is attached to a range of cores that doesn't fit inside one configured socket. It typically appears when GPU autodetection is enabled without CPU topology, so the node falls back to the default one-core-per-socket layout.

## Resolution
<a name="troubleshooting-invalid-registration-resolve"></a>

Configure the CPU topology of the compute node group so the socket boundaries match the hardware:
+ On Slurm 25.11, set `Sockets` (and `Parameters`) in the custom Slurm settings of the compute node group.
+ On Slurm 26.05 and later, remove or correct a `Sockets` override that doesn't match the hardware, and let AWS PCS apply the automatic topology.

For more information, see [Topology behavior by Slurm version](hardware-topology.md#hardware-topology-versions).