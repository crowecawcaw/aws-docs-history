

# Create a Connect attachment for an AWS Cloud WAN core network
<a name="cloudwan-connect-attachment-add"></a>

You can create a Connect attachment using either the Network Manager console or using the AWS CLI. Once you create a Connect attachment to your core network you can create a Connect peer. For the steps to create a Connect peer after creating the Connect attachment, see [Create an AWS Cloud WAN Connect peer for a core network](cloudwan-connect-peer-attachment.md).

**Topics**
+ [Create a Connect attachment using the console](#cloudwan-connect-attachment-console)
+ [Create a Connect attachment or Connect peer using the command line or API](#cloudwan-connect-attachment-cli)

## Create a Connect attachment using the console
<a name="cloudwan-connect-attachment-console"></a>

The following steps create a Connect attachment for a core network using the console. 

**To create a Connect attachment using the console**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network link for the core network you want to add an attachment to.

1. In the navigation pane under the name of the global network, choose **Attachments**.

1. Choose **Create attachment**.

1. Enter a **name** identifying the attachment.

1. From the **Edge location** dropdown list, choose the location where the attachment is located.

1. Choose **Connect**.

1. From the **Connect attachment** section, choose the Connect protocol. This will be either:
   + **GRE**
   + **Tunnel-less (No encapsulation)**

1. Choose the **Transport Attachment ID** that will be used for the Connect attachment.

1. (Optional) For **Routing policy label**, provide a label that will be used to map this policy to attachments. The policy will automatically be applied to any attachment tagged with the same label.

1. (Optional) In the **Tags** section, add **Key** and **Value** tags to further help identify this resource. You can add multiple tags by choosing **Add tag**, or remove any tag by choosing **Remove tag**.

1. Choose **Create attachment**.

## Create a Connect attachment or Connect peer using the command line or API
<a name="cloudwan-connect-attachment-cli"></a>

Use the command line or API to create an AWS Cloud WAN Connect attachment. When using the `CreateConnectAttachment` API pass the following:`"Protocol" : "NO_ENCAP"`.

**To create a Connect attachment or Connect peer using the command line or API**
+ Use `create-connect-attachment`. See [create-connect-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-connect-attachment.html).

If you're creating a Tunnel-less Connect attachment, you must then use the following command line or API to create the Connect peer:
+ `create-connect-peer`. See [create-connect-peer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-connect-peer.html).