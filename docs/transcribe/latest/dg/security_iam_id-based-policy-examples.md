# Amazon Transcribe identity-based policy

examples

By default, users and roles don't have permission to create or modify Amazon Transcribe
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon Transcribe, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Transcribe](../../../service-authorization/latest/reference/list_amazontranscribe.md "../../../service-authorization/latest/reference/list_amazontranscribe.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the AWS Management Console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Permissions required for IAM roles](#auth-role-iam-user "#auth-role-iam-user")
- [Permissions required for Amazon S3 encryption keys](#auth-role-kms-key "#auth-role-kms-key")
- [Allow users to
  view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [AWS KMS encryption context policy](#kms-context-policy "#kms-context-policy")
- [Confused deputy prevention policy](#confused-deputy-policy "#confused-deputy-policy")
- [Viewing transcription jobs based on tags](#tagging-transcription-policy "#tagging-transcription-policy")

## Policy best practices

Identity-based policies determine whether someone can create, access, or delete Amazon Transcribe resources in your
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

## Using the AWS Management Console

To access the Amazon Transcribe console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Amazon Transcribe resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that an entity (users and roles) can use the [AWS Management Console](https://console.aws.amazon.com/transcribe/ "https://console.aws.amazon.com/transcribe/"), attach one of the following AWS-managed
policies to them.

- `AmazonTranscribeFullAccess`: Grants full access to create,
  read, update, delete, and run all Amazon Transcribe resources. It also allows access to Amazon S3
  buckets with `transcribe` in the bucket name.
- `AmazonTranscribeReadOnlyAccess`: Grants read-only access to
  Amazon Transcribe resources so that you can get and list transcription jobs and custom
  vocabularies.

###### Note

You can review the managed permission policies by signing in to the IAM
AWS Management Console and searching by policy name. A search for "transcribe" returns both policies
listed above (_AmazonTranscribeReadOnly_ and
_AmazonTranscribeFullAccess_).

You can also create your own custom IAM policies to allow permissions for
Amazon Transcribe API actions. You can attach these custom policies to the entities that require those
permissions.

## Permissions required for IAM roles

If you create an IAM role to call Amazon Transcribe, it must have
permission to access the Amazon S3 bucket. If applicable, the KMS key
must also be used to encrypt the contents of the bucket. Refer to the following sections for
example policies.

### Trust policies

The IAM entity you use to make your transcription request must have a trust
policy that enables Amazon Transcribe to assume that role. Use the following Amazon Transcribe trust
policy. Note that if you're making a real-time Call Analytics request with post-call analytics enabled, you
must use 'Trust policy for real-time Call Analytics'.

**Trust policy for Amazon Transcribe**

**Trust policy for real-time Call Analytics**

### Amazon S3 input bucket policy

The following policy gives an IAM role permission to access files from the specified
input bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`DOC-EXAMPLE-INPUT-BUCKET`",
 "arn:aws:s3:::`DOC-EXAMPLE-INPUT-BUCKET`/*"
 ]
 }
}`

```

### Amazon S3 output bucket policy

The following policy gives an IAM role permission to write files to the specified
output bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`DOC-EXAMPLE-OUTPUT-BUCKET`/*"
 ]
 }
}`

```

## Permissions required for Amazon S3 encryption keys

If you're using a KMS key to encrypt an Amazon S3 bucket, include the
following in the KMS key policy. This gives Amazon Transcribe access to the contents of
the bucket. For more information about allowing access to KMS keys, see
[Allowing external AWS accounts to access an KMS key](../../../kms/latest/developerguide/key-policy-modifying.md#key-policy-modifying-external-accounts "../../../kms/latest/developerguide/key-policy-modifying.md#key-policy-modifying-external-accounts") in the
_AWS KMS Developer Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`ExampleRole`"
 },
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:`us-west-2`:`111122223333`:key/`KMS-Example-KeyId`"
 }
 ]
}`

```

## Allow users to

view their own permissions

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

## AWS KMS encryption context policy

The following policy grants the IAM role “`ExampleRole`” permission
to use the AWS KMS _Decrypt_ and _Encrypt_
operations for this particular KMS key. This policy works **only** for
requests with at least one encryption context pair, in this case
"`color:indigoBlue`”. For more information on AWS KMS encryption context,
see [AWS KMS encryption context](data-encryption.md#kms-context "data-encryption.md#kms-context").

## Confused deputy prevention policy

Here's an example of an assume role policy that shows how you can use `aws:SourceArn`
and `aws:SourceAccount` with Amazon Transcribe to prevent a confused deputy issue. For
more information on confused deputy prevention, see [Cross-service confused deputy prevention](security-iam-confused-deputy.md "security-iam-confused-deputy.md").

## Viewing transcription jobs based on tags

You can use conditions in your identity-based policy to control access to Amazon Transcribe
resources based on tags. This example shows how you might create a policy that allows viewing a
transcription job. However, permission is granted only if the transcription job tag `Owner`
has the value of that user's user name. This policy also grants the permissions necessary to complete
this action using the AWS Management Console.

You can attach this policy to the IAM entities in your account. If a role named
`test-role` attempts to view a transcription job, the transcription job must be tagged
`Owner=test-role` or `owner=test-role` (condition key names are not
case-sensitive), otherwise they are denied access. For more information, see
[IAM JSON
policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User
Guide_.

For more information on tagging in Amazon Transcribe, see [Tagging resources](tagging.md "tagging.md").
