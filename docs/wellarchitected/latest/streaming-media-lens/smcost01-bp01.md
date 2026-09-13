

# SMCOST01-BP01 Implement lifecycle management for media assets
<a name="smcost01-bp01"></a>

Media assets can reach hundreds of gigabytes per file. Without active lifecycle management, storage costs grow linearly with content volume regardless of whether assets are still accessed. Organizations that produce or acquire content continuously accumulate source, mezzanine, and distribution files that remain in high-cost storage tiers long after their access frequency drops to near zero.

**Desired outcome:**
+ You have automated lifecycle policies that transition media assets to progressively lower-cost storage tiers as access frequency declines.
+ You have separate storage strategies for deterministic access patterns (known content lifecycles) and non-deterministic patterns (back-catalog, user-generated content).
+ You have monitoring that validates lifecycle policy effectiveness and alerts when access patterns shift.

**Common anti-patterns:**
+ Storing all media assets in a single storage class regardless of access frequency, paying premium storage rates for content that is rarely or never accessed.
+ Applying uniform retention policies across all content types without considering differences in access patterns between source files, distribution copies, and temporary processing artifacts.
+ Manually managing storage tier transitions instead of automating lifecycle policies, leading to forgotten assets accumulating in high-cost tiers.
+ Retaining intermediate processing files (chunks, temporary transcodes) after workflow completion without expiration rules.

**Benefits of establishing this best practice:**
+ Storage costs decrease as content ages because assets move automatically to tiers that match their actual access frequency.
+ Operational burden drops because lifecycle rules execute without human intervention or content-by-content decision-making.
+ Content remains accessible when needed because tiering decisions are based on measured access patterns rather than blanket deletion policies.
+ Cost growth becomes predictable because new content follows the same automated lifecycle path as existing content.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Streaming media workloads maintain distinct asset categories with fundamentally different access characteristics. Source and mezzanine files experience intensive reads during processing and then near-zero access afterward. Distribution-format assets follow viewer demand curves where access peaks at launch and declines over weeks or months. Processing artifacts (split segments, temporary transcodes, thumbnails-in-progress) have no value after the workflow completes.

These categories require different lifecycle strategies. Source files that have been successfully transcoded often only need to be retained for re-processing or compliance. A single re-encode request months later doesn't justify keeping terabytes in high-performance storage. The retrieval time you can tolerate for re-processing (minutes, hours, or half a day) determines which archival class is appropriate. Organizations that conflate "we might need this again" with "we need this immediately" overpay by an order of magnitude.

Separating ingest and origination into different buckets creates a clean boundary for lifecycle policy application. Ingest buckets hold source material where aggressive tiering is appropriate. Origination buckets hold distribution content where tiering tracks viewer demand. This separation also stops unintentional reads of source assets by player clients, which would reset access counters and defeat intelligent tiering.

For content with unpredictable access patterns, choosing the right storage class upfront is guesswork. A title in a large back-catalog might receive zero views for months and then spike because of a recommendation algorithm change or a cultural moment. Retrieval fees from archival classes in that scenario would exceed the savings. Automatic access-frequency monitoring that moves objects between tiers without retrieval penalties solves this problem without requiring you to predict viewer behavior.

Lifecycle policies are not set-and-forget. Content access patterns shift as viewer behavior evolves, recommendation systems change, and business priorities shift. A quarterly review of storage class distribution against actual access metrics reveals whether policies are still aligned with reality or whether thresholds need adjustment.

### Implementation steps
<a name="implementation-steps"></a>

1. **Categorize assets and establish separate storage boundaries:** Create distinct buckets for ingest (source and mezzanine files) and origination (distribution-format assets). Apply restrictive access policies on ingest buckets so that only processing workflows read from them, stopping accidental access that would skew analytics.

1. **Analyze existing access patterns with storage class analysis:** Enable [Amazon S3 Analytics Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/userguide/analytics-storage-class.html) on your buckets. Allow 30 days of data collection before making tiering decisions. Use the results to identify the age at which access frequency drops below the transition threshold for each asset category.

1. **Configure lifecycle rules for deterministic access patterns:** Create [S3 Lifecycle Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) that transition source and mezzanine files to S3 Glacier Flexible Retrieval or S3 Glacier Instant Retrieval after processing confirmation. Add expiration rules for intermediate processing artifacts. Transition distribution assets from S3 Standard to S3 Standard-IA based on the access-frequency data from your analytics.

1. **Enable intelligent tiering for non-deterministic access patterns:** Configure [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) for content where access patterns are unpredictable (user-generated content, large back-catalogs, event recordings). Enable the optional Archive Access tier (90 days) and Deep Archive Access tier (180 days) for additional savings on content that may go dormant.

1. **Validate processing completion before archival transitions:** Integrate lifecycle transitions with your processing workflow state. Don't transition source files to archival storage until the workflow confirms successful output. Use object tagging (for example, `processing-status: complete`) as a lifecycle rule condition to stop archiving assets that failed processing and may need re-ingest.

1. **Monitor lifecycle effectiveness and adjust:** Create [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) dashboards showing storage class distribution over time. Use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) reports filtered by S3 storage class to track savings. Set alerts for unexpected storage growth in high-cost tiers. Review lifecycle policies quarterly against current access analytics.

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMCOST01-BP02 Optimize content delivery using edge caching and packaging](smcost01-bp02.html)

**Related documents**
+ [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
+ [Amazon S3 Analytics Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/userguide/analytics-storage-class.html)
+ [S3 Intelligent-Tiering storage class](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html)

**Related examples**
+ [Video on Demand on AWS](https://aws.amazon.com/solutions/implementations/video-on-demand-on-aws/)

**Related services**
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
+ [Amazon S3 Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+ [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)