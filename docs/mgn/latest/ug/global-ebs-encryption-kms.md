

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Using an AWS KMS customer managed key for encryption in member account
<a name="global-ebs-encryption-kms"></a>

If you decide to use a customer managed key, or if your default Amazon EBS encryption key is a customer managed key in member account, you must add permissions to the AWSApplicationMigrationSharingRole\_<MANAGEMENT\_ACCOUNT\_ID> to allow management account to use it.

Using Administrator access, add these permissions to the AWSApplicationMigrationSharingRole\_<MANAGEMENT\_ACCOUNT\_ID>: