Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Amazon Fraud Detector identity-based

policy examples

By default, users and IAM roles don't have permission to create or modify
Amazon Fraud Detector resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS API. An administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the specified resources they need. The
administrator must then attach those policies to the users or groups that require those
permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [AWS-managed (predefined) policy for Amazon Fraud Detector](#aws-managed-policy-for-amazon-fraud-detector "#aws-managed-policy-for-amazon-fraud-detector")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Allow full access to Amazon Fraud Detector resources](#allowing-full-access-to-amazon-fraud-detector-resources "#allowing-full-access-to-amazon-fraud-detector-resources")
- [Allow read-only access to Amazon Fraud Detector resources](#allowing-read-only-access-to-amazon-fraud-detector-resources "#allowing-read-only-access-to-amazon-fraud-detector-resources")
- [Allow access to a specific resource](#allowing-access-to-a-specific-resource "#allowing-access-to-a-specific-resource")
- [Allow access to specific resources when using dual mode API](#allow-access-to-specific-resource-dual-mode-api "#allow-access-to-specific-resource-dual-mode-api")
- [Limiting access based on tags](#limiting-access-based-on-tags "#limiting-access-based-on-tags")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon Fraud Detector resources in your
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

## AWS-managed (predefined) policy for Amazon Fraud Detector

AWS addresses many common use cases by providing standalone IAM policies that are created and administered by AWS. These AWS managed policies grant necessary permissions for common use cases so that you can avoid having to investigate which permissions are needed. For more information, see [AWS Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") in the _AWS Identity and Access Management Management User Guide_ .

The following AWS managed policy, which you can attach to users in your account, is specific to Amazon Fraud Detector:

`AmazonFraudDetectorFullAccess`: Grants full access to Amazon Fraud Detector resources, actions and the supported operations including:

- List and describe all model endpoints in Amazon SageMaker AI
- List all IAM roles in the account
- List all Amazon S3 buckets
- Allow IAM Pass Role to pass a role to Amazon Fraud Detector

This policy does not provide unrestricted S3 access. If you need to upload model training datasets to S3, the `AmazonS3FullAccess` managed policy (or scoped-down custom Amazon S3 access policy) is also required.

You can review the policy’s permissions by signing in to the IAM console and searching by the policy name. You can also create your own custom IAM policies to allow permissions for Amazon Fraud Detector actions and resources as you need them.
You can attach these custom policies to the users or groups that require them.

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

## Allow full access to Amazon Fraud Detector resources

The following example gives an user in your AWS account full access to all Amazon Fraud Detector resources and actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "frauddetector:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow read-only access to Amazon Fraud Detector resources

In this example, you grant an user in your AWS account read-only access to your Amazon Fraud Detector resources.

## Allow access to a specific resource

In this example of a resource-level policy, you grant an user in your AWS account access to all actions and resources except for one particular Detector resource.

## Allow access to specific resources when using dual mode API

Amazon Fraud Detector provides dual mode get APIs that work as both List and Describe operation. A dual mode API when called without any
parameters returns a list of the specified resource associated with your AWS account. A dual mode API when called with parameter
returns the details of the specified resource. The resource can be models, variables, event types, or entity types.

The dual mode APIs support resource-level permissions in IAM policies. However, the resource level permissions are only applied when
one or more parameters are provided as part of the request. For example, if user calls [GetVariables](../api/API_GetVariables.md "../api/API_GetVariables.md") API and provides
a variable name and if there is an IAM Deny policy attached to the variable resource or the variable name, user will receive `AccessDeniedException` error. If user calls
`GetVariables` API and does not specify a variable name, all variables are returned, which can cause information leak.

To allow users to view details of specific resources only, use an IAM `NotResource` policy element in an IAM Deny policy.
After you add this policy element to an IAM Deny policy, users can only view the details of the resources that are specified in the
`NotResource` block. For more information, see [IAM JSON policy elements: NotResource](../../../IAM/latest/UserGuide/reference_policies_elements_notresource.md "../../../IAM/latest/UserGuide/reference_policies_elements_notresource.md")
in the _IAM User Guide_.

The following example policy allows users to access all of Amazon Fraud Detector’s resources. However, the `NotResource` policy element is used to limit [GetVariables](../api/API_GetVariables.md "../api/API_GetVariables.md") API calls to
only the variable names with the prefixes `user*`, `job_*`, and `var*`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "frauddetector:*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": "frauddetector:GetVariables",
 "NotResource": [
 "arn:aws:frauddetector:*:*:variable/user*",
 "arn:aws:frauddetector:*:*:variable/job_*",
 "arn:aws:frauddetector:*:*:variable/var*"
 ]
 }
 ]
}`

```

**Response**

For this example policy, the response exhibit the following behavior:

- A GetVariables call that doesn’t include variable names results in an `AccessDeniedException` error because the request maps to the Deny statement.
- A GetVariables call that includes a variable name that’s not allowed, results in an `AccessDeniedException` error because the variable name doesn’t map to the variable
  name in the `NotResource` block. For example, a GetVariables call with a variable name `email_address` results in an `AccessDeniedException` error.
- A GetVariables call that includes a variable name that matches a variable name in the `NotResource` block is returned
  as expected. For example, a GetVariables call that includes variable name `job_cpa` returns the details of `job_cpa` variable.

## Limiting access based on tags

This example policy demonstrates how to limit access to Amazon Fraud Detector based on resource tags. This example assumes that:

- In your AWS account you have defined two different groups, named Team1 and Team2
- You have created four detectors
- You want to allow members of Team1 to make API calls on 2 detectors
- You want to allow members of Team2 to make API calls on the other 2 detectors

###### To control access to API calls (example)

1. Add a tag with the key `Project` and value `A` to the detectors used by Team1.
2. Add a tag with the key `Project` and value `B` to the detectors used by Team2.
3. Create an IAM policy with a `ResourceTag` condition that denies access to detectors that have tags with key `Project` and value `B`, and attach that policy to Team1.
4. Create an IAM policy with a `ResourceTag` condition that denies access to detectors that have tags with key `Project` and value `A`, and attach that policy to Team2.

The following is an example of a policy that denies specific actions on any Amazon Fraud Detector resource that has a tag with a key of `Project` and a value of `B`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "frauddetector:*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",

 "Action": [

 "frauddetector:CreateModel",
 "frauddetector:CancelBatchPredictionJob",
 "frauddetector:CreateBatchPredictionJob",
 "frauddetector:DeleteBatchPredictionJob",
 "frauddetector:DeleteDetector"
 ],

 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Project": "B"
 }
 }
 }
 ]
}`

```
