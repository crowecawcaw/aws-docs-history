AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Controlling network traffic with security groups on Snowball Edge

A _security group_ acts as a virtual firewall that
controls the traffic for one or more instances. When you launch an instance, you
associate one or more security groups with the instance. You can add rules to each
security group to allow traffic to or from its associated instances. For more
information, see [Amazon EC2 security
groups for Linux instances](../../../AWSEC2/latest/UserGuide/using-network-security.md "../../../AWSEC2/latest/UserGuide/using-network-security.md") in the Amazon EC2 User Guide.

Security groups on Snowball Edge devices are similar to security groups in the AWS
Cloud. Virtual private clouds (VPCs) aren't supported on Snowball Edge devices.

Following, you can find the other differences between Snowball Edge security groups
and EC2 VPC security groups:

- Each Snowball Edge device has a limit of 50 security groups.
- The default security group allows all inbound and outbound traffic.
- Traffic between local instances can use either the private instance IP address
  or a public IP address. For example, suppose that you want to connect using SSH
  from instance A to instance B. In this case, your target IP address can be
  either the public IP or private IP address of instance B, if the security group
  rule allows the traffic.
- Only the parameters listed for AWS CLI actions and API calls are supported.
  These typically are a subset of those supported in EC2 VPC instances.
  For more information about supported AWS CLI actions, see [List of supported EC2-compatible AWS CLI
  commands on a Snowball Edge](using-ec2-endpoint.md#list-cli-commands-ec2-edge "using-ec2-endpoint.md#list-cli-commands-ec2-edge").
  For more information on supported API operations, see [Supported Amazon EC2-compatible API
  operations on a Snowball Edge](using-ec2-endpoint.md#using-ec2-adapter-supported-api "using-ec2-endpoint.md#using-ec2-adapter-supported-api").
