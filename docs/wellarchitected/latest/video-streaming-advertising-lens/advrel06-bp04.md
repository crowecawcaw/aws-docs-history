

# ADVREL06-BP04 Implement automated input failover and slate injection for continuous channel playout

 A FAST channel relies on an ongoing stream of scheduled content assets. If the current asset becomes unavailable, the channel must automatically switch to backup content without viewer-visible disruption. 

 **Desired outcome:** 
+  MediaLive automatic input failover detects input loss within the configured threshold (3 seconds in this design) and switches to a secondary input source. 
+  Slate content from a dedicated pool fills scheduling gaps without manual intervention. 
+  Pre-flight validation alerts operations teams 30 minutes before potential gaps. 

 **Common anti-patterns:** 
+  Single input source with no failover, so origin failure causes channel blackout 
+  No slate content pool, so scheduling gaps result in frozen frames or black screens 
+  Manual intervention required to recover from content availability issues 
+  No pre-flight validation, so asset unavailability is discovered only at playout time 

 **Benefits of establishing this best practice:** 
+  Automated failover with pre-flight validation supports ongoing channel playout. 
+  Viewers experience uninterrupted programming continuity even during origin failures, with slate content filling any gaps transparently. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Every viewer watches the same stream at the same moment, so an interruption reaches all of them together. On-demand streaming hides brief faults inside the client buffer. Continuous playout has no such margin, so a lost input becomes a visible glitch in seconds. Human operators can't react that fast, so recovery must happen automatically. 

 This design uses a 3-second failover threshold to balance false failovers caused by transient jitter against the delay of switching after a real input loss. Primary and secondary inputs run in separate Availability Zones to reduce the impact of an Availability Zone failure. 

 Backup content contains an assumption that the backup is available and playable when required. A slate pool that is missing or corrupt fails at playout time, producing a black screen worse than the fault it was meant to cover. Channel assembly inserts slate into the schedule when no live input is available, so stale or missing content becomes visible immediately. 

 Programming or operations teams curate genre-appropriate filler and decide what viewers see during a gap. Engineering owns the failover mechanics and the validation timing. A pre-flight check runs ahead of playout to catch missing assets early. It leaves enough time for a person or an automated job to fix the gap before viewers see it. Apply the same at the channel level and keep a warm standby ready to take over. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure MediaLive with automatic input failover:** Set up primary and secondary inputs from independent S3 origins or MediaPackage endpoints in different Availability Zones. Set failover threshold to 3000 ms. Test failover by simulating primary input failure and confirming secondary activates within threshold. 

1.  **Maintain a slate content pool with pre-transcoded content:** Create an S3 bucket with 4–8 hours of genre-appropriate filler content, pre-transcoded to all output renditions. Enable cross-region replication. Configure MediaTailor channel assembly to use slate pool content when scheduled assets are unavailable. 

1.  **Implement pre-flight validation Lambda:** Deploy a Lambda function triggered every 15 minutes that validates each scheduled asset's availability for the next 30 minutes. On failure, send SNS notification to operations team and pre-warm the slate fallback. This provides a 30-minute window for manual or automated remediation before viewers are affected. 

1.  **Deploy N\+1 redundancy for active channels:** Maintain a warm standby channel configuration activatable within 60 seconds for each active FAST channel. Test activation quarterly. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL04-BP04 Design your workloads to withstand failures of individual components](advrel04-bp04.md) 
+  [ADVREL04-BP01 Create disaster recovery (DR) runbooks, and regularly test documented backup and restoration processes](advrel04-bp01.md) 

 **Related documents:** 
+  [Automatic input failover in MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/automatic-input-failover.html) 
+  [Build FAST Channel using AWS Elemental MediaLive](https://catalog.us-east-1.prod.workshops.aws/workshops/0e4fc3a0-1e5c-4c76-af24-50489345090b/en-US) 

 **Related services:** 
+  [AWS Elemental MediaLive](https://aws.amazon.com/medialive/) 
+  [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 