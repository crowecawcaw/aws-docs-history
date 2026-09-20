

# SUS04-BP02 Use technologies that support data access and storage patterns
<a name="sus_sus_data_a3"></a>

 Use storage technologies that best support how your data is accessed and stored to minimize the resources provisioned while supporting your workload. 

 **Common anti-patterns:** 
+  You assume that all workloads have similar data storage and access patterns. 
+  You only use one tier of storage, assuming all workloads fit within that tier. 
+  You assume that data access patterns will stay consistent over time. 

 **Benefits of establishing this best practice:** Selecting and optimizing your storage technologies based on data access and storage patterns will help you reduce the required cloud resources to meet your business needs and improve the overall efficiency of cloud workload. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Select the storage solution that aligns best to your access patterns, or consider changing your access patterns to align with the storage solution to maximize performance efficiency. 

### Implementation steps
<a name="implementation-steps"></a>
+ **Evaluate data and access characteristics:** Evaluate your data characteristics and access pattern to collect the key characteristics of your storage needs. Key characteristics to consider include: 
  +  **Data type:** structured, semi-structured, unstructured 
  +  **Data growth:** bounded, unbounded 
  +  **Data durability:** persistent, ephemeral, transient 
  +  **Access patterns:** reads or writes, frequency, spiky, or consistent 
+ **Choose the right storage technology:** Migrate data to the appropriate storage technology that supports your data characteristics and access pattern. Here are some examples of AWS storage technologies and their key characteristics: 


<table>
<thead>
  <tr><th>Type</th><th>Technology</th><th>Key characteristics</th></tr>
</thead>
<tbody>
  <tr><td> Object storage </td><td><a href="https://aws.amazon.com/s3/">Amazon S3</a></td><td> An object storage service with unlimited scalability, high availability, and multiple options for accessibility. Transferring and accessing objects in and out of Amazon S3 can use a service, such as <a href="https://aws.amazon.com/s3/transfer-acceleration/">Transfer Acceleration</a> or <a href="https://aws.amazon.com/s3/features/access-points/">Access Points</a>, to support your location, security needs, and access patterns. </td></tr>
  <tr><td> Archiving storage </td><td><a href="https://aws.amazon.com/s3/storage-classes/glacier/">Amazon Glacier</a></td><td> Storage class of Amazon S3 built for data-archiving. </td></tr>
  <tr><td> Shared file system </td><td><a href="https://aws.amazon.com/efs/">Amazon Elastic File System (Amazon EFS)</a></td><td> Mountable file system that can be accessed by multiple types of compute solutions. Amazon EFS automatically grows and shrinks storage and is performance-optimized to deliver consistent low latencies. </td></tr>
  <tr><td> Shared file system </td><td><a href="https://aws.amazon.com/fsx/">Amazon FSx</a></td><td> Built on the latest AWS compute solutions to support four commonly used file systems: NetApp ONTAP, OpenZFS, Windows File Server, and Lustre. Amazon FSx <a href="https://aws.amazon.com/fsx/when-to-choose-fsx/">latency, throughput, and IOPS</a> vary per file system and should be considered when selecting the right file system for your workload needs. </td></tr>
  <tr><td> Block storage </td><td><a href="https://aws.amazon.com/ebs/">Amazon Elastic Block Store (Amazon EBS)</a></td><td> Scalable, high-performance block-storage service designed for Amazon Elastic Compute Cloud (Amazon EC2). Amazon EBS includes SSD-backed storage for transactional, IOPS-intensive workloads and HDD-backed storage for throughput-intensive workloads. </td></tr>
  <tr><td>Relational database</td><td><a href="https://aws.amazon.com/rds/aurora/">Amazon Aurora</a>, <a href="https://aws.amazon.com/rds/">Amazon RDS</a>, <a href="https://aws.amazon.com/redshift/">Amazon Redshift</a></td><td>Designed to support ACID (atomicity, consistency, isolation, durability) transactions and maintain referential integrity and strong data consistency. Many traditional applications, enterprise resource planning (ERP), customer relationship management (CRM), and ecommerce systems use relational databases to store their data.</td></tr>
  <tr><td>Key-value database</td><td><a href="https://aws.amazon.com/dynamodb/">Amazon DynamoDB</a></td><td>Optimized for common access patterns, typically to store and retrieve large volumes of data. High-traffic web apps, ecommerce systems, and gaming applications are typical use-cases for key-value databases.</td></tr>
</tbody>
</table>

+ **Automate storage allocation:** For storage systems that are a fixed size, such as Amazon EBS or Amazon FSx, monitor the available storage space and automate storage allocation on reaching a threshold. You can leverage Amazon CloudWatch to collect and analyze different metrics for [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html) and [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/monitoring-cloudwatch.html). 
+ **Choose the right storage class:** Choose the appropriate storage class for your data. 
  +  Amazon S3 storage classes can be configured at the object level. A single bucket can contain objects stored across all of the storage classes. 
  +  You can use [Amazon S3 Lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to automatically transition objects between storage classes or remove data without any application changes. In general, you have to make a trade-off between resource efficiency, access latency, and reliability when considering these storage mechanisms. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) 
+  [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) 
+  [Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html) 
+ [ Amazon EBS I/O Characteristics ](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-io-characteristics.html)
+ [ Using Amazon S3 storage classes ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
+  [What is Amazon Glacier?](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html) 

 **Related videos:** 
+ [AWS re:Invent 2023 - Improve Amazon EBS efficiency and be more cost-efficient ](https://www.youtube.com/watch?v=7-CB02rqiuw)
+ [AWS re:Invent 2023 - Optimizing storage price and performance with Amazon S3 ](https://www.youtube.com/watch?v=RxgYNrXPOLw)
+ [AWS re:Invent 2023 - Building and optimizing a data lake on Amazon S3 ](https://www.youtube.com/watch?v=mpQa_Zm1xW8)
+ [AWS re:Invent 2022 - Building modern data architectures on AWS](https://www.youtube.com/watch?v=Uk2CqEt5f0o)
+ [AWS re:Invent 2022 - Modernize apps with purpose-built databases ](https://www.youtube.com/watch?v=V-DiplATdi0)
+ [AWS re:Invent 2022 - Building data mesh architectures on AWS](https://www.youtube.com/watch?v=nGRvlobeM_U)
+ [AWS re:Invent 2023 - Deep dive into Amazon Aurora and its innovations ](https://www.youtube.com/watch?v=je6GCOZ22lI)
+ [AWS re:Invent 2023 - Advanced data modeling with Amazon DynamoDB ](https://www.youtube.com/watch?v=PVUofrFiS_A)

 **Related examples:** 
+ [ Amazon S3 Examples ](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-examples.html)
+ [AWS Purpose Built Databases Workshop ](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US)
+ [ Databases for Developers ](https://catalog.workshops.aws/db4devs/en-US)
+ [AWS Modern Data Architecture Immersion Day ](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US)
+ [ Build a Data Mesh on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/23e6326b-58ee-4ab0-9bc7-3c8d730eb851/en-US)