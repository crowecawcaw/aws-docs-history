# AWS managed policies for AWS Resource Groups

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

###### AWS-managed policies for Resource Groups

- [ResourceGroupsServiceRolePolicy](#security-iam-awsmanpol-ResourceGroupsServiceRolePolicy "#security-iam-awsmanpol-ResourceGroupsServiceRolePolicy")
- [ResourceGroupsTaggingAPITagUntagSupportedResources](#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources "#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources")
- [ResourceGroupsTaggingAPITagUntagSupportedResources](#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources.title "#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources.title")

## AWS managed policy:

ResourceGroupsServiceRolePolicy

You can't attach `ResourceGroupsServiceRolePolicy` to any IAM entities yourself. This
policy can be attached only to a service-linked role that allows Resource Groups to perform
actions on your behalf. For more information, see [Using service-linked roles for
Resource Groups](security_iam_service-linked-roles.md "security_iam_service-linked-roles.md").

This policy grants the permissions required for Resource Groups to retrieve information about
the resources in your resource groups and any AWS CloudFormation stacks that those resources belong
to. This lets Resource Groups generate CloudWatch Events for the group lifecycle events feature.

To see the latest version of this AWS managed policy, see `ResourceGroupsServiceRolePolicy` in the IAM console.

## AWS managed

policy: ResourceGroupsandTagEditorFullAccess

When you attach a policy to a principal entity, you give the entity permissions that
are defined in the policy. AWS managed policies make it easier for you to assign appropriate permissions to
users, groups, and roles than if you had to write the policies yourself.

This policy grants the permissions required for full access to Resource Groups and Tag Editor
functionality.

To see the latest version of this AWS managed policy, see `ResourceGroupsandTagEditorFullAccess` in the IAM console.

For more information about this policy, see
[ResourceGroupsandTagEditorFullAccess](../../../aws-managed-policy/latest/reference/ResourceGroupsandTagEditorFullAccess.md "../../../aws-managed-policy/latest/reference/ResourceGroupsandTagEditorFullAccess.md")in the _AWS Managed Policy Reference Guide_.

## AWS managed

policy: ResourceGroupsandTagEditorReadOnlyAccess

When you attach a policy to a principal entity, you give the entity permissions that
are defined in the policy. AWS managed policies make it easier for you to assign appropriate permissions to
users, groups, and roles than if you had to write the policies yourself.

This policy grants the permissions required for read only access to Resource Groups and Tag Editor
functionality.

To see the latest version of this AWS managed policy, see `ResourceGroupsandTagEditorReadOnlyAccess` in the IAM console.

For more information about this policy, see
[ResourceGroupsandTagEditorReadOnlyAccess](../../../aws-managed-policy/latest/reference/ResourceGroupsandTagEditorReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/ResourceGroupsandTagEditorReadOnlyAccess.md") in the _AWS Managed Policy Reference Guide_.

## AWS managed

policy: ResourceGroupsTaggingAPITagUntagSupportedResources

When you attach a policy to a principal entity, you give the entity permissions that
are defined in the policy. AWS managed policies make it easier for you to assign appropriate permissions to
users, groups, and roles than if you had to write the policies yourself.

This policy grants the permissions required to tag and untag all of the resource types supported by
AWS Resource Groups Tagging API **except**
`AWS::ApiGateway`, `AWS::CloudFormation`, `AWS::CodeBuild`, and `AWS::ServiceCatalog`. Tagging and untagging these excluded resource types requires additional, service-specific permissions which
allow actions other than tagging and untagging. The following list describes which permissions are required to tag and
untag the resource types excluded from the policy:

- The `AWS::ApiGateway` resource types require the `apigateway:Patch` permission
  on the API Gateway resource, and the tag child resource requires the `apigateway:Put`,
  `apigateway:Get`, `apigateway:Delete` permissions.
- The `AWS::CloudFormation` resource types require the `cloudformation:UpdateStack` and
  `cloudformation:UpdateStackSet` permissions.
- The `AWS::CodeBuild` resource types require the `codebuild:UpdateProject` permission.
- The `AWS::ServiceCatalog` resource types require the `servicecatalog:TagResource`,
  `servicecatalog:UntagResource`, `servicecatalog:UpdatePortfolio`, and
  `servicecatalog:UpdateProduct` permissions.

This policy also grants the permissions required to retrieve all tagged, or previously tagged, resources
through the Resource Groups Tagging API.

To see the latest version of this AWS managed policy, see `ResourceGroupsTaggingAPITagUntagSupportedResources` in the IAM console.

For more information about this policy, see
[ResourceGroupsTaggingAPITagUntagSupportedResources](../../../aws-managed-policy/latest/reference/ResourceGroupsTaggingAPITagUntagSupportedResources.md "../../../aws-managed-policy/latest/reference/ResourceGroupsTaggingAPITagUntagSupportedResources.md") in the _AWS Managed Policy Reference Guide_.

## Resource Groups updates to AWS managed

policies

View details about updates to AWS managed policies for Resource Groups since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the [Resource Groups Document history](doc-history.md "doc-history.md")
page.

| Change                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Date              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| Updated policy — [ResourceGroupsTaggingAPITagUntagSupportedResources](#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources.title "#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources.title") | Resource Groups updated this policy to include permissions for eight new services,<br>including Amazon Application Recovery Controller (ARC) and Amazon VPC Lattice. The following permissions were added to the policy:<br>• `kinesisvideo:TagResource`<br>• `kinesisvideo:UntagResource`<br>• `redshift-serverless:TagResource`<br>• `redshift-serverless:UntagResource`<br>• `route53-recovery-control-config:TagResource`<br>• `route53-recovery-control-config:UntagResource`<br>• `route53-recovery-readiness:TagResource`<br>• `route53-recovery-readiness:UntagResource`<br>• `ssm-contacts:TagResource`<br>• `ssm-contacts:UntagResource`<br>• `ssm-incidents:TagResource`<br>• `ssm-incidents:UntagResource`<br>• `vpc-lattice:TagResource`<br>• `vpc-lattice:UntagResource`<br>• `workspaces-web:TagResource`<br>• `workspaces-web:UntagResource` | December 20, 2024 |
| New policy – [ResourceGroupsTaggingAPITagUntagSupportedResources](#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources.title "#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources.title")     | Resource Groups added a new policy to provide the required permissions to tag and untag all of the resource types supported by<br>AWS Resource Groups Tagging API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | October 11, 2024  |
| Policy update – [ResourceGroupsandTagEditorFullAccess](#security-iam-awsmanpol-ResourceGroupsandTagEditorFullAccess.title "#security-iam-awsmanpol-ResourceGroupsandTagEditorFullAccess.title")                                            | Resource Groups updated a policy to include additional AWS CloudFormation permissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | August 10, 2023   |
| Policy update – [ResourceGroupsandTagEditorReadOnlyAccess](#security-iam-awsmanpol-ResourceGroupsandTagEditorReadOnlyAccess.title "#security-iam-awsmanpol-ResourceGroupsandTagEditorReadOnlyAccess.title")                                | Resource Groups updated a policy to include additional AWS CloudFormation permissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | August 10, 2023   |
| New policy – [ResourceGroupsServiceRolePolicy](#security-iam-awsmanpol-ResourceGroupsServiceRolePolicy.title "#security-iam-awsmanpol-ResourceGroupsServiceRolePolicy.title")                                                              | Resource Groups added a new policy to support its service-linked role.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | November 17, 2022 |
| Resource Groups started tracking changes                                                                                                                                                                                                   | Resource Groups started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | November 17, 2022 |
