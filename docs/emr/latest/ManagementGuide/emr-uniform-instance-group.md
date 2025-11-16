# Configure uniform instance

groups for your Amazon EMR cluster

With the instance groups configuration, each node type (master, core, or task)
consists of the same instance type and the same purchasing option for instances:
On-Demand or Spot. You specify these settings when you create an instance group.
They can't be changed later. You can, however, add instances of the same type
and purchasing option to core and task instance groups. You can also remove
instances.

If the cluster's On-Demand Instances match the attributes of open capacity
reservations (instance type, platform, tenancy and Availability Zone) available in your
account, the capacity reservations are applied automatically. You can use open
capacity reservations for primary, core, and task nodes. However, you cannot use
targeted capacity reservations or prevent instances from launching into open
capacity reservations with matching attributes when you provision clusters using
instance groups. If you want to use targeted capacity reservations or prevent
instances from launching into open capacity reservations, use Instance Fleets
instead. For more information, see [Use capacity reservations with
instance fleets in Amazon EMR](on-demand-capacity-reservations.md "on-demand-capacity-reservations.md").

To add different instance types after a cluster is created, you can add
additional task instance groups. You can choose different instance types and
purchasing options for each instance group. For more information, see [Use Amazon EMR cluster scaling to adjust
for changing workloads](emr-scale-on-demand.md "emr-scale-on-demand.md").

When launching instances, the On-Demand Instance's capacity reservation
preference defaults to `open`, which enables it to run in any open
capacity reservation that has matching attributes (instance type, platform,
Availability Zone). For more information about On-Demand Capacity Reservations, see
[Use capacity reservations with
instance fleets in Amazon EMR](on-demand-capacity-reservations.md "on-demand-capacity-reservations.md").

This section covers creating a cluster with uniform instance groups. For more
information about modifying an existing instance group by adding or removing
instances manually or with automatic scaling, see [Manage Amazon EMR clusters](emr-manage.md "emr-manage.md").

## Use the console to

configure uniform instance groups

Console

###### To create a cluster with instance groups with the new

console

1. Sign in to the AWS Management Console, and open the Amazon EMR console
   at [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left
   navigation pane, choose **Clusters**,
   and choose **Create cluster**.
3. Under **Cluster configuration**,
   choose **Instance groups**.
4. Under **Node groups**, there is a
   section for each type of node group. For the primary
   node group, select the **Use multiple primary
   nodes** check box if you want to have 3
   primary nodes. Select the **Use Spot purchasing
   option** check box if you want to use Spot
   purchasing.
5. For the primary and core node groups, select
   **Add instance type** and choose up
   to 5 instance types. For the task group, select
   **Add instance type** and choose up
   to fifteen instance types. Amazon EMR might provision any mix
   of these instance types when it launches the
   cluster.
6. Under each node group type, choose the
   **Actions** dropdown menu next to
   each instance to change these settings:

**Add EBS volumes**

Specify EBS volumes to attach to the
instance type after Amazon EMR provisions it.

**Edit maximum Spot price**

Specify a maximum Spot price for each
instance type in a fleet. You can set this price
either as a percentage of the On-Demand price, or
as a specific dollar amount. If the current Spot
price in an Availability Zone is below your maximum Spot
price, Amazon EMR provisions Spot Instances. You pay
the Spot price, not necessarily the maximum Spot
price. 7. Optionally, expand **Node
configuration** to enter a JSON
configuration or to load JSON from Amazon S3. 8. Choose any other options that apply to your cluster. 9. To launch your cluster, choose **Create
cluster**.

## Use the AWS CLI to create a

cluster with uniform instance groups

To specify the instance groups configuration for a cluster using the
AWS CLI, use the `create-cluster` command along with the
`--instance-groups` parameter. Amazon EMR assumes the On-Demand
Instance option unless you specify the `BidPrice` argument for an
instance group. For examples of `create-cluster` commands that
launch uniform instance groups with On-Demand Instances and a variety of
cluster options, type `aws emr create-cluster help` at the
command line, or see [create-cluster](../../../cli/latest/reference/emr/create-cluster.md "../../../cli/latest/reference/emr/create-cluster.md") in the
_AWS CLI Command Reference_.

You can use the AWS CLI to create uniform instance groups in a cluster that
use Spot Instances. The offered Spot price depends on Availability Zone. When you
use the CLI or API, you can specify the Availability Zone either with the
`AvailabilityZone` argument (if you're using an EC2-classic
network) or the `SubnetID` argument of the `--ec2-attributes` parameter. The Availability Zone or subnet that you select applies to the
cluster, so it's used for all instance groups. If you don't specify an
Availability Zone or subnet explicitly, Amazon EMR selects the Availability Zone with the lowest
Spot price when it launches the cluster.

The following example demonstrates a `create-cluster` command
that creates primary, core, and two task instance groups that all use Spot
Instances. Replace `myKey` with the name of your
Amazon EC2 key pair.

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --name "`MySpotCluster`" \
  --release-label `emr-7.11.0` \
  --use-default-roles \
  --ec2-attributes KeyName=`myKey` \
  --instance-groups \
    InstanceGroupType=`MASTER`,InstanceType=`m5.xlarge`,InstanceCount=`1`,BidPrice=`0.25` \
    InstanceGroupType=`CORE`,InstanceType=`m5.xlarge`,InstanceCount=`2`,BidPrice=`0.03` \
    InstanceGroupType=`TASK`,InstanceType=`m5.xlarge`,InstanceCount=`4`,BidPrice=`0.03` \
    InstanceGroupType=`TASK`,InstanceType=`m5.xlarge`,InstanceCount=`2`,BidPrice=`0.04`
```

Using the CLI, you can create uniform instance group clusters that specify
a unique custom AMI for each instance type in the instance group. This
allows you to use different instance architectures in the same instance
group. Each instance type must use a custom AMI with a matching
architecture. For example, you would configure an m5.xlarge instance type
with an x86_64 architecture custom AMI, and an m6g.xlarge instance type with
a corresponding `AWS AARCH64` (ARM) architecture custom AMI.

The following example shows a uniform instance group cluster created with
two instance types, each with its own custom AMI. Notice that the custom
AMIs are specified only at the instance type level, not at the cluster
level. This is to avoid conflicts between the instance type AMIs and an AMI
at the cluster level, which would cause the cluster launch to fail.

```
aws emr create-cluster
  --release-label emr-5.30.0 \
  --service-role EMR_DefaultRole \
  --ec2-attributes SubnetId=subnet-22XXXX01,InstanceProfile=EMR_EC2_DefaultRole \
  --instance-groups \
    InstanceGroupType=MASTER,InstanceType=m5.xlarge,InstanceCount=1,CustomAmiId=ami-123456 \
    InstanceGroupType=CORE,InstanceType=m6g.xlarge,InstanceCount=1,CustomAmiId=ami-234567
```

You can add multiple custom AMIs to an instance group that you add to a
running cluster. The `CustomAmiId` argument can be used with the
`add-instance-groups` command as shown in the following
example.

```
aws emr add-instance-groups --cluster-id j-123456 \
  --instance-groups \
    InstanceGroupType=Task,InstanceType=m5.xlarge,InstanceCount=1,CustomAmiId=ami-123456
```

## Use the Java SDK to create an

instance group

You instantiate an `InstanceGroupConfig` object that specifies
the configuration of an instance group for a cluster. To use Spot Instances,
you set the `withBidPrice` and `withMarket` properties
on the `InstanceGroupConfig` object. The following code shows how
to define primary, core, and task instance groups that run Spot
Instances.

```
InstanceGroupConfig instanceGroupConfigMaster = new InstanceGroupConfig()
	.withInstanceCount(1)
	.withInstanceRole("MASTER")
	.withInstanceType("m4.large")
	.withMarket("SPOT")
	.withBidPrice("0.25");

InstanceGroupConfig instanceGroupConfigCore = new InstanceGroupConfig()
	.withInstanceCount(4)
	.withInstanceRole("CORE")
	.withInstanceType("m4.large")
	.withMarket("SPOT")
	.withBidPrice("0.03");

InstanceGroupConfig instanceGroupConfigTask = new InstanceGroupConfig()
	.withInstanceCount(2)
	.withInstanceRole("TASK")
	.withInstanceType("m4.large")
	.withMarket("SPOT")
	.withBidPrice("0.10");

```
