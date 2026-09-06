

# Create a static route in AWS Transit Gateway
<a name="tgw-create-static-route"></a>

Create a static route for a VPC, VPN, or transit gateway peering attachment, or you can create a blackhole route that drops traffic that matches the route.

Static routes in a transit gateway route table that target a VPN attachment are not filtered by the Site-to-Site VPN. This might allow unintended outbound traffic flow when using a BGP-based VPN.

**To create a static route using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the route table for which to create a route.

1. Choose **Actions**, **Create static route**.

1. On the **Create static route** page, enter the CIDR block for which to create the route, and then choose **Active**.

1. Choose the attachment for the route.

1. Choose **Create static route**.

**To create a blackhole route using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the route table for which to create a route.

1. Choose **Actions**, **Create static route**.

1. On the **Create static route** page, enter the CIDR block for which to create the route, and then choose **Blackhole**.

1. Choose **Create static route**.

**To create a static route or blackhole route using the AWS CLI**  
Use the [create-transit-gateway-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-transit-gateway-route.html) command.