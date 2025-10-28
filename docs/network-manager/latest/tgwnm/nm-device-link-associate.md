# Associate or disassociate a device

link using AWS Network Manager

Associate a link with a device in your AWS global network. In order to associate a
link with a device, you must first create the link. For more information on creating links,
see [Add a link using AWS Network Manager](nm-site-link-add.md "nm-site-link-add.md").

You can only associate one link with one device. If a link is already associated with a
device, and you want to use that link with another device, you must first disassociate the
link the device it's associated with.

###### To associate a link with a device

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Devices**.
5. Choose the link for the device **ID** that you want to add a link
   to, and then choose the **Links** tab.

###### Note

Choose the link. Do not select the check box. 6. Choose the **Links** tab, and then choose **Associate
link**. 7. Choose the link that you want to associate with the device. 8. Choose **Associate link**.

The link is available to use immediately.
If you to use a link with another device, you must first disassociate the link from its
original device.

###### To disassociate a link from a device

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network ID.
4. In the navigation pane, choose **Devices**.
5. Choose the link for the device **ID** that you want to add a link
   to, and then choose the **Links** tab.

###### Note

Choose the link. Do not select the check box. 6. Choose the **Links** tab, and then choose **Associate
link**. 7. Choose the check box for the link that you want to disassociate from a
device. 8. Choose **Disassociate link**.

Disassociation occurs immediately.
