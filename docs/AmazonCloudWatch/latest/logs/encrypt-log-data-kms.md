# Encrypt log data in CloudWatch Logs using AWS Key Management Service

Log group data is always encrypted in CloudWatch Logs. By default, CloudWatch Logs uses server-side encryption with
256-bit Advanced Encryption Standard Galois/Counter Mode (AES-GCM) to encrypt log data at rest. As an alternative, you can use AWS Key Management Service
for this encryption. If you do, the encryption is done using an AWS KMS key.
Encryption using AWS KMS is enabled at the log group level, by associating a KMS key with a log

group, either when you create the log group or after it exists.

###### Important

CloudWatch Logs now supports encryption context, using `kms:EncryptionContext:aws:logs:arn`
as the key and the ARN of the log group as the value for that key.
If you have log groups
that you have already encrypted with a KMS key, and you would like to restrict
the key to be used with a single account and log group, you should assign a new KMS key that
includes a condition in the IAM policy. For more information, see
[AWS KMS keys and encryption context](#encrypt-log-data-kms-policy "#encrypt-log-data-kms-policy").

###### Important

CloudWatch Logs now supports `kms:ViaService` which allows logs to make AWS KMS calls on your behalf. You should add this to your roles which call CloudWatch Logs in either your Key Policy or in IAM. For more information, see
[kms:ViaService](../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-via-service "../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-via-service").

After you associate a KMS key with a log group, all newly ingested data for the log group is
encrypted using this key. This data is stored in encrypted format throughout its retention
period. CloudWatch Logs decrypts this data whenever it is requested. CloudWatch Logs must have permissions for
the KMS key whenever encrypted data is requested.

If you later disassociate a KMS key from a log group, CloudWatch Logs encrypts newly ingested
data using the CloudWatch Logs
default encryption method. All previously ingested data that was encrypted with the KMS key
remains encrypted with the KMS key. CloudWatch Logs
can still return that data after the KMS key is disassociated, because CloudWatch Logs can still continue to reference
the key. However, if the key is later disabled, then CloudWatch Logs is unable to read the logs
that were encrypted with that key.

###### Important

CloudWatch Logs supports only symmetric KMS keys. Do not use an asymmetric key to encrypt the data in your log groups.
For more information, see [Using Symmetric and Asymmetric Keys](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md").

## Limits

- To perform the following steps, you must have the
  following permissions: `kms:CreateKey`, `kms:GetKeyPolicy`, and
  `kms:PutKeyPolicy`.
- After you associate or disassociate a key from a log group, it can take up
  to five minutes for the operation to take effect.
- If you revoke CloudWatch Logs access to an associated key or delete an associated KMS key,
  your encrypted data in CloudWatch Logs can no longer be retrieved.
- You can't associate a KMS key with an existing log group using the CloudWatch console.

## Step 1: Create an AWS KMS key

To create an KMS key, use the following [create-key](../../../cli/latest/reference/kms/create-key.md "../../../cli/latest/reference/kms/create-key.md") command:

```
`aws kms create-key`
```

The output contains the key ID and Amazon Resource Name (ARN) of the key.
The following is example output:

```
{
    "KeyMetadata": {
        "Origin": "AWS_KMS",
        "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "Description": "",
        "KeyManager": "CUSTOMER",
        "Enabled": true,
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "KeyState": "Enabled",
        "CreationDate": 1478910250.94,
        "Arn": "arn:aws:kms:us-west-2:123456789012:key/6f815f63-e628-448c-8251-e40cb0d29f59",
        "AWSAccountId": "123456789012",
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ]
    }
}
```

## Step 2: Set permissions on the KMS key

By default, all AWS KMS keys are private. Only the resource owner can use it to
encrypt and decrypt data. However, the resource owner can grant permissions to
access the KMS key to other users and resources. With this step, you give the CloudWatch Logs
service principal and the caller role permission to use the key. This service principal must be in the
same AWS Region where the KMS key is stored.

As a best practice, we recommend that you restrict the use of the KMS key to only
those AWS accounts or log groups you specify.

First, save the default policy for your KMS key as `policy.json` using the
following [get-key-policy](../../../cli/latest/reference/kms/get-key-policy.md "../../../cli/latest/reference/kms/get-key-policy.md") command:

```
`aws kms get-key-policy --key-id `key-id` --policy-name default --output text > ./policy.json`
```

Open the `policy.json` file in a text editor and add
the section in bold from one of the following statements. Separate the existing statement from
the new statement with a comma. These statements use `Condition` sections
to enhance the security of the AWS KMS key. For more information, see [AWS KMS keys and encryption context](#encrypt-log-data-kms-policy "#encrypt-log-data-kms-policy").

The `Condition` section in this example restricts the
key to a single log group ARN.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "key-default-1",
 "Statement": [
 {
 "Sid": "Enable IAM User Permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.`us-east-1`.amazonaws.com"
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:Describe*"
 ],
 "Resource": "*",
 "Condition": {
 "ArnEquals": {
 "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:`us-east-1`:`111122223333`:log-group:`log-group-name`"
 }
 }
 }
 ]
}`

```

The `Condition` section in this example limits the use of the
AWS KMS key to the specified account, but it can be used
for any log group.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "key-default-1",
 "Statement": [
 {
 "Sid": "Enable IAM User Permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.`us-east-1`.amazonaws.com"
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:Describe*"
 ],
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:`us-east-1`:`123456789012`:*"
 }
 }
 }
 ]
}`

```

Next, add permissions to the role which will be calling the CloudWatch Logs. You can do this by adding an additional statement to the AWS KMS Key Policy or through
IAM on the role itself. CloudWatch Logs uses `kms:ViaService` to make calls to AWS KMS on the customer’s behalf. For more information, see
[kms:ViaService](../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-via-service "../../../kms/latest/developerguide/conditions-kms.md#conditions-kms-via-service").

To add permissions in the AWS KMS Key Policy, add the following additional statement to your key policy. If you use this method, as best practice,
scope the policy to only the roles that will be interacting with AWS KMS encrypted log groups.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::`account_id`:role/`role_name`"
  },
  "Action": [
    "kms:Encrypt",
    "kms:ReEncrypt*",
    "kms:Decrypt",
    "kms:GenerateDataKey*",
    "kms:Describe*"
  ],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:ViaService": [
        "logs.`region`.amazonaws.com"
      ]
    }
  }
}


```

Alternatively if you would like to manage role permissions in IAM, you can add equivalent permissions through the following policy. This can be added to an existing
role policy or attached to a role as an additional separate policy. If you use this method, as best practice, scope the policy to only the AWS KMS keys which will be used for log
encryption. For more information, see [Edit IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Encrypt",
 "kms:ReEncrypt*",
 "kms:Decrypt",
 "kms:GenerateDataKey*",
 "kms:Describe*"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": [
 "logs.`us-east-1`.amazonaws.com"
 ]
 }
 },
 "Resource": "arn:aws:kms:`us-east-1`:`444455556666`:key/`key_id`"
 }
 ]
}`

```

Finally, add the updated policy using the following [put-key-policy](../../../cli/latest/reference/kms/put-key-policy.md "../../../cli/latest/reference/kms/put-key-policy.md") command:

```
aws kms put-key-policy --key-id `key-id` --policy-name default --policy file://policy.json
```

## Step 3: Associate a KMS key with a log group

You can associate a KMS key with a log group when you create it or after it
exists.

To find whether a log group already has a KMS key associated, use the
following [describe-log-groups](../../../cli/latest/reference/logs/describe-log-groups.md "../../../cli/latest/reference/logs/describe-log-groups.md") command:

```
`aws logs describe-log-groups --log-group-name-prefix "`log-group-name-prefix`"`
```

If the output includes a `kmsKeyId` field, the log group is associated with
the key displayed for the value of that field.

###### To associate the KMS key with a log group when you create it

Use the [create-log-group](../../../cli/latest/reference/logs/create-log-group.md "../../../cli/latest/reference/logs/create-log-group.md")
command as follows:

```
`aws logs create-log-group --log-group-name `my-log-group` --kms-key-id "`key-arn`"`
```

###### To associate the KMS key with an existing log group

Use the [associate-kms-key](../../../cli/latest/reference/logs/associate-kms-key.md "../../../cli/latest/reference/logs/associate-kms-key.md")
command as follows:

```
`aws logs associate-kms-key --log-group-name `my-log-group` --kms-key-id "`key-arn`"`
```

## Step 4: Disassociate key from a log group

To disassociate the KMS key associated with a log group, use the following [disassociate-kms-key](../../../cli/latest/reference/logs/disassociate-kms-key.md "../../../cli/latest/reference/logs/disassociate-kms-key.md") command:

```
`aws logs disassociate-kms-key --log-group-name `my-log-group``
```

## AWS KMS keys and encryption context

To enhance the security of your AWS Key Management Service keys and your encrypted log groups, CloudWatch Logs now puts
log group ARNs as part of the _encryption context_ used to
encrypt your log data. Encryption context
is a set of key-value pairs that are used as additional authenticated data. The encryption
context enables you to use IAM policy conditions to limit access to your AWS KMS key by AWS
account and log group. For more information,
see [Encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context")
and [IAM JSON Policy
Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md").

We recommend that you use different KMS keys for each of your encrypted log groups.

If you have a log group that you encrypted previously and now want to change the log
group to use a new KMS key that works only for that log group, follow these
steps.

###### To convert an encrypted log group to use a KMS key with a policy limiting it to that log group

1. Enter the following command to find the ARN of the log group's current key:

```
aws logs describe-log-groups
```

The output includes the following line. Make a note of the ARN. You need to use it
in step 7.

```
...
"kmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/01234567-89ab-cdef-0123-456789abcdef"
...
```

2. Enter the following command to create a new KMS key:

```
aws kms create-key
```

3. Enter the following command to save the new key's policy to a `policy.json`
   file:

```
aws kms get-key-policy --key-id `new-key-id` --policy-name default --output text > ./policy.json
```

4. Use a text editor to open `policy.json` and add a `Condition`
   expression to the policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "key-default-1",
 "Statement": [
 {
 "Sid": "Enable IAM User Permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.`us-east-1`.amazonaws.com"
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:Describe*"
 ],
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:`us-east-1`:`111122223333`:log-group:`LOG-GROUP-NAME`"
 }
 }
 }
 ]
}`

```

5. Enter the following command to add the updated policy to the new KMS key:

```
aws kms put-key-policy --key-id `new-key-ARN` --policy-name default --policy file://policy.json
```

6. Enter the following command to associate the policy with your log group:

```
aws logs associate-kms-key --log-group-name `my-log-group` --kms-key-id `new-key-ARN`
```

CloudWatch Logs now encrypts all new data using the new key. 7. Next, revoke all permissions except `Decrypt` from the old key. First, enter the
following command to retrieve the old policy:

```
aws kms get-key-policy --key-id `old-key-ARN` --policy-name default --output text > ./policy.json
```

8. Use a text editor to open `policy.json` and remove all values from the `Action` list, except
   for `kms:Decrypt`

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "key-default-1",
 "Statement": [
 {
 "Sid": "Enable IAM User Permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.`region`.amazonaws.com"
 },
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "*"
 }
 ]
}`

```

9. Enter the following command to add the updated policy to the old key:

```
aws kms put-key-policy --key-id `old-key-ARN` --policy-name default --policy file://policy.json
```
