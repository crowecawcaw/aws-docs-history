

# Configuring custom GRES settings in AWS PCS
<a name="gres-custom-settings"></a>

Slurm uses `gres.conf` to manage Generic Resources (GRES), such as GPUs, Multi-Process Service (MPS), and Multi-Instance GPU (MIG) devices, on compute nodes. AWS PCS lets you customize `gres.conf` through the `gresCustomSettings` property of `slurmConfiguration` during compute node group creation or update.

Unlike other custom settings, which are a flat list of parameter and value pairs, `gresCustomSettings` is a list of *records*. Each record is a set of `gres.conf` attributes that describes one GRES device or resource. For example, the record `Name=gpu Type=a100 File=/dev/nvidia[0-7]` declares eight A100 GPUs.

In Slurm, a `gres.conf` record applies to every node in the cluster unless it specifies a `NodeName=` prefix. AWS PCS always adds the `NodeName=` prefix for the compute node group, so you don't specify it, and every record you supply applies only to that compute node group. AWS PCS doesn't support cluster-wide `gres.conf` records.

## Configuring gres.conf settings
<a name="gres-custom-settings-configure"></a>

`gres.conf` custom settings can be configured through the AWS Console, CLI, or SDKs during compute node group creation or modified later through update operations.

------
#### [ AWS Management Console ]

Navigate to **Additional scheduler settings** in the create or edit page for a compute node group resource. Enter one `gres.conf` record per line, in native `gres.conf` form (for example, `Name=gpu Type=a100 File=/dev/nvidia[0-7]`).

------
#### [ AWS CLI ]

For programmatic management of `gres.conf` settings, use the `gresCustomSettings` field in create or update compute node group operations. Each element of the list is one `gres.conf` record.

**Example – Declaring GPU devices on a compute node group**  

```
aws pcs update-compute-node-group \
    --cluster-identifier {{my-cluster}} \
    --compute-node-group-identifier {{my-cng-1}} \
    --slurm-configuration \
    'gresCustomSettings=[{Name=gpu,Type=a100,File=/dev/nvidia[0-7]}]'
```

------

## Supported gres.conf settings for compute node groups
<a name="gres-custom-settings-cng"></a>

The following `gres.conf` attributes are supported in each record at the compute node group level:
+ [AutoDetect](https://slurm.schedmd.com/gres.conf.html#OPT_AutoDetect)
**Note**  
AWS PCS supports `AutoDetect` on Slurm version 25.11 and later.
+ [Name](https://slurm.schedmd.com/gres.conf.html#OPT_Name)
+ [Type](https://slurm.schedmd.com/gres.conf.html#OPT_Type)
+ [Count](https://slurm.schedmd.com/gres.conf.html#OPT_Count)
+ [Cores](https://slurm.schedmd.com/gres.conf.html#OPT_Cores)
+ [Links](https://slurm.schedmd.com/gres.conf.html#OPT_Links)
+ [Flags](https://slurm.schedmd.com/gres.conf.html#OPT_Flags)
+ [File](https://slurm.schedmd.com/gres.conf.html#OPT_File)
+ [MultipleFiles](https://slurm.schedmd.com/gres.conf.html#OPT_MultipleFiles)

For the meaning and accepted values of each attribute, see the Slurm [gres.conf](https://slurm.schedmd.com/gres.conf.html) documentation. AWS PCS validates your records against the same rules that Slurm applies. In particular, each record must declare either a `Name` or an active `AutoDetect` value, and a GPU record (`Name=gpu`) must specify `File` or `MultipleFiles` unless an active `AutoDetect` value discovers the devices.

An *active* `AutoDetect` value is any value that turns detection on, such as `nvml` or `full`. `AutoDetect=off` turns detection off, so it is not an active value and can't stand alone in a record.

## How AWS PCS applies your gres.conf records
<a name="gres-custom-settings-merge"></a>

A GRES configuration appears in two places in the Slurm configuration, and AWS PCS writes both of them:
+ The `gres.conf` records that you supply in `gresCustomSettings` describe the devices that exist on the node.
+ The `Gres` setting in `slurm.conf` declares what the scheduler can allocate, in the form `name[:type]:count`. You supply it as a custom Slurm setting for the compute node group, in `slurmCustomSettings`. For more information, see [Custom Slurm settings for AWS PCS compute node groups](slurm-custom-settings-cng.md).

AWS PCS renders your records into `gres.conf` and reconciles them with the GRES configuration it manages:
+ If you declare a GPU record, it replaces the default GPU record that AWS PCS generates for the compute node group. A GPU record is a record that specifies `Name=gpu` or an `AutoDetect` attribute. You can declare at most one GPU record for a compute node group.
+ Records for other resources, such as `mps`, `shard`, or a resource name of your own, are added alongside the AWS PCS defaults.
+ AWS PCS derives the `GresTypes` setting and the `gres/*` entries of the `AccountingStorageTRES` setting in `slurm.conf` from the `Gres` setting.

On Slurm version 26.05 and later, AWS PCS sets `AutoDetect=full` by default on GPU compute node groups when the node's socket layout is known, either because you set `Sockets` in `slurmCustomSettings` for the compute node group, or because AWS PCS detected the CPU topology automatically. When the socket layout is not available, AWS PCS emits its GPU record without `AutoDetect` instead.

### Constraints between gres.conf and the Gres setting
<a name="gres-custom-settings-constraints"></a>

Slurm needs both sides of the GRES configuration to schedule a resource, and a resource that appears in only one of them doesn't work. An entry in the `Gres` setting in `slurm.conf` with no `gres.conf` record behind it makes the node report fewer resources than are configured, and the node drains. A record with no `Gres` entry leaves the device present on the node but not schedulable.

AWS PCS validates the two against each other when you create or update a compute node group, and rejects the request in the following cases:
+ A `slurm.conf` `Gres` entry names a resource that no `gres.conf` record declares. This includes `gpu`: a `gpu` entry requires a GPU record in `gresCustomSettings`, even when the count is `0`.
+ A `slurm.conf` `Gres` entry declares a higher count of a resource than the `gres.conf` records declare. A lower count is allowed, down to `0`: the `gres.conf` records describe the devices that are present on the node, while `Gres` declares how many of them the scheduler can allocate.
+ A `slurm.conf` `Gres` entry specifies a GPU type that differs from the `Type` of the GPU record in `gres.conf`.

The last two checks depend on what your records declare. AWS PCS can't count devices that Slurm discovers when the node boots, so a record that only enables `AutoDetect` accepts any `gpu` count and type in the `Gres` entry. This is how MIG profiles pass validation. AWS PCS also skips the count check for shared GRES (`mps` and `shard`), and skips the type check when the GPU record declares no `Type`.

AWS PCS accepts a record that has no matching `Gres` entry. The resource exists on the node, but jobs can't request it. Add the `Gres` entry to make it schedulable.

**Important**  
AWS PCS validates the syntax of your records and their consistency with the `Gres` setting. It doesn't validate them against the hardware. A record whose `File`, `Cores`, or `Links` layout doesn't match the devices on the booted node makes the node drain. The same applies to MIG: the profiles that you declare in `Gres` must match the profiles configured on the node. For more information about diagnosing a drained node, see [Troubleshoot invalid node registrations (INVALID\_REG) in AWS PCS](troubleshooting-invalid-registration.md).