# Use EBS direct APIs to access the contents of an EBS snapshot

You can use the Amazon Elastic Block Store (Amazon EBS) direct APIs to create EBS snapshots, write data directly
to your snapshots, read data on your snapshots, and identify the differences or changes between
two snapshots. If you’re an independent software vendor (ISV) who offers backup services for
Amazon EBS, the EBS direct APIs make it more efficient and cost-effective to track incremental changes
on your EBS volumes through snapshots. This can be done without having to create new volumes
from snapshots, and then use Amazon Elastic Compute Cloud (Amazon EC2) instances to compare the differences.

You can create incremental snapshots directly from data on-premises into EBS volumes and the
cloud to use for quick disaster recovery. With the ability to write and read snapshots, you can
write your on-premises data to an EBS snapshot during a disaster. Then after recovery, you can
restore it back to AWS or on-premises from the snapshot. You no longer need to build and
maintain complex mechanisms to copy data to and from Amazon EBS.

This user guide provides an overview of the elements that make up the EBS direct APIs, and
examples of how to use them effectively. For more information about the actions, data types,
parameters, and errors of the APIs, see the [EBS direct APIs reference](../APIReference.md "../APIReference.md"). For more information about the
supported AWS Regions, endpoints, and service quotas for the EBS direct APIs, see [Amazon EBS endpoints and
quotas](../../../general/latest/gr/ebs-service.md "../../../general/latest/gr/ebs-service.md") in the _AWS General Reference_.

###### Topics

- [Pricing](ebsapi-pricing.md "ebsapi-pricing.md")
- [Concepts](ebsapi-elements.md "ebsapi-elements.md")
- [Control access](ebsapi-permissions.md "ebsapi-permissions.md")
- [Read snapshots](readsnapshots.md "readsnapshots.md")
- [Write snapshots](writesnapshots.md "writesnapshots.md")
- [Encryption outcomes](ebsapis-using-encryption.md "ebsapis-using-encryption.md")
- [Validate snapshot data](ebsapis-using-checksums.md "ebsapis-using-checksums.md")
- [Ensure idempotency](ebs-direct-api-idempotency.md "ebs-direct-api-idempotency.md")
- [Error retries](error-retries.md "error-retries.md")
- [Optimize performance](ebsapi-performance.md "ebsapi-performance.md")
- [Service endpoints](using-endpoints.md "using-endpoints.md")
- [SDK code examples](sdk.md "sdk.md")
- [Interface VPC endpoints](ebs-apis-vpc-endpoints.md "ebs-apis-vpc-endpoints.md")
- [CloudTrail logs](logging-ebs-apis-using-cloudtrail.md "logging-ebs-apis-using-cloudtrail.md")
- [FAQs](ebsapi-faq.md "ebsapi-faq.md")
