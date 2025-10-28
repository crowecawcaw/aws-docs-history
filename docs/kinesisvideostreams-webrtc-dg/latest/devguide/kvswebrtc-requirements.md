# System requirements

This section covers basic system requirements for using Amazon Kinesis Video Streams with WebRTC, including
network requirements and environment. It also includes information about debugging
connections.

## Networking requirements

The general networking requirements for the signaling channel service endpoints for
Kinesis Video Streams with WebRTC are:

- HTTPS calls to endpoints hosted at
  `https://*.kinesisvideo.{region}.amazonaws.com`
- WebSocket integrations with endpoints `wss://*.kinesisvideo.{region}.amazonaws.com`
- `STUN` servers at `stun:stun.kinesisvideo.{aws-region}.amazonaws.com:443`
- `TURN` servers at `turn:_._.kinesisvideo.{aws-region}.amazonaws.com:443`
  and `turns:_._.kinesisvideo.{aws-region}.amazonaws.com:443`

###### Note

IPv6 addresses aren't currently supported for `STUN` and `TURN`
servers.

The protocols used between peers as part of the RTCPeerConnection can be either TCP or UDP
based.

Most applications attempt to establish direct, peer-to-peer connections by determining
the IP addresses for each peer, as well as the ports and protocols to be exchanged as
ICE candidates. These candidates are used to attempt to connect to one another using
these candidates. They will attempt each pair until a connection can be
established.

## Network environment

If a message from the viewer has been sent to the master and a log such as `No
 valid ICE candidate` is recorded, then no valid connection route has been
found. This can happen if there is a firewall that prevents direct connection, or if the
network is not reachable.

Do the following to troubleshoot the connectivity issue:

- If you're not using `TURN` on the master side, be sure to
  enable `TURN`.

`TURN` is enabled by default in the C SDK. In the JavaScript SDK,
select `STUN/TURN` or `TURN only` in NAT Traversal.

- For restricted networks, such as an enterprise network, try other available
  networks (wired or wireless).

If you're connecting to a VPN, disconnect from it.

###### Note

You can disregard 403 `Forbidden IP` errors returned by Kinesis Video Streams TURN servers. The servers reject ICE candidate pairs that contain `localhost` IPs, such as `192.168.*` or `10.0.0.*`.

This may cause some, but not all, ICE candidate pairs to fail.

## Debugging ongoing connections

There are a few areas that can cause issues with an established, ongoing WebRTC
connection, but networking is the most common.

You can confirm a VERBOSE level log from the SDK by setting `export
 AWS_KVS_LOG_LEVEL=1` as an environment variable.

###### Note

If no candidate pair is found within the allotted timeout, the ICE agent returns error status `0x5a00000d`.

For additional information about log levels, see [GitHub](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-c/blob/master/README.md#setup-desired-log-level "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-c/blob/master/README.md#setup-desired-log-level").

```
export AWS_KVS_LOG_LEVEL=1
./kvsWebrtcClientMasterGstSample TestChannel
```

You will see logs like the following. From these logs, you can confirm the Interactive
Connectivity Establishment (ICE) candidate (IP address and port) and the selected
candidate pair.

```
2023-02-13 05:57:16 DEBUG   iceAgentReadyStateSetup(): Selected pair w1UdV9fE+_/CuBel1pl, local candidate type: srflx. Round trip time 7 ms. Local candidate priority: 1694498815, ice candidate pair priority: 7240977859836116990
2023-02-13 05:57:16 INFO    onConnectionStateChange(): New connection state 3
2023-02-13 05:57:16 DEBUG   rtcPeerConnectionGetMetrics(): ICE local candidate Stats requested at 16762678365731494
2023-02-13 05:57:16 DEBUG   logSelectedIceCandidatesInformation(): Local Candidate IP Address: XXX.XXX.XXX.XXX
2023-02-13 05:57:16 DEBUG   logSelectedIceCandidatesInformation(): Local Candidate type: srflx
2023-02-13 05:57:16 DEBUG   logSelectedIceCandidatesInformation(): Local Candidate port: 38563
2023-02-13 05:57:16 DEBUG   logSelectedIceCandidatesInformation(): Local Candidate priority: 1694498815
2023-02-13 05:57:16 DEBUG   logSelectedIceCandidatesInformation(): Local Candidate transport protocol: udp
2023-02-13 05:57:16 DEBUG   logSelectedIceCandidatesInformation(): Local Candidate relay protocol: N/A
2023-02-13 05:57:16 DEBUG   logSelectedIceCandidatesInformation(): Local Candidate Ice server source: stun.kinesisvideo.ap-northeast-1.amazonaws.com
2023-02-13 05:57:16 DEBUG   rtcPeerConnectionGetMetrics(): ICE remote candidate Stats requested at 16762678365732111
2023-02-13 05:57:16 DEBUG   logSelectedIceCandidatesInformation(): Remote Candidate IP Address: XXX.XXX.XXX.XXX
2023-02-13 05:57:16 DEBUG   logSelectedIceCandidatesInformation(): Remote Candidate type: srflx
2023-02-13 05:57:16 DEBUG   logSelectedIceCandidatesInformation(): Remote Candidate port: 45867
2023-02-13 05:57:16 VERBOSE signalingClientGetCurrentState(): Signaling Client Get Current State
2023-02-13 05:57:16 DEBUG   logSelectedIceCandidatesInformation(): Remote Candidate priority: 1685921535
2023-02-13 05:57:16 DEBUG   logSelectedIceCandidatesInformation(): Remote Candidate transport protocol: udp
```
