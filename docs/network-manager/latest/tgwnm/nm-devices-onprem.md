# Associate or disassociate an on-premises

link using AWS Network Manager

Associate or disassociate an on-premises device link association in your AWS global network.

You can only associate one link with a customer gateway. If a link is already associated
with a customer gateway, and you want to use that link with another gateway, you must first
disassociate the link the gateway it's currently associated with.

###### To create an on-premises association

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Devices**.
5. Choose the link for the device **ID** that you want to create an
   on-premises association for.
6. Choose the **On-premises associations** tab.
7. Choose **Associate**.
8. Choose the on-premises **Customer gateway**.
9. (Optional) Choose the **Link** used for the connection.
10. Choose **Create on-premises association**.

The link is available to use immediately.

###### To disassociate an on-premises association

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Devices**.
5. Choose the device **ID** link.
6. Choose the **On-premises association** tab.
7. Choose the check box for the on-premises association that you want to
   disassociate.
8. Choose **Disassociate**.

Disassociation occurs immediately.
