# Create an Amazon EMR cluster with instance

fleets or uniform instance groups

When you create a cluster and specify the configuration of the primary node, core
nodes, and task nodes, you have two configuration options. You can use
_instance fleets_ or _uniform instance
groups_. The configuration option you choose applies to all nodes, it
applies for the lifetime of the cluster, and instance fleets and instance groups
cannot coexist in a cluster. The instance fleets configuration is available in Amazon EMR
version 4.8.0 and later, excluding 5.0.x versions.

You can use the Amazon EMR console, the AWS CLI, or the Amazon EMR API to create clusters with
either configuration. When you use the `create-cluster` command from the
AWS CLI, you use either the `--instance-fleets` parameters to create the
cluster using instance fleets or, alternatively, you use the
`--instance-groups` parameters to create it using uniform instance
groups.

The same is true using the Amazon EMR API. You use either the
`InstanceGroups` configuration to specify an array of
`InstanceGroupConfig` objects, or you use the
`InstanceFleets` configuration to specify an array of
`InstanceFleetConfig` objects.

In the new Amazon EMR console, you can choose to use either instance groups or instance
fleets when you create a cluster, and you have the option to use Spot Instances with
each. With the old Amazon EMR console, if you use the default **Quick
Options** settings when you create your cluster, Amazon EMR applies the
uniform instance groups configuration to the cluster and uses On-Demand Instances.
To use Spot Instances with uniform instance groups, or to configure instance fleets
and other customizations, choose **Advanced Options**.

## Instance fleets

The instance fleets configuration offers the widest variety of provisioning
options for Amazon EC2 instances. Each node type has a single instance fleet, and
using a task instance fleet is optional. You can specify up to five EC2 instance
types per fleet, or 30 EC2 instance types per fleet when you create a cluster
using the AWS CLI or Amazon EMR API and an [allocation strategy](emr-instance-fleet.md#emr-instance-fleet-allocation-strategy "emr-instance-fleet.md#emr-instance-fleet-allocation-strategy")
for On-Demand and Spot Instances. For the core and task instance fleets, you
assign a _target capacity_ for On-Demand Instances, and
another for Spot Instances. Amazon EMR chooses any mix of the specified instance
types to fulfill the target capacities, provisioning both On-Demand and Spot
Instances.

For the primary node type, Amazon EMR chooses a single instance type from your list
of instances, and you specify whether it's provisioned as an On-Demand or Spot
Instance. Instance fleets also provide additional options for Spot Instance and
On-Demand purchases. Spot Instance options include a timeout that specifies an
action to take if Spot capacity can't be provisioned, and a preferred allocation
strategy (capacity-optimized) for launching Spot Instance fleets. On-Demand
Instance fleets can also be launched using the allocation strategy
(lowest-price) option. If you use a service role that is not the EMR default
service role, or use an EMR managed policy in your service role, you need to add
additional permissions to the custom cluster service role to enable the
allocation strategy option. For more information, see [Service role for Amazon EMR (EMR role)](emr-iam-role.md "emr-iam-role.md").

For more information about configuring instance fleets, see [Planning and configuring instance fleets for your Amazon EMR cluster](emr-instance-fleet.md "emr-instance-fleet.md").

## Uniform instance groups

Uniform instance groups offer a simpler setup than instance fleets. Each Amazon EMR
cluster can include up to 50 instance groups: one primary instance group
that contains one Amazon EC2 instance, a core instance group that contains one or
more EC2 instances, and up to 48 optional task instance groups. Each core and
task instance group can contain any number of Amazon EC2 instances. You can scale
each instance group by adding and removing Amazon EC2 instances manually, or you can
set up automatic scaling. For information about adding and removing instances,
see [Use Amazon EMR cluster scaling to adjust
for changing workloads](emr-scale-on-demand.md "emr-scale-on-demand.md").

For more information about configuring uniform instance groups, see [Configure uniform instance
groups for your Amazon EMR cluster](emr-uniform-instance-group.md "emr-uniform-instance-group.md").

## Working with instance fleets and

instance groups

###### Topics

- [Planning and configuring instance fleets for your Amazon EMR cluster](emr-instance-fleet.md "emr-instance-fleet.md")
- [Reconfiguring instance fleets for your Amazon EMR cluster](instance-fleet-reconfiguration.md "instance-fleet-reconfiguration.md")
- [Use capacity reservations with
  instance fleets in Amazon EMR](on-demand-capacity-reservations.md "on-demand-capacity-reservations.md")
- [Configure uniform instance
  groups for your Amazon EMR cluster](emr-uniform-instance-group.md "emr-uniform-instance-group.md")
- [Availability Zone
  flexibility for an Amazon EMR cluster](emr-flexibility.md "emr-flexibility.md")
- [Configuring Amazon EMR cluster instance types and best practices for Spot instances](emr-plan-instances-guidelines.md "emr-plan-instances-guidelines.md")
