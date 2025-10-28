# Managing Service Quotas resources with tags

You can use tags to categorize resources by purpose, owner, environment, or other
criteria. A _tag_ is a custom attribute label that you add to an AWS resource
to make it easier to identify, organize, and search for resources. Each tag includes two
parts:

- A **tag key**, such as `CostCenter`,
  `Environment`, or `Project`. Tag keys are case
  sensitive.
- A **tag value**, such as `111122223333` or
  `Production`. You can set the value of a tag to an empty string, but
  you can't set the value of a tag to null. Omitting the tag value is the same as
  using an empty string. Like tag keys, tag values are case sensitive.
  Tags help you do the following:

- Identify and organize your AWS resources. Many services support tagging, so you
  can assign the same tag to resources from different services to indicate that the
  resources are related.
- Track your AWS costs. You activate these tags on the AWS Billing and Cost Management dashboard. AWS
  uses the tags to categorize your costs and deliver a monthly cost allocation report
  to you. For more information, see [Use
  cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the [AWS Billing User Guide](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md").
- Control access to your AWS resources. For more information, see [Controlling access using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in
  the _[IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md")_.

###### Topics

- [Service Quotas resources that support tagging](#sq-supported-resources "#sq-supported-resources")
- [Tag restrictions](#sq-tagging-restrictions "#sq-tagging-restrictions")
- [Enabling the required permissions for tagging Service Quotas
  resources](sq_tags_permissions.md "sq_tags_permissions.md")
- [Managing Service Quotas tags](sq_tags_managing-console.md "sq_tags_managing-console.md")
- [Controlling access using Service Quotas tags](sq_tags_access.md "sq_tags_access.md")

## Service Quotas resources that support tagging

Service Quotas supports tagging the **Applied quotas** resource. An applied quota
is a quota that you requested an increase for, _and_ the increase was approved by Support.

###### Important

You can only tag quotas if they have an applied quota value. Quotas with default
quota values cannot be tagged.

Do not store personally identifiable information (PII) or other confidential or
sensitive information in tags. Tags are not intended to be used for private or
sensitive data.

## Tag restrictions

Restrictions apply to tags on Service Quotas resources, including:

- Maximum number of tags that you can assign to a resource – 50
- Maximum tag key length – 128 Unicode characters
- Maximum tag value length – 256 Unicode characters
- Valid characters for tag key and value – a-z, A-Z, 0-9, space, and the
  following characters: \_ . : / = + - and @
- Tag keys and values are case sensitive.
- Don't use `aws:` as a prefix for tag keys. It is reserved for AWS
  use.
