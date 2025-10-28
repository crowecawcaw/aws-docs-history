# SEC07-BP04 Define scalable data lifecycle management

Understand your data lifecycle requirements as they relate to your
different levels of data classification and handling.  This can
include how data is handled when it first enters your environment,
how data is transformed, and the rules for its destruction. Consider
factors such as retention periods, access, auditing, and tracking
provenance.

**Desired outcome:** You classify
data as close as possible to the point and time of ingestion. When
data classification requires masking, tokenization, or other
processes that reduce sensitivity level, you perform these actions
as close as possible to point and time of ingestion.

You delete data in accordance with your policy when it is no longer
appropriate to keep, based on its classification.

**Common anti-patterns:**

- Implementing a one-size-fits-all approach to data lifecycle
  management, without considering varying sensitivity levels and
  access requirements.
- Considering lifecycle management only from the perspective of
  either data that is usable, or data that is backed up, but not
  both.
- Assuming that data that has entered your workload is valid,
  without establishing its value or provenance.
- Relying on data durability as a substitute for data backups and
  protection.
- Retaining data beyond its usefulness and required retention
  period.

**Benefits of establishing this best
practice:** A well-defined and scalable data lifecycle
management strategy helps maintain regulatory compliance, improves
data security, optimizes storage costs, and enables efficient data
access and sharing while maintaining appropriate controls.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data within a workload is often dynamic.  The form it takes when
entering your workload environment can be different from when it
is stored or used in business logic, reporting, analytics, or
machine learning.  In addition, the value of data can change over
time. Some data is temporal in nature and loses value as it gets
older.  Consider how these changes to your data impact evaluation
under your data classification scheme and associated controls.
 Where possible, use an automated lifecycle mechanism, such as
[Amazon S3 lifecycle policies](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") and the
[Amazon Data Lifecycle Manager](https://aws.amazon.com/ebs/data-lifecycle-manager/ "https://aws.amazon.com/ebs/data-lifecycle-manager/"), to configure your data retention,
archiving, and expiration processes. For data stored in DynamoDB,
you can use the
[Time
To Live (TTL)](../../../amazondynamodb/latest/developerguide/TTL.md "../../../amazondynamodb/latest/developerguide/TTL.md") feature to define a per-item expiration
timestamp. 

Distinguish between data that is available for use, and data that
is stored as a backup.  Consider using
[AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/") to automate the backup of data across AWS services.
 [Amazon EBS snapshots](../../../ebs/latest/userguide/ebs-snapshots.md "../../../ebs/latest/userguide/ebs-snapshots.md") provide a way to copy an EBS volume and store
it using S3 features, including lifecycle, data protection, and
access to protection mechanisms. Two of these mechanisms are
[S3
Object Lock](../../../AmazonS3/latest/userguide/object-lock.md "../../../AmazonS3/latest/userguide/object-lock.md") and
[AWS Backup Vault Lock](../../../aws-backup/latest/devguide/vault-lock.md "../../../aws-backup/latest/devguide/vault-lock.md"), which can provide you with additional
security and control over your backups. Manage clear separation of
duties and access for backups. Isolate backups at the account
level to maintain separation from the affected environment during
an event.

Another aspect of lifecycle management is recording the history of
data as it progresses through your workload, called _data
provenance tracking_. This can give confidence that you
know where the data came from, any transformations performed, what
owner or process made those changes, and when.  Having this
history helps with troubleshooting issues and investigations
during potential security events.  For example, you can log
metadata about transformations in an
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") table.  Within a data lake, you can keep copies of
transformed data in different S3 buckets for each data pipeline
stage. Store schema and timestamp information in an
[AWS Glue Data Catalog](../../../glue/latest/dg/catalog-and-crawler.md "../../../glue/latest/dg/catalog-and-crawler.md").  Regardless of your solution, consider
the requirements of your end users to determine the appropriate
tooling you need to report on your data provenance.  This will
help you determine how to best track your provenance.

### Implementation steps

1. Analyze the workload's data types, sensitivity levels, and
   access requirements to classify the data and define
   appropriate lifecycle management strategies.
2. Design and implement data retention policies and automated
   destruction processes that align with legal, regulatory, and
   organizational requirements.
3. Establish processes and automation for continuous monitoring,
   auditing, and adjustment of data lifecycle management
   strategies, controls, and policies as workload requirements
   and regulations evolve.
   1. Detect resources that do not have automated lifecycle
      management turned on with
      [AWS Config](../../../config/latest/developerguide/s3-lifecycle-policy-check.md "../../../config/latest/developerguide/s3-lifecycle-policy-check.md")

## Resources

**Related best practices:**

- [COST04-BP05
  Enforce data retention policies](../framework/cost_decomissioning_resources_data_retention.md "../framework/cost_decomissioning_resources_data_retention.md")
- [SUS04-BP03
  Use policies to manage the lifecycle of your datasets](../framework/sus_sus_data_a4.md "../framework/sus_sus_data_a4.md")

**Related documents:**

- [Data
  Classification Whitepaper](../../../whitepapers/latest/data-classification/data-classification-overview.md "../../../whitepapers/latest/data-classification/data-classification-overview.md")
- [AWS Blueprint for Ransomware Defense](https://d1.awsstatic.com/whitepapers/compliance/AWS-Blueprint-for-Ransomware-Defense.pdf "https://d1.awsstatic.com/whitepapers/compliance/AWS-Blueprint-for-Ransomware-Defense.pdf")
- [DevOps
  Guidance: Improve traceability with data provenance
  tracking](../devops-guidance/ag.dlm.md "../devops-guidance/ag.dlm.md")

**Related examples:**

- [How
  to protect sensitive data for its entire lifecycle in
  AWS](https://aws.amazon.com/blogs/security/how-to-protect-sensitive-data-for-its-entire-lifecycle-in-aws/ "https://aws.amazon.com/blogs/security/how-to-protect-sensitive-data-for-its-entire-lifecycle-in-aws/")
- [Build
  data lineage for data lakes using AWS Glue, Amazon Neptune,
  and Spline](https://aws.amazon.com/blogs/big-data/build-data-lineage-for-data-lakes-using-aws-glue-amazon-neptune-and-spline/ "https://aws.amazon.com/blogs/big-data/build-data-lineage-for-data-lakes-using-aws-glue-amazon-neptune-and-spline/")

**Related tools:**

- [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/")
- [Amazon Data Lifecycle Manager](https://aws.amazon.com/ebs/data-lifecycle-manager/ "https://aws.amazon.com/ebs/data-lifecycle-manager/")
- [AWS Identity and Access Management Access Analyzer](https://aws.amazon.com/iam/access-analyzer/ "https://aws.amazon.com/iam/access-analyzer/")
