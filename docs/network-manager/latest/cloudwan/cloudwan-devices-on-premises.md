

# Associate or disassociate an on-premises link in an AWS Cloud WAN global network
<a name="cloudwan-devices-on-premises"></a>

Associate or disassociate an on-premises device link association in your Cloud WAN global network.

You can only associate one link with a customer gateway. If a link is already associated with a customer gateway, and you want to use that link with another gateway, you must first disassociate the link the gateway it's currently associated with.

**To create an on-premises association**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**.

1. Choose the link for the device **ID** that you want to create an on-premises association for. 

1. Choose the **On-premises associations** tab.

1. Choose **Associate**.

1. Choose the on-premises **Customer gateway**.

1. (Optional) Choose the **Link** used for the connection. 

1. Choose **Create on-premises association**.

   The link is available to use immediately.

**To disassociate an on-premises association**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**.

1. Choose the device **ID** link.

1. Choose the **On-premises association** tab.

1. Choose the check box for the on-premises association that you want to disassociate. 

1. Choose **Disassociate**.

   Disassociation occurs immediately.