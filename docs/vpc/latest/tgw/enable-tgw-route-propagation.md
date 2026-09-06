

# Enable route propagation to a transit gateway route table in AWS Transit Gateway
<a name="enable-tgw-route-propagation"></a>

Use route propagation to add a route from an attachment to a route table.

**To propagate a route to a transit gateway attachment route table**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the route table for which to create a propagation.

1. Choose **Actions**, **Create propagation**.

1. On the **Create propagation** page, choose the attachment.

1. Choose **Create propagation**.

**To enable route propagation using the AWS CLI**  
Use the [enable-transit-gateway-route-table-propagation](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-transit-gateway-route-table-propagation.html) command.