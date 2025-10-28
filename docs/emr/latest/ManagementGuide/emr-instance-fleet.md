# Planning and configuring instance fleets for your Amazon EMR cluster

###### Note

The instance fleets configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.0 and 5.0.3.

The instance fleet configuration for Amazon EMR clusters lets you select a wide
variety of provisioning options for Amazon EC2 instances, and helps you develop a
flexible and elastic resourcing strategy for each node type in your cluster.

In an instance fleet configuration, you specify a _target
capacity_ for [On-Demand
Instances](../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md "../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md") and [Spot
Instances](../../../AWSEC2/latest/UserGuide/using-spot-instances.md "../../../AWSEC2/latest/UserGuide/using-spot-instances.md") within each fleet. When the cluster launches, Amazon EMR
provisions instances until the targets are fulfilled. When Amazon EC2 reclaims a Spot
Instance in a running cluster because of a price increase or instance failure,
Amazon EMR tries to replace the instance with any of the instance types that you
specify. This makes it easier to regain capacity during a spike in Spot pricing.

You can specify a maximum of five Amazon EC2 instance types per fleet for Amazon EMR to
use when fulfilling the targets, or a maximum of 30 Amazon EC2 instance types per
fleet when you create a cluster using the AWS CLI or Amazon EMR API and an [allocation strategy](#emr-instance-fleet-allocation-strategy "#emr-instance-fleet-allocation-strategy")
for On-Demand and Spot Instances.

You can also select multiple subnets for different Availability Zones. When Amazon EMR
launches the cluster, it looks across those subnets to find the instances and
purchasing options you specify. If Amazon EMR detects an AWS large-scale event in
one or more of the Availability Zones, Amazon EMR automatically attempts to route traffic
away from the impacted Availability Zones and tries to launch new clusters that you
create in alternate Availability Zones according to your selections. Note that cluster
Availability Zone selection happens only at cluster creation. Existing cluster nodes are
not automatically re-launched in a new Availability Zone in the event of an Availability Zone
outage.

## **Considerations for working with instance fleets**

Consider the following items when you use instance fleets with
Amazon EMR.

- You can have one instance fleet, and only one, per node type
  (primary, core, task). You can specify up to five Amazon EC2 instance
  types for each fleet on the AWS Management Console (or a maximum of 30 types per
  instance fleet when you create a cluster using the AWS CLI or Amazon EMR
  API and an [Allocation strategy for instance
  fleets](#emr-instance-fleet-allocation-strategy "#emr-instance-fleet-allocation-strategy")).
- Amazon EMR chooses any or all of the specified Amazon EC2 instance types to
  provision with both Spot and On-Demand purchasing options.
- You can establish target capacities for Spot and On-Demand
  Instances for the core fleet and task fleet. Use vCPU or a generic
  unit assigned to each Amazon EC2 instance that counts toward the targets.
  Amazon EMR provisions instances until each target capacity is totally
  fulfilled. For the primary fleet, the target is always one.
- You can choose one subnet (Availability Zone) or a range. If you choose a
  range, Amazon EMR provisions capacity in the Availability Zone that is the best
  fit.
- When you specify a target capacity for Spot Instances:
  - For each instance type, specify a maximum Spot price.
    Amazon EMR provisions Spot Instances if the Spot price is below
    the maximum Spot price. You pay the Spot price, not
    necessarily the maximum Spot price.
  - For each fleet, define a timeout period for provisioning
    Spot Instances. If Amazon EMR can't provision Spot capacity, you
    can terminate the cluster or switch to provisioning
    On-Demand capacity instead. This only applies for
    provisioning clusters, not resizing them. If the timeout
    period ends during the cluster resizing process,
    unprovisioned Spot requests will be nullified without
    transferring to On-Demand capacity.

- For each fleet, you can specify one of the following allocation
  strategies for your Spot Instances: price-capacity optimized,
  capacity-optimized, capacity-optimized-prioritized, lowest-price, or diversified across all
  pools.
- For each fleet, you can apply the following allocation strategies for
  your On-Demand Instances: the lowest-price strategy or the prioritized strategy.
- For each fleet with On-Demand Instances, you can choose to apply capacity
  reservation options.
- If you use allocation strategy for instance fleets, the following considerations apply when you choose subnets for your EMR cluster:
  - When Amazon EMR provisions a cluster with a task fleet, it filters out subnets that lack enough available IP addresses to
    provision all instances of the requested EMR cluster. This includes IP addresses required for the primary, core, and task instance fleets
    during cluster launch. Amazon EMR then leverages its allocation strategy to determine the instance pool, based on instance type and remaining
    subnets with sufficient IP addresses, to launch the cluster.
  - If Amazon EMR cannot launch the whole cluster due to insufficient available IP addresses, it will attempt to identify subnets with enough
    free IP addresses to launch the essential (core and primary) instance fleets. In such scenarios, your task instance fleet will go into a suspended
    state, rather than terminating the cluster with an error.
  - If none of the specified subnets contain enough IP addresses to provision the essential core and primary instance fleets, the cluster
    launch will fail with a **VALIDATION_ERROR**. This triggers a **CRITICAL** severity cluster termination
    event, notifying you that the cluster cannot be launched. To prevent this issue, we recommend increasing the number of IP addresses in your subnets.

- If you run Amazon EMR release **emr-7.7.0** and above, and you use allocation strategy for instance fleets, you can
  scale the cluster up to 4000 EC2 instances and 14000 EBS volumes per instance fleet. For release versions below **emr-7.7.0**, the cluster
  can be scaled up only to 2000 EC2 instances and 7000 EBS volumes per instance fleet.
- When you launch On-Demand Instances, you can use open or targeted capacity reservations for primary, core, and task nodes
  in your accounts. You might see insufficient capacity with On-Demand Instances with allocation strategy for instance fleets. We
  recommend that you specify multiple instance types to diversify and reduce the chance of experiencing insufficient capacity.
  For more information, see [Use capacity reservations with
  instance fleets in Amazon EMR](on-demand-capacity-reservations.md "on-demand-capacity-reservations.md").

## Instance fleet options

Use the following guidelines to understand instance fleet options.

###### Topics

- [Setting
  target capacities](#emr-fleet-capacity "#emr-fleet-capacity")
- [Launch
  options](#emr-fleet-spot-options "#emr-fleet-spot-options")
- [Multiple subnet (Availability Zones) options](#emr-multiple-subnet-options "#emr-multiple-subnet-options")
- [Master node configuration](#emr-master-node-configuration "#emr-master-node-configuration")

### \*\*Setting

target capacities\*\*

Specify the target capacities you want for the core fleet and task
fleet. When you do, that determines the number of On-Demand Instances
and Spot Instances that Amazon EMR provisions. When you specify an instance,
you decide how much each instance counts toward the target. When an
On-Demand Instance is provisioned, it counts toward the On-Demand
target. The same is true for Spot Instances. Unlike core and task
fleets, the primary fleet is always one instance. Therefore, the target
capacity for this fleet is always one.

When you use the console, the vCPUs of the Amazon EC2 instance type are
used as the count for target capacities by default. You can change this
to **Generic units**, and then specify the count for
each EC2 instance type. When you use the AWS CLI, you manually assign
generic units for each instance type.

###### Important

When you choose an instance type using the AWS Management Console, the number of **vCPU** shown for each **Instance type** is the number of YARN vcores for that instance type, not the number of EC2 vCPUs for that instance type. For more information on the number of vCPUs for each instance type, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

For each fleet, you specify up to five Amazon EC2 instance types. If you
use an [Allocation strategy for instance
fleets](#emr-instance-fleet-allocation-strategy "#emr-instance-fleet-allocation-strategy") and create
a cluster using the AWS CLI or the Amazon EMR API, you can specify up to 30 EC2
instance types per instance fleet. Amazon EMR chooses any combination of
these EC2 instance types to fulfill your target capacities. Because
Amazon EMR wants to fill target capacity completely, an overage might happen.
For example, if there are two unfulfilled units, and Amazon EMR can only
provision an instance with a count of five units, the instance still
gets provisioned, meaning that the target capacity is exceeded by three
units.

If you reduce the target capacity to resize a running cluster, Amazon EMR
attempts to complete application tasks and terminates instances to meet
the new target. For more information, see [Terminate at task completion](emr-scaledown-behavior.md#emr-scaledown-terminate-task "emr-scaledown-behavior.md#emr-scaledown-terminate-task").

### \*\*Launch

options\*\*

For Spot Instances, you can specify a **Maximum Spot
price** for each instance type in a fleet. You can set this
price either as a percentage of the On-Demand price, or as a specific
dollar amount. Amazon EMR provisions Spot Instances if the current Spot price
in an Availability Zone is below your maximum Spot price. You pay the Spot
price, not necessarily the maximum Spot price.

###### Note

Spot Instances with a defined duration (also known as Spot blocks)
are no longer available to new customers from July 1, 2021. For
customers who have previously used the feature, we will continue to
support Spot Instances with a defined duration until December 31, 2022.

Available in Amazon EMR 5.12.1 and later, you have the option to launch
Spot and On-Demand Instance fleets with optimized capacity allocation.
This allocation strategy option can be set in the old AWS Management Console or using
the API `RunJobFlow`. Note that you can't customize
allocation strategy in the new console. Using the allocation strategy
option requires additional service role permissions. If you use the
default Amazon EMR service role and managed policy ([EMR_DefaultRole](emr-iam-role.md "emr-iam-role.md") and
`AmazonEMRServicePolicy_v2`) for the cluster, the
permissions for the allocation strategy option are already included. If
you're not using the default Amazon EMR service role and managed policy, you
must add them to use this option. See [Service role for Amazon EMR (EMR role)](emr-iam-role.md "emr-iam-role.md").

For more information about Spot Instances, see [Spot Instances](../../../AWSEC2/latest/UserGuide/using-spot-instances.md "../../../AWSEC2/latest/UserGuide/using-spot-instances.md")
in the Amazon EC2 User Guide. For more information about On-Demand Instances,
see [On-Demand
Instances](../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md "../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md") in the Amazon EC2 User Guide.

If you choose to launch On-Demand Instance fleets with the
lowest-price allocation strategy, you have the option to use capacity
reservations. Capacity reservation options can be set using the Amazon EMR
API `RunJobFlow`. Capacity reservations require additional
service role permissions which you must add to use these options. See
[Allocation strategy
permissions](#create-cluster-allocation-policy "#create-cluster-allocation-policy"). Note that you
can't customize capacity reservations in the new console.

### **Multiple subnet (Availability Zones) options**

When you use instance fleets, you can specify multiple Amazon EC2 subnets
within a VPC, each corresponding to a different Availability Zone. If you use
EC2-Classic, you specify Availability Zones explicitly. Amazon EMR identifies the
best Availability Zone to launch instances according to your fleet
specifications. Instances are always provisioned in only one Availability Zone.
You can select private subnets or public subnets, but you can't mix the
two, and the subnets you specify must be within the same VPC.

### **Master node configuration**

Because the primary instance fleet is only a single instance, its
configuration is slightly different from core and task instance fleets.
You only select either On-Demand or Spot for the primary instance
fleet because it consists of only one instance. If you use the console
to create the instance fleet, the target capacity for the purchasing
option you select is set to 1. If you use the AWS CLI, always set either
`TargetSpotCapacity` or
`TargetOnDemandCapacity` to 1 as appropriate. You can
still choose up to five instance types for the primary instance
fleet (or a maximum of 30 when you use the allocation strategy option
for On-Demand or Spot Instances). However, unlike core and task instance
fleets, where Amazon EMR might provision multiple instances of different
types, Amazon EMR selects a single instance type to provision for the
primary instance fleet.

## Allocation strategy for instance

fleets

With Amazon EMR versions 5.12.1 and later, you can use the allocation strategy option with
On-Demand and Spot Instances for each cluster node. When you create a cluster using the
AWS CLI, Amazon EMR API, or Amazon EMR console with an allocation strategy, you can specify up to 30
Amazon EC2 instance types per fleet. With the default Amazon EMR cluster instance fleet configuration,
you can have up to 5 instance types per fleet. We recommend that you use the allocation
strategy option for faster cluster provisioning, more accurate Spot Instance allocation, and
fewer Spot Instance interruptions.

###### Topics

- [Allocation strategy with
  On-Demand Instances](#emr-instance-fleet-allocation-strategy-od "#emr-instance-fleet-allocation-strategy-od")
- [Allocation strategy with
  Spot Instances](#emr-instance-fleet-allocation-strategy-spot "#emr-instance-fleet-allocation-strategy-spot")
- [Allocation strategy
  permissions](#emr-instance-fleet-allocation-strategy-permissions "#emr-instance-fleet-allocation-strategy-permissions")
- [Required IAM permissions for an
  allocation strategy](#create-cluster-allocation-policy "#create-cluster-allocation-policy")

### Allocation strategy with

On-Demand Instances

The following allocation strategies are available for your On-Demand Instances:

`lowest-price` **(default)**
The lowest-price allocation strategy launches On-Demand instances from the lowest priced pool that
has available capacity. If the lowest-priced pool doesn't have available capacity, the On-Demand Instances come from the
next lowest-priced pool with available capacity.

`prioritized`
The prioritized allocation strategy lets you specify a priority value for each instance type for your instance fleet. Amazon EMR launches your On-Demand Instances
that have the highest priority. If you use this strategy, you must configure the priority for at least one instance type.
If you don't configure the priority value for an instance type, Amazon EMR assigns the lowest priority to that instance type. Each instance fleet (primary, core, or task) in a cluster
can have a different priority value for a given instance type.

###### Note

If you use the **capacity-optimized-prioritized** Spot allocation strategy, Amazon EMR applies the same priorities
to both your On-Demand Instances and Spot instances when you set priorities.

### Allocation strategy with

Spot Instances

For _Spot Instances_ you can choose from one of the following
allocation strategies:

**`price-capacity-optimized` (recommended)**

The price-capacity optimized allocation strategy launches Spot instances
from the Spot instance pools that have the highest capacity available and
the lowest price for the number of instances that are launching. As a
result, the price-capacity optimized strategy typically has a higher chance
of getting Spot capacity, and delivers lower interruption rates.This is the default strategy
for Amazon EMR releases 6.10.0 and higher.

**`capacity-optimized`**

The capacity-optimized allocation strategy launches Spot Instances into
the most available pools with the lowest chance of interruption in the near
term. This is a good option for workloads that might have a higher cost of
interruption associated with work that gets restarted. This is the default
strategy for Amazon EMR releases 6.9.0 and lower.

**`capacity-optimized-prioritized`**

The capacity-optimized-prioritized allocation strategy lets you specify a priority value for each instance type in your
instance fleet. Amazon EMR optimizes for capacity first, but it respects instance type priorities on a best-effort basis, such as if the priority
doesn't significantly affect the fleet's ability to provision optimal capacity. We recommend this option if you have workloads that must
have a minimal amount of disruption that still have a need for certain instance types. If you use this strategy, you must configure the priority
for at least one instance type. If you don't configure a priority for any instance type, Amazon EMR assigns the lowest priority value to that instance type.
Each instance fleet (primary, core, or task) in a cluster can have a different priority value for a given instance type.

###### Note

If you use the **prioritized** On-Demand allocation strategy, Amazon EMR applies the same priority value
to both your On-Demand and Spot Instances when you set priorities.

**`diversified`**

With the diversified allocation strategy, Amazon EC2 distributes Spot Instances
across all Spot capacity pools.

**`lowest-price`**

The lowest-price allocation strategy launches Spot Instances from the
lowest priced pool that has available capacity. If the lowest-priced pool
doesn't have available capacity, the Spot Instances come from the next
lowest priced pool that has available capacity. If a pool runs out of
capacity before it fulfills your requested capacity, the Amazon EC2 fleet draws
from the next lowest priced pool to continue to fulfill your request. To
ensure that your desired capacity is met, you might receive Spot Instances
from several pools. Because this strategy only considers instance price, and
does not consider capacity availability, it might lead to high interruption
rates.

### Allocation strategy

permissions

The allocation strategy option requires several IAM permissions that are
automatically included in the default Amazon EMR service role and Amazon EMR managed policy
(`EMR_DefaultRole` and `AmazonEMRServicePolicy_v2`). If you
use a custom service role or managed policy for your cluster, you must add these
permissions before you create the cluster. For more information, see [Allocation strategy
permissions](#create-cluster-allocation-policy "#create-cluster-allocation-policy").

Optional On-Demand Capacity Reservations (ODCRs) are available when you use the
On-Demand allocation strategy option. Capacity reservation options let you specify a
preference for using reserved capacity first for Amazon EMR clusters. You can use this to
ensure that your critical workloads use the capacity you have already reserved using
open or targeted ODCRs. For non-critical workloads, the capacity reservation preferences
let you specify whether reserved capacity should be consumed.

Capacity reservations can only be used by instances that match their attributes
(instance type, platform, and Availability Zone). By default, open capacity reservations are
automatically used by Amazon EMR when provisioning On-Demand Instances that match the
instance attributes. If you don't have any running instances that match the attributes
of the capacity reservations, they remain unused until you launch an instance matching
their attributes. If you don't want to use any capacity reservations when launching your
cluster, you must set capacity reservation preference to **none** in
launch options.

However, you can also target a capacity reservation for specific workflows. This
enables you to explicitly control which instances are allowed to run in that reserved
capacity. For more information about On-Demand capacity reservations, see [Use capacity reservations with
instance fleets in Amazon EMR](on-demand-capacity-reservations.md "on-demand-capacity-reservations.md").

### Required IAM permissions for an

allocation strategy

Your [Service role for Amazon EMR (EMR role)](emr-iam-role.md "emr-iam-role.md") requires additional
permissions to create a cluster that uses the allocation strategy option for On-Demand
or Spot Instance fleets.

We automatically include these permissions in the default Amazon EMR service role [EMR_DefaultRole](emr-iam-role.md "emr-iam-role.md") and the Amazon EMR managed
policy [AmazonEMRServicePolicy_v2](emr-managed-iam-policies.md "emr-managed-iam-policies.md").

If you use a custom service role or managed policy for your cluster, you must add the
following permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteLaunchTemplate",
 "ec2:CreateLaunchTemplate",
 "ec2:DescribeLaunchTemplates",
 "ec2:CreateLaunchTemplateVersion",
 "ec2:CreateFleet"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowEC2Deletelaunchtemplate"
 }
 ]
}`

```

The following service role permissions are required to create a cluster that uses open
or targeted capacity reservations. You must include these permissions in addition to the
permissions required for using the allocation strategy option.

###### Example Policy document for service role

capacity reservations

To use open capacity reservations, you must include the following additional
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeCapacityReservations",
 "ec2:DescribeLaunchTemplateVersions",
 "ec2:DeleteLaunchTemplateVersions"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowEC2Describecapacityreservations"
 }
 ]
}`

```

To use targeted capacity reservations, you must include the following additional
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeCapacityReservations",
 "ec2:DescribeLaunchTemplateVersions",
 "ec2:DeleteLaunchTemplateVersions",
 "resource-groups:ListGroupResources"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowEC2Describecapacityreservations"
 }
 ]
}`

```

## Configure instance fleets for your cluster

Console

###### To create a cluster with instance fleets with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation pane,
   choose **Clusters**, and choose **Create
   cluster**.
3. Under **Cluster configuration**, choose
   **Instance fleets**.
4. For each **Node group**, select **Add
   instance type** and choose up to 5 instance types for
   primary and core instance fleets and up to fifteen instance types for
   task instance fleets. Amazon EMR might provision any mix of these instance
   types when it launches the cluster.
5. Under each node group type, choose the **Actions**
   dropdown menu next to each instance to change these settings:

**Add EBS volumes**

Specify EBS volumes to attach to the instance type after
Amazon EMR provisions it.

**Edit weighted capacity**

For the core node group, change this value to any number
of units that fits your applications. The number of YARN
vCores for each fleet instance type is used as the default
weighted capacity units. You can't edit weighted capacity
for the primary node.

**Edit maximum Spot price**

Specify a maximum Spot price for each instance type in a
fleet. You can set this price either as a percentage of the
On-Demand price, or as a specific dollar amount. If the
current Spot price in an Availability Zone is below your maximum
Spot price, Amazon EMR provisions Spot Instances. You pay the
Spot price, not necessarily the maximum Spot price. 6. Optionally, to add security groups for your nodes, expand
**EC2 security groups (firewall)** in the
**Networking** section and select your security
group for each node type. 7. Optionally, select the check box next to **Apply allocation
strategy** if you want to use the allocation strategy
option, and select the allocation strategy that you want to specify for
the Spot Instances. You shouldn't select this option if your Amazon EMR
service role doesn't have the required permissions. For more
information, see [Allocation strategy for instance
fleets](#emr-instance-fleet-allocation-strategy "#emr-instance-fleet-allocation-strategy"). 8. Choose any other options that apply to your cluster. 9. To launch your cluster, choose **Create
cluster**.

AWS CLI
To create and launch a cluster with instance fleets with the AWS CLI, follow
these guidelines:

- To create and launch a cluster with instance fleets, use the
  `create-cluster` command along with
  `--instance-fleet` parameters.
- To get configuration details about the instance fleets in a cluster,
  use the `list-instance-fleets` command.
- To add multiple custom Amazon Linux AMIs to a cluster you’re creating, use the
  `CustomAmiId` option with each `InstanceType`
  specification. You can configure instance fleet nodes with multiple
  instance types and multiple custom AMIs to fit your requirements. See
  [Examples: Creating a
  cluster with the instance fleets configuration](#create-cluster-instance-fleet-cli "#create-cluster-instance-fleet-cli").
- To make changes to the target capacity for an instance fleet, use the
  `modify-instance-fleet` command.
- To add a task instance fleet to a cluster that doesn't already have
  one, use the `add-instance-fleet` command.
- Multiple custom AMIs can be added to the task instance fleet using the
  CustomAmiId argument with the add-instance-fleet command. See [Examples: Creating a
  cluster with the instance fleets configuration](#create-cluster-instance-fleet-cli "#create-cluster-instance-fleet-cli").
- To use the allocation strategy option when creating an instance fleet,
  update the service role to include the example policy document in the
  following section.
- To use the capacity reservations options when creating an instance
  fleet with On-Demand allocation strategy, update the service role to
  include the example policy document in the following section.
- The instance fleets are automatically included in the default EMR
  service role and Amazon EMR managed policy (`EMR_DefaultRole` and
  `AmazonEMRServicePolicy_v2`). If you are using a custom
  service role or custom managed policy for your cluster, you must add the
  new permissions for allocation strategy in the following section.

## Examples: Creating a

cluster with the instance fleets configuration

The following examples demonstrate `create-cluster` commands
with a variety of options that you can combine.

###### Note

If you have not previously created the default Amazon EMR service role and
EC2 instance profile, use `aws emr create-default-roles` to
create them before using the `create-cluster` command.

###### Example: On-Demand primary, On-Demand core with single instance type,

Default VPC

```
aws emr create-cluster --release-label `emr-5.3.1` --service-role EMR_DefaultRole \
  --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
  --instance-fleets \
    InstanceFleetType=MASTER,TargetOnDemandCapacity=1,InstanceTypeConfigs=['{InstanceType=m5.xlarge}'] \
    InstanceFleetType=CORE,TargetOnDemandCapacity=1,InstanceTypeConfigs=['{InstanceType=m5.xlarge}']
```

###### Example: Spot primary, Spot core with single instance type, default

VPC

```
aws emr create-cluster --release-label emr-5.3.1 --service-role EMR_DefaultRole \
  --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
  --instance-fleets \
    InstanceFleetType=MASTER,TargetSpotCapacity=1,\
InstanceTypeConfigs=['{InstanceType=m5.xlarge,BidPrice=0.5}'] \
    InstanceFleetType=CORE,TargetSpotCapacity=1,\
InstanceTypeConfigs=['{InstanceType=m5.xlarge,BidPrice=0.5}']
```

###### Example: On-Demand primary, mixed core with single instance type,

single EC2 subnet

```
aws emr create-cluster --release-label emr-5.3.1 --service-role EMR_DefaultRole \
  --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole,SubnetIds=['subnet-ab12345c'] \
  --instance-fleets \
    InstanceFleetType=MASTER,TargetOnDemandCapacity=1,\
InstanceTypeConfigs=['{InstanceType=m5.xlarge}'] \
    InstanceFleetType=CORE,TargetOnDemandCapacity=2,TargetSpotCapacity=6,\
InstanceTypeConfigs=['{InstanceType=m5.xlarge,BidPrice=0.5,WeightedCapacity=2}']
```

###### Example: On-Demand primary, spot core with multiple weighted instance

Types, Timeout for Spot, Range of EC2 Subnets

```
aws emr create-cluster --release-label emr-5.3.1 --service-role EMR_DefaultRole \
  --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole,SubnetIds=['subnet-ab12345c','subnet-de67890f'] \
  --instance-fleets \
    InstanceFleetType=MASTER,TargetOnDemandCapacity=1,\
InstanceTypeConfigs=['{InstanceType=m5.xlarge}'] \
    InstanceFleetType=CORE,TargetSpotCapacity=11,\
InstanceTypeConfigs=['{InstanceType=m5.xlarge,BidPrice=0.5,WeightedCapacity=3}',\
'{InstanceType=m4.2xlarge,BidPrice=0.9,WeightedCapacity=5}'],\
LaunchSpecifications={SpotSpecification='{TimeoutDurationMinutes=120,TimeoutAction=SWITCH_TO_ON_DEMAND}'}
```

###### Example: On-Demand primary, mixed core and task with multiple

weighted instance types, timeout for core Spot Instances, range of EC2
subnets

```
aws emr create-cluster --release-label emr-5.3.1 --service-role EMR_DefaultRole \
  --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole,SubnetIds=['subnet-ab12345c','subnet-de67890f'] \
  --instance-fleets \
    InstanceFleetType=MASTER,TargetOnDemandCapacity=1,InstanceTypeConfigs=['{InstanceType=m5.xlarge}'] \
    InstanceFleetType=CORE,TargetOnDemandCapacity=8,TargetSpotCapacity=6,\
InstanceTypeConfigs=['{InstanceType=m5.xlarge,BidPrice=0.5,WeightedCapacity=3}',\
'{InstanceType=m4.2xlarge,BidPrice=0.9,WeightedCapacity=5}'],\
LaunchSpecifications={SpotSpecification='{TimeoutDurationMinutes=120,TimeoutAction=SWITCH_TO_ON_DEMAND}'} \
    InstanceFleetType=TASK,TargetOnDemandCapacity=3,TargetSpotCapacity=3,\
InstanceTypeConfigs=['{InstanceType=m5.xlarge,BidPrice=0.5,WeightedCapacity=3}']
```

###### Example: Spot primary, no core or task, Amazon EBS configuration, default

VPC

```
aws emr create-cluster --release-label Amazon EMR 5.3.1 --service-role EMR_DefaultRole \
  --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
  --instance-fleets \
    InstanceFleetType=MASTER,TargetSpotCapacity=1,\
LaunchSpecifications={SpotSpecification='{TimeoutDurationMinutes=60,TimeoutAction=TERMINATE_CLUSTER}'},\
InstanceTypeConfigs=['{InstanceType=m5.xlarge,BidPrice=0.5,\
EbsConfiguration={EbsOptimized=true,EbsBlockDeviceConfigs=[{VolumeSpecification={VolumeType=gp2,\
SizeIn GB=100}},{VolumeSpecification={VolumeType=io1,SizeInGB=100,Iop s=100},VolumesPerInstance=4}]}}']
```

###### Example: Multiple custom AMIs, multiple instance types, on-demand

primary, on-demand core

```
aws emr create-cluster --release-label Amazon EMR 5.3.1 --service-role EMR_DefaultRole \
  --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
  --instance-fleets \
    InstanceFleetType=MASTER,TargetOnDemandCapacity=1,\
InstanceTypeConfigs=['{InstanceType=m5.xlarge,CustomAmiId=ami-123456},{InstanceType=m6g.xlarge, CustomAmiId=ami-234567}'] \
    InstanceFleetType=CORE,TargetOnDemandCapacity=1,\
InstanceTypeConfigs=['{InstanceType=m5.xlarge,CustomAmiId=ami-123456},{InstanceType=m6g.xlarge, CustomAmiId=ami-234567}']
```

###### Example: Add a task node to a running cluster with multiple instance

types and multiple custom AMIs

```
aws emr add-instance-fleet --cluster-id j-123456 --release-label Amazon EMR 5.3.1 \
  --service-role EMR_DefaultRole \
  --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
  --instance-fleet \
    InstanceFleetType=Task,TargetSpotCapacity=1,\
InstanceTypeConfigs=['{InstanceType=m5.xlarge,CustomAmiId=ami-123456}',\
'{InstanceType=m6g.xlarge,CustomAmiId=ami-234567}']
```

###### Example: Use a JSON configuration file

You can configure instance fleet parameters in a JSON file, and then
reference the JSON file as the sole parameter for instance fleets. For
example, the following command references a JSON configuration file,
`my-fleet-config.json`:

```
aws emr create-cluster --release-label emr-5.30.0 --service-role EMR_DefaultRole \
--ec2-attributes InstanceProfile=EMR_EC2_DefaultRole \
--instance-fleets file://`my-fleet-config.json`
```

The `my-fleet-config.json` file specifies
primary, core, and task instance fleets as shown in the following
example. The core instance fleet uses a maximum Spot price
(`BidPrice`) as a percentage of On-Demand, while the task
and primary instance fleets use a maximum Spot price
(BidPriceAsPercentageofOnDemandPrice) as a string in USD.

```
[
    {
        "Name": "Masterfleet",
        "InstanceFleetType": "MASTER",
        "TargetSpotCapacity": 1,
        "LaunchSpecifications": {
            "SpotSpecification": {
                "TimeoutDurationMinutes": 120,
                "TimeoutAction": "SWITCH_TO_ON_DEMAND"
            }
        },
        "InstanceTypeConfigs": [
            {
                "InstanceType": "m5.xlarge",
                "BidPrice": "0.89"
            }
        ]
    },
    {
        "Name": "Corefleet",
        "InstanceFleetType": "CORE",
        "TargetSpotCapacity": 1,
        "TargetOnDemandCapacity": 1,
        "LaunchSpecifications": {
          "OnDemandSpecification": {
            "AllocationStrategy": "lowest-price",
            "CapacityReservationOptions":
            {
                "UsageStrategy": "use-capacity-reservations-first",
                "CapacityReservationResourceGroupArn": "String"
            }
        },
            "SpotSpecification": {
                "AllocationStrategy": "capacity-optimized",
                "TimeoutDurationMinutes": 120,
                "TimeoutAction": "TERMINATE_CLUSTER"
            }
        },
        "InstanceTypeConfigs": [
            {
                "InstanceType": "m5.xlarge",
                "BidPriceAsPercentageOfOnDemandPrice": 100
            }
        ]
    },
    {
        "Name": "Taskfleet",
        "InstanceFleetType": "TASK",
        "TargetSpotCapacity": 1,
        "LaunchSpecifications": {
          "OnDemandSpecification": {
            "AllocationStrategy": "lowest-price",
            "CapacityReservationOptions":
            {
                "CapacityReservationPreference": "none"
            }
        },
            "SpotSpecification": {
                "TimeoutDurationMinutes": 120,
                "TimeoutAction": "TERMINATE_CLUSTER"
            }
        },
        "InstanceTypeConfigs": [
            {
                "InstanceType": "m5.xlarge",
                "BidPrice": "0.89"
            }
        ]
    }
]
```

## Modify target capacities for

an instance fleet

Use the `modify-instance-fleet` command to specify new target
capacities for an instance fleet. You must specify the cluster ID and the
instance fleet ID. Use the `list-instance-fleets` command to
retrieve instance fleet IDs.

```
aws emr modify-instance-fleet --cluster-id `<cluster-id>` \
  --instance-fleet \
    InstanceFleetId='`<instance-fleet-id>`',TargetOnDemandCapacity=1,TargetSpotCapacity=1
```

## Add a task instance fleet to a

cluster

If a cluster has only primary and core instance fleets, you can use the
`add-instance-fleet` command to add a task instance fleet.
You can only use this to add task instance fleets.

```
aws emr add-instance-fleet --cluster-id `<cluster-id>`
  --instance-fleet \
    InstanceFleetType=TASK,TargetSpotCapacity=1,\
LaunchSpecifications={SpotSpecification='{TimeoutDurationMinutes=20,TimeoutAction=TERMINATE_CLUSTER}'},\
InstanceTypeConfigs=['{InstanceType=m5.xlarge,BidPrice=0.5}']
```

## Get configuration

details of instance fleets in a cluster

Use the `list-instance-fleets` command to get configuration
details of the instance fleets in a cluster. The command takes a cluster ID
as input. The following example demonstrates the command and its output for
a cluster that contains a primary task instance group and a core task
instance group. For full response syntax, see [ListInstanceFleets](../../../ElasticMapReduce/latest/API/API_ListInstanceFleets.md "../../../ElasticMapReduce/latest/API/API_ListInstanceFleets.md") in the
_Amazon EMR API Reference._

```
list-instance-fleets --cluster-id `<cluster-id>`
```

```
{
    "InstanceFleets": [
        {
            "Status": {
                "Timeline": {
                    "ReadyDateTime": 1488759094.637,
                    "CreationDateTime": 1488758719.817
                },
                "State": "RUNNING",
                "StateChangeReason": {
                    "Message": ""
                }
            },
            "ProvisionedSpotCapacity": 6,
            "Name": "CORE",
            "InstanceFleetType": "CORE",
            "LaunchSpecifications": {
                "SpotSpecification": {
                    "TimeoutDurationMinutes": 60,
                    "TimeoutAction": "TERMINATE_CLUSTER"
                }
            },
            "ProvisionedOnDemandCapacity": 2,
            "InstanceTypeSpecifications": [
                {
                    "BidPrice": "0.5",
                    "InstanceType": "m5.xlarge",
                    "WeightedCapacity": 2
                }
            ],
            "Id": "if-1ABC2DEFGHIJ3"
        },
        {
            "Status": {
                "Timeline": {
                    "ReadyDateTime": 1488759058.598,
                    "CreationDateTime": 1488758719.811
                },
                "State": "RUNNING",
                "StateChangeReason": {
                    "Message": ""
                }
            },
            "ProvisionedSpotCapacity": 0,
            "Name": "MASTER",
            "InstanceFleetType": "MASTER",
            "ProvisionedOnDemandCapacity": 1,
            "InstanceTypeSpecifications": [
                {
                    "BidPriceAsPercentageOfOnDemandPrice": 100.0,
                    "InstanceType": "m5.xlarge",
                    "WeightedCapacity": 1
                }
            ],
           "Id": "if-2ABC4DEFGHIJ4"
        }
    ]
}


```
