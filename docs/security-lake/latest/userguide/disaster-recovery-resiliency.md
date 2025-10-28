# Resilience in Amazon Security Lake

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. These Availability Zones offer you an effective way to design and
operate applications and databases. Availability Zones are more highly available, fault tolerant, and scalable than
traditional single or multiple data center infrastructures.

The availability of Security Lake is tied to Region availability. Distribution across multiple Availability Zones helps the service
tolerate failures in any single Availability Zone.

The availability of the Security Lake data plane is not tied to any Region availability.
However, the availability of the Security Lake control plane is closely tied to US East (N.
Virginia) Region availability.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Security Lake, in which data is backed by Amazon Simple Storage Service (Amazon S3); offers several
features to help support your data resiliency and backup needs.

**Lifecycle configuration**
A lifecycle configuration is a set of rules that define actions that Amazon S3 applies to a group of objects. With
lifecycle configuration rules, you can tell Amazon S3 to transition objects to less expensive storage classes, archive them, or delete
them. For more information, see [Managing your storage lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") in the
_Amazon S3 User Guide_.

**Versioning**
Versioning is a means of keeping multiple variants of an object in the same bucket. You can use versioning to
preserve, retrieve, and restore every version of every object stored in your Amazon S3 bucket. Versioning helps you recover
from both unintended user actions and application failures. For more information, see [Using versioning in S3 buckets](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md")
in the _Amazon S3 User Guide_.

**Storage classes**
Amazon S3 offers a range of storage classes to choose from depending on the requirements of your workload.
The S3 Standard-IA and S3 One Zone-IA storage classes are designed for data you access about once a month and need milliseconds
access. The S3 Glacier Instant Retrieval storage class is designed for long-lived archive data accessed with milliseconds access
that you access about once a quarter. For archive data that does not require immediate access, such as backups, you can use the
S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes. For more information, see
[Using Amazon S3 storage classes](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md")
in the _Amazon S3 User Guide_.
