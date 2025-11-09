# Verifying and naming your subnet route tables

After you've created and configured your VPC, complete the following steps to
specify a name for your route tables. You'll need to verify that the following details
are correct for your route table:

- The route table associated with the subnet that your NAT gateway resides in must
  include a route that points internet traffic to an internet gateway. This ensures
  that your NAT gateway can access the internet.
- The route tables associated with your private subnets must be configured to
  point internet traffic to the NAT gateway. This enables the streaming instances in
  your private subnets to communicate with the internet.

###### To verify and name your subnet route tables

1. In the navigation pane, choose **Subnets**, and then select the
   public subnet that you created. For example, **WorkSpaces Secure Browser 2.0 Public
   Subnet**.
2. On the **Route Table** tab, choose the ID of the route table.
   For example, **rtb-12345678**.
3. Select the route table. Under **Name**, choose the edit
   (pencil) icon, and enter a name for the table. For example, enter the name
   `workspacesweb-public-routetable`. Then select the check mark
   to save the name.
4. With the public route table still selected, on the **Routes**
   tab, verify that there are two routes: one for local traffic, and one that sends all
   other traffic through the VPC's internet gateway. The following table describes
   these two routes:

| Destination                                                              | Target            | Description                                                                                                                                               |
| ------------------------------------------------------------------------ | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Public subnet IPv4 CIDR block (for example,<br>10.0.0/20)                | Local             | All traffic from the resources destined for IPv4 addresses within the<br>public subnet IPv4 CIDR block. This traffic is routed locally within the<br>VPC. |
| Traffic destined to all other IPv4 addresses (for example,<br>0.0.0.0/0) | Outbound (igw-ID) | Traffic destined for all other IPv4 addresses is routed to the internet<br>gateway (identified by igw-ID) that was created by the VPC wizard.             |

5. In the navigation pane, choose **Subnets**. Then, select the
   first private subnet that you created (for example, `WorkSpaces Secure Browser
Private Subnet1`).
6. On the **Route Table** tab, choose the route table's ID.
7. Select the route table. Under **Name**, choose the edit
   (pencil) icon, and enter a name for the table. For example, enter the name
   `workspacesweb-private-routetable`. Then choose the check
   mark to save the name.
8. On the **Routes** tab, verify that the route table includes the
   following routes:

| Destination                                                                                                       | Target            | Description                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Public subnet IPv4 CIDR block (for example,<br>10.0.0/20)                                                         | Local             | All traffic from the resources destined for IPv4 addresses within the<br>public subnet IPv4 CIDR block is routed locally within the VPC. |
| Traffic destined to all other IPv4 addresses (for example,<br>0.0.0.0/0)                                          | Outbound (nat-ID) | Traffic destined for all other IPv4 addresses is routed to the NAT<br>gateway (identified by nat-ID).                                    |
| Traffic destined for S3 buckets (applicable if you specified an S3<br>endpoint) [pl-ID (com.amazonaws.region.s3)] | Storage (vpce-ID) | Traffic destined for S3 buckets is routed to the S3 endpoint<br>(identified by vpce-ID).                                                 |

9. In the navigation pane, choose **Subnets**. Then select the
   second private subnet that you created (for example, `WorkSpaces Secure Browser
Private Subnet2`).
10. On the **Route Table** tab, verify that the selected route
    table is the private route table (for example,
    `workspacesweb-private-routetable`). If the route table is
    different, choose **Edit** and select your private route table
    instead.
