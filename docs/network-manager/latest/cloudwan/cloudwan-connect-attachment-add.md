# Create a Connect attachment for an AWS Cloud WAN
 core network

You can create a Connect attachment using either the Network Manager console or using the AWS CLI.
 Once you create a Connect attachment to your core network you can create a Connect peer. For
 the steps to create a Connect peer after creating the Connect attachment, see [Create an AWS Cloud WAN Connect peer for a core
 network](cloudwan-connect-peer-attachment.md "cloudwan-connect-peer-attachment.md").

###### Topics

* [Create a Connect attachment using the
 console](#cloudwan-connect-attachment-console "#cloudwan-connect-attachment-console")
* [Create a Connect attachment or Connect
 peer using the command line or API](#cloudwan-connect-attachment-cli "#cloudwan-connect-attachment-cli")

## Create a Connect attachment using the
 console


The following steps create a Connect attachment for a core network using the console. 


###### To create a Connect attachment using the console

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network link for the core network you want to add an attachment to.
4. In the navigation pane under the name of the global network, choose **Attachments**.
5. Choose **Create attachment**.
6. Enter a `name` identifying the attachment.
7. From the **Edge location** dropdown list, choose the location where the attachment is located.
8. Choose **Connect**.
9. From the **Connect attachment** section, choose the Connect
 protocol. This will be either:




	* **GRE**
	* **Tunnel-less (No encapsulation)**
10. Choose the **Transport Attachment ID** that will be used for
 the Connect attachment.
11. (Optional) In the **Tags** section, add
 **Key** and **Value** tags to further help
 identify this resource. You can add multiple tags by choosing **Add
 tag**, or remove any tag by choosing **Remove
 tag**.
12. Choose **Create attachment**.

## Create a Connect attachment or Connect
 peer using the command line or API


Use the command line or API to create an AWS Cloud WAN Connect attachment. When using the
 `CreateConnectAttachment` API pass the following:`"Protocol" :
 "NO_ENCAP"`.



###### To create a Connect attachment or Connect peer using the command line or
 API


* Use `create-connect-attachment`. See [create-connect-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-connect-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-connect-attachment.html").

If you're creating a Tunnel-less Connect attachment, you must then use the following command line or
 API to create the Connect peer:



* `create-connect-peer`. See [create-connect-peer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-connect-peer.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-connect-peer.html").
