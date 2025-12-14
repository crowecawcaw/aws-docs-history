# Security Hub CSPM controls for Amazon SES

These AWS Security Hub CSPM controls evaluate the Amazon Simple Email Service (Amazon SES) service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [SES.1] SES contact lists should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::SES::ContactList`

**AWS Configrule:** `tagged-ses-contactlist` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

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

**AWS Configrule:** `tagged-ses-configurationset` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredTagKeys` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

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

## [SES.3] SES configuration sets should have TLS enabled for sending emails

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::SES::ConfigurationSet`

**AWS Configrule:** `ses-sending-tls-required`

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon SES configuration set requires TLS connections. The control fails if the TLS Policy is not set to `'REQUIRE'` for a configuration set.

By default, Amazon SES uses opportunistic TLS, which means emails can be sent unencrypted if a TLS connection cannot be established with the receiving mail server. Enforcing TLS for email sending ensures that messages are only delivered when a secure encrypted connection can be established.
This helps protect the confidentiality and integrity of email content during transmission between Amazon SES and the recipient's mail server. If a secure TLS connection cannot be established, the message will not be delivered, preventing potential exposure of sensitive information.

###### Note

While TLS 1.3 is the default delivery method for Amazon SES, without enforcing TLS requirement through configuration sets, messages could potentially be delivered in plaintext if a TLS connection fails.
To pass this control, you must configure the TLS Policy to `'REQUIRE'` in your SES configuration set's delivery options. When TLS is required, messages are only delivered if a TLS connection can be established with the receiving mail server.

### Remediation

To configure Amazon SES to require TLS connections for a configuration set, see [Amazon SES and security protocols](../../../ses/latest/dg/security-protocols.md#security-ses-to-receiver "../../../ses/latest/dg/security-protocols.md#security-ses-to-receiver")
in the _Amazon SES Developer Guide_.
