# Connecting to a database in a VPC

The following example shows how to connect a MySQL database running
in a virtual private cloud (VPC) . The example assumes that you're starting with
your default VPC and that you need to create a MySQL database. If you
already have a VPC, make sure that it's configured as shown. If you have a
MySQL database, you can use that instead of creating a new
one.

###### Steps

- [Step 1: Configure a VPC](#vpc-example-1 "#vpc-example-1")
- [Step 2: Create and configure security
  groups](#vpc-example-2 "#vpc-example-2")
- [Step 3: Create a database](#vpc-example-3 "#vpc-example-3")
- [Step 4: Create a data source connector](#vpc-example-4 "#vpc-example-4")

## Step 1: Configure a VPC

Configure your VPC so that you have a private subnet and a security group for
Amazon Kendra to access a MySQL database running in the
subnet. The subnets provided in the VPC configuration must be in the
US West (Oregon) Region, the US East (N. Virginia) Region, or the Europe (Ireland) Region.

###### To configure a VPC using Amazon VPC

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. From the navigation pane, choose **Route tables**,
   then choose **Create route table**.
3. For the **Name** field, enter `Private
subnet route table`. From the **VPC**
   dropdown, select your VPC, and then choose **Create route
   table**. Choose **Close** to return to the
   list of route tables.
4. From the navigation pane, choose **NAT gateways**,
   then choose **Create NAT gateway**.
5. From the **Subnet** dropdown, choose the subnet
   that's the public subnet. Make a note of the subnet ID.
6. If you don't have an Elastic IP address, choose **Create New
   EIP**, choose **Create a NAT Gateway**,
   and then choose **Close**.
7. From the navigation pane, choose **Route
   tables**.
8. From the route table list, choose the **Private subnet route
   table** that you created in step 3. From
   **Actions**, choose **Edit
   routes**.
9. Choose **Add route**. For the destination, enter
   `0.0.0.0/0` to allow all outgoing traffic to
   the internet. For **Target**, choose **NAT
   Gateway**, and then choose the gateway that you created in
   step 4. Choose **Save changes**, and then choose
   **Close**.
10. From **Actions**, choose **Edit subnet
    associations**.
11. Choose the subnets that you want to be private. Don't choose the
    subnet with the NAT gateway that you noted previously. Choose
    **Save associations** when you're done.

## Step 2: Create and configure security

groups

Next, configure security groups for your database.

###### To create and configure security groups

1. Sign in to the AWS Management Console and open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. From the description of your VPC, note the IPv4 CIDR.
3. From the navigation pane, choose **Security groups**
   and then choose **Create security group**.
4. For **Security group name**, enter
   `DataSourceInboundSecurityGroup`. Provide a
   description, then choose your VPC from the list. Choose **Create
   security group** and then choose
   **Close**.
5. Choose the **Inbound rules** tab.
6. Choose **Edit inbound rules**, and then choose
   **Add rule**
7. For a database, enter the port number for the **Port
   range**. For example, for MySQL it's
   `3306`, and, for HTTPS, it's
   `443`. For the **Source**,
   type the Classless Inter-Domain Routing (CIDR) of your VPC. Choose
   **Save rules** and then choose
   **Close**.

The security group allows anyone within the VPC to connect to the database,
and it allows outbound connections to the internet.

## Step 3: Create a database

Create a database to hold your documents, or you can use your existing
database.

For instructions on how to create a MySQL database, see [MySQL](data-source-mysql.md "data-source-mysql.md").

## Step 4: Create a data source connector

After you configure your VPC and create your database, you can create a data
source connector for the database. For information about database connectors
that Amazon Kendra supports, see [Supported
connectors](data-sources.md "data-sources.md").

For your database, make sure that you configure your VPC, the private subnets
that you created in your VPC, and the security group that you created in your
VPC.
