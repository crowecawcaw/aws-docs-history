# Key AWS services

- **Resilient architecture**
  - **[Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"):** Leverage Amazon S3 object storage
    and replication to provide durability and resilience of
    your data on AWS. It is available Regionally (resilient
    against events that impact an entire Availability Zone)
    and also supports cross-Regional replication for
    geographic isolation.
  - **[Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/ "https://aws.amazon.com/ec2/autoscaling/"):** Maintain workload
    availability and automatically add or remove Amazon EC2
    instances according to conditions you define. You can
    also use the dynamic and predictive scaling features of
    Amazon EC2 Auto Scaling to respond to changing demand as
    well as schedule the right number of Amazon EC2
    instances based on predicted demand to scale faster.
  - **[Amazon Route 53](https://aws.amazon.com/route53/ "https://aws.amazon.com/route53/"):** Use the 100% availability of
    Route 53's data plane to direct traffic based on latency,
    proximity, and workload health checks to enable a variety
    of low-latency, fault-tolerant architectures.
  - **[AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/"):** Connect your data
    centers to AWS over dedicated, private, and consistent
    connections using Direct Connect.
  - [**Amazon Virtual Private Cloud (VPC)**](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/"): Provision
    a logically isolated section of AWS where you can launch
    AWS resources.
  - **[Amazon CloudFront](https://aws.amazon.com/cloudfront/ "https://aws.amazon.com/cloudfront/"):** You can cache your content
    in CloudFront's edge locations worldwide and reduce the
    workload on your origin by only fetching content from
    your origin when needed. You can use CloudFront's native
    origin failover capability to automatically serve your
    content from a backup origin when your primary origin is
    unavailable.
  - \*\*[Amazon RDS Multi-AZ](https://aws.amazon.com/rds/features/multi-az/ "https://aws.amazon.com/rds/features/multi-az/") or

  [Amazon Aurora](https://aws.amazon.com/rds/aurora/ "https://aws.amazon.com/rds/aurora/"):\*\* Use Amazon RDS or Aurora
  Multi-AZ deployments to provide enhanced availability
  for production database workloads. Amazon RDS
  synchronously replicates data from a primary instance to
  a secondary in a different AZ which runs on a
  fault-isolated and independent infrastructure. In case
  of infrastructure failure, Amazon RDS automatically
  fails over to the standby so that you can resume
  database operations. These database services can also be
  configured to asynchronously replicate your data to
  additional AWS Regions to support multi-Region
  architectures.
  - **[Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/"):** Amazon DynamoDB is a fully
    managed NoSQL database service that provides fast and
    predictable performance with seamless scalability.
    DynamoDB automatically spreads the data and traffic for
    your tables over a sufficient number of servers to handle
    your throughput and storage requirements and your
    data that is stored is automatically replicated across
    multiple Availability Zones in an AWS Region. DynamoDB
    also supports
    [Global Tables](https://aws.amazon.com/dynamodb/global-tables/ "https://aws.amazon.com/dynamodb/global-tables/") to give you the ability to store your data
    across multiple AWS Regions.
  - **[AWS Shield and AWS Shield Advanced](https://aws.amazon.com/shield/ "https://aws.amazon.com/shield/"):** AWS Shield is a managed service that provides protection
    against distributed denial of service (DDoS) exploits for
    workloads running on
    AWS. AWS Shield Advanced provides additional protections against more
    sophisticated and larger exploits for your workloads
    running on Amazon EC2, ELB (ELB),
    Amazon CloudFront, AWS Global Accelerator, and Route 53.
  - **[AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/"):** AWS Lambda lets you run code
    without provisioning or managing servers. AWS Lambda is
    designed to use replication and redundancy to provide
    high availability for both the service itself and for
    the Lambda functions it operates. There are no
    maintenance windows or scheduled downtimes for either.

- **Monitoring**
  - **[CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/"):**
    Amazon CloudWatch is the principal monitoring service
    for AWS Cloud resources and the workloads that you run on
    AWS.
  - **[Amazon VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md"): Amazon** VPC Flow Logs is
    a feature that enables you to capture information about
    the IP traffic going to and from network interfaces in
    your VPC. Amazon VPC Flow Logs can be monitored through
    CloudWatch.

- **Backup and retention**
  - [**Amazon Glacier**](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"): Amazon Glacier, is an
    extremely low-cost storage service optimized for
    infrequently used data, or cold data.
  - **[Amazon EBS snapshots](../../../AWSEC2/latest/UserGuide/EBSSnapshots.md "../../../AWSEC2/latest/UserGuide/EBSSnapshots.md"),** and

  [**Amazon RDS snapshots**](../../../AmazonRDS/latest/UserGuide/USER_CreateSnapshot.md "../../../AmazonRDS/latest/UserGuide/USER_CreateSnapshot.md"): Snapshots for both
  Amazon RDS and Amazon EBS allow point-in-time recovery
  of the data stored in them. They can be configured to run
  automatically or at a scheduled time.
  - **[AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/"):** AWS Backup is a centralized
    backup service that simplifies and provides a
    cost-effective way for you to back up your workload data
    across AWS services in the AWS Cloud and on-premises.
    Storage volumes, databases, and file systems are backed
    up to a central place where you can configure and audit
    the AWS resources you are backing up, automate backup
    scheduling, set retention policies, and monitor
    recent backup and restore activity.
