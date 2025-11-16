# Monitor Kinesis Video Streams with WebRTC

You can monitor an Amazon Kinesis Video Streams with WebRTC using Amazon CloudWatch, which collects and
processes raw data from Amazon Kinesis Video Streams with WebRTC into readable, near real-time metrics. These
statistics are recorded for a period of 15 months, so that you can access historical information
and gain a better perspective on how your web application or service is performing.

Amazon Kinesis Video Streams provides the following metrics:

###### Topics

- [Signaling metrics](#kvswebrtc-monitoring-cw-signaling "#kvswebrtc-monitoring-cw-signaling")
- [TURN metrics](#kvswebrtc-monitoring-cw-turn "#kvswebrtc-monitoring-cw-turn")
- [WebRTC ingestion metrics](#kvswebrtc-monitoring-cw-ingest "#kvswebrtc-monitoring-cw-ingest")

## Signaling metrics

This section provides information on how to monitor and troubleshoot signaling-related issues using CloudWatch Logs.

| Metric name                   | Description                                                                                                | Unit         | Dimensions                      |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------ | ------------------------------- |
| **Failure**                   | '0' is emitted if the Operation mentioned in dimension returns 200 status code<br>response. '1' otherwise. | Count        | Operation, SignalingChannelName |
| **Latency**                   | Measures the time it takes for the service to receive a request and return<br>a response.                  | Milliseconds | Operation, SignalingChannelName |
| **MessagesTransferred.Count** | The total number of messages sent and received for a channel.                                              | Count        | SignalingChannelName            |

The `Operation` dimension applies to the following APIs:

- ConnectAsMaster
- ConnectAsViewer
- SendSdpOffer
- SendSdpAnswer
- SendCandidate
- SendAlexaOfferToMaster
- GetIceServerConfig
- Disconnect

## TURN metrics

This section provides information on how to monitor and troubleshoot TURN-related issues
using CloudWatch Logs.

| Metric name              | Description                                                                              | Unit  | Dimensions           |
| ------------------------ | ---------------------------------------------------------------------------------------- | ----- | -------------------- |
| **TURNConnectedMinutes** | '1' is emitted for each TURN allocation that is used to stream data through in a minute. | Count | SignalingChannelName |

## WebRTC ingestion metrics

This section provides information on how to monitor and troubleshoot WebRTC ingestion-related issues using CloudWatch Logs.

| Metric name                | Description                                                                                                                                                                    | Unit         | Dimensions                            |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | ------------------------------------- |
| **Failure**                | '0' is emitted if the Operation mentioned in dimension returns 200 status code response. '1' otherwise.                                                                        | Count        | Operation, SignalingChannelName       |
| **Latency**                | Measures the time it takes for the service to receive a request and return a response.                                                                                         | Milliseconds | Operation, SignalingChannelName       |
| **TotalBitrate**           | Total bitrate sent. If Role is specified, this represents the total bitrate sent by the MASTER participant or the aggregate total bitrate sent by the VIEWER participant.      | bps          | Operation, SignalingChannelName, Role |
| **TotalPacketCount**       | Total packet count sent. If Role is specified, this represents the total bitrate sent by the MASTER participant or the aggregate total bitrate sent by the VIEWER participant. | Count        | Operation, SignalingChannelName, Role |
| **WebRTCRecordingMinutes** | The number of WebRTCRecordingMinute occured for a channel.                                                                                                                     | Count        | Operation, SignalingChannelName, Role |
| **WebRTCViewerMinutes**    | The number of WebRTCViewerMinute occured for a channel.                                                                                                                        | Count        | Operation, SignalingChannelName, Role |

The `Operation` dimension applies to the following APIs:

- JoinStorageSession
- JoinStorageSessionAsViewer

`Role` dimension:

- MASTER
- VIEWER
