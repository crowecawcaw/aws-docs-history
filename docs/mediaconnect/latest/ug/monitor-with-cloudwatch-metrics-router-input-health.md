

# AWS Elemental MediaConnect metrics to monitor router input health
<a name="monitor-with-cloudwatch-metrics-router-input-health"></a>

AWS Elemental MediaConnect sends metrics to CloudWatch. You can review specific metrics to evaluate the health of your router inputs. For details about each metric, see the tables in this section.

For information about flow metrics, see [Metrics to monitor flow health](monitor-with-cloudwatch-metrics-flow-health.md).

**Topics**
+ [Router input metrics](#monitor-with-cloudwatch-metrics-router-input)
+ [Content quality metrics for router inputs](#monitor-with-cloudwatch-metrics-router-input-content-quality)
+ [Failover metrics for router inputs](#monitor-with-cloudwatch-metrics-router-input-failover)
+ [Merge metrics for router inputs](#monitor-with-cloudwatch-metrics-router-input-merge)
+ [Router input metrics for MediaConnect flow connections](#monitor-with-cloudwatch-metrics-router-input-flow)

## Router input metrics
<a name="monitor-with-cloudwatch-metrics-router-input"></a>

The following table lists router input metrics that AWS Elemental MediaConnect sends to CloudWatch.


| Metric | Description | 
| --- | --- | 
| RouterInputARQRequests | The number of retransmitted packets that were requested through automatic repeat request (ARQ).<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: RIST, SRT | 
| RouterInputBitRate | The bitrate of the payload, not including protocol overhead.<br />Units: bits per second (bps)<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputCCErrors | The number of times that a continuity error occurred. This error indicates an incorrect packet order or lost packets.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputConnected | The status of the input. A value of 1 indicates that the input is connected, and a value of 0 (zero) indicates that the input is disconnected.<br />Units: None<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: SRT | 
| RouterInputDisconnections | The number of times that the input status changed from connected to disconnected.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: SRT | 
| RouterInputFECPackets | The number of forward error correction packets.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: RTP/FEC | 
| RouterInputJitter | The jitter measurement specific to the protocol being used.<br />Units: Milliseconds<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: RIST, SRT | 
| RouterInputLatency | The recovery latency of the input stream.<br />Units: Milliseconds<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: RIST, SRT, RTP/FEC | 
| RouterInputNotRecoveredPackets | The number of packets that were lost during transit and were not recovered by error correction.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputRecoveredPackets | The number of packets that were recovered through retransmission.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputRejections | The number of times the connection was rejected by the peer.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: SRT | 
| RouterInputRoundTripTime | The amount of time it takes for the input to send a signal and receive an acknowledgment.<br />Units: Milliseconds<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTotalPackets | The total number of packets received by the input.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTR101PCRAccuracyError | The number of PCR accuracy errors in the transport stream.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTR101TSByteError | The number of times that a transport stream byte error occurred. This error indicates that the sync byte did not appear after the prescribed number of bytes.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTR101TSSyncLoss | The number of transport stream sync loss errors.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputUptime | The amount of time the input has been receiving data.<br />Units: Seconds<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 

## Content quality metrics for router inputs
<a name="monitor-with-cloudwatch-metrics-router-input-content-quality"></a>

The following table lists the content quality metrics that AWS Elemental MediaConnect sends to CloudWatch.


| Metric | Description | 
| --- | --- | 
|  RouterInputAudioStreamMissing  | Monitors instances when the expected audio stream is not detected in the content. A value of 1 indicates that the audio stream is missing from the router input and a value of 0 (zero) indicates that the audio stream is present. <br />Units: None<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone  | 
|  RouterInputBlackFramesBreaching  | Monitors instances when the duration of black frames in the video exceeds the specified threshold. A value of 1 indicates that the duration is breaching the specified threshold and a value of 0 (zero) indicates that the duration is not breaching the specified threshold. <br />Units: None<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone  | 
|  RouterInputFrozenFramesBreaching  | Monitors instances when the video remains unchanged for longer than the specified threshold. A value of 1 indicates that the duration is breaching the specified threshold and a value of 0 (zero) indicates that the duration is not breaching the specified threshold. <br />Units: None<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone  | 
|  RouterInputSilentAudioBreaching  | Monitors instances when the duration of silent audio exceeds the specified threshold. A value of 1 indicates that the duration is breaching the specified threshold and a value of 0 (zero) indicates that the duration is not breaching the specified threshold. <br />Units: None<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone  | 
|  RouterInputTimecodePresent  | Indicates whether a valid timecode is present in the media stream. A value of 1 indicates that a valid timecode is present in the media stream and a value of 0 (zero) indicates that a valid timecode is not present in the media stream. <br />Units: None<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone  | 
|  RouterInputVideoStreamMissing  | Monitors instances when the expected video stream is absent from the content. A value of 1 indicates that the video stream is missing from the router input and a value of 0 (zero) indicates that the video stream is present. <br />Units: None<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone  | 

## Failover metrics for router inputs
<a name="monitor-with-cloudwatch-metrics-router-input-failover"></a>

When you configure a router input for failover, MediaConnect collects two sets of metrics: aggregate metrics for the overall router input, as well as source-level metrics to track the individual failover sources. 

### Aggregate failover metrics
<a name="cloudwatch-metrics-router-input-failover-aggregate"></a>

These metrics give you a view of the failover router input's performance. 


| Metric | Description | 
| --- | --- | 
| RouterInputFailoverActiveSource | Index of the currently active source.<br />Units: None<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputFailoverSwitches | The total number of times the router input has switched sources.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: Protocols: All | 
| RouterInputPostFailoverBitRate | The bitrate of the payload after failover, not including protocol overhead. <br />Units: bits per second (bps)<br />Valid dimensions: +  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputPostFailoverCCErrors | The number of continuity errors in the transport stream after failover.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputPostFailoverNotRecoveredPackets | The number of unrecovered packets after failover.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputPostFailoverRecoveredPackets | The number of recovered packets after failover.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputPostFailoverTR101PCRAccuracyError | The number of PCR accuracy errors in the transport stream after failover.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputPostFailoverTR101TSByteError | The number of times that a transport stream byte error occurred after failover. This error indicates that the sync byte did not appear after the prescribed number of bytes.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputPostFailoverTR101TSSyncLoss | The number of transport stream sync loss errors after failover.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 

### Source-level failover metrics
<a name="cloudwatch-metrics-router-input-failover-source"></a>

For router inputs that are configured for failover, the basic router input metrics are also available with an additional `RouterInputFailoverSourceIndex` dimension. This enables you to monitor the performance of the first failover source (`RouterInputFailoverSourceIndex=0`) and the second failover source (`RouterInputFailoverSourceIndex=1`) separately.


| Metric | Description | 
| --- | --- | 
| RouterInputARQRequests | The number of retransmitted packets that were requested through automatic repeat request (ARQ).<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: RIST, SRT | 
| RouterInputBitRate | The bitrate of the payload, not including protocol overhead. <br />Units: bits per second (bps)<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputCCErrors | The number of times that a continuity error occurred. This error indicates an incorrect packet order or lost packets.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputConnected | The status of the input. A value of 1 indicates that the input is connected, and a value of 0 (zero) indicates that the input is disconnected.<br />Units: None<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: SRT | 
| RouterInputDisconnections | The number of times that the input status changed from connected to disconnected.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: SRT | 
| RouterInputFECPackets | The number of forward error correction packets.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: RTP/FEC | 
| RouterInputJitter | The jitter measurement specific to the protocol being used.<br />Units: Milliseconds<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: RIST, SRT | 
| RouterInputLatency | The recovery latency of the input stream.<br />Units: Milliseconds<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputNotRecoveredPackets | The number of packets that were lost during transit and were not recovered by error correction.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputRecoveredPackets | The number of packets that were recovered through retransmission.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputRejections | The number of times the connection was rejected by the peer.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: SRT | 
| RouterInputRoundTripTime | The amount of time it takes for the input to send a signal and receive an acknowledgment.<br />Units: Milliseconds<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTotalPackets | The total number of packets received by the input.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTR101PCRAccuracyError | The number of PCR accuracy errors in the transport stream.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTR101TSByteError | The number of times that a transport stream byte error occurred. This error indicates that the sync byte did not appear after the prescribed number of bytes.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTR101TSSyncLoss | The number of transport stream sync loss errors.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputUptime | The amount of time the input has been receiving data.<br />Units: Seconds<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputFailoverSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputFailoverSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 

## Merge metrics for router inputs
<a name="monitor-with-cloudwatch-metrics-router-input-merge"></a>

Similar to failover, when you configure a router input for merge, MediaConnect provides both aggregate and source-level metrics.

### Aggregate merge metrics
<a name="cloudwatch-metrics-router-input-merge-aggregate"></a>

These metrics give you a high-level, overall view of the merge input's performance. They include data that applies to the entire merge configuration, without differentiating between the two merge sources.


| Metric | Description | 
| --- | --- | 
| RouterInputMergeActive | The merge status of all router input sources. A value of 1 indicates that all sources are merged. A value of 0 (zero) indicates that at least one source is not actively merged with 2022-7. <br />Units: None<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: RTP, RIST | 
| RouterInputMergeSkew | Maximum time skew between the two router input sources.<br />Units: Milliseconds<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: RTP, RIST | 
| RouterInputPostMergeBitRate | The bitrate of the payload after merge, not including protocol overhead. <br />Units: bits per second (bps)<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: RTP, RIST | 
| RouterInputPostMergeCCErrors | The number of continuity errors in the transport stream after merge.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: RTP, RIST | 
| RouterInputPostMergeNotRecoveredPackets | The number of unrecovered packets after merge.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: RTP, RIST | 
| RouterInputPostMergeRecoveredPackets | The number of recovered packets after merge.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: RTP, RIST | 
| RouterInputPostMergeTR101PCRAccuracyError | The number of PCR accuracy errors in the transport stream after merge.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputPostMergeTR101TSByteError | The number of times that a transport stream byte error occurred after merge. This error indicates that the sync byte did not appear after the prescribed number of bytes.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputPostMergeTR101TSSyncLoss | The number of transport stream sync loss errors after merge.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 

### Source-level merge metrics
<a name="cloudwatch-metrics-router-input-merge-source"></a>

For router inputs that are configured for merge, the basic router input metrics are also available with an additional `RouterInputMergeSourceIndex` dimension. This enables you to monitor the performance of the first merge source (`RouterInputMergeSourceIndex=0`) and the second merge source (`RouterInputMergeSourceIndex=1`) separately.


| Metric | Description | 
| --- | --- | 
| RouterInputARQRequests | The number of retransmitted packets that were requested through automatic repeat request (ARQ).<br />Units: Count<br />Valid dimensions: +  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputBitRate | The bitrate of the payload, not including protocol overhead.<br />Units: bits per second (bps)<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputCCErrors | The number of times that a continuity error occurred. This error indicates an incorrect packet order or lost packets.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputConnected | The status of the input. A value of 1 indicates that the input is connected, and a value of 0 (zero) indicates that the input is disconnected.<br />Units: None<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: SRT | 
| RouterInputDisconnections | The number of times that the input status changed from connected to disconnected.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: SRT | 
| RouterInputFECPackets | The number of forward error correction packets.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: RTP/FEC | 
| RouterInputJitter | The jitter measurement specific to the protocol being used.<br />Units: Milliseconds<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: RIST, SRT | 
| RouterInputLatency | The recovery latency of the input stream.<br />Units: Milliseconds<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputNotRecoveredPackets | The number of packets that were lost during transit and were not recovered by error correction.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputRecoveredPackets | The number of packets that were recovered through retransmission.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputRejections | The number of times the connection was rejected by the peer.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: SRT | 
| RouterInputRoundTripTime | The amount of time it takes for the input to send a signal and receive an acknowledgment.<br />Units: Milliseconds<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTotalPackets | The total number of packets received by the input.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTR101PCRAccuracyError | The number of PCR accuracy errors in the transport stream.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTR101TSByteError | The number of times that a transport stream byte error occurred. This error indicates that the sync byte did not appear after the prescribed number of bytes.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTR101TSSyncLoss | The number of transport stream sync loss errors.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputUptime | The amount of time the input has been receiving data.<br />Units: Seconds<br />Valid dimensions:+  RouterInputName, RouterInputID, RouterInputMergeSourceIndex, AvailabilityZone <br />+  RouterInputARN, RouterInputMergeSourceIndex <br />+  AvailabilityZone <br />Protocols: All | 

## Router input metrics for MediaConnect flow connections
<a name="monitor-with-cloudwatch-metrics-router-input-flow"></a>

When a router input receives content from a MediaConnect flow, MediaConnect sends the following metrics to CloudWatch. 


| Metric | Description | 
| --- | --- | 
| RouterInputBitRate | The bitrate of the payload, not including protocol overhead.<br />Units: bits per second (bps)<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone, UpstreamFlowOutputName, UpstreamFlowARN <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputCCErrors | The number of times that a continuity error occurred. This error indicates an incorrect packet order or lost packets.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone, UpstreamFlowOutputName, UpstreamFlowARN <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputLatency | The recovery latency of the input stream.<br />Units: Milliseconds<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone, UpstreamFlowOutputName, UpstreamFlowARN <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: RIST, SRT, RTP/FEC | 
| RouterInputNotRecoveredPackets | The number of packets that were lost during transit and were not recovered by error correction.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone, UpstreamFlowOutputName, UpstreamFlowARN <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputRecoveredPackets | The number of packets that were recovered through retransmission.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone, UpstreamFlowOutputName, UpstreamFlowARN <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTR101PCRAccuracyError | The number of PCR accuracy errors in the transport stream.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone, UpstreamFlowOutputName, UpstreamFlowARN <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTR101TSByteError | The number of times that a transport stream byte error occurred. This error indicates that the sync byte did not appear after the prescribed number of bytes.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone, UpstreamFlowOutputName, UpstreamFlowARN <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputTR101TSSyncLoss | The number of transport stream sync loss errors.<br />Units: Count<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone, UpstreamFlowOutputName, UpstreamFlowARN <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 
| RouterInputUptime | The amount of time the input has been receiving data.<br />Units: Seconds<br />Valid dimensions:+  RouterInputName, RouterInputID, AvailabilityZone, UpstreamFlowOutputName, UpstreamFlowARN <br />+  RouterInputARN <br />+  AvailabilityZone <br />Protocols: All | 

**Note**  
When no MediaConnect flow is connected to the router input, the UpstreamFlowOutputName and UpstreamFlowARN dimensions display as `<unconnected>`. 