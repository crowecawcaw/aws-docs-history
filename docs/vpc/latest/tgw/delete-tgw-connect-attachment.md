

# Delete a Connect attachment in AWS Transit Gateway
<a name="delete-tgw-connect-attachment"></a>

If you no longer need a Connect attachment, you can delete it. You must first delete any Connect peers for the attachment.

**To delete a Connect attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**.

1. Select the Connect attachment, and choose **Actions**, **Delete transit gateway attachment**.

1. Enter **delete** and choose **Delete**.

**To delete a Connect attachment using the AWS CLI**  
Use the [delete-transit-gateway-connect](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-transit-gateway-connect.html) command.