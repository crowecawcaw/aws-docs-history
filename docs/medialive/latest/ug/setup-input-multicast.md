

# Create a multicast input
<a name="setup-input-multicast"></a>

Use the following procedure to create a multicast input in the MediaLive console. Before you start, collect the details that are listed in [Obtain information](setup-multicast-obtain-info.md).

**To create a multicast input**

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. In the navigation pane, choose **Inputs**. On the **Inputs** page, choose **Create input**.

1. For **Input name**, enter a name for the input.

1. For **Input type**, choose **Multicast**.

1. Complete the multicast source fields as described in the table that follows this procedure. Complete the **Secondary source** section only if the upstream system sends a second copy of the stream for SMPTE 2022-7 seamless protection switching.

1. (Optional) In the **Tags** section, create tags to associate with this input. For more information, see [Tagging resources](tagging.md).

1. Choose **Create**.

   MediaLive creates the input and adds it to the list on the **Inputs** page.

The input identifies the multicast group, or groups, to join. When you start a channel that uses the input, the node joins the group and receives the stream. The node joins on the logical interface that you choose when you [attach the input to the channel](input-multicast.md).

The following table describes the fields for a multicast input.


| Field | Description | 
| --- | --- | 
| Multicast URL | Required. The URL of the multicast stream, in the form `{{protocol}}://{{group}}:{{port}}`. The protocol is `rtp` or `udp`. The group is an IPv4 multicast address. For example, `rtp://233.252.0.1:5000`. | 
| Multicast source IP | Optional. The IP address of the device that sends the multicast stream. Complete this field when the network uses source-specific multicast (SSM), or when several senders use the same group and you want to receive only one of them. For example, `192.168.0.13`. | 
| Secondary source – Secondary URL | Optional. The URL of the second copy of the stream, for SMPTE 2022-7 seamless protection switching. Use the same URL form as **Multicast URL**. The second copy can use the same group and port as the first copy, or a different group and port. It must arrive on a different network interface of the node.<br />When you complete this field, you must choose two logical interfaces when you attach the input to the channel. For more information, see [SMPTE 2022-7 seamless protection switching for multicast inputs](multicast-2022-7.md). | 
| Secondary source – Secondary source IP | Optional. The IP address of the device that sends the second copy of the stream, for SSM. You can complete this field only when you also complete **Secondary URL**. | 

If you use the MediaLive API or the AWS CLI instead of the console, use the members of `MulticastSettings` in the input. The following table shows the API member for each console field.


| Console field | API member | 
| --- | --- | 
| Multicast URL | Sources[0].Url | 
| Multicast source IP | Sources[0].SourceIp | 
| Secondary URL | Sources[0].SecondaryUrl | 
| Secondary source IP | Sources[0].SecondarySourceIp | 

You can add or remove the secondary source later by editing the input. Before you edit the input, detach it from every channel. You can then change the logical interfaces on the input attachment when you attach the input again. For more information, see [Editing an input](edit-input.md).