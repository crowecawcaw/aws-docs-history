# Replicating objects within and across Regions

You can use replication to enable automatic, asynchronous copying of objects across Amazon S3
buckets. Buckets that are configured for object replication can be owned by the same
AWS account or by different accounts. You can replicate objects to a single destination bucket
or to multiple destination buckets. The destination buckets can be in different AWS Regions or
within the same Region as the source bucket.

There are two types of replication: _live replication_ and
_on-demand replication_.

- **Live replication** – **To
  automatically replicate new and updated objects** as they are written to the
  source bucket, use live replication. Live replication doesn't replicate any objects that
  existed in the bucket before you set up replication. To replicate objects that existed
  before you set up replication, use on-demand replication.
- **On-demand replication** – **To
  replicate existing objects** from the source bucket to one or more destination
  buckets on demand, use S3 Batch Replication. For more information about replicating
  existing objects, see [When to use S3 Batch Replication](#batch-replication-scenario "#batch-replication-scenario").
  There are two forms of live replication: _Cross-Region Replication
  (CRR)_ and _Same-Region Replication
  (SRR)_.

- **Cross-Region Replication (CRR)** – You can use CRR
  to replicate objects across Amazon S3 buckets in different AWS Regions. For more information
  about CRR, see [When to use Cross-Region Replication](#crr-scenario "#crr-scenario").
- **Same-Region Replication (SRR)** – You can use
  SRR to copy objects across Amazon S3 buckets in the same AWS Region. For more information about
  SRR, see [When to use Same-Region Replication](#srr-scenario "#srr-scenario").

###### Topics

- [Why use replication?](#replication-scenario "#replication-scenario")
- [When to use Cross-Region Replication](#crr-scenario "#crr-scenario")
- [When to use Same-Region Replication](#srr-scenario "#srr-scenario")
- [When to use two-way replication (bi-directional
  replication)](#two-way-replication-scenario "#two-way-replication-scenario")
- [When to use S3 Batch Replication](#batch-replication-scenario "#batch-replication-scenario")
- [Workload requirements and live
  replication](#replication-workload-requirements "#replication-workload-requirements")
- [What does Amazon S3 replicate?](replication-what-is-isnot-replicated.md "replication-what-is-isnot-replicated.md")
- [Requirements and considerations for
  replication](replication-requirements.md "replication-requirements.md")
- [Setting up live replication overview](replication-how-setup.md "replication-how-setup.md")
- [Managing or pausing live replication](disable-replication.md "disable-replication.md")
- [Replicating existing objects with
  Batch Replication](s3-batch-replication-batch.md "s3-batch-replication-batch.md")
- [Troubleshooting replication](replication-troubleshoot.md "replication-troubleshoot.md")
- [Monitoring replication with metrics, event notifications,
  and statuses](replication-metrics.md "replication-metrics.md")

## Why use replication?

Replication can help you do the following:

- **Replicate objects while retaining metadata** –
  You can use replication to make copies of your objects that retain all metadata, such as
  the original object creation times and version IDs. This capability is important if you
  must ensure that your replica is identical to the source object.
- **Replicate objects into different storage classes**
  – You can use replication to directly put objects into S3 Glacier Flexible Retrieval,
  S3 Glacier Deep Archive, or another storage class in the destination buckets. You
  can also replicate your data to the same storage class and use lifecycle configurations on
  the destination buckets to move your objects to a colder storage class as they age.
- **Maintain object copies under different ownership**
  – Regardless of who owns the source object, you can tell Amazon S3 to change replica
  ownership to the AWS account that owns the destination bucket. This is referred to as
  the _owner override_ option. You can use this option to restrict access
  to object replicas.
- **Keep objects stored over multiple AWS Regions**
  – To ensure geographic differences in where your data is kept, you can set multiple
  destination buckets across different AWS Regions. This feature might help you meet
  certain compliance requirements.
- **Replicate objects within 15 minutes** – To
  replicate your data in the same AWS Region or across different Regions within a
  predictable time frame, you can use S3 Replication Time Control (S3 RTC). S3 RTC replicates 99.99 percent of new
  objects stored in Amazon S3 within 15 minutes (backed by a service-level agreement). For more
  information, see [Meeting compliance requirements with
  S3 Replication Time Control](replication-time-control.md "replication-time-control.md").

###### Note

S3 RTC does not apply to Batch Replication. Batch Replication is an on-demand
replication job, and can be tracked with S3 Batch Operations. For more information, see [Tracking job status and completion reports](batch-ops-job-status.md "batch-ops-job-status.md").

- **Sync buckets, replicate existing objects, and replicate
  previously failed or replicated objects** – To sync buckets and
  replicate existing objects, use Batch Replication as an on-demand replication action. For
  more information about when to use Batch Replication, see [When to use S3 Batch Replication](#batch-replication-scenario "#batch-replication-scenario").
- **Replicate objects and fail over to a bucket in another
  AWS Region** – To keep all metadata and objects in sync across buckets
  during data replication, use two-way replication (also known as bi-directional
  replication) rules before configuring Amazon S3 Multi-Region Access Point failover controls. Two-way replication
  rules help ensure that when data is written to the S3 bucket that traffic fails over to,
  that data is then replicated back to the source bucket.

## When to use Cross-Region Replication

S3 Cross-Region Replication (CRR) is used to copy objects across Amazon S3 buckets in different
AWS Regions. CRR can help you do the following:

- **Meet compliance requirements** – Although Amazon S3
  stores your data across multiple geographically distant Availability Zones by default,
  compliance requirements might dictate that you store data at even greater distances. To
  satisfy these requirements, use Cross-Region Replication to replicate data between distant
  AWS Regions.
- **Minimize latency** – If your customers are in
  two geographic locations, you can minimize latency in accessing objects by maintaining
  object copies in AWS Regions that are geographically closer to your users.
- **Increase operational efficiency** – If you have
  compute clusters in two different AWS Regions that analyze the same set of objects, you
  might choose to maintain object copies in those Regions.

## When to use Same-Region Replication

Same-Region Replication (SRR) is used to copy objects across Amazon S3 buckets in the same
AWS Region. SRR can help you do the following:

- **Aggregate logs into a single bucket** – If you
  store logs in multiple buckets or across multiple accounts, you can easily replicate logs
  into a single, in-Region bucket. Doing so allows for simpler processing of logs in a
  single location.
- **Configure live replication between production and test
  accounts** – If you or your customers have production and test accounts
  that use the same data, you can replicate objects between those multiple accounts, while
  maintaining object metadata.
- **Abide by data sovereignty laws** – You might be
  required to store multiple copies of your data in separate AWS accounts within a certain
  Region. Same-Region Replication can help you automatically replicate critical data when
  compliance regulations don't allow the data to leave your country.

## When to use two-way replication (bi-directional

replication)

- **Build shared datasets across multiple AWS Regions**
  – With replica modification sync, you can easily replicate metadata changes, such
  as object access control lists (ACLs), object tags, or object locks, on replication
  objects. This two-way replication is important if you want to keep all objects and object
  metadata changes in sync. You can [enable replica modification sync](replication-for-metadata-changes.md#enabling-replication-for-metadata-changes "replication-for-metadata-changes.md#enabling-replication-for-metadata-changes") on a new or existing replication rule when
  performing two-way replication between two or more buckets in the same or different
  AWS Regions.
- **Keep data synchronized across Regions during failover**
  – You can synchronize data in buckets between AWS Regions by configuring two-way
  replication rules with S3 Cross-Region Replication (CRR) directly from a Multi-Region Access Point. To make
  an informed decision on when to initiate failover, you can also enable S3 replication
  metrics so that you can monitor the replication in Amazon CloudWatch, in S3 Replication Time Control (S3 RTC), or from the
  Multi-Region Access Point.
- **Make your application highly available** – Even
  in the event of a Regional traffic disruption, you can use two-way replication rules to
  keep all metadata and objects in sync across buckets during data replication.

## When to use S3 Batch Replication

Batch Replication replicates existing objects to different buckets as an on-demand
option. Unlike live replication, these jobs can be run as needed. Batch Replication can help
you do the following:

- **Replicate existing objects** – You can use
  Batch Replication to replicate objects that were added to the bucket before Same-Region
  Replication or Cross-Region Replication were configured.
- **Replicate objects that previously failed to replicate**
  – You can filter a Batch Replication job to attempt to replicate objects with a
  replication status of **FAILED**.
- **Replicate objects that were already replicated**
  – You might be required to store multiple copies of your data in separate
  AWS accounts or AWS Regions. Batch Replication can replicate existing objects to
  newly added destinations.
- **Replicate replicas of objects that were created from a
  replication rule** – Replication configurations create replicas of
  objects in destination buckets. Replicas of objects can be replicated only with
  Batch Replication.

## Workload requirements and live

replication

Depending on your workload requirements, some types of live replication will be better
suited to your use case than others. Use the following table to determine which type of
replication to use for your situation, and whether to use S3 Replication Time Control (S3 RTC) for your workload.
S3 RTC replicates 99.99 percent of new objects stored in Amazon S3 within 15 minutes (backed by a
service-level agreement, or SLA). For more information, see [Meeting compliance requirements with
S3 Replication Time Control](replication-time-control.md "replication-time-control.md").

| Workload requirement                                                                                  | S3 RTC (15-minute SLA) | Cross-Region Replication (CRR) | Same-Region Replication (SRR) |
| ----------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------------ | ----------------------------- |
| Replicate objects between different AWS accounts                                                      | Yes                    | Yes                            | Yes                           |
| Replicate objects within the same AWS Region within 24-48 hours (not SLA<br>backed)                   | No                     | No                             | Yes                           |
| Replicate objects between different AWS Regions within 24-48 hours (not SLA<br>backed)                | No                     | Yes                            | No                            |
| Predictable replication time: Backed by SLA to replicate 99.9 percent of objects<br>within 15 minutes | Yes                    | No                             | No                            |
