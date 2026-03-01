# Create and Configure a New VPC

This topic describes how to use the VPC wizard to create a VPC with a
public subnet and one private subnet. As part of this process, the wizard
creates an internet gateway and a NAT gateway. It also creates a custom route
table associated with the public subnet and updates the main route table
associated with the private subnet. The NAT gateway is automatically created in
the public subnet of your VPC.

After you use the wizard to create the initial
VPC configuration, you'll add a second private subnet. For more information
about this configuration, see [VPC with Public and Private Subnets (NAT)](../../../vpc/latest/userguide/VPC_Scenario2.md "../../../vpc/latest/userguide/VPC_Scenario2.md") in the _Amazon VPC User Guide_.

###### Note

If you already have a VPC, complete the steps in [Add a NAT Gateway to an Existing VPC](add-nat-gateway-existing-vpc.md "add-nat-gateway-existing-vpc.md") instead.

###### Contents

- [Step 1: Allocate an Elastic IP Address](#allocate-elastic-ip "#allocate-elastic-ip")
- [Step 2: Create a New VPC](#vpc-with-private-and-public-subnets-nat "#vpc-with-private-and-public-subnets-nat")
- [Step 3: Add a Second Private Subnet](#vpc-with-private-and-public-subnets-add-private-subnet-nat "#vpc-with-private-and-public-subnets-add-private-subnet-nat")
- [Step 4: Verify and Name Your Subnet Route Tables](#verify-name-route-tables "#verify-name-route-tables")

## Step 1: Allocate an Elastic IP Address

Before you create your VPC, you must allocate an Elastic IP address in
your WorkSpaces Applications Region. You must first allocate an Elastic IP address for use in
your VPC, and then associate it with your NAT gateway. For more information,
see [Elastic
IP Addresses](../../../vpc/latest/userguide/vpc-eips.md "../../../vpc/latest/userguide/vpc-eips.md") in the _Amazon VPC User
Guide_.

###### Note

Charges may apply to Elastic IP addresses that you use. For more information, see [Elastic IP Addresses](https://aws.amazon.com/ec2/pricing/on-demand/#Elastic_IP_Addresses "https://aws.amazon.com/ec2/pricing/on-demand/#Elastic_IP_Addresses") on the Amazon EC2 pricing page.

Complete the following steps if you don't already have an Elastic IP address. If you want to use an existing Elastic IP address, verify that it's not currently associated with another instance or network interface.

###### To allocate an Elastic IP address

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Network & Security**, choose **Elastic IPs**.
3. Choose **Allocate New Address**, and then choose **Allocate**.
4. Note the Elastic IP address.
5. In the upper right of the **Elastic IPs** pane, click the X icon to close the pane.

## Step 2: Create a New VPC

Complete the following steps to create a new VPC with a public subnet and one private subnet.

###### To create a new VPC

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **VPC Dashboard**.
3. Choose **Launch VPC Wizard**.
4. In **Step 1: Select a VPC Configuration**, choose **VPC with Public
   and Private Subnets**, and then choose **Select**.
5. In **Step 2: VPC with Public and Private Subnets**, configure the VPC as follows:
   - For **IPv4 CIDR block**, specify an IPv4 CIDR block for the VPC.
   - For **IPv6 CIDR block**, keep the default value, **No IPv6 CIDR Block**.
   - For **VPC name**, type a unique name for the VPC.

6. Configure the public subnet as follows:
   - For **Public subnet's IPv4 CIDR**, specify the CIDR block for the
     subnet.
   - For **Availability Zone**, keep the default value, **No Preference**.
   - For **Public subnet name**, type a name for the subnet; for example,
     `AppStream2 Public Subnet`.

7. Configure the first private subnet as follows:
   - For **Private subnet's IPv4 CIDR**, specify the CIDR block for the subnet.
     Make a note of the value that you specify.
   - For **Availability Zone**, select a specific zone and make a note of the zone that you select.
   - For **Private subnet name**, type a name for the subnet; for example,
     `AppStream2 Private Subnet1`.
   - For the remaining fields, where applicable, keep the default values.

8. For **Elastic IP Allocation ID**, click in the text box and select the value
   that corresponds to the Elastic IP address that you created. This
   address is assigned to the NAT gateway. If you don't have an Elastic
   IP address, create one by using the
   Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
9. For **Service endpoints**, if an Amazon S3 endpoint is required for your
   environment, specify one. An S3 endpoint is required to provide
   users with access to [home
   folders](home-folders.md "home-folders.md") or to enable [application settings
   persistence](app-settings-persistence.md "app-settings-persistence.md") for your users in a private network.

To specify an Amazon S3 endpoint, do the following:

    1. Choose **Add Endpoint**.
    2. For **Service**, select the entry in the list that ends with "s3" (the `com.amazonaws.``region``.s3` entry that corresponds to the Region in which the VPC is being created).
    3. For **Subnet**, choose **Private subnet**.
    4. For **Policy**, keep the default value, **Full Access**.

10. For **Enable DNS hostnames**, keep the default value, **Yes**.
11. For **Hardware tenancy**, keep the default value, **Default**.
12. Choose **Create VPC**.
13. Note that it takes several minutes to set up your VPC. After the VPC is created, choose **OK**.

## Step 3: Add a Second Private Subnet

In the previous step ([Step 2: Create a New VPC](#vpc-with-private-and-public-subnets-nat "#vpc-with-private-and-public-subnets-nat")), you created a VPC with one public subnet and one private subnet. Perform the following steps to add a second private subnet. We recommend that you add a second private subnet in a different
Availability Zone than your first private subnet.

1. In the navigation pane, choose
   **Subnets**.
2. Select the first private subnet that you created in the previous step. On the **Description** tab, below the list of subnets, make a note of the Availability Zone for this subnet.
3. On the upper left of the subnets pane, choose **Create Subnet**.
4. For **Name tag**, type a name for the private subnet; for example,
   `AppStream2 Private Subnet2`.
5. For **VPC**, select the VPC that you created in the previous step.
6. For **Availability Zone**, select an Availability Zone other than the one you
   are using for your first private subnet. Selecting a
   different Availability Zone increases fault tolerance
   and helps prevent insufficient capacity errors.
7. For **IPv4 CIDR block**, specify a unique
   CIDR block range for the new subnet. For example, if your first private subnet has an IPv4 CIDR block range of
   `10.0.1.0/24`, you could specify a CIDR
   block range of `10.0.2.0/24` for the new private subnet.
8. Choose **Create**.
9. After your subnet is created, choose **Close**.

## Step 4: Verify and Name Your Subnet Route Tables

After you've created and configured your VPC, complete the following steps to specify a name for your route tables, and to verify that:

- The route table associated with the subnet in which your NAT gateway resides includes a route that points internet traffic to an internet gateway. This ensures that your NAT gateway can access the internet.
- The route tables associated with your private subnets are configured to point internet
  traffic to the NAT gateway. This enables the streaming instances in your
  private subnets to communicate with the internet.

1. In the navigation pane, choose **Subnets**, and
   select the public subnet that you created; for example, `WorkSpaces Applications
Public Subnet`.
   1. On the **Route Table** tab, choose the ID
      of the route table; for example,
      `rtb-12345678`.
   2. Select the route table. Under **Name**,
      choose the edit icon (the pencil), and type a name (for
      example, `appstream2-public-routetable`), and
      then select the check mark to save the name.
   3. With the public route table still selected, on the **Routes** tab, verify that
      there is one route for local traffic and another route that sends all
      other traffic to the internet gateway for the VPC. The following table describes these two routes:

   | Destination                                                             | Target                | Description                                                                                                                                    |
   | ----------------------------------------------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
   | Public subnet IPv4 CIDR Block (for example, 10.0.0/20)                  | Local                 | All traffic from the resources destined for IPv4 addresses within the public subnet IPv4 CIDR block is routed locally within the VPC.          |
   | Traffic destined to all other IPv4<br>addresses (for example, 0.0.0.0/0 | Outbound (`igw-``ID`) | Traffic destined for all other IPv4 addresses is routed to the internet gateway (identified by `igw-``ID`) that was created by the VPC Wizard. |

2. In the navigation pane, choose **Subnets**, and select the first
   private subnet that you created (for example, `AppStream2 Private Subnet1`).
   1. On the **Route Table** tab, choose the ID of the route
      table.
   2. Select the route table. Under **Name**, choose the edit icon (the pencil), and enter a name (for example,
      `appstream2-private-routetable`), and then choose the check mark to save the
      name.
   3. On the **Routes** tab, verify that the route table includes the following routes:

   | Destination                                                                                                                 | Target                | Description                                                                                                                           |
   | --------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
   | Public subnet IPv4 CIDR Block (for example, 10.0.0/20)                                                                      | Local                 | All traffic from the resources destined for IPv4 addresses within the public subnet IPv4 CIDR block is routed locally within the VPC. |
   | Traffic destined to all other IPv4 addresses (for example, 0.0.0.0/0                                                        | Outbound (`nat-``ID`) | Traffic destined for all other IPv4 addresses is routed to the NAT gateway (identified by `nat-``ID`).                                |
   | Traffic destined for S3 buckets (applicable if you specified an S3 endpoint)<br>[`pl-``ID` (`com.amazonaws.``region``.s3`)] | Storage (`vpce-``ID`) | Traffic destined for S3 buckets is routed to the S3 endpoint (identified by `vpce-``ID`).                                             |

3. In the navigation pane, choose **Subnets**, and select the second
   private subnet that you created (for example, `AppStream2 Private Subnet2`).
4. On the **Route Table** tab, verify that the route table is the
   private route table (for example, `appstream2-private-routetable`). If the
   route table is different, choose **Edit** and select this route table.

**Next Steps**

To enable your fleet instances, app block builders, and image builders to
access the internet, complete the steps in [Enable Internet Access for Your Fleet, Image Builder, or App Block Builder in Amazon WorkSpaces Applications](managing-network-manual-enable-internet-access.md "managing-network-manual-enable-internet-access.md").
