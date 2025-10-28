# Delete a Connect attachment in AWS Transit Gateway

If you no longer need a Connect attachment, you can delete it. You must first
delete any Connect peers for the attachment.

###### To delete a Connect attachment using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit gateway
   attachments**.
3. Select the Connect attachment, and choose **Actions**,
   **Delete transit gateway attachment**.
4. Enter `delete` and choose **Delete**.

###### To delete a Connect attachment using the AWS CLI

Use the [delete-transit-gateway-connect](../../../cli/latest/reference/ec2/delete-transit-gateway-connect.md "../../../cli/latest/reference/ec2/delete-transit-gateway-connect.md") command.
