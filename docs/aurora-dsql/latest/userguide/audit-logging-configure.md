

# Configuring audit settings

Connect to your cluster as `admin` or as a member of `pg_dsql_audit_admin`. Then use SQL to choose what to audit for each database role.

Before you can change audit settings, set up audit log delivery for the cluster. For instructions on setting up audit log delivery, see [Setting up audit log delivery](audit-logging-setup.md#audit-logging-set-up-delivery).

## Audit settings
<a name="audit-logging-settings"></a>

The following table describes the audit settings that you can change.


| Setting | Default | Description | 
| --- |--- |--- |
| dsql\_audit.log | none | The classes of statements to audit. Specify a comma-separated list of classes, or all or none. To exclude a class, put a minus sign (-) in front of it, as in all,-misc. For the list of classes, see [Statement classes](#audit-logging-classes). | 
| dsql\_audit.log\_parameter | off | When on, records the values of the bound parameters of each statement in the parameters field. | 
| dsql\_audit.log\_parameter\_max\_size | 0 | The maximum size, in bytes, of a text, bytea, or other variable-length parameter value to record. Longer values appear as <long param suppressed>. The default, 0, records values of any size. To reduce your log delivery and storage charges, AWS recommends 4096 (4 KB). Applies only when dsql\_audit.log\_parameter is on. | 
| dsql\_audit.log\_rows | off | When on, records the number of rows that each statement read or changed in the rows\_affected field. | 
| dsql\_audit.log\_statement | on | When on, records the statement text in the statement\_text field. When off, the statement\_text and parameters fields contain <not logged>. | 

## Statement classes
<a name="audit-logging-classes"></a>

The following table describes the classes that you can use in the `dsql_audit.log` setting. Class names aren't case sensitive.


| Class | Statements | 
| --- |--- |
| read | SELECT, and COPY when the source is a table or a query. | 
| write | INSERT, UPDATE, DELETE, and COPY when the destination is a table. | 
| function | Function calls. | 
| role | Statements that manage roles and privileges, such as GRANT, REVOKE, CREATE ROLE, ALTER ROLE, DROP ROLE, AWS IAM GRANT, and AWS IAM REVOKE. | 
| ddl | All data definition language (DDL) statements that aren't in the role class. | 
| misc | Statements that aren't in another class, such as SET. This class includes misc\_set. | 
| misc\_set | SET statements. | 

**Note**  
Keep the following in mind when you choose what to audit:  
You choose what to audit by statement class and by database role.
Aurora DSQL always audits changes to audit settings, including the statement text and the parameter values of the change.
Statements that fail before they run, such as statements with syntax errors, have no audit records.
Aurora DSQL doesn't audit statements that access only the system catalog tables in the `pg_catalog` schema.

## Setting a cluster-wide baseline
<a name="audit-logging-cluster-wide"></a>

To set an audit setting for all database roles, use `ALTER SYSTEM`. The setting applies to every role that doesn't have its own value for the setting. This includes roles that you create later. Run `ALTER SYSTEM` outside an explicit transaction block.

The following SQL example audits DDL statements, role and privilege changes, and writes for all roles:

```sql
ALTER SYSTEM SET dsql_audit.log = 'ddl,role,write';
```

To remove a cluster-wide setting, reset it, as in the following SQL example:

```sql
ALTER SYSTEM RESET dsql_audit.log;
```

## Setting audit settings for a role
<a name="audit-logging-per-role"></a>

To set an audit setting for a specific database role, use the `sys.set_audit_config` function. Specify the role, the setting, and the value.

The following SQL example audits DDL statements, role and privilege changes, and writes of the {{app\_user}} role. It also records the bound parameter values and the row counts of the role's statements:

```sql
SELECT sys.set_audit_config('{{app_user}}', 'dsql_audit.log', 'ddl,role,write');
SELECT sys.set_audit_config('{{app_user}}', 'dsql_audit.log_parameter', 'on');
SELECT sys.set_audit_config('{{app_user}}', 'dsql_audit.log_rows', 'on');
```

To return a setting of a role to its default value, use the `sys.reset_audit_config` function. The following SQL example resets the `dsql_audit.log` setting of the {{app\_user}} role:

```sql
SELECT sys.reset_audit_config('{{app_user}}', 'dsql_audit.log');
```

## Excluding a role from audit logging
<a name="audit-logging-exclude-role"></a>

A cluster-wide baseline applies to every database role, including roles that run frequent, routine statements, such as monitoring or health-check roles. To reduce the volume of audit records, exclude these roles from auditing. To exclude a role, set its `dsql_audit.log` setting to `none`. The following SQL example excludes the {{monitor\_user}} role:

```sql
SELECT sys.set_audit_config('{{monitor_user}}', 'dsql_audit.log', 'none');
```

To exclude only some classes of statements, set the classes to audit for the role. The role's value replaces the baseline, so include every class that you want to audit. The following SQL example audits all statements of the {{reporting\_user}} role except reads:

```sql
SELECT sys.set_audit_config('{{reporting_user}}', 'dsql_audit.log', 'all,-read');
```

To audit the role with the cluster-wide baseline again, reset its setting, as in the following SQL example:

```sql
SELECT sys.reset_audit_config('{{monitor_user}}', 'dsql_audit.log');
```

Only `admin` and members of `pg_dsql_audit_admin` can change audit settings, so other roles can't exclude themselves. Aurora DSQL records every change to audit settings, so your audit trail shows who excluded a role and when. To check which roles you excluded, see [Viewing audit settings](#audit-logging-view-settings).

## How Aurora DSQL applies audit settings
<a name="audit-logging-apply"></a>

The following details describe how Aurora DSQL applies audit settings to the statements of each connection.
+ **Settings of the connecting role.** Aurora DSQL applies the audit settings of the database role that you connect as. If you change the current role in a transaction, for example with `SET LOCAL ROLE`, the settings of the role that you connected as still apply.
+ **Changes apply to new connections.** Changes to audit settings apply to new connections, and can take a few minutes to apply. To make sure that a connection uses the latest settings, reconnect.

## Viewing audit settings
<a name="audit-logging-view-settings"></a>

**Settings of your connection**  
To see the audit settings that apply to your current connection, run `SHOW`:

```sql
SHOW dsql_audit.log;
```

**Settings of specific roles**  
To see the audit settings that you set for specific roles, query the `pg_db_role_setting` catalog:

```sql
SELECT r.rolname, s.setconfig
FROM pg_db_role_setting s
JOIN pg_roles r ON r.oid = s.setrole;
```