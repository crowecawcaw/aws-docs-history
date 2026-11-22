

# ADVREL06-BP03 Design player-side resilience for SGAI manifest and ad stream retrieval

 In SGAI, the player fetches personalized ad streams after receiving the manifest with SCTE-35 markers. If the player can't retrieve the ad stream, the ad break fails. 

 **Desired outcome:** 
+  Players handle ad stream fetch failures gracefully with retry logic, partial pod delivery, and CDN failover. 
+  Dual SCTE-35 signaling (manifest and transport stream) provides redundancy against signaling corruption. 
+  Server-side telemetry detects player-side ad insertion errors in real time. 

 **Common anti-patterns:** 
+  No player-side retry logic: a single transient CDN error causes the entire ad break to fail. 
+  Failing the entire ad pod when one of multiple planned ads can't load. 
+  Single SCTE-35 signaling path: corruption in either manifest or transport stream removes ad break detection. 
+  No server-side visibility into player-side ad insertion errors: failures go undetected. 

 **Benefits of establishing this best practice:** 
+  Player-side resilience helps ad breaks succeed even during transient CDN issues. 
+  Dual SCTE-35 signaling provides redundancy against signaling corruption. 
+  Real-time error telemetry enables rapid detection and resolution of device-specific failures. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Unlike server-side ad insertion, where a single origin stitches content, SGAI distributes stitching to a fleet of devices. The fleet includes smart TVs, set-top boxes, mobile apps, and browser players. Each device has different network stacks, timeout behaviors, and retry implementations. The ad decision infrastructure logs the manifest delivery, but the viewer sees dead air because the device could not fetch the creative in time. 

 The timing budget for player-side recovery is the ad break duration itself. Every retry attempt, DNS resolution, and TLS handshake consumes seconds from a fixed window. If the total fetch-and-retry cycle exceeds the break length, the player must either cut into content or abandon the break. During popular live events, millions of players simultaneously hit the same SCTE-35 splice point. Uncoordinated retries create a thundering-herd amplification that can convert a transient CDN error into a sustained outage. 

 Partial-fill delivery preserves revenue from the ads that loaded when one creative in a multi-slot pod fails. Slate avoids the encoding-profile mismatch that a fresh mid-break creative can cause. Dual signaling paths for break detection add redundancy. If CDN processing strips or corrupts the manifest-level markers, transport-stream splice information still triggers break detection. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement player-side retry with jitter:** Configure maximum 2 retries with 500 ms timeout per attempt. Total ad fetch budget: SCTE-35 signaled break duration minus 1 second. Add randomized jitter (0–200 ms) to retry timing to avoid thundering herd on shared CDN origins. 

1.  **Configure player partial pod delivery:** When any ad in a pod fails to load after retry, deliver successfully loaded ads and fill the remaining break time with slate. Don't abandon the entire break because of one failed ad. 

1.  **Implement player-side CDN failover:** Configure primary and secondary CDN origins for ad creative delivery. On HTTP 5xx or timeout, retry against the secondary CDN origin within the retry window. 

1.  **Stream player-side errors to Kinesis for real-time monitoring:** Collect player-side ad insertion error events and stream them to Kinesis Data Streams. Use Amazon Managed Service for Apache Flink to compute rolling error rates per content title. Alert when ad break failure rate exceeds 10% over a 15-minute window. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL04-BP02 Architect defensively against failures](advrel04-bp02.md) 
+  [ADVREL01-BP04 Implement chaos engineering practices](advrel01-bp04.md) 

 **Related documents:** 
+  [SGAI live configuration in MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/sgai-live-configuration.html) 

 **Related services:** 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) 
+  [Amazon Managed Service for Apache Flink](https://aws.amazon.com/managed-service-apache-flink/) 