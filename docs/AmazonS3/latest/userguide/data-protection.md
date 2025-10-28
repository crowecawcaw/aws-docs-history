# Data protection in Amazon S3

In addition to the resilience offered by the AWS global infrastructure, Amazon S3 offers a
number of features to help protect your data against accidental deletions or Regional
failures.

**S3 Replication**

You can use live replication to enable automatic, asynchronous copying of
objects across Amazon S3 buckets. Buckets that are configured for object replication
can be owned by the same AWS account or by different accounts. You can
replicate objects to a single destination bucket or to multiple destination
buckets. The destination buckets can be in different AWS Regions or within the
same Region as the source bucket. To enable failover controls, you can configure
replication to be two-way (bidirectional) so that your source and destination
buckets can be kept in sync during a Regional failure. For more information, see
[Replicating objects within and across Regions](replication.md "replication.md").

**Multi-Region Access Points and failover controls**

Amazon S3 Multi-Region Access Points provide a global endpoint that applications can use to fulfill
requests from S3 buckets that are located in multiple AWS Regions. You can use
Multi-Region Access Points to build multi-Region applications with the same architecture that's
used in a single Region, and then run those applications anywhere in the world.
Instead of sending requests over the congested public internet, Multi-Region Access Points provide
built-in network resilience with acceleration of internet-based requests to
Amazon S3. Application requests made to a Multi-Region Access Point global endpoint use [AWS Global Accelerator](../../../global-accelerator/latest/dg.md "../../../global-accelerator/latest/dg.md") to automatically route over the AWS
global network to the closest-proximity S3 bucket with an active routing status.
For more information about Multi-Region Access Points, see [Managing multi-Region traffic with Multi-Region Access Points](MultiRegionAccessPoints.md "MultiRegionAccessPoints.md").

With Amazon S3 Multi-Region Access Point failover controls, you can maintain business continuity
during Regional traffic disruptions, while also giving your applications a
multi-Region architecture to fulfill compliance and redundancy needs. If your
Regional traffic gets disrupted, you can use Multi-Region Access Point failover controls to select
which AWS Regions behind an Amazon S3 Multi-Region Access Point will process data-access and storage
requests.

To support failover, you can set up your Multi-Region Access Point in an active-passive
configuration, with traffic flowing to the active Region during normal
conditions, and a passive Region on standby for failover. If you have S3
Cross-Region Replication (CRR) enabled with two-way replication rules, you
can keep your buckets synchronized during a failover. For more information
about failover controls, see [Amazon S3 Multi-Region Access Points failover controls](MrapFailover.md "MrapFailover.md").

**S3 Versioning**

Versioning is a means of keeping multiple variants of an object in the same bucket. You can
use versioning to preserve, retrieve, and restore every version of every object
stored in your Amazon S3 bucket. With versioning, you can easily recover from both
unintended user actions and application failures. For more information, see
[Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").

**S3 Object Lock**

You can use S3 Object Lock to store objects using a _write once, read
many_ (WORM) model. Using S3 Object Lock, you can prevent an
object from being deleted or overwritten for a fixed amount of time or
indefinitely. S3 Object Lock enables you to meet regulatory requirements that
require WORM storage or simply to add an additional layer of protection against
object changes and deletion. For more information, see [Locking objects with Object Lock](object-lock.md "object-lock.md").

**AWS Backup**

Amazon S3 is natively integrated with AWS Backup, a fully managed, policy-based service
that you can use to centrally define backup policies to protect your data in
Amazon S3. After you define your backup policies and assign Amazon S3 resources to the
policies, AWS Backup automates the creation of Amazon S3 backups and securely stores the
backups in an encrypted backup vault that you designate in your backup plan. For
more information, see [Backing up your Amazon S3 data](backup-for-s3.md "backup-for-s3.md").

For a tutorial on using some of these features together to protect your data, see [Tutorial: Protecting data on Amazon S3 against accidental deletion or application bugs using
S3 Versioning, S3 Object Lock, and S3 Replication](https://aws.amazon.com/getting-started/hands-on/protect-data-on-amazon-s3/?ref=docs_gateway/amazons3/DataDurability.html "https://aws.amazon.com/getting-started/hands-on/protect-data-on-amazon-s3/?ref=docs_gateway/amazons3/DataDurability.html").

###### Important

In addition to using the preceding features to protect your data, we recommend reviewing
the recommendations in [Security best practices for Amazon S3](security-best-practices.md "security-best-practices.md").

###### Topics

- [Replicating objects within and across Regions](replication.md "replication.md")
- [Managing multi-Region traffic with Multi-Region Access Points](MultiRegionAccessPoints.md "MultiRegionAccessPoints.md")
- [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md")
- [Locking objects with Object Lock](object-lock.md "object-lock.md")
- [Backing up your Amazon S3 data](backup-for-s3.md "backup-for-s3.md")
