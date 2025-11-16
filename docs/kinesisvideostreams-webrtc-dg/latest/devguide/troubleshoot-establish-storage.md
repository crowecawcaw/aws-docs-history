# Troubleshoot issues connecting with the storage session

This section provides guidance on troubleshooting issues related to setting up and configuring storage for recording video streams.

###### Topics

- [Controlling and controlled peers](#troubleshoot-control-peers "#troubleshoot-control-peers")
- [Review supported codecs](#troubleshoot-review-codecs "#troubleshoot-review-codecs")
- [If channel is not mapped to a stream, will also throw 400 InvalidArgumentException](#troubleshoot-channel-mapping "#troubleshoot-channel-mapping")

## Controlling and controlled peers

In WebRTC, the controlling peer initiates the connection to the controlled peer by sending an SDP offer. For peer-to-peer sessions, the viewer participant initiates the connection by sending an offer to the master participant through Signaling. When connecting to the storage session for WebRTC ingestion, the storage session is the controlling peer. For master participants, they still remain the controlled participant. However, viewer participants switch from controlling to controlled.

Upon calling [JoinStorageSession](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md") or [JoinStorageSessionAsViewer](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md"), all participants must respond with an SDP answer and exchange ICE candidates with the storage session.

For a sequence diagram, see Understanding WebRTC ingestion and storage.

###### Important

Signaling messages received from the storage session do not have a senderClientId field in the JSON, which differs from the peer-to-peer master, which always receives senderClientId field with the SDP offer and ICE candidates.

## Review supported codecs

When [sending an SDP answer](SendSdpAnswer.md "SendSdpAnswer.md") and [exchanging ICE candidates](SendIceCandidate.md "SendIceCandidate.md") with the storage session, we recommend
including a `correlationId` in the messages. Including a
`correlationId` in the messages allows the storage session to return
`statusResponse` messages. These messages will contain the
`correlationId` of the input message, allowing you to track which
message the `statusResponse` belongs to. This allows you to receive
immediate feedback about why your SDP answers was rejected.

For more information about `correlationId` and
`statusResponse`, see [Asynchronous message reception](async-message-reception-api.md "async-message-reception-api.md").

One common reason the storage session might reject the SDP answer is that the
storage session wasn't able to accept codecs specified in the answer. A sample
`statusResponse` may look like the following:

```
{
  "correlationId": "1700186220273",
  "errorType": "InvalidArgumentException",
  "statusCode": "400",
  "success": false
}
```

As you review the SDP answer contents, review the lines starting with
`a=rtpmap` and verify that the codecs match the storage session's
supported codecs. Below is a snippet of a sample SDP answer containing opus audio
and VP8 video.

```
...
a=rtpmap:111 opus/48000/2
...
a=rtpmap:120 VP8/90000
...
```

See [JoinStorageSession](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md") for a list of supported codecs.

## If channel is not mapped to a stream, will also throw 400 InvalidArgumentException

### Review transceiver directions

In the SDP answer, review the directionality of the video and audio transceivers. The lines in the SDP look like this:

```
a=sendrecv
a=recvonly
```

For master participants, the following requirements are in place:

- H.264 video: sendonly
- Opus audio: sendonly or sendrecv

For viewer participants, the following requirements are in place:

- H.264 video: recvonly
- Opus audio: recvonly or sendrecv

If the service requirements are not met, a statusResponse with 400 IllegalArgumentException will be returned if the correlationId is provided when the answer was sent.

When using the KVS-provided WebRTC ingestion sample applications:

- Master participants: Ensure the "send video" and "send audio" settings are both enabled
- Viewer participants: Ensure "send video" setting is disabled

### Review ICE candidate conversion

When receiving ICE candidates from the KVS Signaling SDK, the application may need to convert the string into the ICE candidate object.

ICE candidates received from the storage session do not contain an SDPMID property, and do not come with a senderClientId.

Review your application logic for adding the ICE candidates received from remote into your application's RTCPeerConnection object.

### Review ICE candidate queuing logic

All ICE candidates received from the storage session need to be added to the RTCPeerConnection via the addIceCandidate API.

Even though the storage session sends the SDP offer before the ICE candidates, due to the asynchronous nature of the Signaling message delivery, the application may receive the ICE candidates before receiving the offer.

In this case, you will need to implement a temporary buffer to hold the ICE candidates.

The logic implemented in the KVS sample applications is as follows:

1. The samples maintain a map of the senderClientId to its RTCPeerConnection.
2. The samples maintain another map of the senderClientId to a list of pending Ice Candidates.
3. When an ICE candidate is received, check the PeerConnection map. If the PeerConnection map does not have a connection yet, add it to the pending list. Otherwise, add the ICE candidate to the PeerConnection.
4. When the offer is received, it creates the RTCPeerConnection and add it to the PeerConnection map. Then, add all ICE candidates from the pending queue to this PeerConnection.
