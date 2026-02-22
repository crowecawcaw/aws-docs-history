# Service link private connectivity options

You can configure the service link with a private connection for the traffic between the
Outposts and home AWS Region. You can choose to use Direct Connect private or transit VIFs.

Select the private connectivity option when you create your Outpost in the AWS Outposts console.
For instructions, see [Create an
Outpost](order-outpost-capacity.md#create-outpost "order-outpost-capacity.md#create-outpost").

When you select the private connectivity option, a service link VPN connection is
established after the Outpost is installed, using a VPC and subnet that you specify. This
allows private connectivity through the VPC and minimizes public internet exposure.

The following image shows both options to establish a service link VPN private connection
between your Outposts and the AWS Region:

![The service link private connection options.](images/outpost-rack2ndgen-sl-private-connection-options.PNG)

###### Note

Second-generation Outposts racks require a larger subnet size (/24 or larger) and a VPC Endpoint for the Outposts service.

###### IP Address Planning for Private Connectivity

When configuring private connectivity for the Outposts service link, plan your IP
addressing carefully to avoid future conflicts. Service Link VIFs are immutable. You cannot
create CoIP pools or DVR subnet ranges assigned to the Local Gateway (LGW) that overlap
with existing Service Link address ranges or VPC CIDR ranges used for the dedicated private
connectivity VPC, as they will cause BGP routing conflicts and affect Service Link
functionality.

## Prerequisites

The following prerequisites are required before you can configure private connectivity
for your Outpost:

- You must configure permissions for an IAM entity (user or role) to allow the user
  or role to create the service-linked role for private connectivity. The IAM entity
  needs permission to access the following actions:

      + `iam:CreateServiceLinkedRole` on
       `arn:aws:iam::*:role/aws-service-role/outposts.amazonaws.com/AWSServiceRoleForOutposts*`
      + `iam:PutRolePolicy` on
       `arn:aws:iam::*:role/aws-service-role/outposts.amazonaws.com/AWSServiceRoleForOutposts*`
      + `ec2:DescribeVpcs`
      + `ec2:DescribeSubnets`

  For more information, see [AWS Identity and Access Management for
  AWS Outposts](identity-access-management.md "identity-access-management.md")

- In the same AWS account and Availability Zone as your Outpost, create a VPC for
  the sole purpose of Outpost private connectivity with a subnet /24 or larger that does
  not conflict with 10.1.0.0/16. For example, you might use 10.3.0.0/16.

###### Important

Do not delete this VPC as it maintains the connection to your Outposts.

- Configure the subnet security group to allow traffic for UDP 443 inbound and
  outbound directions.
- Advertise the subnet CIDR to your on-premises network. You can use AWS Direct Connect to
  do so. For more information, see [Direct Connect
  virtual interfaces](../../../directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.md "../../../directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.md") and [Working with
  Direct Connect gateways](../../../directconnect/latest/UserGuide/direct-connect-gateways.md "../../../directconnect/latest/UserGuide/direct-connect-gateways.md") in the _Direct Connect User Guide_.
- Create a new VPC endpoint for AWS Outposts in your private connectivity VPC and
  subnet.

Use the following VPC endpoint settings:

    + **Service**: Outposts
     (com.amazonaws.`region`.outposts)


    Example:
     `com.amazonaws.`us-west-2`.outposts`
    + **Endpoint type**: Interface
    + **Private DNS Enabled**: set to false
     (disabled)
    + **VPC**: the VPC you created for private
     connectivity
    + **Subnet**: the subnet you created for private
     connectivity

Use the following **IAM policy document**:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "outposts:StartConnection",
 "outposts:GetConnection"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Principal": "*"
 }
 ]
}`

```

- Create a security group for the endpoint and authorize **inbound** TCP port 443 and ICMP traffic with addresses of
  `0.0.0.0/0` and with no **outbound**
  rules.

###### Note

To select the private connectivity option when your Outpost is in
**PENDING** status, choose **Outposts** from the AWS Outposts
console and select your Outpost. Choose **Actions**, **Add private
connectivity** and follow the steps.

After you select the private connectivity option for your Outpost, AWS Outposts automatically
creates a service-linked role in your account that enables it to complete the following tasks
on your behalf:

- Creates network interfaces in the subnet and VPC that you specify, and creates a
  security group for the network interfaces.
- Grants permission to the AWS Outposts service to attach the network interfaces to a service
  link endpoint instance in the account.
- Attaches the network interfaces to the service link endpoint instances from the
  account.
  For more information about the service-linked role, see [Service-linked roles
  for AWS Outposts](using-service-linked-roles.md "using-service-linked-roles.md").

###### Important

After your Outpost is installed, confirm connectivity to the private IPs in your subnet
from your Outpost.

###### Note

VPC configuration cannot be changed after order placement. If incorrect VPC specifications are provided during ordering, the Outpost must be decommissioned and a new order placed.

## Option 1. Private connectivity through Direct Connect

private VIFs

Create an AWS Direct Connect connection, private virtual interface, and virtual private
gateway to allow your on-premises Outpost to access the VPC.

For more information, see the following sections in the
_Direct Connect User Guide_:

- [Dedicated and hosted
  connections](../../../directconnect/latest/UserGuide/WorkingWithConnections.md "../../../directconnect/latest/UserGuide/WorkingWithConnections.md")
- [Create a private virtual
  interface](../../../directconnect/latest/UserGuide/create-private-vif.md "../../../directconnect/latest/UserGuide/create-private-vif.md")
- [Virtual private gateway
  associations](../../../directconnect/latest/UserGuide/virtualgateways.md "../../../directconnect/latest/UserGuide/virtualgateways.md")

If the AWS Direct Connect connection is in a different AWS account from your VPC, see
[Associating a
virtual private gateway across accounts](../../../directconnect/latest/UserGuide/multi-account-associate-vgw.md "../../../directconnect/latest/UserGuide/multi-account-associate-vgw.md") in the
_Direct Connect User Guide_.

## Option 2. Private connectivity through Direct Connect

transit VIFs

Create an AWS Direct Connect connection, transit virtual interface, and transit gateway to
allow your on-premises Outpost to access the VPC.

For more information, see the following sections in the
_Direct Connect User Guide_:

- [Dedicated and hosted
  connections](../../../directconnect/latest/UserGuide/WorkingWithConnections.md "../../../directconnect/latest/UserGuide/WorkingWithConnections.md")
- [Create a transit
  virtual interface to the Direct Connect gateway](../../../directconnect/latest/UserGuide/create-transit-vif-dx.md "../../../directconnect/latest/UserGuide/create-transit-vif-dx.md")
- [Transit
  gateway associations](../../../directconnect/latest/UserGuide/direct-connect-transit-gateways.md "../../../directconnect/latest/UserGuide/direct-connect-transit-gateways.md")
