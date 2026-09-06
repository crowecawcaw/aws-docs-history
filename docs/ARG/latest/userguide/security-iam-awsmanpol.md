

# AWS managed policies for AWS Resource Groups
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

**AWS-managed policies for Resource Groups**
+ [ResourceGroupsServiceRolePolicy](#security-iam-awsmanpol-ResourceGroupsServiceRolePolicy)
+ [ ResourceGroupsTaggingAPITagUntagSupportedResources](#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources)
+ [ResourceGroupsTaggingAPITagUntagSupportedResources](#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources.title) 

## AWS managed policy: ResourceGroupsServiceRolePolicy
<a name="security-iam-awsmanpol-ResourceGroupsServiceRolePolicy"></a>

You can't attach `ResourceGroupsServiceRolePolicy` to any IAM entities yourself. This policy can be attached only to a service-linked role that allows Resource Groups to perform actions on your behalf. For more information, see [Using service-linked roles for Resource Groups](using-service-linked-roles.md).

This policy grants the permissions required for Resource Groups to retrieve information about the resources in your resource groups and any CloudFormation stacks that those resources belong to. This lets Resource Groups generate CloudWatch Events for the group lifecycle events feature. 

To see the latest version of this AWS managed policy, see `[ResourceGroupsServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsServiceRolePolicy)` in the IAM console.

## AWS managed policy: ResourceGroupsandTagEditorFullAccess
<a name="security-iam-awsmanpol-ResourceGroupsandTagEditorFullAccess"></a>

When you attach a policy to a principal entity, you give the entity permissions that are defined in the policy. AWS managed policies make it easier for you to assign appropriate permissions to users, groups, and roles than if you had to write the policies yourself.

This policy grants the permissions required for full access to Resource Groups and Tag Editor functionality. 

To see the latest version of this AWS managed policy, see `[ResourceGroupsandTagEditorFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess)` in the IAM console.

For more information about this policy, see [ ResourceGroupsandTagEditorFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ResourceGroupsandTagEditorFullAccess.html)in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: ResourceGroupsandTagEditorReadOnlyAccess
<a name="security-iam-awsmanpol-ResourceGroupsandTagEditorReadOnlyAccess"></a>

When you attach a policy to a principal entity, you give the entity permissions that are defined in the policy. AWS managed policies make it easier for you to assign appropriate permissions to users, groups, and roles than if you had to write the policies yourself.

This policy grants the permissions required for read only access to Resource Groups and Tag Editor functionality.

To see the latest version of this AWS managed policy, see `[ResourceGroupsandTagEditorReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorReadOnlyAccess)` in the IAM console.

For more information about this policy, see [ ResourceGroupsandTagEditorReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ResourceGroupsandTagEditorReadOnlyAccess.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: ResourceGroupsTaggingAPITagUntagSupportedResources
<a name="security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources"></a>

When you attach a policy to a principal entity, you give the entity permissions that are defined in the policy. AWS managed policies make it easier for you to assign appropriate permissions to users, groups, and roles than if you had to write the policies yourself.

This policy grants the permissions required to tag and untag all of the resource types supported by AWS Resource Groups Tagging API **except** `AWS::ApiGateway`, `AWS::CloudFormation`, `AWS::CodeBuild`, and `AWS::ServiceCatalog`. Tagging and untagging these excluded resource types requires additional, service-specific permissions which allow actions other than tagging and untagging. The following list describes which permissions are required to tag and untag the resource types excluded from the policy:
+ The `AWS::ApiGateway` resource types require the `apigateway:Patch` permission on the API Gateway resource, and the tag child resource requires the `apigateway:Put`, `apigateway:Get`, `apigateway:Delete` permissions. 
+ The `AWS::CloudFormation` resource types require the `cloudformation:UpdateStack` and `cloudformation:UpdateStackSet` permissions. 
+ The `AWS::CodeBuild` resource types require the `codebuild:UpdateProject` permission. 
+ The `AWS::ServiceCatalog` resource types require the `servicecatalog:TagResource`, `servicecatalog:UntagResource`, `servicecatalog:UpdatePortfolio`, and `servicecatalog:UpdateProduct` permissions. 

This policy also grants the permissions required to retrieve all tagged, or previously tagged, resources through the Resource Groups Tagging API. 

To see the latest version of this AWS managed policy, see `[ ResourceGroupsTaggingAPITagUntagSupportedResources](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsTaggingAPITagUntagSupportedResources)` in the IAM console. 

For more information about this policy, see [ ResourceGroupsTaggingAPITagUntagSupportedResources](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ResourceGroupsTaggingAPITagUntagSupportedResources.html) in the *AWS Managed Policy Reference Guide*. 

## Resource Groups updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Resource Groups since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Resource Groups Document history](doc-history.md) page.


| Change | Description | Date | 
| --- | --- | --- | 
| Updated policy — [ResourceGroupsTaggingAPITagUntagSupportedResources](#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources.title)  | Resource Groups updated this policy to include permissions for eight new services, including Amazon Application Recovery Controller (ARC) and Amazon VPC Lattice. The following permissions were added to the policy:+ `kinesisvideo:TagResource`<br />+ `kinesisvideo:UntagResource`<br />+ `redshift-serverless:TagResource`<br />+ `redshift-serverless:UntagResource`<br />+ `route53-recovery-control-config:TagResource`<br />+ `route53-recovery-control-config:UntagResource`<br />+ `route53-recovery-readiness:TagResource`<br />+ `route53-recovery-readiness:UntagResource`<br />+ `ssm-contacts:TagResource`<br />+ `ssm-contacts:UntagResource`<br />+ `ssm-incidents:TagResource`<br />+ `ssm-incidents:UntagResource`<br />+ `vpc-lattice:TagResource`<br />+ `vpc-lattice:UntagResource`<br />+ `workspaces-web:TagResource`<br />+ `workspaces-web:UntagResource` | December 20, 2024 | 
| New policy – [ResourceGroupsTaggingAPITagUntagSupportedResources](#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources.title)  | Resource Groups added a new policy to provide the required permissions to tag and untag all of the resource types supported by AWS Resource Groups Tagging API.  | October 11, 2024 | 
| Policy update – [ResourceGroupsandTagEditorFullAccess](#security-iam-awsmanpol-ResourceGroupsandTagEditorFullAccess.title)  | Resource Groups updated a policy to include additional AWS CloudFormation permissions. | August 10, 2023 | 
| Policy update – [ResourceGroupsandTagEditorReadOnlyAccess](#security-iam-awsmanpol-ResourceGroupsandTagEditorReadOnlyAccess.title)  | Resource Groups updated a policy to include additional AWS CloudFormation permissions. | August 10, 2023 | 
| New policy – [ResourceGroupsServiceRolePolicy](#security-iam-awsmanpol-ResourceGroupsServiceRolePolicy.title) | Resource Groups added a new policy to support its service-linked role. | November 17, 2022 | 
| Resource Groups started tracking changes | Resource Groups started tracking changes for its AWS managed policies. | November 17, 2022 | 