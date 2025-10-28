# Tagging AWS Elemental MediaConnect resources

A _tag_ is a custom attribute label that you assign or that AWS assigns to an AWS resource. Each tag has two parts:

- A _tag key_ (for example, `CostCenter`, `Environment`, or `Project`). Tag keys are case
  sensitive.
- An optional field known as a _tag value_ (for example, `111122223333` or `Production`).
  Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.
  Tags help you do the following:

- Identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different
  services to indicate that the resources are related. For example, you could assign the same tag to an AWS Elemental MediaConnect flow that you
  assign to an AWS Elemental MediaLive channel
  output.
- Track your AWS costs. You activate these tags on the AWS Billing and Cost Management dashboard. AWS uses the tags to categorize your costs and deliver a monthly
  cost allocation report to you. For more information, see [Use
  Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.
  The following sections provide more information about tags for AWS Elemental MediaConnect.

###### Topics

- [AWS Elemental MediaConnect resources that support tagging](supported-resources.md "supported-resources.md")
- [Tag naming and usage conventions](tagging-restrictions.md "tagging-restrictions.md")
- [Managing tags](tagging-add-edit-delete.md "tagging-add-edit-delete.md")
