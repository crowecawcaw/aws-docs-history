# Encrypt query results with

AWS Key Management Service

By default, CloudWatch Logs encrypts the stored results of your CloudWatch Logs Insights queries using the
default CloudWatch Logs server-side encryption method. You can choose to use a AWS KMS key to
encrypt these results instead. If you associate a AWS KMS key with your encryption
results, then CloudWatch Logs uses that key to encrypt the stored results of all queries in the
account.

If you later disassociate a the key from your query results, CloudWatch Logs goes back to the
default encryption method for later queries. But the queries that ran while the key was
associated are still encrypted with that key. CloudWatch Logs can still return those results after
the KMS key is disassociated, because CloudWatch Logs can still continue to reference the key.
However, if the key is later disabled, then CloudWatch Logs is unable to read the query results
that were encrypted with that key.

###### Important

CloudWatch Logs supports only symmetric KMS keys. Do not use an asymmetric key to encrypt
your query results. For more information, see [Using Symmetric and Asymmetric
Keys](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md").

## Limits

- To perform the following steps, you must have the following permissions:
  `kms:CreateKey`, `kms:GetKeyPolicy`, and
  `kms:PutKeyPolicy`.
- After you associate or disassociate a key from your query results, it can
  take up to five minutes for the operation to take effect.
- If you revoke CloudWatch Logs access to an associated key or delete an associated
  KMS key, your encrypted data in CloudWatch Logs can no longer be retrieved.
- You can't use the CloudWatch console to associate a key, you must use the AWS CLI
  or CloudWatch Logs API.

## Step 1: Create an AWS KMS key

To create a KMS key use the following [create-key](../../../cli/latest/reference/kms/create-key.md "../../../cli/latest/reference/kms/create-key.md") command:

```
`aws kms create-key`
```

The output contains the key ID and Amazon Resource Name (ARN) of the key. The
following is example output:

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

By default, all KMS keys are private. Only the resource owner can use it to
encrypt and decrypt data. However, the resource owner can grant permissions to
access the key to other users and resources. With this step, you give the CloudWatch Logs
service principal permission to use the key. This service principal must be in the
same AWS Region where the key is stored.

As a best practice, we recommend that you restrict the use of the key to only
those AWS accounts that you specify.

First, save the default policy for your KMS key as
`policy.json` using the following [get-key-policy](../../../cli/latest/reference/kms/get-key-policy.md "../../../cli/latest/reference/kms/get-key-policy.md")
command:

```
`aws kms get-key-policy --key-id `key-id` --policy-name default --output text > ./policy.json`
```

Open the `policy.json` file in a text editor and add the
section in bold from one of the following statements. Separate the existing
statement from the new statement with a comma. These statements use
`Condition` sections to enhance the security of the AWS KMS key. For
more information, see [AWS KMS keys and encryption context](encrypt-log-data-kms.md#encrypt-log-data-kms-policy "encrypt-log-data-kms.md#encrypt-log-data-kms-policy").

The `Condition` section in this example limits the use of the AWS KMS key
to the CloudWatch Logs Insights query results in the specified account.

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
 "kms:Encrypt*",
 "kms:Decrypt*",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:Describe*"
 ],
 "Resource": "*",
 "Condition": {
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:logs:`us-east-1`:`111122223333`:query-result:*"
 },
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 }
 }
 }
 ]
}`

```

Finally, add the updated policy using the following [put-key-policy](../../../cli/latest/reference/kms/put-key-policy.md "../../../cli/latest/reference/kms/put-key-policy.md")
command:

```
aws kms put-key-policy --key-id `key-id` --policy-name default --policy file://policy.json
```

## Step 3: Associate a KMS key with your query

results

###### To associate the KMS key with the query results in the account

Use the [disassociate-kms-key](../../../cli/latest/reference/logs/disassociate-kms-key.md "../../../cli/latest/reference/logs/disassociate-kms-key.md") command as follows:

```
`aws logs associate-kms-key --resource-identifier "arn:aws:logs:`region`:`account-id`:query-result:*" --kms-key-id "`key-arn`"`
```

## Step 4: Disassociate a key from query

results in the account

To disassociate the KMS key associated with query results, use the following
[disassociate-kms-key](../../../cli/latest/reference/logs/disassociate-kms-key.md "../../../cli/latest/reference/logs/disassociate-kms-key.md") command:

```
`aws logs disassociate-kms-key --resource-identifier "arn:aws:logs:`region`:`account-id`:query-result:*"`
```
