# Accept or reject an AWS Cloud WAN core network
 attachment

When you create an attachment and associate it to a segment that requires an
 acceptance from the core network owner, the newly created attachment goes into a
 **Pending attachment acceptance** state. The core network owner has
 to review the attachment and choose to accept or reject the request.

###### To accept or reject an attachment using the console

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network ID.
4. Under **Core network** in the navigation pane, choose **Attachments**.
5. Select the check box for the specific attachment that is in the
 **Pending attachment acceptance** state. Details about the
 attachment are displayed in the lower part of the page.
6. Choose **Accept** or **Reject**.
7. If you chose **Accept**, the attachment goes into a
 **Creating (Accept)** state. If you chose
 **Reject**, the attachment goes into a **Rejected
 (Reject)** state.
