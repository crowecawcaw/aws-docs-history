# Security Hub controls for AWS AppConfig

These Security Hub controls evaluate the AWS AppConfig service and resources.

These controls may not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [AppConfig.1] AWS AppConfig applications should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::AppConfig::Application`

**AWS Config rule:** `appconfig-application-tagged`

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredKeyTags` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           |

This control checks whether an AWS AppConfig application has tags with the specific keys defined in the parameter
`requiredKeyTags`. The control fails if the application doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredKeyTags`. If the parameter `requiredKeyTags` isn't provided, the control only checks for the existence
of a tag key and fails if the application isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[Define permissions based on attributes with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md")
in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Best practices and strategies](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_Tagging AWS Resources and Tag Editor User Guide_.

### Remediation

To add tags to an AWS AppConfig application, see [TagResource](../../../appconfig/2019-10-09/APIReference/API_TagResource.md "../../../appconfig/2019-10-09/APIReference/API_TagResource.md") in the _AWS AppConfig API Reference_.

## [AppConfig.2] AWS AppConfig configuration profiles should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::AppConfig::ConfigurationProfile`

**AWS Config rule:** `appconfig-configuration-profile-tagged`

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredKeyTags` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           |

This control checks whether an AWS AppConfig configuration profile has tags with the specific keys defined in the parameter
`requiredKeyTags`. The control fails if the configuration profile doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredKeyTags`. If the parameter `requiredKeyTags` isn't provided, the control only checks for the existence
of a tag key and fails if the configuration profile isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[Define permissions based on attributes with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md")
in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Best practices and strategies](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_Tagging AWS Resources and Tag Editor User Guide_.

### Remediation

To add tags to an AWS AppConfig configuration profile, see [TagResource](../../../appconfig/2019-10-09/APIReference/API_TagResource.md "../../../appconfig/2019-10-09/APIReference/API_TagResource.md") in the _AWS AppConfig API Reference_.

## [AppConfig.3] AWS AppConfig environments should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::AppConfig::Environment`

**AWS Config rule:** `appconfig-environment-tagged`

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredKeyTags` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           |

This control checks whether an AWS AppConfig environment has tags with the specific keys defined in the parameter
`requiredKeyTags`. The control fails if the environment doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredKeyTags`. If the parameter `requiredKeyTags` isn't provided, the control only checks for the existence
of a tag key and fails if the environment isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[Define permissions based on attributes with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md")
in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Best practices and strategies](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_Tagging AWS Resources and Tag Editor User Guide_.

### Remediation

To add tags to an AWS AppConfig environment, see [TagResource](../../../appconfig/2019-10-09/APIReference/API_TagResource.md "../../../appconfig/2019-10-09/APIReference/API_TagResource.md") in the _AWS AppConfig API Reference_.

## [AppConfig.4] AWS AppConfig extension associations should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::AppConfig::ExtensionAssociation`

**AWS Config rule:** `appconfig-extension-association-tagged`

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `requiredKeyTags` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value           |

This control checks whether an AWS AppConfig extension association has tags with the specific keys defined in the parameter
`requiredKeyTags`. The control fails if the extension association doesn’t have any tag keys or if it doesn’t have all the keys specified in the
parameter `requiredKeyTags`. If the parameter `requiredKeyTags` isn't provided, the control only checks for the existence
of a tag key and fails if the extension association isn't tagged with any key. System tags, which are automatically applied and begin with `aws:`,
are ignored.

A tag is a label that you assign to an AWS resource, and it consists of a key and an optional value. You can create tags to
categorize resources by purpose, owner, environment, or other criteria. Tags can help you identify, organize, search for, and filter resources.
Tagging also helps you track accountable resource owners for actions and notifications. When you use tagging, you can implement attribute-based
access control (ABAC) as an authorization strategy, which defines permissions based on tags. You can attach tags to IAM entities (users or roles)
and to AWS resources. You can create a single ABAC policy or a separate set of policies for your IAM principals. You can design these ABAC
policies to allow operations when the principal's tag matches the resource tag. For more information, see
[Define permissions based on attributes with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md")
in the _IAM User Guide_.

###### Note

Don’t add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible
to many AWS services, including AWS Billing. For more tagging best practices, see
[Best practices and strategies](../../../tag-editor/latest/userguide/tagging.md#tag-best-practices "../../../tag-editor/latest/userguide/tagging.md#tag-best-practices") in the
_Tagging AWS Resources and Tag Editor User Guide_.

### Remediation

To add tags to an AWS AppConfig extension association, see [TagResource](../../../appconfig/2019-10-09/APIReference/API_TagResource.md "../../../appconfig/2019-10-09/APIReference/API_TagResource.md") in the _AWS AppConfig API Reference_.
