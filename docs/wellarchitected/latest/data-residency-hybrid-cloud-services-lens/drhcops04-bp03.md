# DRHCOPS04-BP03 Review the available data storage options for Local Zones and Outposts to build architectures that keep data within required geographic boundaries

Thoroughly understand the applicable data laws and regulations for
your specific workloads (as per DRHCOPS01).

Be aware that while Outposts and Local Zones allow data processing closer to users, they may still be across geographic borders from the connected AWS Availability Zone or Region.
Account for the fact that logging, monitoring, and snapshot data may be transferred back to the AWS Region, which could have cross-border data transfer implications.

**Desired outcome**: Evaluate and
select appropriate data storage solutions for Local Zones and
Outposts that store data within specified geographic boundaries,
adhering to data residency and compliance mandates.

**Benefits of establishing this best
practice:** Using the right data storage options for
Local Zones and Outposts helps organizations maintain control over
their data's physical location, verifying that they comply with
regional regulations and internal policies and benefit from the
low-latency and local processing capabilities of these AWS
offerings.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Review preferred storage options for Outposts, including
instance storage like Amazon Elastic Block Store (Amazon EBS) or
Amazon Simple Storage Service (Amazon S3) on Outposts. For
Amazon S3 on Outposts, use Amazon S3 versioning or Amazon S3
replication.

Preferred storage options for Local Zones might include landing
zone controls. For more information, see
[Best
Practices for managing data residency in AWS Local Zones using
landing zone controls](https://aws.amazon.com/blogs/compute/best-practices-for-managing-data-residency-in-aws-local-zones-using-landing-zone-controls/ "https://aws.amazon.com/blogs/compute/best-practices-for-managing-data-residency-in-aws-local-zones-using-landing-zone-controls/").
