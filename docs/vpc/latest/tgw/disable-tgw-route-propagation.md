

# Disable route propagation in AWS Transit Gateway
<a name="disable-tgw-route-propagation"></a>

Remove a propagated route from a route table attachment.

**To disable route propagation using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the route table to delete the propagation from.

1. On the lower part of the page, choose the **Propagations** tab.

1. Select the attachment and then choose **Delete propagation**.

1. When prompted for confirmation, choose **Delete propagation**.

**To disable route propagation using the AWS CLI**  
Use the [disable-transit-gateway-route-table-propagation](https://docs.aws.amazon.com/cli/latest/reference/ec2/disable-transit-gateway-route-table-propagation.html) command.