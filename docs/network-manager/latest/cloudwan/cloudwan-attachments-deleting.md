# Delete an AWS Cloud WAN core network attachment

You can delete any attachment from your core network. Deleted attachments can't be
 recovered. This section including the steps to delete an attachment using the AWS Cloud WAN
 console or by using the command line or API.

###### To delete an attachment using the console

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network ID.
4. Under **Core network** in the navigation pane, choose **Attachments**.
5. Select the check box for the attachment that you want to delete.
6. Choose **Delete**.
7. Confirm that you want to delete the attachment by choosing
 **Delete** again. 


The attachment is removed from the **Attachments**
 page.
Use the command line or API to delete any of your core network attachments.


###### To delete an attachment using the command line or API


* For a Connect, transit gateway route table, VPC, or Site-to-Site VPN
 attachment, see [delete-attachment](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/delete-attachment.html "https://docs.aws.amazon.com/cli/latest/reference/networkmanager/delete-attachment.html").
* For a Connect peer attachment, see [delete-transit-gateway-connect-peer](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-transit-gateway-connect-peer.html "https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-transit-gateway-connect-peer.html").
