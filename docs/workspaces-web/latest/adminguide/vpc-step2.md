

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces-web/latest/adminguide/vpc-step2.html)

1. In the navigation pane, choose **Subnets**. Then, select a private subnet (for example, **WSB-VPC-subnet-private1-us-east-1a**). 

1. On the **Route Table** tab, choose the route table's ID. 

1. Select the route table. Under **Name**, choose the edit (pencil) icon, and enter a name for the table. For example, enter the name **WSB-VPC-private-routetable**. Then choose the check mark to save the name. 

1. On the **Routes** tab, verify that the route table includes the following routes:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces-web/latest/adminguide/vpc-step2.html)

1. In the navigation pane, choose **Subnets**. Then select the second private subnet that you created (for example, **WorkSpaces Secure Browser Private Subnet2**). 

1. On the **Route Table** tab, verify that the selected route table is the private route table (for example, **workspacesweb-private-routetable**). If the route table is different, choose **Edit** and select your private route table instead. 