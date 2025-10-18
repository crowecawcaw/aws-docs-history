# Resilience in AWS CloudTrail

The AWS global infrastructure is built around AWS Regions and Availability Zones.
 AWS Regions provide multiple physically separated and isolated Availability Zones, which
 are connected with low-latency, high-throughput, and highly redundant networking. With
 Availability Zones, you can design and operate applications and databases that automatically
 fail over between Availability Zones without interruption. Availability Zones are more
 highly available, fault tolerant, and scalable than traditional single or
 multiple
 data center infrastructures. If you specifically need to replicate your
 CloudTrail log files over greater geographic distances, you can use [Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html") for your trail Amazon S3
 buckets, which enables automatic, asynchronous copying of objects across buckets in
 different AWS Regions.

For more information about AWS Regions and Availability Zones, see [AWS Global
 Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, CloudTrail offers several features to help support your data resiliency and backup needs.

**Trails and event data stores that log events in all AWS Regions**

When you create a multi-Region trail, CloudTrail creates trails with identical
 configurations in all enabled AWS Regions in your account.

When you create a multi-Region event data store, CloudTrail collects events that occur in all AWS Regions in your account.

**Versioning, lifecycle configuration, and object lock protection for
 CloudTrail log data**

Because CloudTrail uses Amazon S3 buckets to store log files, you can also use the features provided
 by Amazon S3 to help support your data resiliency and backup needs. For more information, see
 [Resilience in
 Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/disaster-recovery-resiliency.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/disaster-recovery-resiliency.html").
