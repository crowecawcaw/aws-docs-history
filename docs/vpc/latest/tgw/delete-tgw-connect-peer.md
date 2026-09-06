

# Delete a Connect peer in AWS Transit Gateway
<a name="delete-tgw-connect-peer"></a>

If you no longer need a Connect peer, you can delete it.

**To delete a Connect peer using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**.

1. Select the Connect attachment.

1. In the **Connect Peers** tab, select the Connect peer and choose **Actions**, **Delete connect peer**.

**To delete a Connect peer using the AWS CLI**  
Use the [delete-transit-gateway-connect-peer](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-transit-gateway-connect-peer.html) command.