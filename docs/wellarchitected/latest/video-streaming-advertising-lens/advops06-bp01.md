

# ADVOPS06-BP01 Establish continual linear streaming operational readiness

 FAST channels operate continuously without natural maintenance windows. Any playout interruption affects viewer experience and ad revenue with no opportunity to defer recovery. Before a FAST channel begins serving viewers, validate its operational readiness, including multi-AZ failover testing and EPG completeness validation. 

 **Desired outcome:** 
+  FAST channel infrastructure is validated for continual operations with verified monitoring, failover procedures, and capacity planning before channel launch. 
+  Multi-AZ MediaLive failover and Multi-Region failover routing are pre-configured and tested before any viewer traffic is accepted. 
+  EPG completeness validation covers all upcoming time slots with confirmed content availability and correct asset specifications. 

 **Common anti-patterns:** 
+  Launching FAST channels without validating multi-AZ or Multi-Region failover procedures. 
+  Assuming that content origin availability guarantees playout continuity without testing CDN routing under failure conditions. 
+  Not fully testing failover procedures before channel launch, discovering that failover takes 8 minutes instead of 30 seconds for the first time during an actual Availability Zone failure. 
+  Lacking EPG completeness validation. 

 **Benefits of establishing this best practice:** 
+  Validated continual operational readiness reduces unplanned playout interruptions. 
+  Pre-tested failover procedures enable rapid recovery from regional degradation. 
+  Confirmed capacity planning reduces the risk of resource exhaustion during peak viewing periods. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A FAST channel failure creates a blackout that all concurrent viewers see at once. Pre-launch operational readiness is a critical task for reducing the sizeable cost of discovering a problem in production. 

 AWS Elemental MediaLive supports automatic input failover configured at the channel level. MediaLive switches to the secondary source when the primary (S3 bucket, MediaPackage origin, or other source) becomes unavailable and input loss exceeds the configured input-loss threshold. Place the primary and secondary inputs in separate Availability Zones. The secondary must replicate content independently. Test the failover configuration before launch. 

 Use Multi-Region failover for FAST channels with large audiences where single-region availability doesn't meet business requirements. The failover path requires: cross-region content origin replication (S3 Cross-Region Replication), CloudFront origin failover groups (primary and failover origins in different regions), and pre-configured DNS routing that can activate the secondary region within seconds. 

 Use EPG completeness validation to catch the most common FAST channel failures before launch: schedule gaps, missing assets, and duration mismatches. A validation Lambda function running 60 minutes before each scheduling window verifies all three conditions and triggers a notification, giving content operations time to address issues before viewers see them. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Validate MediaLive channel redundancy and test multi-AZ automatic input failover:** Confirm that your MediaLive channels are configured with automatic input failover using two input sources in separate Availability Zones. Test the failover by simulating primary input loss and confirming that failover completes within the configured input-loss threshold (for example, 3000 ms) and that viewers experience less than 10 seconds of disruption. Document the measured failover time and add it to the channel's operational runbook. 

1.  **Conduct capacity planning analysis at 150% of expected peak concurrent viewer load:** Before launch, run capacity analysis to confirm that MediaLive, MediaPackage, and the CDN configuration can sustain 150% of expected peak concurrent viewer load without resource contention. Use CloudWatch metrics from similar channel launches as capacity planning benchmarks. For live event FAST channels (sports, news), model the traffic spike pattern rather than steady-state load. 

1.  **Implement automated EPG completeness validation 60 minutes before scheduled playout:** Deploy a Lambda function triggered by EventBridge on a 15-minute schedule. The function checks all EPG entries in the upcoming 60-minute window: (1) asset ID exists in the content origin, (2) asset duration matches scheduled slot duration within a 5-second tolerance, (3) all required renditions (resolution, bit rate, codec) are available, (4) no scheduling gaps exist between program entries. Route validation failures to an SNS topic that notifies content operations through email and Slack. 

1.  **Test content origin replication and CDN routing under simulated primary failure:** Before launch, simulate a primary region content origin failure by blocking access to the primary S3 bucket and verifying that CloudFront origin failover activates correctly. Measure the time from primary origin failure to full CDN traffic on the secondary origin. Confirm that content availability and ad break delivery are maintained through the failover. Document the measured failover time and compare against the channel uptime SLO. 

1.  **Create and execute a channel launch readiness checklist with required sign-offs:** Define a standardized readiness checklist covering: monitoring dashboards configured (all KPIs green), automatic input failover tested and documented, EPG validation running and passing, slate content configured and accessible, content availability validated for first 24 hours of schedule, load testing completed at 150% of expected peak, rollback procedure documented and tested. Require sign-off from the designated readiness owner before activating the channel. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS06-BP02 Implement observability for scheduling, ad fill, and playout health](advops06-bp02.md) 

 **Related documents:** 
+  [Automatic input failover in MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/automatic-input-failover.html) 
+  [Deploying virtual linear OTT channels using AWS Media Services](https://aws.amazon.com/blogs/media/deploying-virtual-linear-ott-channels-using-aws-media-services/) 

 **Related services:** 
+  [AWS Elemental MediaLive](https://aws.amazon.com/medialive/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 