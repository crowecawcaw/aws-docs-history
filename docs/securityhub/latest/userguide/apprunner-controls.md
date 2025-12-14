# Security Hub CSPM controls for AWS App Runner

These AWS Security Hub CSPM controls evaluate the AWS App Runner service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [AppRunner.1] App Runner services should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::AppRunner::Service`

**AWS Config rule:** [apprunner-service-tagged](../../../config/latest/developerguide/apprunner-service-tagged.md "../../../config/latest/developerguide/apprunner-service-tagged.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredKeyTags` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an AWS App Runner service has tags with the specific keys
defined in the parameter `requiredKeyTags`. The control fails if the
App Runner service doesn’t have any tag keys or if it doesn’t have all the keys specified in
the parameter `requiredKeyTags`. If the parameter
`requiredKeyTags` isn't provided, the control only checks for the
existence of a tag key and fails if the App Runner service isn't tagged with any key. System
tags, which are automatically applied and begin with `aws:`, are
ignored.

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

For information about adding tags to an AWS App Runner service, see [TagResource](../../../apprunner/latest/api/API_TagResource.md "../../../apprunner/latest/api/API_TagResource.md") in the _AWS App Runner API
Reference_.

## [AppRunner.2] App Runner VPC connectors should be tagged

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:**
`AWS::AppRunner::VpcConnector`

**AWS Config rule:**
[apprunner-vpc-connector-tagged](../../../config/latest/developerguide/apprunner-vpc-connector-tagged.md "../../../config/latest/developerguide/apprunner-vpc-connector-tagged.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter         | Description                                                                                        | Type                            | Allowed custom values                                                                                                                                                         | Security Hub CSPM default value |
| ----------------- | -------------------------------------------------------------------------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `requiredKeyTags` | List of non-system tag keys that the evaluated resource must contain. Tag keys are case sensitive. | StringList (maximum of 6 items) | 1–6 tag keys that meet [AWS requirements](../../../tag-editor/latest/userguide/tagging.md#tag-conventions "../../../tag-editor/latest/userguide/tagging.md#tag-conventions"). | No default value                |

This control checks whether an AWS App Runner VPC connector has tags with the specific keys
defined in the parameter `requiredKeyTags`. The control fails if the
VPC connector doesn’t have any tag keys or if it doesn’t have all the keys specified in
the parameter `requiredKeyTags`. If the parameter
`requiredKeyTags` isn't provided, the control only checks for the
existence of a tag key and fails if the VPC connector isn't tagged with any key. System
tags, which are automatically applied and begin with `aws:`, are
ignored.

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

For information about adding tags to an AWS App Runner VPC connector, see [TagResource](../../../apprunner/latest/api/API_TagResource.md "../../../apprunner/latest/api/API_TagResource.md") in the _AWS App Runner API
Reference_.
