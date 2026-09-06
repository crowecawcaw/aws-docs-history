

# Access a service network through a service-network endpoint
<a name="access-with-service-network-endpoint"></a>

You can access a service network using a service-network endpoint. A service-network endpoint provides private access to resource configurations and services in the service network.

## Prerequisites
<a name="prerequisites-sn-endpoints"></a>

To create a service-network endpoint, you must meet the following prerequisites.
+ You must have a service network that was either created by you or shared with you from another account through AWS RAM.
+ If a service network is shared with you from another account, you must review and accept the resource share that contains the service network. For more information, see [Accepting and rejecting invitations](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-invitations.html) in the *AWS RAM User Guide*.
+ For VPC Lattice services associated with the service network, the service-network endpoint requires a contiguous /28 block (16 IPv4 addresses) per Availability Zone. This /28 block is allocated when the endpoint is created, even if no services are currently in the service network. The /28 block must consist of 16 contiguous, unoccupied IPv4 addresses and cannot overlap with the five AWS-reserved addresses (first four and last IP in the subnet). For IPv6, a /80 block per Availability Zone is allocated for VPC Lattice services. Ensure that sufficient free contiguous address space is available in each subnet you select.
+ For VPC Lattice resources (Layer 4/TCP) associated with the service network, one IPv4 address per resource configuration per Availability Zone is required. Contiguous address space is not required. Up to 63 IP addresses can be allocated per elastic network interface. When additional resource configurations exceed this limit, an additional elastic network interface is created in the same subnet. For IPv6, a /80 block is assigned on the first elastic network interface created for resources; no additional elastic network interfaces are created when using IPv6.

If you need to avoid consuming VPC CIDR IP addresses, or anticipate a large number of resource configurations associated with the service network, consider using a service network VPC association instead. For more information, see [Manage VPC endpoint associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-endpoint-associations) in the *Amazon VPC Lattice User Guide*.

## Create a service network endpoint
<a name="create-service-network-endpoint"></a>

Create a service-network endpoint to access the service network that was shared with you. After you create a service-network endpoint, you can only modify its security groups or tags.

**To create a service-network endpoint**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **PrivateLink and Lattice**, choose **Endpoints**.

1. Choose **Create endpoint**.

1. You can specify a name to make it easier to find and manage the endpoint.

1. For **Type**, choose **Service networks**.

1. For **Service networks**, select the service network.

1. For **Network settings**, select your VPC from which you'll access the service network.

1. If, you want to configure private DNS support, select **Additional settings**, **Enable private DNS name**. To use this feature, ensure that the attributes **Enable DNS hostnames** and **Enable DNS support** are enabled for your VPC.

1. For **Subnets**, select a subnet to create the endpoint network interface in.

   In a production environment, for high availability and resiliency, we recommend configuring at least two Availability Zones for each VPC endpoint.

1. For **Security groups**, select a security group.

   If you do not specify a security group, we associate the default security group for the VPC.

1. Choose **Create endpoint**.

**To create a service-network endpoint using the command line**
+ [create-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint.html) (AWS CLI)
+ [New-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2VpcEndpoint.html) (Tools for Windows PowerShell)