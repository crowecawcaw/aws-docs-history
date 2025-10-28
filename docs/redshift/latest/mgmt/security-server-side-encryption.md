Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Encryption at rest

Server-side encryption is about data encryption at rest—that is, Amazon Redshift optionally encrypts your
data as it writes it in its data centers and decrypts
it for you when you access it. As long as you authenticate your request and you have
access permissions, there is no difference in the way you access encrypted or
unencrypted data.

Amazon Redshift protects data at rest through encryption. Optionally, you can protect all data stored on
disks within a cluster and all backups in Amazon S3 with Advanced Encryption Standard AES-256.

To manage the keys used for encrypting and decrypting your Amazon Redshift resources, you use
[AWS Key Management Service (AWS KMS)](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md"). AWS KMS combines secure,
highly available hardware and software to provide a key management system scaled for the cloud.
Using AWS KMS, you can create encryption keys and define the policies that control how these keys
can be used. AWS KMS supports AWS CloudTrail, so you can audit key usage to verify that keys are being
used appropriately. You can use your AWS KMS keys in combination with Amazon Redshift and supported AWS
services.. For a list of services that
support AWS KMS, see [How AWS Services Use AWS KMS](../../../kms/latest/developerguide/services.md "../../../kms/latest/developerguide/services.md")
in the _AWS Key Management Service Developer Guide_.

If you choose to manage your provisioned cluster or serverless namespace's admin password using AWS Secrets Manager,
Amazon Redshift also accepts an additional AWS KMS key that AWS Secrets Manager uses to encrypt your credentials.
This additional key can be an automatically generated key from AWS Secrets Manager, or a custom key that you provide.

Amazon Redshift query editor v2 securely stores information entered into the query editor as follows:

- The Amazon Resource Name (ARN) of the KMS key used to encrypt query editor v2 data.
- Database connection information.
- Names and content of files and folders.
  Amazon Redshift query editor v2 encrypts information using block-level encryption with either your KMS key or the service account KMS key.
  The encryption of your Amazon Redshift data is controlled by your Amazon Redshift cluster properties.

###### Topics

- [Amazon Redshift database encryption](working-with-db-encryption.md "working-with-db-encryption.md")
