

# Changing the character set of an RDS Custom for Oracle DB instance
<a name="custom-managing.character-set"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](RDS-Custom-for-Oracle-end-of-support.md).

RDS Custom for Oracle defaults to the character set US7ASCII. You might want to specify different character sets to meet language or multibyte character requirements. When you use RDS Custom for Oracle, you can pause automation and then change the character set of your database manually.

Changing the character set of an RDS Custom for Oracle DB instance has the following requirements:
+ You can only change the character on a newly provisioned RDS Custom instance that has an empty or starter database with no application data. For all other scenarios, change the character set using DMU (Database Migration Assistant for Unicode).
+ You can only change to a character set supported by RDS for Oracle. For more information, see [Supported DB character sets](Appendix.OracleCharacterSets.md#Appendix.OracleCharacterSets.db-character-set.supported).

**To change the character set of an RDS Custom for Oracle DB instance**

1. Pause RDS Custom automation. For more information, see [Pausing and resuming your RDS Custom DB instance](custom-managing.customizing-env.md#custom-managing.pausing).

1. Log in to your database as a user with `SYSDBA` privileges.

1. Restart the database in restricted mode, change the character set, and then restart the database in normal mode.

   Run the following script in your SQL client:

   ```
   SHUTDOWN IMMEDIATE;
   STARTUP RESTRICT;
   ALTER DATABASE CHARACTER SET INTERNAL_CONVERT AL32UTF8;
   SHUTDOWN IMMEDIATE;
   STARTUP;
   SELECT VALUE FROM NLS_DATABASE_PARAMETERS WHERE PARAMETER = 'NLS_CHARACTERSET';
   ```

   Verify that the output shows the correct character set:

   ```
   VALUE
   --------
   AL32UTF8
   ```

1. Resume RDS Custom automation. For more information, see [Pausing and resuming your RDS Custom DB instance](custom-managing.customizing-env.md#custom-managing.pausing).