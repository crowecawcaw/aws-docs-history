# Working with custom engine versions for Amazon RDS Custom for Oracle

###### Note

End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md "RDS-Custom-for-Oracle-end-of-support.md").

A _custom engine version (CEV)_ for Amazon RDS Custom for Oracle is a binary volume
snapshot of a database engine and specific Amazon Machine Image (AMI). By default, RDS Custom for Oracle uses the
latest available AMI managed by RDS Custom, but you can specify an AMI that was used in a previous CEV. You store your database
installation files in Amazon S3. RDS Custom uses the installation files and the AMI to create your
CEV for you.

###### Topics

- [Preparing to create a CEV](custom-cev.preparing.md "custom-cev.preparing.md")
- [Creating a CEV](custom-cev.create.md "custom-cev.create.md")
- [Modifying CEV status](custom-cev.modify.md "custom-cev.modify.md")
- [Viewing CEV details for Amazon RDS Custom for Oracle](custom-cev.view.md "custom-cev.view.md")
- [Deleting a CEV](custom-cev.delete.md "custom-cev.delete.md")
