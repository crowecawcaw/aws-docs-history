

# SMPTE 2022-7 seamless protection switching for multicast inputs
<a name="multicast-2022-7"></a>

*SMPTE 2022-7 seamless protection switching* protects a channel against the loss of one network path. The Society of Motion Picture and Television Engineers (SMPTE) defines it in the standard ST 2022-7.

Your upstream system sends two identical copies of the stream, usually on two separate networks. The node receives both copies, one on each of two network interfaces, and merges them packet by packet. If packets are lost or delayed on one path, MediaLive uses the packets from the other path. The output continues without a glitch, and the channel doesn't restart when the lost path returns.

Before you start, confirm that your upstream system sends two identical copies of the stream. Also confirm that the node has a logical interface on each network that carries a copy.

**To set up SMPTE 2022-7 seamless protection switching**

1. On the input, complete **Secondary URL**. If you use source-specific multicast (SSM), also complete **Secondary source IP**. For more information, see [Create a multicast input](setup-input-multicast.md).

1. On the channel, [attach the input](input-multicast.md) and choose two different logical interfaces. The **Primary interface** receives the stream at **Multicast URL**. The **Secondary interface** receives the stream at **Secondary URL**.

When you start the channel, the node receives both copies of the stream and merges them.

The following rules and behaviors apply to a multicast input that has a secondary source.
+ The two copies must carry the same content in RTP packets with the same RTP sequence numbers. SMPTE 2022-7 uses the RTP sequence numbers to merge the two copies. You create the two copies with your upstream system. MediaLive doesn't create them.
+ The two copies can use the same multicast group and port, or different groups and ports. They must arrive on two different logical interfaces of the node.

  MediaLive rejects the channel if the input attachment names the same logical interface twice. It also rejects the channel if the input attachment names only one logical interface. To fix the error, choose a different logical interface for each copy.
+ Leave the **Source IP address** field in the **Multicast settings** of the input attachment empty. MediaLive rejects the channel if the input attachment sets this field. If you use SSM, set the source IP addresses on the input instead, one for each copy (**Multicast source IP** and **Secondary source IP**).
+ If one copy stops arriving while the channel runs, MediaLive raises the **Stopped Receiving UDP Input** [alert](monitor-activity-types-alerts-channels.md). The channel continues from the other copy. The alert clears when the copy returns. The `RtpPacketsLost` [metric](monitoring-eml-metrics.md) stays at 0 for as long as at least one copy delivers every packet.
+ A channel that uses a multicast input is a single-pipeline channel. The two copies protect the one pipeline. They don't create a second pipeline.