

# Fast backup and restore of TiDB on AWS
<a name="tidb-backup-restore"></a>

Publication date: **February 16, 2023 ([Diagram history](diagram-history.md))**

TiDB is an open-source MySQL-compatible database that supports hybrid transactional and analytical processing (HTAP). TiDB clusters deployed on AWS use [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/) for fast backup and restore of several terabytes of data in one hour without impacting cluster performance.

## Fast backup and restore of TiDB on AWS diagram
<a name="tidb-backup-restore-diagram1"></a>

![Architecture diagram showing fast backup and restore of TiDB on AWS using Amazon EBS snapshots and Amazon S3.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/tidb-backup-restore.png)


The following steps describe the architecture:

1. When the user submits a backup request, TiDB Operator checks and collects information from volumes mounted to TiKV and creates a backup job. The backup job pauses the scheduler and garbage collection.

1. The backup job asks AWS to create an Amazon EBS snapshot and resumes the schedulers and garbage collection. After the snapshot completes, the backup job saves the metadata to [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. When the user submits a restore request, the backup job creates a restore job that retrieves backup metadata from Amazon S3 and extracts snapshot information. It invokes the AWS API to create volumes from the Amazon EBS snapshot and returns the created volume information to TiDB Operator.

1. TiDB Operator configures [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/) and mounts the restored volumes to corresponding nodes. After the data restore completes, the TiDB cluster exits restore mode and starts all TiDB nodes to serve requests.

## Further reading
<a name="tidb-backup-restore-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)