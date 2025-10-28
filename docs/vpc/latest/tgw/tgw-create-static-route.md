# Create a static route in AWS Transit Gateway

Create a static route for a VPC, VPN, or transit gateway peering
attachment, or you can create a blackhole route that drops traffic that matches the
route.

Static routes in a transit gateway route table that target a VPN attachment are not
filtered by the Site-to-Site VPN. This might allow unintended outbound traffic flow when
using a BGP-based VPN.

###### To create a static route using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Route
   Tables**.
3. Select the route table for which to create a route.
4. Choose **Actions**, **Create static
   route**.
5. On the **Create static route** page, enter the CIDR block
   for which to create the route, and then choose **Active**.
6. Choose the attachment for the route.
7. Choose **Create static route**.

###### To create a blackhole route using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Route
   Tables**.
3. Select the route table for which to create a route.
4. Choose **Actions**, **Create static
   route**.
5. On the **Create static route** page, enter the CIDR block for
   which to create the route, and then choose
   **Blackhole**.
6. Choose **Create static route**.

###### To create a static route or blackhole route using the AWS CLI

Use the [create-transit-gateway-route](../../../cli/latest/reference/ec2/create-transit-gateway-route.md "../../../cli/latest/reference/ec2/create-transit-gateway-route.md") command.
