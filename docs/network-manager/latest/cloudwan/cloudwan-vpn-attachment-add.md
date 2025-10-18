# Create a Site-to-Site VPN attachment for an AWS Cloud WAN core
 network

You can create a Site-to-Site VPN attachment using either the Network Manager console or the AWS CLI.

###### Topics

* [Create a Site-to-Site VPN attachment using the
 console](#cloudwan-vpn-attachment-console "#cloudwan-vpn-attachment-console")
* [Create a Site-to-Site VPN attachment using the command
 line or API](#cloudwan-vpn-attachment-cli "#cloudwan-vpn-attachment-cli")

## Create a Site-to-Site VPN attachment using the
 console


The following steps create a Site-to-Site VPN attachment for a core network using the
 console


###### To create a Site-to-Site VPN attachment using the console

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network link for the core network you want to add an attachment to.
4. In the navigation pane under the name of the global network, choose **Attachments**.
5. Choose **Create attachment**.
6. Enter a `name` identifying the attachment.
7. From the **Edge location** dropdown list, choose the location where the attachment is located.
8. Choose **VPN**.
9. From the **VPN attachment** section, choose the VPN ID to be
 used for the VPN attachment.
10. (Optional) In the **Tags** section, add
 **Key** and **Value** pairs to further
 help identify this resource. You can add multiple tags by choosing **Add
 tag**, or remove any tag by choosing **Remove
 tag**.
11. Choose **Create attachment**.

## Create a Site-to-Site VPN attachment using the command
 line or API


Use the command line or API to create an AWS Cloud WAN Site-to-Site VPN attachment.



###### To create a Site-to-Site VPN attachment using the command line or API


* Use `create-site-to-site-vpn-attachment`. See [create-site-to-site-vpn-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-site-to-site-vpn-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-site-to-site-vpn-attachment.html").
