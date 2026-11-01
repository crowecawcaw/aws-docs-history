

# Obtain information
<a name="setup-multicast-obtain-info"></a>

Obtain the following information from the video engineer in your organization who operates the multicast source:
+ The protocol, the multicast group address, and the port of the stream. The protocol is RTP or UDP. The group address is an IPv4 multicast address, for example `233.252.0.1`.

  You enter this information as a URL in the form `{{protocol}}://{{group}}:{{port}}`, for example `rtp://233.252.0.1:5000`.
+ Whether the upstream system sends the stream from a fixed source address, and what that address is. If the network uses source-specific multicast (SSM), the node must name that source address when it joins the group.
+ Whether the upstream system sends a second, identical copy of the stream for SMPTE 2022-7 seamless protection switching. If it does, obtain the protocol, group address, port, and (if SSM) source address of the second copy. The two copies usually travel on separate networks. For more information, see [SMPTE 2022-7 seamless protection switching for multicast inputs](multicast-2022-7.md).
+ The logical interface names on the MediaLive Anywhere node that connect to the network, or networks, that carry the stream. You choose these logical interfaces when you attach the input to the channel. If you weren't involved in [designing the MediaLive Anywhere cluster](emla-deploy-design-cluster.md), obtain this information from the video engineer who was.