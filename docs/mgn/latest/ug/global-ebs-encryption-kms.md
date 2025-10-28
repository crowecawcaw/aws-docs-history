NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Using an AWS KMS customer managed key

for encryption in member account

If you decide to use a customer managed key, or if your default Amazon EBS encryption key is a customer managed key
in member account, you must add permissions to the
AWSApplicationMigrationSharingRole\_<MANAGEMENT_ACCOUNT_ID> to allow management account
to use it.

Using Administrator access, add these permissions to the
AWSApplicationMigrationSharingRole\_<MANAGEMENT_ACCOUNT_ID>:
