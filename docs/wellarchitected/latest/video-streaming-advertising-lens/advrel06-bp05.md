

# ADVREL06-BP05 Design redundant content origin architecture with cross-region replication

 In a single-origin FAST channel architecture, a storage failure, regional impairment, or network issue causes a complete channel blackout. Replicate content origins across Regions with automatic failover at the CDN layer. 

 **Desired outcome:** 
+  Content origins are replicated across regions with CloudFront origin failover so that an origin failure in the primary region is transparent to viewers. 
+  S3 versioning and Object Lock protect against accidental deletion during active playout. 
+  Origin health is monitored continuously with CloudFront and S3 metrics. 

 **Common anti-patterns:** 
+  Single-Region content origin with no replication, so regional impairment causes total blackout. 
+  No CDN-level origin failover, so origin failure requires manual DNS or configuration changes. 
+  No protection against accidental content deletion or corruption during active playout. 
+  No monitoring of origin health, so failures are detected only when viewers report blackouts. 

 **Benefits of establishing this best practice:** 
+  Redundant origins with CDN failover provide uninterrupted content delivery even during regional impairments. 
+  S3 versioning and Object Lock protect against operational errors that could disrupt live channels. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 An origin is the source of truth for every segment a channel plays, and FAST playout pulls those segments continuously with little advance buffering. On-demand players buffer well ahead and absorb a brief origin fault. A live channel has almost no margin, so an unresponsive origin becomes visible within seconds. In this scenario, origin availability becomes a threshold for how reliable a channel can be. 

 Cross-Region replication protects pre-staged content by copying objects to a second region before they are needed. Freshly ingested content is the exception. A live-to-VOD segment written moments ago might not have replicated yet, and a failover at that instant finds the secondary origin incomplete. Replication lag is the gap between writing an object and having a safe copy. Static origins suit content staged in advance. Live sources that need transcoding fit a redundant ingest path instead of a static bucket. 

 An operator can remove or overwrite an object that is still on air, and the channel then requests a segment that no longer exists. Object Lock in governance mode blocks that action for content in active use. Retention windows must outlast the scheduled use of each asset, because a lock that expires mid-playout offers no protection. 

 The secondary region choice belongs with the teams that own DR and data residency. Content operations owns deletion discipline and must know which objects are locked and why. Watch origin health at the edge and at the source. A rising error rate at either layer is the earliest warning that failover might be near. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable S3 Cross-Region Replication:** Configure S3 CRR from the primary content origin bucket to a secondary region bucket. Set replication rule to replicate all objects and optionally replicate delete markers. Monitor replication lag using S3 Replication Time Control (RTC) so that objects are replicated within 15 minutes. 

1.  **Configure CloudFront origin failover groups:** Create a CloudFront origin group with the primary S3 bucket as the default origin and the replicated bucket as the failover origin. Configure failover criteria: HTTP 5xx errors and HTTP 403 errors trigger failover. Test origin failover by blocking primary bucket access and verifying CloudFront automatically serves from secondary. 

1.  **Enable S3 Object Lock for active content:** Configure Object Lock in governance mode on the current week's scheduled content. This guards against accidental deletion or modification during active playout. Set retention period to 7 days beyond scheduled end of use. 

1.  **Monitor origin health with CloudWatch alarms:** Configure CloudWatch alarms on S3 4xxErrors and 5xxErrors request metrics and CloudFront OriginLatency. Alert when origin error rate exceeds 1% sustained over 5 minutes. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL03-BP02 Choose AWS Regions that meet your legal and disaster recovery requirements](advrel03-bp02.md) 
+  [ADVREL04-BP05 Back up data in multiple locations with consideration for regulatory requirements](advrel04-bp05.md) 

 **Related documents:** 
+  [Optimize high availability with CloudFront origin failover](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html) 

 **Related services:** 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/) 