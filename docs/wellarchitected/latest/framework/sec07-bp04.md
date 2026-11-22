

# SEC07-BP04 Define scalable data lifecycle management

 Lifecycle management defines how data is handled when it arrives, how it is transformed, how long it is kept, and how it is destroyed. Tie these rules to your classification levels to keep protection appropriate as data ages and make retention and destruction deliberate. 

 **Desired outcome:** 
+  You classify data as close as possible to the point and time of ingestion. 
+  You apply masking, tokenization, or other sensitivity-reducing steps as close as possible to the point and time of ingestion when classification calls for them. 
+  You delete data in line with your policy once its classification no longer justifies keeping it. 

 **Common anti-patterns:** 
+  Teams apply one lifecycle approach to all data, ignoring differences in sensitivity and access requirements. 
+  Teams consider lifecycle for usable data or for backups, but not both. 
+  Teams assume data entering the workload is valid without establishing its value or provenance. 
+  Teams treat data durability as a substitute for backups and protection. 
+  Teams retain data beyond its usefulness and its required retention period. 

 **Benefits of establishing this best practice:** 
+  Regulatory adherence improves, because retention and destruction follow defined rules. 
+  Storage costs drop as data moves to cheaper tiers or is expired on schedule. 
+  Security improves, because backups are isolated and protected from the environment they came from. 
+  Investigations are faster, because you can trace where data came from and how it changed. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Your workload transforms data for business logic, reporting, analytics, or machine learning, and each form may carry a different sensitivity. Some data also loses value as it ages, which affects how you protect it and how long to keep it. Automate transitions where possible. [Amazon S3 lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) and [Amazon Data Lifecycle Manager](https://aws.amazon.com/ebs/data-lifecycle-manager/) handle retention, archiving, and expiration, and the [Time to Live](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) feature in Amazon DynamoDB expires items on a per-item timestamp. 

 Separate the data you use from the data you keep as a backup. These data types have different access patterns and threats, and treating them as one source can create risk if an event corrupts your live environment. [AWS Backup](https://aws.amazon.com/backup/) automates backups across services, and [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html) store volume copies with lifecycle and protection features. Immutability controls such as [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) and [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) prevent a backup from being altered or deleted, even by an administrator, so backups remain trustworthy after a ransomware event. Isolate backups in a separate account and apply separation of duties for access. 

 Lifecycle management also includes *data provenance tracking*, where you record where data came from, what transformations ran, who or what made them, and when. Use this history to verify a data set's origin and reconstruct events during an investigation. How you record it depends on your architecture. You might log transformation metadata in an [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) table, keep a copy of the data at each pipeline stage in a separate location, or store schema and timestamp information in an [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html). Match the level of provenance detail to your users' reporting needs. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Classify data and define lifecycle rules per level:** Analyze the data types, sensitivity levels, and access requirements in your workload, and define a lifecycle management strategy for each level. 

1.  **Implement retention and automated destruction:** Design retention policies and automated destruction that align with legal, regulatory, and organizational requirements, and apply them with automated lifecycle mechanisms. 

1.  **Separate and protect backups:** Distinguish live data from backups, automate backups across your services, isolate them in a separate account, and apply immutability controls so backups cannot be altered or deleted. 

1.  **Monitor and adjust as requirements change:** Establish continuous monitoring and auditing of your lifecycle controls, and adjust them as workload requirements and regulations evolve. Detect resources without automated lifecycle management enabled using [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/s3-lifecycle-policy-check.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC07-BP01 Understand your data classification scheme](sec07-bp01.md) 
+  [SEC07-BP02 Apply data protection controls based on data sensitivity](sec07-bp02.md) 
+  [COST03-BP03 Enforce data retention policies](cost03-bp03.md) 
+  [SUS04-BP01 Eliminate unnecessary data](sus04-bp01.md) 

 **Related documents:** 
+  [Data classification whitepaper](https://docs.aws.amazon.com/pdfs/whitepapers/latest/data-classification/data-classification.pdf) 
+  [AWS Blueprint for Ransomware Defense](https://d1.awsstatic.com/whitepapers/compliance/AWS-Blueprint-for-Ransomware-Defense.pdf) 
+  [DevOps Guidance: improve traceability with data provenance tracking](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dlm.8-improve-traceability-with-data-provenance-tracking.html) 

 **Related tools:** 
+  [AWS Backup](https://aws.amazon.com/backup/) 
+  [Amazon Data Lifecycle Manager](https://aws.amazon.com/ebs/data-lifecycle-manager/) 
+  [AWS IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) 