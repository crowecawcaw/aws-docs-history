# Least-privilege permissions

Since your KMS keys protect sensitive information, we recommend following the principle
of least-privileged access. Delegate the minimum permissions required to perform a task when
you define your key policies. Only allow all actions (`kms:*`) on a KMS key
policy if you plan to further restrict permissions with additional IAM policies. If you
plan to manage permissions with IAM policies, limit who has the ability to create and
attach IAM policies to IAM principals and [monitor for policy changes](../../../awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.md#cloudwatch-alarms-for-cloudtrail-iam-policy-changes "../../../awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.md#cloudwatch-alarms-for-cloudtrail-iam-policy-changes").

If you allow all actions (`kms:*`) in both the key policy and the IAM policy,
the principal has both administrative and usage permissions to the KMS key. As a security
best practice, we recommend only delegating these permissions to specific principals. You
can do this by explicitly naming the principal in the key policy or by limiting which
principals the IAM policy is attached to. You can also use [condition keys](policy-conditions.md "policy-conditions.md") to restrict permissions. For example,
you can use the [`aws:PrincipalTag`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principaltag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principaltag") to allow all actions if the principal making
the API call has the tag specified in the condition rule.

For help understanding how policy statements are evaluated in AWS, see [Policy evaluation
logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") in the _IAM User Guide_. We recommend reviewing this
topic before writing policies to reduce the chance that your policy has unintended effects,
such as providing access to principals that should not have access.

###### Tip

When testing an application in a non-production envrionment, use [IAM Access Analyzer](https://aws.amazon.com/iam/features/analyze-access/ "https://aws.amazon.com/iam/features/analyze-access/") to
help you apply least-privileges to your IAM policies.

If you use IAM users instead of IAM roles, we strongly recommend enabling AWS [multi-factor authentication](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") (MFA) to
mitigate the vulnerability of long-term credentials. You can use MFA to do the following:

- Require that users validate their credentials with MFA before performing
  privileged actions, such as scheduling key deletion.
- Split ownership of an administrator account password and MFA device between
  individuals to implement split authorization.

###### Learn more

- [AWS managed
  policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md")
- [Techniques for writing least privilege IAM policies](https://aws.amazon.com//blogs/security/techniques-for-writing-least-privilege-iam-policies/ "https://aws.amazon.com//blogs/security/techniques-for-writing-least-privilege-iam-policies/")

## Implementing least privileged

permissions

When you give an AWS service permission to use a KMS key, ensure that the
permission is valid only for the resources that the service must access on your behalf.
This least privilege strategy helps to prevent unauthorized use of a KMS key when
requests are passed between AWS services.

To implement a least privilege strategy, use we recommend using AWS KMS encryption
context condition keys and the global source ARN or source account condition
keys.

### Using encryption context

condition keys

The most effective way to implement least privileged permissions when using AWS KMS
resources is to include the [kms:EncryptionContext:context-key](conditions-kms.md#conditions-kms-encryption-context "conditions-kms.md#conditions-kms-encryption-context") or [kms:EncryptionContextKeys](conditions-kms.md#conditions-kms-encryption-context-keys "conditions-kms.md#conditions-kms-encryption-context-keys") condition keys in the
policy that allows principals to call AWS KMS cryptographic operations. These
condition keys are particularly effective because they associate the permission with
the [encryption context](encrypt_context.md "encrypt_context.md") that is bound to the
ciphertext when the resource is encrypted.

Use encryption context conditions keys only when the action in the policy
statement is [CreateGrant](../APIReference/API_CreateGrant.md "../APIReference/API_CreateGrant.md") or
an AWS KMS symmetric cryptographic operation that takes an
`EncryptionContext` parameter, such as the operations like [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") or [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md"). (For a list of supported
operations, see [kms:EncryptionContext:context-key](conditions-kms.md#conditions-kms-encryption-context "conditions-kms.md#conditions-kms-encryption-context") or [kms:EncryptionContextKeys](conditions-kms.md#conditions-kms-encryption-context-keys "conditions-kms.md#conditions-kms-encryption-context-keys").) If you use these
condition keys to allow other operations, such as [DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md"), permission will be
denied.

Set the value to the encryption context that the service uses when it encrypts the
resource. This information is typically available in the Security chapter of the
service documentation. For example, the [encryption context for AWS Proton](../../../proton/latest/adminguide/data-protection.md#encryption-context "../../../proton/latest/adminguide/data-protection.md#encryption-context") identifies the AWS Proton
resource and its associated template. The [AWS Secrets Manager encryption context](../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-encryption-context "../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-encryption-context") identifies the secret and its version. The
[encryption context for Amazon Location](../../../location/latest/developerguide/encryption-at-rest.md#location-encryption-context "../../../location/latest/developerguide/encryption-at-rest.md#location-encryption-context") identifies the tracker or collection.

The following example key policy statement allows Amazon Location Service to create grants on
behalf of authorized users. This policy statement limits the permission by using the
[kms:ViaService](conditions-kms.md#conditions-kms-via-service "conditions-kms.md#conditions-kms-via-service"), [kms:CallerAccount](conditions-kms.md#conditions-kms-caller-account "conditions-kms.md#conditions-kms-caller-account"), and
`kms:EncryptionContext:*context-key*` condition keys to tie the permission to a
particular tracker resource.

```
{
  "Sid": "Allow Amazon Location to create grants on behalf of authorized users",
  "Effect": "Allow",
  "Principal": {
    "AWS": "`arn:aws:iam::111122223333:role/LocationTeam`"
  },
  "Action": "kms:CreateGrant",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:ViaService": "geo.us-west-2.amazonaws.com",
      "kms:CallerAccount": "`111122223333`",
      "kms:EncryptionContext:aws:geo:arn": "`arn:aws:geo:us-west-2:111122223333:tracker/SAMPLE-Tracker`"
    }
  }
}
```

### Using `aws:SourceArn` or

`aws:SourceAccount` condition keys

When the principal in a key policy statement is an [AWS service principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services"), we strongly recommend that you use the [aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") or [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition keys, in addition
to the `kms:EncryptionContext:*context-key*` condition key. The ARN and account values
are included in the authorization context only when a request comes to AWS KMS from
another AWS service. This combination of conditions implements least privileged
permissions and avoids a potential [confused deputy scenario](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"). Service principals are not typically used as
principals in a key policy, but some AWS services, such as AWS CloudTrail, require it.

To use the `aws:SourceArn` or `aws:SourceAccount` global
condition keys, set the value to the Amazon Resource Name (ARN) or account of the
resource that is being encrypted. For example, in a key policy statement that gives
AWS CloudTrail permission to encrypt a trail, set the value of `aws:SourceArn`
to the ARN of the trail. Whenever possible, use `aws:SourceArn`, which is
more specific. Set the value to the ARN or an ARN pattern with wildcard characters.
If you don't know the ARN of the resource, use `aws:SourceAccount`
instead.

###### Note

If a resource ARN includes characters that are not permitted in an AWS KMS key
policy, you cannot use that resource ARN in the value of the
`aws:SourceArn` condition key. Instead, use the
`aws:SourceAccount` condition key.
For details about key policy document rules, see [Key policy format](key-policy-overview.md#key-policy-format "key-policy-overview.md#key-policy-format").

In the following example key policy, the principal who gets the permissions is the
AWS CloudTrail service principal, `cloudtrail.amazonaws.com`. To implement
least privilege, this policy uses the `aws:SourceArn` and
`kms:EncryptionContext:*context-key*` condition keys. The policy statement allows
CloudTrail to use the KMS key to [generate the data key](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") that it uses to encrypt a trail. The
`aws:SourceArn` and `kms:EncryptionContext:*context-key*` conditions are
evaluated independently. Any request to use the KMS key for the specified
operation must satisfy both conditions.

To restrict the service's permission to the `finance` trail in the
example account (111122223333) and `us-west-2` Region, this
policy statement sets the `aws:SourceArn` condition key to the ARN of a
particular trail. The condition statement uses the [ArnEquals](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_ARN "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_ARN") operator to ensure that every element in the ARN is evaluated
independently when matching. The example also uses the
`kms:EncryptionContext:*context-key*` condition key to limit the permission to trails
in a particular account and Region.

Before using this key policy, replace the example account ID, Region, and trail
name with valid values from your account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCloudTrailToEncryptLogs",
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action": "kms:GenerateDataKey",
 "Resource": "*",
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": [
 "arn:aws:cloudtrail:`us-west-2`:`111122223333`:trail/`finance`"
 ]
 },
 "StringLike": {
 "kms:EncryptionContext:aws:cloudtrail:arn": [
 "arn:aws:cloudtrail:*:`111122223333`:trail/*"
 ]
 }
 }
 }
 ]
}`

```
