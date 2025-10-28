# Amazon EMR cluster error: Instance type not supported

If you create a cluster, and it fails with the error message "The requested instance type `InstanceType` is not supported in the requested Availability Zone," it means that you created the cluster and specified an instance type for one or more instance groups that is not supported by Amazon EMR in the Region and Availability Zone where the cluster was created. Amazon EMR may support an instance type in one Availability Zone within a Region and not another. The subnet you select for a cluster determines the Availability Zone within the Region.

## Solution

###### Determine available instance types in an Availability Zone using the AWS CLI

- Use the `ec2 run-instances` command with the `--dry-run` option. In the example below, replace `m5.xlarge` with the instance type you want to use, `ami-035be7bafff33b6b6` with the AMI associated with that instance type, and `subnet-12ab3c45` with a subnet in the Availability Zone you want to query.

```
aws ec2 run-instances --instance-type `m5.xlarge` --dry-run --image-id `ami-035be7bafff33b6b6` --subnet-id `subnet-12ab3c45`
```

For instructions on finding an AMI ID, see [Find a Linux AMI](../../../AWSEC2/latest/UserGuide/finding-an-ami.md "../../../AWSEC2/latest/UserGuide/finding-an-ami.md"). To find a subnet ID, you can use the [describe-subnets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-subnets.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-subnets.html") command.

To learn more about how to discover available instance types, see [Find an Amazon EC2 instance type](../../../AWSEC2/latest/UserGuide/instance-discovery.md "../../../AWSEC2/latest/UserGuide/instance-discovery.md").

After you determine the instance types available, you can do any of the following:

- Create the cluster in the same Region and EC2 Subnet, and choose a different instance type with similar capabilities as your initial choice. For a list of supported instance types, see [Supported instance types with Amazon EMR](emr-supported-instance-types.md "emr-supported-instance-types.md"). To compare capabilities of EC2 instance types, see [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").
- Choose a subnet for the cluster in an Availability Zone where the instance type is available and supported by Amazon EMR.

**Mitigate instance fleet cluster launch failures because of unsupported primary instance types
in Amazon EMR**

Primary nodes are essential in Amazon EMR clusters. An EMR cluster launch might
fail with an `instance type not supported` error where Amazon EMR attempts to launch the cluster
in an Availability Zone where if the primary instance type isn't supported.
Enhanced Availability Zone selection for instance fleet clusters in Amazon EMR
automatically filters out unsupported AZs for the primary instance types you specified in the cluster
configuration. This means Amazon EMR won't choose an Availability Zone
where the configured primary instance types are not supported, which prevents cluster launch failures because
of unsupported instance types.

To enable this improvement, add the required permission to the service role or policy for your cluster.
The latest version of `AmazonEMRServicePolicy_v2` includes this permission, so if you use that policy,
the improvement is already available. If you use a custom service role or policy, add the permission
`ec2:DescribeInstanceTypeOfferings` when launching your cluster.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ec2:DescribeInstanceTypeOfferings"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ],
 "Sid": "AllowEC2Describeinstancetypeofferings"
 }
 ]
}`

```
