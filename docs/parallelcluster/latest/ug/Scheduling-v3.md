# `Scheduling` section

**(Required)** Defines the job scheduler that's used in the
cluster and the compute instances that the job scheduler manages. You can either use the Slurm
or AWS Batch scheduler. Each supports a different set of settings and properties.

###### Topics

- [Scheduling properties](#Scheduling-v3.properties "#Scheduling-v3.properties")
- [AwsBatchQueues](#Scheduling-v3-AwsBatchQueues "#Scheduling-v3-AwsBatchQueues")
- [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues")
- [SlurmSettings](#Scheduling-v3-SlurmSettings "#Scheduling-v3-SlurmSettings")

```
Scheduling:
  Scheduler: slurm
  ScalingStrategy: `string`
  SlurmSettings:
    MungeKeySecretArn: `string`
    ScaledownIdletime: `integer`
    QueueUpdateStrategy: `string`
    EnableMemoryBasedScheduling: `boolean`
    CustomSlurmSettings: `[dict]`
    CustomSlurmSettingsIncludeFile: `string`
    Database:
      Uri: `string`
      UserName: `string`
      PasswordSecretArn: `string`
      DatabaseName: `string`
    ExternalSlurmdbd: `boolean`
      Host: `string`
      Port: `integer`
    Dns:
      DisableManagedDns: `boolean`
      HostedZoneId: `string`
      UseEc2Hostnames: `boolean`
  SlurmQueues:
    - Name: `string`
      ComputeSettings:
        LocalStorage:
          RootVolume:
            Size: `integer`
            Encrypted: `boolean`
            VolumeType: `string`
            Iops: `integer`
            Throughput: `integer`
          EphemeralVolume:
            MountDir: `string`
      CapacityReservationTarget:
        CapacityReservationId: `string`
        CapacityReservationResourceGroupArn: `string`
      CapacityType: `string`
      AllocationStrategy: `string`
      JobExclusiveAllocation: `boolean`
      CustomSlurmSettings: `dict`
      Tags:
        - Key: `string`
          Value: `string`
      HealthChecks:
        Gpu:
          Enabled: `boolean`
      Networking:
        SubnetIds:
          - `string`
        AssignPublicIp: `boolean`
        SecurityGroups:
          - `string`
        AdditionalSecurityGroups:
          - `string`
        PlacementGroup:
          Enabled: `boolean`
          Id: `string`
          Name: `string`
        Proxy:
          HttpProxyAddress: `string`
      ComputeResources:
        - Name: `string`
          InstanceType: `string`
          Instances:
            - InstanceType: `string`
          MinCount: `integer`
          MaxCount: `integer`
          DynamicNodePriority: `integer`
          StaticNodePriority: `integer`
          SpotPrice: `float`
          DisableSimultaneousMultithreading: `boolean`
          SchedulableMemory: `integer`
          HealthChecks:
            Gpu:
              Enabled: `boolean`
          Efa:
            Enabled: `boolean`
            GdrSupport: `boolean`
          CapacityReservationTarget:
            CapacityReservationId: `string`
            CapacityReservationResourceGroupArn: `string`
          Networking:
            PlacementGroup:
              Enabled: `boolean`
              Name: `string`
          CustomSlurmSettings: `dict`
          Tags:
            - Key: `string`
              Value: `string`
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
      Iam:
        InstanceProfile: `string`
        InstanceRole: `string`
        S3Access:
          - BucketName: `string`
            EnableWriteAccess: `boolean`
            KeyName: `string`
        AdditionalIamPolicies:
          - Policy: `string`
      Image:
        CustomAmi: `string`
```

```
Scheduling:
  Scheduler: awsbatch
  AwsBatchQueues:
    - Name: `string`
      CapacityType: `string`
      Networking:
        SubnetIds:
          - `string`
        AssignPublicIp: `boolean`
        SecurityGroups:
          - `string`
        AdditionalSecurityGroups:
          - `string`
      ComputeResources:  # this maps to a Batch compute environment (initially we support only 1)
        - Name: `string`
          InstanceTypes:
            - `string`
          MinvCpus: `integer`
          DesiredvCpus: `integer`
          MaxvCpus: `integer`
          SpotBidPercentage: `float`
```

## `Scheduling` properties

**`Scheduler` (**Required**, `String`)**

Specifies the type of scheduler that's used. Supported values are `slurm`
and `awsbatch`.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

###### Note

`awsbatch` only supports the `alinux2` operating system and
`x86_64` platform.

**`ScalingStrategy` (**Optional**, `String`)**

Allows you to choose how dynamic Slurm nodes scale up. Supported values are
`all-or-nothing`, `greedy-all-or-nothing` and
`best-effort` The default value is `all-or-nothing`.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

###### Note

The scaling strategy applies only to nodes to be resumed by Slurm, not to nodes
that are eventually already running.

- `all-or-nothing`This strategy strictly follows an
  all-or-nothing-approach, aimed at avoiding idle instances at the end of the scaling
  process. It operates on an all-or-nothing basis, meaning it either scales up
  completely or not at all. Be aware that there may be additional costs due to
  temporarily launched instances, when jobs require over 500 nodes or span multiple
  compute resources. This strategy has the lowest throughput among the three possible
  Scaling Strategies. The scaling time depends on the number of jobs submitted per
  Slurm resume program execution. Also, you can't scale far beyond the default
  RunInstances resource account limit per execution, which is 1000 instances by
  defaults. More details can be found at the [Amazon EC2 API throttling
  documentation](../../../AWSEC2/latest/APIReference/throttling.md "../../../AWSEC2/latest/APIReference/throttling.md")
- `greedy-all-or-nothing` Similar to the all-or-nothing strategy, it
  aims to avoid idle instances post-scaling. This strategy allows for temporary
  over-scaling during the scaling process in order to achieve higher throughput than
  the all-or-nothing approach but also comes with the same scaling limit of 1000
  instances as per the RunInstances resource account limit.
- `best-effort` This strategy prioritizes high throughput, even if it
  means that some instances might be idle at the end of the scaling process. It
  attempts to allocate as many nodes as requested by the jobs, but there's a
  possibility of not fulfilling the entire request. Unlike the other strategies, the
  best-effort approach can accumulate more instances than the standard RunInstances
  limit, at the cost of having idle resources along the multiple scaling process
  executions.

Each strategy is designed to cater to different scaling needs, allowing you to select one
that meets your specific requirements and constraints.

## `AwsBatchQueues`

**(Optional)** The AWS Batch queue settings. Only one queue is
supported. If [Scheduler](#yaml-Scheduling-Scheduler "#yaml-Scheduling-Scheduler") is set
to `awsbatch`, this section is required. For more information about the
`awsbatch` scheduler, see [networking setup](network-configuration-v3-batch.md "network-configuration-v3-batch.md") and [Using AWS Batch (awsbatch) scheduler with
AWS ParallelCluster](awsbatchcli-v3.md "awsbatchcli-v3.md").

```
AwsBatchQueues:
  - Name: `string`
    CapacityType: `string`
    Networking:
      SubnetIds:
        - `string`
      AssignPublicIp: `boolean`
      SecurityGroups:
        - `string`
      AdditionalSecurityGroups:
        - `string`
    ComputeResources:  # this maps to a Batch compute environment (initially we support only 1)
      - Name: `string`
        InstanceTypes:
          - `string`
        MinvCpus: `integer`
        DesiredvCpus: `integer`
        MaxvCpus: `integer`
        SpotBidPercentage: `float`
```

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

### `AwsBatchQueues`

properties

**`Name` (**Required**, `String`)**

The name of the AWS Batch queue.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

**`CapacityType`
(**Optional**, `String`)**

The type of the compute resources that the AWS Batch queue uses. Supported values
are `ONDEMAND` , `SPOT` or `CAPACITY_BLOCK`. The
default value is `ONDEMAND`.

###### Note

If you set `CapacityType` to `SPOT`, your account must
contain an `AWSServiceRoleForEC2Spot` service-linked role. You can create
this role using the following AWS CLI command.

```
``$` aws iam create-service-linked-role --aws-service-name spot.amazonaws.com`
```

For more information, see [Service-linked role for Spot Instance requests](../../../AWSEC2/latest/UserGuide/spot-requests.md#service-linked-roles-spot-instance-requests "../../../AWSEC2/latest/UserGuide/spot-requests.md#service-linked-roles-spot-instance-requests") in the _Amazon
Amazon EC2 User Guide for Linux Instances_.

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

#### `Networking`

**(Required)** Defines the networking configuration for
the AWS Batch queue.

```
Networking:
  SubnetIds:
    - `string`
  AssignPublicIp: `boolean`
  SecurityGroups:
    - `string`
  AdditionalSecurityGroups:
    - `string`
```

##### `Networking` properties

**`SubnetIds` (**Required**,
`[String]`)**

Specifies the ID of an existing subnet to provision the AWS Batch queue in.
Currently only one subnet is supported.

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

**`AssignPublicIp` (**Optional**,
`String`)**

Creates or assigns a public IP address to the nodes in the AWS Batch queue.
Supported values are `true` and `false`. The default depends
on the subnet that you specified.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

**`SecurityGroups` (**Optional**,
`[String]`)**

List of security groups that the AWS Batch queue uses. If you don't specify
security groups, AWS ParallelCluster creates new security groups.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

**`AdditionalSecurityGroups` (**Optional**, `[String]`)**

List of security groups that the AWS Batch queue uses.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

#### `ComputeResources`

**(Required)** Defines the ComputeResources configuration
for the AWS Batch queue.

```
ComputeResources:  # this maps to a Batch compute environment (initially we support only 1)
  - Name: `string`
    InstanceTypes:
      - `string`
    MinvCpus: `integer`
    DesiredvCpus: `integer`
    MaxvCpus: `integer`
    SpotBidPercentage: `float`
```

##### `ComputeResources` properties

**`Name` (**Required**,
`String`)**

The name of the AWS Batch queue compute environment.

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

**`InstanceTypes` (**Required**,
`[String]`)**

The AWS Batch compute environment array of instance types. All of the instance
types must use the `x86_64` architecture.

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

**`MinvCpus` (**Optional**,
`Integer`)**

The minimum number of VCPUs that an AWS Batch compute environment can
use.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

**`DesiredVcpus` (**Optional**,
`Integer`)**

The desired number of VCPUs in the AWS Batch compute environment. AWS Batch
adjusts this value between `MinvCpus` and `MaxvCpus` based
on the demand in the job queue.

[Update policy: This
setting is not analyzed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-ignored-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-ignored-v3")

**`MaxvCpus` (**Optional**,
`Integer`)**

The maximum number of VCPUs for the AWS Batch compute environment. You can't set
this to a value that's lower than `DesiredVcpus`.

[Update policy: This setting
can't be decreased during an update.](using-pcluster-update-cluster-v3.md#update-policy-no-decrease-v3 "using-pcluster-update-cluster-v3.md#update-policy-no-decrease-v3")

**`SpotBidPercentage` (**Optional**,
`Float`)**

The maximum percentage of the On-Demand price for the instance type that an
Amazon EC2 Spot Instance price can reach before instances are launched. The default value
is `100` (100%). The supported range is
`1`-`100`.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

## `SlurmQueues`

**(Optional)** Settings for the Slurm queue. If [Scheduler](#yaml-Scheduling-Scheduler "#yaml-Scheduling-Scheduler") is set to
`slurm`, this section is required.

```
SlurmQueues:
  - Name: `string`
    ComputeSettings:
      LocalStorage:
        RootVolume:
          Size: `integer`
          Encrypted: `boolean`
          VolumeType: `string`
          Iops: `integer`
          Throughput: `integer`
        EphemeralVolume:
          MountDir: `string`
    CapacityReservationTarget:
      CapacityReservationId: `string`
      CapacityReservationResourceGroupArn: `string`
    CapacityType: `string`
    AllocationStrategy: `string`
    JobExclusiveAllocation: `boolean`
    CustomSlurmSettings: `dict`
    Tags:
      - Key: `string`
        Value: `string`
    HealthChecks:
      Gpu:
        Enabled: `boolean`
    Networking:
      SubnetIds:
        - `string`
      AssignPublicIp: `boolean`
      SecurityGroups:
        - `string`
      AdditionalSecurityGroups:
        - `string`
      PlacementGroup:
        Enabled: `boolean`
        Id: `string`
        Name: `string`
      Proxy:
        HttpProxyAddress: `string`
    ComputeResources:
      - Name: `string`
        InstanceType: `string`
        Instances:
          - InstanceType: `string`
        MinCount: `integer`
        MaxCount: `integer`
        DynamicNodePriority: `integer`
        StaticNodePriority: `integer`
        SpotPrice: `float`
        DisableSimultaneousMultithreading: `boolean`
        SchedulableMemory: `integer`
        HealthChecks:
          Gpu:
            Enabled: `boolean`
        Efa:
          Enabled: `boolean`
          GdrSupport: `boolean`
        CapacityReservationTarget:
          CapacityReservationId: `string`
          CapacityReservationResourceGroupArn: `string`
        Networking:
          PlacementGroup:
            Enabled: `boolean`
            Name: `string`
        CustomSlurmSettings: `dict`
        Tags:
          - Key: `string`
            Value: `string`
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
    Iam:
      InstanceProfile: `string`
      InstanceRole: `string`
      S3Access:
        - BucketName: `string`
          EnableWriteAccess: `boolean`
          KeyName: `string`
      AdditionalIamPolicies:
        - Policy: `string`
    Image:
      CustomAmi: `string`
```

[Update policy: For this list
values setting, a new value can be added during an update or the compute fleet must be
stopped when removing an existing value.](using-pcluster-update-cluster-v3.md#update-policy-list-values-v3 "using-pcluster-update-cluster-v3.md#update-policy-list-values-v3")

### `SlurmQueues`

properties

**`Name` (**Required**, `String`)**

The name of the Slurm queue.

###### Note

Cluster size may change during an update. For more information, see
[Cluster capacity size and update](slurm-workload-manager-v3.md "slurm-workload-manager-v3.md")

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

**`CapacityReservationTarget`**

###### Note

`CapacityReservationTarget` is added with AWS ParallelCluster version
3.3.0.

```
CapacityReservationTarget:
   CapacityReservationId: `string`
   CapacityReservationResourceGroupArn: `string`
```

Specifies the On-Demand capacity reservation for the queue's compute
resources.

**`CapacityReservationId` (**Optional**,
`String`)**

The ID of the existing capacity reservation to target for the queue's
compute resources. The ID can refer to an [ODCR](../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md") or a
[Capacity Block for
ML](../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md").

The reservation must use the same platform that the instance uses. For
example, if your instances run on `rhel8`, your capacity reservation
must run on the Red Hat Enterprise Linux platform. For more information, see
[Supported platforms](../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md#capacity-reservations-platforms "../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md#capacity-reservations-platforms") in the _Amazon EC2 User Guide for Linux
Instances_.

###### Note

If you include [Instances](#yaml-Scheduling-SlurmQueues-ComputeResources-Instances "#yaml-Scheduling-SlurmQueues-ComputeResources-Instances") in the cluster configuration, you must
exclude this queue level `CapacityReservationId` setting from the
configuration.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`CapacityReservationResourceGroupArn` (**Optional**, `String`)**

The Amazon Resource Name (ARN) of the resource group that serves as the service-linked group of
capacity reservations for the queue's compute resources. AWS ParallelCluster
identifies and uses the most appropriate capacity reservation from the resource
group based on the following conditions:

- If `PlacementGroup` is enabled in [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") /
  [Networking](#yaml-Scheduling-SlurmQueues-ComputeResources-Networking "#yaml-Scheduling-SlurmQueues-ComputeResources-Networking") or [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") /
  [ComputeResources](#Scheduling-v3-SlurmQueues-ComputeResources "#Scheduling-v3-SlurmQueues-ComputeResources") / [Networking](#yaml-Scheduling-SlurmQueues-ComputeResources-Networking "#yaml-Scheduling-SlurmQueues-ComputeResources-Networking"), AWS ParallelCluster selects a resource
  group that targets the instance type and `PlacementGroup` for a
  compute resource, if the compute resource exists.

The `PlacementGroup` must target one of the instance types
that's defined in [ComputeResources](#Scheduling-v3-SlurmQueues-ComputeResources "#Scheduling-v3-SlurmQueues-ComputeResources").

- If `PlacementGroup` isn't enabled in [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") /
  [Networking](#yaml-Scheduling-SlurmQueues-ComputeResources-Networking "#yaml-Scheduling-SlurmQueues-ComputeResources-Networking") or [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") /
  [ComputeResources](#Scheduling-v3-SlurmQueues-ComputeResources "#Scheduling-v3-SlurmQueues-ComputeResources") / [Networking](#yaml-Scheduling-SlurmQueues-ComputeResources-Networking "#yaml-Scheduling-SlurmQueues-ComputeResources-Networking"), AWS ParallelCluster selects a resource
  group that targets only the instance type of a compute resource, if the
  compute resource exists.

The resource group must have at least one ODCR for each instance type
reserved in an Availability Zone across all of the queue's compute resources and
Availability Zones. For more information, see [Launch instances with On-Demand Capacity Reservations (ODCR)](launch-instances-odcr-v3.md "launch-instances-odcr-v3.md").

For more information on multiple subnet configuration requirements, see
[Networking](#Scheduling-v3-SlurmQueues-Networking "#Scheduling-v3-SlurmQueues-Networking") / [SubnetIds](#yaml-Scheduling-SlurmQueues-Networking-SubnetIds "#yaml-Scheduling-SlurmQueues-Networking-SubnetIds").

###### Note

Multiple Availability Zones is added in AWS ParallelCluster version
3.4.0.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`CapacityType`
(**Optional**, `String`)**

The type of the compute resources that the Slurm queue uses. Supported values
are `ONDEMAND` , `SPOT` or `CAPACITY_BLOCK`. The default value is
`ONDEMAND`.

###### Note

If you set the `CapacityType` to `SPOT`, your account must
have an `AWSServiceRoleForEC2Spot` service-linked role. You can use the following
AWS CLI command to create this role.

```
``$` aws iam create-service-linked-role --aws-service-name spot.amazonaws.com`
```

For more information, see [Service-linked role for Spot Instance requests](../../../AWSEC2/latest/UserGuide/spot-requests.md#service-linked-roles-spot-instance-requests "../../../AWSEC2/latest/UserGuide/spot-requests.md#service-linked-roles-spot-instance-requests") in the _Amazon
Amazon EC2 User Guide for Linux Instances_.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`AllocationStrategy` (**Optional**,
`String`)**

Specify the allocation strategy for all the compute resources defined in [Instances](#yaml-Scheduling-SlurmQueues-ComputeResources-Instances "#yaml-Scheduling-SlurmQueues-ComputeResources-Instances").

Valid values: `lowest-price` | `capacity-optimized` |
`price-capacity-optimized` | `prioritized` | `capacity-optimized-prioritized`

| CapacityType   | Allowed strategies                                                                         |
| -------------- | ------------------------------------------------------------------------------------------ |
| ONDEMAND       | lowest-price, prioritized                                                                  |
| SPOT           | lowest-price, capacity-optimized, price-capacity-optimized, capacity-optimized-prioritized |
| CAPACITY_BLOCK | Not supported — AllocationStrategy cannot be configured                                    |

Default: `lowest-price`

**`lowest-price`**

- If you use `CapacityType = ONDEMAND`, Amazon EC2 Fleet uses price to
  determine the order and launches the lowest price instances first.
- If you use `CapacityType = SPOT`, Amazon EC2 Fleet launches
  instances from the lowest price Spot Instance pool that has available
  capacity. If a pool runs out of capacity before it fulfills your required
  capacity, Amazon EC2 Fleet fulfills your request by launching instances for you. In
  particular, Amazon EC2 Fleet launches instances from the lowest price Spot Instance
  pool that has available capacity. Amazon EC2 Fleet might launch Spot Instances from
  several different pools.
- If you set `CapacityType = CAPACITY_BLOCK`, there are no
  allocation strategies, thus `AllocationStrategy` parameter cannot
  be configured.

**`capacity-optimized`**

- If you set `CapacityType = ONDEMAND`,
  `capacity-optimized` isn't available.
- If you set `CapacityType = SPOT`, Amazon EC2 Fleet launches
  instances from Spot Instance pools with optimal capacity for the number of
  instances to be launched.

**`price-capacity-optimized`**

- If you set `CapacityType = ONDEMAND`,
  `capacity-optimized` isn't available.
- If you set `CapacityType = SPOT`, Amazon EC2
  Fleet identifies the pools with the highest capacity
  availability for the number of instances that are launching.
  This means that we will request Spot Instances from the
  pools that we believe have the lowest chance of interruption
  in the near term. Amazon EC2 Fleet then requests Spot Instances
  from the lowest priced of these pools.

**`prioritized`**

- If you set `CapacityType = ONDEMAND`, Amazon EC2 Fleet honors the
  priority order that AWS ParallelCluster applies to the LaunchTemplate overrides when
  multiple subnets are specified. AWS ParallelCluster derives the override `priority`
  from the position of the target subnet in `SlurmQueues/Networking/SubnetIds`
  with the first Subnet getting the highest priority.
  The priorities are drived by AWS ParallelCluster in descending order from
  `SlurmQueues/Networking/SubnetIds`, with the first SubnetId having the
  highest priority and the last SubnetID having the lowest priority.
- If you set `CapacityType = SPOT`, `prioritized` isn't
  available.

**`capacity-optimized-prioritized`**

- If you set `CapacityType = ONDEMAND`, `capacity-optimized-prioritized`
  isn't available.
- If you set `CapacityType = SPOT`, Amazon EC2 Fleet optimizes for
  capacity first and then applies, on a best-effort basis, the priority order that
  AWS ParallelCluster assigns to LaunchTemplate overrides.
  The priorities are drived by AWS ParallelCluster in descending order from
  `SlurmQueues/Networking/SubnetIds`, with the first SubnetId having the
  highest priority and the last SubnetID having the lowest priority.

All overrides that target the same subnet receive the same priority value.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

###### Note

`AllocationStrategy` is supported starting in AWS ParallelCluster
version 3.3.0.

**New in 3.14.0**: `prioritized` (for On-Demand)
and `capacity-optimized-prioritized` (for Spot).

**`JobExclusiveAllocation` (**Optional**,
`String`)**

If set to `true`, the Slurm partition `OverSubscribe` flag
is set to `EXCLUSIVE`. When
`OverSubscribe`=`EXCLUSIVE`, jobs in the partition have
exclusive access to all allocated nodes. For more information, see [EXCLUSIVE](https://slurm.schedmd.com/slurm.conf.html#OPT_EXCLUSIVE "https://slurm.schedmd.com/slurm.conf.html#OPT_EXCLUSIVE") in
the Slurm documentation.

Valid values: `true` | `false`

Default: `false`

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

###### Note

`JobExclusiveAllocation` is supported starting in AWS ParallelCluster
version 3.7.0.

**`CustomSlurmSettings` (**Optional**,
`Dict`)**

Defines the custom Slurm partition (queue) configuration settings.

Specifies a dictionary of custom Slurm configuration parameter key-value pairs
that apply to queues (partitions).

Each separate key-value pair, such as `Param1: Value1`, is added
separately to the end of the Slurm partition configuration line in the format
`Param1=Value1`.

You can only specify Slurm configuration parameters that aren't deny-listed in
`CustomSlurmSettings`. For information about deny-listed Slurm
configuration parameters, see [Deny-listed Slurm configuration parameters for CustomSlurmSettings](slurm-configuration-settings-v3.md#slurm-configuration-denylists-v3 "slurm-configuration-settings-v3.md#slurm-configuration-denylists-v3").

AWS ParallelCluster only checks whether a parameter is in a deny list.
AWS ParallelCluster doesn't validate your custom Slurm configuration parameter syntax
or semantics. It is your responsibility to validate your custom Slurm configuration
parameters. Invalid custom Slurm configuration parameters can cause Slurm daemon
failures that can lead to cluster create and update failures.

For more information about how to specify custom Slurm configuration parameters
with AWS ParallelCluster, see [Slurm configuration customization](slurm-configuration-settings-v3.md "slurm-configuration-settings-v3.md").

For more information about Slurm configuration parameters, see [slurm.conf](https://slurm.schedmd.com/slurm.conf.html "https://slurm.schedmd.com/slurm.conf.html") in the Slurm
documentation.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

###### Note

`CustomSlurmSettings` is supported starting with AWS ParallelCluster
version 3.6.0.

**`Tags` (**Optional**, [String])**

A list of tag key-value pairs. [ComputeResource](#yaml-Scheduling-SlurmQueues-ComputeResources-Tags "#yaml-Scheduling-SlurmQueues-ComputeResources-Tags") tags override duplicate tags specified in the
[Tags section](Tags-v3.md "Tags-v3.md") or in `SlurmQueues` /
`Tags`.

**`Key` (**Optional**, `String`)**

The tag key.

**`Value`
(**Optional**, `String`)**

The tag value.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`HealthChecks`
(**Optional**)**

Specify compute node health checks on all compute resources in the queue.

`Gpu`
(**Optional**)

Specify GPU health checks on all compute resources in a queue.

###### Note

AWS ParallelCluster doesn't support `HealthChecks` /
`Gpu` in nodes that use `alinux2` ARM operating
systems. These platforms don't support the [NVIDIA Data Center GPU Manager (DCGM)](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/getting-started.html#supported-linux-distributions "https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/getting-started.html#supported-linux-distributions").

Enabling GPU health checks when using instance types whose total GPU
memory size is higher than 327680 MiB is discouraged.

`Enabled` (**Optional**,
`Boolean`)

Whether AWS ParallelCluster performs GPU health checks on compute nodes.
The default is `false`.

###### `Gpu` health check behavior

- If `Gpu` / `Enabled` is set to `true`,
  AWS ParallelCluster performs GPU health checks on compute resources in the
  queue.
- The `Gpu` health check performs GPU health checks on compute
  resources to prevent the submission of jobs on nodes with a degraded
  GPU.
- If a compute node fails a `Gpu` health check, the compute
  node state changes to `DRAIN`. New jobs don't start on this node.
  Existing jobs run to completion. After all running jobs complete, the
  compute node terminates if it's a dynamic node, and it's replaced if it's a
  static node.
- The duration of the `Gpu` health check depends on the selected
  instance type, the number of GPUs in the instance, the total GPU memory and
  the number of `Gpu` health check targets (equivalent to the number
  of job GPU targets). For example, on a p4d.24xlarge, the typical duration is
  3 minutes.
- If the `Gpu` health check runs on an instance that's not
  supported, it exits and the job runs on the compute node. For example, if an
  instance doesn't have a GPU, or, if an instance has a GPU, but it isn't an
  NVIDIA GPU, the health check exits and the job runs on the compute node.
  Only NVIDIA GPUs are supported.
- The `Gpu` health check uses the `dcgmi` tool to
  perform health checks on a node and takes the following steps:

When the `Gpu` health check begins in a node:

    1. It detects whether the `nvidia-dcgm` and
     `nvidia-fabricmanager` services are running.
    2. If these services aren't running, the `Gpu` health check
     starts them.
    3. It detects whether the persistence mode is enabled.
    4. If the persistence mode isn't enabled, the `Gpu` health
     check enables it.

At the end of the health check, the `Gpu` health check
restores these services and resources to their initial state.

- If the job is assigned to a specific set of node GPUs, the
  `Gpu` health check runs only on that specific set. Otherwise,
  the `Gpu` health check runs on all GPUs in the node.
- If a compute node receives 2 or more `Gpu` health check
  requests at the same time, only the first health check runs and the others
  are skipped. This is also the case for health checks that target node GPUs.
  You can check the log files for additional information regarding this
  situation.
- The health check log for a specific compute node is available in the
  `/var/log/parallelcluster/slurm_health_check.log` file.
  The file is available in Amazon CloudWatch, in the cluster CloudWatch log group, where you
  can find:
  - Details on the action run by the `Gpu` health check,
    including enabling and disabling services and persistence mode.
  - The GPU identifier, serial ID, and the UUID.
  - The health check output.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

###### Note

`HealthChecks` is supported starting in AWS ParallelCluster version
3.6.0.

#### `Networking`

**(Required)** Defines the networking configuration for
the Slurm queue.

```
Networking:
  SubnetIds:
    - `string`
  AssignPublicIp: `boolean`
  SecurityGroups:
    - `string`
  AdditionalSecurityGroups:
    - `string`
  PlacementGroup:
    Enabled: `boolean`
    Id: `string`
    Name: `string`
  Proxy:
    HttpProxyAddress: `string`
```

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

##### `Networking` properties

**`SubnetIds` (**Required**,
`[String]`)**

The IDs of existing subnets that you provision the Slurm
queue in.

If you configure instance types in [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") / [ComputeResources](#Scheduling-v3-SlurmQueues-ComputeResources "#Scheduling-v3-SlurmQueues-ComputeResources") / [InstanceType](#yaml-Scheduling-SlurmQueues-ComputeResources-InstanceType "#yaml-Scheduling-SlurmQueues-ComputeResources-InstanceType"), you can only define one subnet.

If you configure instance types in [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") / [ComputeResources](#Scheduling-v3-SlurmQueues-ComputeResources "#Scheduling-v3-SlurmQueues-ComputeResources") / [Instances](#yaml-Scheduling-SlurmQueues-ComputeResources-Instances "#yaml-Scheduling-SlurmQueues-ComputeResources-Instances"), you can define a single subnet or multiple
subnets.

If you use multiple subnets, all subnets defined for a queue must be in the
same VPC, with each subnet in a separate Availability Zone (AZ).

For example, suppose you define subnet-1 and subnet-2 for your queue.

`subnet-1` and `subnet-2` can't both be in AZ-1.

`subnet-1` can be in AZ-1 and `subnet-2` can be in
AZ-2.

If you configure only one instance type and want to use multiple subnets,
define your instance type in `Instances` rather than
`InstanceType`.

For example, define `ComputeResources` / `Instances` /
`InstanceType`=`instance.type` instead of
`ComputeResources` /
`InstanceType`=`instance.type`.

###### Note

Elastic Fabric Adapter (EFA) isn't supported over different availability
zones.

The use of multiple Availability Zones might cause increases in storage
networking latency and added inter-AZ data transfer costs. For example, this could
occur when an instance accesses file storage that's located in a different AZ. For
more information, see [Data Transfer within the same AWS Region](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer_within_the_same_AWS_Region "https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer_within_the_same_AWS_Region").

###### Cluster updates to change from the use of a single subnet to multiple

subnets:

- Suppose the subnet definition of a cluster is defined with a single subnet
  and an AWS ParallelCluster managed FSx for Lustre file system. Then, you can't
  update this cluster with an updated subnet ID definition directly. To make the
  cluster update, you must first change the managed file system to an external
  file system. For more information, see [Convert AWS ParallelCluster managed storage to external storage](shared-storage-conversion-v3.md "shared-storage-conversion-v3.md").
- Suppose the subnet definition of a cluster is defined with a single subnet
  and an external Amazon EFS file system if EFS mount targets don't exist for all of
  the AZs for the multiple subnets defined to be added. Then, you can't update
  this cluster with an updated subnet ID definition directly. To make the
  cluster update or to create a cluster, you must first create all of the mount
  targets for all of the AZs for the defined multiple subnets.

###### Availability Zones and cluster capacity reservations defined in [CapacityReservationResourceGroupArn](#yaml-Scheduling-SlurmQueues-CapacityReservationResourceGroupArn "#yaml-Scheduling-SlurmQueues-CapacityReservationResourceGroupArn"):

- You can't create a cluster if there is no overlap between the set of
  instance types and availability zones covered by the defined capacity
  reservation resource group and the set of instance types and availability
  zones defined for the queue.
- You can create a cluster if there is a partial overlap between the set of
  instance types and availability zones covered by the defined capacity
  reservation resource group and the set of instance types and availability
  zones defined for the queue. AWS ParallelCluster sends a warning message about
  the partial overlap for this case.
- For more information, see [Launch instances with On-Demand Capacity Reservations (ODCR)](launch-instances-odcr-v3.md "launch-instances-odcr-v3.md").

###### Note

Multiple Availability Zones is added in AWS ParallelCluster version
3.4.0.

###### Warning

This warning applies to all 3.x.y AWS ParallelCluster versions prior to
version 3.3.1. AWS ParallelCluster version 3.3.1 isn't impacted if this parameter
is changed.

For AWS ParallelCluster 3 versions prior to version 3.3.1:

If you change this parameter and update a cluster this creates a new managed
FSx for Lustre file system and deletes the existing managed FSx for Lustre file system
without preserving the existing data. This results in data loss. Before you
proceed, make sure you back up the data from the existing FSx for Lustre file
system if you want to preserve data. For more information, see [Working with backups](../../../fsx/latest/LustreGuide/using-backups-fsx.md "../../../fsx/latest/LustreGuide/using-backups-fsx.md") in the _FSx for Lustre User
Guide_.

If a new subnet value is added, [Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

If a subnet value is removed, [Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`AssignPublicIp` (**Optional**,
`String`)**

Creates or assigns a public IP address to the nodes in the Slurm queue.
Supported values are `true` and `false`. The subnet that you
specify determines the default value. A subnet with public IPs default to
assigning public IP addresses.

If you define a p4d or hpc6id instance type, or
another instance type that has multiple network interfaces or a network interface
card, you must set [HeadNode](HeadNode-v3.md "HeadNode-v3.md") /
[Networking](HeadNode-v3.md#HeadNode-v3-Networking "HeadNode-v3.md#HeadNode-v3-Networking") / [ElasticIp](HeadNode-v3.md#yaml-HeadNode-Networking-ElasticIp "HeadNode-v3.md#yaml-HeadNode-Networking-ElasticIp") to
`true` to provide public access. AWS public IPs can only be
assigned to instances launched with a single network interface. For this case, we
recommend that you use a [NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") to provide
public access to the cluster compute nodes. In this case, set
`AssignPublicIp` to `false`. For more information on IP
addresses, see [Assign a public IPv4 address during instance launch](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#public-ip-addresses "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#public-ip-addresses") in the
_Amazon EC2 User Guide for Linux Instances_.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

**`SecurityGroups` (**Optional**,
`[String]`)**

A list of security groups to use for the Slurm queue. If no security groups
are specified, AWS ParallelCluster creates security groups for you.

Verify that the security groups are configured correctly for your [SharedStorage](SharedStorage-v3.md "SharedStorage-v3.md") systems.

###### Warning

This warning applies to all 3.`x`.`y` AWS ParallelCluster
versions prior to version 3.3.0. AWS ParallelCluster version 3.3.0 isn't impacted
if this parameter is changed.

For AWS ParallelCluster 3 versions prior to version 3.3.0:

If you change this parameter and update a cluster this creates a new managed
FSx for Lustre file system and deletes the existing managed FSx for Lustre file system
without preserving the existing data. This results in data loss. Make sure to
back up the data from the existing FSx for Lustre file system if you want to
preserve data. For more information, see [Working with
backups](../../../fsx/latest/LustreGuide/using-backups-fsx.md "../../../fsx/latest/LustreGuide/using-backups-fsx.md") in the _FSx for Lustre User Guide_.

###### Warning

If you enable [Efa](#yaml-Scheduling-SlurmQueues-ComputeResources-Efa "#yaml-Scheduling-SlurmQueues-ComputeResources-Efa") for your
compute instances, make sure that your EFA-enabled instances are members of a
security group that allows all inbound and outbound traffic to itself.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

**`AdditionalSecurityGroups` (**Optional**, `[String]`)**

A list of additional security groups to use for the Slurm queue.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

**`PlacementGroup` (**Optional**)**

Specifies the placement group settings for the Slurm queue.

```
PlacementGroup:
  Enabled: `boolean`
  Id: `string`
  Name: `string`
```

[Update policy: All
compute nodes must be stopped for a managed placement group deletion. The compute fleet
must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-remove-placement-group-v3 "using-pcluster-update-cluster-v3.md#update-policy-remove-placement-group-v3")

**`Enabled` (**Optional**,
`Boolean`)**

Indicates whether a placement group is used for the Slurm queue. The
default is `false`.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Id` (**Optional**,
`String`)**

The placement group ID for an existing cluster placement group that
the Slurm queue uses. Make sure to provide the placement group
_ID_ and _not the name_.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Name` (**Optional**,
`String`)**

The placement group name for an existing cluster placement group that
the Slurm queue uses. Make sure to provide the placement group
_name_ and _not the ID_.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

###### Note

- If `PlacementGroup` / `Enabled` is set to
  `true`, without a `Name` or `Id` defined,
  each compute resource is assigned its own managed placement group, unless
  [ComputeResources](#Scheduling-v3-SlurmQueues-ComputeResources "#Scheduling-v3-SlurmQueues-ComputeResources") / [Networking](#yaml-Scheduling-SlurmQueues-ComputeResources-Networking "#yaml-Scheduling-SlurmQueues-ComputeResources-Networking") / [PlacementGroup](#yaml-Scheduling-SlurmQueues-ComputeResources-Networking-PlacementGroup "#yaml-Scheduling-SlurmQueues-ComputeResources-Networking-PlacementGroup") is defined to override this
  setting.
- Starting with AWS ParallelCluster version 3.3.0, [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues")
  / [Networking](#Scheduling-v3-SlurmQueues-Networking "#Scheduling-v3-SlurmQueues-Networking") / [PlacementGroup](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup") / [Name](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Name "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Name") was added as a preferred alternative to [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues")
  / [Networking](#Scheduling-v3-SlurmQueues-Networking "#Scheduling-v3-SlurmQueues-Networking") / [PlacementGroup](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup") / [Id](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Id "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Id").

[PlacementGroup](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup") / [Id](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Id "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Id") and [PlacementGroup](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup") / [Name](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Name "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Name") are equivalent. You can use either one.

If you include both [PlacementGroup](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup") / [Id](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Id "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Id") and [PlacementGroup](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup") / [Name](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Name "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Name"), AWS ParallelCluster fails. You can only choose
one or the other.

You don't need to update your cluster to use [PlacementGroup](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup") / [Name](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Name "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup-Name").

**`Proxy`
(**Optional**)**

Specifies the proxy settings for the Slurm queue.

```
Proxy:
  HttpProxyAddress: `string`
```

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`HttpProxyAddress` (**Optional**,
`String`)**

Defines an HTTP or HTTPS proxy server for the Slurm queue. Typically,
it's `https://`x.x.x.x:8080``.

There's no default value.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

#### `Image`

**(Optional)** Specifies the image to use for the Slurm
queue. To use the same AMI for all nodes, use the [CustomAmi](Image-v3.md#yaml-Image-CustomAmi "Image-v3.md#yaml-Image-CustomAmi") setting in the [Image section](Image-v3.md "Image-v3.md").

```
Image:
  CustomAmi: `string`
```

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

##### `Image`

Properties

**`CustomAmi`
(**Optional**, `String`)**

The AMI to use for the Slurm queue instead of the default AMIs. You can use
the pcluster CLI command to view a list of the default AMIs.

###### Note

The AMI must be based on the same operating system that's used by the head node.

```
`pcluster list-official-images`
```

If the custom AMI requires additional permissions for its launch, you must add
these permissions to the head node policy.

For example, if a custom AMI has an encrypted snapshot associated with it, the
following additional policies are required in the head node policies.

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

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

#### `ComputeResources`

**(Required)** Defines the `ComputeResources`
configuration for the Slurm queue.

###### Note

- Cluster size may change during an update. For more information, see
  [Cluster capacity size and update](slurm-workload-manager-v3.md "slurm-workload-manager-v3.md").
- New compute resources can be added to the cluster only if they are deployed in subnets
  that belong to CIDR blocks that exist when the cluster is created.

```
ComputeResources:
  - Name: `string`
    InstanceType: `string`
    Instances:
      - InstanceType: `string`
    MinCount: `integer`
    MaxCount: `integer`
    DynamicNodePriority: `integer`
    StaticNodePriority: `integer`
    SpotPrice: `float`
    DisableSimultaneousMultithreading: `boolean`
    SchedulableMemory: `integer`
    HealthChecks:
      Gpu:
        Enabled: `boolean`
    Efa:
      Enabled: `boolean`
      GdrSupport: `boolean`
    CapacityReservationTarget:
      CapacityReservationId: `string`
      CapacityReservationResourceGroupArn: `string`
    Networking:
      PlacementGroup:
        Enabled: `boolean`
        Name: `string`
    CustomSlurmSettings: `dict`
    Tags:
      - Key: `string`
        Value: `string`
```

[Update policy: For this list
values setting, a new value can be added during an update or the compute fleet must be
stopped when removing an existing value.](using-pcluster-update-cluster-v3.md#update-policy-list-values-v3 "using-pcluster-update-cluster-v3.md#update-policy-list-values-v3")

##### `ComputeResources` properties

**`Name` (**Required**,
`String`)**

The name of the Slurm queue compute environment. The name can have up to 25
characters.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

**`InstanceType` (**Required**,
`String`)**

The instance type that's used in this Slurm compute resource. All of the
instance types in a cluster must use the same processor architecture. Instances
can use either the `x86_64` or `arm64` architecture.

The cluster configuration must define either [InstanceType](#yaml-Scheduling-SlurmQueues-ComputeResources-InstanceType "#yaml-Scheduling-SlurmQueues-ComputeResources-InstanceType") or [Instances](#yaml-Scheduling-SlurmQueues-ComputeResources-Instances "#yaml-Scheduling-SlurmQueues-ComputeResources-Instances"). If both are defined, AWS ParallelCluster fails.

When you define `InstanceType`, you can't define multiple subnets.
If you configure only one instance type and want to use multiple subnets, define
your instance type in `Instances` rather than in
`InstanceType`. For more information, see [Networking](#Scheduling-v3-SlurmQueues-Networking "#Scheduling-v3-SlurmQueues-Networking") /
[SubnetIds](#yaml-Scheduling-SlurmQueues-Networking-SubnetIds "#yaml-Scheduling-SlurmQueues-Networking-SubnetIds").

If you define a p4d or hpc6id instance type, or
another instance type that has multiple network interfaces or a network interface
card, you must launch the compute instances in private subnet as described in
[AWS ParallelCluster using two subnets](network-configuration-v3-two-subnets.md "network-configuration-v3-two-subnets.md"). AWS public IPs can
only be assigned to instances that are launched with a single network interface.
For more information, see [Assign a public IPv4 address during instance launch](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#public-ip-addresses "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#public-ip-addresses") in the
_Amazon EC2 User Guide for Linux Instances_.

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

**`Instances` (**Required**)**

Specifies the list of instance types for a compute resource. To specify the
allocation strategy for the list of instance types, see [AllocationStrategy](#yaml-Scheduling-SlurmQueues-AllocationStrategy "#yaml-Scheduling-SlurmQueues-AllocationStrategy").

The cluster configuration must define either [InstanceType](#yaml-Scheduling-SlurmQueues-ComputeResources-InstanceType "#yaml-Scheduling-SlurmQueues-ComputeResources-InstanceType") or [Instances](#yaml-Scheduling-SlurmQueues-ComputeResources-Instances "#yaml-Scheduling-SlurmQueues-ComputeResources-Instances"). If both are defined, AWS ParallelCluster
fails.

For more information, see [Multiple instance type allocation with Slurm](slurm-multiple-instance-allocation-v3.md "slurm-multiple-instance-allocation-v3.md").

```
Instances:
   - InstanceType: `string`
```

###### Note

Starting with AWS ParallelCluster version 3.7.0,
`EnableMemoryBasedScheduling` can be enabled if you configure
multiple instance types in [Instances](#yaml-Scheduling-SlurmQueues-ComputeResources-Instances "#yaml-Scheduling-SlurmQueues-ComputeResources-Instances").

For AWS ParallelCluster versions 3.2.0 to 3.6.`x`,
`EnableMemoryBasedScheduling` can't be enabled if you configure
multiple instance types in [Instances](#yaml-Scheduling-SlurmQueues-ComputeResources-Instances "#yaml-Scheduling-SlurmQueues-ComputeResources-Instances").

[Update policy: For this list
values setting, a new value can be added during an update or the compute fleet must be
stopped when removing an existing value.](using-pcluster-update-cluster-v3.md#update-policy-list-values-v3 "using-pcluster-update-cluster-v3.md#update-policy-list-values-v3")

**`InstanceType` (**Required**,
`String`)**

The instance type to use in this Slurm compute resource. All of the
instance types in a cluster must use the same processor architecture, either
`x86_64` or `arm64`.

The instance types listed in [Instances](#yaml-Scheduling-SlurmQueues-ComputeResources-Instances "#yaml-Scheduling-SlurmQueues-ComputeResources-Instances") must have:

- The same number of vCPUs, or, if [DisableSimultaneousMultithreading](#yaml-Scheduling-SlurmQueues-ComputeResources-DisableSimultaneousMultithreading "#yaml-Scheduling-SlurmQueues-ComputeResources-DisableSimultaneousMultithreading") is set to
  `true`, the same number of cores.
- The same number of accelerators of the same manufacturers.
- EFA supported, if [Efa](#yaml-Scheduling-SlurmQueues-ComputeResources-Efa "#yaml-Scheduling-SlurmQueues-ComputeResources-Efa") / [Enabled](#yaml-Scheduling-SlurmQueues-ComputeResources-Efa-Enabled "#yaml-Scheduling-SlurmQueues-ComputeResources-Efa-Enabled") set to `true`.

The instance types that are listed in [Instances](#yaml-Scheduling-SlurmQueues-ComputeResources-Instances "#yaml-Scheduling-SlurmQueues-ComputeResources-Instances") can have:

- Different amount of memory.

In this case, the minimum memory is to be set as a consumable
Slurm resource.

###### Note

Starting with AWS ParallelCluster version 3.7.0,
`EnableMemoryBasedScheduling` can be enabled if you
configure multiple instance types in [Instances](#yaml-Scheduling-SlurmQueues-ComputeResources-Instances "#yaml-Scheduling-SlurmQueues-ComputeResources-Instances").

For AWS ParallelCluster versions 3.2.0 to
3.6.`x`,
`EnableMemoryBasedScheduling` can't be enabled if you
configure multiple instance types in [Instances](#yaml-Scheduling-SlurmQueues-ComputeResources-Instances "#yaml-Scheduling-SlurmQueues-ComputeResources-Instances").

- Different network cards.

In this case, the number of network interfaces configured for the
compute resource is defined by the instance type with the smallest
number of network cards.

- Different network bandwidth.
- Different instance store size.

If you define a p4d or hpc6id instance
type, or another instance type that has multiple network interfaces or a
network interface card, you must launch the compute instances in private
subnet as described in [AWS ParallelCluster using two subnets](network-configuration-v3-two-subnets.md "network-configuration-v3-two-subnets.md"). AWS public IPs
can only be assigned to instances launched with a single network interface.
For more information, see [Assign a public IPv4 address during instance launch](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#public-ip-addresses "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#public-ip-addresses") in the
_Amazon EC2 User Guide for Linux Instances_.

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

###### Note

`Instances` is supported starting with AWS ParallelCluster version
3.3.0.

**`MinCount` (**Optional**,
`Integer`)**

The minimum number of instances that the Slurm compute resource uses. The
default is 0.

###### Note

Cluster size may change during an update. For more information, see
[Cluster capacity size and update](slurm-workload-manager-v3.md "slurm-workload-manager-v3.md")

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

**`MaxCount` (**Optional**,
`Integer`)**

The maximum number of instances that the Slurm compute resource uses. The
default is 10.

When you use `CapacityType = CAPACITY_BLOCK`, `MaxCount`
must be equal to `MinCount` and greater than 0, because all the
instances part of the Capacity Block reservation are managed as static
nodes.

At cluster creation time, the head node waits for all the static nodes to be
ready before signaling the success of cluster creation. However, when you use
`CapacityType = CAPACITY_BLOCK`, the nodes part of the compute
resources associated to Capacity Blocks won't be considered for this check. The
cluster will be created even if not all the configured Capacity Blocks are
active.

###### Note

Cluster size may change during an update. For more information, see
[Cluster capacity size and update](slurm-workload-manager-v3.md "slurm-workload-manager-v3.md")

**`DynamicNodePriority` (**Optional**,
`Integer`)**

The priority of dynamic nodes in a queue compute resource. The priority maps
to the Slurm node [`Weight`](https://slurm.schedmd.com/slurm.conf.html#OPT_Weight "https://slurm.schedmd.com/slurm.conf.html#OPT_Weight") configuration parameter for the compute resource
dynamic nodes. The default value is `1000`.

Slurm prioritizes nodes with the lowest `Weight` values
first.

###### Warning

The use of many different `Weight` values in a Slurm partition
(queue) might slow down the rate of job scheduling in the queue.

In AWS ParallelCluster versions earlier than version 3.7.0, both static and
dynamic nodes were assigned the same default weight of `1`. In this
case, Slurm might prioritize idle dynamic nodes over idle static nodes due to
the naming schema for static and dynamic nodes. When all else is equal, Slurm
schedules nodes alphabetically by name.

###### Note

`DynamicNodePriority` is added in AWS ParallelCluster version
3.7.0.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

**`StaticNodePriority` (**Optional**,
`Integer`)**

The priority of static nodes in a queue compute resource. The priority maps to
the Slurm node [`Weight`](https://slurm.schedmd.com/slurm.conf.html#OPT_Weight "https://slurm.schedmd.com/slurm.conf.html#OPT_Weight") configuration parameter for the compute resource
static nodes. The default value is `1`.

Slurm prioritizes nodes with the lowest `Weight` values
first.

###### Warning

The use of many different `Weight` values in a Slurm partition
(queue) might slow down the rate of job scheduling in the queue.

###### Note

`StaticNodePriority` is added in AWS ParallelCluster version
3.7.0.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

**`SpotPrice` (**Optional**,
`Float`)**

The maximum price that paid for an Amazon EC2 Spot Instance before any instances are
launched. The default value is the On-Demand price.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`DisableSimultaneousMultithreading` (**Optional**, `Boolean`)**

If `true`, multithreading on the nodes in the Slurm queue is
disabled. The default value is `false`.

Not all instance types can disable multithreading. For a list of instance
types that support disabling multithreading, see [CPU cores and threads for each CPU core per instance type](../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md#cpu-options-supported-instances-values "../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md#cpu-options-supported-instances-values") in the
_Amazon EC2 User Guide_.

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

**`SchedulableMemory` (**Optional**,
`Integer`)**

The amount of memory in MiB that's configured in the Slurm parameter
`RealMemory` for the compute nodes of a compute resource. This value
is the upper limit for the node memory available to jobs when [SlurmSettings](#Scheduling-v3-SlurmSettings "#Scheduling-v3-SlurmSettings") / [EnableMemoryBasedScheduling](#yaml-Scheduling-SlurmSettings-EnableMemoryBasedScheduling "#yaml-Scheduling-SlurmSettings-EnableMemoryBasedScheduling") is enabled. The default value
is 95 percent of the memory that's listed in [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types "https://aws.amazon.com/ec2/instance-types") and returned by the Amazon EC2
API [DescribeInstanceTypes](../../../AWSEC2/latest/APIReference/API_DescribeInstanceTypes.md "../../../AWSEC2/latest/APIReference/API_DescribeInstanceTypes.md"). Make sure to convert values that are given in
GiB to MiB.

Supported values: `1-EC2Memory`

`EC2Memory` is the memory (in MiB) that's listed in [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types "https://aws.amazon.com/ec2/instance-types") and
returned by the Amazon EC2 API [DescribeInstanceTypes](../../../AWSEC2/latest/APIReference/API_DescribeInstanceTypes.md "../../../AWSEC2/latest/APIReference/API_DescribeInstanceTypes.md"). Make sure to convert values that are given in
GiB to MiB.

This option is most relevant when [SlurmSettings](#Scheduling-v3-SlurmSettings "#Scheduling-v3-SlurmSettings") / [EnableMemoryBasedScheduling](#yaml-Scheduling-SlurmSettings-EnableMemoryBasedScheduling "#yaml-Scheduling-SlurmSettings-EnableMemoryBasedScheduling") is enabled. For more
information, see [Slurm memory-based scheduling](slurm-mem-based-scheduling-v3.md "slurm-mem-based-scheduling-v3.md").

###### Note

`SchedulableMemory` is supported starting with AWS ParallelCluster
version 3.2.0.

Starting with version 3.2.0, by default, AWS ParallelCluster configures
`RealMemory` for Slurm compute nodes to 95 percent of the memory
that's returned by the Amazon EC2 API `DescribeInstanceTypes`. This
configuration is independent of the value of
`EnableMemoryBasedScheduling`.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`HealthChecks` (**Optional**)**

Specify health checks on a compute resource.

`Gpu` (**Optional**)

Specify GPU health checks on a compute resource.

`Enabled` (**Optional**,
`Boolean`)

Whether AWS ParallelCluster performs GPU health checks on compute a
resource in a queue. The default is `false`.

###### Note

AWS ParallelCluster doesn't support `HealthChecks` /
`Gpu` in nodes that use `alinux2` ARM
operating systems. These platforms don't support the [NVIDIA Data Center GPU Manager (DCGM)](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/getting-started.html#supported-linux-distributions "https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/getting-started.html#supported-linux-distributions").

###### `Gpu` health check behavior

- If `Gpu` / `Enabled` is set to
  `true`, AWS ParallelCluster performs health GPU health checks
  on a compute resource.
- The `Gpu` health check performs health checks on a
  compute resource to prevent the submission of jobs on nodes with a
  degraded GPU.
- If a compute node fails a `Gpu` health check, the compute
  node state changes to `DRAIN`. New jobs don't start on this
  node. Existing jobs run to completion. After all running jobs complete,
  the compute node terminates if it's a dynamic node, and it's replaced if
  it's a static node.
- The duration of the `Gpu` health check depends on the
  selected instance type, the number of GPUs in the instance, and the
  number of `Gpu` health check targets (equivalent to the
  number of job GPU targets). For an instance with 8 GPUs, the typical
  duration is less than 3 minutes.
- If the `Gpu` health check runs on an instance that's not
  supported, it exits and the job runs on the compute node. For example,
  if an instance doesn't have a GPU, or, if an instance has a GPU, but it
  isn't an NVIDIA GPU, the health check exits and the job runs on the
  compute node. Only NVIDIA GPUs are supported.
- The `Gpu` health check uses the `dcgmi` tool
  to perform health checks on a node and takes the following steps:

When the `Gpu` health check begins in a node:

    1. It detects whether the `nvidia-dcgm` and
     `nvidia-fabricmanager` services are running.
    2. If these services aren't running, the `Gpu` health
     check starts them.
    3. It detects whether the persistence mode is enabled.
    4. If the persistence mode isn't enabled, the `Gpu`
     health check enables it.

At the end of the health check, the `Gpu` health check
restores these services and resources to their initial state.

- If the job is assigned to a specific set of node GPUs, the
  `Gpu` health check runs only on that specific set.
  Otherwise, the `Gpu` health check runs on all GPUs in the
  node.
- If a compute node receives 2 or more `Gpu` health check
  requests at the same time, only the first health check runs and the
  others are skipped. This is also the case for health checks targeting
  node GPUs. You can check the log files for additional information
  regarding this situation.
- The health check log for a specific compute node is available in the
  `/var/log/parallelcluster/slurm_health_check.log`
  file. This file is available in Amazon CloudWatch, in the cluster CloudWatch log group,
  where you can find:
  - Details on the action run by the `Gpu` health check,
    including enabling and disabling services and persistence
    mode.
  - The GPU identifier, serial ID, and the UUID.
  - The health check output.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

###### Note

`HealthChecks` is supported starting in AWS ParallelCluster version
3.6.0.

**`Efa`
(**Optional**)**

Specifies the Elastic Fabric Adapter (EFA) settings for the nodes in the
Slurm queue.

```
Efa:
  Enabled: `boolean`
  GdrSupport: `boolean`
```

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Enabled` (**Optional**,
`Boolean`)**

Specifies that Elastic Fabric Adapter (EFA) is enabled. To view the list
of Amazon EC2 instances that support EFA, see [Supported
instance types](../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types "../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types") in the _Amazon EC2 User Guide for Linux
Instances_. For more information, see [Elastic Fabric Adapter](efa-v3.md "efa-v3.md"). We recommend that you use a
cluster [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") / [Networking](#Scheduling-v3-SlurmQueues-Networking "#Scheduling-v3-SlurmQueues-Networking") / [PlacementGroup](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup") to minimize latencies between
instances.

The default value is `false`.

###### Note

Elastic Fabric Adapter (EFA) isn't supported over different
availability zones. For more information, see [SubnetIds](#yaml-Scheduling-SlurmQueues-Networking-SubnetIds "#yaml-Scheduling-SlurmQueues-Networking-SubnetIds").

###### Warning

If you're defining a custom security group in [SecurityGroups](#yaml-Scheduling-SlurmQueues-Networking-SecurityGroups "#yaml-Scheduling-SlurmQueues-Networking-SecurityGroups"), make sure that your EFA-enabled instances are
members of a security group that allows all inbound and outbound traffic
to itself.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`GdrSupport` (**Optional**,
`Boolean`)**

**(Optional)** Starting with
AWS ParallelCluster version 3.0.2, this setting has no effect. Elastic Fabric
Adapter (EFA) support for GPUDirect RDMA (remote direct memory access) is
always enabled if it's supported by the instance type for the Slurm
compute resource and the operating system.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`CapacityReservationTarget`**

```
CapacityReservationTarget:
   CapacityReservationId: `string`
   CapacityReservationResourceGroupArn: `string`
```

Specifies the on-demand capacity reservation to use for the compute
resource.

**`CapacityReservationId` (**Optional**, `String`)**

The ID of the existing capacity reservation to target for the queue's
compute resources. The id can refer to an [ODCR](../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md")
or a [Capacity Block for
ML](../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-blocks.md").

When this parameter is specified at compute resource level, InstanceType
is optional, it will be automatically retrieved from the reservation.

**`CapacityReservationResourceGroupArn` (**Optional**, `String`)**

Indicates the Amazon Resource Name (ARN) of the resource group that serves as the service
linked group of capacity reservations for the compute resource.
AWS ParallelCluster identifies and uses the most appropriate capacity
reservation from the group. The resource group must have at least one ODCR
for each instance type that's listed for the compute resource. For more
information, see [Launch instances with On-Demand Capacity Reservations (ODCR)](launch-instances-odcr-v3.md "launch-instances-odcr-v3.md").

- If `PlacementGroup` is enabled in [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") /
  [Networking](#yaml-Scheduling-SlurmQueues-ComputeResources-Networking "#yaml-Scheduling-SlurmQueues-ComputeResources-Networking") or [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") /
  [ComputeResources](#Scheduling-v3-SlurmQueues-ComputeResources "#Scheduling-v3-SlurmQueues-ComputeResources") / [Networking](#yaml-Scheduling-SlurmQueues-ComputeResources-Networking "#yaml-Scheduling-SlurmQueues-ComputeResources-Networking"), AWS ParallelCluster selects a
  resource group that targets the instance type and
  `PlacementGroup` for a compute resource if it
  exists.

The `PlacementGroup` must target one of the instances
types defined in [ComputeResources](#Scheduling-v3-SlurmQueues-ComputeResources "#Scheduling-v3-SlurmQueues-ComputeResources").

- If `PlacementGroup` isn't enabled in [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") /
  [Networking](#yaml-Scheduling-SlurmQueues-ComputeResources-Networking "#yaml-Scheduling-SlurmQueues-ComputeResources-Networking") or [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") /
  [ComputeResources](#Scheduling-v3-SlurmQueues-ComputeResources "#Scheduling-v3-SlurmQueues-ComputeResources") / [Networking](#yaml-Scheduling-SlurmQueues-ComputeResources-Networking "#yaml-Scheduling-SlurmQueues-ComputeResources-Networking"), AWS ParallelCluster selects a
  resource group that targets only the instance type of a compute
  resource, if it exists.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

###### Note

`CapacityReservationTarget` is added with AWS ParallelCluster
version 3.3.0.

**`Networking`**

```
Networking:
  PlacementGroup:
    Enabled: `boolean`
    Name: `string`
```

[Update policy: All
compute nodes must be stopped for a managed placement group deletion. The compute fleet
must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-remove-placement-group-v3 "using-pcluster-update-cluster-v3.md#update-policy-remove-placement-group-v3")

**`PlacementGroup` (**Optional**)**

Specifies the placement group settings for the compute resource.

**`Enabled` (**Optional**,
`Boolean`)**

Indicates whether a placement group is used for the compute
resource.

- If set to `true`, without a `Name`
  defined, that compute resource is assigned its own managed
  placement group, regardless of the [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") / [Networking](#Scheduling-v3-SlurmQueues-Networking "#Scheduling-v3-SlurmQueues-Networking") / [PlacementGroup](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup") setting.
- If set to `true`, with a `Name` defined,
  that compute resource is assigned the named placement group,
  regardless of `SlurmQueues` / `Networking` /
  `PlacementGroup` settings.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Name` (**Optional**,
`String`)**

The placement group name for an existing cluster placement group
that's used for the compute resource.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

###### Note

- If both `PlacementGroup` / `Enabled` and
  `Name` aren't set, their respective values default to the
  [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") / [Networking](#Scheduling-v3-SlurmQueues-Networking "#Scheduling-v3-SlurmQueues-Networking") / [PlacementGroup](#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup "#yaml-Scheduling-SlurmQueues-Networking-PlacementGroup") settings.
- `ComputeResources` / `Networking` /
  `PlacementGroup` is added with AWS ParallelCluster version
  3.3.0.

**`CustomSlurmSettings` (**Optional**,
`Dict`)**

**(Optional)** Defines the custom Slurm node
(compute resource) configuration settings.

Specifies a dictionary of custom Slurm configuration parameter key-value
pairs that apply to Slurm nodes (compute resources).

Each separate key-value pair, such as `Param1: Value1`, is added
separately to the end of the Slurm node configuration line in the format
`Param1=Value1`.

You can only specify Slurm configuration parameters that aren't deny-listed
in `CustomSlurmSettings`. For information about deny-listed Slurm
configuration parameters, see [Deny-listed Slurm configuration parameters for CustomSlurmSettings](slurm-configuration-settings-v3.md#slurm-configuration-denylists-v3 "slurm-configuration-settings-v3.md#slurm-configuration-denylists-v3").

AWS ParallelCluster only checks whether a parameter is in a deny list.
AWS ParallelCluster doesn't validate your custom Slurm configuration parameter
syntax or semantics. It is your responsibility to validate your custom Slurm
configuration parameters. Invalid custom Slurm configuration parameters can
cause Slurm daemon failures that can lead to cluster create and update
failures.

For more information about how to specify custom Slurm configuration
parameters with AWS ParallelCluster, see [Slurm configuration customization](slurm-configuration-settings-v3.md "slurm-configuration-settings-v3.md").

For more information about Slurm configuration parameters, see [slurm.conf](https://slurm.schedmd.com/slurm.conf.html "https://slurm.schedmd.com/slurm.conf.html") in the
Slurm documentation.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

###### Note

`CustomSlurmSettings` is supported starting with
AWS ParallelCluster version 3.6.0.

**`Tags` (**Optional**, [String])**

A list of tag key-value pairs. `ComputeResource` tags override
duplicate tags specified in the [Tags section](Tags-v3.md "Tags-v3.md")
or [SlurmQueues](#yaml-Scheduling-SlurmQueues-Tags "#yaml-Scheduling-SlurmQueues-Tags") / `Tags`.

**`Key` (**Optional**,
`String`)**

The tag key.

**`Value` (**Optional**,
`String`)**

The tag value.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

#### `ComputeSettings`

**(Required)** Defines the `ComputeSettings`
configuration for the Slurm queue.

##### `ComputeSettings` properties

Specifies the properties of `ComputeSettings` of the nodes in the Slurm
queue.

```
ComputeSettings:
  LocalStorage:
    RootVolume:
      Size: `integer`
      Encrypted: `boolean`
      VolumeType: `string`
      Iops: `integer`
      Throughput: `integer`
     EphemeralVolume:
      MountDir: `string`
```

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`LocalStorage` (**Optional**)**

Specifies the properties of `LocalStorage` of the nodes in the
Slurm queue.

```
LocalStorage:
  RootVolume:
    Size: `integer`
    Encrypted: `boolean`
    VolumeType: `string`
    Iops: `integer`
    Throughput: `integer`
  EphemeralVolume:
    MountDir: `string`
```

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`RootVolume` (**Optional**)**

Specifies the details of the root volume of the nodes in the Slurm
queue.

```
RootVolume:
  Size: `integer`
  Encrypted: `boolean`
  VolumeType: `string`
  Iops: `integer`
  Throughput: `integer`
```

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Size` (**Optional**,
`Integer`)**

Specifies the root volume size in gibibytes (GiB) for the nodes in
the Slurm queue. The default size comes from the AMI. Using a
different size requires that the AMI supports `growroot`.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Encrypted` (**Optional**,
`Boolean`)**

If `true`, the root volume of the nodes in the Slurm
queue are encrypted. The default value is `false`.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`VolumeType` (**Optional**,
`String`)**

Specifies the [Amazon EBS volume
type](../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md "../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md") of the nodes in the Slurm queue. Supported values are
`gp2`, `gp3`, `io1`,
`io2`, `sc1`, `st1`, and
`standard`. The default value is `gp3`.

For more information, see [Amazon EBS volume
types](../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md "../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md") in the _Amazon EC2 User Guide_.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Iops` (**Optional**,
`Boolean`)**

Defines the number of IOPS for `io1`, `io2`,
and `gp3` type volumes.

The default value, supported values, and `volume_iops`
to `volume_size` ratio varies by `VolumeType`
and `Size`.

**`VolumeType` = `io1`**

Default `Iops` = 100

Supported values `Iops` = 100–64000
†

Maximum `volume_iops` to `volume_size`
ratio = 50 IOPS per GiB. 5000 IOPS requires a
`volume_size` of at least 100 GiB.

**`VolumeType` = `io2`**

Default `Iops` = 100

Supported values `Iops` = 100–64000 (256000
for `io2` Block Express volumes) †

Maximum `Iops` to `Size` ratio = 500
IOPS per GiB. 5000 IOPS requires a `Size` of at least
10 GiB.

**`VolumeType` = `gp3`**

Default `Iops` = 3000

Supported values `Iops` = 3000–16000
†

Maximum `Iops` to `Size` ratio = 500
IOPS per GiB for volumes with IOPS greater than 3000.

† Maximum IOPS is guaranteed only on [Instances built on the Nitro System](../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances "../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances") that are also
provisioned with more than 32,000 IOPS. Other instances can have up to
32,000 IOPS. Earlier `io1` volumes might not reach full
performance unless you [modify the
volume](../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md "../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md"). `io2` Block Express volumes support
`volume_iops` values up to 256000 on `R5b`
instance types. For more information, see [`io2` Block Express volumes](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md#io2-block-express "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md#io2-block-express") in the
_Amazon EC2 User Guide_.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Throughput` (**Optional**,
`Integer`)**

Defines the throughput for `gp3` volume types, in
MiB/s. This setting is valid only when `VolumeType` is
`gp3`. The default value is `125`. Supported
values: 125–1000 MiB/s

The ratio of `Throughput` to `Iops` can be
no more than 0.25. The maximum throughput of 1000 MiB/s requires that
the `Iops` setting is at least 4000.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`EphemeralVolume` (**Optional**,
`Boolean`)**

Specifies the settings for the ephemeral volume. The ephemeral volume is
created by combining all instance store volumes into a single logical volume
formatted with the `ext4` file system. The default is
`/scratch`. If the instance type doesn't have any instance
store volumes, no ephemeral volume is created. For more information, see
[Instance store volumes](../../../AWSEC2/latest/UserGuide/InstanceStorage.md#instance-store-volumes "../../../AWSEC2/latest/UserGuide/InstanceStorage.md#instance-store-volumes") in the
_Amazon EC2 User Guide_.

```
EphemeralVolume:
  MountDir: `string`
```

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`MountDir` (**Optional**,
`String`)**

The mount directory for the ephemeral volume for each node in the
Slurm queue.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

#### `CustomActions`

**(Optional)** Specifies custom scripts to run on the
nodes in the Slurm queue.

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
```

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

##### `CustomActions` Properties

**`OnNodeStart` (**Optional**,
`String`)**

Specifies a sequence of scripts or single script to run on the nodes in the
Slurm queue before any node deployment bootstrap action is started.
AWS ParallelCluster doesn't support including both a single script and
`Sequence` for the same custom action. For more information, see
[Custom bootstrap actions](custom-bootstrap-actions-v3.md "custom-bootstrap-actions-v3.md").

**`Sequence` (**Optional**)**

List of scripts to run.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Script` (**Required**,
`String`)**

The file to use. The file path can start with
`https://` or `s3://`.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Args` (**Optional**,
`[String]`)**

The list of arguments to pass to the script.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Script` (**Required**,
`String`)**

The file to use for a single script. The file path can start with
`https://` or `s3://`.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Args` (**Optional**,
`[String]`)**

The list of arguments to pass to the single script.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`OnNodeConfigured` (**Optional**,
`String`)**

Specifies a sequence of scripts or a single script to run on the nodes in the
Slurm queue after all of the node bootstrap actions are complete.
AWS ParallelCluster doesn't support including both a single script and
`Sequence` for the same custom action. For more information, see
[Custom bootstrap actions](custom-bootstrap-actions-v3.md "custom-bootstrap-actions-v3.md").

**`Sequence` (**Optional**)**

List of scripts to run.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Script` (**Required**,
`String`)**

The file to use. The file path can start with
`https://` or `s3://`.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Args` (**Optional**,
`[String]`)**

The list of arguments to pass to the script.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Script` (**Required**,
`String`)**

The file to use for a single script. The file path can start with
`https://`or `s3://`.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

**`Args` (**Optional**,
`[String]`)**

A list of arguments to pass to the single script.

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

[Update policy: The
compute fleet must be stopped or QueueUpdateStrategy must be set for this setting to be changed
for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

###### Note

`Sequence` is added starting with AWS ParallelCluster version
3.6.0. When you specify `Sequence`, you can list multiple scripts for
a custom action. AWS ParallelCluster continues to support configuring a custom
action with a single script, without including `Sequence`.

AWS ParallelCluster doesn't support including both a single script and
`Sequence` for the same custom action.

#### `Iam`

**(Optional)** Defines optional IAM settings for the
Slurm queue.

```
Iam:
  S3Access:
    - BucketName: `string`
      EnableWriteAccess: `boolean`
      KeyName: `string`
  AdditionalIamPolicies:
    - Policy: `string`
  InstanceProfile: `string`
  InstanceRole: `string`
```

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

##### `Iam`

Properties

**`InstanceProfile` (**Optional**,
`String`)**

Specifies an instance profile to override the default instance role or
instance profile for the Slurm queue. You cannot specify both
`InstanceProfile` and `InstanceRole`. The format is
`arn:${Partition}:iam::${Account}:instance-profile/${InstanceProfileName}`.

If this is specified, the `S3Access` and
`AdditionalIamPolicies` settings can't be specified.

We recommend that you specify one or both of the `S3Access` and
`AdditionalIamPolicies` settings because features added to
AWS ParallelCluster often require new permissions.

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

**`InstanceRole` (**Optional**,
`String`)**

Specifies an instance role to override the default instance role or instance
profile for the Slurm queue. You cannot specify both
`InstanceProfile` and `InstanceRole`. The format is
`arn:${Partition}:iam::${Account}:role/${RoleName}`.

If this is specified, the `S3Access` and
`AdditionalIamPolicies` settings can't be specified.

We recommend that you specify one or both of the `S3Access` and
`AdditionalIamPolicies` settings because features added to
AWS ParallelCluster often require new permissions.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

**`S3Access`
(**Optional**)**

Specifies a bucket for the Slurm queue. This is used to generate policies to
grant the specified access to the bucket in the Slurm queue.

If this is specified, the `InstanceProfile` and
`InstanceRole` settings can't be specified.

We recommend that you specify one or both of the `S3Access` and
`AdditionalIamPolicies` settings because features added to
AWS ParallelCluster often require new permissions.

```
S3Access:
  - BucketName: `string`
    EnableWriteAccess: `boolean`
    KeyName: `string`
```

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

**`BucketName` (**Required**,
`String`)**

The name of the bucket.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

**`KeyName` (**Optional**,
`String`)**

The key for the bucket. The default value is `*`.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

**`EnableWriteAccess` (**Optional**,
`Boolean`)**

Indicates whether write access is enabled for the bucket.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

**`AdditionalIamPolicies` (**Optional**)**

Specifies a list of Amazon Resource Names (ARNs) of IAM policies for Amazon EC2 .
This list is attached to the root role used for the Slurm queue in addition to
the permissions that are required by AWS ParallelCluster.

An IAM policy name and its ARN are different. Names can't be used.

If this is specified, the `InstanceProfile` and
`InstanceRole` settings can't be specified.

We recommend that you use `AdditionalIamPolicies` because
`AdditionalIamPolicies` are added to the permissions that
AWS ParallelCluster requires, and the `InstanceRole` must include all
permissions required. The permissions required often change from release to
release as features are added.

There's no default value.

```
AdditionalIamPolicies:
  - Policy: `string`
```

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

**`Policy` (**Required**,
`[String]`)**

List of IAM policies.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

## `SlurmSettings`

**(Optional)** Defines the settings for Slurm that apply to
the entire cluster.

```
SlurmSettings:
  ScaledownIdletime: `integer`
  QueueUpdateStrategy: `string`
  EnableMemoryBasedScheduling: `boolean`
  CustomSlurmSettings: `[dict]`
  CustomSlurmSettingsIncludeFile: `string`
  Database:
    Uri: `string`
    UserName: `string`
    PasswordSecretArn: `string`
  ExternalSlurmdbd:
    Host: `string`
    Port: `integer`
  Dns:
    DisableManagedDns: `boolean`
    HostedZoneId: `string`
    UseEc2Hostnames: `boolean`
```

### `SlurmSettings`

Properties

**`ScaledownIdletime` (**Optional**,
`Integer`)**

Defines the amount of time (in minutes) that there's no job and the Slurm node
terminates.

The default value is `10`.

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

**`MungeKeySecretArn` (**Optional**,
`String`)**

The Amazon Resource Name (ARN) of the plaintext AWS Secrets Manager secret that
contains the base64-encoded munge key to be used in the Slurm cluster. This munge key
will be used to authenticate RPC calls between Slurm client commands and Slurm daemons
acting as remote servers. If MungeKeySecretArn is not provided, AWS ParallelCluster will
generate a random munge key for the cluster.

###### Note

`MungeKeySecretArn` is supported starting with AWS ParallelCluster
version 3.8.0.

###### Warning

If the MungeKeySecretArn is newly added to an existing cluster, ParallelCluster
will not restore the previous munge Key in the event of a Rollback or when later
removing the MungeKeySecretArn. Instead, a new random munge key will be
generated.

If the AWS ParallelCluster user has the permission to [DescribeSecret](../../../secretsmanager/latest/apireference/API_DescribeSecret.md "../../../secretsmanager/latest/apireference/API_DescribeSecret.md") on that specific secret resource, MungeKeySecretArn is
validated. MungeKeySecretArn is valid if:

- The specified secret exists, and
- The secret is plaintext and contains a valid base64-encoded string, and
- The decoded binary munge key has a size between 256 and 8192 bits.

If the pcluster user IAM policy doesn't include DescribeSecret, MungeKeySecretArn
is not validated and a warning message is displayed. For more information, see [Base AWS ParallelCluster pcluster user policy](iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-base-user-policy "iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-base-user-policy").

When you update MungeKeySecretArn, the compute fleet and all login nodes must be
stopped.

If the secret value in the secret ARN is modified while the ARN remains the same,
the cluster won't automatically be updated with the new munge key. In order to use the
secret ARN's new munge key, you must stop the compute fleet and login nodes then run
the following command from the head node.

`sudo /opt/parallelcluster/scripts/slurm/update_munge_key.sh`

After you run the command, you can resume both the compute fleet and login nodes:
the newly provisioned compute and login nodes will automatically start using the new
munge key.

To generate a base64-encoded custom munge key, you can use the [mungekey utility](https://github.com/dun/munge/wiki/Man-8-mungekey "https://github.com/dun/munge/wiki/Man-8-mungekey")
distributed with the munge software and then encode it using the base64 utility
generally available in your OS. Alternatively, you either use bash (please set the bs
parameter between 32 and 1024)

`dd if=/dev/random bs=128 count=1 2>/dev/null | base64 -w 0`

or Python as follows:

```
import random
import os
import base64

# key length in bytes
key_length=128

base64.b64encode(os.urandom(key_length)).decode("utf-8")
```

[Update Policy: The compute fleet and
login nodes must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md "using-pcluster-update-cluster-v3.md")

**`QueueUpdateStrategy` (**Optional**,
`String`)**

Specifies the replacement strategy for the [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues")
section parameters that have the following update policy:

[Update policy: The compute
fleet must be stopped or QueueUpdateStrategy must be set for this
setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3 "using-pcluster-update-cluster-v3.md#update-policy-queue-update-strategy-v3")

The `QueueUpdateStrategy` value is used only when a cluster update
process starts.

Valid values: `COMPUTE_FLEET_STOP` | `DRAIN` |
`TERMINATE`

Default value: `COMPUTE_FLEET_STOP`

**`DRAIN`**

Nodes in queues with changed parameter values are set to
`DRAINING`. Nodes in this state don't accept new jobs and running
jobs continue to completion.

After a node becomes `idle` (`DRAINED`), a node is
replaced if the node is static, and the node is terminated if the node is
dynamic. Other nodes in other queues without changed parameter values aren't
impacted.

The time this strategy needs to replace all of the queue nodes with changed
parameter values depends on the running workload.

**`COMPUTE_FLEET_STOP`**

The default value of the `QueueUpdateStrategy` parameter. With
this setting, updating parameters under the [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") section requires you to [stop
the compute fleet](pcluster.md "pcluster.md") before you perform a cluster update:

```
`$` `pcluster update-compute-fleet --status STOP_REQUESTED`
```

**`TERMINATE`**

In queues with changed parameter values, running jobs are terminated and the
nodes are powered down immediately.

Static nodes are replaced and dynamic nodes are terminated.

Other nodes in other queues without changed parameter values aren't
impacted.

[Update policy: This
setting is not analyzed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-ignored-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-ignored-v3")

###### Note

`QueueUpdateStrategy` is supported starting with AWS ParallelCluster
version 3.2.0.

**`EnableMemoryBasedScheduling` (**Optional**,
`Boolean`)**

If `true`, memory-based scheduling is enabled in Slurm.
For more information, see [SlurmQueues](#Scheduling-v3-SlurmQueues "#Scheduling-v3-SlurmQueues") / [ComputeResources](#Scheduling-v3-SlurmQueues-ComputeResources "#Scheduling-v3-SlurmQueues-ComputeResources") / [SchedulableMemory](#yaml-Scheduling-SlurmQueues-ComputeResources-SchedulableMemory "#yaml-Scheduling-SlurmQueues-ComputeResources-SchedulableMemory").

The default value is `false`.

###### Warning

Enabling memory-based scheduling impacts the way that the Slurm
scheduler handles jobs and node allocation.

For more information, see [Slurm memory-based scheduling](slurm-mem-based-scheduling-v3.md "slurm-mem-based-scheduling-v3.md").

###### Note

`EnableMemoryBasedScheduling` is supported starting with
AWS ParallelCluster version 3.2.0.

###### Note

Starting with AWS ParallelCluster version 3.7.0,
`EnableMemoryBasedScheduling` can be enabled if you configure multiple
instance types in [Instances](#yaml-Scheduling-SlurmQueues-ComputeResources-Instances "#yaml-Scheduling-SlurmQueues-ComputeResources-Instances").

For AWS ParallelCluster versions 3.2.0 to 3.6.`x`,
`EnableMemoryBasedScheduling` can't be enabled if you configure
multiple instance types in [Instances](#yaml-Scheduling-SlurmQueues-ComputeResources-Instances "#yaml-Scheduling-SlurmQueues-ComputeResources-Instances").

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

**`CustomSlurmSettings` (**Optional**,
`[Dict]`)**

Defines the custom Slurm settings that apply to the entire cluster.

Specifies a list of Slurm configuration dictionaries of key-value pairs to be
appended to the end of the `slurm.conf` file that AWS ParallelCluster
generates.

Each dictionary in the list appears as a separate line added to the Slurm
configuration file. You can specify either simple or complex parameters.

Simple parameters consist of a single key pair, as shown in the following
examples:

```
 - Param1: 100
 - Param2: "SubParam1,SubParam2=SubValue2"
```

Example rendered in Slurm configuration:

```
Param1=100
Param2=SubParam1,SubParam2=SubValue2
```

Complex Slurm configuration parameters consist of multiple space-separated
key-value, pairs as shown in the next examples:

```
 - NodeName: test-nodes[1-10]
   CPUs: 4
   RealMemory: 4196
   ... # other node settings
 - NodeSet: test-nodeset
   Nodes: test-nodes[1-10]
   ... # other nodeset settings
 - PartitionName: test-partition
   Nodes: test-nodeset
   ... # other partition settings

```

Example, rendered in Slurm configuration:

```
NodeName=test-nodes[1-10] CPUs=4 RealMemory=4196 ... # other node settings
NodeSet=test-nodeset Nodes=test-nodes[1-10] ... # other nodeset settings
PartitionName=test-partition Nodes=test-nodeset ... # other partition settings
```

###### Note

Custom Slurm nodes must not contain the `-st-` or `-dy-`
patterns in their names. These patterns are reserved for nodes managed by
AWS ParallelCluster.

If you specify custom Slurm configuration parameters in
`CustomSlurmSettings`, you must not specify custom Slurm configuration
parameters for `CustomSlurmSettingsIncludeFile`.

You can only specify Slurm configuration parameters that aren't deny-listed in
`CustomSlurmSettings`. For information about deny-listed Slurm
configuration parameters, see [Deny-listed Slurm configuration parameters for CustomSlurmSettings](slurm-configuration-settings-v3.md#slurm-configuration-denylists-v3 "slurm-configuration-settings-v3.md#slurm-configuration-denylists-v3").

AWS ParallelCluster only checks whether a parameter is in a deny list.
AWS ParallelCluster doesn't validate your custom Slurm configuration parameter syntax
or semantics. It is your responsibility to validate your custom Slurm configuration
parameters. Invalid custom Slurm configuration parameters can cause Slurm daemon
failures that can lead to cluster create and update failures.

For more information about how to specify custom Slurm configuration parameters
with AWS ParallelCluster, see [Slurm configuration customization](slurm-configuration-settings-v3.md "slurm-configuration-settings-v3.md").

For more information about Slurm configuration parameters, see [slurm.conf](https://slurm.schedmd.com/slurm.conf.html "https://slurm.schedmd.com/slurm.conf.html") in the Slurm
documentation.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

###### Note

`CustomSlurmSettings` is supported starting with AWS ParallelCluster
version 3.6.0.

**`CustomSlurmSettingsIncludeFile` (**Optional**, `String`)**

Defines the custom Slurm settings that apply to the entire cluster.

Specifies the custom Slurm file consisting of custom Slurm configuration
parameters to be appended at the end of the `slurm.conf` file that
AWS ParallelCluster generates.

You must include the path to the file. The path can start with
`https://` or `s3://`.

If you specify custom Slurm configuration parameters for
`CustomSlurmSettingsIncludeFile`, you must not specify custom Slurm
configuration parameters for `CustomSlurmSettings`.

###### Note

Custom Slurm nodes must not contain the `-st-` or `-dy-`
patterns in their names. These patterns are reserved for nodes managed by
AWS ParallelCluster.

You can only specify Slurm configuration parameters that aren't deny-listed in
`CustomSlurmSettingsIncludeFile`. For information about deny-listed
Slurm configuration parameters, see [Deny-listed Slurm configuration parameters for CustomSlurmSettings](slurm-configuration-settings-v3.md#slurm-configuration-denylists-v3 "slurm-configuration-settings-v3.md#slurm-configuration-denylists-v3").

AWS ParallelCluster only checks whether a parameter is in a deny list.
AWS ParallelCluster doesn't validate your custom Slurm configuration parameter syntax
or semantics. It is your responsibility to validate your custom Slurm configuration
parameters. Invalid custom Slurm configuration parameters can cause Slurm daemon
failures that can lead to cluster create and update failures.

For more information about how to specify custom Slurm configuration parameters
with AWS ParallelCluster, see [Slurm configuration customization](slurm-configuration-settings-v3.md "slurm-configuration-settings-v3.md").

For more information about Slurm configuration parameters, see [slurm.conf](https://slurm.schedmd.com/slurm.conf.html "https://slurm.schedmd.com/slurm.conf.html") in the Slurm
documentation.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

###### Note

`CustomSlurmSettings` is supported starting with AWS ParallelCluster
version 3.6.0.

### `Database`

**(Optional)** Defines the settings to enable
Slurm Accounting on the cluster. For more information, see [Slurm accounting with AWS ParallelCluster](slurm-accounting-v3.md "slurm-accounting-v3.md").

```
Database:
   Uri: `string`
   UserName: `string`
   PasswordSecretArn: `string`
```

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

#### `Database`

properties

**`Uri`
(**Required**, `String`)**

The address to the database server that's used as the backend for Slurm
accounting. This URI must be formatted as `host:port` and must not
contain a scheme, such as `mysql://`. The host can either be an IP
address or a DNS name that's resolvable by the head node. If a port isn't provided,
AWS ParallelCluster uses the MySQL default port 3306.

AWS ParallelCluster bootstraps the Slurm accounting database to the cluster and
must access the database.

The database must be reachable before the following occurs:

- A cluster is created.
- Slurm accounting is enabled with a cluster update.

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

**`UserName` (**Required**,
`String`)**

The identity that Slurm uses to connect to the database, write accounting
logs, and perform queries. The user must have both read and write permissions on the
database.

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

**`PasswordSecretArn` (**Required**,
`String`)**

The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that
contains the `UserName` plaintext password. This password is used
together with `UserName` and Slurm accounting to authenticate on the
database server.

###### Note

- When you create a secret using the AWS Secrets Manager console be
  sure to select "Other type of secret", select plaintext, and only include the
  password text in the secret.
- You cannot use the '#' character in the Database password as Slurm does not
  support it in slurmdbd.conf.
- For more information on how to use AWS Secrets Manager to create a secret
  refer to [Create an AWS Secrets Manager Secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md").

If the user has the permission to [DescribeSecret](../../../secretsmanager/latest/apireference/API_DescribeSecret.md "../../../secretsmanager/latest/apireference/API_DescribeSecret.md"), `PasswordSecretArn` is validated.
`PasswordSecretArn` is valid if the specified secret exists. If the
user IAM policy doesn't include `DescribeSecret`,
`PasswordSecretArn` isn't validated and a warning message is displayed.
For more information, see [Base AWS ParallelCluster pcluster user policy](iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-base-user-policy "iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-base-user-policy").

When you update `PasswordSecretArn`, the compute fleet must be
stopped. If the secret value changes, and the secret ARN doesn't change, the cluster
isn't automatically updated with the new database password. To update the cluster
for the new secret value, you must run the following command from within the head
node after the compute fleet is stopped.

```
`$` sudo /opt/parallelcluster/scripts/slurm/update_slurm_database_password.sh
```

###### Warning

We recommend that you only change the database password when the compute fleet
is stopped to avoid loss of accounting data.

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

**`DatabaseName` (**Optional**,
`String`)**

Name of the database on the database server (defined by the Uri parameter) to be
used for Slurm Accounting.

The name of the database may contain lowercase letters, numbers and underscores.
The name may not be longer than 64 characters.

This parameter maps to the `StorageLoc` parameter of [slurmdbd.conf](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_StorageLoc "https://slurm.schedmd.com/slurmdbd.conf.html#OPT_StorageLoc").

If `DatabaseName` is not provided, ParallelCluster will use the name
of the cluster to define a value for `StorageLoc`.

Updating the `DatabaseName` is allowed, with the following
considerations:

- If a database with a name DatabaseName does not yet exist on the database
  server, slurmdbd will create it. It will be your responsibility to reconfigure
  the new database as needed (e.g. adding the accounting entities — clusters,
  accounts, users, associations, QOSs, etc.).
- If a database with a name DatabaseName already exists on the database
  server, slurmdbd will use it for the Slurm Accounting functionality.

[Update policy: The compute
fleet must be stopped for this setting to be changed for an update.](using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3 "using-pcluster-update-cluster-v3.md#update-policy-compute-fleet-v3")

###### Note

`Database` is added starting with release 3.3.0.

### ExternalSlurmdbd

**(Optional)** Defines the settings to enable Slurm Accounting
with an external slurmdbd server. For more information, see [Slurm accounting with AWS ParallelCluster](slurm-accounting-v3.md "slurm-accounting-v3.md").

```
ExternalSlurmdbd:
  Host: `string`
  Port: `integer`
```

#### `ExternalSlurmdbd`

properties

**`Host` (**Required**, `String`)**

The address to the external slurmdbd server for Slurm accounting. The host can either be an IP address or a DNS name that's resolvable by the head node.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

**`Port` (**Optional**,
`Integer`)**

The port the slurmdbd service listens to. The default value is `6819`.

[Update policy: This
setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3 "using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3")

### `Dns`

**(Optional)** Defines the settings for Slurm that apply
to the entire cluster.

```
Dns:
  DisableManagedDns: `boolean`
  HostedZoneId: `string`
  UseEc2Hostnames: `boolean`
```

#### `Dns`

properties

**`DisableManagedDns` (**Optional**,
`Boolean`)**

If `true`, the DNS entries for the cluster aren't created and Slurm
node names aren't resolvable.

By default, AWS ParallelCluster creates a Route 53 hosted zone where nodes are
registered when launched. The default value is `false`. If
`DisableManagedDns` is set to `true`, the hosted zone isn't
created by AWS ParallelCluster.

To learn how to use this setting to deploy clusters in subnets with no internet
access, see [AWS ParallelCluster in a single subnet with no internet
access](aws-parallelcluster-in-a-single-public-subnet-no-internet-v3.md "aws-parallelcluster-in-a-single-public-subnet-no-internet-v3.md").

###### Warning

A name resolution system is required for the cluster to operate properly. If
`DisableManagedDns` is set to `true`, you must provide a
name resolution system. To use the Amazon EC2 default DNS, set
`UseEc2Hostnames` to `true`. Alternatively, configure your
own DNS resolver and make sure that node names are registered when instances are
launched. For example, you can do this by configuring [CustomActions](#Scheduling-v3-SlurmQueues-CustomActions "#Scheduling-v3-SlurmQueues-CustomActions") / [OnNodeStart](#yaml-Scheduling-SlurmQueues-CustomActions-OnNodeStart "#yaml-Scheduling-SlurmQueues-CustomActions-OnNodeStart").

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

**`HostedZoneId` (**Optional**,
`String`)**

Defines a custom Route 53 hosted zone ID to use for DNS name resolution for the
cluster. When provided, AWS ParallelCluster registers cluster nodes in the specified
hosted zone and doesn't create a managed hosted zone.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")

**`UseEc2Hostnames` (**Optional**,
`Boolean`)**

If `true`, cluster compute nodes are configured with the default EC2
hostname. The Slurm `NodeHostName` is also updated with this
information. The default is `false`.

To learn how to use this setting to deploy clusters in subnets with no internet
access, see [AWS ParallelCluster in a single subnet with no internet
access](aws-parallelcluster-in-a-single-public-subnet-no-internet-v3.md "aws-parallelcluster-in-a-single-public-subnet-no-internet-v3.md").

###### Note

**This note isn't relevant starting with AWS ParallelCluster
version 3.3.0.**

For AWS ParallelCluster supported versions prior to 3.3.0:

When `UseEc2Hostnames` is set to `true`, the Slurm
configuration file is set with the AWS ParallelCluster `prolog` and
`epilog` scripts:

- `prolog` runs to add nodes info to `/etc/hosts` on
  compute nodes when each job is allocated.
- `epilog` runs to clean contents written by
  `prolog`.
  To add custom `prolog` or `epilog` scripts, add them to
  the `/opt/slurm/etc/pcluster/prolog.d/` or
  `/opt/slurm/etc/pcluster/epilog.d/` folders respectively.

[Update policy: If this setting is
changed, the update is not allowed.](using-pcluster-update-cluster-v3.md#update-policy-fail-v3 "using-pcluster-update-cluster-v3.md#update-policy-fail-v3")
