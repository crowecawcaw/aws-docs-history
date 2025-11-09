# Network Requirements | Low-Latency

Streaming

IVS low-latency streaming relies on RTMP(S), SRT, and WebRTC protocols for the
transmission of media and data. To ensure a seamless experience, the destinations and ports
listed below must be accessible to broadcast with a given protocol. Any restrictions on
inbound or outbound traffic to these destinations may disrupt the functionality of IVS
low-latency streaming.

Note: The information in this document does not apply when streaming content to IVS over
AWS PrivateLink. For more information, see [Private Ingest](private-ingest-ll.md "private-ingest-ll.md").

## Ports

| Protocol      | Destinations          | Port                                                                    |
| ------------- | --------------------- | ----------------------------------------------------------------------- |
| RTMPS         | \*.live-video.net     | TCP:443                                                                 |
| Insecure RTMP | \*.live-video.net     | TCP:1935                                                                |
| SRT           | \*.srt.live-video.net | TCP:9000                                                                |
| WebRTC        | \*.live-video.net     | TCP:4443 (SDP exchange)<br>UDP:32768-61000 (ephemeral ports for WebRTC) |

## IP Ranges

The
data plane for IVS low-latency streaming is global. To broadcast to IVS, it is
important that all subnets for the service IVS_LOW_LATENCY in [ip-ranges.json](../../../vpc/latest/userguide/aws-ip-ranges.md "../../../vpc/latest/userguide/aws-ip-ranges.md") must be accessible, regardless of their region or your
chosen AWS Region. Streamers may be connected to any subnet automatically. See
[Global Solution, Regional Control](what-is.md#what-is-aws "what-is.md#what-is-aws") for details.

For a list of all IVS_LOW_LATENCY subnets, run the following `jq`
commands:

**ipv4**

```
curl https://ip-ranges.amazonaws.com/ip-ranges.json | jq -r '.prefixes[] | select(.service=="IVS_LOW_LATENCY") | .ip_prefix'
```

**ipv6**

```
curl https://ip-ranges.amazonaws.com/ip-ranges.json | jq -r '.ipv6_prefixes[] | select(.service=="IVS_LOW_LATENCY") | .ipv6_prefix'
```
