# Enable route propagation to a transit gateway route

table in AWS Transit Gateway

Use route propagation to add a route from an attachment to a route table.

###### To propagate a route to a transit gateway attachment route table

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Route
   Tables**.
3. Select the route table for which to create a propagation.
4. Choose **Actions**, **Create
   propagation**.
5. On the **Create propagation** page, choose the attachment.
6. Choose **Create propagation**.

###### To enable route propagation using the AWS CLI

Use the [enable-transit-gateway-route-table-propagation](../../../cli/latest/reference/ec2/enable-transit-gateway-route-table-propagation.md "../../../cli/latest/reference/ec2/enable-transit-gateway-route-table-propagation.md") command.
