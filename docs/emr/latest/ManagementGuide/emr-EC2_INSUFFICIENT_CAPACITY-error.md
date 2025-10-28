# Amazon EMR cluster error: EC2 is out of capacity

An _EC2 is out of capacity for `InstanceType`_ error occurs when you attempt to create a
cluster, or add instances to a cluster, in an Availability Zone which has no more of the specified EC2 instance type. The subnet that you select
for a cluster determines the Availability Zone.

To create a cluster, do one of the following:

- Specify a different instance type with similar capabilities
- Create the cluster in a different Region
- Select a subnet in an Availability Zone where the instance type you want might be available.
  To add instances to a running cluster, do one of the following:

- Modify instance group configurations or instance fleet configurations to add available instance types with similar capabilities. For a list of supported instance types, see [Supported instance types with Amazon EMR](emr-supported-instance-types.md "emr-supported-instance-types.md"). To compare capabilities of EC2 instance types, see [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").
- Terminate the cluster and recreate it in a Region and Availability Zone where the instance type is available.
