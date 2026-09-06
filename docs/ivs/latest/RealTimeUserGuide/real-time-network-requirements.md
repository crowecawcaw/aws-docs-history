

# Network Requirements \| Real-Time Streaming
<a name="real-time-network-requirements"></a>

Amazon IVS real-time streaming relies on WebRTC and WebSocket protocols for the transmission of media and data. To ensure a seamless experience, the destinations and ports listed below must be accessible. Any restrictions on inbound or outbound traffic to these destinations may disrupt the functionality of IVS real-time streaming.

You can use this [network test tool](https://diagnostics.ivs.rocks/) to ensure that your network is properly configured and that traffic to and from the necessary destinations and ports is not being blocked.

## Common
<a name="real-time-network-requirements-common"></a>


| Destination | Ports | 
| --- | --- | 
| \*.live-video.net | TCP:443 | 

## Media
<a name="real-time-network-requirements-media"></a>

By default, IVS real-time streaming relies on UDP for the transmission of media to ensure low-latency and high-performance streaming. If UDP is blocked for participants subscribing to media, TCP is used as a fallback. TCP fallback is not supported for publishing, so if UDP traffic is completely blocked, publishing will fail.


| Destination | Ports | 
| --- | --- | 
| All subnets listed under the `IVS_REALTIME` service in [ip-ranges.json](https://docs.aws.amazon.com/vpc/latest/userguide/aws-ip-ranges.html) must be accessible, regardless of their `region` or your chosen AWS Region. Participants may be connected to any subnet automatically. See [Global Solution, Regional Control](what-is.md) for details. | UDP:3478<br />UDP:443<br />TCP:3478 (Fallback)<br />TCP:443 | 