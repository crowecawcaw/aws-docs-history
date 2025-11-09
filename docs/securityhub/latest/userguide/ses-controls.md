# Security Hub controls for Amazon SES

These AWS Security Hub controls evaluate the Amazon Simple Email Service (Amazon SES) service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [SES.1] SES contact lists should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::SES::ContactList`

**AWS Configrule:** `tagged-ses-contactlist` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           |

This control checks whether an Amazon SES contact list has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the contact list doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the contact list isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to an Amazon SES contact list, see [TagResource](../../../ses/latest/APIReference-V2/API_TagResource.md "../../../ses/latest/APIReference-V2/API_TagResource.md")
in the _Amazon SES API v2 Reference_.

## [SES.2] SES configuration sets should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::SES::ConfigurationSet`

**AWS Configrule:** `tagged-ses-configurationset` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           |

This control checks whether an Amazon SES configuration set has tags with the specific keys defined in the parameter
`requiredTagKeys`. The control fails if the configuration set doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredTagKeys`. If the parameter `requiredTagKeys` isn't provided, the control only checks for the existence
of a tag key and fails if the configuration set isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_AWS General Reference_.

### Remediation

To add tags to an Amazon SES configuration set, see [TagResource](../../../ses/latest/APIReference-V2/API_TagResource.md "../../../ses/latest/APIReference-V2/API_TagResource.md")
in the _Amazon SES API v2 Reference_.
