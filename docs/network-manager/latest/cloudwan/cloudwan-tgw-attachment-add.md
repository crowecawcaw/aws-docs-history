# Create a transit gateway route table attachment for an AWS Cloud WAN core network

Add a transit gateway route table attachment to your AWS Cloud WAN core network.

## Create a transit gateway route table attachment

using the console

The following steps create a transit gateway route table attachment for a core network using the
console.

###### To create a transit gateway route table attachment using the console

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network link for the core network you want to add an attachment to.
4. In the navigation pane under the name of the global network, choose **Attachments**.
5. Choose **Create attachment**.
6. Enter a `name` identifying the attachment.
7. From the **Edge location** dropdown list, choose the location where the attachment is located.
8. From the **Attachment type** dropdown list, choose
   **Transit gateway route table**.
9. In the **Transit gateway route table attachment** section, choose
   the **Transit gateway peering** that will be used for the route
   table attachment. For information on creating a peering, see [Create a peering in an AWS Cloud WAN core
   network](cloudwan-peerings-create.md "cloudwan-peerings-create.md").
10. From the **Transit gateway route table** list, choose
    the route table to be used for the peering. For information about
    creating a transit gateway route table, see [Transit gateway route tables](../../../vpc/latest/tgw/tgw-route-tables.md "../../../vpc/latest/tgw/tgw-route-tables.md")
    in the _AWS Transit Gateway Guide_.
11. (Optional) In the **Tags** section, add **Key**
    and **Value** tags to help identify this resource. You can add
    multiple tags by choosing **Add tag**, or remove any tag by
    choosing **Remove tag**.
12. Choose **Create attachment**.

## Create a transit gateway route table attachment

using the command line or API

Use the command line or API to create an AWS Cloud WAN transit gateway route table attachment.

###### To create a transit gateway route table attachment using the command line or API

- Use `create-transit-gateway-route-table-attachment`. See [create-transit-gateway-route-table-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-transit-gateway-route-table-attachment.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-transit-gateway-route-table-attachment.html").
