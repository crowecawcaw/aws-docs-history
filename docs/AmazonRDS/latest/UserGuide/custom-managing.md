# Managing an Amazon RDS Custom for Oracle DB instance

Amazon RDS Custom supports a subset of the usual management tasks for Amazon RDS DB instances.
Following, you can find instructions for the supported RDS Custom for Oracle management tasks using the
AWS Management Console and the AWS CLI.

###### Topics

- [Working with container databases (CDBs) in
  RDS Custom for Oracle](custom-managing.md "custom-managing.md")
- [Working with high availability features for RDS Custom for Oracle](custom-managing.md "custom-managing.md")
- [Customizing your RDS Custom
  environment](custom-managing.md "custom-managing.md")
- [Modifying your RDS Custom for Oracle DB instance](custom-managing.md "custom-managing.md")
- [Changing the character set of an RDS Custom for Oracle DB instance](custom-managing.md "custom-managing.md")
- [Setting the NLS_LANG value in RDS Custom for Oracle](custom-managing.md "custom-managing.md")
- [Support for Transparent Data Encryption](#custom-managing.tde "#custom-managing.tde")
- [Tagging RDS Custom for Oracle resources](custom-managing.md "custom-managing.md")
- [Deleting an RDS Custom for Oracle DB instance](custom-managing.md "custom-managing.md")

## Support for Transparent Data Encryption

RDS Custom supports Transparent Data Encryption (TDE) for RDS Custom for Oracle DB instances.

However, you can't enable TDE using an option in a custom option group as you can in RDS for Oracle. You turn on TDE
manually. For information about using Oracle Transparent Data Encryption, see [Securing stored data using Transparent
Data Encryption](http://docs.oracle.com/cd/E11882_01/network.112/e40393/asotrans.htm#BABFGJAG "http://docs.oracle.com/cd/E11882_01/network.112/e40393/asotrans.htm#BABFGJAG") in the Oracle documentation.
