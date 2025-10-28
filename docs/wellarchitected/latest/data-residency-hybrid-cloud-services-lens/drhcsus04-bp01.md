# DRHCSUS04-BP01 Consider sustainable object storage options for Local Zones

Amazon S3 Object storage in AWS Regions used by workloads deployed
in AWS Local Zones can be optimized to use the most
energy-efficient and sustainable service tiers, based on data
access and resiliency requirements.

**Desired outcome:** Data and
objects are stored in the lowest cost and most sustainable Amazon S3 service tier based on access profiles.

**Benefits of establishing this best
practice:** The energy and cost efficiency of Amazon S3
object storage will be aligned to the data resiliency and access
requirements.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Although Amazon S3 is not available natively in Local Zones, you
can still use S3 buckets located in AWS Regions to store data
that is not, or is no longer, subject to data residency
policies. When doing so, review the
[Amazon S3 Storage Classes](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md"), and implement
[Amazon S3 storage lifecycle policies](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") to migrate infrequently
accessed data into more sustainable storage Classes such as
[Amazon Glacier](../../../AmazonS3/latest/userguide/glacier-storage-classes.md "../../../AmazonS3/latest/userguide/glacier-storage-classes.md").

This practice not only optimizes storage costs and improves data
management but also reduces energy consumption and environmental
impact through the use of the most energy-efficient storage
technologies.
