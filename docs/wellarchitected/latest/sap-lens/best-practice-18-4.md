# Best Practice 18.4 – Evaluate the cost

impact of storage options based on the required characteristics

Select from object storage, file storage, and block storage services to host, archive,
and secure your SAP system. Design your storage to reduce cost and increase
agility.

**Suggestion 18.4.1 – Evaluate the most cost-effective way to design
for the I/O and throughput requirements of your workload**

For most SAP requirements, solid state drives (SSDs) are recommended for your EBS
volumes. To ensure a flexible, cost-effective selection, we recommend starting with the
General Purpose Amazon EBS type `gp3`, if supported by the instance family. Over time,
review the usage using CloudWatch metrics and application/database monitoring. If higher
durability or I/O rates greater than 16,000 per volume are required, consider the
Provisioned IOPS Amazon EBS type.

- AWS Documentation: [Amazon EBS
  volume types](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md")
  To balance cost and performance considerations, the storage configuration used for
  SAP HANA data and log volumes should meet the SAP storage KPI. The storage layouts
  outlined in the following document have been tested for the SAP TDI guidelines: [SAP HANA Tailored Data Center Integration](https://www.sap.com/documents/2016/05/e8705aae-717c-0010-82c7-eda71af511fa.html "https://www.sap.com/documents/2016/05/e8705aae-717c-0010-82c7-eda71af511fa.html")

- AWS Documentation: [Storage Configuration for SAP HANA](../../../sap/latest/sap-hana/hana-ops-storage-config.md "../../../sap/latest/sap-hana/hana-ops-storage-config.md")

**Suggestion 18.4.2 – Plan for dynamic changes to storage size and
configuration**

Optimize storage costs by right sizing storage according to data usage or IOPS
requirements.

Extend volume size dynamically as required. Evaluate the option of changing volume
types during activities that require increased performance such as application upgrades.

- AWS Documentation: [Requesting Volume Modifications](../../../AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.md "../../../AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.md")
  Ensure all orphaned or unused volumes are reviewed regularly to ensure cost control.

- AWS Documentation: [List Amazon EBS volume or snapshot information](https://aws.amazon.com/premiumsupport/knowledge-center/ebs-volume-snapshot-ec2-instance/ "https://aws.amazon.com/premiumsupport/knowledge-center/ebs-volume-snapshot-ec2-instance/")

**Suggestion 18.4.3 – Evaluate the cost benefits for object
storage**

The core data for an SAP system is contained within the database and resides on
Amazon EBS. Amazon S3 can provide low-cost object storage for auxiliary data, such as
backups or archives and large objects such as images or documents. Cost can be further
optimized by selecting the appropriate [storage
type](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") for your retention and durability needs.

**Suggestion 18.4.4 – Evaluate the cost benefits for shared file
systems**

Amazon Elastic File System (Amazon EFS) provides a serverless, set-and-forget, elastic
file system that lets you share file data without provisioning or managing storage. Cost
can be further optimized by selecting the appropriate storage class based on your
performance and availability requirement.

Amazon FSx provides a fully managed highly available and durable file storage solution
built on Windows Server. Data deduplication allows you to optimize costs even further by
removing redundant data.

Common SAP use cases for Amazon EFS or Amazon FSx include `sapmnt`,
transports, interface files, storing backups, and software. Use of Amazon EFS or Amazon
FSx can provide cost benefits over deploying your own highly available NFS solution.

- AWS Documentation: [Amazon EFS](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/")
- AWS Documentation: [Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/")
