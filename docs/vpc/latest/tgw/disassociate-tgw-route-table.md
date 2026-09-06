

# Delete an association for a transit gateway route table in AWS Transit Gateway
<a name="disassociate-tgw-route-table"></a>

You can disassociate a transit gateway route table from a transit gateway attachment.

**To disassociate a transit gateway route table using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the route table.

1. In the lower part of the page, choose the **Associations** tab.

1. Choose the attachment to disassociate and then choose **Delete association**.

1. When prompted for confirmation, choose **Delete association**.

**To disassociate a transit gateway route table using the AWS CLI**  
Use the [disassociate-transit-gateway-route-table](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-transit-gateway-route-table.html) command.