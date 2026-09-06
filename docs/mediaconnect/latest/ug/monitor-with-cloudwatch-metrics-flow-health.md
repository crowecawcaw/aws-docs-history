

# AWS Elemental MediaConnect metrics to monitor flow health
<a name="monitor-with-cloudwatch-metrics-flow-health"></a>

AWS Elemental MediaConnect sends metrics to CloudWatch. You can review specific metrics to evaluate the health of your flow. If the flow is unhealthy, these metrics can help you determine where the issue originates. For details about each metric, see the tables in this section.

For information about source metrics, see [Metrics to monitor flow source health](monitor-with-cloudwatch-metrics-source-health.md).

**Note**  
Metrics tracked by MediaConnect adhere to the standard as defined by the TR 101 290 spec.

**Topics**
+ [Flow metrics](#monitor-with-cloudwatch-metrics-flow-health-flow)
+ [TR 101 290 Priority 1 metrics](#monitor-with-cloudwatch-metrics-flow-health-p1)
+ [TR 101 290 Priority 2 metrics](#monitor-with-cloudwatch-metrics-flow-health-p2)
+ [Content quality metrics](#monitor-with-cloudwatch-metrics-content-quality-metrics)
+ [Maintenance metrics](#monitor-with-cloudwatch-metrics-flow-health-maintenance)

## Flow metrics
<a name="monitor-with-cloudwatch-metrics-flow-health-flow"></a>

The following table lists network metrics that AWS Elemental MediaConnect sends to CloudWatch.


| Metric | Description | 
| --- | --- | 
| ARQRecovered | The number of dropped packets that were recovered by automatic repeat request (ARQ). This metric doesn't apply to flows that receive content from an entitlement or to flows that have multiple sources. For flows that have multiple sources, use the SourceARQRecovered metric to view data for each source.<br />Units: Count<br />Valid dimensions: +  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| ARQRequests | The number of retransmitted packets that were requested through automatic repeat request (ARQ) and received. This metric doesn't apply to flows that receive content from an entitlement or to flows that have multiple sources. For flows that have multiple sources, use the SourceARQRequests metric to view data for each source.<br />Units: Count<br />Valid dimensions: +  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| BitRate | The bitrate of the incoming (source) video.<br />Units: bits per second (bps)<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| Connected | The status of the source. A value of 1 indicates that the source is connected and a value of 0 (zero) indicates that the source is disconnected. This metric applies only to sources that use the Zixi, SRT, or RIST protocols.<br />Units: None<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
|  ConsecutiveDrops  | The number of data packets that were dropped in a row during transmission of data to or from MediaConnect.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
|  ConsecutiveNotRecovered  | The number of data packets that were not recovered in a row. After a data packet is dropped, error correction attempts to recover that packet. This metric helps to identify extended periods of data packets that were dropped and not recovered.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| Disconnections | The number of times that the source status changed from connected to disconnected.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| DroppedPackets | The number of packets that were lost during transit. This value is measured before any error correction takes place.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
|  FailoverSwitches  | The total number of times the flow switches back and forth between sources when using the * Failover* mode for source failover. <br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| FECPackets | The number of packets that were transmitted using forward error correction (FEC) and received. This metric applies only to flows that have one source that uses the RTP-FEC or Zixi protocols. It doesn't apply to flows that receive content from an entitlement or to flows that have multiple sources. For flows that have multiple sources, use the SourceFECPackets metric to view data for each source.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| FECRecovered | The number of packets that were transmitted using forward error correction (FEC), lost during transit, and recovered. This metric applies only to flows that have one source that uses the RTP-FEC or Zixi protocols. It doesn't apply to flows that receive content from an entitlement or to flows that have multiple sources. For flows that have multiple sources, use the SourceFECRecovered metric to view data for each source.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| MergeActive | The merge status of all sources on the flow. A value of 1 indicates that all sources are merged. A value of 0 (zero) indicates that at least one source is not actively merged with 2022-7. <br />Units: None<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| MergeLatency | The maximum value for SourceMergeLatency.<br />Units: Milliseconds<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| NotRecoveredPackets | The number of packets that were lost during transit and were not recovered by error correction.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| OverflowPackets | The number of packets that were lost in transit because the video required more buffer than was available. This metric doesn't apply to flows that receive content from an entitlement or to flows that have multiple sources.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| PacketLossPercent | The percentage of packets that were lost during transit, even if they were recovered.<br />Units: Percent<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| RecoveredPackets | The number of packets that were lost during transit, but recovered.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| RoundTripTime | The amount of time it takes for the source to send a signal and receive an acknowledgment from AWS Elemental MediaConnect. This metric doesn't apply to flows that receive content from an entitlement or to flows that have multiple sources. For flows that have multiple sources, use the SourceRoundTripTime metric to view data for each source.<br />Units: Milliseconds<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| TotalPackets | The total number of packets that were received.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 

## TR 101 290 Priority 1 metrics
<a name="monitor-with-cloudwatch-metrics-flow-health-p1"></a>

The following table lists TR 101 290 Priority 1 metrics that AWS Elemental MediaConnect sends to CloudWatch.


| Metric | Description | 
| --- | --- | 
| ContinuityCounter | The number of times that a continuity error occurred. This error indicates an incorrect packet order or lost packets.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| PATError | The number of times that a program association table (PAT) error occurred. This error indicates that the PAT is missing. The PAT lists the programs that are available in a transport stream (TS) and points to the program map tables (PMTs). The decoder needs the PAT to do its job.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| PIDError | The number of times that a packet identifier (PID) error occurred. This error indicates that a PID is missing its associated data stream. The PIDs are identifiers that provide the location of the video, audio, and data streams. This error can occur after the transport stream has been multiplexed and then remultiplexed.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| PMTError | The number of times that a program map table (PMT) error occurred. This error happens when the PMT is not received at least every 500 milliseconds (ms). Each PMT contains a list of PIDs, which help decoders reassemble data. The decoder needs the PMTs to do its job.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| TSByteError | The number of times that a transport stream byte error occurred. This error indicates that the sync byte did not appear after the prescribed number of bytes.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| TSSyncLoss | The number of times that a TS sync loss error occurred. This error happens after two or more consecutive TS byte errors.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 

## TR 101 290 Priority 2 metrics
<a name="monitor-with-cloudwatch-metrics-flow-health-p2"></a>

The following table lists TR 101 290 Priority 2 metrics that AWS Elemental MediaConnect sends to CloudWatch.


| Metric | Description | 
| --- | --- | 
| CATError | The number of times that a conditional access table (CAT) error occurred. This error indicates that the CAT is not present. The CAT tells the integrated receiver decoder (IRD) where to find management messages for the conditional access (CA) systems that are in use.<br />Units: Count<br />Valid dimensions: +  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| CRCError | The number of times that a cyclic redundancy check (CRC) error occurred. This error happens when a CRC determines that data is corrupted.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| PCRAccuracyError | The number of times that a program clock register (PCR) accuracy error occurred. This error happens when the value of the transmitted PCR differs from what is expected by more than 500 nanoseconds (ns). When a stream is encoded, the encoder assigns periodic PCR values of the encoder's program clock. The decoder relies on these values to ensure that the stream is kept in sync.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| PCRError | The number of times that a PCR error occurred. This error happens when PCR values are not sent frequently enough. The service relies on consistent, frequent PCRs to reset the local 27 MHz system clock. Although the error occurs when the interval exceeds 100 milliseconds (ms), best practices dictate that PCRs should be received at least every 40 ms. <br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| PTSError | The number of times that a presentation timestamp (PTS) error occurred. This error happens when a presentation timestamp (PTS) is not received at least every 700 ms. This can occur if the PTS is sent less frequently or not at all. The most common cause of this error is when the transport stream (TS) is scrambled.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| TransportError | The number of times that a primary transport error occurred. This error indicates that the TS packet is unusable. When this error occurs, ignore all other TR 101 290 errors for this packet.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 

## Content quality metrics
<a name="monitor-with-cloudwatch-metrics-content-quality-metrics"></a>

The following table lists the content quality metrics that AWS Elemental MediaConnect sends to CloudWatch.


| Metric | Description | 
| --- | --- | 
|  AudioStreamMissing  | Monitors instances when the expected audio stream is not detected in the content. A value of 1 indicates that the audio stream is missing from the source. <br />Units: None<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
|  BlackFramesBreaching  | Monitors instances when the duration of black frames in the video exceeds the specified threshold. A value of 1 indicates that the duration is breaching the specified threshold and a value of 0 (zero) indicates that the duration is not breaching the specified threshold. <br />Units: None<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
|  FrozenFramesBreaching  | Monitors instances when the video remains unchanged for longer than the specified threshold. A value of 1 indicates that the duration is breaching the specified threshold and a value of 0 (zero) indicates that the duration is not breaching the specified threshold. <br />Units: None<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
|  SilentAudioBreaching  | Monitors instances when the duration of silent audio exceeds the specified threshold. A value of 1 indicates that the duration is breaching the specified threshold and a value of 0 (zero) indicates that the duration is not breaching the specified threshold. <br />Units: None<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
|  TimecodePresent  | Indicates whether a valid timecode is present in the media stream. A value of 1 indicates that a valid timecode is present in the media stream and a value of 0 (zero) indicates that a valid timecode is not present in the media stream. <br />Units: None<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
|  VideoStreamMissing  | Monitors instances when the expected video stream is absent from the content. A value of 1 indicates that the video stream is missing from the source. <br />Units: None<br />Valid dimensions:+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 

## Maintenance metrics
<a name="monitor-with-cloudwatch-metrics-flow-health-maintenance"></a>

The following table lists flow maintenance metrics that AWS Elemental MediaConnect sends to CloudWatch.


| Metric | Description | 
| --- | --- | 
|  MaintenanceCanceled  | Maintenance for this flow is cancelled by MediaConnect. <br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  All flows  | 
|  MaintenanceFailed  | Maintenance did not complete successfully for this flow. <br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  All flows  | 
|  MaintenanceRescheduled  | MediaConnect is unable to perform maintenance at the previously scheduled date and time. A new date and time has been automatically assigned by MediaConnect for this flow's maintenance. <br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  All flows  | 
| MaintenanceScheduled | Maintenance is scheduled for the flow.<br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  All flows  | 
| MaintenanceStarted | Maintenance has started and is currently in progress for this flow. <br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  All flows  | 
| MaintenanceSucceeded | Maintenance completed successfully for this flow. <br />Units: Count<br />Valid dimensions:+  Flow ARN <br />+  All flows  | 