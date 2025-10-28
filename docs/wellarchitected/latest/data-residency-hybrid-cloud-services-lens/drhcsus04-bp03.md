# DRHCSUS04-BP03 Consider sustainable storage options for AWS Outposts

Both Amazon S3 on Outposts and Amazon EBS provide tools for data lifecycle management, the functions of which should be considered in advance when sizing and ordering storage for an AWS Outposts.

**Desired outcome:** Amazon S3 resources deployed on Outposts can be minimized to align with workload demands, not over-provisioned.

**Benefits of establishing this best
practice:** Amazon S3 and Amazon EBS storage sizing can
be minimized through the implementation of data retention and
lifecycle management tools.

**Level of risk exposed if this best
practice is not established:** Medium

##

[Amazon S3 on Outposts](https://aws.amazon.com/s3/outposts/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc "https://aws.amazon.com/s3/outposts/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc") provides object storage on-premises for use with data residency workloads. AWS Outposts have a fixed amount of Amazon EBS and Amazon S3 storage capacity that is pre-configured while ordering. Because capacity can be scaled up or down after deployment, it is recommended that both Amazon EBS and Amazon S3 storage be sized appropriately for your data residency storage requirements, accounting for future needs but not excessively over-provisioned.

When sizing Amazon S3 on Outposts storage before ordering,
consider the potential of using
[Amazon S3 lifecycle polices](../../../AmazonS3/latest/userguide/S3OutpostsLifecycleManaging.md "../../../AmazonS3/latest/userguide/S3OutpostsLifecycleManaging.md") to expire bucket objects, delete
non-current objects, or delete incomplete multi-part uploads to
reduce overall Amazon S3 storage requirements. By managing Amazon S3 buckets and objects to maintain only current or necessary data,
you can improve sustainability by minimizing Outposts storage
resources and power requirements.

Also consider the potential of using
[Amazon Data Lifecycle Manager](https://aws.amazon.com/ebs/data-lifecycle-manager/ "https://aws.amazon.com/ebs/data-lifecycle-manager/") to manage Amazon EBS snapshot and
Amazon EBS-backed AMI retention policies to reduce overall Amazon S3 storage requirements.
