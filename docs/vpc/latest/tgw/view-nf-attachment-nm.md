

# View AWS Transit Gateway network function attachments
<a name="view-nf-attachment-nm"></a>

You can view your network function attachments, including your AWS Network Firewall attachments, using either Amazon VPC Console or the Network Manager console to get a visual representation of your network topology. 

## View a network function attachment using the Network Manager console
<a name="view-nf-attachment-console"></a>

You can view a network function attachments using the Network Manager console.

**To view firewall attachments in Network Manager**

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Create a global network in Network Manager if you don't already have one.

1. Register your transit gateway with Network Manager.

1. Under **Global Networks**, choose the global network where the attachment is located.

1. In the navigation pane, choose **Transit gateways.** 

1. Choose the transit gateway that you want to view attachments for.

1. Choose **Topology tree** view. Network Firewall attachments appear with a network function icon.

1. To view details about a specific firewall attachment, select the transit gateway in the topology view, then select the **Network function** tab.

The Network Manager console provides detailed information about your firewall attachments, including their status, associated transit gateway, and Availability Zones.

## View a network function attachment using the Amazon VPC Console console
<a name="view-nf-attachment-vpc"></a>

Use the VPC console to see a list of your transit gateway attachment types.

**To view transit gateway attachment types using the VPC console**
+ See [View a VPC attachment](view-vpc-attachment.md). 