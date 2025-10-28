# Delete a transit gateway in AWS Transit Gateway

You can't delete a transit gateway with existing attachments. You need to delete all
attachments before you can delete a transit gateway.

###### To delete a transit gateway using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. Choose the transit gateway to delete.
3. Choose **Actions**, **Delete transit
   gateway**. Enter `delete` and choose
   **Delete** to confirm the deletion.

###### To delete a transit gateway using the AWS CLI

Use the [delete-transit-gateway](../../../cli/latest/reference/ec2/delete-transit-gateway.md "../../../cli/latest/reference/ec2/delete-transit-gateway.md") command.
