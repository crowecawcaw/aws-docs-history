

# Stored procedures for audit policies for RDS for Db2

The built-in stored procedures described in this topic manage audit policies for Amazon RDS for Db2 databases that use audit logging. Use [rdsadmin.configure\_db\_audit](#db2-sp-configure-db-audit) and [rdsadmin.disable\_db\_audit](#db2-sp-disable-db-audit) to manage database-level audit logging. For more information, see [Db2 audit logging](Db2.Options.Audit.md). Use the other stored procedures in this topic to manage object-level audit policies. For more information, see [Db2 object-level audit policies](db2-object-level-audit.md). To run these procedures, the master user must first connect to the `rdsadmin` database.

Refer to the following built-in stored procedures for information about their syntax, parameters, usage notes, and examples.

**Topics**
+ [rdsadmin.configure\_db\_audit](#db2-sp-configure-db-audit)
+ [rdsadmin.disable\_db\_audit](#db2-sp-disable-db-audit)
+ [rdsadmin.create\_audit\_policy](#db2-sp-create-audit-policy)
+ [rdsadmin.alter\_audit\_policy](#db2-sp-alter-audit-policy)
+ [rdsadmin.attach\_audit\_policy](#db2-sp-attach-audit-policy)
+ [rdsadmin.detach\_audit\_policy](#db2-sp-detach-audit-policy)
+ [rdsadmin.drop\_audit\_policy](#db2-sp-drop-audit-policy)

## rdsadmin.configure\_db\_audit
<a name="db2-sp-configure-db-audit"></a>

Configures the audit policy for the RDS for Db2 database specified by {{db\_name}}. If the policy you're configuring doesn't exist, calling this stored procedure creates it. If this policy does exist, calling this stored procedure modifies it with the parameter values that you provide.

### Syntax
<a name="db2-sp-configure-db-audit-syntax"></a>

```
db2 "call rdsadmin.configure_db_audit(
    '{{db_name}}', 
    '{{category}}', 
    '{{category_setting}}', 
    '?')"
```

### Parameters
<a name="db2-sp-configure-db-audit-parameters"></a>

The following parameters are required.

{{db\_name}}  
The DB name of the RDS for Db2 database to configure the audit policy for. The data type is `varchar`.

{{category}}  
The name of the category to configure this audit policy for. The data type is `varchar`. The following are valid values for this parameter:  
+ `ALL` – With `ALL`, Amazon RDS doesn't include the `CONTEXT`, `EXECUTE`, or `ERROR` categories.
+ `AUDIT` 
+ `CHECKING` 
+ `CONTEXT` 
+ `ERROR` 
+ `EXECUTE` – You can configure this category with data or without data. With data means to also log input data values provided for any host variables and parameter markers. The default is without data. For more information, see the description of the {{category\_setting}} parameter and the [Examples](#db2-sp-configure-db-audit-examples).
+ `OBJMAINT` 
+ `SECMAINT` 
+ `SYSADMIN` 
+ `VALIDATE` 
For more information about these categories, see the [IBM Db2 documentation](https://www.ibm.com/docs/en/db2/11.1?topic=statements-create-audit-policy).

{{category\_setting}}  
The setting for the specified audit category. The data type is `varchar`.  
The following table shows the valid category setting values for each category.  

<a name="db2-option-reference"></a>
<table>
<thead>
  <tr><th>Category</th><th>Valid category settings</th></tr>
</thead>
<tbody>
  <tr><td><code>ALL</code><br /><code>AUDIT</code><br /><code>CHECKING</code><br /><code>CONTEXT</code><br /><code>OBJMAINT</code><br /><code>SECMAINT</code><br /><code>SYSADMIN</code><br /><code>VALIDATE</code></td><td><code>BOTH|FAILURE|SUCCESS|NONE</code></td></tr>
  <tr><td><code>ERROR</code></td><td><code>AUDIT|NORMAL</code>. The default is <code>NORMAL</code>.</td></tr>
  <tr><td><code>EXECUTE</code></td><td><code>BOTH,WITH|BOTH,WITHOUT|FAILURE,WITH|FAILURE,WITHOUT|SUCCESS,WITH|SUCCESS,WITHOUT|NONE</code></td></tr>
</tbody>
</table>


### Usage notes
<a name="db2-sp-configure-db-audit-usage-notes"></a>

Before you call `rdsadmin.configure_db_audit`, make sure the RDS for Db2 DB instance with the database you're configuring the audit policy for is associated with an option group that has the `DB2_AUDIT` option. For more information, see [Setting up Db2 audit logging](Db2.Options.Audit.md#db2-audit-setting-up).

After you configure the audit policy, you can check the status of the audit configuration for the database by following the steps in [Check the audit configuration](Db2.Options.Audit.md#db2-audit-check-config-status).

Specifying `ALL` for the `category` parameter doesn't include the `CONTEXT`, `EXECUTE`, or `ERROR` categories. To add these categories to your audit policy, call `rdsadmin.configure_db_audit` separately with each category that you want to add. For more information, see [Examples](#db2-sp-configure-db-audit-examples).

### Examples
<a name="db2-sp-configure-db-audit-examples"></a>

The following examples create or modify the audit policy for a database named `TESTDB`. In examples 1 through 5, if the `ERROR` category wasn't previously configured, this category is set to `NORMAL` (the default). To change that setting to `AUDIT`, follow [Example 6: Specifying the ERROR category](#example-6).

**Example 1: Specifying the `ALL` category**

```
db2 "call rdsadmin.configure_db_audit('TESTDB', 'ALL', 'BOTH', ?)"
```

In the example, the call configures the `AUDIT`, `CHECKING`, `OBJMAINT`, `SECMAINT`, `SYSADMIN`, and `VALIDATE` categories in the audit policy. Specifying `BOTH` means that both successful and failing events will be audited for each of these categories.

**Example 2: Specifying the `EXECUTE` category with data**

```
db2 "call rdsadmin.configure_db_audit('TESTDB', 'EXECUTE', 'SUCCESS,WITH', ?)"
```

In the example, the call configures the `EXECUTE` category in the audit policy. Specifying `SUCCESS,WITH` means that logs for this category will include only successful events, and will include input data values provided for host variables and parameter markers.

**Example 3: Specifying the `EXECUTE` category without data**

```
db2 "call rdsadmin.configure_db_audit('TESTDB', 'EXECUTE', 'FAILURE,WITHOUT', ?)"
```

In the example, the call configures the `EXECUTE` category in the audit policy. Specifying `FAILURE,WITHOUT` means that logs for this category will include only failing events, and won't include input data values provided for host variables and parameter markers.

**Example 4: Specifying the `EXECUTE` category without status events**

```
db2 "call rdsadmin.configure_db_audit('TESTDB', 'EXECUTE', 'NONE', ?)"
```

In the example, the call configures the `EXECUTE` category in the audit policy. Specifying `NONE` means that no events in this category will be audited.

**Example 5: Specifying the `OBJMAINT` category**

```
db2 "call rdsadmin.configure_db_audit('TESTDB', 'OBJMAINT', 'NONE', ?)"
```

In the example, the call configures the `OBJMAINT` category in the audit policy. Specifying `NONE` means that no events in this category will be audited.

**Example 6: Specifying the `ERROR` category**

```
db2 "call rdsadmin.configure_db_audit('TESTDB', 'ERROR', 'AUDIT', ?)"
```

In the example, the call configures the `ERROR` category in the audit policy. Specifying `AUDIT` means that all errors, including errors occurring within audit logging itself, are captured in the logs. The default error type is `NORMAL`. With `NORMAL`, errors generated by the audit are ignored and only the `SQLCODE`s for errors associated with the operation being performed are captured.

## rdsadmin.disable\_db\_audit
<a name="db2-sp-disable-db-audit"></a>

Stops audit logging for the RDS for Db2 database specified by {{db\_name}} and removes the audit policy configured for it. 

**Note**  
This stored procedure only removes audit policies that were configured by calling [rdsadmin.configure\_db\_audit](#db2-sp-configure-db-audit). Object-level audit policies aren't affected. For more information, see [Db2 object-level audit policies](db2-object-level-audit.md).

### Syntax
<a name="db2-sp-disable-db-audit-syntax"></a>

```
db2 "call rdsadmin.disable_db_audit('{{db_name}}', ?)"
```

### Parameters
<a name="db2-sp-disable-db-audit-parameters"></a>

The following parameters are required.

{{db\_name}}  
The DB name of the RDS for Db2 database to disable audit logging for. The data type is `varchar`.

### Usage notes
<a name="db2-sp-disable-db-audit-usage-notes"></a>

Calling `rdsadmin.disable_db_audit` doesn't disable audit logging for the RDS for Db2 DB instance. To disable audit logging at the DB instance level, remove the option group from the DB instance. For more information, see [Disabling Db2 audit logging](Db2.Options.Audit.md#db2-audit-disabling).

### Examples
<a name="db2-sp-disable-db-audit-examples"></a>

The following example disables audit logging for a database named `TESTDB`.

```
db2 "call rdsadmin.disable_db_audit('TESTDB', ?)"
```

## rdsadmin.create\_audit\_policy
<a name="db2-sp-create-audit-policy"></a>

Creates an object-level audit policy in the RDS for Db2 database specified by {{db\_name}}. The audit policy doesn't audit anything until you attach it to an object by calling [rdsadmin.attach\_audit\_policy](#db2-sp-attach-audit-policy). For more information, see [Db2 object-level audit policies](db2-object-level-audit.md).

### Syntax
<a name="db2-sp-create-audit-policy-syntax"></a>

```
db2 "call rdsadmin.create_audit_policy(
    ?,
    '{{db_name}}',
    '{{policy_name}}',
    '{{category}}',
    '{{category_status}}',
    '{{error_type}}')"
```

### Parameters
<a name="db2-sp-create-audit-policy-parameters"></a>

The following output parameter is required:

?  
A parameter marker that outputs the ID of the task. This parameter only accepts `?`.

The following input parameters are required:

{{db\_name}}  
The name of the database to create the audit policy in. Specify one of your own databases. You can't specify the `rdsadmin` database. The data type is `varchar`.

{{policy\_name}}  
The name of the audit policy to create. The name must be a Db2 ordinary identifier of up to 128 characters, and can't be `DBA_AUDIT` or start with `RDS_DAS_`. The data type is `varchar`.

{{category}}  
The audit category to configure. The data type is `varchar`. The following are valid values for this parameter:  
+ `ALL` – All Db2 audit categories, including `CONTEXT` and `EXECUTE`. `EXECUTE` is configured without data.
+ `AUDIT`
+ `CHECKING`
+ `CONTEXT`
+ `EXECUTE` – The same as `EXECUTE WITHOUT DATA`.
+ `EXECUTE WITH DATA` – Audits the `EXECUTE` category, and also logs input data values provided for any host variables and parameter markers.
+ `EXECUTE WITHOUT DATA` – Audits the `EXECUTE` category without input data values.
+ `OBJMAINT`
+ `SECMAINT`
+ `SYSADMIN`
+ `VALIDATE`
For more information about these categories, see [Audit categories in the IBM Db2 documentation](https://www.ibm.com/docs/en/db2/12.1.x?topic=facility-audit-categories).

{{category\_status}}  
The events to audit for the category. The data type is `varchar`. The following are valid values for this parameter:  
+ `BOTH` – Audit both successful and failing events.
+ `SUCCESS` – Audit only successful events.
+ `FAILURE` – Audit only failing events.
+ `NONE` – Audit no events in this category.

{{error\_type}}  
How Db2 handles errors that occur while it writes audit records. The data type is `varchar`. The following are valid values for this parameter:  
+ `NORMAL` – Errors generated by the audit are ignored, and the statement that is being audited runs.
+ `AUDIT` – All errors, including errors that occur within audit logging itself, are returned. The statement that is being audited fails if its audit record can't be written.

### Usage notes
<a name="db2-sp-create-audit-policy-usage-notes"></a>

Before you call `rdsadmin.create_audit_policy`, make sure that the RDS for Db2 DB instance is associated with an option group that has the `DB2_AUDIT` option. For more information, see [Setting up Db2 audit logging](Db2.Options.Audit.md#db2-audit-setting-up).

To configure more categories for the audit policy, call [rdsadmin.alter\_audit\_policy](#db2-sp-alter-audit-policy) once for each category that you want to add.

For information about checking the status of creating an audit policy, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

For error messages returned when calling `rdsadmin.create_audit_policy`, see [Object-level audit policy errors](db2-troubleshooting.md#db2-troubleshooting-audit-policy-sp-errors).

### Examples
<a name="db2-sp-create-audit-policy-examples"></a>

The following examples connect to the `rdsadmin` database and create audit policies in a database named `TESTDB`. Replace {{master\_username}} and {{master\_password}} with your own information.

**Example 1: Creating an audit policy for the `EXECUTE` category with data**

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.create_audit_policy(?, 'TESTDB', 'TEST_POLICY', 'EXECUTE WITH DATA', 'BOTH', 'NORMAL')"
```

In the example, the call creates an audit policy named `TEST_POLICY` that audits the `EXECUTE` category. Specifying `EXECUTE WITH DATA` means that logs will include input data values provided for host variables and parameter markers. Specifying `BOTH` means that both successful and failing events will be audited.

**Example 2: Creating an audit policy for the `CHECKING` category**

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.create_audit_policy(?, 'TESTDB', 'TEST_CHECKING_POLICY', 'CHECKING', 'FAILURE', 'NORMAL')"
```

In the example, the call creates an audit policy named `TEST_CHECKING_POLICY` that audits the `CHECKING` category. Specifying `FAILURE` means that only failing authorization checks will be audited.

**Example 3: Creating an audit policy with the `AUDIT` error type**

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.create_audit_policy(?, 'TESTDB', 'TEST_STRICT_POLICY', 'ALL', 'BOTH', 'AUDIT')"
```

In the example, the call creates an audit policy named `TEST_STRICT_POLICY` that audits all categories for both successful and failing events. Specifying `AUDIT` for the error type means that a statement fails if its audit record can't be written.

## rdsadmin.alter\_audit\_policy
<a name="db2-sp-alter-audit-policy"></a>

Modifies an object-level audit policy in the RDS for Db2 database specified by {{db\_name}}. Each call modifies one category, the error type, or both.

### Syntax
<a name="db2-sp-alter-audit-policy-syntax"></a>

```
db2 "call rdsadmin.alter_audit_policy(
    ?,
    '{{db_name}}',
    '{{policy_name}}',
    '{{category}}',
    '{{category_status}}',
    '{{error_type}}')"
```

### Parameters
<a name="db2-sp-alter-audit-policy-parameters"></a>

The following output parameter is required:

?  
A parameter marker that outputs the ID of the task. This parameter only accepts `?`.

The following input parameters are required:

{{db\_name}}  
The name of the database that contains the audit policy. Specify one of your own databases. You can't specify the `rdsadmin` database. The data type is `varchar`.

{{policy\_name}}  
The name of the audit policy to modify. The data type is `varchar`.

The following input parameters are optional. To leave a setting unchanged, specify an empty string (`''`). You must specify {{category}} and {{category\_status}}, {{error\_type}}, or all three.

{{category}}  
The audit category to modify. Specify {{category}} and {{category\_status}} together. The data type is `varchar`. For valid values, see the {{category}} parameter of [rdsadmin.create\_audit\_policy](#db2-sp-create-audit-policy).

{{category\_status}}  
The events to audit for the category. The data type is `varchar`. Valid values: `BOTH`, `SUCCESS`, `FAILURE`, `NONE`. For descriptions of these values, see [rdsadmin.create\_audit\_policy](#db2-sp-create-audit-policy).

{{error\_type}}  
How Db2 handles errors that occur while it writes audit records. The data type is `varchar`. Valid values: `NORMAL`, `AUDIT`. For descriptions of these values, see [rdsadmin.create\_audit\_policy](#db2-sp-create-audit-policy).

### Usage notes
<a name="db2-sp-alter-audit-policy-usage-notes"></a>

Calling `rdsadmin.alter_audit_policy` changes only the category that you specify. Other categories keep their current settings. Specifying `ALL` for the {{category}} parameter sets every category to the status that you specify, and sets the `EXECUTE` category to audit without data.

Changes to an audit policy that's attached to an object take effect without detaching and reattaching the policy.

For information about checking the status of modifying an audit policy, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

For error messages returned when calling `rdsadmin.alter_audit_policy`, see [Object-level audit policy errors](db2-troubleshooting.md#db2-troubleshooting-audit-policy-sp-errors).

### Examples
<a name="db2-sp-alter-audit-policy-examples"></a>

The following examples connect to the `rdsadmin` database and modify an audit policy named `TEST_POLICY` in a database named `TESTDB`. Replace {{master\_username}} and {{master\_password}} with your own information.

**Example 1: Adding a category**

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.alter_audit_policy(?, 'TESTDB', 'TEST_POLICY', 'VALIDATE', 'BOTH', '')"
```

In the example, the call adds the `VALIDATE` category to the audit policy for both successful and failing events. The other categories and the error type don't change.

**Example 2: Turning off a category**

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.alter_audit_policy(?, 'TESTDB', 'TEST_POLICY', 'EXECUTE', 'NONE', '')"
```

In the example, the call stops auditing the `EXECUTE` category. Specifying `NONE` means that no events in this category will be audited.

**Example 3: Changing the error type**

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.alter_audit_policy(?, 'TESTDB', 'TEST_POLICY', '', '', 'AUDIT')"
```

In the example, the call changes the error type of the audit policy to `AUDIT`. The categories don't change.

## rdsadmin.attach\_audit\_policy
<a name="db2-sp-attach-audit-policy"></a>

Attaches an object-level audit policy to an object in the RDS for Db2 database specified by {{db\_name}}. After the policy is attached, Db2 audits activity on the object according to the policy.

### Syntax
<a name="db2-sp-attach-audit-policy-syntax"></a>

```
db2 "call rdsadmin.attach_audit_policy(
    ?,
    '{{db_name}}',
    '{{object_type}}',
    '{{object_name}}',
    '{{policy_name}}')"
```

### Parameters
<a name="db2-sp-attach-audit-policy-parameters"></a>

The following output parameter is required:

?  
A parameter marker that outputs the ID of the task. This parameter only accepts `?`.

The following input parameters are required:

{{db\_name}}  
The name of the database that contains the audit policy and the object. Specify one of your own databases. You can't specify the `rdsadmin` database. The data type is `varchar`.

{{object\_type}}  
The type of object to attach the audit policy to. The data type is `varchar`. The following are valid values for this parameter:  
+ `TABLE` – A table, specified as `SCHEMA.TABLE`.
+ `USER` – A user.
+ `GROUP` – A group.
+ `ROLE` – A role.
+ `TRUSTED CONTEXT` – A trusted context.
+ `ACCESSCTRL`, `CREATE_SECURE_OBJECT`, `DATAACCESS`, `SECADM`, `SQLADM`, `SYSCTRL`, `SYSMAINT`, `SYSMON`, `WLMADM` – An authority. The audit policy applies to the users who hold the authority.

{{object\_name}}  
The name of the object. For the `TABLE` object type, include the schema, for example `TESTSCHEMA.TESTTABLE`. For the authority object types, specify an empty string (`''`). The data type is `varchar`.

{{policy\_name}}  
The name of the audit policy to attach. The data type is `varchar`.

### Usage notes
<a name="db2-sp-attach-audit-policy-usage-notes"></a>

Each object can have only one audit policy attached. To replace the audit policy attached to an object, first call [rdsadmin.detach\_audit\_policy](#db2-sp-detach-audit-policy).

The object must exist before you attach an audit policy to it.

You can't attach an audit policy to the `DATABASE`, `SYSADM`, or `DBADM` objects. To audit at the database level, use [rdsadmin.configure\_db\_audit](#db2-sp-configure-db-audit). You also can't attach an audit policy to the users `RDSDB`, `RDSADMIN`, or `SECADMUSER`.

For information about checking the status of attaching an audit policy, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

For error messages returned when calling `rdsadmin.attach_audit_policy`, see [Object-level audit policy errors](db2-troubleshooting.md#db2-troubleshooting-audit-policy-sp-errors).

### Examples
<a name="db2-sp-attach-audit-policy-examples"></a>

The following examples connect to the `rdsadmin` database and attach an audit policy named `TEST_POLICY` to objects in a database named `TESTDB`. Replace {{master\_username}} and {{master\_password}} with your own information.

**Example 1: Attaching an audit policy to a table**

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.attach_audit_policy(?, 'TESTDB', 'TABLE', 'TESTSCHEMA.TESTTABLE', 'TEST_POLICY')"
```

In the example, the call attaches the audit policy to the `TESTTABLE` table in the `TESTSCHEMA` schema.

**Example 2: Attaching an audit policy to a user**

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.attach_audit_policy(?, 'TESTDB', 'USER', 'TESTUSER', 'TEST_POLICY')"
```

In the example, the call attaches the audit policy to the user `TESTUSER`. Db2 audits the activity of `TESTUSER` in the database.

**Example 3: Attaching an audit policy to a role**

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.attach_audit_policy(?, 'TESTDB', 'ROLE', 'TESTROLE', 'TEST_POLICY')"
```

In the example, the call attaches the audit policy to the role `TESTROLE`. Db2 audits the activity of users who hold the role.

**Example 4: Attaching an audit policy to an authority**

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.attach_audit_policy(?, 'TESTDB', 'DATAACCESS', '', 'TEST_POLICY')"
```

In the example, the call attaches the audit policy to the `DATAACCESS` authority. Db2 audits the activity of users who hold `DATAACCESS`. For authorities, specify an empty string for {{object\_name}}.

## rdsadmin.detach\_audit\_policy
<a name="db2-sp-detach-audit-policy"></a>

Detaches the object-level audit policy from an object in the RDS for Db2 database specified by {{db\_name}}. The audit policy itself isn't dropped.

### Syntax
<a name="db2-sp-detach-audit-policy-syntax"></a>

```
db2 "call rdsadmin.detach_audit_policy(
    ?,
    '{{db_name}}',
    '{{object_type}}',
    '{{object_name}}')"
```

### Parameters
<a name="db2-sp-detach-audit-policy-parameters"></a>

The following output parameter is required:

?  
A parameter marker that outputs the ID of the task. This parameter only accepts `?`.

The following input parameters are required:

{{db\_name}}  
The name of the database that contains the object. Specify one of your own databases. You can't specify the `rdsadmin` database. The data type is `varchar`.

{{object\_type}}  
The type of object to detach the audit policy from. The data type is `varchar`. For valid values, see the {{object\_type}} parameter of [rdsadmin.attach\_audit\_policy](#db2-sp-attach-audit-policy).

{{object\_name}}  
The name of the object. For the `TABLE` object type, include the schema, for example `TESTSCHEMA.TESTTABLE`. For the authority object types, specify an empty string (`''`). The data type is `varchar`.

### Usage notes
<a name="db2-sp-detach-audit-policy-usage-notes"></a>

You don't specify the audit policy, because each object can have only one audit policy attached.

You can't detach audit policies from the `DATABASE`, `SYSADM`, or `DBADM` objects. To stop database-level audit logging, use [rdsadmin.disable\_db\_audit](#db2-sp-disable-db-audit).

For information about checking the status of detaching an audit policy, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

For error messages returned when calling `rdsadmin.detach_audit_policy`, see [Object-level audit policy errors](db2-troubleshooting.md#db2-troubleshooting-audit-policy-sp-errors).

### Examples
<a name="db2-sp-detach-audit-policy-examples"></a>

The following example connects to the `rdsadmin` database and detaches the audit policy from the `TESTTABLE` table in the `TESTSCHEMA` schema of a database named `TESTDB`. Replace {{master\_username}} and {{master\_password}} with your own information.

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.detach_audit_policy(?, 'TESTDB', 'TABLE', 'TESTSCHEMA.TESTTABLE')"
```

The following example connects to the `rdsadmin` database and detaches the audit policy from the `DATAACCESS` authority in a database named `TESTDB`.

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.detach_audit_policy(?, 'TESTDB', 'DATAACCESS', '')"
```

## rdsadmin.drop\_audit\_policy
<a name="db2-sp-drop-audit-policy"></a>

Drops an object-level audit policy from the RDS for Db2 database specified by {{db\_name}}.

### Syntax
<a name="db2-sp-drop-audit-policy-syntax"></a>

```
db2 "call rdsadmin.drop_audit_policy(
    ?,
    '{{db_name}}',
    '{{policy_name}}')"
```

### Parameters
<a name="db2-sp-drop-audit-policy-parameters"></a>

The following output parameter is required:

?  
A parameter marker that outputs the ID of the task. This parameter only accepts `?`.

The following input parameters are required:

{{db\_name}}  
The name of the database that contains the audit policy. Specify one of your own databases. You can't specify the `rdsadmin` database. The data type is `varchar`.

{{policy\_name}}  
The name of the audit policy to drop. The data type is `varchar`.

### Usage notes
<a name="db2-sp-drop-audit-policy-usage-notes"></a>

You can't drop an audit policy that's attached to an object. First, detach the audit policy from all objects by calling [rdsadmin.detach\_audit\_policy](#db2-sp-detach-audit-policy). To find the objects that an audit policy is attached to, see [Viewing object-level audit policies and attachments](db2-object-level-audit.md#db2-object-level-audit-viewing).

For information about checking the status of dropping an audit policy, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

For error messages returned when calling `rdsadmin.drop_audit_policy`, see [Object-level audit policy errors](db2-troubleshooting.md#db2-troubleshooting-audit-policy-sp-errors).

### Examples
<a name="db2-sp-drop-audit-policy-examples"></a>

The following example connects to the `rdsadmin` database and drops an audit policy named `TEST_POLICY` from a database named `TESTDB`. Replace {{master\_username}} and {{master\_password}} with your own information.

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.drop_audit_policy(?, 'TESTDB', 'TEST_POLICY')"
```