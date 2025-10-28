# Delete an association for a transit gateway

route table in AWS Transit Gateway

You can disassociate a transit gateway route table from a transit gateway attachment.

###### To disassociate a transit gateway route table using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Route
   Tables**.
3. Select the route table.
4. In the lower part of the page, choose the **Associations**
   tab.
5. Choose the attachment to disassociate and then choose **Delete association**.
6. When prompted for confirmation, choose **Delete association**.

###### To disassociate a transit gateway route table using the AWS CLI

Use the [disassociate-transit-gateway-route-table](../../../cli/latest/reference/ec2/disassociate-transit-gateway-route-table.md "../../../cli/latest/reference/ec2/disassociate-transit-gateway-route-table.md") command.
