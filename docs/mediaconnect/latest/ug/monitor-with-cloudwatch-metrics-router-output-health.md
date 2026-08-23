# AWS Elemental MediaConnect metrics to monitor router output health

AWS Elemental MediaConnect sends metrics to CloudWatch. You can review specific metrics to evaluate the
health of your router outputs. For details about each metric, see the tables in this
section.

For information about flow metrics, see [Metrics to
monitor flow health](monitor-with-cloudwatch-metrics-flow-health.md "monitor-with-cloudwatch-metrics-flow-health.md").

###### Topics

- [Standard output metrics](#monitor-with-cloudwatch-metrics-router-output "#monitor-with-cloudwatch-metrics-router-output")
- [Router output metrics for MediaConnect flow connections](#monitor-with-cloudwatch-metrics-router-output-flow "#monitor-with-cloudwatch-metrics-router-output-flow")
- [Router output metrics for MediaLive connections](#monitor-with-cloudwatch-metrics-router-output-medialive "#monitor-with-cloudwatch-metrics-router-output-medialive")
- [Route metrics](#monitor-with-cloudwatch-metrics-router-output-route "#monitor-with-cloudwatch-metrics-router-output-route")

## Standard output metrics

The following table lists router standard output metrics that AWS Elemental MediaConnect sends
to CloudWatch.

| Metric                       | Description                                                                                                                                                                                                                                                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RouterOutputARQRequests`    | The number of retransmitted packets that were requested<br>through automatic repeat request (ARQ).<br>Units: Count<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, AvailabilityZone<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: RIST, SRT                                               |
| `RouterOutputBitRate`        | The bitrate of the output stream payload, not including protocol<br>overhead.<br>Units: bits per second (bps)<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, AvailabilityZone<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: All                                                          |
| `RouterOutputConnected`      | The status of the output. A value of 1 indicates that the<br>output is connected, and a value of 0 (zero) indicates that<br>the output is disconnected.<br>Units: None<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, AvailabilityZone<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: SRT |
| `RouterOutputDisconnections` | The number of times that the output status changed from<br>connected to disconnected.<br>Units: Count<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, AvailabilityZone<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: SRT                                                                  |
| `RouterOutputFECPackets`     | The number of forward error correction packets sent by the output.<br>Units: Count<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, AvailabilityZone<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: RTP/FEC                                                                                 |
| `RouterOutputLatency`        | The latency of the output stream.<br>Units: Milliseconds<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, AvailabilityZone<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: SRT                                                                                                               |
| `RouterOutputRejections`     | The number of times the connection was rejected by the peer.<br>Units: Count<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, AvailabilityZone<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: SRT                                                                                           |
| `RouterOutputResentPackets`  | The number of packets that were retransmitted to the<br>output destination.<br>Units: Count<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, AvailabilityZone<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: RIST, SRT                                                                      |
| `RouterOutputRoundTripTime`  | The amount of time it takes for the output to send a<br>signal and receive an acknowledgment.<br>Units: Milliseconds<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, AvailabilityZone<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: RIST, SRT                                             |
| `RouterOutputTotalPackets`   | The total number of packets sent by the output.<br>Units: Count<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, AvailabilityZone<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                        |

## Router output metrics for MediaConnect flow connections

When a router output sends content to a MediaConnect flow, MediaConnect
sends the following metrics to CloudWatch.

| Metric                | Description                                                                                                                                                                                                                                                                                          |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RouterOutputBitRate` | The bitrate of the output stream payload, not including protocol<br>overhead.<br>Units: bits per second (bps)<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, AvailabilityZone, DownstreamFlowSourceName, DownstreamFlowARN<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: All |

###### Note

When no AWS Elemental MediaConnect flow is connected to the router output, the
DownstreamFlowSourceName and DownstreamFlowARN dimensions display as
`<unconnected>`.

## Router output metrics for MediaLive connections

When a router output sends content to a MediaLive input, MediaConnect
sends the following metrics to CloudWatch.

| Metric                | Description                                                                                                                                                                                                                                                                         |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RouterOutputBitRate` | The bitrate of the output stream payload, not including protocol<br>overhead.<br>Units: bits per second (bps)<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, AvailabilityZone, DownstreamMediaLiveInputID<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: All |

###### Note

When no MediaLive input is connected to the router output, the
DownstreamMediaLiveInputID dimension displays as
`<unconnected>`.

## Route metrics

These metrics track the connection between a router input and a
router output. MediaConnect publishes these metrics on the output side of the
route.

| Metric                       | Description                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RouteBitRate`               | The bitrate of the content on the route between the router<br>input and the router output.<br>Units: bits per second (bps)<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, RouterOutputAvailabilityZone, RouterInputName, RouterInputID, RouterInputAvailabilityZone<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: All |
| `RouteFabricRecoveryLatency` | The recovery latency for the route between the router<br>input and the router output.<br>Units: Milliseconds<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, RouterOutputAvailabilityZone, RouterInputName, RouterInputID, RouterInputAvailabilityZone<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: All               |
| `RouteNotRecoveredPackets`   | The number of packets lost between the router input and<br>the router output.<br>Units: Count<br>Valid dimensions:<br>• RouterOutputName, RouterOutputID, RouterOutputAvailabilityZone, RouterInputName, RouterInputID, RouterInputAvailabilityZone<br>• RouterOutputARN<br>• AvailabilityZone<br>Protocols: All                              |

###### Note

When the router output is running but not connected to a router input, the
RouterInputName, RouterInputID and RouterInputAvailabilityZone dimensions display
as `<unrouted>`.
