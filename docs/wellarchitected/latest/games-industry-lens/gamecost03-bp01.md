# GAMECOST03-BP01 Choose the appropriate type of storage for user

generated content to reduce costs

Each type of data generated and stored in your game has unique
characteristics that you should consider when determining the right
storage solution for your workload.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Use Amazon S3 Object Lifecycle Management to store object data in
the most cost-effective storage class. Amazon S3 provides multiple
[storage
classes](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md") and
[object
lifecycle management](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") to make it straightforward to set up
simple and fine-grained policies to automatically transition data
between storage tiers to reduce costs. Instead of simply storing
data in the S3 standard storage class by default, consider setting
up a lifecycle configuration to transition data between tiers
automatically over time, or use S3 Intelligent-Tiering storage
class for unknown or changing access patterns.

Alternatively, S3 Intelligent-Tiering can cost-effectively and
automatically transition data between tiers and is recommended as
a default storage class since it provides cost optimization
without the need to manually setup lifecycle policies, and is now
the best choice for small and short-lived objects. For more
information, see
[Amazon S3 Intelligent-Tiering – Improved Cost Optimizations for
Short-Lived and Small Objects](https://aws.amazon.com/blogs/aws/amazon-s3-intelligent-tiering-further-automating-cost-savings-for-short-lived-and-small-objects/ "https://aws.amazon.com/blogs/aws/amazon-s3-intelligent-tiering-further-automating-cost-savings-for-short-lived-and-small-objects/").

Common use cases for Amazon S3 include storage of game assets,
static content, game logs, data lake storage, and backups. For use
cases where file systems are required, such as attaching shared
file systems to workstations during development, consider using
[Amazon Elastic File System (Amazon EFS)](../../../AWSEC2/latest/UserGuide/AmazonEFS.md "../../../AWSEC2/latest/UserGuide/AmazonEFS.md"), which provides different
storage classes and automatically grows and shrinks as you add and
remove files with no need for manage the infrastructure.

[Amazon S3 One Zone](../../../AmazonS3/latest/userguide/storage-class-intro.md#sc-infreq-data-access "../../../AmazonS3/latest/userguide/storage-class-intro.md#sc-infreq-data-access")-IA is an ideal storage option for transient
data related to in-game sessions, matchmaking, or other ephemeral
information that can be re-created as needed. That type of game
data does not require redundancy across multiple Availability
Zones (AZs). This lower-cost storage class is well-suited for
records of player actions, game events, and other telemetry data
used for analytics or debugging.

The key cost optimization benefit of using S3 Express One Zone for
such game data is the significant cost savings compared to the
standard S3 storage class, with up to a 20% reduction in storage
costs. This can be particularly advantageous for games with large
volumes of data that do not require the same level of durability
and availability as mission-critical application data. By
leveraging S3 One Zone, game developers and publishers can
optimize their cloud storage costs without compromising the
overall player experience.

### Implementation steps

- Configure Amazon S3 lifecycle policies to transition data
  between storage classes or use S3 Intelligent-Tiering as a
  default for automatic cost optimization with changing access
  patterns.
- Use S3 One Zone-Infrequent Access for transient game session
  data, such as telemetry and matchmaking records, to reduce
  storage costs by up to 20% while maintaining sufficient
  availability.
- For shared file system needs during development, use Amazon EFS to simplify storage management with elastic capacity and
  multiple storage classes.
