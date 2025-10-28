# Associate or disassociate a Connect peer using AWS Network Manager

Associate or disassociate a Connect peer device link association in your AWS global network.

You can only associate one link with a Connect peer. If a link is already associated
with a Connect peer, and you want to use that link with another Connect peer, you must first
disassociate the link the Connect peer it's associated with.

###### To create a Connect peer association

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Devices**.
5. Choose the link for the device **ID** that you want to create an
   on-premises association for.
6. Choose the **Connect peer** tab.
7. Choose **Associate**.
8. Choose the on-premises **Connect peer**.
9. (Optional) Choose the **Link** used for the connection.
10. Choose **Create Connect peer association**.

The link is available to use immediately.

###### To disassociate a Connect peer association

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Devices**.
5. Choose the device **ID** link.
6. Choose the **Connect peer** tab.
7. Choose the check box for the Connect peer that you want to disassociate.
8. Choose **Disassociate**.

Disassociation occurs immediately.
