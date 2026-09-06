

# Associate a transit gateway route table in AWS Transit Gateway
<a name="associate-tgw-route-table"></a>

You can associate a transit gateway route table with a transit gateway attachment.

**To associate a transit gateway route table using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the route table.

1. In the lower part of the page, choose the **Associations** tab.

1. Choose **Create association**.

1. Choose the attachment to associate and then choose **Create association**.

**To associate a transit gateway route table using the AWS CLI**  
Use the [associate-transit-gateway-route-table](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-transit-gateway-route-table.html) command.