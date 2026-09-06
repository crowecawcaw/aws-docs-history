

# Tagging RDS Custom for Oracle resources
<a name="custom-managing.tagging"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

You can tag RDS Custom resources as with Amazon RDS resources, but with some important differences:
+ Don't create or modify the `AWSRDSCustom` tag that's required for RDS Custom automation. If you do, you might break the automation.
+ The `Name` tag is added to RDS Custom resources with prefix value of `do-not-delete-rds-custom` or `rds-custom!oracle-do-not-delete`. Any customer-passed value for the key is overwritten.
+ Tags added to RDS Custom DB instances during creation are propagated to all other related RDS Custom resources.
+ Tags aren't propagated when you add them to RDS Custom resources after DB instance creation.

For general information about resource tagging, see [Tagging Amazon RDS resources](USER_Tagging.md).