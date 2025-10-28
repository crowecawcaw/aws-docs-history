# `HeadNode` section

**(Required)** Specifies the configuration for the head node.

```
HeadNode:
  InstanceType: `string`
  Networking:
    SubnetId: `string`
    ElasticIp: `string/boolean`
    SecurityGroups:
      - `string`
    AdditionalSecurityGroups:
      - `string`
    Proxy:
      HttpProxyAddress: `string`
  DisableSimultaneousMultithreading: `boolean`
  Ssh:
    KeyName: `string`
    AllowedIps: `string`
  LocalStorage:
    RootVolume:
      Size: `integer`
      Encrypted: `boolean`
      VolumeType: `string`
      Iops: `integer`
      Throughput: `integer`
      DeleteOnTermination: `boolean`
    EphemeralVolume:
      MountDir: `string`
  SharedStorageType: `string`
  Dcv:
    Enabled: `boolean`
    Port: `integer`
    AllowedIps: `string`
  CustomActions:
    OnNodeStart:
      Sequence:
        - Script: `string`
          Args:
            - `string`
      Script: `string`
      Args:
        - `string`
    OnNodeConfigured:
      Sequence:
        - Script: `string`
          Args:
            - `string`
      Script: `string`
      Args:
        - `string`
    OnNodeUpdated:
      Sequence:
        - Script: `string`
          Args:
            - `string`
      Script: `string`
      Args:
        - `string`
  Iam:
    InstanceRole: `string`
    InstanceProfile: `string`
    S3Access:
      - BucketName: `string`
        EnableWriteAccess: `boolean`
        KeyName: `string`
    AdditionalIamPolicies:
      - Policy: `string`
  Imds:
    Secured: `boolean`
  Image:
    CustomAmi: `string`
```

## `HeadNode` properties

`InstanceType` (**Required**, `String`)

Specifies the instance type for the head node.

Specifies the Amazon EC2 instance type that's used for the head node. The architecture of
the instance type must be the same as the architecture used for the AWS Batch
[InstanceType](Scheduling-v3.md#yaml-Scheduling-AwsBatchQueues-ComputeResources-InstanceTypes "Scheduling-v3.md#yaml-Scheduling-AwsBatchQueues-ComputeResources-InstanceTypes") or Slurm
[InstanceType](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-InstanceType "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-InstanceType")
setting.

###### Note

AWS ParallelCluster doesn't support the following instance types for the
`HeadNode` setting.

- hpc6id

If you define a p4d instance type or another instance type that has multiple
network interfaces or a network interface card, you must set
[ElasticIp](#yaml-HeadNode-Networking-ElasticIp "#yaml-HeadNode-Networking-ElasticIp")
to `true` to provide public access. AWS public IPs can only be assigned
to instances launched with a single network interface. For this case, we recommend
that you use a [NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") to provide public access to the cluster compute nodes. For more
information, see [Assign
a public IPv4 address during instance launch](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#public-ip-addresses "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#public-ip-addresses") in the _Amazon EC2 User
Guide for Linux Instances_.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`DisableSimultaneousMultithreading`
(**Optional**, `Boolean`)

If `true`, disables hyper-threading on the head node. The default value
is `false`.

Not all instance types can disable hyper-threading. For a list of instance types
that support disabling hyperthreading, see [CPU cores and threads for each CPU core per instance type](../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md#cpu-options-supported-instances-values "../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md#cpu-options-supported-instances-values") in the
_Amazon EC2 User Guide_.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`SharedStorageType`
(**Optional**, `String`)

Specifies the type of storage used for internally shared data. Internally shared
data includes data that AWS ParallelCluster uses to manage the cluster and the default
shared `/home` if not specified in the [SharedStorage section](SharedStorage-v3.md "SharedStorage-v3.md") as a Mount directory to mount a shared filesystem
volume. For more details on internal shared data refer [AWS ParallelCluster internal directories](directories-v3.md "directories-v3.md").

If `Ebs`, which is the default storage type, the head node will export
portions of its root volume as shared directories for compute nodes and login nodes
using NFS.

If `Efs`, ParallelCluster will create an EFS filesystem to use for
shared internal data and `/home`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

###### Note

When the cluster scales out, the EBS storage type may present performance
bottlenecks as the head node shares data from the root volume with the compute
nodes using NFS exports. Using EFS, you can avoid NFS exports as your cluster scales
out and avoid performance bottlenecks associated with them. It is recommended to
choose EBS for max read/write potential for small files and installation process.
Choose EFS for scale.

## `Networking`

**(Required)** Defines the networking configuration for the
head node.

```
Networking:
  SubnetId: `string`
  ElasticIp: `string/boolean`
  SecurityGroups:
    - `string`
  AdditionalSecurityGroups:
    - `string`
  Proxy:
    HttpProxyAddress: `string`
```

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

### `Networking` properties

`SubnetId` (**Required**, `String`)

Specifies the ID of an existing subnet in which to provision the head node.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`ElasticIp` (**Optional**, `String`)

Creates or assigns an Elastic IP address to the head node. Supported values are
`true`, `false`, or the ID of an existing Elastic IP address.
The default is `false`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`SecurityGroups`
(**Optional**, `[String]`)

List of Amazon VPC security group ids to use for the head node. These replace the security
groups that AWS ParallelCluster creates if this property is not included.

Verify that the security groups are configured correctly for your [SharedStorage](SharedStorage-v3.md "SharedStorage-v3.md") systems.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`AdditionalSecurityGroups`
(**Optional**, `[String]`)

List of additional Amazon VPC security group ids to use for the head node.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`Proxy` (**Optional**)

Specifies the proxy settings for the head node.

```
Proxy:
                            HttpProxyAddress:
                            `string`
```

`HttpProxyAddress` (**Optional**,
`String`)

Defines an HTTP or HTTPS proxy server, typically
`https://`x.x.x.x:8080``.

There is no default value.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

## `Ssh`

**(Optional)** Defines the configuration for SSH access to the
head node.

```
Ssh:
      KeyName: `string`
      AllowedIps: `string`
```

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

### `Ssh` properties

`KeyName` (**Optional**, `String`)

Names an existing Amazon EC2 key pair to enable SSH access to the head node.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`AllowedIps` (**Optional**, `String`)

Specifies the CIDR-formatted IP range or a prefix list id for SSH connections to
the head node. The default is `0.0.0.0/0`.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

## `LocalStorage`

**(Optional)** Defines the local storage configuration for the head node.

```
LocalStorage:
  RootVolume:
    Size: `integer`
    Encrypted: `boolean`
    VolumeType: `string`
    Iops: `integer`
    Throughput: `integer`
    DeleteOnTermination: `boolean`
  EphemeralVolume:
    MountDir: `string`
```

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

### `LocalStorage` properties

`RootVolume`
(**Required**)

Specifies the root volume storage for the head node.

```
RootVolume:
  Size: `integer`
  Encrypted: `boolean`
  VolumeType: `string`
  Iops: `integer`
  Throughput: `integer`
  DeleteOnTermination: `boolean`
```

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`Size`
(**Optional**, `Integer`)

Specifies the head node root volume size in gibibytes (GiB). The
default size comes from the AMI. Using a different size requires that
the AMI supports `growroot`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`Encrypted`
(**Optional**, `Boolean`)

Specifies if the root volume is encrypted. The default value is `true`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`VolumeType` (**Optional**, `String`)

Specifies the [Amazon EBS volume type](../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md "../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md"). Supported values are `gp2`, `gp3`,
`io1`, `io2`, `sc1`, `st1`,
and `standard`. The default value is `gp3`.

For more information, see [Amazon EBS volume types](../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md "../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md")
in the _Amazon EC2 User Guide_.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`Iops`
(**Optional**, `Integer`)

Defines the number of IOPS for `io1`, `io2`,
and `gp3` type volumes.

The default value, supported values, and `volume_iops`
to `volume_size` ratio varies by `VolumeType`
and `Size`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`VolumeType` = `io1`

Default `Iops` = 100

Supported values `Iops` = 100–64000 †

Maximum `Iops` to `Size` ratio = 50
IOPS per GiB. 5000 IOPS requires a `Size` of at
least 100 GiB.

`VolumeType` = `io2`

Default `Iops` = 100

Supported values `Iops` = 100–64000
(256000 for `io2` Block Express volumes) †

Maximum `Iops` to `Size` ratio = 500
IOPS per GiB. 5000 IOPS requires a `Size` of at
least 10 GiB.

`VolumeType` = `gp3`

Default `Iops` = 3000

Supported values `Iops` = 3000–16000

Maximum `Iops` to `Size` ratio = 500
IOPS per GiB. 5000 IOPS requires a `Size` of at
least 10 GiB.

† Maximum IOPS is guaranteed only on [Instances built on the Nitro System](../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances "../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances") provisioned with more than
32,000 IOPS. Other instances guarantee up to 32,000 IOPS. Older
`io1` volumes might not reach full performance unless you
[modify the volume](../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md "../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md"). `io2` Block Express volumes support
`Iops` values up to 256000 on `R5b` instance types.
For more information, see [`io2` Block Express volumes](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md#io2-block-express "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md#io2-block-express") in the _Amazon EC2 User Guide_.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`Throughput`
(**Optional**, `Integer`)

Defines the throughput for `gp3` volume types, in MiB/s.
This setting is valid only when `VolumeType` is `gp3`.
The default value is `125`. Supported values: 125–1000 MiB/s

The ratio of `Throughput` to `Iops` can be no
more than 0.25. The maximum throughput of 1000 MiB/s requires that the
`Iops` setting is at least 4000.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`DeleteOnTermination` (**Optional**,
`Boolean`)

Specifies whether the root volume should be deleted when the head node
is terminated. The default value is `true`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`EphemeralVolume`
(**Optional**)

Specifies details for any instance store volume. For more information, see
[Instance store volumes](../../../AWSEC2/latest/UserGuide/InstanceStorage.md#instance-store-volumes "../../../AWSEC2/latest/UserGuide/InstanceStorage.md#instance-store-volumes") in the _Amazon EC2 User Guide_.

```
EphemeralVolume:
  MountDir: `string`
```

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`MountDir` (**Optional**,
`String`)

Specifies the mount directory for the instance store volume. The
default is `/scratch`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

## `Dcv`

**(Optional)** Defines configuration settings for the Amazon DCV server
that runs on the head node.

For more information, see [Connect to the head and login nodes through Amazon DCV](dcv-v3.md "dcv-v3.md").

```
Dcv:
  Enabled: `boolean`
  Port: `integer`
  AllowedIps: `string`
```

###### Important

By default, the Amazon DCV port setup by AWS ParallelCluster is open to all IPv4 addresses. However,
you can connect to a Amazon DCV port only if you have the URL for the Amazon DCV session and connect to
the Amazon DCV session within 30 seconds of when the URL is returned from `pcluster dcv-connect`.
Use the `AllowedIps` setting to further restrict access to the Amazon DCV port with a
CIDR-formatted IP range, and use the `Port` setting to set a nonstandard port.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

### `Dcv` properties

`Enabled` (**Required**, `Boolean`)

Specifies whether Amazon DCV is enabled on the head node. The default value is
`false`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

###### Note

Amazon DCV automatically generates a self-signed certificate that's used to secure
traffic between the Amazon DCV client and the Amazon DCV server that runs on the head node. To
configure your own certificate, see [Amazon DCV HTTPS certificate](dcv-v3.md#dcv-v3-certificate "dcv-v3.md#dcv-v3-certificate").

`Port` (**Optional**, `Integer`)

Specifies the port for Amazon DCV. The default value is `8443`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`AllowedIps`
(**Optional, Recommended**, `String`)

Specifies the CIDR-formatted IP range for connections to Amazon DCV. This setting
is used only when AWS ParallelCluster creates the security group. The default value is
`0.0.0.0/0`, which allows access from any internet address.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

## `CustomActions`

**(Optional)** Specifies custom scripts to run on the head node.

```
CustomActions:
  OnNodeStart:
    Sequence:
      - Script: `string`
        Args:
          - `string`
    Script: `string`
    Args:
      - `string`
  OnNodeConfigured:
    Sequence:
      - Script: `string`
        Args:
          - `string`
    Script: `string`
    Args:
      - `string`
  OnNodeUpdated:
    Sequence:
      - Script: `string`
        Args:
          - `string`
    Script: `string`
    Args:
      - `string`
```

### `CustomActions` properties

`OnNodeStart`
(**Optional**)

Specifies single script or a sequence of scripts to run on the head node before any
node deployment bootstrap action is started. For more information, see [Custom bootstrap actions](custom-bootstrap-actions-v3.md "custom-bootstrap-actions-v3.md").

`Sequence` (**Optional**)

List of scripts to run. AWS ParallelCluster runs the scripts in the
same order as they are listed in the configuration file, starting with
the first.

`Script` (**Required**,
`String`)

Specifies the file to use. The file path can start with
`https://` or `s3://`.

`Args` (**Optional**,
`[String]`)

List of arguments to pass to the script.

`Script` (**Required**,
`String`)

Specifies the file to use for a single script. The file path can start
with `https://` or `s3://`.

`Args`
(**Optional**, `[String]`)

List of arguments to pass to the single script.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`OnNodeConfigured`
(**Optional**)

Specifies a single script or a sequence of scripts to run on the head node after
the node bootstrap actions are complete. For more information, see [Custom bootstrap actions](custom-bootstrap-actions-v3.md "custom-bootstrap-actions-v3.md").

`Sequence` (**Optional**)

Specifies the list of scripts to run.

`Script` (**Required**,
`String`)

Specifies the file to use. The file path can start with
`https://` or `s3://`.

`Args` (**Optional**,
`[String]`)

List of arguments to pass to the script.

`Script` (**Required**,
`String`)

Specifies the file to use for a single script. The file path can start with `https://` or `s3://`.

`Args` (**Optional**,
`[String]`)

List of arguments to pass to the single script.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`OnNodeUpdated`
(**Optional**)

Specifies a single script or a sequence of scripts to run on the head node after
node update actions are complete. For more information, see [Custom bootstrap actions](custom-bootstrap-actions-v3.md "custom-bootstrap-actions-v3.md").

`Sequence` (**Optional**)

Specifies the list of scripts to run.

`Script` (**Required**,
`String`)

Specifies the file to use. The file path can start with
`https://` or `s3://`.

`Args` (**Optional**,
`[String]`)

List of arguments to pass to the script.

`Script` (**Required**,
`String`)

Specifies the file to use for the single script. The file path
can start with `https://` or `s3://`.

`Args` (**Optional**,
`[String]`)

List of arguments to pass to the single script.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

###### Note

`OnNodeUpdated` is added starting with AWS ParallelCluster 3.4.0.

`Sequence` is added starting with AWS ParallelCluster version 3.6.0.
When you specify `Sequence`, you can list multiple scripts for a
custom action. AWS ParallelCluster continues to support configuring a custom action
with a single script, without including `Sequence`.

AWS ParallelCluster doesn't support including both a single script and
`Sequence` for the same custom action.

## `Iam`

**(Optional)** Specifies either an instance role or an instance
profile to use on the head node to override the default instance role or instance profile for
the cluster.

```
Iam:
  InstanceRole: `string`
  InstanceProfile: `string`
  S3Access:
    - BucketName: `string`
      EnableWriteAccess: `boolean`
      KeyName: `string`
  AdditionalIamPolicies:
    - Policy: `string`
```

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

### `Iam` properties

`InstanceProfile`
(**Optional**, `String`)

Specifies an instance profile to override the default head node instance profile.
You can't specify both `InstanceProfile` and `InstanceRole`.
The format is
`arn:`Partition`:iam::`Account`:instance-profile/`InstanceProfileName``.

If this is specified, the `S3Access` and `AdditionalIamPolicies`
settings can't be specified.

We recommend that you specify one or both of the `S3Access`
and `AdditionalIamPolicies` settings because features added to
AWS ParallelCluster often require new permissions.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

`InstanceRole`
(**Optional**, `String`)

Specifies an instance role to override the default head node instance role.
You can't specify both `InstanceProfile` and `InstanceRole`.
The format is
`arn:`Partition`:iam::`Account`:role/`RoleName``.

If this is specified, the `S3Access` and `AdditionalIamPolicies`
settings can't be specified.

We recommend that you specify one or both of the `S3Access`
and `AdditionalIamPolicies` settings because features added to AWS ParallelCluster
often require new permissions.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

### `S3Access`

`S3Access` (**Optional**)

Specifies a bucket. This is used to generate policies to grant the specified
access to the bucket.

If this is specified, the `InstanceProfile` and `InstanceRole`
settings can't be specified.

We recommend that you specify one or both of the `S3Access`
and `AdditionalIamPolicies` settings because features added to
AWS ParallelCluster often require new permissions.

```
S3Access:
  - BucketName: `string`
    EnableWriteAccess: `boolean`
    KeyName: `string`
```

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`BucketName`
(**Required**, `String`)

The name of the bucket.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`KeyName`
(**Optional**, `String`)

The key for the bucket. The default value is "`*`".

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`EnableWriteAccess` (**Optional**,
`Boolean`)

Indicates whether write access is enabled for the bucket. The
default value is `false`.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

### `AdditionalIamPolicies`

`AdditionalIamPolicies`
(**Optional**)

Specifies a list of Amazon Resource Names (ARNs) of IAM policies for Amazon EC2.
This list is attached to the root role used for the head node in addition to
the permissions required by AWS ParallelCluster.

An IAM policy name and its ARN are different. Names can't be used.

If this is specified, the `InstanceProfile` and `InstanceRole`
settings can't be specified.

We recommend that you use `AdditionalIamPolicies` because
`AdditionalIamPolicies` are added to the permissions that AWS ParallelCluster
requires, and the `InstanceRole` must include all permissions required.
The permissions required often change from release to release as features are
added.

There is no default value.

```
AdditionalIamPolicies:
  - Policy: `string`
```

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

`Policy` (**Optional**,
`[String]`)

List of IAM policies.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

## `Imds`

**(Optional)** Specifies the properties for instance metadata
service (IMDS). For more information, see [How instance metadata service version 2 works](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md#instance-metadata-v2-how-it-works "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md#instance-metadata-v2-how-it-works") in the _Amazon EC2 User Guide_.

```
Imds:
    Secured: `boolean`
```

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

### `Imds` properties

`Secured` (**Optional**, `Boolean`)

If `true`, restricts access to the head node's IMDS (and the
instance profile credentials) to a subset of superusers.

If `false`, every user in the head node has access to the head
node's IMDS.

The following users are permitted access to the head node's IMDS:

- root user
- cluster administrative user (`pc-cluster-admin` by default)
- operating system specific default user (`ec2-user` on Amazon
  Linux 2 and RedHat, and `ubuntu` on Ubuntu 18.04.

The default is `true`.

The `default` users are responsible for ensuring a cluster has
the permissions it needs to interact with AWS resources. If you disable
`default` user IMDS access, AWS ParallelCluster can't manage the
compute nodes and stops working. Don't disable `default` user
IMDS access.

When a user is granted access to the head node's IMDS, they can use the permissions
included in the [head node's instance profile](iam-roles-in-parallelcluster-v3.md "iam-roles-in-parallelcluster-v3.md").
For example, they can use these permissions to launch Amazon EC2 instances or to
read the password for an AD domain that the cluster is configured to use for
authentication.

To restrict IMDS access, AWS ParallelCluster manages a chain of
`iptables`.

Cluster users with `sudo` access can selectively enable or disable
access to the head node's IMDS for other individual users, including `default`
users, by running the command:

```
``$` sudo /opt/parallelcluster/scripts/imds/imds-access.sh --allow `<USERNAME>``
```

You can disable user IMDS access with the `--deny` option for this command.

If you unknowingly disable `default` user IMDS access, you can
restore the permission by using the `--allow` option.

###### Note

Any customization of `iptables` or `ip6tables`
rules can interfere with the mechanism used to restrict IMDS access on
the head node.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

## `Image`

**(Optional)** Defines a custom image for the head node.

```
Image:
     CustomAmi: `string`
```

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

### `Image` properties

`CustomAmi`
(**Optional**, `String`)

Specifies the ID of a custom AMI to use for the head node instead of the
default AMI. For more information, see [AWS ParallelCluster AMI customization](custom-ami-v3.md "custom-ami-v3.md").

If the custom AMI requires additional permissions for its launch, these
permissions must be added to both the user and head node policies.

For example, if a custom AMI has an encrypted snapshot associated with it,
the following additional policies are required in both the user and head
node policies:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:ReEncrypt*",
 "kms:CreateGrant",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`<AWS_KMS_KEY_ID>`"
 ]
 }
 ]
}`

```

To troubleshoot custom AMI validation warnings, see [Troubleshooting custom AMI issues](troubleshooting-v3-custom-amis.md "troubleshooting-v3-custom-amis.md").

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")
