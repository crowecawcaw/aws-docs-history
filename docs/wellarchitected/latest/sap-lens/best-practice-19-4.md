# Best Practice 19.4 – Review backup

strategy for improvements

When running SAP on AWS, you should evaluate your approach to backups and retention
to optimize the costs associated with location, retention, and recovery.

**Suggestion 19.4.1 – Evaluate the locations of your
backups**

Amazon S3 is the suggested long-term storage solution for your SAP system backups for
its low cost, durability, and storage class options. To copy the data on your Amazon EBS
volumes to Amazon S3, you can use point in time snapshots, integrated database tools, or
direct API calls to transfer data.

Snapshots are _incremental_ backups, which means that only the
blocks on the device that have changed after your most recent snapshot are saved. This
minimizes the time required to create the snapshot and saves storage costs by not
duplicating data.

Database backup solutions require a knowledge of database state to ensure
consistency. AWS provides an SAP HANA backup solution (AWS Backint Agent for SAP HANA)
at no additional cost which integrates directly with Amazon S3. For other SAP supported
databases, there are database vendors or third-party provided backup tools available which
support backing up directly to Amazon S3.

- SAP Documentation: [Featured backup solutions](https://www.sap.com/dmc/exp/2013_09_adpd/enEN/#/solutions?search=backup "https://www.sap.com/dmc/exp/2013_09_adpd/enEN/#/solutions?search=backup")
  For ad-hoc requirements or as a staging area, it might be necessary to first back up
  to Amazon EBS. For these use cases, an `ST1` volume type is a low-cost HDD
  volume which provides throughput and performance characteristics suitable for backups.
  Selecting `ST1` can reduce your overall storage costs when the need to back up
  the SAP database to disk is required.

- AWS Documentation: [Amazon EBS volume
  types](https://aws.amazon.com/ebs/features/#Amazon_EBS_volume_types "https://aws.amazon.com/ebs/features/#Amazon_EBS_volume_types")
  If using Amazon EFS for backups, consider EFS-Infrequent Access. This storage class
  reduces storage costs for files that are not accessed every day. Amazon EFS One
  Zone-Infrequent Access is not recommended for backups due to the data only residing in one
  Availability Zone.

**Suggestion 19.4.2 – Review and implement a retention policy for
standard backups**

To control costs, you need to implement a retention policy aligned with your business
requirements that covers the storage services in use.

Amazon S3 offers a range of storage classes designed for different use cases with
characteristics such as cost per GB, minimum storage duration charge, and retrieval fee
(where applicable). Understanding the retention and access requirements for your backups
will help determine which storage class is most suitable to meet your requirements.

S3 Lifecycle policies can be used to automatically transfer to a different storage
class without any changes to your application. For example, backups with shorter retention
periods might be better suited to S3 Standard than S3-IA or Amazon Glacier options due to the
minimum storage duration charges and retrieval fees associated with these classes. Backups
with longer retention periods such as monthly backups for audit purposes are better suited
to S3-IA or Amazon Glacier dependent on the required retention period.

Amazon Data Lifecycle Manager can be used to automate the creation, retention, and deletion of EBS snapshots
and EBS-backed AMIs.

Amazon EFS lifecycle management automatically manages cost-effective file storage for your
file systems.

- AWS Documentation: [Amazon S3
  Storage Classes](https://aws.amazon.com/s3/storage-classes "https://aws.amazon.com/s3/storage-classes")
- AWS Documentation: [Amazon S3 Storage Classes
  Infographic](https://aws.amazon.com/s3/storage-classes-infographic/ "https://aws.amazon.com/s3/storage-classes-infographic/")
- AWS Service: [Amazon Data Lifecycle Manager](../../../AWSEC2/latest/UserGuide/snapshot-lifecycle.md "../../../AWSEC2/latest/UserGuide/snapshot-lifecycle.md") for EBS
  snapshots and EBS-backed AMIs
- AWS Documentation: [Amazon EFS
  Lifecycle Management](../../../efs/latest/ug/lifecycle-management-efs.md "../../../efs/latest/ug/lifecycle-management-efs.md")
- AWS Service: [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/")

**Suggestion 19.4.3 – Create a strategy for ad-hoc backups**

Ad-hoc backups of a system or component might be required prior to a change or as a
reference for system state at a particular point in time. When the required retention does
not align with your standard lifecycle policy, you might need to adopt a separate schedule
or process for ensuring that storage usage and deletion is cost eﬀective for the individual
requirements of that backup.

- AWS Documentation: [Amazon S3 Storage Lifecycle
  Management](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md")
- AWS Documentation: [Amazon EBS Snapshots
  Archive](../../../AWSEC2/latest/UserGuide/snapshot-archive.md "../../../AWSEC2/latest/UserGuide/snapshot-archive.md")

**Suggestion 19.4.4 – Review backup setup against recovery
approach**

Backups are used to revert a system to a previous point in time and to guard against
failure scenarios. Ensuring cost efficiency through a robust, but not excessive, use of
backup storage requires that you review the recovery approach. Challenge assumptions on
requirements for older more granular backups. Determine if these earlier backups would be
required in the event of a recovery.

For example, it is a valid strategy to use both database and file system backups.
However, if the primary mechanism for recovery is using database restore tools, there
might be opportunities to optimize costs by reducing the retention or deleting snapshot
backups for some volumes.

- AWS Documentation: [Amazon
  EBS snapshots](../../../AWSEC2/latest/UserGuide/EBSSnapshots.md "../../../AWSEC2/latest/UserGuide/EBSSnapshots.md")
- AWS Documentation: [AWS Trusted Advisor best practice checklist](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/")
