

# Db2 object-level audit policies

With object-level audit policies, you can create your own Db2 audit policies and attach them to specific objects in a database that you created on an RDS for Db2 DB instance, such as tables, users, groups, roles, trusted contexts, and authorities. Amazon RDS records the activity that each policy covers and uploads the audit records to the Amazon S3 bucket that you configured for [Db2 audit logging](Db2.Options.Audit.md).

Object-level audit policies complement database-level audit logging. Use [rdsadmin.configure\_db\_audit](db2-sp-managing-audit-policies.md#db2-sp-configure-db-audit) to audit activity across a whole database. Use object-level audit policies to audit only the objects that you need, for example a single table that contains sensitive data, or a single user.

**Topics**
+ [Using object-level audit policies with database-level audit logging](#db2-object-level-audit-with-db-audit)
+ [Setting up object-level audit policies](#db2-object-level-audit-setting-up)
+ [Managing object-level audit policies](#db2-object-level-audit-managing)
+ [Viewing object-level audit policies and attachments](#db2-object-level-audit-viewing)
+ [Viewing audit logs for object-level audit policies](#db2-object-level-audit-viewing-logs)
+ [Behavior during DB instance and database operations](#db2-object-level-audit-operations)
+ [Limitations for object-level audit policies](#db2-object-level-audit-limitations)
+ [Troubleshooting object-level audit policies](#db2-object-level-audit-troubleshooting)

## Using object-level audit policies with database-level audit logging
<a name="db2-object-level-audit-with-db-audit"></a>

You can use object-level audit policies and database-level audit logging at the same time, in the same database. The two features work together as follows:
+ **Amazon RDS manages database-level audit logging** – `rdsadmin.configure_db_audit` manages an audit policy named `DBA_AUDIT`, which Amazon RDS attaches to the `DATABASE`, `SYSADM`, and `DBADM` objects. You can't attach object-level audit policies to those objects, and you can't modify `DBA_AUDIT` with the object-level audit policy stored procedures.
+ **All applicable policies are used** – When an event is covered by `DBA_AUDIT` and by an object-level audit policy, Db2 audits the event according to each applicable policy.
+ **The two features are independent** – Calling `rdsadmin.configure_db_audit` doesn't change your object-level audit policies. Calling [rdsadmin.disable\_db\_audit](db2-sp-managing-audit-policies.md#db2-sp-disable-db-audit) removes only the `DBA_AUDIT` policy. Your object-level audit policies remain attached and continue to record activity.
+ **Removing the option affects both** – Removing the `DB2_AUDIT` option from your DB instance stops both kinds of auditing. For more information, see [Behavior during DB instance and database operations](#db2-object-level-audit-operations).
+ **Logs share the same location** – Audit records from both features are uploaded to the database-level location in your Amazon S3 bucket. Db2 writes audit records by category, so records for the same category are in the same files whichever policy produced them.

## Setting up object-level audit policies
<a name="db2-object-level-audit-setting-up"></a>

To set up an object-level audit policy, complete the following steps.

**Topics**
+ [Step 1: Enable Db2 audit logging on the DB instance](#db2-object-level-audit-enable-option)
+ [Step 2: Create an audit policy](#db2-object-level-audit-create-policy)
+ [Step 3: Attach the audit policy to an object](#db2-object-level-audit-attach-policy)
+ [Step 4: Check the status of the tasks](#db2-object-level-audit-check-tasks)
+ [Step 5: Check the attachment](#db2-object-level-audit-check-attachment)

### Step 1: Enable Db2 audit logging on the DB instance
<a name="db2-object-level-audit-enable-option"></a>

Your RDS for Db2 DB instance must be associated with an option group that has the `DB2_AUDIT` option. If you haven't done so already, complete steps 1 through 4 in [Setting up Db2 audit logging](Db2.Options.Audit.md#db2-audit-setting-up).

You don't need to call `rdsadmin.configure_db_audit` to use object-level audit policies.

### Step 2: Create an audit policy
<a name="db2-object-level-audit-create-policy"></a>

Connect to the `rdsadmin` database using the master username and master password for your RDS for Db2 DB instance. Then, call the [rdsadmin.create\_audit\_policy](db2-sp-managing-audit-policies.md#db2-sp-create-audit-policy) stored procedure.

The following example connects to the `rdsadmin` database and creates an audit policy named `TEST_POLICY` in a database named `TESTDB`. The policy audits the `EXECUTE` category with input data, for both successful and failing events, with an error type of `NORMAL`. Replace {{master\_username}} and {{master\_password}} with your own information.

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.create_audit_policy(?, 'TESTDB', 'TEST_POLICY', 'EXECUTE WITH DATA', 'BOTH', 'NORMAL')"
```

The stored procedure returns the ID of the task that creates the policy.

```
  Value of output parameters
  --------------------------
  Parameter Name  : OUT_TASK_ID
  Parameter Value : 101

  Return Status = 0
```

An audit policy doesn't audit anything until you attach it to an object.

### Step 3: Attach the audit policy to an object
<a name="db2-object-level-audit-attach-policy"></a>

Call the [rdsadmin.attach\_audit\_policy](db2-sp-managing-audit-policies.md#db2-sp-attach-audit-policy) stored procedure.

The following example connects to the `rdsadmin` database and attaches the `TEST_POLICY` audit policy to the `TESTTABLE` table in the `TESTSCHEMA` schema of the `TESTDB` database.

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "call rdsadmin.attach_audit_policy(?, 'TESTDB', 'TABLE', 'TESTSCHEMA.TESTTABLE', 'TEST_POLICY')"
```

### Step 4: Check the status of the tasks
<a name="db2-object-level-audit-check-tasks"></a>

The object-level audit policy stored procedures run asynchronously. To check that the policy was created and attached, call [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status). The following example connects to the `rdsadmin` database and lists the object-level audit policy tasks for the `TESTDB` database.

```
db2 "connect to rdsadmin user {{master_username}} using {{master_password}}"
db2 "select task_id, task_type, database_name, lifecycle,
    varchar(bson_to_json(task_input_params), 500) as task_params,
    cast(task_output as varchar(500)) as task_output
    from table(rdsadmin.get_task_status(null, 'TESTDB', null))
    where task_type like '%AUDIT_POLICY'"
```

The query produces output similar to the following example:

```
TASK_ID  TASK_TYPE            DATABASE_NAME  LIFECYCLE
-------  -------------------  -------------  ---------
    101  CREATE_AUDIT_POLICY  TESTDB         SUCCESS
    102  ATTACH_AUDIT_POLICY  TESTDB         SUCCESS

... continued ...
TASK_PARAMS
--------------------------------------------------------------------------------------------
{ "STMT" : "CREATE AUDIT POLICY TEST_POLICY CATEGORIES EXECUTE WITH DATA STATUS BOTH ERROR TYPE NORMAL" }
{ "STMT" : "AUDIT TABLE TESTSCHEMA.TESTTABLE USING POLICY TEST_POLICY" }

... continued ...
TASK_OUTPUT
---------------------------------------------------
2026-11-02T20:27:03.029Z Task execution has started.
2026-11-02T20:27:04.285Z Task execution has completed successfully.
```

If a task fails, `LIFECYCLE` is `ERROR`, and `TASK_OUTPUT` contains the Db2 SQLSTATE, SQLCODE, and error details. For more information, see [Troubleshooting object-level audit policies](#db2-object-level-audit-troubleshooting).

### Step 5: Check the attachment
<a name="db2-object-level-audit-check-attachment"></a>

Connect to the database and query the `SYSCAT.AUDITUSE` catalog view. The following example connects to the `TESTDB` database and shows the objects that object-level audit policies are attached to. Replace {{master\_username}} and {{master\_password}} with your own information.

```
db2 "connect to TESTDB user {{master_username}} using {{master_password}}"
db2 "select auditpolicyname, objecttype, objectschema, objectname
    from syscat.audituse
    where auditpolicyname <> 'DBA_AUDIT'"
```

The query produces output similar to the following example:

```
AUDITPOLICYNAME  OBJECTTYPE  OBJECTSCHEMA  OBJECTNAME
---------------  ----------  ------------  ----------
TEST_POLICY      T           TESTSCHEMA    TESTTABLE
```

After the attachment is listed, Db2 audits activity on the object according to the audit policy, and Amazon RDS uploads the audit records to your Amazon S3 bucket. For more information, see [Viewing audit logs for object-level audit policies](#db2-object-level-audit-viewing-logs).

## Managing object-level audit policies
<a name="db2-object-level-audit-managing"></a>

After you set up an object-level audit policy, you can modify it, move it to a different object, or remove it.

**Topics**
+ [Modifying an object-level audit policy](#db2-object-level-audit-modifying)
+ [Moving an object-level audit policy to a different object](#db2-object-level-audit-moving)
+ [Removing an object-level audit policy](#db2-object-level-audit-removing)

### Modifying an object-level audit policy
<a name="db2-object-level-audit-modifying"></a>

To change the categories or the error type of an audit policy, call [rdsadmin.alter\_audit\_policy](db2-sp-managing-audit-policies.md#db2-sp-alter-audit-policy). Each call changes one category, the error type, or both. Categories that you don't specify keep their current settings. To audit several categories with one policy, call `rdsadmin.alter_audit_policy` once for each additional category.

### Moving an object-level audit policy to a different object
<a name="db2-object-level-audit-moving"></a>

Each object can have only one audit policy attached. To replace the audit policy that's attached to an object, call [rdsadmin.detach\_audit\_policy](db2-sp-managing-audit-policies.md#db2-sp-detach-audit-policy). Wait for the detach task to complete, as described in [Step 4: Check the status of the tasks](#db2-object-level-audit-check-tasks). Then, call [rdsadmin.attach\_audit\_policy](db2-sp-managing-audit-policies.md#db2-sp-attach-audit-policy) with the new policy.

### Removing an object-level audit policy
<a name="db2-object-level-audit-removing"></a>

To remove an audit policy, detach it from every object that it's attached to by calling [rdsadmin.detach\_audit\_policy](db2-sp-managing-audit-policies.md#db2-sp-detach-audit-policy). Then, call [rdsadmin.drop\_audit\_policy](db2-sp-managing-audit-policies.md#db2-sp-drop-audit-policy). You can't drop an audit policy that's still attached to an object.

## Viewing object-level audit policies and attachments
<a name="db2-object-level-audit-viewing"></a>

To view your object-level audit policies, connect to the database that contains them and query the Db2 catalog views `SYSCAT.AUDITPOLICIES` and `SYSCAT.AUDITUSE`.

The following example connects to the `TESTDB` database and lists the object-level audit policies and their settings.

```
db2 "connect to TESTDB user {{master_username}} using {{master_password}}"
db2 "select auditpolicyname, auditstatus, checkingstatus, contextstatus,
    executestatus, executewithdata, objmaintstatus, secmaintstatus,
    sysadminstatus, validatestatus, errortype
    from syscat.auditpolicies
    where auditpolicyname <> 'DBA_AUDIT'"
```

The query produces output similar to the following example:

```
AUDITPOLICYNAME  AUDITSTATUS  CHECKINGSTATUS  CONTEXTSTATUS  EXECUTESTATUS  EXECUTEWITHDATA
---------------  -----------  --------------  -------------  -------------  ---------------
TEST_POLICY      N            N               N              B              Y

... continued ...
OBJMAINTSTATUS  SECMAINTSTATUS  SYSADMINSTATUS  VALIDATESTATUS  ERRORTYPE
--------------  --------------  --------------  --------------  ---------
N               N               N               N               N
```

The following example connects to the `TESTDB` database and lists the objects that object-level audit policies are attached to.

```
db2 "connect to TESTDB user {{master_username}} using {{master_password}}"
db2 "select auditpolicyname, objecttype, subobjecttype, objectschema, objectname
    from syscat.audituse
    where auditpolicyname <> 'DBA_AUDIT'"
```

The query produces output similar to the following example:

```
AUDITPOLICYNAME  OBJECTTYPE  SUBOBJECTTYPE  OBJECTSCHEMA  OBJECTNAME
---------------  ----------  -------------  ------------  ----------
TEST_POLICY      T                          TESTSCHEMA    TESTTABLE
TEST_POLICY      i           U              -             TESTUSER
TEST_POLICY      g                          -             DATAACCESS
```

For information about the values in these catalog views, see [SYSCAT.AUDITPOLICIES in the IBM Db2 documentation](https://www.ibm.com/docs/en/db2/12.1.x?topic=views-syscatauditpolicies) and [SYSCAT.AUDITUSE in the IBM Db2 documentation](https://www.ibm.com/docs/en/db2/12.1.x?topic=views-syscataudituse).

## Viewing audit logs for object-level audit policies
<a name="db2-object-level-audit-viewing-logs"></a>

Amazon RDS uploads audit records for object-level audit policies to the database-level location in your Amazon S3 bucket:
+ Database level logs – `{{bucket_name}}/db2-audit-logs/{{dbi_resource_id}}/{{date_time_utc}}/{{db_name}}/`

After you attach an audit policy, wait for at least one hour before viewing the audit data in your Amazon S3 bucket. For more information, see [Viewing audit logs](Db2.Options.Audit.md#db2-audit-viewing-logs).

## Behavior during DB instance and database operations
<a name="db2-object-level-audit-operations"></a>

The following table describes what happens to object-level audit policies during DB instance and database operations.


| Operation | Behavior | 
| --- | --- | 
| Rebooting, failing over, or modifying the DB instance class or storage | Audit policies and their attachments are kept, and auditing continues. | 
| Removing the `DB2_AUDIT` option from the DB instance | Amazon RDS detaches all object-level audit policies in every database. The audit policies themselves are kept. After you add the `DB2_AUDIT` option back, reattach the audit policies that you want to use. | 
| Restoring a database with [rdsadmin.restore\_database](db2-sp-managing-databases.md#db2-sp-restore-database) | Amazon RDS removes object-level audit policies from the restored database. Create and attach the audit policies again after the restore. | 
| Dropping a table | Db2 removes the attachment for that table. If you create the table again, attach the audit policy again. | 
| Removing a user with [rdsadmin.remove\_user](db2-sp-granting-revoking-privileges.md#db2-sp-remove-user) | Audit policies attached to the user stay attached. If you add a user with the same name later, that user is audited. To stop auditing, detach the audit policy. | 
| Calling [rdsadmin.disable\_db\_audit](db2-sp-managing-audit-policies.md#db2-sp-disable-db-audit) | No effect on object-level audit policies. | 

## Limitations for object-level audit policies
<a name="db2-object-level-audit-limitations"></a>

The following limitations apply to object-level audit policies:
+ Your DB instance must be associated with an option group that has the `DB2_AUDIT` option for all object-level audit policy operations, including detaching and dropping audit policies.
+ `rdsadmin.create_audit_policy` and `rdsadmin.alter_audit_policy` accept one category for each call.
+ The `ALL` category includes every Db2 audit category, including `EXECUTE` and `CONTEXT`. This is different from `rdsadmin.configure_db_audit`, where `ALL` doesn't include the `CONTEXT`, `EXECUTE`, or `ERROR` categories.
+ The status for a category is one of `BOTH`, `SUCCESS`, `FAILURE`, or `NONE`. To audit input data, use the `EXECUTE WITH DATA` category. The {{category\_setting}} values that `rdsadmin.configure_db_audit` uses, such as `BOTH,WITH`, aren't supported.
+ Each object can have only one audit policy attached.
+ You can't attach audit policies to the `DATABASE`, `SYSADM`, or `DBADM` objects. To audit at the database level, use `rdsadmin.configure_db_audit`.
+ You can't create, modify, attach, or drop audit policies named `DBA_AUDIT` or audit policies with names that start with `RDS_DAS_`.
+ You can't attach audit policies to the users `RDSDB`, `RDSADMIN`, or `SECADMUSER`, which are used by Amazon RDS.
+ Table names must include the schema, in the format `SCHEMA.TABLE`.
+ Audit policy names and object names must be Db2 ordinary identifiers. They must start with a letter, `@`, `#`, or `$`, can contain only letters, digits, `_`, `@`, `#`, and `$`, and can be up to 128 characters. Names are converted to uppercase. Objects with names that require double quotes can't be used with these stored procedures.
+ You can't use object-level audit policies in the `rdsadmin` database.
+ Auditing adds work for the database and generates audit records. Some categories, such as `EXECUTE WITH DATA`, can generate a large volume of records for frequently used objects. Attach audit policies only to the objects that you need to audit, and test the effect on your workload before you use them in production.

## Troubleshooting object-level audit policies
<a name="db2-object-level-audit-troubleshooting"></a>

Use the following information to troubleshoot common issues with object-level audit policies.

### Calling a stored procedure returns an error
<a name="db2-object-level-audit-troubleshooting-call-error"></a>

The stored procedures validate their parameters before they create a task. If a parameter isn't valid, the call returns an error and doesn't create a task. For a list of errors, see [Object-level audit policy errors](db2-troubleshooting.md#db2-troubleshooting-audit-policy-sp-errors).

### A task has the ERROR lifecycle
<a name="db2-object-level-audit-troubleshooting-task-error"></a>

If a task fails, check `TASK_OUTPUT` in the output of `rdsadmin.get_task_status`. The following table lists common causes.


| `TASK_OUTPUT` contains | Cause | Solution | 
| --- | --- | --- | 
| `Instance-level audit is not active` | Db2 audit logging isn't enabled on the DB instance, because the DB instance isn't associated with an option group that has the `DB2_AUDIT` option. | Add the `DB2_AUDIT` option. For more information, see [Step 1: Enable Db2 audit logging on the DB instance](#db2-object-level-audit-enable-option). | 
| `SQLSTATE 42704` | The object or the audit policy doesn't exist. | Check the object and policy names. Table names must include the schema. | 
| `SQLSTATE 42710` | An audit policy with this name already exists. | Use a different name, or modify the existing policy. | 
| `SQLSTATE 5U041` | The object already has an audit policy attached. | Detach the audit policy from the object, and then attach the new one. | 
| `SQLSTATE 42893` | The audit policy is still attached to an object. | Detach the audit policy from all objects, and then drop it. | 
| `SQLSTATE 40001` | The statement timed out waiting for a lock, or was chosen as a deadlock victim. | Call the stored procedure again. | 
| `The audit policy operation could not be completed because of an internal error` | An internal error occurred. | Call the stored procedure again later. If the error continues, contact AWS Support. | 

### No audit records in the Amazon S3 bucket
<a name="db2-object-level-audit-troubleshooting-no-records"></a>

If audit records for an object-level audit policy are missing from your Amazon S3 bucket, check the following:
+ The audit policy is attached to the object. For more information, see [Viewing object-level audit policies and attachments](#db2-object-level-audit-viewing).
+ The categories and statuses of the audit policy include the activity that you expect. For example, an audit policy that sets the `CHECKING` category to `FAILURE` audits only failed authorization checks.
+ At least one hour has passed since the activity occurred.

For other causes, such as IAM permissions or Amazon S3 bucket settings, see [No data in the Amazon S3 bucket](Db2.Options.Audit.md#db2-audit-troubleshooting-missing-data).