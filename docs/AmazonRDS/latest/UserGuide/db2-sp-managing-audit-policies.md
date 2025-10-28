# Stored procedures for audit policies for

RDS for Db2

The built-in stored procedures described in this topic manage audit policies for
Amazon RDS for Db2 databases that use audit logging. For more information, see [Db2 audit logging](Db2.Options.md "Db2.Options.md"). To run these procedures, the master user must first
connect to the `rdsadmin` database.

Refer to the following built-in stored procedures for information about their syntax,
parameters, usage notes, and examples.

###### Stored procedures

- [rdsadmin.configure_db_audit](#db2-sp-configure-db-audit "#db2-sp-configure-db-audit")
- [rdsadmin.disable_db_audit](#db2-sp-disable-db-audit "#db2-sp-disable-db-audit")

## rdsadmin.configure_db_audit

Configures the audit policy for the RDS for Db2 database specified by
`db_name`. If the policy you're configuring doesn't exist,
calling this stored procedure creates it. If this policy does exist, calling this stored
procedure modifies it with the parameter values that you provide.

### Syntax

```
db2 "call rdsadmin.configure_db_audit(
    '`db_name`',
    '`category`',
    '`category_setting`',
    '?')"
```

### Parameters

The following parameters are required.

`db_name`

The DB name of the RDS for Db2 database to configure the audit policy
for. The data type is `varchar`.

`category`

The name of the category to configure this audit policy for. The data
type is `varchar`. The following are valid values for this
parameter:

- `ALL` –
  With
  `ALL`, Amazon RDS doesn't include the
  `CONTEXT`, `EXECUTE`, or
  `ERROR` categories.
- `AUDIT`
- `CHECKING`
- `CONTEXT`
- `ERROR`
- `EXECUTE` –
  You
  can configure this category with data or without data. With data
  means to also log input data values provided for any host
  variables and parameter markers. The default is without data.
  For more information, see the description of the
  `category_setting` parameter and
  the [Examples](#db2-sp-configure-db-audit-examples "#db2-sp-configure-db-audit-examples").
- `OBJMAINT`
- `SECMAINT`
- `SYSADMIN`
- `VALIDATE`

For more information about these categories, see the [IBM Db2 documentation](https://www.ibm.com/docs/en/db2/11.1?topic=statements-create-audit-policy "https://www.ibm.com/docs/en/db2/11.1?topic=statements-create-audit-policy").

`category_setting`

The setting for the specified audit category. The data type is
`varchar`.

The following table shows the valid category setting values for each
category.

| Category                                                                       | Valid category settings |
| ------------------------------------------------------------------------------ | ----------------------- | --------------------------------- | ------------ | --------------- | ------------ | --------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ALL` `AUDIT` `CHECKING` `CONTEXT` `OBJMAINT` `SECMAINT` `SYSADMIN` `VALIDATE` | `BOTH                   | FAILURE                           | SUCCESS      | NONE`           |
| `ERROR`                                                                        | `AUDIT                  | NORMAL`. The default is `NORMAL`. |
| `EXECUTE`                                                                      | `BOTH,WITH              | BOTH,WITHOUT                      | FAILURE,WITH | FAILURE,WITHOUT | SUCCESS,WITH | SUCCESS,WITHOUT | NONE` | ### Usage notes Before you call `rdsadmin.configure_db_audit`, make sure the RDS for Db2 DB instance with the database you're configuring the audit policy for is associated with an option group that has the `DB2_AUDIT` option. For more information, see [Setting up Db2 audit logging](Db2.Options.md#db2-audit-setting-up "Db2.Options.md#db2-audit-setting-up"). After you configure the audit policy, you can check the status of the audit configuration for the database by following the steps in [Check the audit configuration](Db2.Options.md#db2-audit-check-config-status "Db2.Options.md#db2-audit-check-config-status"). Specifying `ALL` for the `category` parameter doesn't include the `CONTEXT`, `EXECUTE`, or `ERROR` categories. To add these categories to your audit policy, call `rdsadmin.configure_db_audit` separately with each category that you want to add. For more information, see [Examples](#db2-sp-configure-db-audit-examples "#db2-sp-configure-db-audit-examples"). ### Examples The following examples create or modify the audit policy for a database named `TESTDB`. In examples 1 through 5, if the `ERROR` category wasn't previously configured, this category is set to `NORMAL` (the default). To change that setting to `AUDIT`, follow [Example 6: Specifying the ERROR category](#example-6 "#example-6"). **Example 1: Specifying the `ALL` category** `db2 "call rdsadmin.configure_db_audit('TESTDB', 'ALL', 'BOTH', ?)"` In the example, the call configures the `AUDIT`, `CHECKING`, `OBJMAINT`, `SECMAINT`, `SYSADMIN`, and `VALIDATE` categories in the audit policy. Specifying `BOTH` means that both successful and failing events will be audited for each of these categories. **Example 2: Specifying the `EXECUTE` category with data** `db2 "call rdsadmin.configure_db_audit('TESTDB', 'EXECUTE', 'SUCCESS,WITH', ?)"` In the example, the call configures the `EXECUTE` category in the audit policy. Specifying `SUCCESS,WITH` means that logs for this category will include only successful events, and will include input data values provided for host variables and parameter markers. **Example 3: Specifying the `EXECUTE` category without data** `db2 "call rdsadmin.configure_db_audit('TESTDB', 'EXECUTE', 'FAILURE,WITHOUT', ?)"` In the example, the call configures the `EXECUTE` category in the audit policy. Specifying `FAILURE,WITHOUT` means that logs for this category will include only failing events, and won't include input data values provided for host variables and parameter markers. **Example 4: Specifying the `EXECUTE` category without status events** `db2 "call rdsadmin.configure_db_audit('TESTDB', 'EXECUTE', 'NONE', ?)"` In the example, the call configures the `EXECUTE` category in the audit policy. Specifying `NONE` means that no events in this category will be audited. **Example 5: Specifying the `OBJMAINT` category** `db2 "call rdsadmin.configure_db_audit('TESTDB', 'OBJMAINT', 'NONE', ?)"` In the example, the call configures the `OBJMAINT` category in the audit policy. Specifying `NONE` means that no events in this category will be audited. **Example 6: Specifying the `ERROR` category** `db2 "call rdsadmin.configure_db_audit('TESTDB', 'ERROR', 'AUDIT', ?)"` In the example, the call configures the `ERROR` category in the audit policy. Specifying `AUDIT` means that all errors, including errors occurring within audit logging itself, are captured in the logs. The default error type is `NORMAL`. With `NORMAL`, errors generated by the audit are ignored and only the `SQLCODE`s for errors associated with the operation being performed are captured. ## rdsadmin.disable_db_audit Stops audit logging for the RDS for Db2 database specified by `db_name` and removes the audit policy configured for it. ###### Note This stored procedure only removes audit policies that were configured by calling [rdsadmin.configure_db_audit](#db2-sp-configure-db-audit "#db2-sp-configure-db-audit"). ### Syntax ``db2 "call rdsadmin.disable_db_audit('`db_name`', ?)"`` ### Parameters The following parameters are required. `db_name` The DB name of the RDS for Db2 database to disable audit logging for. The data type is `varchar`. ### Usage notes Calling `rdsadmin.disable_db_audit` doesn't disable audit logging for the RDS for Db2 DB instance. To disable audit logging at the DB instance level, remove the option group from the DB instance. For more information, see [Disabling Db2 audit logging](Db2.Options.md#db2-audit-disabling "Db2.Options.md#db2-audit-disabling"). ### Examples The following example disables audit logging for a database named `TESTDB`. `db2 "call rdsadmin.disable_db_audit('TESTDB', ?)"` |
