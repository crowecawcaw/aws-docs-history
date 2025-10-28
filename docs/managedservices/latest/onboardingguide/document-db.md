# Use AMS SSP to provision Amazon DocumentDB (with MongoDB compatibility) in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon DocumentDB (with MongoDB compatibility) capabilities directly in your AMS managed account. Amazon DocumentDB (with MongoDB compatibility) is a fast, scalable, highly available, and fully managed document database service that supports MongoDB
workloads. Amazon DocumentDB gives you the performance, scalability,
and availability you need when operating mission-critical MongoDB workloads at scale. Amazon DocumentDB implements the Apache 2.0
open source MongoDB 3.6 API by emulating the responses that a MongoDB client expects from a MongoDB server, allowing you
to use your existing MongoDB drivers and tools with
Amazon DocumentDB. In Amazon DocumentDB, the storage and compute are decoupled, allowing each to scale independently, and you can increase
the read capacity to millions of
requests per second by adding up to 15 low latency read replicas, regardless of the size of your data. Amazon DocumentDB is
designed for 99.99% availability and
replicates six copies of your data across three AWS Availability Zones (AZs). You can use AWS Database Migration Service (DMS) for free (for
six months) to migrate
your on-premises or Amazon Elastic Compute Cloud (Amazon EC2) MongoDB databases to Amazon DocumentDB with virtually no downtime.
To learn more, see
[Amazon DocumentDB (with MongoDB compatibility)](https://aws.amazon.com/documentdb/ "https://aws.amazon.com/documentdb/").

## Amazon DocumentDB in AWS Managed Services FAQ

**Q: How do I request access to Amazon DocumentDB in my AMS account?**

Amazon DocumentDB console and data access roles can be requested through the submission of two AMS RFCs,
console access and data access:

Request access to Amazon DocumentDB by submitting an RFC with the Management | AWS
service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM role to your account:
`customer_documentdb_role`. After it's provisioned in your
account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon DocumentDB in my AMS account?**

Amazon DocumentDB requires Amazon RDS-specific permissions. Because AMS fully manages
Amazon RDS, the IAM role for Amazon DocumentDB includes some restrictions to actions on
Amazon RDS. The following restrictions apply:

- Access to the `DeleteDBInstance` and `DeleteDBCluster` APIs have been restricted.
  To use those deletion APIs, submit an RFC with the Management | Advanced stack components | Identity and Access Management (IAM) | Update entity or policy (managed automation) change type (ct-27tuth19k52b4).
- You can't add or remove tags from Amazon RDS instances.
- You can't make your Amazon DocumentDB instance public.

**Q: What are the prerequisites or dependencies to using Amazon DocumentDB in my AMS account?**

Amazon S3 and AWS KMS are required in order to use Amazon DocumentDB, if Amazon S3 buckets are encrypted with AWS KMS keys.
