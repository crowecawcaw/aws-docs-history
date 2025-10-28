# Access AWS Secrets Manager secrets from a different

account

To allow users in one account to access secrets in another account
(_cross-account access_), you must allow access both in a resource policy
and in an identity policy. This is different than granting access to identities in the same
account as the secret.

Cross-account permission is effective only for the following operations:

- [CancelRotateSecret](../apireference/API_CancelRotateSecret.md "../apireference/API_CancelRotateSecret.md")
- [DeleteResourcePolicy](../apireference/API_DeleteResourcePolicy.md "../apireference/API_DeleteResourcePolicy.md")
- [DeleteSecret](../apireference/API_DeleteSecret.md "../apireference/API_DeleteSecret.md")
- [DescribeSecret](../apireference/API_DescribeSecret.md "../apireference/API_DescribeSecret.md")
- [GetRandomPassword](../apireference/API_GetRandomPassword.md "../apireference/API_GetRandomPassword.md")
- [GetResourcePolicy](../apireference/API_GetResourcePolicy.md "../apireference/API_GetResourcePolicy.md")
- [GetSecretValue](../apireference/API_GetSecretValue.md "../apireference/API_GetSecretValue.md")
- [ListSecretVersionIds](../apireference/API_ListSecretVersionIds.md "../apireference/API_ListSecretVersionIds.md")
- [PutResourcePolicy](../apireference/API_PutResourcePolicy.md "../apireference/API_PutResourcePolicy.md")
- [PutSecretValue](../apireference/API_PutSecretValue.md "../apireference/API_PutSecretValue.md")
- [RemoveRegionsFromReplication](../apireference/API_RemoveRegionsFromReplication.md "../apireference/API_RemoveRegionsFromReplication.md")
- [ReplicateSecretToRegions](../apireference/API_ReplicateSecretToRegions.md "../apireference/API_ReplicateSecretToRegions.md")
- [RestoreSecret](../apireference/API_RestoreSecret.md "../apireference/API_RestoreSecret.md")
- [RotateSecret](../apireference/API_RotateSecret.md "../apireference/API_RotateSecret.md")
- [StopReplicationToReplica](../apireference/API_StopReplicationToReplica.md "../apireference/API_StopReplicationToReplica.md")
- [TagResource](../apireference/API_TagResource.md "../apireference/API_TagResource.md")
- [UntagResource](../apireference/API_UntagResource.md "../apireference/API_UntagResource.md")
- [UpdateSecret](../apireference/API_UpdateSecret.md "../apireference/API_UpdateSecret.md")
- [UpdateSecretVersionStage](../apireference/API_UpdateSecretVersionStage.md "../apireference/API_UpdateSecretVersionStage.md")
- [ValidateResourcePolicy](../apireference/API_ValidateResourcePolicy.md "../apireference/API_ValidateResourcePolicy.md")
  You can use the `BlockPublicPolicy` parameter with the [PutResourcePolicy](../apireference/API_PutResourcePolicy.md "../apireference/API_PutResourcePolicy.md") action to help protect your resources by
  preventing public access from being granted through the resource policies that are directly
  attached to your secrets. You can also use [IAM Access Analyzer](../../../IAM/latest/UserGuide/best-practices.md#bp-preview-access "../../../IAM/latest/UserGuide/best-practices.md#bp-preview-access") to
  verify cross-account access.

You must also allow the identity to use the KMS key that the secret is encrypted with.
This is because you can't use the AWS managed key (`aws/secretsmanager`) for
cross-account access. Instead, you must encrypt your secret with a KMS key that you create,
and then attach a key policy to it. There is a charge for creating KMS keys. To change the
encryption key for a secret, see [Modify an AWS Secrets Manager secret](manage_update-secret.md "manage_update-secret.md").

###### Important

Resource-based policies granting `secretsmanager:PutResourcePolicy`
permission gives principals, even those in other accounts, the ability to modify your
resource-based policies. This permission lets principals escalate existing permissions like
obtaining full administrative access to secrets. We recommend you apply the principle of
[least privileged
access](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") to your policies. For more information, see [Resource-based policies](auth-and-access_resource-policies.md "auth-and-access_resource-policies.md").

The following example policies assume you have a secret and encryption key in
_Account1_, and an identity in _Account2_ that you
want to allow to access the secret value.

###### Step 1: Attach a resource policy to the secret in _Account1_

- The following policy allows `ApplicationRole` in
  `Account2` to access the secret in
  `Account1`. To use this policy, see [Resource-based policies](auth-and-access_resource-policies.md "auth-and-access_resource-policies.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`ApplicationRole`"
 },
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "*"
 }
 ]
}`

```

###### Step 2: Add a statement to the key policy for the KMS key in

_Account1_

- The following key policy statement allows `ApplicationRole`
  in `Account2` to use the KMS key in
  `Account1` to decrypt the secret in
  `Account1`. To use this statement, add it to the key policy for
  your KMS key. For more information, see [Changing a key
  policy](../../../kms/latest/developerguide/key-policy-modifying.md "../../../kms/latest/developerguide/key-policy-modifying.md").

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::`Account2`:role/`ApplicationRole`"
  },
  "Action": [
    "kms:Decrypt",
    "kms:DescribeKey"
  ],
  "Resource": "*"
}
```

###### Step 3: Attach an identity policy to the identity in

_Account2_

- The following policy allows `ApplicationRole` in
  `Account2` to access the secret in
  `Account1` and decrypt the secret value by using the encryption
  key which is also in `Account1`. To use this policy, see [Identity-based policies](auth-and-access_iam-policies.md "auth-and-access_iam-policies.md"). You can find the ARN for your secret in the
  Secrets Manager console on the secret details page under **Secret ARN**.
  Alternatively, you can call [`describe-secret`](../../../cli/latest/reference/secretsmanager/describe-secret.md "../../../cli/latest/reference/secretsmanager/describe-secret.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secretName-AbCdEf`"
 },
 {
 "Effect": "Allow",
 "Action": "kms:Decrypt",
 "Resource": "arn:aws:kms:`us-east-1`:`123456789012`:key/`EncryptionKey`"
 }
 ]
}`

```
