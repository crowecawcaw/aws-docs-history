# Using AWS KMS keys for Amazon EFS

Amazon EFS integrates with AWS Key Management Service (AWS KMS) for key management. Amazon EFS uses customer managed keys to
encrypt your file system in the following way:

- **Encrypting metadata at rest** – Amazon EFS uses the
  AWS managed key for Amazon EFS, `aws/elasticfilesystem`, to encrypt and decrypt
  file system metadata (that is, file names, directory names, and directory
  contents).
- **Encrypting file data at rest** – You choose the
  customer managed key used to encrypt and decrypt file data (that is, the contents of your files).
  You can enable, disable, or revoke grants on this customer managed key. This customer managed key can be one
  of the two following types:
  - **AWS managed key for Amazon EFS** – This is the
    default customer managed key, `aws/elasticfilesystem`. You're not charged to
    create and store a customer managed key, but there are usage charges. To learn more, see
    [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").
  - **Customer managed key** – This is the most
    flexible KMS key to use, because you can configure its key policies and grants for
    multiple users or services. For more information on creating customer managed keys, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide._

  If you use a customer managed key for file data encryption and decryption, you can enable
  key rotation. When you enable key rotation, AWS KMS automatically rotates your key
  once per year. Additionally, with a customer managed key, you can choose when to disable,
  re-enable, delete, or revoke access to your customer managed key at any time. For more
  information, see Using AWS KMS keys for Amazon EFS.

###### Important

Amazon EFS accepts only symmetric customer managed keys. You cannot use asymmetric customer managed keys with
Amazon EFS.

Data encryption and decryption at rest are handled transparently. However, AWS account
IDs specific to Amazon EFS appear in your AWS CloudTrail logs related to AWS KMS actions. For more
information, see [Amazon EFS log file entries for encrypted-at-rest
file systems](logging-using-cloudtrail.md#efs-encryption-cloudtrail "logging-using-cloudtrail.md#efs-encryption-cloudtrail").

## Amazon EFS key policies for AWS KMS

Key policies are the primary way to control access to customer managed keys. For more
information on key policies, see [Key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
_AWS Key Management Service Developer Guide._ The following list describes all the
AWS KMS–related permissions that are required or otherwise supported by Amazon EFS for
encrypted at rest file systems:

- **kms:Encrypt** – (Optional) Encrypts plaintext
  into ciphertext. This permission is included in the default key policy.
- **kms:Decrypt** – (Required) Decrypts
  ciphertext. Ciphertext is plaintext that has been previously encrypted. This
  permission is included in the default key policy.
- **kms:ReEncrypt** – (Optional) Encrypts data on
  the server side with a new customer managed key, without exposing the plaintext of the data on
  the client side. The data is first decrypted and then re-encrypted. This permission is
  included in the default key policy.
- **kms:GenerateDataKeyWithoutPlaintext** –
  (Required) Returns a data encryption key encrypted under a customer managed key. This permission
  is included in the default key policy under **kms:GenerateDataKey\***.
- **kms:CreateGrant** – (Required) Adds a grant
  to a key to specify who can use the key and under what conditions. Grants are
  alternate permission mechanisms to key policies. For more information on grants, see
  [Grants in
  AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") in the _AWS Key Management Service Developer Guide._ This
  permission is included in the default key policy.
- **kms:DescribeKey** – (Required) Provides
  detailed information about the specified customer managed key. This permission is included in
  the default key policy.
- **kms:ListAliases** – (Optional) Lists all of
  the key aliases in the account. When you use the console to create an encrypted file
  system, this permission populates the **Select
  KMS key** list. We recommend using this permission to provide the best
  user experience. This permission is included in the default key policy.

### AWS managed key for Amazon EFS KMS

policy

The KMS policy JSON for the AWS managed key for Amazon EFS,
`aws/elasticfilesystem` is as follows:

```
{
    "Version": "2012-10-17",
    "Id": "auto-elasticfilesystem-1",
    "Statement": [
        {
            "Sid": "Allow access to EFS for all principals in the account that are authorized to use EFS",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:CreateGrant",
                "kms:DescribeKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "elasticfilesystem.us-east-2.amazonaws.com",
                    "kms:CallerAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "Allow direct access to key metadata to the account",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:root"
            },
            "Action": [
                "kms:Describe*",
                "kms:Get*",
                "kms:List*",
                "kms:RevokeGrant"
            ],
            "Resource": "*"
        }
    ]
}
```

## Key states and their effects

The state of your KMS key directly affects access to your encrypted file
system:

Enabled

Normal operation - full read and write access to the file system

Disabled

File system becomes inaccessible after a brief period. Can be re-enabled.

Pending deletion

File system becomes inaccessible. Deletion can be canceled during the waiting
period.

Deleted

File system permanently inaccessible. This action cannot be reversed.

###### Warning

If you disable or delete the KMS key used for your file system, or revoke Amazon EFS
access to the key, your file system will become inaccessible. This can result in data loss
if you don't have backups. Always ensure you have proper backup procedures in place before
making changes to encryption keys.
