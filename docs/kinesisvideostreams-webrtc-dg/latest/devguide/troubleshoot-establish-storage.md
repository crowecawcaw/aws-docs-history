# Troubleshoot issues connecting with the storage session

This section provides guidance on troubleshooting issues related to setting up and configuring storage for recording video streams.

###### Topics

- [Controlling and controlled peers](#troubleshoot-control-peers "#troubleshoot-control-peers")
- [Review supported codecs](#troubleshoot-review-codecs "#troubleshoot-review-codecs")

## Controlling and controlled peers

In WebRTC, the controlling peer initiates the connection to the controlled
peer by sending an SDP offer. For peer-to-peer sessions, the viewer participant
initiates the connection by sending an offer to the master participant through
Signaling. When connecting to the storage session for WebRTC ingestion, the storage
session is the controlling peer. For master participants, they still remain the
controlled participant. However, viewer participants switch from controlling to
controlled.

Upon calling [JoinStorageSession](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md") or [JoinStorageSessionAsViewer](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md"), all participants
must respond with an SDP answer and exchange ICE candidates with the storage
session.

For a sequence diagram, see [Understanding WebRTC ingestion and storage](getting-started-ingestion.md#understanding-ingestion "getting-started-ingestion.md#understanding-ingestion").

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
