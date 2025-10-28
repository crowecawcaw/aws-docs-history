# Access a service network through a

service-network endpoint

You can access a service network using a service-network endpoint. A service-network
endpoint provides private access to resource configurations and services in the service
network.

## Prerequisites

To create a service-network endpoint, you must meet the following prerequisites.

- You must have a service network that was either created by you or shared with you from
  another account through AWS RAM.
- If a service network is shared with you from another account, you must review and accept
  the resource share that contains the service network. For more information, see [Accepting and rejecting invitations](../../../ram/latest/userguide/working-with-shared-invitations.md "../../../ram/latest/userguide/working-with-shared-invitations.md") in the
  _AWS RAM User Guide_.
- A service network endpoint initially requires a contiguous /28 block of IPv4 addresses
  available in an Availability Zone. If you add a resource configuration to the service network that is
  associated with your endpoint, you need an additional /28 block available in the same subnet,
  as each resource consumes a unique IP per Availability Zone.

If you plan on adding over 16 resource configurations to a service network, additional
/28 blocks are consumed on the service network endpoint to
accommodate new resources. We recommend that if you need to avoid using VPC CIDR IPs, you use
a service network VPC association. For more information, see [Manage VPC endpoint associations](../../../vpc-lattice/latest/ug/service-network-associations.md#service-network-vpc-endpoint-associations "../../../vpc-lattice/latest/ug/service-network-associations.md#service-network-vpc-endpoint-associations") in the _Amazon VPC Lattice User
Guide_.

## Create a service network endpoint

Create a service-network endpoint to access the service network that was shared with
you. After you create a service-network endpoint, you can only modify its security groups or tags.

###### To create a service-network endpoint

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **PrivateLink and Lattice**, choose **Endpoints**.
3. Choose **Create endpoint**.
4. You can specify a name to make it easier to find and manage the endpoint.
5. For **Type**, choose **Service networks**.
6. For **Service networks**, select the service network.
7. For **Network settings**, select your VPC from which you'll access the
   service network.
8. If, you want to configure private DNS support, select **Additional
   settings**, **Enable DNS name**. To use this feature, ensure that
   the attributes **Enable DNS hostnames** and **Enable DNS
   support** are enabled for your VPC.
9. For **Subnets**, select a subnet to create the endpoint network interface in.

In a production environment, for high availability and resiliency, we recommend configuring at least two Availability Zones for each VPC endpoint. 10. For **Security groups**, select a security group.

If you do not specify a security group, we associate the default security group for the VPC. 11. Choose **Create endpoint**.

###### To create a service-network endpoint using the command line

- [create-vpc-endpoint](../../../cli/latest/reference/ec2/create-vpc-endpoint.md "../../../cli/latest/reference/ec2/create-vpc-endpoint.md")
  (AWS CLI)
- [New-EC2VpcEndpoint](../../../powershell/latest/reference/items/New-EC2VpcEndpoint.md "../../../powershell/latest/reference/items/New-EC2VpcEndpoint.md")
  (Tools for Windows PowerShell)
