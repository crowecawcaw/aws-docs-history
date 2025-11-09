# Recover deleted Amazon EBS snapshots and EBS-backed AMIs with Recycle Bin

Recycle Bin is a data recovery feature that enables you to restore accidentally
deleted Amazon EBS snapshots and EBS-backed AMIs. When using Recycle Bin, if your resources are deleted, they are
retained in the Recycle Bin for a time period that you specify before being permanently deleted.

You can restore a resource from the Recycle Bin at any time before its retention period expires.
After you restore a resource from the Recycle Bin, the resource is removed from the Recycle Bin and
you can use it in the same way that you use any other resource of that type in your account. If the retention
period expires and the resource is not restored, the resource is permanently deleted from the Recycle Bin
and it is no longer available for recovery.

Using Recycle Bin helps to ensure business continuity by protecting your business-critical
data against accidental deletion.

Recycle Bin is assessed as a service capability of Amazon Elastic Block Store (Amazon EBS). Any [AWS services in Scope by Compliance](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/")
Program (FedRAMP, HIPAA BAA, SOC, etc) which lists Amazon EBS will also apply to Recycle Bin.

###### Topics

- [Supported resources](#supported-resources "#supported-resources")
- [How does it work?](recycle-bin-concepts.md "recycle-bin-concepts.md")
- [Considerations](recycle-bin-factors.md "recycle-bin-factors.md")
- [Quotas](#recycle-bin-quotas "#recycle-bin-quotas")
- [Related services](#recycle-bin-integrations "#recycle-bin-integrations")
- [Pricing](#recycle-bin-pricing "#recycle-bin-pricing")
- [Control access](recycle-bin-perms.md "recycle-bin-perms.md")
- [Create retention rule](recycle-bin-create-rule.md "recycle-bin-create-rule.md")
- [Update retention rule](recycle-bin-update-rule.md "recycle-bin-update-rule.md")
- [Lock retention rule](recycle-bin-lock.md "recycle-bin-lock.md")
- [Unlock retention rule](recycle-bin-unlock.md "recycle-bin-unlock.md")
- [Tag retention rules](recycle-bin-tag-resource.md "recycle-bin-tag-resource.md")
- [Delete retention rules](recycle-bin-delete-rule.md "recycle-bin-delete-rule.md")
- [Recover deleted snapshots](recycle-bin-working-with-snaps.md "recycle-bin-working-with-snaps.md")
- [Recover deleted AMIs](recycle-bin-working-with-amis.md "recycle-bin-working-with-amis.md")
- [Monitor using EventBridge](rbin-eventbridge.md "rbin-eventbridge.md")
- [Monitor using CloudTrail](recycle-bin-ct.md "recycle-bin-ct.md")
- [Service endpoints](rbin-service-endpoints.md "rbin-service-endpoints.md")
- [Use interface VPC endpoints](rbin-vpcendpoints.md "rbin-vpcendpoints.md")

## Supported resources

Recycle Bin supports the following resource types:

- Amazon EBS snapshots

###### Important

Recycle Bin retention rules also apply to archived snapshots in the archive storage
tier. If you delete an archived snapshot that matches a retention rule, that snapshot is
retained in the Recycle Bin for the period defined in the retention rule. Archived
snapshots are billed at the rate for archived snapshots while they are in the Recycle Bin.

- Amazon EBS-backed Amazon Machine Images (AMIs)

###### Note

Retention rules also apply to disabled AMIs.

## Quotas

The following quotas apply to Recycle Bin.

| Quota                                      | Default quota |
| ------------------------------------------ | ------------- |
| Retention rules per Region                 | 250           |
| Tag key and value pairs per retention rule | 50            |

## Related services

Recycle Bin works with the following services:

- **AWS CloudTrail** — Enables you to record events
  that occur in Recycle Bin. For more information, see [Monitor Recycle Bin using AWS CloudTrail](recycle-bin-ct.md "recycle-bin-ct.md").

## Pricing

There are no additional charges for using Recycle Bin and retention rules. For more
information, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").

- **Amazon EBS snapshots** — Snapshots
  in the Recycle Bin are billed at the same rate as regular snapshots
  in your account.
- **EBS-backed AMIs** — AMIs in the
  Recycle Bin do not incur any additional charges.

###### Note

Some resources might still appear in the Recycle Bin console or in the AWS CLI and
API output for a short period after their retention periods have expired and they
have been permanently deleted. You are not billed for these resources. Billing stops
as soon as the retention period expires.

You can use the following AWS generated cost allocation tags for cost tracking and
allocation purposes when using AWS Billing and Cost Management.

- Key: `aws:recycle-bin:resource-in-bin`
- Value: `true`

For more information, see [AWS-generated cost
allocation tags](../../../awsaccountbilling/latest/aboutv2/aws-tags.md "../../../awsaccountbilling/latest/aboutv2/aws-tags.md") in the _AWS Billing and Cost Management User Guide_.
