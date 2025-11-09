# Connect to your instances using

a private IP address and EC2 Instance Connect Endpoint

EC2 Instance Connect Endpoint allows you to connect securely to an instance from the internet, without
using a bastion host, or requiring that your virtual private cloud (VPC) has direct internet
connectivity.

###### Benefits

- You can connect to your instances without requiring the instances to have a public
  IPv4 or IPv6 address. AWS charges for all public IPv4 addresses, including public IPv4 addresses
  associated with running instances and Elastic IP addresses. For more information, see the **Public IPv4 Address**
  tab on the [Amazon VPC pricing page](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").
- You can connect to your instances from the internet without requiring that your
  VPC has direct internet connectivity through an [internet
  gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md").
- You can control access to the creation and use of the EC2 Instance Connect Endpoints to connect
  to instances using [IAM policies and permissions](permissions-for-ec2-instance-connect-endpoint.md "permissions-for-ec2-instance-connect-endpoint.md").
- All attempts to connect to your instances, both successful and unsuccessful, are
  logged to [CloudTrail](log-ec2-instance-connect-endpoint-using-cloudtrail.md "log-ec2-instance-connect-endpoint-using-cloudtrail.md").

###### Pricing

There is no additional cost for using EC2 Instance Connect Endpoints. If you use an EC2 Instance Connect Endpoint
to connect to an instance in a different Availability Zone, there is an [additional
charge for data transfer](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer_within_the_same_AWS_Region "https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer_within_the_same_AWS_Region") across Availability Zones.

###### Contents

- [How it works](#how-eice-works "#how-eice-works")
- [Considerations](#ec2-instance-connect-endpoint-prerequisites "#ec2-instance-connect-endpoint-prerequisites")
- [Permissions](permissions-for-ec2-instance-connect-endpoint.md "permissions-for-ec2-instance-connect-endpoint.md")
- [Security groups](eice-security-groups.md "eice-security-groups.md")
- [Create an EC2 Instance Connect Endpoint](create-ec2-instance-connect-endpoints.md "create-ec2-instance-connect-endpoints.md")
- [Modify an EC2 Instance Connect Endpoint](modify-ec2-instance-connect-endpoint.md "modify-ec2-instance-connect-endpoint.md")
- [Delete an EC2 Instance Connect Endpoint](delete-ec2-instance-connect-endpoint.md "delete-ec2-instance-connect-endpoint.md")
- [Connect to an instance](connect-using-eice.md "connect-using-eice.md")
- [Log
  connections](log-ec2-instance-connect-endpoint-using-cloudtrail.md "log-ec2-instance-connect-endpoint-using-cloudtrail.md")
- [Service-linked role](eice-slr.md "eice-slr.md")
- [Quotas](eice-quotas.md "eice-quotas.md")

## How it works

EC2 Instance Connect Endpoint is an identity-aware TCP proxy. The EC2 Instance Connect Endpoint Service establishes a
private tunnel from your computer to the endpoint using the credentials for your IAM
entity. Traffic is authenticated and authorized before it reaches your VPC.

You can [configure additional security group
rules](eice-security-groups.md "eice-security-groups.md") to restrict inbound traffic to your instances. For example, you can use
inbound rules to allow traffic on management ports only from the EC2 Instance Connect Endpoint.

You can configure route table rules to allow the endpoint to connect to any instance in
any subnet of the VPC.

The following diagram shows how a user can connect to their instances from the internet
using an EC2 Instance Connect Endpoint. First, create an **EC2 Instance Connect Endpoint** in subnet A.
We create a network interface for the endpoint in the subnet, which serves as the entry
point for traffic destined to your instances in the VPC. If the route table for subnet B
allows traffic from subnet A, then you can use the endpoint to reach instances in subnet
B.

![Overview of the EC2 Instance Connect Endpoint flow.](images/ec2-instance-connect-endpoint.png)

## Considerations

Before you begin, consider the following.

- EC2 Instance Connect Endpoint is intended specifically for management traffic use cases, not
  for high volume data transfers. High volume data  transfers are
  throttled.
- You can create an EC2 Instance Connect Endpoint to support traffic to an instance that has a
  private IPv4 address or IPv6 address. The IP address type of the endpoint must
  match the IP address of the instance. You can create an endpoint that supports
  all IP address types.
- (Linux instances) If you use your own key pair, you can use any Linux AMI.
  Otherwise, your instance must have EC2 Instance Connect installed. For information
  about which AMIs include EC2 Instance Connect and how to install it on other supported
  AMIs, see [Install
  EC2 Instance Connect](ec2-instance-connect-set-up.md "ec2-instance-connect-set-up.md").
- You can assign a security group to an EC2 Instance Connect Endpoint. Otherwise, we use the
  default security group for the VPC. The security group for an EC2 Instance Connect Endpoint
  must allow outbound traffic to the destination instances. For more information,
  see [Security groups for EC2 Instance Connect Endpoint](eice-security-groups.md "eice-security-groups.md").
- You can configure an EC2 Instance Connect Endpoint to preserve the source IP addresses of
  clients when routing requests to the instances. Otherwise, the IP address of the
  network interface becomes the client IP address for all incoming traffic.
  - If you turn on client IP preservation, the security groups for the
    instances must allow traffic from the clients. Also, the instances must
    be in the same VPC as the EC2 Instance Connect Endpoint.
  - If you turn off client IP preservation, the security groups for the
    instances must allow traffic from the VPC. This is the default.
  - Client IP preservation is only supported on IPv4 EC2 Instance Connect Endpoints. To
    use client IP preservation, the IP address type of the EC2 Instance Connect Endpoint
    must be IPv4. Client IP preservation is not supported when the IP
    address type is dual-stack or IPv6.
  - The following instance types do not support client IP preservation:
    C1, CG1, CG2, G1, HI1, M1, M2, M3, and T1. If you turn on client IP
    preservation and attempt to connect to an instance with one of these
    instance types by using EC2 Instance Connect Endpoint, the connection fails.
  - Client IP preservation is not supported when traffic is routed through
    a transit gateway.

- When you create an EC2 Instance Connect Endpoint, a service-linked role is automatically
  created for the Amazon EC2 service in AWS Identity and Access Management (IAM). Amazon EC2 uses the
  service-linked role to provision network interfaces in your account, which are
  required when creating EC2 Instance Connect Endpoints. For more information, see [Service-linked role for EC2 Instance Connect Endpoint](eice-slr.md "eice-slr.md").
- You can create only 1 EC2 Instance Connect Endpoint per VPC and per subnet. For more
  information, see [Quotas for EC2 Instance Connect Endpoint](eice-quotas.md "eice-quotas.md"). If
  you need to create another EC2 Instance Connect Endpoint in a different Availability Zone
  within the same VPC, you must first delete the existing EC2 Instance Connect Endpoint.
  Otherwise, you'll receive a quota error.
- Each EC2 Instance Connect Endpoint can support up to 20 concurrent connections.
- The maximum duration for an established TCP connection is 1 hour (3,600
  seconds). You can specify the maximum allowed duration in an IAM policy, which
  can be up to 3,600 seconds. For more information, see [Permissions to use EC2 Instance Connect Endpoint to connect to
  instances](permissions-for-ec2-instance-connect-endpoint.md#iam-OpenTunnel "permissions-for-ec2-instance-connect-endpoint.md#iam-OpenTunnel").

The duration of the connection is not determined by the duration of your IAM
credentials. If your IAM credentials expire, the connection continues to persist
until the specified maximum duration is reached. When you connect to an instance
using the EC2 Instance Connect Endpoint console experience, set **Max tunnel duration
(seconds)** to a value that is less than the duration of your IAM
credentials. If your IAM credentials expire early, terminate the connection to
your instance by closing the browser page.
