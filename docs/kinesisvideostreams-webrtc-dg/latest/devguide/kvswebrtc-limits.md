# Amazon Kinesis Video Streams with WebRTC service quotas

Kinesis Video Streams with WebRTC has the following service quotas:

###### Important

The following service quotas are either soft **[s]**, which can
be increased, or hard **[h]**, which can't be increased. You will
see [s] and [h] next to individual service quota in the tables below.

###### Note

TPS stands for _transactions per second_.

###### Topics

- [Control plane API service quotas](#limits-control-plane "#limits-control-plane")
- [Signaling API service quotas](#limits-signaling-service "#limits-signaling-service")
- [TURN service quotas](#limits-turn-service "#limits-turn-service")
- [WebRTC ingestion service quotas](#limits-ingestion "#limits-ingestion")
- [Troubleshooting](#troubleshooting "#troubleshooting")

## Control plane API service quotas

The following section describes service quotas for the control plane APIs.

| API                                   | Maximum API request rate per AWS account | Maximum number of channels per AWS account per AWS Region                                                                       | Maximum API request per channel |
| ------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **CreateSignalingChannel**            | 50 TPS [s]                               | • For US East (N. Virginia) (us-east-1) and US West (Oregon) (us-west-2) only - 10,000<br>• All other supported Regions - 5,000 | N/A                             |
| **DeleteSignalingChannel**            | 50 TPS [h]                               | N/A                                                                                                                             | 5 TPS [h]                       |
| **DescribeMediaStorageConfiguration** | 50 TPS [h]                               | N/A                                                                                                                             | 5 TPS [h]                       |
| **DescribeSignalingChannel**          | 300 TPS [h]                              | N/A                                                                                                                             | 5 TPS [h]                       |
| **GetSignalingChannelEndpoint**       | 300 TPS [h]                              | N/A                                                                                                                             | N/A                             |
| **ListSignalingChannels**             | 50 TPS [h]                               | N/A                                                                                                                             | N/A                             |
| **ListTagsForResource**               | 50 TPS [h]                               | N/A                                                                                                                             | 5 TPS [h]                       |
| **TagResource**                       | 50 TPS [h]                               | N/A                                                                                                                             | 5 TPS [h]                       |
| **UntagResource**                     | 50 TPS [h]                               | N/A                                                                                                                             | 5 TPS [h]                       |
| **UpdateMediaStorageConfiguration**   | 10 TPS [h]                               | N/A                                                                                                                             | 5 TPS [h]                       |
| **UpdateSignalingChannel**            | 50 TPS [h]                               | N/A                                                                                                                             | 5 TPS [h]                       |

## Signaling API service quotas

The following section describes service quotas for the signaling component in Kinesis Video Streams with
WebRTC. For more information, see [How it works](kvswebrtc-how-it-works.md "kvswebrtc-how-it-works.md").

| API             | Maximum GO_AWAY message grace period prior to terminating connection | Maximum API request rate per channel | Maximum number of concurrent connections per channel | Maximum connection duration | Maximum idle connection timeout period |
| --------------- | -------------------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------- | --------------------------- | -------------------------------------- |
| ConnectAsMaster | 1 minute (h)                                                         | 3 TPS (h)                            | 1 (h)                                                | 1 hour (h)                  | 10 minutes (h)                         |
| ConnectAsViewer | 1 minute (h)                                                         | 3 TPS (h)                            | 10 (s)                                               | 1 hour (h)                  | 10 minutes (h)                         |

| API                    | Maximum API request rate                                                          | Maximum message payload size |
| ---------------------- | --------------------------------------------------------------------------------- | ---------------------------- |
| SendAlexaOffertoMaster | • 5 TPS per signaling channel (h)<br>• 100 TPS per AWS Region per AWS account (s) | N/A                          |
| SendICECandidate       | 20 TPS per WebSocket connection (h)                                               | 10k (h)                      |
| SendSDPAnswer          | 5 TPS per WebSocket connection (h)                                                | 10k (h)                      |
| SendSDPOffer           | 5 TPS per WebSocket connection (h)                                                | 10k (h)                      |

## TURN service quotas

The following section describes service quotas for the Traversal Using Relays around NAT
(TURN) component in Kinesis Video Streams with WebRTC. For more information, see [How it works](kvswebrtc-how-it-works.md "kvswebrtc-how-it-works.md").

| API or parameter      | Value                                                                             |
| --------------------- | --------------------------------------------------------------------------------- |
| GetIceServerConfig    | • 5 TPS per signaling channel (h)<br>• 100 TPS per AWS Region per AWS account (s) |
| Bit Rate              | 5Mbps (h)                                                                         |
| Credential Lifecycle  | 5 minutes (h)                                                                     |
| Number of allocations | 50 per signaling channel (h)                                                      |

## WebRTC ingestion service quotas

The following section describes service quotas for the media recording component in Amazon Kinesis Video Streams WebRTC. For more information, see [Use Amazon Kinesis Video Streams with WebRTC to ingest and store media](webrtc-ingestion.md "webrtc-ingestion.md").

**JoinStorageSession**

- API:
  - Per AWS account - 50 TPS (h)
  - Per channel - 2 TPS (h)

- Streaming session quotas:
  - Bit rate - 1 Mbps (s)
  - Session duration - 1 hour (h)
  - Idle timeout - 3 minutes (h)

## Troubleshooting

You can only connect **one** master and **one or more** viewers to a single signaling channel.

It isn't possible to connect multiple masters to a single
signaling channel.
