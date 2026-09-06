

# Oracle Transparent Data Encryption
<a name="Appendix.Oracle.Options.AdvSecurity"></a>

Amazon RDS supports Oracle Transparent Data Encryption (TDE), a feature of the Oracle Advanced Security option available in Oracle Enterprise Edition. This feature automatically encrypts data before it is written to storage and automatically decrypts data when the data is read from storage. This option is only supported for the Bring Your Own License (BYOL) model.

TDE is useful in scenarios where you need to encrypt sensitive data in case data files and backups are obtained by a third party. TDE is also useful when you need to comply with security-related regulations. 

A detailed explanation about TDE in Oracle Database is beyond the scope of this guide. For information, see the following Oracle Database resources:
+ [Introduction to Transparent Data Encryption](https://docs.oracle.com/en/database/oracle/oracle-database/19/asoag/introduction-to-transparent-data-encryption.html#GUID-62AA9447-FDCD-4A4C-B563-32DE04D55952) in the Oracle Database documentation
+ [Oracle advanced security](https://www.oracle.com/security/database-security/) in the Oracle Database documentation
+ [Oracle advanced security Transparent Data Encryption best practices](https://www.oracle.com/br/a/tech/docs/technical-resources/twp-transparent-data-encryption-bestpractices.pdf), which is an Oracle whitepaper

For more information about using TDE with RDS for Oracle, see the following blogs:
+ [Oracle Database Encryption Options on Amazon RDS](https://aws.amazon.com/blogs/apn/oracle-database-encryption-options-on-amazon-rds/)
+ [Migrate a cross-account TDE-enabled Amazon RDS for Oracle DB instance with reduced downtime using AWS DMS](https://aws.amazon.com/blogs/database/migrate-a-cross-account-tde-enabled-amazon-rds-for-oracle-db-instance-with-reduced-downtime-using-aws-dms/)

## TDE encryption modes
<a name="Appendix.Oracle.Options.AdvSecurity.Modes"></a>

Oracle Transparent Data Encryption supports two encryption modes: TDE tablespace encryption and TDE column encryption. TDE tablespace encryption is used to encrypt entire application tables. TDE column encryption is used to encrypt individual data elements that contain sensitive data. You can also apply a hybrid encryption solution that uses both TDE tablespace and column encryption. 

**Note**  
Amazon RDS manages the Oracle Wallet and TDE master key for the DB instance. You do not need to set the encryption key using the command `ALTER SYSTEM set encryption key`. 

After you enable the `TDE` option, you can check the status of the Oracle Wallet by using the following command: 

```
SELECT * FROM v$encryption_wallet;
```

To create an encrypted tablespace, use the following command:

```
CREATE TABLESPACE encrypt_ts ENCRYPTION DEFAULT STORAGE (ENCRYPT);
```

To specify the encryption algorithm, use the following command:

```
CREATE TABLESPACE encrypt_ts ENCRYPTION USING 'AES256' DEFAULT STORAGE (ENCRYPT);
```

The previous statements for encrypting a tablespace are the same as you would use on an on-premises Oracle database.

## Restrictions for the TDE option
<a name="Appendix.Oracle.Options.Timezone.Restrictions"></a>

The TDE option is permanent and persistent. After you associate your DB instance with an option group that has the TDE option enabled, you can't do the following actions:
+ Disable the `TDE` option in the currently associated option group.
+ Associate your DB instance with a different option group that doesn't include the `TDE` option.
+ Share a DB snapshot that uses the `TDE` option. For more information about sharing DB snapshots, see [Sharing a DB snapshot for Amazon RDS](USER_ShareSnapshot.md).

For more information about persistent and permanent options, see [Persistent and permanent options](USER_WorkingWithOptionGroups.md#Overview.OptionGroups.Permanent).

## Determining whether your DB instance is using TDE
<a name="Appendix.Oracle.Options.AdvSecurity.Querying"></a>

You might want to determine whether your DB instance is associated with an option group that has the `TDE` option enabled. To view the option group that a DB instance is associated with, use the RDS console, the [describe-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) AWS CLI command, or the API operation [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html).

## Adding the TDE option
<a name="Appendix.Oracle.Options.AdvSecurity.Add"></a>

**Important**  
The TDE option is permanent and cannot be removed from a DB instance. If you need to reverse this decision later, you must decrypt all data, export it, and import into a new DB instance without TDE. Plan accordingly before enabling TDE.

To add the `TDE` option to your DB instance, complete the following steps:

1. (Recommended) Take a snapshot of your DB instance.

1. Do one of the following tasks:
   + Create a new option group from scratch. For more information, see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create).
   + Copy an existing option group using the AWS CLI or API. For more information, see [Copying an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Copy).
   + Reuse an existing non-default option group. A best practice is to use an option group that isn't currently associated with any DB instances or snapshots.

1. Add the new option to the option group from the preceding step.

1. If the option group that is currently associated with your DB instance has options enabled, add these options to your new option group. This strategy prevents the existing options from being uninstalled while enabling the new option.

1. Add the new option group to your DB instance.

### Console
<a name="Appendix.Oracle.Options.TDE.Console"></a>

**To add the TDE option to an option group and associate it with your DB instance**

1. In the RDS console, choose **Option groups.**

1. Choose the name of the option group to which you want to add the option.

1. Choose **Add option**.

1. For **Option name**, choose **TDE**, and then configure the option settings. 

1. Choose **Add option**.
**Important**  
If you add the **TDE** option to an option group that is currently attached to one or more DB instances, a brief outage occurs while all the DB instances are automatically restarted. 

   For more information about adding options, see [Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption).

1. Associate the option group with a new or existing DB instance: 
   + For a new DB instance, apply the option group when you launch the instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md). 
   + For an existing DB instance, apply the option group by modifying the instance and attaching the new option group. The DB instance doesn't restart as part of this operation. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md). 

### AWS CLI
<a name="Appendix.Oracle.Options.TDE.CLI"></a>

In the following example, you use the AWS CLI [add-option-to-option-group](https://docs.aws.amazon.com/cli/latest/reference/rds/add-option-to-option-group.html) command to add the `TDE` option to an option group called `myoptiongroup`.

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
    --option-group-name "{{myoptiongroup}}" \
    --options "{{OptionName=TDE}}" \
    --apply-immediately
```

For Windows:

```
aws rds add-option-to-option-group ^
    --option-group-name "{{myoptiongroup}}" ^
    --options "{{OptionName=TDE}}" ^
    --apply-immediately
```

## Copying your data to a DB instance that doesn't include the TDE option
<a name="Appendix.Oracle.Options.AdvSecurity.Remove"></a>

You can't remove the TDE option from a DB instance or associate it with an option group that doesn't include the TDE option. To migrate your data to an instance that doesn't include the TDE option, do the following: 

1.  Decrypt the data on your DB instance. 

1.  Copy the data to a new DB instance that is not associated with an option group that has `TDE` enabled. 

1.  Delete your original DB instance.

You can use the same name for the new instance as the previous DB instance.

## Considerations when using TDE with Oracle Data Pump
<a name="Appendix.Oracle.Options.AdvSecurity.Pump"></a>

You can use Oracle Data Pump to import or export encrypted dump files. Amazon RDS supports the password encryption mode `(ENCRYPTION_MODE=PASSWORD)` for Oracle Data Pump. Amazon RDS does not support transparent encryption mode `(ENCRYPTION_MODE=TRANSPARENT)` for Oracle Data Pump. For more information, see [Importing using Oracle Data Pump](Oracle.Procedural.Importing.DataPump.md). 