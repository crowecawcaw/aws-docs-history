# Delete a prefix list reference in AWS Transit Gateway

If you no longer need a prefix list reference, you can delete it from your transit gateway route table. Deleting the reference does not delete the prefix list.

###### To delete a prefix list reference using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit Gateway Route
   Tables**.
3. Select the transit gateway route table.
4. Choose the prefix list reference, and choose **Delete
   references**.
5. Choose **Delete references**.

###### To modify a prefix list reference using the AWS CLI

Use the [delete-transit-gateway-prefix-list-reference](../../../cli/latest/reference/ec2/delete-transit-gateway-prefix-list-reference.md "../../../cli/latest/reference/ec2/delete-transit-gateway-prefix-list-reference.md") command.
