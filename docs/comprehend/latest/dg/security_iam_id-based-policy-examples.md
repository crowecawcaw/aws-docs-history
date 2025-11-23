# Identity-based policy

examples for Amazon Comprehend

By default, users and roles don't have permission to create or modify Amazon Comprehend
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon Comprehend, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Comprehend](../../../service-authorization/latest/reference/list_amazoncomprehend.md "../../../service-authorization/latest/reference/list_amazoncomprehend.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Amazon Comprehend
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Permissions required to perform document analysis
  actions](#security-iam-based-policy-perform-cmp-actions "#security-iam-based-policy-perform-cmp-actions")
- [Permissions required to use KMS encryption](#auth-kms-permissions "#auth-kms-permissions")
- [AWS managed (predefined)
  policies for Amazon Comprehend](#access-policy-aws-managed-policies "#access-policy-aws-managed-policies")
- [Role-based permissions required for
  asynchronous operations](#auth-role-permissions "#auth-role-permissions")
- [Permissions to allow all Amazon Comprehend actions](#custom-policy-all-all-actions "#custom-policy-all-all-actions")
- [Permissions to allow topic modeling actions](#custom-policy-allow-topic-modeling "#custom-policy-allow-topic-modeling")
- [Permissions required for a custom asynchronous analysis job](#tagging-resources "#tagging-resources")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon Comprehend resources in your
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

## Using the Amazon Comprehend

console

To access the Amazon Comprehend console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Amazon Comprehend resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

For minimum Amazon Comprehend console permissions, you can attach the
`ComprehendReadOnly` AWS managed policy to
the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

To use the Amazon Comprehend console, you also need permissions for the actions shown in
the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "iam:ListRoles",
 "iam:GetRole",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
 }`

```

The Amazon Comprehend console needs these additional permissions for the following
reasons:

- `iam` permissions to list the available IAM roles for your
  account.
- `s3` permissions to access the Amazon S3 buckets and objects that
  contain the data for topic modeling.

When you create an asynchronous batch job or a topic modeling job using the
console, you have the option to have the console create an IAM role for your job. To
create an IAM role, users must be granted the following additional permissions to
create IAM roles and policies, and to attach policies to roles:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Action":
 [
 "iam:CreateRole",
 "iam:CreatePolicy",
 "iam:AttachRolePolicy"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action":
 [
 "iam:PassRole"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/*Comprehend*"
 }
 ]
 }`

```

The Amazon Comprehend console needs these additional permissions for the following
reasons:

- `iam` permissions to create roles and policies and to attach
  roles and policies. The `iam:PassRole` action enables the console
  to pass the role to Amazon Comprehend.

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

## Permissions required to perform document analysis

actions

The following example policy grants permissions to use the Amazon Comprehend document analysis actions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "AllowDetectActions",
 "Effect": "Allow",
 "Action": [
 "comprehend:DetectEntities",
 "comprehend:DetectKeyPhrases",
 "comprehend:DetectDominantLanguage",
 "comprehend:DetectSentiment",
 "comprehend:DetectTargetedSentiment",
 "comprehend:DetectSyntax",
 "textract:DetectDocumentText",
 "textract:AnalyzeDocument"
 ],
 "Resource": "*"
 }
 ]
}`

```

The policy has one statement that grants permission to use the
`DetectEntities`, `DetectKeyPhrases`, `DetectDominantLanguage`,
`DetectTargetedSentiment`, `DetectSentiment`, and `DetectSyntax` actions.
The policy statement also grants permissions to use two Amazon Textract API methods. Amazon Comprehend calls these methods to extract
text from image files and scanned PDF documents. You can remove these permissions for users that never run custom
inference for these types of input files.

A user with this policy would not be able to perform batch actions or asynchronous actions in your account.

The policy doesn't specify the `Principal` element because you don't
specify the principal who gets the permission in an identity-based policy. When you
attach a policy to a user, the user is the implicit principal. When you attach a
permissions policy to an IAM role, the principal identified in the role's trust policy
gets the permissions.

For a table showing all the Amazon Comprehend API actions and the resources that they apply to, see [Actions,
resources, and condition keys for Amazon Comprehend](../../../service-authorization/latest/reference/list_amazoncomprehend.md "../../../service-authorization/latest/reference/list_amazoncomprehend.md") in the _Service Authorization
Reference_.

## Permissions required to use KMS encryption

To fully use Amazon Key Management Service (KMS) for data and job encryption in an asynchronous job,
you need to grant permissions for the actions shown in the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "kms:CreateGrant"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDatakey"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": [
 "s3.`us-east-1`.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

When you create an asychronous job with Amazon Comprehend you use input data stored on Amazon S3. With S3, you have the option to encrypt your stored data, which is encrypted by S3, not by Amazon Comprehend. We can decrypt and read that encrypted input data
if you provide `kms:Decrypt` permission for the key with which the original input data was encrypted to the data
access role used by the Amazon Comprehend job.

You also have the option of using KMS customer-managed keys (CMK) to encrypt the output results on S3, as well as the storage
volume used during job processing. When you do this, you can use the same KMS key for both types of encryption, but this is not
necessary. Separate fields are available when creating the job to specify the keys for output encryption and volume encryption and
you can even use a KMS key from a different account.

When using KMS encryption, `kms:CreateGrant` permission is required for volume encryption and `kms:GenerateDataKey` permission
is needed for output data encryption. For reading encrypted input (as when the input data is already encrypted by Amazon S3), `kms:Decrypt`
permission is required. The IAM role needs to give these permissions as needed. However, if the key is from a different account than is currently
being used, the KMS key policy for that kms key must also give these permissions to the data access role for the job.

## AWS managed (predefined)

policies for Amazon Comprehend

AWS addresses many common use cases by providing standalone IAM policies that are
created and administered by AWS. These AWS managed policies grant necessary
permissions for common use cases so that you can avoid having to investigate what
permissions are needed. For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

The following AWS managed policies, which you can attach to users in your account,
are specific to Amazon Comprehend:

- **ComprehendFullAccess** – Grants full
  access to Amazon Comprehend resources including running topic modeling jobs. Includes
  permission to list and get IAM roles.
- **ComprehendReadOnly** – Grants
  permission to run all Amazon Comprehend actions except
  `StartDominantLanguageDetectionJob`,
  `StartEntitiesDetectionJob`,
  `StartKeyPhrasesDetectionJob`,
  `StartSentimentDetectionJob`,
  `StartTargetedSentimentDetectionJob`, and
  `StartTopicsDetectionJob`.

You need to apply the following additional policy to any user that will use
Amazon Comprehend:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Action":
 [
 "iam:PassRole"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/*Comprehend*"
 }
 ]
 }`

```

You can review the managed permissions policies by signing in to the IAM console
and searching for specific policies there.

These policies work when you are using AWS SDKs or the AWS CLI.

You can also create your own custom IAM policies to allow permissions for Amazon Comprehend
actions and resources. You can attach these custom policies to the users, groups or
roles that require those permissions.

## Role-based permissions required for

asynchronous operations

To use the Amazon Comprehend asynchronous operations, you must grant Amazon Comprehend access to the Amazon S3 bucket that contains
your document collection. You do this by creating a data access role in your account with a trust policy to
trust the Amazon Comprehend service principal. For more information about creating a role, see [Creating a role to delegate permissions to an AWS
service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _AWS Identity and Access Management User Guide_.

The following shows an example trust policy for the role that you create. To help with
[confused deputy prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md"),
you restrict the scope of the permission by using one or more global condition context keys. Set
the `aws:SourceAccount` value to your account ID. If you use the `ArnEquals` condition,
set the `aws:SourceArn` value to the ARN of the job. Use a wildcard for the job number in the ARN,
because Amazon Comprehend generates this number as part of job creation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "comprehend.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:comprehend:`us-west-2:111122223333`:pii-entities-detection-job/*"
 }
 }
 }
 ]
 }`

```

After you create the role, create an access policy for that role. This should grant the Amazon S3
`GetObject` and `ListBucket` permissions to the Amazon S3 bucket that contains your input
data, and the Amazon S3 `PutObject` permission to your Amazon S3 output data bucket.

## Permissions to allow all Amazon Comprehend actions

After you sign up for AWS, you create an administrator user to manage your
account, including creating users and managing their permissions.

You might choose to create a user who has permissions for all Amazon
Comprehend actions (think of this user as a service-specific administrator) for
working with Amazon Comprehend. You can attach the following permissions policy
to this user.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Sid": "AllowAllComprehendActions",
 "Effect": "Allow",
 "Action":
 [
 "comprehend:*",
 "iam:ListRoles",
 "iam:GetRole",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation",
 "iam:CreateRole",
 "iam:CreatePolicy",
 "iam:AttachRolePolicy",
 "kms:CreateGrant",
 "kms:Decrypt",
 "kms:GenerateDatakey"
 ],
 "Resource": "*"
 },
 {
 "Action":
 [
 "iam:PassRole"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/*Comprehend*"
 }
 ]
}`

```

These permissions can be modified with regard to encryption in the following ways:

- To enable Amazon Comprehend to analyze documents stored in an encrypted S3 bucket, the IAM role must have the `kms:Decrypt` permission.
- To enable Amazon Comprehend to encrypt documents stored on a storage volume attached to the compute instance that processes the analysis job, the IAM role
  must have the `kms:CreateGrant` permission.
- To enable Amazon Comprehend to encrypt the output results in their S3 bucket, the IAM role
  must have the `kms:GenerateDataKey` permission.

## Permissions to allow topic modeling actions

The following permissions policy grants user permissions to perform the Amazon
Comprehend topic modeling operations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowTopicModelingActions",
 "Effect": "Allow",
 "Action": [
 "comprehend:DescribeTopicsDetectionJob",
 "comprehend:ListTopicsDetectionJobs",
 "comprehend:StartTopicsDetectionJob"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Permissions required for a custom asynchronous analysis job

###### Important

If you have an IAM policy which restricts model access, you won't be able to complete an
inference job with a custom model. Your IAM policy should be updated to having a
wildcard resource for a custom async analysis job.

If you are using the [StartDocumentClassificationJob](API_StartDocumentClassificationJob.md "API_StartDocumentClassificationJob.md") and [StartEntitiesDetectionJob](API_StartEntitiesDetectionJob.md "API_StartEntitiesDetectionJob.md") APIs, you need to update your IAM policy
unless you are currently using wildcards as resources. If you are using a [StartEntitiesDetectionJob](API_StartEntitiesDetectionJob.md "API_StartEntitiesDetectionJob.md") using a pretrained model this does not impact
you and you don't need to make any changes.

The following example policy contains an **outdated**
reference.

```
{
    "Action": [
        "comprehend:StartDocumentClassificationJob",
        "comprehend:StartEntitiesDetectionJob",
    ],
    "Resource": [
        "arn:aws:comprehend:us-east-1:123456789012:document-classifier/myClassifier",
        "arn:aws:comprehend:us-east-1:123456789012:entity-recognizer/myRecognizer"
    ],
    "Effect": "Allow"
}
```

This is the **updated** policy you need to use to
sucessfully run StartDocumentClassificationJob and StartEntitiesDetectionJob.

```
{
    "Action": [
        "comprehend:StartDocumentClassificationJob",
        "comprehend:StartEntitiesDetectionJob",
    ],
    "Resource": [
        "arn:aws:comprehend:us-east-1:123456789012:document-classifier/myClassifier",
        "arn:aws:comprehend:us-east-1:123456789012:document-classification-job/*",
        "arn:aws:comprehend:us-east-1:123456789012:entity-recognizer/myRecognizer",
        "arn:aws:comprehend:us-east-1:123456789012:entities-detection-job/*"
    ],
    "Effect": "Allow"
}
```
