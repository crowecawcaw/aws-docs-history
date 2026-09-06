

# Add a segment to an AWS Cloud WAN core network policy version
<a name="cloudwan-policy-segments"></a>

The following steps guide you through configuring a core network for a policy version using the **Policy versions** link on the AWS Network Manager console. Before adding a segment you must first have configured your [network settings](cloudwan-core-network-config.md). For more information, about network Segments, see [Segments](cloudwan-create-policy-version.md#cloudwan-policy-create-segment). 

**To configure a segment**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity** choose **Cloud WAN**.

1. On the **Global networks** page, choose the global network ID that for the core network you want to create a policy version for, and then choose **Core network**.

1. In the navigation pane, choose **Policy versions**.

1. Choose **Create policy version**.

1. Choose **Segments**.

1. In the **Segments** section, Choose **Create**.

1. Enter the **Segment name** and **Segment description** to identify the segment.

1. From the **Edge locations** dropdown list, choose one or more segments to create.

1. Choose **Require acceptance** if you require approval for attachments to be mapped to this segment. 

1. Choose **Isolated attachments** if you need this segment isolated. Attachments in isolated segments can't communicate with other segments, and attachments in other segments can't communicate with the isolated segment.
**Important**  
** Isolated attachments** is required if you're adding an intra-segment for use with service insertion.

1. For the **Segment filter**, choose if you want to **Allow all** shared routes from other segments, to **Allowed selected** segments, or to **Deny selected** segments. The default value is to **Allow all** segments.

1. (Optional) If you want to limit your edge locations for the segment, choose **Choose edge locations**, and then choose the edge locations you want to limit the segment to.

1. Choose **Create policy**.