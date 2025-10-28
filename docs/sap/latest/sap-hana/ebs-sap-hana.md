# Amazon EBS snapshots for SAP HANA

Amazon EBS snapshots provide point-in-time backups of your EBS volumes to Amazon S3. EBS snapshots are stored incrementally, which means that only the blocks that have changed after your last snapshot are saved, and you are billed only for the changed blocks.

###### Note

EBS snapshots are created at the block level. Creating EBS snapshots does not utilize storage throughput from the underlying EBS volume, or network bandwidth or CPU resources from the Amazon EC2 instance.

If you have Amazon EC2 instances running SAP HANA, you can automate the creation and retention of application-consistent EBS snapshots of the EBS volumes attached to those instances. You can then use these EBS snapshots to restore the entire SAP HANA database to the point-in-time when the EBS snapshot creation was initiated. EBS snapshots are created in a specific AWS Region, and they can be used to restore EBS volumes in any Availability Zone in that Region. EBS snapshots can also be copied to secondary Regions or AWS accounts for Disaster Recovery (DR) purposes.

The time it takes to restore an EBS volume from an EBS snapshot depends on several factors that can impact the [initialization of volume](../../../AWSEC2/latest/UserGuide/ebs-initialize.md "../../../AWSEC2/latest/UserGuide/ebs-initialize.md"). To reduce the time needed to restore a volume from a snapshot, we recommend that you enable the snapshot for [Amazon EBS fast snapshot restore](../../../AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.md "../../../AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.md"). Fast snapshot restore enables you to create a volume from a snapshot that is fully initialized at creation. When you automate application-consistent EBS snapshots for SAP HANA with Amazon Data Lifecycle Manager, you can configure your policy to automatically enable those snapshots for fast snapshot restore. For more information, see [Considerations](dlm-sap-considerations.md "dlm-sap-considerations.md").

We recommend that you use AWS Backint Agent for SAP HANA as your primary backup mechanism, and to create application-consistent EBS snapshots for SAP HANA to supplement your DR strategy, by maintaining copies in other Regions and/or accounts.
