On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Key management

CodeGuru Security encrypts your data using one of two types of KMS keys:

- An AWS owned KMS key. This is the default encryption method.
- A customer managed KMS key. To use your own KMS key, you need to create the key and
  then provide a key policy to grant permissions to CodeGuru Security to use the key.
  The following sections explain how to create and use a customer managed KMS key to encrypt your
  data.

## Create a customer managed KMS key

You can create customer managed KMS key using either the AWS KMS console or the
[`CreateKey`](../../../kms/latest/APIReference/API_CreateKey.md "../../../kms/latest/APIReference/API_CreateKey.md") API. When creating the key, you can use an existing
symmetric key in your account or create a symmetric customer managed KMS key. CodeGuru Security
does not support
[asymmetric KMS keys](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md"). Additionally, you will need a AWS KMS key in the same
AWS Region as your scans, or a
[multi-region key](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md"). For more information see
[Creating symmetric
encryption AWS KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS KMS user guide_.

## Permissions for code encryption with a customer managed

KMS key

To use your encryption key, you need to create a policy that allows access to
AWS KMS key actions and a policy that allows Amazon CodeGuru Security to use those
actions.

If you are setting, updating, or resetting the encryption key for your account it is
recommended to use an Amazon CodeGuru Security administrator policy, such as
`AmazonCodeGuruSecurityFullAccess`.

The key policy for KMS must allow the following actions:

- `kms:CreateGrant`
- `kms:Decrypt`
- `kms:DescribeKey`
- `kms:GenerateDataKeyWithoutPlainText`
- `kms:Encrypt`
- `kms:RetireGrant`

After you've verified that you have the correct KMS permissions in your key policy, you
must create a policy to attach to your CodeGuru Security access role that allows CodeGuru Security to use
your key for encryption. Add the following statements to your policy and replace
`<region>` with the AWS Region where you are running
CodeGuru Security scans:

```
  {
    "Effect": "Allow",
      "Action": "kms:CreateGrant",
      "Resource": "*",
      "Condition": {
          "ForAllValues:StringEquals": {
              "kms:GrantOperations": [
                  "GenerateDataKey",
                  "GenerateDataKeyWithoutPlaintext",
                  "Encrypt",
                  "Decrypt",
                  "RetireGrant",
                  "DescribeKey"
              ]
          },
          "StringEquals": {
              "kms:ViaService": [
                  "codeguru-security.`<region>`.amazonaws.com"
              ]
          }
      }
  },
  {
      "Effect": "Allow",
      "Action": [
          "kms:Encrypt",
          "kms:Decrypt",
          "kms:RetireGrant",
          "kms:DescribeKey",
          "kms:GenerateDataKeyWithoutPlaintext"
      ],
      "Resource": "*",
      "Condition": {
          "StringEquals": {
              "kms:ViaService": [
                  "codeguru-security.`<region>`.amazonaws.com"
              ]
          }
      }
  }
```

For information on key policies, see
[Using
Key Policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

## Configure encryption with the Amazon CodeGuru Security

API

To set a customer managed key for encryption, use the
[`UpdateAccountConfiguration`](../security-api/API_UpdateAccountConfiguration.md "../security-api/API_UpdateAccountConfiguration.md")
operation. In the API request, for the
`EncryptionConfig` object, use the `kmsKeyArn` field to
specify the ARN of the AWS KMS encryption key you want to use. If you call
`UpdateAccountConfiguration` and pass `null` or nothing for
`kmsKeyArn`, an AWS owned key will be used for encryption.

To view the current KMS key ARN that is being used for encryption, call
`GetAccountConfiguration`. If you attempt to use
`GetAccountConfiguration` when you haven't set a
customer managed key, the operation returns `null` which means that
an AWS owned key is being used for encryption.

If you delete the key or change it's policy to deny access to Amazon CodeGuru Security you will be
unable to access your findings and dashboard metrics and code scans will fail for your
account.
