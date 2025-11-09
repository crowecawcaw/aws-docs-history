# SUS04-BP02 Use technologies that support data access and

storage patterns

Use storage technologies that best support how your
data is accessed and stored to minimize the resources
provisioned while supporting your workload.

**Common anti-patterns:**

- You assume that all workloads have similar data storage and access patterns.
- You only use one tier of storage, assuming all workloads fit within that tier.
- You assume that data access patterns will stay consistent over time.

**Benefits of establishing this best practice:** Selecting
and optimizing your storage technologies based on data access and storage patterns will
help you reduce the required cloud resources to meet your business needs and improve
the overall efficiency of cloud workload.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Select the storage solution that aligns best to your access
patterns, or consider changing your access patterns to align
with the storage solution to maximize performance efficiency.

### Implementation steps

- **Evaluate data and access characteristics:**
  Evaluate your data characteristics and access pattern to
  collect the key characteristics of your storage needs.
  Key characteristics to consider include:
  - **Data type:** structured, semi-structured,
    unstructured
  - **Data growth:** bounded, unbounded
  - **Data durability:** persistent, ephemeral,
    transient
  - **Access patterns:** reads or writes,
    frequency, spiky, or consistent

- **Choose the right storage technology:**
  Migrate data to the appropriate storage technology that supports
  your data characteristics and access pattern. Here are some
  examples of AWS storage technologies and their
  key characteristics:

| Type                | Technology                                                                                                                                                                                                                                                | Key characteristics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Object storage      | [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")                                                                                                                                                                                      | An object storage service with unlimited scalability,<br>high availability, and multiple options for accessibility.<br>Transferring and accessing objects in and out of Amazon S3<br>can use a service, such as<br>[Transfer Acceleration](https://aws.amazon.com/s3/transfer-acceleration/ "https://aws.amazon.com/s3/transfer-acceleration/")<br>or [Access<br>Points](https://aws.amazon.com/s3/features/access-points/ "https://aws.amazon.com/s3/features/access-points/"), to support your location, security needs, and access<br>patterns. |
| Archiving storage   | [Amazon Glacier](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/")                                                                                                                                 | Storage class of Amazon S3 built for data-archiving.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Shared file system  | [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/")                                                                                                                                                      | Mountable file system that can be accessed by multiple<br>types of compute solutions. Amazon EFS automatically<br>grows and shrinks storage and is performance-optimized<br>to deliver consistent low latencies.                                                                                                                                                                                                                                                                                                                                   |
| Shared file system  | [Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/")                                                                                                                                                                                   | Built on the latest AWS compute solutions to support<br>four commonly used file systems: NetApp ONTAP, OpenZFS,<br>Windows File Server, and Lustre. Amazon FSx<br>[latency,<br>throughput, and IOPS](https://aws.amazon.com/fsx/when-to-choose-fsx/ "https://aws.amazon.com/fsx/when-to-choose-fsx/") vary per file system and should be<br>considered when selecting the right file system for your<br>workload needs.                                                                                                                            |
| Block storage       | [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/")                                                                                                                                                      | Scalable, high-performance block-storage service<br>designed for Amazon Elastic Compute Cloud (Amazon EC2).<br>Amazon EBS includes SSD-backed storage for transactional,<br>IOPS-intensive workloads and HDD-backed storage for<br>throughput-intensive workloads.                                                                                                                                                                                                                                                                                 |
| Relational database | [Amazon Aurora](https://aws.amazon.com/rds/aurora/ "https://aws.amazon.com/rds/aurora/"), [Amazon RDS](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/"), [Amazon Redshift](https://aws.amazon.com/redshift/ "https://aws.amazon.com/redshift/") | Designed to support ACID (atomicity, consistency, isolation, durability) transactions and maintain referential integrity and strong data consistency. Many traditional applications, enterprise resource planning (ERP), customer relationship management (CRM), and ecommerce systems use relational databases to store their data.                                                                                                                                                                                                               |
| Key-value database  | [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/")                                                                                                                                                                    | Optimized for common access patterns, typically to store and retrieve large volumes of data. High-traffic web apps, ecommerce systems, and gaming applications are typical use-cases for key-value databases.                                                                                                                                                                                                                                                                                                                                      |

- **Automate storage allocation:**
  For storage systems that are a fixed size, such as
  Amazon EBS or Amazon FSx, monitor the available
  storage space and automate storage allocation on
  reaching a threshold. You can leverage Amazon CloudWatch
  to collect and analyze different metrics for
  [Amazon EBS](../../../AWSEC2/latest/UserGuide/using_cloudwatch_ebs.md "../../../AWSEC2/latest/UserGuide/using_cloudwatch_ebs.md") and
  [Amazon FSx](../../../fsx/latest/WindowsGuide/monitoring-cloudwatch.md "../../../fsx/latest/WindowsGuide/monitoring-cloudwatch.md").
- **Choose the right storage class:**
  Choose the appropriate storage class for your data.
  - Amazon S3 storage classes can be configured at the object
    level. A single bucket can contain objects stored
    across all of the storage classes.
  - You can use
    [Amazon S3 Lifecycle policies](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") to automatically transition objects
    between storage classes or remove data without any application changes.
    In general, you have to make a trade-off between resource
    efficiency, access latency, and reliability when considering
    these storage mechanisms.

## Resources

**Related documents:**

- [Amazon EBS volume types](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md")
- [Amazon EC2 instance store](../../../AWSEC2/latest/UserGuide/InstanceStorage.md "../../../AWSEC2/latest/UserGuide/InstanceStorage.md")
- [Amazon S3 Intelligent-Tiering](../../../AmazonS3/latest/userguide/intelligent-tiering.md "../../../AmazonS3/latest/userguide/intelligent-tiering.md")
- [Amazon EBS I/O Characteristics](../../../AWSEC2/latest/WindowsGuide/ebs-io-characteristics.md "../../../AWSEC2/latest/WindowsGuide/ebs-io-characteristics.md")
- [Using Amazon S3 storage classes](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md")
- [What
  is Amazon Glacier?](../../../amazonglacier/latest/dev/introduction.md "../../../amazonglacier/latest/dev/introduction.md")

**Related videos:**

- [AWS re:Invent 2023 - Improve Amazon EBS efficiency and be more cost-efficient](https://www.youtube.com/watch?v=7-CB02rqiuw "https://www.youtube.com/watch?v=7-CB02rqiuw")
- [AWS re:Invent 2023 - Optimizing storage price and performance with Amazon S3](https://www.youtube.com/watch?v=RxgYNrXPOLw "https://www.youtube.com/watch?v=RxgYNrXPOLw")
- [AWS re:Invent 2023 - Building and optimizing a data lake on Amazon S3](https://www.youtube.com/watch?v=mpQa_Zm1xW8 "https://www.youtube.com/watch?v=mpQa_Zm1xW8")
- [AWS re:Invent 2022 - Building modern data architectures on AWS](https://www.youtube.com/watch?v=Uk2CqEt5f0o "https://www.youtube.com/watch?v=Uk2CqEt5f0o")
- [AWS re:Invent 2022 - Modernize apps with purpose-built databases](https://www.youtube.com/watch?v=V-DiplATdi0 "https://www.youtube.com/watch?v=V-DiplATdi0")
- [AWS re:Invent 2022 - Building data mesh architectures on AWS](https://www.youtube.com/watch?v=nGRvlobeM_U "https://www.youtube.com/watch?v=nGRvlobeM_U")
- [AWS re:Invent 2023 - Deep dive into Amazon Aurora and its innovations](https://www.youtube.com/watch?v=je6GCOZ22lI "https://www.youtube.com/watch?v=je6GCOZ22lI")
- [AWS re:Invent 2023 - Advanced data modeling with Amazon DynamoDB](https://www.youtube.com/watch?v=PVUofrFiS_A "https://www.youtube.com/watch?v=PVUofrFiS_A")

**Related examples:**

- [Amazon S3 Examples](../../../sdk-for-javascript/v2/developer-guide/s3-examples.md "../../../sdk-for-javascript/v2/developer-guide/s3-examples.md")
- [AWS Purpose Built Databases Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US")
- [Databases for Developers](https://catalog.workshops.aws/db4devs/en-US "https://catalog.workshops.aws/db4devs/en-US")
- [AWS Modern Data Architecture Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US")
- [Build a Data Mesh on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/23e6326b-58ee-4ab0-9bc7-3c8d730eb851/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/23e6326b-58ee-4ab0-9bc7-3c8d730eb851/en-US")
