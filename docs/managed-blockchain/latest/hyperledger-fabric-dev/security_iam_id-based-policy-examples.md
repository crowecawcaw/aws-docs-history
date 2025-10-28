# Amazon Managed Blockchain (AMB) Hyperledger Fabric Identity-Based

Policy Examples

By default, IAM users and roles don't have permission to create or modify
AMB Access Hyperledger Fabric resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS API. An IAM administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the specified resources they need. The
administrator must then attach those policies to the IAM users or groups that require
those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy Best
  Practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Allow Users
  to View Their Own Permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Using the
  AMB Access Hyperledger Fabric Console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Performing All AMB Access Actions on All Accessible Networks for an AWS Account](#security_iam_id-based-policy-examples-access-one-bucket "#security_iam_id-based-policy-examples-access-one-bucket")
- [Controlling access using tags](#security_iam_id-based-policy-examples-tags "#security_iam_id-based-policy-examples-tags")

## Policy Best

Practices

Identity-based policies determine whether someone can create, access, or delete AMB Access Hyperledger Fabric resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Allow Users

to View Their Own Permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Using the

AMB Access Hyperledger Fabric Console

To access the Amazon Managed Blockchain (AMB) Hyperledger Fabric console, you must have a minimum set of
permissions. These permissions must allow you to list and view details about the
AMB Access Hyperledger Fabric resources in your AWS account. If you create an identity-based policy
that is more restrictive than the minimum required permissions, the console won't
function as intended for entities (IAM users or roles) with that policy.

To ensure that those entities can still use the AMB Access Hyperledger Fabric console, also attach
the following AWS managed policy to the entities.

```
AmazonManagedBlockchainConsoleFullAccess
```

For more information, see [Adding Permissions to a User](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that you're trying to perform.

## Performing All AMB Access Actions on All Accessible Networks for an AWS Account

The following example shows you how to grant an IAM user in AWS account `123456789012`access to
all the network and member resources in the account in the `us-east-1` Region. This example shows how the user
is permitted to list and create; manage networks, proposals, members, and nodes; and reject invitations to join
other networks.

###### Note

- `Deny` and `Allow` actions on a resource (for example `Network`) only affect actions
  on the resource itself and _do not_ apply to child resources such as `Member` and
  `Node`.
- Child resources (such as nodes, members and invitations) must have AWS account ids in their policy
  so they can be enforced as shown in the following example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "ManageNetworkResources",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:CreateNetwork",
 "managedblockchain:GetNetwork",
 "managedblockchain:CreateProposal",
 "managedblockchain:ListProposals",
 "managedblockchain:CreateMember",
 "managedblockchain:ListMembers"
 ],
 "Resource": [
 "arn:aws:managedblockchain:`us-east-1`::networks/`*`"
 ]
 },

 {
 "Sid": "ManageMemberResources",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:GetMember",
 "managedblockchain:DeleteMember",
 "managedblockchain:CreateNode",
 "managedblockchain:ListNodes"
 ],
 "Resource": [
 "arn:aws:managedblockchain:`us-east-1`:`123456789012`:members/`*`"
 ]
 },

 {
 "Sid": "ManageNodeResources",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:GetNode",
 "managedblockchain:DeleteNode",
 "managedblockchain:UpdateNode"
 ],
 "Resource": [
 "arn:aws:managedblockchain:`us-east-1`:`123456789012`:nodes/`*`"
 ]
 },

 {
 "Sid": "ManageProposalResources",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:GetProposal",
 "managedblockchain:ListProposalVotes",
 "managedblockchain:VoteOnProposal"
 ],
 "Resource": [
 "arn:aws:managedblockchain:`us-east-1`::proposals/`*`"
 ]
 },

 {
 "Sid": "ManageInvitationResources",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:RejectInvitation"
 ],
 "Resource": [
 "arn:aws:managedblockchain:`us-east-1`:`123456789012`:invitations/`*`"
 ]
 }
 ]
}`

```

## Controlling access using tags

The following example policy statements demonstrate how you can use tags to limit access to AMB Access Hyperledger Fabric resources and actions performed on those resources.

To tag resources during creation, policy statements that allow the create action for the resource as well as the `TagResource` action must be attached to the IAM principal performing the operation.

###### Note

This topic includes examples of policy statements with a `Deny` effect.
Each policy statement assumes that a statement with a broader `Allow`
effect for the same actions exists; the `Deny` policy statement
restricts that otherwise overly-permissive allow statement.

###### Example – Require a tag key with either of two values to be added during network creation

The following identity-based policy statements allow the IAM principal to create a network only if the network is created with the tags specified.

The statement with the `Sid` set to `RequireTag` specifies that network creation is allowed only if the network is created with a tag that has a tag key of `department` and a value of either `sales` or `marketing`; otherwise, the create network operation fails.

The statement with `Sid` set to `AllowTagging` allows the IAM principal to tag networks, which are not associated with an AWS account ID. It also allows tagging of members in the specified AWS account, `111122223333`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RequireTag",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:CreateNetwork"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringLike": {
 "aws:RequestTag/department": [
 "sales",
 "marketing"
 ]
 }
 }
 },
 {
 "Sid": "AllowTagging",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:TagResource"
 ],
 "Resource": [
 "arn:aws:managedblockchain:us-east-1::networks/*",
 "arn:aws:managedblockchain:us-east-1:`111122223333`:members/*"
 ]
 }
 ]
}`

```

###### Example – Deny access to networks that have a specific tag key

The following identity-based policy statement denies the IAM principal the ability to retrieve or view information for networks that have a tag with a tag key of `restricted`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyRestrictedNetwork",
 "Effect": "Deny",
 "Action": [
 "managedblockchain:GetNetwork"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/restricted": [
 "*"
 ]
 }
 }
 }
 ]
}`

```

###### Example – Deny member creation for networks with a specific tag key and value

The following identity-based policy statement denies the IAM principal from creating a member on any network that has a tag with a tag key of `department` with the value of `accounting`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyMemberCreation",
 "Effect": "Deny",
 "Action": [
 "managedblockchain:CreateMember"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/department": "accounting"
 }
 }
 }
 ]
}`

```

###### Example – Allow member creation only if a specific tag key and value are added

The following identity-based policy statements allow the IAM principal to create members in the account `111122223333` only if the member is created with a tag that has the tag key of `department` and a tag value of `accounting`; otherwise, the create member operation fails.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RestrictMemberCreation",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:CreateMember"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/department": "accounting"
 }
 }
 },
 {
 "Sid": "AllowTaggingOfMembers",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:TagResource"
 ],
 "Resource": [
 "arn:aws:managedblockchain:us-east-1:`111122223333`:members/*"
 ]
 }
 ]
}`

```

###### Example – Allow access only to members that have a specified tag key

The following identity-based policy statement allows the IAM principal to retrieve or view information about members only if the member has a tag with a tag key of `unrestricted`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:GetMember"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/unrestricted": [
 "*"
 ]
 }
 }
 }
 ]
}`

```

###### Example – Deny node creation if a specific tag key and value are added during creation

The following identity-based policy statement denies the IAM principal the ability to create a node if a tag with the tag key of `department` and a value of `analytics` is added during creation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyCreateNodeWithTag",
 "Effect": "Deny",
 "Action": [
 "managedblockchain:CreateNode"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/department": [
 "analytics"
 ]
 }
 }
 }
 ]
}`

```

###### Example – Deny node creation for members with a specific tag key and value

The following identity-based policy statement denies the IAM principal the ability to create a node if the member to which the node will belong has a tag with a tag key of `department` and a tag value of `analytics`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyCreateNodeForTaggedMember",
 "Effect": "Deny",
 "Action": [
 "managedblockchain:CreateNode"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/department": [
 "analytics"
 ]
 }
 }
 }
 ]
}`

```

###### Example – Allow access only to nodes with a specific tag key and value

The following identity-based policy statement allows the IAM principal to retrieve or view information about nodes only if the node has a tag with a tag key of `department` and a tag value of `sales`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowTaggedNodeAccess",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:GetNode"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/department": [
 "sales"
 ]
 }
 }
 }
 ]
}`

```

###### Example – Deny access to nodes with a specific tag key

The following identity-based policy statement denies the IAM principal the ability to retrieve or view information about a node if the node has a tag with a tag key of `restricted`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyAccessToTaggedNodes",
 "Effect": "Deny",
 "Action": [
 "managedblockchain:GetNode"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/restricted": [
 "*"
 ]
 }
 }
 }
 ]
}`

```

###### Example – Allow proposal creation only for networks with a specific tag key and value

The following identity-based policy statement allows the IAM principal to create a proposal only if the network for which the proposal is made has a tag with a tag key of `department` and a value of `accounting`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateProposalOnlyForTaggedNetwork",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:CreateProposal"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/department": [
 "accounting"
 ]
 }
 }
 }
 ]
}`

```

###### Example – Allow proposal creation only if a specific tag key and value are added

The following identity-based policy statements allow the IAM principal to create a proposal for inviting the specified account `123456789012` to the network only if a tag with a tag key of `consortium` and a tag value of `exampleconsortium` is added during proposal creation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RequireTagWithProposal",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:CreateProposal"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/consortium": [
 "exampleconsortium"
 ]
 }
 }
 },
 {
 "Sid": "AllowProposalAndInvitationTagging",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:TagResource"
 ],
 "Resource": [
 "arn:aws:managedblockchain:us-east-1::proposals/*",
 "arn:aws:managedblockchain:us-east-1:123456789012:invitations/*"
 ]
 }
 ]
}`

```

###### Example – Allow access only to proposals with a specific tag key and value

The following identity-based policy statement allows the IAM principal to retrieve and view proposals only if the proposal has a tag with a tag key of `consortium` and a tag value of `exampleconsortium`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowOnlyTaggedProposalAccess",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:GetProposal"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/consortium": [
 "exampleconsortium"
 ]
 }
 }
 }
 ]
}`

```

###### Example – Deny the ability to vote on proposals based on a specific tag key and value

The following identity-based policy statement denies the IAM principal the ability to vote on proposals that have a tag with the tag key of `consortium` and a tag value of `exampleconsortium`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyVoteOnTaggedProposal",
 "Effect": "Deny",
 "Action": [
 "managedblockchain:VoteOnProposal"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/consortium": [
 "exampleconsortium"
 ]
 }
 }
 }
 ]
}`

```

###### Example – Deny the ability to reject an invitation with a specific tag and value

The following identity-based policy statement denies the IAM principal the ability to reject on invitation that has a tag with the tag key of `consortium` and a tag value of `exampleconsortium`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "1",
 "Effect": "Deny",
 "Action": [
 "managedblockchain:RejectInvitation"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/consortium": [
 "exampleconsortium"
 ]
 }
 }
 }
 ]
}`

```
