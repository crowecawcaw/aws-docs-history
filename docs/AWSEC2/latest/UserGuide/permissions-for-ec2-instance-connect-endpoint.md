# Grant permissions to use

EC2 Instance Connect Endpoint

By default, IAM entities don't have permission to create, describe, or modify
EC2 Instance Connect Endpoints. An IAM administrator can create IAM policies that grant the
permissions required to perform specific actions on the resources that they need.

For information about creating IAM policies, see [Creating IAM
policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

The following example policies show how you can control the permissions that users
have to EC2 Instance Connect Endpoints.

###### Examples

- [Permissions to create, describe,
  modify, and delete EC2 Instance Connect Endpoints](#iam-CreateInstanceConnectEndpoint "#iam-CreateInstanceConnectEndpoint")
- [Permissions to use EC2 Instance Connect Endpoint to connect to
  instances](#iam-OpenTunnel "#iam-OpenTunnel")
- [Permissions to connect only from a specific IP
  address range](#iam-sourceip "#iam-sourceip")

## Permissions to create, describe,

modify, and delete EC2 Instance Connect Endpoints

To create and modify an EC2 Instance Connect Endpoint, users require permissions for the
following actions:

- `ec2:CreateInstanceConnectEndpoint`
- `ec2:CreateNetworkInterface`
- `ec2:CreateTags`
- `ec2:ModifyInstanceConnectEndpoint`
- `iam:CreateServiceLinkedRole`

To describe and delete EC2 Instance Connect Endpoints, users require permissions for the
following actions:

- `ec2:DescribeInstanceConnectEndpoints`
- `ec2:DeleteInstanceConnectEndpoint`

You can create a policy that grants permission to create, describe, modify, and
delete EC2 Instance Connect Endpoints in all subnets. Alternatively, you can restrict actions for
specified subnets only by specifying the subnet ARNs as the allowed
`Resource` or by using the `ec2:SubnetID` condition key.
You can also use the `aws:ResourceTag` condition key to explicitly allow
or deny endpoint creation with certain tags. For more information, see [Policies
and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.

**Example IAM policy**

In the following example IAM policy, the `Resource` section grants
permission to create, modify, and delete endpoints in all subnets, specified by the
asterisk (`*`). The `ec2:Describe*` API actions do not support
resource-level permissions. Therefore, the `*` wildcard is necessary in
the `Resource` element.

## Permissions to use EC2 Instance Connect Endpoint to connect to

instances

The `ec2-instance-connect:OpenTunnel` action grants permission to
establish a TCP connection to an instance to connect over the EC2 Instance Connect Endpoint. You
can specify the EC2 Instance Connect Endpoint to use. Alternatively, a `Resource` with
an asterisk (`*`) allows users to use any available EC2 Instance Connect Endpoint. You
can also restrict access to instances based on the presence or absence of resource
tags as condition keys.

###### Conditions

- `ec2-instance-connect:remotePort` – The port on the
  instance that can be used to establish a TCP connection. When this condition
  key is used, attempting to connect to an instance on any other port other
  than the port specified in the policy results in a failure.
- `ec2-instance-connect:privateIpAddress` – The
  destination private IP address associated with the instance that you want to
  establish a TCP connection with. You can specify a single IP address, such
  as `10.0.0.1/32`, or a range of IPs through CIDRs, such as
  `10.0.1.0/28`. When this condition key is used, attempting to
  connect to an instance with a different private IP address or outside the
  CIDR range results in a failure.
- `ec2-instance-connect:maxTunnelDuration` – The maximum
  duration for an established TCP connection. The unit is seconds and the
  duration ranges from a minimum of 1 second to a maximum of 3,600 seconds (1
  hour). If the condition is not specified, the default duration is set to
  3,600 seconds (1 hour). Attempting to connect to an instance for longer than
  the specified duration in the IAM policy or for longer than the default
  maximum results in a failure. The connection is disconnected after the
  specified duration.

If `maxTunnelDuration` is specified in the IAM policy and the
value specified is less than 3,600 seconds (the default), then you must
specify `--max-tunnel-duration` in the command when connecting to
an instance. For information about how to connect to an instance, see [Connect to an Amazon EC2 instance using
EC2 Instance Connect Endpoint](connect-using-eice.md "connect-using-eice.md").

You can also grant a user access to establish connections to instances based on
the presence of resource tags on the EC2 Instance Connect Endpoint. For more information, see
[Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.

For Linux instances, the `ec2-instance-connect:SendSSHPublicKey` action
grants permission to push the public key to an instance. The `ec2:osuser`
condition specifies the name of the OS (operating system) user that can push the
public key to an instance. Use the [default username for the
AMI](connection-prereqs-general.md#connection-prereqs-get-info-about-instance "connection-prereqs-general.md#connection-prereqs-get-info-about-instance") that you used to launch the instance. For more information, see [Grant IAM permissions for
EC2 Instance Connect](ec2-instance-connect-configure-IAM-role.md "ec2-instance-connect-configure-IAM-role.md").

**Example IAM policy**

The following example IAM policies allow an IAM principal to connect to an
instance using only the specified EC2 Instance Connect Endpoint, identified by the specified
endpoint ID `eice-123456789abcdef`. The connection is successfully
established only if all the conditions are satisfied.

###### Note

The `ec2:Describe*` API actions do not support resource-level
permissions. Therefore, the `*` wildcard is necessary in the
`Resource` element.

Linux
This example evaluates if the connection to the instance is
established on —port 22 (SSH), if the private IP address of the
instance lies within the range of `10.0.1.0/31` (between
`10.0.1.0` and `10.0.1.1`), and the
`maxTunnelDuration` is less than or equal to
`3600` seconds. The connection is disconnected after
`3600` seconds (1 hour).

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "EC2InstanceConnect",
 "Action": "ec2-instance-connect:OpenTunnel",
 "Effect": "Allow",
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:instance-connect-endpoint/`eice-123456789abcdef`",
 "Condition": {
 "NumericEquals": {
 "ec2-instance-connect:remotePort": "`22`"
 },
 "IpAddress": {
 "ec2-instance-connect:privateIpAddress": "`10.0.1.0/31`"
 },
 "NumericLessThanEquals": {
 "ec2-instance-connect:maxTunnelDuration": "`3600`"
 }
 }
 },
 {
 "Sid": "SSHPublicKey",
 "Effect": "Allow",
 "Action": "ec2-instance-connect:SendSSHPublicKey",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ec2:osuser": "`ami-username`"
 }
 }
 },
 {
 "Sid": "Describe",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeInstanceConnectEndpoints"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

Windows
This example evaluates if the connection to the instance is
established on port 3389 (RDP), if the private IP address of the
instance lies within the range of `10.0.1.0/31` (between
`10.0.1.0` and `10.0.1.1`), and the
`maxTunnelDuration` is less than or equal to
`3600` seconds. The connection is disconnected after
`3600` seconds (1 hour).

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "EC2InstanceConnect",
 "Action": "ec2-instance-connect:OpenTunnel",
 "Effect": "Allow",
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:instance-connect-endpoint/`eice-123456789abcdef`",
 "Condition": {
 "NumericEquals": {
 "ec2-instance-connect:remotePort": "`3389`"
 },
 "IpAddress": {
 "ec2-instance-connect:privateIpAddress": "`10.0.1.0/31`"
 },
 "NumericLessThanEquals": {
 "ec2-instance-connect:maxTunnelDuration": "`3600`"
 }
 }
 },
 {
 "Sid": "Describe",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeInstanceConnectEndpoints"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## Permissions to connect only from a specific IP

address range

The following example IAM policy allows an IAM principal to connect to an instance
on condition they are connecting from an IP address within the IP address range
specified in the policy. If the IAM principal calls `OpenTunnel` from an
IP address not within `192.0.2.0/24` (the example IP address range in
this policy), the response is `Access Denied`. For more information, see
[`aws:SourceIp`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceip "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceip") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "ec2-instance-connect:OpenTunnel",
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:instance-connect-endpoint/`eice-123456789abcdef`",
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": "`192.0.2.0/24`"
 },
 "NumericEquals": {
 "ec2-instance-connect:remotePort": "`22`"
 }
 }
 },
 {
 "Sid": "SSHPublicKey",
 "Effect": "Allow",
 "Action": "ec2-instance-connect:SendSSHPublicKey",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ec2:osuser": "`ami-username`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeInstanceConnectEndpoints"
 ],
 "Resource": "*"
 }
 ]
}`

```
