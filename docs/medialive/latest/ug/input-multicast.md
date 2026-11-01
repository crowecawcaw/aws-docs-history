

# Channel input—Multicast input
<a name="input-multicast"></a>

Before you attach the input, check how it is set up. On the **Inputs** page, choose the input. The **Multicast settings** section of the input details shows the multicast URL. It also shows the source IP address and the secondary source, if you set them when you created the input. For example:
+ **Multicast URL: rtp://233.252.0.1:5000**
+ **Secondary URL: rtp://233.252.0.2:5000**

When you attach the input, complete the logical interface fields:
+ If the input has no secondary source, choose one logical interface. The node joins the multicast group on the network interface that this logical interface maps to.
+ If the input has a secondary source, choose two different logical interfaces. The **Primary interface** receives the stream at **Multicast URL**. The **Secondary interface** receives the stream at **Secondary URL**.

  If you choose the same logical interface twice, or only one, MediaLive rejects the channel. To fix the error, choose two different logical interfaces. For more information, see [SMPTE 2022-7 seamless protection switching for multicast inputs](multicast-2022-7.md).

In the MediaLive API, these are the members of `LogicalInterfaceNames` in the input attachment: the first member is the primary interface and the second member is the secondary interface.

For information about the **Multicast settings** in the **Network input settings** section that appears after you confirm the attachment, see [Input settings—Network input settings](input-network-input.md).