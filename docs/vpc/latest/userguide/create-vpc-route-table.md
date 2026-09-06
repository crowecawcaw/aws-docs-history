

# Create a route table for your VPC
<a name="create-vpc-route-table"></a>

Complete the following tasks to create and configure a custom route table for your VPC. By default your new route table contains local routes that allow communication within the VPC. You can add routes to direct network traffic to specific targets based on the destination IP address range.

To apply route table routes to a particular subnet, you must associate the route table with the subnet. A route table can be associated with multiple subnets. However, a subnet can only be associated with one route table at a time. Any subnet not explicitly associated with a table is implicitly associated with the main route table by default.

You can disassociate a subnet from a route table. Until you associate the subnet with another route table, it's implicitly associated with the main route table.

**Note**  
There is a quota on the number of route tables that you can create per VPC. There is also a quota on the number of routes that you can add per route table. For more information, see [Amazon VPC quotas](amazon-vpc-limits.md).

**Topics**
+ [Create the route table](#CustomRouteTable)
+ [Add routes to the route table](#AddRoutes)
+ [Associate a subnet with the route table](#AssociateSubnet)

## Create the route table
<a name="CustomRouteTable"></a>

**To create a route table using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**.

1. Choose **Create route table**.

1. (Optional) For **Name**, enter a name for your route table.

1. For **VPC**, choose your VPC.

1. (Optional) To add a tag, choose **Add new tag** and enter the tag key and tag value.

1. Choose **Create route table**.

**To create a route table using the AWS CLI**  
Use the [create-route-table](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-route-table.html) command.

## Add routes to the route table
<a name="AddRoutes"></a>

**To add routes to a route table using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**, and select the route table.

1. Choose **Actions**, **Edit routes**.

1. Choose **Add route**.

1. For **Destination** enter one of the following:
   + An IP address range - For example, 192.168.0.0/16
   + A single IP address - For example, 192.168.10.1/32
   + The ID of a prefix list - For example, pl-0abcdef1234567890

1. For **Target**, select a resource type (for example, a network interface) and then enter the ID of the resource (for example, eni-11223344556677889).

1. Choose **Save changes**.

**To add routes to a route table using the AWS CLI**  
Use the [create-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-route.html) command.

## Associate a subnet with the route table
<a name="AssociateSubnet"></a>

**To associate a route table with a subnet using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**, and then select the route table.

1. On the **Subnet associations** tab, choose **Edit subnet associations**.

1. Select the check box for the subnet to associate with the route table.

1. Choose **Save associations**.

**To associate or disassociate a subnet with a route table using the AWS CLI**
+ [associate-route-table](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-route-table.html)
+ [disassociate-route-table](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-route-table.html)