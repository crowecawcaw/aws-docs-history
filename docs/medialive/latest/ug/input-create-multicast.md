

# Creating a multicast input
<a name="input-create-multicast"></a>

This section describes how to create a multicast input. A multicast input connects an IP multicast stream on your network to a channel. The channel runs on a node in an AWS Elemental MediaLive Anywhere cluster. Create the input before you create the channel that ingests the input.

**Note**  
Multicast inputs are supported only on AWS Elemental MediaLive Anywhere deployments. For more information about these deployments, see [Setting up AWS Elemental MediaLive Anywhere](setup-emla.md).

With a multicast input, the node joins the multicast group when the channel starts and receives the transport stream (TS) that the upstream system sends to that group. The node joins the group on the network interface that you choose when you [attach the input to the channel](input-multicast.md).

A multicast input can optionally have a *secondary source*: a second copy of the same stream, delivered on a second network interface. MediaLive merges the two copies with SMPTE 2022-7 seamless protection switching. For more information, see [SMPTE 2022-7 seamless protection switching for multicast inputs](multicast-2022-7.md).

**Topics**
+ [Obtain information](setup-multicast-obtain-info.md)
+ [Create a multicast input](setup-input-multicast.md)
+ [SMPTE 2022-7 seamless protection switching for multicast inputs](multicast-2022-7.md)