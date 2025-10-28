# Set up the Amazon VPC where your Amazon Neptune DB cluster is located

An Amazon Neptune DB cluster can _only_ be created in an Amazon Virtual Private Cloud
(Amazon VPC). Its endpoints are accessible within that VPC, and if [Neptune public endpoints](neptune-public-endpoints.md "neptune-public-endpoints.md") are enabled,
they can also be accessed outside of the VPC and over the internet.

There are a number of different ways to set up the VPC, depending on how you
want to access your DB cluster.

Here are some things to keep in mind when configuring the VPC where
your Neptune DB cluster is located:

- Your VPC must have at least two [subnets](#security-vpc-add-subnets "#security-vpc-add-subnets"). These subnets must be in two
  different Availability Zones (AZs). By distributing your cluster instances across
  at least two AZs, Neptune helps ensure that there are always instances available
  in your DB cluster even in the unlikely event of an availability zone failure.
  The cluster volume for your Neptune DB cluster always spans three AZs to provide
  durable storage with extremely low likelihood of data loss.
- The CIDR blocks in each subnet must be large enough to provide
  IP addresses that Neptune may need during maintenance activities, failover,
  and scaling.
- The VPC must have a DB subnet group that contains subnets that you
  have created. Neptune chooses one of the subnets in the subnet group and an IP
  address within that subnet to associate with each DB instance in the DB cluster.
  The DB instance is then located in the same AZ as the subnet.
- The VPC should have [DNS
  enabled](#get-started-vpc-dns "#get-started-vpc-dns") (both DNS hostnames and DNS resolution).
- The VPC must have a [VPC
  security group](#security-vpc-security-group "#security-vpc-security-group") to allows access to your DB cluster.
- Tenancy in a Neptune VPC should be set to
  **Default**.

## Adding subnets to the VPC where your Neptune DB cluster is located

A subnet is a range of IP addresses in your VPC. You can launch resources such as
a Neptune DB cluster or an EC2 instance into a specific subnet. When you create a
subnet, you specify the IPv4 CIDR block for the subnet, which is a subset of the VPC
CIDR block. Each subnet must reside entirely within one Availability Zone (AZ) and
cannot span zones. By launching instances in separate Availability Zones, you can
protect your applications from a failure in one of the zones. See [VPC subnet documentation](../../../vpc/latest/userguide/configure-subnets.md "../../../vpc/latest/userguide/configure-subnets.md") for
more information.

A Neptune DB cluster requires at least two VPC subnets.

###### To add subnets to a VPC

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Subnets**.
3. In the **VPC Dashboard** choose **Subnets**,
   and then choose **Create subnet**.
4. On the **Create subnet** page, choose the VPC where you
   want to create the subnet.
5. Under **Subnet settings**, make the following choices:
   1. Enter a name for the new subnet under **Subnet name**.
   2. Choose an Availability Zone (AZ) for the subnet, or leave the choice
      at **No preference**.
   3. Enter the subnet's IP address block under **IPv4 CIDR block**.
   4. Add tags to the subnet if you need to.
   5. Choose

6. If you want to create another subnet at the same time, choose
   **Add new subnet**.
7. Choose **Create subnet** to create the new subnet(s).

## Configuring VPC in Amazon Neptune

Create a subnet group.

###### To create a Neptune subnet group

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. Choose **Subnet groups**, and then choose **Create
   DB Subnet Group**.
3. Enter a name and description for the new subnet group (the description is
   required).
4. Under **VPC**, choose the VPC where you want this subnet
   group to be located.
5. Under **Avalability zone**, choose the AZ where you want
   this subnet group to be located.
6. Under **Subnet**, add one or more of the subnets in this
   AZ to this subnet group.
7. Choose **Create** to create the new subnet group.

## Create a security group using the VPC console

Security groups provide access to your Neptune DB cluster in the VPC. They act
as a firewall for the associated DB cluster, controlling both inbound and outbound
traffic at the instance level. By default, a DB instance is created with a firewall
and a default security group that prevents any access to it. To enable access, you
must have a VPC security group with additional rules.

The following procedure shows you how to add a custom TCP rule that specifies
the port range and IP addresses for the Amazon EC2 instance to use to access your Neptune
DB cluster. You can use the VPC security group assigned to the EC2 instance rather
than its IP address.

###### To create a VPC security group for Neptune on the console

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the upper-right corner of the console, choose the AWS region where
   you want to create a VPC security group for Neptune. In the list of Amazon VPC
   resources for that region, it should show that you have at least one VPC and several
   subnets. If it does not, you don't have a default VPC in that Region.
3. In the navigation pane under **Security**, choose
   **Security Groups**.
4. Choose **Create security group**. In the **Create
   security group** window, enter the **Security group name**,
   a **Description**, and the identifier of the VPC where your
   Neptune DB cluster will reside.
5. Add an inbound rule for the security group of an Amazon EC2 instance that you want
   connected to your Neptune DB cluster:
   1. In the **Inbound rules** area, choose **Add rule**.
   2. In the **Type** list, leave **Custom TCP** selected.
   3. In the **Port range** box, enter **8182**,
      the default port value for Neptune.
   4. Under **Source**, enter the IP address range (CIDR value)
      from which you will access Neptune, or choose an existing security group name.
   5. If you need to add more IP addresses or different port ranges, choose
      **Add rule** again.

6. In the Outbound rules area, you can also add one or more outbound rules
   if you need to.
7. When you finish, choose **Create security group**.

You can use this new VPC security group when you create a new Neptune DB cluster.

If you use a default VPC, a default subnet group spanning all of the VPC's subnets is
already created for you. When you choose the **Create database** in the
Neptune console, the default VPC is used unless you specify a different one.

## Make sure that you have DNS support in your VPC

Domain Name System (DNS) is a standard by which names used on the internet are resolved to
their corresponding IP addresses. A DNS hostname uniquely names a computer and consists
of a host name and a domain name. DNS servers resolve DNS hostnames to their corresponding
IP addresses.

Check to make sure that DNS hostnames and DNS resolution are both enabled
in your VPC. The VPC network attributes `enableDnsHostnames` and
`enableDnsSupport` must be set to `true`. To view and modify
these attributes, go to the VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").

For more information, see [Using DNS with your
VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md").

###### Note

If you are using Route 53, confirm that your configuration does not override DNS
network attributes in your VPC.
