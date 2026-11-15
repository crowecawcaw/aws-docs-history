

# ADVSEC02-BP02 Protect linear distribution feeds and ad signaling in converged delivery
<a name="advsec02-bp02"></a>

 When linear broadcast workflows converge with cloud-based ad insertion, SCTE-35 markers move from physically secured facilities to IP contribution links and programmable control planes. Without transport and control-plane integrity, unauthorized parties can insert or suppress ad breaks and affect monetization. 

 **Desired outcome:** 
+  You have secured contribution feeds from broadcast encoders to cloud media services with encrypted transport and source restrictions. 
+  Only authorized services and operators can create or change SCTE-35 schedule actions, and packaging origins can't be reached through unapproved paths. 
+  You can correlate anomalous marker timing, duration, or frequency with the control-plane action that caused it. 

 **Common anti-patterns:** 
+  Accepting unencrypted MPEG-TS ingest from broadcast encoders without validating the source, so a network-adjacent system can inject SCTE-35 markers. 
+  Granting broad access to scheduling APIs, which lets a valid identity create ad breaks outside its operational responsibility. 
+  Monitoring marker syntax without comparing markers with approved event schedules, which treats a valid but unauthorized signal as legitimate. 

 **Benefits of establishing this best practice:** 
+  Reduces the risk of revenue manipulation through unauthorized ad-break insertion or suppression in premium linear content. 
+  Preserves the integrity of contribution feeds and ad signaling as they cross organizational and network boundaries. 
+  Produces evidence that distinguishes encoder faults, scheduling errors, and unauthorized control-plane activity. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Converged delivery moves SCTE-35 markers from a closed broadcast chain into a system with external contribution links and programmable control planes. A permitted schedule action can create an unauthorized break even when the contribution feed is encrypted. Treat source transport and marker authoring as separate trust boundaries. 

 Contribution protocol selection depends on latency, loss recovery, and deployed encoder support. Secure Reliable Transport (SRT) combines encryption with retransmission for lossy networks. Reliable Internet Stream Transport (RIST) can provide similar contribution resilience in compatible environments. Older encoders might require RTMP over TLS during migration. The weakest active path determines residual risk, so assign an owner and retirement date to any temporary legacy route. 

 Marker integrity also depends on authority and context. A valid SCTE-35 message can still be harmful when it comes from the wrong schedule API caller or appears outside an approved avail. Compare markers with the event schedule and expected cadence to help separate malformed input from misuse of a legitimate control plane. 

 Protect packaging and origin endpoints from direct access that bypasses the approved delivery tier. This boundary limits unauthorized retrieval and unmonitored manifest requests, but it doesn't validate which creative a VAST response selects. Creative-origin validation, pre-stitch hash checks, and viewer-session authentication belong to the creative-delivery integrity control. 

 Monitoring needs evidence from both paths. Media metrics reveal unexpected break timing or duration, while control-plane audit records identify who changed schedule state. Correlate the two to distinguish encoder faults, schedule mistakes, and deliberate manipulation. Keep the event calendar and approved marker policy with the evidence so responders can evaluate an anomaly without reconstructing business context during an incident. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Secure contribution ingest:** Configure AWS Elemental MediaLive inputs to accept an encrypted protocol supported by the source encoder, such as SRT or RTMP over TLS. Restrict each input to approved source addresses and record an owner and retirement date for any legacy path. 

1.  **Constrain marker authoring:** Limit MediaLive schedule-action permissions to the services and operators that create approved ad avails. Separate routine scheduling from emergency access, and record every schedule API call in AWS CloudTrail. 

1.  **Protect packaging and manifest origins:** Restrict AWS Elemental MediaPackage and AWS Elemental MediaTailor origins to the approved delivery tier. Block direct paths that bypass the distribution and authorization controls used by the workload. 

1.  **Monitor ad-signal integrity:** Publish metrics for SCTE-35 cadence, break duration, and schedule alignment. Alert on markers outside approved avails, unexpected frequency changes, or control-plane actions that don't match the event calendar. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC02-BP01 Encrypt DSP to SSP communication in transit using TLS](advsec02-bp01.md) 
+  [ADVSEC04-BP04 Secure ad creative delivery and content integrity across converged channels](advsec04-bp04.md) 

 **Related documents:** 
+  [Secure Media Delivery at the Edge on AWS](https://aws.amazon.com/solutions/guidance/secure-media-delivery-at-the-edge-on-aws/) 
+  [MediaLive SCTE-35 passthrough](https://docs.aws.amazon.com/medialive/latest/ug/scte-35-passthrough-or-removal.html) 
+  [MediaPackage SCTE-35 message options](https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html) 
+  [MediaTailor SSAI with CDN workflow](https://docs.aws.amazon.com/mediatailor/latest/ug/ssai-cdn-workflow.html) 

 **Related services:** 
+  [AWS Elemental MediaLive](https://aws.amazon.com/medialive/) 
+  [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/) 
+  [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 