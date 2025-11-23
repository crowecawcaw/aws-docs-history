# Using identity-based policies (IAM

policies) for Directory Service

This topic provides examples of identity-based policies in which an account
administrator can attach permissions policies to IAM identities (users, groups, and
roles). These examples demonstrate IAM policies in Directory Service. You should modify and create
your own policies to suit your needs and environment.

###### Important

We recommend that you first review the introductory topics that explain the basic
concepts and options available for you to manage access to your Directory Service resources. For
more information, see [Overview of managing access permissions to
your Directory Service resources](IAM_Auth_Access_Overview.md "IAM_Auth_Access_Overview.md").

The sections in this topic cover the following:

- [Permissions required
  to use the Directory Service console](#UsingWithDS_IAM_RequiredPermissions_Console "#UsingWithDS_IAM_RequiredPermissions_Console")
- [AWS managed (predefined)
  policies for Directory Service](#IAM_Auth_Access_ManagedPolicies "#IAM_Auth_Access_ManagedPolicies")
- [Customer managed policy examples](#IAMPolicyExamples_DS "#IAMPolicyExamples_DS")
- [Using tags with IAM
  policies](#using_tags_with_iam_policies "#using_tags_with_iam_policies")
  The following shows an example of a permissions policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDsEc2IamGetRole",
 "Effect": "Allow",
 "Action": [
 "ds:CreateDirectory",
 "ec2:RevokeSecurityGroupIngress",
 "ec2:CreateNetworkInterface",
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeVpcs",
 "ec2:CreateSecurityGroup",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:DeleteSecurityGroup",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeSubnets",
 "iam:GetRole"
 ],
 "Resource": "*"
 },
 {
 "Sid": "WarningAllowsCreatingRolesWithDirSvcPrefix",
 "Effect": "Allow",
 "Action": [
 "iam:CreateRole",
 "iam:PutRolePolicy"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/DirSvc*"
 },
 {
 "Sid": "AllowPassRole",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`Your-Role-Name`",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "cloudwatch.amazonaws.com"
 }
 }
 }
 ]
}`

```

The three statements in the policy grant permissions as follows:

- The first statement grants permission to create an Directory Service directory. Because
  Directory Service doesn't support permissions at the resource level, the policy specifies a
  wildcard character (\*) as the `Resource` value.
- The second statement grants permissions to access IAM actions, so that
  Directory Service can read and create IAM roles on your behalf. The wildcard character (\*)
  at the end of the `Resource` value means that the statement allows
  permission for the IAM actions on any IAM role. To limit this permission to
  a specific role, replace the wildcard character (\*) in the resource ARN with the
  specific role name. For more information, see [IAM Actions](../../../IAM/latest/APIReference/API_Operations.md "../../../IAM/latest/APIReference/API_Operations.md").
- The third statement grants permissions to a specific set of resources in
  Amazon EC2 that are necessary to allow Directory Service to create, configure, and destroy its
  directories. Replace the role ARN with your role. For more information, see
  [Amazon EC2 Actions](../../../AWSEC2/latest/APIReference/API_Operations.md "../../../AWSEC2/latest/APIReference/API_Operations.md").
  You don't see a `Principal` element in the policy, because in an
  identity-based policy you don't specify the principal who gets the permission. When you
  attach the policy to a user, the user is the implicit principal. When you attach a
  permission policy to an IAM role, the principal identified in the role's trust policy
  gets the permissions.

For a table showing all of the Directory Service API actions and the resources that they apply to,
see [Directory Service API permissions: Actions,
resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md "UsingWithDS_IAM_ResourcePermissions.md").

## Permissions required

to use the Directory Service console

For a user to work with the Directory Service console, that user must have permissions listed
in the preceding policy or the permissions granted by the Directory Service Full
Access Role or Directory Service Read Only role, described in [AWS managed (predefined)
policies for Directory Service](#IAM_Auth_Access_ManagedPolicies "#IAM_Auth_Access_ManagedPolicies").

If you create an IAM policy that is more restrictive than the minimum required
permissions, the console won't function as intended for users with that IAM
policy.

## AWS managed (predefined)

policies for Directory Service

AWS addresses many common use cases by providing predefined, or managed, IAM
policies that are created and administered by AWS. Managed policies grant
necessary permissions for common use cases, which helps you decide what permissions
you need. For more information, see [AWS managed policies for AWS Directory Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Customer managed policy examples

In this section, you can find example user policies that grant permissions for
various Directory Service actions.

###### Note

All examples use the US West (Oregon) Region (`us-west-2`) and contain
fictitious account IDs.

###### Examples

- [Example 1: Allow
  a user to perform any Describe action on any Directory Service resource](#IAMPolicyExamples_DS_perform_describe_action "#IAMPolicyExamples_DS_perform_describe_action")
- [Example 2: Allow a user
  to create a directory](#IAMPolicyExamples_DS_create_directory "#IAMPolicyExamples_DS_create_directory")

### Example 1: Allow

a user to perform any Describe action on any Directory Service resource

The following permissions policy grants permissions to a user to run all of
the actions that begin with `Describe` in an AWS Managed Microsoft AD with the
directory ID `d-1234567890` in the AWS account
`111122223333`. These actions show information about an Directory Service
resource, such as a directory or snapshot. Make sure to change the AWS Region
and account number to the region you want to use and your account number.

JSON

```
`{
"Version":"2012-10-17",
 "Statement":[
 {
"Effect":"Allow",
 "Action":"ds:Describe*",
 "Resource": "arn:aws:ds:us-west-2:`111122223333`:directory/`d-1234567890`"
 }
 ]
}`

```

### Example 2: Allow a user

to create a directory

The following permissions policy grants permissions to allow a user to create
a directory and all other related resources, such as snapshots and trusts. In
order to do so, permissions to certain Amazon EC2 services are also required.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:CreateNetworkInterface",
 "ec2:CreateSecurityGroup",
 "ec2:DeleteNetworkInterface",
 "ec2:DeleteSecurityGroup",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupIngress",
 "ec2:CreateTags"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ds:CreateDirectory",
 "ds:DescribeDirectories"
 ],
 "Resource": "arn:aws:ds:*:`111122223333`:*"
 }
 ]
}`

```

## Using tags with IAM

policies

You can apply tag-based resource-level permissions in the IAM policies you use
for most Directory Service API actions. This gives you better control over what resources a user
can create, modify, or use. You use the `Condition` element (also called
the `Condition` block) with the following condition context keys and
values in an IAM policy to control user access (permissions) based on a resource's
tags:

- Use
  `aws`:`ResourceTag`/`tag-key`:
  `tag-value` to allow or deny user actions on
  resources with specific tags.
- Use
  `aws`:`ResourceTag`/`tag-key`:
  `tag-value` to require that a specific tag be used
  (or not used) when making an API request to create or modify a resource that
  allows tags.
- Use `aws`:`TagKeys`:
  [`tag-key`, ...] to require that a specific set of tag
  keys be used (or not used) when making an API request to create or modify a
  resource that allows tags.

###### Note

The condition context keys and values in an IAM policy apply only to those
Directory Service actions where an identifier for a resource capable of being tagged is a
required parameter.

[Controlling
access using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_ has additional information on using tags. The
[IAM
JSON policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") section of that guide has detailed syntax,
descriptions, and examples of the elements, variables, and evaluation logic of JSON
policies in IAM.

The following tag policy allows creating an Directory Service directory as long as the
following tags are used:

- Environment: Production
- Owner: Infrastructure Team
- Cost center: 1234

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ds:CreateDirectory"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Environment": "Production",
 "aws:RequestTag/Owner": "Infrastructure-Team",
 "aws:RequestTag/CostCenter": "12345"
 }
 }
 }
 ]
}`

```

The following tag policy allows updating and deleting Directory Service directories as long as
the following tags are used:

- Project: Atlas
- Department: Engineering
- Environment: Staging

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ds:DeleteDirectory",
 "ds:UpdateDirectory"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Project": "Atlas",
 "aws:ResourceTag/Department": "Engineering",
 "aws:ResourceTag/Environment": "Staging"
 }
 }
 }
 ]
}`

```

The following tag policy denies resource tagging for Directory Service where the resource has
one of the following tags:

- Production
- Security
- Confidential

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "ds:AddTagsToResource"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": ["Production", "Security", "Confidential"]
 }
 }
 }
 ]
}`

```

For more information about ARNs, see [Amazon
Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

The following list of Directory Service API operations support tag-based resource-level
permissions:

- [AcceptSharedDirectory](../devguide/API_AcceptSharedDirectory.md "../devguide/API_AcceptSharedDirectory.md")
- [AddIpRoutes](../devguide/API_AddIpRoutes.md "../devguide/API_AddIpRoutes.md")
- [AddTagsToResource](../devguide/API_AddTagsToResource.md "../devguide/API_AddTagsToResource.md")
- [CancelSchemaExtension](../devguide/API_CancelSchemaExtension.md "../devguide/API_CancelSchemaExtension.md")
- [CreateAlias](../devguide/API_CreateAlias.md "../devguide/API_CreateAlias.md")
- [CreateComputer](../devguide/API_CreateComputer.md "../devguide/API_CreateComputer.md")
- [CreateConditionalForwarder](../devguide/API_CreateConditionalForwarder.md "../devguide/API_CreateConditionalForwarder.md")
- [CreateSnapshot](../devguide/API_CreateSnapshot.md "../devguide/API_CreateSnapshot.md")
- [CreateLogSubscription](../devguide/API_CreateLogSubscription.md "../devguide/API_CreateLogSubscription.md")
- [CreateTrust](../devguide/API_CreateTrust.md "../devguide/API_CreateTrust.md")
- [DeleteConditionalForwarder](../devguide/API_DeleteConditionalForwarder.md "../devguide/API_DeleteConditionalForwarder.md")
- [DeleteDirectory](../devguide/API_DeleteDirectory.md "../devguide/API_DeleteDirectory.md")
- [DeleteLogSubscription](../devguide/API_DeleteLogSubscription.md "../devguide/API_DeleteLogSubscription.md")
- [DeleteSnapshot](../devguide/API_DeleteSnapshot.md "../devguide/API_DeleteSnapshot.md")
- [DeleteTrust](../devguide/API_DeleteTrust.md "../devguide/API_DeleteTrust.md")
- [DeregisterEventTopic](../devguide/API_DeregisterEventTopic.md "../devguide/API_DeregisterEventTopic.md")
- [DescribeConditionalForwarders](../devguide/API_DescribeConditionalForwarders.md "../devguide/API_DescribeConditionalForwarders.md")
- [DescribeDomainControllers](../devguide/API_DescribeDomainControllers.md "../devguide/API_DescribeDomainControllers.md")
- [DescribeEventTopics](../devguide/API_DescribeEventTopics.md "../devguide/API_DescribeEventTopics.md")
- [DescribeSharedDirectories](../devguide/API_DescribeSharedDirectories.md "../devguide/API_DescribeSharedDirectories.md")
- [DescribeSnapshots](../devguide/API_DescribeSnapshots.md "../devguide/API_DescribeSnapshots.md")
- [DescribeTrusts](../devguide/API_DescribeTrusts.md "../devguide/API_DescribeTrusts.md")
- [DisableRadius](../devguide/API_DisableRadius.md "../devguide/API_DisableRadius.md")
- [DisableSso](../devguide/API_DisableSso.md "../devguide/API_DisableSso.md")
- [EnableRadius](../devguide/API_EnableRadius.md "../devguide/API_EnableRadius.md")
- [EnableSso](../devguide/API_EnableSso.md "../devguide/API_EnableSso.md")
- [GetSnapshotLimits](../devguide/API_GetSnapshotLimits.md "../devguide/API_GetSnapshotLimits.md")
- [ListIpRoutes](../devguide/API_ListIpRoutes.md "../devguide/API_ListIpRoutes.md")
- [ListSchemaExtensions](../devguide/API_ListSchemaExtensions.md "../devguide/API_ListSchemaExtensions.md")
- [ListTagsForResource](../devguide/API_ListTagsForResource.md "../devguide/API_ListTagsForResource.md")
- [RegisterEventTopic](../devguide/API_RegisterEventTopic.md "../devguide/API_RegisterEventTopic.md")
- [RejectSharedDirectory](../devguide/API_RejectSharedDirectory.md "../devguide/API_RejectSharedDirectory.md")
- [RemoveIpRoutes](../devguide/API_RemoveIpRoutes.md "../devguide/API_RemoveIpRoutes.md")
- [RemoveTagsFromResource](../devguide/API_RemoveTagsFromResource.md "../devguide/API_RemoveTagsFromResource.md")
- [ResetUserPassword](../devguide/API_ResetUserPassword.md "../devguide/API_ResetUserPassword.md")
- [RestoreFromSnapshot](../devguide/API_RestoreFromSnapshot.md "../devguide/API_RestoreFromSnapshot.md")
- [ShareDirectory](../devguide/API_ShareDirectory.md "../devguide/API_ShareDirectory.md")
- [StartSchemaExtension](../devguide/API_StartSchemaExtension.md "../devguide/API_StartSchemaExtension.md")
- [UnshareDirectory](../devguide/API_UnshareDirectory.md "../devguide/API_UnshareDirectory.md")
- [UpdateConditionalForwarder](../devguide/API_UpdateConditionalForwarder.md "../devguide/API_UpdateConditionalForwarder.md")
- [UpdateNumberOfDomainControllers](../devguide/API_UpdateNumberOfDomainControllers.md "../devguide/API_UpdateNumberOfDomainControllers.md")
- [UpdateRadius](../devguide/API_UpdateRadius.md "../devguide/API_UpdateRadius.md")
- [UpdateTrust](../devguide/API_UpdateTrust.md "../devguide/API_UpdateTrust.md")
- [VerifyTrust](../devguide/API_VerifyTrust.md "../devguide/API_VerifyTrust.md")
