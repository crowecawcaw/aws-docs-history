# High performance workloads

## S3 Express One Zone

You can use Amazon S3 Express One Zone for high-performance workloads. S3 Express One Zone is the first S3
storage class where you can select a single Availability Zone with the option to co-locate
your object storage with your compute resources which provides the highest possible access
speed. Objects in S3 Express One Zone are stored in directory buckets located in Availability Zones.
For more information on directory buckets, see [Directory
buckets](directory-buckets-overview.md "directory-buckets-overview.md").

Amazon S3 Express One Zone is a high-performance, single-zone Amazon S3 storage class that is
purpose-built to deliver consistent, single-digit millisecond data access for your most
latency-sensitive applications. S3 Express One Zone is the lowest latency cloud-object storage class
available today, with data access speeds up to 10x faster and with request costs 50 percent
lower than S3 Standard. Applications can benefit immediately from requests being completed up
to an order of magnitude faster. S3 Express One Zone provides similar performance elasticity as
other S3 storage classes. S3 Express One Zone is used for workloads or performance-critical applications that
require consistent single-digit millisecond latency.

As with other Amazon S3 storage classes, you don't need to plan or provision capacity or
throughput requirements in advance. You can scale your storage up or down, based on need,
and access your data through the Amazon S3 API.

The Amazon S3 Express One Zone storage class is designed for 99.95 percent availability within a single Availability Zone and is backed
by the [Amazon S3 Service Level Agreement](https://aws.amazon.com/s3/sla/ "https://aws.amazon.com/s3/sla/"). With
S3 Express One Zone, your data is redundantly stored on multiple devices within a single
Availability Zone. S3 Express One Zone is designed to handle concurrent device failures by quickly
detecting and repairing any lost redundancy. If the existing device encounters a
failure, S3 Express One Zone automatically shifts requests to new devices within an Availability Zone.
This redundancy helps ensure uninterrupted access to your data within an Availability
Zone.

S3 Express One Zone is ideal for any application where it's important to minimize the latency
required to access an object. Such applications can be human-interactive workflows, like
video editing, where creative professionals need responsive access to content from their
user interfaces. S3 Express One Zone also benefits analytics and machine learning workloads that
have similar responsiveness requirements from their data, especially workloads with lots of
smaller accesses or large numbers of random accesses. S3 Express One Zone can be used with other
AWS services to support analytics and artificial intelligence and machine learning (AI/ML)
workloads, such as Amazon EMR, Amazon SageMaker AI, and Amazon Athena.

![Diagram showing how S3 Express One Zone works.](images/s3-express-one-zone.png)

For the directory buckets that use the S3 Express One Zone storage class, data is stored across multiple devices
within a single Availability Zone but doesn't store data redundantly across Availability
Zones. When you create a directory bucket to use the S3 Express One Zone storage class, we recommend that you specify an AWS Region and
an Availability Zone that's local to your Amazon EC2, Amazon Elastic Kubernetes Service, or Amazon Elastic Container Service (Amazon ECS) compute instances
to optimize performance.

When using S3 Express One Zone, you can interact with your directory bucket in a virtual private cloud (VPC) by
using a gateway VPC endpoint. With a gateway endpoint, you can access S3 Express One Zone
directory buckets from your VPC without an internet gateway or NAT device for your VPC,
and at no additional cost.

You can use many of the same Amazon S3 API operations and features with directory buckets
that you use with general purpose buckets and other storage classes. These include Mountpoint for
Amazon S3, server-side encryption with Amazon S3 managed keys (SSE-S3), server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), S3 Batch Operations, and S3 Block
Public Access. You can access S3 Express One Zone by using the Amazon S3 console, AWS Command Line Interface (AWS CLI),
AWS SDKs, and the Amazon S3 REST API.

For more information about S3 Express One Zone, see the following topics.

- [Overview](#s3-express-one-zone-overview "#s3-express-one-zone-overview")
- [Features of S3 Express One Zone](#s3-express-features "#s3-express-features")
- [Related services](#s3-express-related-services "#s3-express-related-services")
- [Next steps](#s3-express-next-steps "#s3-express-next-steps")

### Overview

To optimize performance and reduce latency, S3 Express One Zone introduces the following new
concepts.

#### Availability Zones

The Amazon S3 Express One Zone storage class is designed for 99.95 percent availability within a single Availability Zone and is backed
by the [Amazon S3 Service Level Agreement](https://aws.amazon.com/s3/sla/ "https://aws.amazon.com/s3/sla/"). With
S3 Express One Zone, your data is redundantly stored on multiple devices within a single
Availability Zone. S3 Express One Zone is designed to handle concurrent device failures by quickly
detecting and repairing any lost redundancy. If the existing device encounters a
failure, S3 Express One Zone automatically shifts requests to new devices within an Availability Zone.
This redundancy helps ensure uninterrupted access to your data within an Availability
Zone.

An Availability Zone is one or more discrete data centers with redundant power,
networking, and connectivity in an AWS Region. When you create a directory bucket,
you choose the Availability Zone and AWS Region where your bucket will be located.

##### Single Availability Zone

When you create a directory bucket, you choose the Availability Zone and
AWS Region.

Directory buckets use the S3 Express One Zone storage class, which is built to be used by
performance-sensitive applications. S3 Express One Zone is the first S3 storage class where you can select a single Availability Zone with
the option to co-locate your object storage with your compute resources, which provides the highest possible access speed.

With
S3 Express One Zone, your data is redundantly stored on multiple devices within a single
Availability Zone. S3 Express One Zone is designed for 99.95 percent availability within a single Availability Zone and is backed
by the [Amazon S3 Service Level Agreement](https://aws.amazon.com/s3/sla/ "https://aws.amazon.com/s3/sla/"). For more information, see [Availability Zones](#s3-express-overview-az "#s3-express-overview-az")

#### Endpoints and gateway VPC

endpoints

Bucket-management API operations for directory buckets are available through a
Regional endpoint and are referred to as Regional endpoint API operations. Examples
of Regional endpoint API operations are `CreateBucket` and
`DeleteBucket`. After you create a directory bucket, you can use
Zonal endpoint API operations to upload and manage the objects in your directory
bucket. Zonal endpoint API operations are available through a Zonal endpoint.
Examples of Zonal endpoint API operations are `PutObject` and
`CopyObject`.

You can access S3 Express One Zone from your VPC by using gateway VPC endpoints. After you
create a gateway endpoint, you can add it as a target in your route table for
traffic destined from your VPC to S3 Express One Zone. As with Amazon S3, there is no additional
charge for using gateway endpoints. For more information about how to configure
gateway VPC endpoints, see [Networking for directory buckets](s3-express-networking.md "s3-express-networking.md")

#### Session-based

authorization

With S3 Express One Zone, you authenticate and authorize requests through a new
session-based mechanism that is optimized to provide the lowest latency. You can use
`CreateSession` to request temporary credentials that provide
low-latency access to your bucket. These temporary credentials are scoped to a
specific S3 directory bucket. Session tokens are used only with Zonal (object-level)
operations (with the exception of [CopyObject](directory-buckets-objects-copy.md "directory-buckets-objects-copy.md")). For more information, see [Authorizing Zonal endpoint API operations with
CreateSession](s3-express-create-session.md "s3-express-create-session.md").

The [supported AWS SDKs
for S3 Express One Zone](s3-express-SDKs.md#s3-express-getting-started-accessing-sdks "s3-express-SDKs.md#s3-express-getting-started-accessing-sdks") handle session establishment and refreshment on your
behalf. To protect your sessions, temporary security
credentials expire after 5 minutes. After you download and install the AWS SDKs and
configure the necessary AWS Identity and Access Management (IAM) permissions, you can immediately start
using API operations.

### Features of S3 Express One Zone

The following S3 features are available for S3 Express One Zone. For a complete list of
supported API operationss and unsupported features, see [Differences for directory buckets](s3-express-differences.md "s3-express-differences.md").

#### Access management and

security

You can use the following features to audit and manage access. By default, directory
buckets are private and can be accessed only by users who are explicitly granted
access. Unlike general purpose buckets, which can set the access control boundary at the
bucket, prefix, or object tag level, the access control boundary for
directory buckets is set only at the bucket level. For more information, see [Authorizing Regional endpoint API operations with IAM](s3-express-security-iam.md "s3-express-security-iam.md").

- [S3 Block Public
  Access](access-control-block-public-access.md "access-control-block-public-access.md") – All S3 Block Public Access settings are enabled
  by default at the bucket level. This default setting can't be modified.
- [S3 Object Ownership](about-object-ownership.md "about-object-ownership.md") (bucket
  owner enforced by default) – Access control lists (ACLs) are not
  supported for directory buckets. Directory buckets automatically use the
  bucket owner enforced setting for S3 Object Ownership. Bucket owner enforced
  means that ACLs are disabled, and the bucket owner automatically owns and
  has full control over every object in the bucket. This default setting can't
  be modified.
- [AWS Identity and Access Management (IAM)](s3-express-security-iam.md "s3-express-security-iam.md") –
  IAM helps you securely control access to your directory buckets. You can
  use IAM to grant access to bucket management (Regional) API operations and
  object management (Zonal) API operations through the
  `s3express:CreateSession` action. For more information, see
  [Authorizing Regional endpoint API operations with IAM](s3-express-security-iam.md "s3-express-security-iam.md"). Unlike object-management
  actions, bucket management actions cannot be cross-account. Only the bucket
  owner can perform those actions.
- [Bucket
  policies](s3-express-security-iam-example-bucket-policies.md "s3-express-security-iam-example-bucket-policies.md") – Use IAM-based policy language to configure
  resource-based permissions for your directory buckets. You can also use
  IAM to control access to the `CreateSession` API operation,
  which allows you to use the Zonal, or object management, API operations. You
  can grant same-account or cross-account access to Zonal API operations. For
  more information about S3 Express One Zone permissions and policies, see [Authorizing Regional endpoint API operations with IAM](s3-express-security-iam.md "s3-express-security-iam.md").
- [IAM Access Analyzer for S3](access-analyzer.md "access-analyzer.md")
  – Evaluate and monitor your access policies to make sure that the
  policies provide only the intended access to your S3 resources.

#### Logging and

monitoring

S3 Express One Zone uses the following S3 logging and monitoring tools that you can use to
monitor and control how your resources are being used:

- [Amazon CloudWatch metrics](cloudwatch-monitoring.md "cloudwatch-monitoring.md") –
  Monitor your AWS resources and applications by using CloudWatch to collect and
  track metrics. S3 Express One Zone uses the same CloudWatch namespace as other Amazon S3
  storage classes (`AWS/S3`) and supports daily storage metrics for
  directory buckets: `BucketSizeBytes` and
  `NumberOfObjects`. For more information, see [Monitoring metrics with Amazon CloudWatch](cloudwatch-monitoring.md "cloudwatch-monitoring.md").
- [AWS CloudTrail logs](cloudtrail-logging-s3-info.md "cloudtrail-logging-s3-info.md") – AWS CloudTrail is an
  AWS service that helps you implement operational and risk auditing,
  governance, and compliance of your AWS account by recording the actions
  taken by a user, role, or an AWS service. For S3 Express One Zone, CloudTrail captures
  Regional endpoint API operations (for example, `CreateBucket` and
  `PutBucketPolicy`) as management events and Zonal API
  operations (for example, `GetObject` and `PutObject`)
  as data events. These events include actions taken in the AWS Management Console,
  AWS Command Line Interface (AWS CLI), AWS SDKs, and AWS API operations. For more
  information, see [Logging with AWS CloudTrail for S3 Express One Zone](s3-express-one-zone-logging.md "s3-express-one-zone-logging.md").

###### Note

Amazon S3 server access logs aren't supported with S3 Express One Zone.

#### Object management

You can manage your object storage by using the Amazon S3 console, AWS SDKs, and AWS CLI. The
following features are available for object management with S3 Express One Zone:

- [S3 Batch Operations](batch-ops-create-job.md "batch-ops-create-job.md") – Use
  Batch Operations to perform bulk operations on objects in directory buckets, for
  example, **Copy** and **Invoke AWS Lambda function**. For example, you can use
  Batch Operations to copy objects between directory buckets and
  general purpose buckets. With Batch Operations, you can manage billions of objects at
  scale with a single S3 request by using the AWS SDKs or AWS CLI or a few
  clicks in the Amazon S3 console.
- [Import](create-import-job.md "create-import-job.md")
  – After you create a directory bucket, you can populate your bucket
  with objects by using the import feature in the Amazon S3 console. Import is a
  streamlined method for creating Batch Operations jobs to copy objects from general
  purpose buckets to directory buckets.

#### AWS SDKs and client

libraries

You can manage your object storage by using the AWS SDKs and client libraries.

- [Mountpoint for Amazon S3](https://github.com/awslabs/mountpoint-s3/blob/main/doc/SEMANTICS.md "https://github.com/awslabs/mountpoint-s3/blob/main/doc/SEMANTICS.md") – Mountpoint for Amazon S3 is an open source file
  client that delivers high-throughput access, lowering compute costs for data
  lakes on Amazon S3. Mountpoint for Amazon S3 translates local file system API calls to S3
  object API calls like `GET` and `LIST`. It is ideal
  for read-heavy data lake workloads that process petabytes of data and need
  the high elastic throughput provided by Amazon S3 to scale up and down across
  thousands of instances.
- [S3A](https://hadoop.apache.org/docs/stable/hadoop-aws/tools/hadoop-aws/index.html#Introducing_the_Hadoop_S3A_client "https://hadoop.apache.org/docs/stable/hadoop-aws/tools/hadoop-aws/index.html#Introducing_the_Hadoop_S3A_client") – S3A is a
  recommended Hadoop-compatible interface for accessing data
  stores in Amazon S3. S3A replaces the S3N
  Hadoop file system client.
- [PyTorch on AWS](../../../sagemaker/latest/dg/pytorch.md "../../../sagemaker/latest/dg/pytorch.md") – PyTorch on AWS
  is an open source deep-learning framework that makes it easier to develop
  machine learning models and deploy them to production.
- [AWS SDKs](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/") – You can use
  the AWS SDKs when developing applications with Amazon S3. The AWS SDKs
  simplify your programming tasks by wrapping the underlying Amazon S3 REST API.
  For more information about using the AWS SDKs with S3 Express One Zone, see [AWS SDKs](s3-express-SDKs.md#s3-express-getting-started-accessing-sdks "s3-express-SDKs.md#s3-express-getting-started-accessing-sdks").

### Encryption and data

protection

Objects in S3 Express One Zone are automatically encrypted by server-side encryption with Amazon S3
managed keys (SSE-S3). S3 Express One Zone also supports server-side encryption with AWS Key Management Service
(AWS KMS) keys (SSE-KMS). S3 Express One Zone doesn't support server-side encryption with
customer-provided encryption keys (SSE-C), or dual-layer server-side encryption with
AWS KMS keys (DSSE-KMS). For more information, see [Data protection and encryption](s3-express-data-protection.md "s3-express-data-protection.md").

S3 Express One Zone offers you the option to choose the checksum algorithm that is used to
validate your data during upload or download. You can select one of the following Secure
Hash Algorithms (SHA) or Cyclic Redundancy Check (CRC) data-integrity check algorithms:
CRC32, CRC32C, SHA-1, and SHA-256. MD5-based checksums are not supported with the
S3 Express One Zone storage class.

For more information, see [S3 additional checksum best
practices](s3-express-optimizing-performance.md#s3-express-optimizing-performance-checksums "s3-express-optimizing-performance.md#s3-express-optimizing-performance-checksums").

### AWS Signature Version 4

(SigV4)

S3 Express One Zone uses AWS Signature Version 4 (SigV4). SigV4 is
a signing protocol used to authenticate requests to Amazon S3 over HTTPS. S3 Express One Zone
signs requests by using AWS Sigv4. For more information, see [Authenticating Requests (AWS Signature Version 4)](../API/sig-v4-authenticating-requests.md "../API/sig-v4-authenticating-requests.md") in the
_Amazon Simple Storage Service API Reference_.

### Strong consistency

S3 Express One Zone provides strong read-after-write consistency for `PUT` and
`DELETE` requests of objects in your directory buckets in all
AWS Regions. For more information, see [Amazon S3 data consistency model](Welcome.md#ConsistencyModel "Welcome.md#ConsistencyModel").

### Related services

You can use the following AWS services with the S3 Express One Zone storage class to support your
specific low-latency use case.

- [Amazon Elastic Compute Cloud (Amazon EC2)](../../../ec2/index.md "../../../ec2/index.md") – Amazon EC2
  provides secure and scalable computing capacity in the AWS Cloud. Using Amazon EC2
  lessens your need to invest in hardware up front, so you can develop and deploy
  applications faster. You can use Amazon EC2 to launch as many or as few virtual
  servers as you need, configure security and networking, and manage
  storage.
- [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") – Lambda is a compute service that lets you run
  code without provisioning or managing servers. You configure notification
  settings on a bucket, and grant Amazon S3 permission to invoke a function on the
  function's resource-based permissions policy.
- [Amazon Elastic Kubernetes Service
  (Amazon EKS)](../../../eks/latest/userguide/what-is-eks.md "../../../eks/latest/userguide/what-is-eks.md") – Amazon EKS is a managed service that eliminates the need
  to install, operate, and maintain your own Kubernetes control
  plane on AWS. [Kubernetes](https://kubernetes.io/docs/concepts/overview/ "https://kubernetes.io/docs/concepts/overview/") is an open source system that
  automates the management, scaling, and deployment of containerized
  applications.
- [Amazon Elastic Container Service (Amazon ECS)](../../../AmazonECS/latest/developerguide/Welcome.md "../../../AmazonECS/latest/developerguide/Welcome.md") – Amazon ECS is a fully managed container
  orchestration service that helps you easily deploy, manage, and scale
  containerized applications.
- [AWS Key Management Service (AWS KMS)](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") – AWS Key Management Service (AWS KMS) is an AWS managed service that makes it easy for you to create and control the encryption keys that are used to encrypt your data. The AWS KMS keys that you create in AWS KMS are protected by FIPS 140-2 validated hardware security modules (HSM).
  To use or manage your KMS keys, you interact with AWS KMS.
- [Amazon Athena](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md") –
  Athena is an interactive query service that makes it easy to analyze data
  directly in Amazon S3 by using standard [SQL](../../../athena/latest/ug/ddl-sql-reference.md "../../../athena/latest/ug/ddl-sql-reference.md"). You can also use
  Athena to interactively run data analytics by using Apache Spark
  without having to plan for, configure, or manage resources. When you run
  Apache Spark applications on Athena, you submit
  Spark code for processing and receive the results
  directly.
- [Amazon SageMaker
  Training](../../../sagemaker/latest/dg/how-it-works-training.md "../../../sagemaker/latest/dg/how-it-works-training.md") – Review the options for training models with Amazon
  SageMaker, including built-in algorithms, custom algorithms, libraries, and
  models from the AWS Marketplace.
- [AWS Glue](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md")
  – AWS Glue is a serverless data-integration service that makes it easy for
  analytics users to discover, prepare, move, and integrate data from multiple
  sources. You can use AWS Glue for analytics, machine learning, and application
  development. AWS Glue also includes additional productivity and data-ops tooling
  for authoring, running jobs, and implementing business workflows.
- [Amazon EMR](../../../emr/latest/ManagementGuide/emr-what-is-emr.md "../../../emr/latest/ManagementGuide/emr-what-is-emr.md") – Amazon EMR is a managed cluster platform that simplifies
  running big data frameworks, such as Apache Hadoop and
  Apache Spark, on AWS to process and analyze vast amounts of
  data.
- [AWSCloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") – AWSCloudTrail is s an AWS service
  that helps you enable operational and risk auditing, governance, and compliance of your AWS account.
  Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in
  the AWS Management Console, AWS Command Line Interface, and AWS SDKs and APIs.
- [AWS
  CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") – is a service that helps you model and set
  up your AWS resources so that you can spend less time managing those resources
  and more time focusing on your applications that run in AWS. You create a
  template that describes all the AWS resources that you want (like Amazon EC2
  instances or Amazon RDS DB instances), and CloudFormation takes care of
  provisioning and configuring those resources for you. You don't need to
  individually create and configure AWS resources and figure out what's
  dependent on what; CloudFormation handles that.

### Next steps

For more information about working with the S3 Express One Zone storage class and directory buckets,
see the following topics:

- [Tutorial: Getting started with S3 Express One Zone](s3-express-getting-started.md "s3-express-getting-started.md")
- [S3 Express One Zone Availability Zones and Regions](s3-express-Endpoints.md "s3-express-Endpoints.md")
- [Networking for directory buckets in an Availability Zone](directory-bucket-az-networking.md "directory-bucket-az-networking.md")
- [Creating directory buckets in an Availability Zone](directory-bucket-create.md "directory-bucket-create.md")
- [Regional and Zonal endpoints for directory buckets in an Availability Zone](endpoint-directory-buckets-AZ.md "endpoint-directory-buckets-AZ.md")
- [Optimizing S3 Express One Zone performance](s3-express-performance.md "s3-express-performance.md")
