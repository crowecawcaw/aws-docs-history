# Tagging RDS Custom for SQL Server resources

You can tag RDS Custom resources as with Amazon RDS resources, but with some important differences:

- Don't create or modify the `AWSRDSCustom` tag that's required for RDS Custom automation. If you do, you
  might break the automation.
- The `Name` tag is added to RDS Custom resources with the prefix
  `do-not-delete-rds-custom`. Any customer-passed value for the key is
  overwritten.
- Tags added to RDS Custom DB instances during creation are propagated to all other related RDS Custom resources.
- Tags aren't propagated when you add them to RDS Custom resources after DB instance creation.
  For general information about resource tagging, see [Tagging Amazon RDS resources](USER_Tagging.md "USER_Tagging.md").
