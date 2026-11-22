

# ADVSUS01-BP08 Identify and remove redundant data across advertising storage infrastructure

 Participants in the real-time advertising supply chain accrue large volumes of data, much of which serves no lasting purpose. Redundant creatives, expired logs, and superseded artifacts consume storage and the resources behind it long after their value ends. Retaining advertising data only as long as its purpose requires reduces the storage footprint and the energy and carbon associated with it. 

 **Desired outcome:** 
+  Advertising data lifecycle policies retain each data category only as long as its specific purpose requires. 
+  Duplicate ad files, expired creatives, and unused container images are automatically identified and removed. 
+  S3 Storage Lens provides visibility into unused and duplicated data across all advertising storage buckets. 

 **Common anti-patterns:** 
+  Bid event logs, impression logs, and expired creatives are retained indefinitely because no lifecycle policy distinguishes short-lived advertising data from data with a regulatory retention requirement. 
+  Multiple draft and test versions of the same ad creative are kept permanently even though they can be recreated from source assets. 
+  Real-time bidding container repositories accumulate years of superseded image versions because no expiry policy removes untagged or unpulled images. 
+  Unattached storage volumes and noncurrent object versions persist after campaigns end, consuming storage with no active purpose. 

 **Benefits of establishing this best practice:** 
+  Storage volume tracks the genuine retention needs of each advertising data category rather than growing without bound. 
+  Automated lifecycle and expiry rules remove redundant creatives, logs, and images without manual intervention. 
+  Removing unattached volumes and superseded container images reclaims storage that was consuming resources with no value. 
+  Storage Lens visibility exposes unused buckets and missing lifecycle rules before they accumulate into large redundant footprints. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising data is not uniform, and treating it as one undifferentiated pool is the root cause of unbounded storage growth. Classify advertising data by category. Each category has a distinct purpose, a distinct rate at which its value decays, and a distinct retention driver. Draft and test creatives can be recreated from source assets, so they need almost no retention. Bid event logs lose query value within days but may be subject to a short user-data retention obligation. Impression logs are often subject to a multi-year regulatory requirement. Historical campaign archives are kept for contractual reasons. This classification helps you create retention and deletion rules follow from the class and verify that your storage footprint tracks actual need. 

 Versioned object stores retain every superseded creative unless a noncurrent-version rule expires them. Container registries that serve real-time bidding fleets collect years of superseded image tags because no expiry policy removes the untagged or unpulled ones. Unattached block-storage volumes persist after campaigns end. None of these accumulations are visible by default, so use visibility tooling to detect them. Measure the sustainability gain through stored-byte volume and resource counts. 

 Automated expiry keeps redundant data from accumulating, but data that looks disposable can still be subject to a retention obligation or a post-campaign dispute. Take a snapshot before destructive deletion where contents may still be needed. Anchor every expiry rule to the documented retention driver for that data class. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure S3 lifecycle policies for all advertising data categories:** Transition bid event logs to S3 Intelligent-Tiering after 7 days as access frequency declines, and expire them after your retention period (typically 30–90 days for user-associated data). Transition impression logs to S3 Glacier Instant Retrieval after 30 days and to S3 Glacier Deep Archive after 90 days, expiring them after the applicable regulatory requirement (often 1–3 years). Move active campaign creative assets to S3 Intelligent-Tiering 30 days after campaign end, and historical campaign archives to S3 Glacier Flexible Retrieval after 6 months with expiry set by contract. Expire draft and test assets after 14 days. 

1.  **Enable DynamoDB TTL on all bid event and user profile tables:** Configure DynamoDB TTL attributes on bid event tables with expiration set to 30 days from write time. For user profile data, set TTL to 30–90 days from last activity, aligned with your data retention policy. TTL deletions incur no charge and don't consume write capacity. 

1.  **Implement ECR lifecycle policies for RTB container images:** Configure ECR lifecycle policies that delete untagged images immediately, retain only the number of tagged images your rollback policy actually requires, and delete images not pulled in the last 90 days regardless of tags. This helps avoid ECR accumulating years of superseded container image versions. 

1.  **Use S3 Storage Lens for storage optimization discovery:** Enable S3 Storage Lens across your advertising storage accounts. Review monthly reports for buckets with high noncurrent version counts (indicates missing lifecycle rules), buckets with incomplete multipart uploads (wasted storage from abandoned uploads), and prefixes with zero access in the last 30 days (candidates for archival or deletion). 

1.  **Audit orphaned EBS volumes quarterly:** Use [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) to identify EBS volumes with state "available" (not attached to any instance) for more than 7 days. Unattached EBS volumes incur both storage cost and resource consumption without providing value. 

1.  **Delete orphaned EBS volumes that serve no active purpose:** Review the volumes identified by the quarterly audit and delete those not serving an active purpose. Snapshot any volume whose contents may still be needed before deletion, so the data can be recovered if required. 

1.  **Remove obsolete ad file versions automatically:** Enable S3 versioning on buckets storing ad creative assets with noncurrent version lifecycle rules that expire previous versions after 30 days. Review S3 Storage Lens monthly for buckets with high noncurrent version counts. Evaluate how you are using data to remove use cases, dimensions, and ad creative versions that no longer provide value. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS01-BP06 Keep yield analytics off the auction path so its compute scales with events, not traffic](advsus01-bp06.md) 

 **Related documents:** 
+  [Setting an S3 Lifecycle configuration on a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html) 
+  [Amazon ECR lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) 

 **Related services:** 
+  [Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html) 
+  [Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) 
+  [Amazon DynamoDB TTL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) 
+  [Amazon ECR](https://aws.amazon.com/ecr/) 
+  [AWS Config](https://aws.amazon.com/config/) 