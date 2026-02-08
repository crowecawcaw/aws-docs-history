# Changing the character set of an RDS Custom for Oracle DB instance

RDS Custom for Oracle defaults to the character set US7ASCII. You might want to specify different character sets to meet language or multibyte character
requirements. When you use RDS Custom for Oracle, you can pause automation and then change the character set of your database manually.

Changing the character set of an RDS Custom for Oracle DB instance has the following requirements:

- You can only change the character on a newly provisioned RDS Custom instance that has an empty or starter database with no
  application data. For all other scenarios, change the character set using DMU (Database Migration Assistant for Unicode).
- You can only change to a character set supported by RDS for Oracle. For more information, see [Supported DB character sets](Appendix.md#Appendix.OracleCharacterSets.db-character-set.supported "Appendix.md#Appendix.OracleCharacterSets.db-character-set.supported").

###### To change the character set of an RDS Custom for Oracle DB instance

1. Pause RDS Custom automation. For more information, see [Pausing and resuming your RDS Custom DB instance](custom-managing.md#custom-managing.pausing "custom-managing.md#custom-managing.pausing").
2. Log in to your database as a user with `SYSDBA` privileges.
3. Restart the database in restricted mode, change the character set, and then restart the database in normal mode.

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

4. Resume RDS Custom automation. For more information, see [Pausing and resuming your RDS Custom DB instance](custom-managing.md#custom-managing.pausing "custom-managing.md#custom-managing.pausing").
