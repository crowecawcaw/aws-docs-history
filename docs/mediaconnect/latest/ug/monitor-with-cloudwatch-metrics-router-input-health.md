# AWS Elemental MediaConnect

metrics to monitor router input health

AWS Elemental MediaConnect sends metrics to CloudWatch. You can review specific metrics to evaluate the
health of your router inputs. For details about each metric, see the
tables in this section.

For information about flow metrics, see [Metrics to
monitor flow health](monitor-with-cloudwatch-metrics-flow-health.md "monitor-with-cloudwatch-metrics-flow-health.md").

###### Topics

- [Router input
  metrics](#monitor-with-cloudwatch-metrics-router-input "#monitor-with-cloudwatch-metrics-router-input")
- [Failover
  metrics for router inputs](#monitor-with-cloudwatch-metrics-router-input-failover "#monitor-with-cloudwatch-metrics-router-input-failover")
- [Merge
  metrics for router inputs](#monitor-with-cloudwatch-metrics-router-input-merge "#monitor-with-cloudwatch-metrics-router-input-merge")

## Router input

metrics

The following table lists router input metrics that AWS Elemental MediaConnect sends to
CloudWatch.

| Metric                             | Description                                                                                                                                                                                                                                                                                                                |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RouterInputARQRequests`           | The number of retransmitted packets that were requested<br>through automatic repeat request (ARQ).<br>Units: Count<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: RIST, SRT                                                            |
| `RouterInputBitRate`               | The bitrate of the payload, not including protocol<br>overhead.<br>Units: bits per second (bps)<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                     |
| `RouterInputCCErrors`              | The number of times that a continuity error occurred. This<br>error indicates an incorrect packet order or lost<br>packets.<br>Units: Count<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                         |
| `RouterInputConnected`             | The status of the input. A value of 1 indicates that the<br>input is connected, and a value of 0 (zero) indicates that<br>the input is disconnected.<br>Units: None<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: SRT                 |
| `RouterInputDisconnections`        | The number of times that the input status changed from<br>connected to disconnected.<br>Units: Count<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: SRT                                                                                |
| `RouterInputFECPackets`            | The number of forward error correction packets.<br>Units: Count<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: RTP/FEC                                                                                                                 |
| `RouterInputJitter`                | The jitter measurement specific to the protocol being<br>used.<br>Units: Milliseconds<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: RIST, SRT                                                                                         |
| `RouterInputLatency`               | The recovery latency of the input stream.<br>Units: Milliseconds<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: RIST, SRT, RTP/FEC                                                                                                     |
| `RouterInputNotRecoveredPackets`   | The number of packets that were lost during transit and<br>were not recovered by error correction.<br>Units: Count<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                  |
| `RouterInputRecoveredPackets`      | The number of packets that were recovered through<br>retransmission.<br>Units: Count<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                |
| `RouterInputRejections`            | The number of times the connection was rejected by the peer.<br>Units: Count<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: SRT                                                                                                        |
| `RouterInputRoundTripTime`         | The amount of time it takes for the input to send a signal<br>and receive an acknowledgment.<br>Units: Milliseconds<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                 |
| `RouterInputTotalPackets`          | The total number of packets received by the input.<br>Units: Count<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                                  |
| `RouterInputTR101PCRAccuracyError` | The number of PCR accuracy errors in the transport<br>stream.<br>Units: Count<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                       |
| `RouterInputTR101TSByteError`      | The number of times that a transport stream byte error<br>occurred. This error indicates that the sync byte did not<br>appear after the prescribed number of bytes.<br>Units: Count<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All |
| `RouterInputTR101TSSyncLoss`       | The number of transport stream sync loss errors.<br>Units: Count<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                                    |
| `RouterInputUptime`                | The amount of time the input has been receiving data.<br>Units: Seconds<br>Valid dimensions:<br>• RouterInputName, RouterInputID, AvailabilityZone<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                             |

## Failover

metrics for router inputs

When you configure a router input for failover, MediaConnect collects two sets
of metrics: aggregate metrics for the overall router input, as well as
source-level metrics to track the individual failover sources.

### Aggregate failover

metrics

These metrics give you a view of the failover router input's performance.

| Metric                                         | Description                                                                                                                                                                                                                                                                         |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RouterInputFailoverActiveSource`              | Index of the currently active source.<br>Units: None<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                                                               |
| `RouterInputFailoverSwitches`                  | The total number of times the router input has switched sources.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: Protocols: All                                                                                                        |
| `RouterInputPostFailoverBitRate`               | The bitrate of the payload after failover, not including protocol<br>overhead.<br>Units: bits per second (bps)<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                     |
| `RouterInputPostFailoverCCErrors`              | The number of continuity errors in the transport stream<br>after failover.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                         |
| `RouterInputPostFailoverNotRecoveredPackets`   | The number of unrecovered packets after failover.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                                                  |
| `RouterInputPostFailoverRecoveredPackets`      | The number of recovered packets after failover.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                                                    |
| `RouterInputPostFailoverTR101PCRAccuracyError` | The number of PCR accuracy errors in the transport<br>stream after failover.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                       |
| `RouterInputPostFailoverTR101TSByteError`      | The number of times that a transport stream byte error<br>occurred after failover. This error indicates that the sync byte did not<br>appear after the prescribed number of bytes.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All |
| `RouterInputPostFailoverTR101TSSyncLoss`       | The number of transport stream sync loss errors after failover.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                                    |

### Source-level failover

metrics

For router inputs that are configured for failover, the basic router input
metrics are also available with an additional `RouterInputFailoverSourceIndex`
dimension. This enables you to monitor the performance of the primary
failover source (`RouterInputFailoverSourceIndex=0`) and the secondary failover
source (`RouterInputFailoverSourceIndex=1`) separately.

| Metric                             | Description                                                                                                                                                                                                                                                                                          |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RouterInputARQRequests`           | The number of retransmitted packets that were requested<br>through automatic repeat request (ARQ).<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: RIST, SRT                                                            |
| `RouterInputBitRate`               | The bitrate of the payload, not including protocol<br>overhead.<br>Units: bits per second (bps)<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                     |
| `RouterInputCCErrors`              | The number of times that a continuity error occurred. This<br>error indicates an incorrect packet order or lost<br>packets.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: All                                         |
| `RouterInputConnected`             | The status of the input. A value of 1 indicates that the<br>input is connected, and a value of 0 (zero) indicates that<br>the input is disconnected.<br>Units: None<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: SRT                 |
| `RouterInputDisconnections`        | The number of times that the input status changed from<br>connected to disconnected.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: SRT                                                                                |
| `RouterInputFECPackets`            | The number of forward error correction packets.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: RTP/FEC                                                                                                                 |
| `RouterInputJitter`                | The jitter measurement specific to the protocol being<br>used.<br>Units: Milliseconds<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: RIST, SRT                                                                                         |
| `RouterInputLatency`               | The recovery latency of the input stream.<br>Units: Milliseconds<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                                                    |
| `RouterInputNotRecoveredPackets`   | The number of packets that were lost during transit and<br>were not recovered by error correction.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                  |
| `RouterInputRecoveredPackets`      | The number of packets that were recovered through<br>retransmission.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                                |
| `RouterInputRejections`            | The number of times the connection was rejected by the peer.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: SRT                                                                                                        |
| `RouterInputRoundTripTime`         | The amount of time it takes for the input to send a signal<br>and receive an acknowledgment.<br>Units: Milliseconds<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                 |
| `RouterInputTotalPackets`          | The total number of packets received by the input.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                                                  |
| `RouterInputTR101PCRAccuracyError` | The number of PCR accuracy errors in the transport<br>stream.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                                       |
| `RouterInputTR101TSByteError`      | The number of times that a transport stream byte error<br>occurred. This error indicates that the sync byte did not<br>appear after the prescribed number of bytes.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: All |
| `RouterInputTR101TSSyncLoss`       | The number of transport stream sync loss errors.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                                                    |
| `RouterInputUptime`                | The amount of time the input has been receiving data.<br>Units: Seconds<br>Valid dimensions:<br>• RouterInputARN, RouterInputFailoverSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                                             |

## Merge

metrics for router inputs

Similar to failover, when you configure a router input for merge, MediaConnect
provides both aggregate and source-level metrics.

### Aggregate merge metrics

These metrics give you a high-level, overall view of the merge input's
performance. They include data that applies to the entire merge
configuration, without differentiating between the two merge sources.

| Metric                                      | Description                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RouterInputMergeActive`                    | The merge status of all router input sources. A value of 1<br>indicates that all sources are merged. A value of 0 (zero)<br>indicates that at least one source is not actively merged<br>with 2022-7.<br>Units: None<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: RTP, RIST |
| `RouterInputMergeSkew`                      | Maximum time skew between the two router input sources.<br>Units: Milliseconds<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: RTP, RIST                                                                                                                                       |
| `RouterInputPostMergeBitRate`               | The bitrate of the payload after merge, not including protocol<br>overhead.<br>Units: bits per second (bps)<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: RTP, RIST                                                                                                          |
| `RouterInputPostMergeCCErrors`              | The number of continuity errors in the transport stream<br>after merge.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: RTP, RIST                                                                                                                              |
| `RouterInputPostMergeNotRecoveredPackets`   | The number of unrecovered packets after merge.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: RTP, RIST                                                                                                                                                       |
| `RouterInputPostMergeRecoveredPackets`      | The number of recovered packets after merge.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: RTP, RIST                                                                                                                                                         |
| `RouterInputPostMergeTR101PCRAccuracyError` | The number of PCR accuracy errors in the transport<br>stream after merge.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                                                  |
| `RouterInputPostMergeTR101TSByteError`      | The number of times that a transport stream byte error<br>occurred after merge. This error indicates that the sync byte did not<br>appear after the prescribed number of bytes.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                            |
| `RouterInputPostMergeTR101TSSyncLoss`       | The number of transport stream sync loss errors after merge.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN<br>• AvailabilityZone<br>Protocols: All                                                                                                                                               |

### Source-level merge metrics

For router inputs that are configured for merge, the basic router input
metrics are also available with an additional `RouterInputMergeSourceIndex`
dimension. This enables you to monitor the performance of the first merge
source (`RouterInputMergeSourceIndex=0`) and the second merge source
(`RouterInputMergeSourceIndex=1`) separately.

| Metric                             | Description                                                                                                                                                                                                                                                                                       |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RouterInputARQRequests`           | The number of retransmitted packets that were<br>requested through automatic repeat request (ARQ).<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                  |
| `RouterInputBitRate`               | The bitrate of the payload, not including protocol<br>overhead.<br>Units: bits per second (bps)<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                     |
| `RouterInputCCErrors`              | The number of times that a continuity error occurred. This<br>error indicates an incorrect packet order or lost<br>packets.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: All                                         |
| `RouterInputConnected`             | The status of the input. A value of 1 indicates that the<br>input is connected, and a value of 0 (zero) indicates that<br>the input is disconnected.<br>Units: None<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: SRT                 |
| `RouterInputDisconnections`        | The number of times that the input status changed from<br>connected to disconnected.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: SRT                                                                                |
| `RouterInputFECPackets`            | The number of forward error correction packets.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: RTP/FEC                                                                                                                 |
| `RouterInputJitter`                | The jitter measurement specific to the protocol being<br>used.<br>Units: Milliseconds<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: RIST, SRT                                                                                         |
| `RouterInputLatency`               | The recovery latency of the input stream.<br>Units: Milliseconds<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                                                    |
| `RouterInputNotRecoveredPackets`   | The number of packets that were lost during transit and<br>were not recovered by error correction.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                  |
| `RouterInputRecoveredPackets`      | The number of packets that were recovered through<br>retransmission.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                                |
| `RouterInputRejections`            | The number of times the connection was rejected by the peer.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: SRT                                                                                                        |
| `RouterInputRoundTripTime`         | The amount of time it takes for the input to send a signal<br>and receive an acknowledgment.<br>Units: Milliseconds<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                 |
| `RouterInputTotalPackets`          | The total number of packets received by the input.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                                                  |
| `RouterInputTR101PCRAccuracyError` | The number of PCR accuracy errors in the transport<br>stream.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                                       |
| `RouterInputTR101TSByteError`      | The number of times that a transport stream byte error<br>occurred. This error indicates that the sync byte did not<br>appear after the prescribed number of bytes.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: All |
| `RouterInputTR101TSSyncLoss`       | The number of transport stream sync loss errors.<br>Units: Count<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                                                    |
| `RouterInputUptime`                | The amount of time the input has been receiving data.<br>Units: Seconds<br>Valid dimensions:<br>• RouterInputARN, RouterInputMergeSourceIndex<br>• AvailabilityZone<br>Protocols: All                                                                                                             |
