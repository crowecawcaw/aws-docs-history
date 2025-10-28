# Disable route propagation in AWS Transit Gateway

Remove a propagated route from a route table attachment.

###### To disable route propagation using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Route
   Tables**.
3. Select the route table to delete the propagation from.
4. On the lower part of the page, choose the **Propagations**
   tab.
5. Select the attachment and then choose **Delete propagation**.
6. When prompted for confirmation, choose **Delete propagation**.

###### To disable route propagation using the AWS CLI

Use the [disable-transit-gateway-route-table-propagation](../../../cli/latest/reference/ec2/disable-transit-gateway-route-table-propagation.md "../../../cli/latest/reference/ec2/disable-transit-gateway-route-table-propagation.md") command.
