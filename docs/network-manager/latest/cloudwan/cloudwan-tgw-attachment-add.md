

# Create a transit gateway route table attachment for an AWS Cloud WAN core network
<a name="cloudwan-tgw-attachment-add"></a>

Add a transit gateway route table attachment to your AWS Cloud WAN core network. 

## Create a transit gateway route table attachment using the console
<a name="cloudwan-rtb-attachment-console"></a>

The following steps create a transit gateway route table attachment for a core network using the console.

**To create a transit gateway route table attachment using the console**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network link for the core network you want to add an attachment to.

1. In the navigation pane under the name of the global network, choose **Attachments**.

1. Choose **Create attachment**.

1. Enter a **name** identifying the attachment.

1. From the **Edge location** dropdown list, choose the location where the attachment is located.

1. From the **Attachment type** dropdown list, choose **Transit gateway route table**.

1. In the **Transit gateway route table attachment** section, choose the **Transit gateway peering** that will be used for the route table attachment. For information on creating a peering, see [Create a peering in an AWS Cloud WAN core network](cloudwan-peerings-create.md).

1. From the **Transit gateway route table** list, choose the route table to be used for the peering. For information about creating a transit gateway route table, see [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html) in the *AWS Transit Gateway Guide*.

1. (Optional) For **Routing policy label**, provide a label that will be used to map this policy to attachments. The policy will automatically be applied to any attachment tagged with the same label.

1. (Optional) In the **Tags** section, add **Key** and **Value** tags to help identify this resource. You can add multiple tags by choosing **Add tag**, or remove any tag by choosing **Remove tag**.

1. Choose **Create attachment**.

## Create a transit gateway route table attachment using the command line or API
<a name="cloudwan-rtb-attachment-cli"></a>

Use the command line or API to create an AWS Cloud WAN transit gateway route table attachment.

**To create a transit gateway route table attachment using the command line or API**
+ Use `create-transit-gateway-route-table-attachment`. See [create-transit-gateway-route-table-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-transit-gateway-route-table-attachment.html).