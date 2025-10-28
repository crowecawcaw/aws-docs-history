# Add a route to a transit gateway route table using

AWS Transit Gateway

To route traffic between the peered transit gateways, you must add a static route to
the transit gateway route table that points to the transit gateway peering attachment.
The owner of the accepter transit gateway must also add a static route to their transit gateway's
route table.

###### To create a static route using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Route
   Tables**.
3. Select the route table for which to create a route.
4. Choose **Actions**, **Create static
   route**.
5. On the **Create static route** page, enter the CIDR block for
   which to create the route. For example, specify the CIDR block of a VPC that's
   attached to the peer transit gateway.
6. Choose the peering attachment for the route.
7. Choose **Create static route**.

###### To create a static route using the AWS CLI

Use the [create-transit-gateway-route](../../../cli/latest/reference/ec2/create-transit-gateway-route.md "../../../cli/latest/reference/ec2/create-transit-gateway-route.md") command.

###### Important

After you create the route, the transit gateway peering attachment must already be
associated with the transit gateway route table. For more information, see [Associate a transit gateway route table in AWS Transit Gateway](associate-tgw-route-table.md "associate-tgw-route-table.md").
