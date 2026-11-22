

# View AWS Transit Gateway network function attachments

You can view both network function attachment types in Amazon VPC Console and the Network Manager console.

## View a network function attachment using Amazon VPC Console
<a name="view-nf-attachment-vpc"></a>

**To view a network function attachment**

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/home#TransitGatewayAttachments).

1. In the navigation pane, choose **Transit Gateways**.

1. Choose **Transit gateway attachments**.

1. Select an attachment with a type of **Network function** to view its details, including its state, transit gateway, and Availability Zones.

## View a network function attachment using the Network Manager console
<a name="view-nf-attachment-console"></a>

**To view a network function attachment in Network Manager**

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Create a global network in Network Manager if you don't already have one.

1. Register your transit gateway with Network Manager.

1. Under **Global Networks**, choose the global network where the attachment is located.

1. In the navigation pane, choose **Transit gateways**.

1. Choose the transit gateway whose attachments you want to view.

1. Choose **Topology tree**. Network function attachments appear with a network function icon.

1. To view attachment details, select the transit gateway in the topology and then choose the **Network function** tab.

The Network Manager console shows the attachment state, associated transit gateway, and Availability Zones.