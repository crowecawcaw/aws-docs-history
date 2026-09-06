

# Delete a static route in AWS Transit Gateway
<a name="tgw-delete-static-route"></a>

Delete static routes from a transit gateway route table.

**To delete a static route using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the route table for which to delete the route, and choose **Routes**.

1. Choose the route to delete.

1. Choose **Delete static route**.

1. In the confirmation box, choose **Delete static route**.

**To delete a static route using the AWS CLI**  
Use the [delete-transit-gateway-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-transit-gateway-route.html) command.