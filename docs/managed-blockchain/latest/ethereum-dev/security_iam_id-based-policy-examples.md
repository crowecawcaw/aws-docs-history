# Identity-based policy

examples for Amazon Managed Blockchain (AMB) Access Ethereum

By default, users and roles don't have permission to create or modify AMB Access Ethereum
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by AMB Access Ethereum, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Managed Blockchain (AMB) Access Ethereum](../../../service-authorization/latest/reference/list_amazonmanagedblockchain.md "../../../service-authorization/latest/reference/list_amazonmanagedblockchain.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the AMB Access Ethereum
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Performing all available actions for AMB Access Ethereum](#security_iam_id-based-policy-example "#security_iam_id-based-policy-example")
- [Controlling access using tags](#security_iam_id-based-policy-examples-tags "#security_iam_id-based-policy-examples-tags")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete AMB Access Ethereum resources in your
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
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
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

## Using the AMB Access Ethereum

console

To access the Amazon Managed Blockchain (AMB) Access Ethereum console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the AMB Access Ethereum resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the AMB Access Ethereum console, also attach the
AMB Access Ethereum `ConsoleAccess` or `ReadOnly` AWS managed policy to
the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

`AmazonManagedBlockchainConsoleFullAccess`

## Allow users

to view their own permissions

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

## Performing all available actions for AMB Access Ethereum

This example shows how you grant users AWS account access in the
`us-east-1` Region so that they can do the following:

- List all Ethereum networks
- Create and list nodes on all those networks
- Get and delete nodes in AWS account
  `111122223333`
- Get and delete accessors in AWS account
  `555555555555`
- Create WebSocket connections, and send HTTP requests
  to an Ethereum node

###### Note

- If you want to grant access across all Regions, replace `us-east-1`
  with `*`.
- You must specify the AWS account ID of the
  node and accessor resources in the policy that you want to enforce.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "WorkWithEthereumNetworks",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:ListNetworks",
                "managedblockchain:GetNetwork"
            ],
            "Resource": [
                "arn:aws:managedblockchain:`us-east-1`::networks/n-ethereum-mainnet"


            ]
        },
        {
            "Sid": "CreateAndListEthereumNodes",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:CreateNode",
                "managedblockchain:ListNodes"
            ],
            "Resource": [
                "arn:aws:managedblockchain:`us-east-1`::networks/*"
            ]
        },
        {
            "Sid": "ManageEthereumNodes",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:GetNode",
                "managedblockchain:DeleteNode"
            ],
            "Resource": [
                "arn:aws:managedblockchain:`us-east-1`:`111122223333`:nodes/*"
            ]
        },
         {
            "Sid": "GetAndDeleteAccessors",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:GetAccessor",
                "managedblockchain:DeleteAccessor"
            ],
            "Resource": [
                "arn:aws:managedblockchain:`us-east-1`:`555555555555`:accessors/*"
            ]
        },
        {
            "Sid": "CreateAndListAccessors",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:CreateAccessor",
                "managedblockchain:ListAccessors"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "WorkWithEthereumNodes",
            "Effect": "Allow",
            "Action": [
                "managedblockchain:POST",
                "managedblockchain:GET",
                "managedblockchain:Invoke"

            ],
            "Resource": [
                "arn:aws:managedblockchain:`us-east-1`:`111122223333`:*"
             ]
        }
    ]
}

```

## Controlling access using tags

The following example policies demonstrate how you can use tags to limit access to AMB Access Ethereum resources and actions performed on those resources.

###### Note

This topic includes examples of policy statements with a `Deny` effect.
These policies assume that other policies with `Allow` effect for
those actions exist with broader applicability. The `Deny` policy
statement is being used to restrict that otherwise overly-permissive allow
statement.

###### Example – Deny access to networks with a specific tag key

The following identity-based policy statement denies the IAM principal the
ability to retrieve or view network information if the network has a tag with
the tag key of `restricted`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyTaggedNetworkAccess",
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

###### Example – Deny node creation on networks that have a specific tag and value

The following identity-based policy statement denies the IAM principal the ability to create a node on an Ethereum public network tagged in the AWS account with the tag key of `department` and the value `accounting`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyCreateNodeForNetworkWithTag",
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
 "accounting"
 ]
 }
 }
 }
 ]
}`

```

###### Example – Require a specific tag key and value to be added when a node is created

The following identity-based policy statements allow an IAM principal to create a node for the AWS account 111122223333 only if a key with the tag key of `department` and a value of `accounting` is added during creation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RequireTagForCreateNode",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:CreateNode"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/department": [
 "accounting"
 ]
 }
 }
 },
 {
 "Sid": "AllowTaggingNodes",
 "Effect": "Allow",
 "Action": [
 "managedblockchain:TagResource"
 ],
 "Resource": [
 "arn:aws:managedblockchain:us-east-1:`111122223333`:nodes/*"
 ]
 }
 ]
}`

```

###### Example – Deny listing nodes for networks that have a specific tag key and value

The following identity-based policy statement denies the IAM principal the ability to list nodes on an Ethereum public network tagged in the AWS account with the tag key of `department` and the value `accounting`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyListNodesForNetworkWithTag",
 "Effect": "Deny",
 "Action": [
 "managedblockchain:ListNodes"
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

###### Example – Deny retrieving and viewing node information for nodes with a specific tag key and value

The following identity-based policy statement denies the IAM principal the ability to view node information for nodes that have a tag with the tag key of `department` and the value `accounting`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyGetNodeWithNodeTag",
 "Effect": "Deny",
 "Action": [
 "managedblockchain:GetNode"
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
