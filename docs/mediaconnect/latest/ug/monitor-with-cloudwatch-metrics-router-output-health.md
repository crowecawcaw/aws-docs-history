# AWS Elemental MediaConnect metrics to monitor router output health

AWS Elemental MediaConnect sends metrics to CloudWatch. You can review specific metrics to evaluate the
health of your router outputs. For details about each metric, see the tables in this
section.

For information about flow metrics, see [Metrics to
monitor flow health](monitor-with-cloudwatch-metrics-flow-health.md "monitor-with-cloudwatch-metrics-flow-health.md").

###### Topics

- [Router output
  metrics](#monitor-with-cloudwatch-metrics-router-output "#monitor-with-cloudwatch-metrics-router-output")

## Router output

metrics

The following table lists router output metrics that AWS Elemental MediaConnect sends
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
