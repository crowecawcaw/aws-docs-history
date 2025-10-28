End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Identity-based policy

examples for Amazon Lex

By default, users and roles don't have permission to create or modify Amazon Lex
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon Lex, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Lex](../../../service-authorization/latest/reference/list_amazonlex.md "../../../service-authorization/latest/reference/list_amazonlex.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Amazon Lex
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Delete All Amazon Lex Bots](#security_iam_id-based-policy-examples-access-one-bot "#security_iam_id-based-policy-examples-access-one-bot")
- [Allow a user to
  migrate a bot to Amazon Lex V2 APIs](#security_iam_id-based-policy-examples-migrate "#security_iam_id-based-policy-examples-migrate")
- [Use a Tag to Access a Resource](#security_iam_id-based-policy-examples-tag "#security_iam_id-based-policy-examples-tag")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon Lex resources in your
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

## Using the Amazon Lex

console

To access the Amazon Lex console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Amazon Lex resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

AWS addresses many common use cases by providing standalone
IAM policies that are created and administered by AWS. These
policies are called AWS managed policies. AWS managed policies make
it easier for you to assign appropriate permissions to users,
groups, and roles than if you had to write the policies yourself.
For more information, see [AWS Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User
Guide_.

The following AWS managed policies, which you can attach to
groups and roles in your account, are specific to Amazon Lex:

- **AmazonLexReadOnly** —
  Grants read-only access to Amazon Lex resources.
- **AmazonLexRunBotsOnly**
  — Grants access to run Amazon Lex conversational bots.
- **AmazonLexFullAccess**
  — Grants full access to create, read, update, delete,
  and run all Amazon Lex resources. Also grants the ability to
  associate Lambda functions whose name starts with
  `AmazonLex` with Amazon Lex intents.

###### Note

You can review these permissions policies by signing in to the
IAM console and searching for specific policies.

The **AmazonLexFullAccess** policy
doesn't grant the user permission to use the
`KendraSearchIntent` intent to query an Amazon Kendra index.
To query an index, you must add additional permissions to the
policy. For the required permissions, see [IAM Policy for Amazon Kendra
Search](built-in-intent-kendra-search.md#kendra-search-iam "built-in-intent-kendra-search.md#kendra-search-iam").

You can also create your own custom IAM policies to allow
permissions for Amazon Lex API actions. You can attach these custom
policies to the IAM roles or groups that require those
permission.

For details about AWS managed policies for Amazon Lex, see [AWS managed policies for
Amazon Lex](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

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

## Delete All Amazon Lex Bots

This example policy grants a user in your AWS account
permission to delete any bot in your account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lex:DeleteBot"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Allow a user to

migrate a bot to Amazon Lex V2 APIs

The following IAM permission policy allows a user to start migrating
a bot from Amazon Lex to Amazon Lex V2 APIs and to see the list of migrations and
their progress.

##

Use a Tag to Access a Resource

This example policy grants a user or role in your AWS
account permission to use the `PostText` operation with
any resource tagged with the key `Department`
and the value `Support`.
