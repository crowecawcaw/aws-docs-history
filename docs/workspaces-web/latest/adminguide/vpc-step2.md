

# Verifying your subnet route tables (optional)
<a name="vpc-step2"></a>

The VPC wizard automatically configures the route tables for you. If you created your VPC manually or want to confirm the configuration, you can verify that the following details are correct for your route table:
+ The route table associated with the subnet that your NAT gateway resides in must include a route that points internet traffic to an internet gateway. This ensures that your NAT gateway can access the internet. 
+ The route tables associated with your private subnets must be configured to point internet traffic to the NAT gateway. This enables the streaming instances in your private subnets to communicate with the internet. 

**To verify and name your subnet route tables**

1. In the navigation pane, choose **Subnets**, and then select a public subnet. For example, **WSB-VPC-subnet-public1-us-east-1a**. 

1. On the **Route Table** tab, choose the ID of the route table. For example, **rtb-12345678**. 

1. Select the route table. Under **Name**, choose the edit (pencil) icon, and enter a name for the table. For example, enter the name **workspacesweb-public-routetable**. Then select the check mark to save the name. 

1. With the public route table still selected, on the **Routes** tab, verify that there are two routes: one for local traffic, and one that sends all other traffic through the VPC's internet gateway. The following table describes these two routes: 


<table>
<thead>
  <tr><th>Destination</th><th>Target</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Public subnet IPv4 CIDR block (for example, 10.0.0/20)</td><td>Local</td><td>All traffic from the resources destined for IPv4 addresses within the public subnet IPv4 CIDR block. This traffic is routed locally within the VPC.</td></tr>
  <tr><td>Traffic destined to all other IPv4 addresses (for example, 0.0.0.0/0)</td><td>Outbound (igw-ID)</td><td>Traffic destined for all other IPv4 addresses is routed to the internet gateway (identified by igw-ID) that was created by the VPC wizard.</td></tr>
</tbody>
</table>


1. In the navigation pane, choose **Subnets**. Then, select a private subnet (for example, **WSB-VPC-subnet-private1-us-east-1a**). 

1. On the **Route Table** tab, choose the route table's ID. 

1. Select the route table. Under **Name**, choose the edit (pencil) icon, and enter a name for the table. For example, enter the name **WSB-VPC-private-routetable**. Then choose the check mark to save the name. 

1. On the **Routes** tab, verify that the route table includes the following routes:


<table>
<thead>
  <tr><th>Destination</th><th>Target</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>Public subnet IPv4 CIDR block (for example, 10.0.0/20)</td><td>Local</td><td>All traffic from the resources destined for IPv4 addresses within the public subnet IPv4 CIDR block is routed locally within the VPC.</td></tr>
  <tr><td>Traffic destined to all other IPv4 addresses (for example, 0.0.0.0/0)</td><td>Outbound (nat-ID)</td><td>Traffic destined for all other IPv4 addresses is routed to the NAT gateway (identified by nat-ID).</td></tr>
  <tr><td>Traffic destined for S3 buckets (applicable if you specified an S3 endpoint) [pl-ID (com.amazonaws.region.s3)]</td><td>Storage (vpce-ID)</td><td>Traffic destined for S3 buckets is routed to the S3 endpoint (identified by vpce-ID).</td></tr>
</tbody>
</table>


1. In the navigation pane, choose **Subnets**. Then select the second private subnet that you created (for example, **WorkSpaces Secure Browser Private Subnet2**). 

1. On the **Route Table** tab, verify that the selected route table is the private route table (for example, **workspacesweb-private-routetable**). If the route table is different, choose **Edit** and select your private route table instead. 