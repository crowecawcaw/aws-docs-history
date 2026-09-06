

# AWS Elemental MediaConnect metrics to monitor flow output health
<a name="monitor-with-cloudwatch-metrics-output-health"></a>

AWS Elemental MediaConnect sends metrics to CloudWatch. You can review specific metrics to evaluate the health of the output of your flow. 

**Topics**
+ [Output metrics for transport stream protocols](#monitor-with-cloudwatch-metrics-output-health-ts)
+ [Output metrics for NDI®](#monitor-with-cloudwatch-metrics-output-health-ndi)
+ [Output metrics for CDI protocols](#monitor-with-cloudwatch-metrics-output-health-cdi)
+ [Output metrics for router connections](#monitor-with-cloudwatch-metrics-output-health-router)

## Output metrics for transport stream protocols
<a name="monitor-with-cloudwatch-metrics-output-health-ts"></a>


| Metric | Description | 
| --- | --- | 
| ConnectedOutputs | The number of outputs that are currently connected. <br />This metric applies to outputs that use the Zixi or SRT protocol. <br />Units: Count<br />Valid dimensions: +  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| OutputARQRequests | The number of retransmitted packets that were requested through automatic repeat request (ARQ) and received. <br />This metric applies to outputs that use the SRT protocol or output to MediaLive.<br />Units: Count<br />Valid dimensions:+   Output ARN  <br />+   Flow ARN  <br />+   Availability Zone  <br />+   All flows   | 
| OutputBitrate | The bitrate of the outgoing (output) video. <br />This metric applies to outputs that use the SRT protocols or output to MediaLive.<br />Units: bits per second (bps)<br />Valid dimensions:+   Output ARN  <br />+   Flow ARN  <br />+   Availability Zone  <br />+   All flows   Both MediaConnect and the Zixi protocol use bandwidth optimization techniques that can affect bitrate measurements:   In flows with Zixi outputs, Zixi often optimizes network usage by substituting repetitive content packets with null packets.   For entitlements, MediaConnect performs similar optimization between the content originator's flow and the subscriber's flow.   <br />For example, in a 30 Mbps stream with repetitive content (like a black slate), either optimization might reduce the bitrate to 5 Mbps. These bitrate fluctuations are normal and don't affect content quality, but they might be noticeable in your bitrate monitoring. <br />Additionally, the `OutputBitrate` value can vary depending on the selected protocol due to non-payload packets, retransmitted packets, packet headers, and other protocol-specific packets. Due to these factors, the bitrate value reported by this metric might vary between outputs.  | 
| OutputConnected | The status of the output. A value of 1 indicates that the output is connected, and a value of 0 (zero) indicates that the output is disconnected. <br />This metric applies to outputs that use the Zixi or SRT protocol.<br />Units: None<br />Valid dimensions:+  Output ARN <br />+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| OutputDisconnections | The number of times that the output status changed from connected to disconnected. <br />This metric applies to outputs that use the Zixi or SRT protocol.<br />Units: Count<br />Valid dimensions:+  Output ARN <br />+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| OutputNotRecoveredPackets | The number of packets that were lost during transit and were not recovered by error correction. <br />This metric applies to outputs to MediaLive.<br />Units: Count<br />Valid dimensions:+   Output ARN  <br />+   Flow ARN  <br />+   Availability Zone  <br />+   All flows   | 
| OutputResentPackets | The number of packets that were retransmitted to the output destination. <br />This metric applies to outputs that use the SRT protocol or output to MediaLive.<br />Units: Count<br />Valid dimensions:+   Output ARN  <br />+   Flow ARN  <br />+   Availability Zone  <br />+   All flows   | 
| OutputRoundTripTime | The amount of time it takes for the output to send a signal and receive an acknowledgment from the output destination. <br />This metric applies to outputs that use the SRT protocol or output to MediaLive.<br />Units: Milliseconds<br />Valid dimensions:+   Output ARN  <br />+   Flow ARN  <br />+   Availability Zone  <br />+   All flows   | 
| OutputTotalPackets | The total number of packets that were sent to the output. <br />This metric applies to outputs that use the SRT protocols or output to MediaLive.<br />Units: Count<br />Valid dimensions:+  Output ARN <br />+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 

## Output metrics for NDI®
<a name="monitor-with-cloudwatch-metrics-output-health-ndi"></a>


| Metric | Description | 
| --- | --- | 
|  OutputConnectedReceivers  | The number of NDI receivers that are connected to the flow output.<br />This metric applies to NDI outputs only.<br />Valid dimensions:+  Output ARN <br />+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
|  OutputGeneratedAudioSamples  | The number of audio samples that are sent to each individual NDI receiver.<br />This metric applies to NDI outputs only. <br />This metric is published even if no receivers are currently connected. If multiple receivers are connected, keep in mind this value represents the number sent to each receiver, not the total across all receivers. The value is not multiplied based on the number of receivers.<br />Valid dimensions:+  Output ARN <br />+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
|  OutputGeneratedVideoFrames  | The number of video frames that are sent to each individual NDI receiver.<br />This metric applies to NDI outputs only. <br />This metric is published even if no receivers are currently connected. If multiple receivers are connected, keep in mind this value represents the number sent to each receiver, not the total across all receivers. The value is not multiplied based on the number of receivers.<br />Valid dimensions:+  Output ARN <br />+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 

## Output metrics for CDI protocols
<a name="monitor-with-cloudwatch-metrics-output-health-cdi"></a>


| Metric | Description | 
| --- | --- | 
| OutputDroppedPayloads | Payloads that were lost during transit from MediaConnect to the output. A payload is a frame of video or an audio sample. Payloads can consist of multiple packets. Payload metrics are only applicable when using CDI. <br />Units: Count<br />Valid dimensions:+  Output ARN <br />+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| OutputLatePayloads | Packets of a payload that arrive at the output outside of MediaConnect's internal buffer. A payload is a frame of video or an audio sample. Payloads can consist of multiple packets. Payload metrics are only applicable when using CDI. <br />Units: Count<br />Valid dimensions:+  Output ARN <br />+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| OutputTotalBytes | Total amount of bytes transferred from MediaConnect to the output. <br />This metric is only applicable when using CDI.<br />Units: Bytes<br />Valid dimensions:+  Output ARN <br />+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| OutputTotalPayloads | Total amount of payloads delivered from MediaConnect to the output. A payload is a frame of video or an audio sample. Payloads can consist of multiple packets. Payload metrics are only applicable when using CDI. <br />Units: Count<br />Valid dimensions:+  Output ARN <br />+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 

## Output metrics for router connections
<a name="monitor-with-cloudwatch-metrics-output-health-router"></a>

The following table lists source metrics that MediaConnect sends to CloudWatch when a flow output sends content to a router input. 


| Metric | Description | 
| --- | --- | 
| OutputEnabled | The status of the output. A value of 1 indicates that the output is enabled, and a value of 0 (zero) indicates that the output is disabled.<br />Units: None<br />Valid dimensions:+  Output ARN <br />+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 
| OutputBitrate | The bitrate of the outgoing (output) video.<br />Units: bits per second (bps)<br />Valid dimensions:+  Output ARN <br />+  Flow ARN <br />+  Availability Zone <br />+  All flows  | 