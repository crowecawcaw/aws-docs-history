# Create a Direct Connect gateway attachment for an

AWS Cloud WAN core network

You can add a Direct Connect gateway attachment using either the Network Manager console or using the
AWS CLI. The Direct Connect gateway must first be created using the Direct Connect console before it
can be added as an attachment in Cloud WAN. For more information about Direct Connect gateway
attachments and Cloud WAN, see [Direct Connect gateway
attachments](cloudwan-dxattach-about.md "cloudwan-dxattach-about.md").

###### Topics

- [Create a Direct Connect gateway attachment using
  the console](#cloudwan-dxattachment-console "#cloudwan-dxattachment-console")
- [Create a Direct Connect gateway attachment using
  the command line or API](#cloudwan-dxattachment-cli "#cloudwan-dxattachment-cli")

## Create a Direct Connect gateway attachment using

the console

The following steps create a Direct Connect gateway attachment for a core network using the
console.

###### To create a Direct Connect gateway attachment using the console

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global Networks**.
3. On the **Global networks** page, choose the global network link for the core network you want to add an attachment to.
4. In the navigation pane under he name of the global network, choose **Attachments**.
5. Choose **Create attachment**.
6. Enter a **Name** identifying the attachment.
7. From the **Attachment type** drop-down list choose
   **Direct Connect gateway**.
8. For the **Edge locations**, choose one of the following:
   - **All** — Choose this option if you want to associate
     all edge locations in your core network with the Direct Connect gateway.
     When choosing this option, any new edge locations deployed in a core
     network policy version are automatically added to the Direct Connect
     gateway attachment and updated with the Direct Connect gateway. This
     does not automatically update any edge locations you might remove from
     the core network policy.
   - **Specific** — Choose this option if you want to
     associate only a subset of edge locations from your core network policy
     with the Direct Connect gateway. When choosing this option, you must
     manually add new or remove edge locations to the Direct Connect gateway
     attachment after deploying a core network policy version. A Direct
     Connect attachment will be attached to the core network edge according
     to the core network policy edge locations but will associated to the
     segment based on the segment edge locations..

9. In the **Direct Connect gateway attachment** section, choose the
   Direct Connect gateway to use for connecting Direct Connect to the Cloud WAN core
   network.

###### Note

A Direct Connect gateway can be used for only one core network, and can't
be used for any other Direct Connect gateway type. 10. Choose **Create attachment**.

## Create a Direct Connect gateway attachment using

the command line or API

Use the command line or API to create a Direct Connect gateway attachment.

###### To create a Direct Connect gateway attachment using the command line or API

- Use `create-direct-connect-gateway-attachment`. See [create-direct-connect-gateway-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-direct-connect-gateway-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-direct-connect-gateway-attachment.html").
