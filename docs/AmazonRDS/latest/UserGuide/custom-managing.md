

# Managing an Amazon RDS Custom for Oracle DB instance
<a name="custom-managing"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

Amazon RDS Custom supports a subset of the usual management tasks for Amazon RDS DB instances. Following, you can find instructions for the supported RDS Custom for Oracle management tasks using the AWS Management Console and the AWS CLI.

**Topics**
+ [Working with container databases (CDBs) in RDS Custom for Oracle](custom-managing.multitenant.md)
+ [Working with high availability features for RDS Custom for Oracle](custom-managing.ha.md)
+ [Customizing your RDS Custom environment](custom-managing.customizing-env.md)
+ [Modifying your RDS Custom for Oracle DB instance](custom-managing.modifying.md)
+ [Changing the character set of an RDS Custom for Oracle DB instance](custom-managing.character-set.md)
+ [Setting the NLS\_LANG value in RDS Custom for Oracle](custom-managing.nlslang.md)
+ [Support for Transparent Data Encryption](#custom-managing.tde)
+ [Tagging RDS Custom for Oracle resources](custom-managing.tagging.md)
+ [Deleting an RDS Custom for Oracle DB instance](custom-managing.deleting.md)

## Support for Transparent Data Encryption
<a name="custom-managing.tde"></a>

RDS Custom supports Transparent Data Encryption (TDE) for RDS Custom for Oracle DB instances.

However, you can't enable TDE using an option in a custom option group as you can in RDS for Oracle. You turn on TDE manually. For information about using Oracle Transparent Data Encryption, see [Securing stored data using Transparent Data Encryption](http://docs.oracle.com/cd/E11882_01/network.112/e40393/asotrans.htm#BABFGJAG) in the Oracle documentation.