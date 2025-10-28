# Tagging AWS Network Firewall resources

A _tag_ is a custom attribute label that you assign or that AWS assigns to an AWS resource. Each tag has two parts:

- A _tag key_, for example `CostCenter`, `Environment`, or `Project`. Tag keys are case
  sensitive.
- An optional _tag value_, for example, `111122223333` or `Production`.
  Omitting the tag value is the same as using an empty string. Tag values are case sensitive.
  You can use tags to do the following:

- Identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different
  services to indicate that the resources are related. For example, you could
  assign the same tag to an Amazon Virtual Private Cloud VPC that you
  assign to an firewall and firewall policy in AWS Network Firewall.
- Track your AWS costs. To do this, you activate tags on the AWS Billing and Cost Management dashboard. AWS uses the tags to categorize your costs and deliver a monthly
  cost allocation report to you. For more information, see [Use
  cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.
  The following sections provide more information about tags for AWS Network Firewall.

## Supported resources in Network Firewall

The following resources in Network Firewall support tagging:

- Firewalls
- Firewall policies
- Rule groups

For information about adding and managing tags, see [Managing tags](#tagging-add-edit-delete "#tagging-add-edit-delete").

## Tag naming and usage conventions

The following basic naming and usage conventions apply to using tags with Network Firewall resources:

- Each resource can have a maximum of 50 tags.
- For each resource, each tag key must be unique, and each tag key can have only one value.
- The maximum tag key length is 128 Unicode characters in UTF-8.
- The maximum tag value length is 256 Unicode characters in UTF-8.
- Allowed characters are letters, numbers, spaces representable in UTF-8, and the following characters: **_. : + = @ \_ / -_** (hyphen). Amazon EC2 resources allow any characters.
- Tag keys and values are case sensitive. As a best practice, decide on a strategy for capitalizing tags, and consistently implement that
  strategy across all resource types. For example, decide whether to use `Costcenter`, `costcenter`, or
  `CostCenter`, and use the same convention for all tags. Avoid using similar tags with inconsistent case treatment.
- The `aws:` prefix is prohibited for tags; it's reserved for AWS use. You can't edit or delete tag keys or values with this
  prefix. Tags with this prefix do not count against your tags per resource quota.

## Managing tags

For ease of use and best results, use the Tag Editor in the AWS Resource Groups console. It
provides a central, unified way to create and manage your tags. For more information,
see [Working
with Tag Editor](../../../awsconsolehelpdocs/latest/gsg/tag-editor.md "../../../awsconsolehelpdocs/latest/gsg/tag-editor.md").

You can also use AWS Network Firewall to apply tags while you are creating
and managing your Network Firewall firewalls, firewall policies, and rule groups.
