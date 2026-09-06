

# Manage subnet route tables
<a name="WorkWithRouteTables"></a>

Use the following procedures to manage VPC routing using route tables.

**Topics**
+ [Determine the route table for a subnet](#SubnetRouteTables)
+ [Determine the explicit associations](#Route_Which_Associations)
+ [Add, modify, and remove routes](#AddRemoveRoutes)
+ [Enable or disable route propagation](#EnableDisableRouteProp)
+ [Change the route table for a subnet](#ChangeRouteTable)

## Determine the route table for a subnet
<a name="SubnetRouteTables"></a>

You can determine which route table a subnet is associated with by looking at the subnet details in the Amazon VPC console.

**To determine the route table for a subnet using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Subnets**.

1. Select the subnet.

1. Choose the **Route table** tab to view information about the route table and its routes. To determine whether the association is to the main route table, and if that association is explicit, see [Determine the explicit associations](#Route_Which_Associations).

## Determine the explicit associations
<a name="Route_Which_Associations"></a>

You can determine how many and which subnets or gateways are explicitly associated with a route table.

The main route table can have explicit and implicit subnet associations. Custom route tables have only explicit associations.

Subnets that aren't explicitly associated with any route table have an implicit association with the main route table. You can explicitly associate a subnet with the main route table. For an example of why you might do that, see [Replace the main route table](Route_Replacing_Main_Table.md).

**To determine which subnets are explicitly associated using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**.

1. Check the **Explicit subnet association** column to determine the explicitly associated subnets and the **Main** column to determine whether this is the main route table.

1. Select the route table and choose the **Subnet associations** tab.

1. The subnets under **Explicit subnet associations** are explicitly associated with the route table. The subnets under **Subnets without explicit associations** belong to the same VPC as the route table, but are not associated with any route table, so they are implicitly associated with the main route table for the VPC.

**To determine which gateways are explicitly associated using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**.

1. Select the route table and choose the **Edge associations** tab.

**To describe one or more route tables and view its associations using the AWS CLI**  
Use the [describe-route-tables](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-route-tables.html) command.

## Add, modify, and remove routes
<a name="AddRemoveRoutes"></a>

You can add, modify, and delete routes for your route tables.

For more information about working with static routes for a Site-to-Site VPN connection, see [Editing Static Routes for a Site-to-Site VPN Connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-edit-static-routes) in the *AWS Site-to-Site VPN User Guide*.

**Considerations**
+ You can only modify routes that you've added.
+ When you modify or delete a route, existing connections that use these routes are affected. Connections that use the other routes are not affected.
+ There is a quota on the number of routes that you can add per route table. For more information, see [Amazon VPC quotas](amazon-vpc-limits.md).

**To update the routes for a route table using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**, and select the route table.

1. Choose **Actions**, **Edit routes**.

1. To add a route, choose **Add route**. For **Destination** enter an IP address range, a single IP address, or the ID of a prefix list. For **Target**, select the resource type and then enter the ID of the resource.

1. To modify a route, enter the new destination CIDR block or prefix list ID and choose a target.

1. To delete a route, choose **Remove**.

1. Choose **Save changes**.

**To update the routes for a route table using the AWS CLI**

If you add a route using a command line tool or the API, the destination CIDR block is automatically modified to its canonical form. For example, if you specify `100.68.0.18/18` for the CIDR block, we create a route with a destination CIDR block of `100.68.0.0/18`.
+ [create-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-route.html)
+ [replace-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/replace-route.html)
+ [delete-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-route.html)

## Enable or disable route propagation
<a name="EnableDisableRouteProp"></a>

Route propagation allows a virtual private gateway to automatically propagate routes to your route tables. This means that you don't need to manually add or remove VPN routes.

To complete this process, you must have a virtual private gateway.

For more information, see [Site-to-Site VPN routing options](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNRoutingTypes.html) in the *Site-to-Site VPN User Guide*.

**To enable or disable route propagation using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**, and then select the route table.

1. Choose **Actions**, **Edit route propagation**.

1. Select or clear the **Enable** check box next to the virtual private gateway.

1. Choose **Save**.

**To enable or disable route propagation using the AWS CLI**
+ [enable-vgw-route-propagation](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-vgw-route-propagation.html)
+ [disable-vgw-route-propagation](https://docs.aws.amazon.com/cli/latest/reference/ec2/disable-vgw-route-propagation.html)

## Change the route table for a subnet
<a name="ChangeRouteTable"></a>

You can change the route table association for a subnet.

When you change the route table, your existing connections in the subnet are dropped unless the new route table contains a route for the same traffic to the same target.

**To change a subnet route table association using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Subnets**, and then select the subnet.

1. From the **Route table** tab, choose **Edit route table association**.

1. For **Route table ID**, select the new route table.

1. Choose **Save**.

**To change the route table associated with a subnet using the AWS CLI**  
Use the [replace-route-table-association](https://docs.aws.amazon.com/cli/latest/reference/ec2/replace-route-table-association.html) command.