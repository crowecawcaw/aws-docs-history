

# Running minor version upgrade prechecks in Amazon RDS for Oracle
<a name="USER_UpgradeDBInstance.Oracle.Precheck"></a>

Before Amazon RDS for Oracle performs a DB minor version upgrade, it checks that your DB instance is in a state that allows the upgrade to finish. If a check finds a problem, the upgrade can't proceed until you fix it.

You can run these checks yourself at any time without starting an upgrade. This way, you can find and fix problems before your maintenance window. To run the checks, use the Amazon RDS procedure `rdsadmin.rdsadmin_precheck_tasks.precheck_minor_upgrade`. The precheck is read-only. It doesn't change your data or your configuration.

The procedure returns a task ID. The precheck writes its results to a log file named `dbtask-{{task_id}}.log` in the BDUMP directory. To download the log file, see [Downloading a database log file](USER_LogAccess.Procedural.Downloading.md).

**Note**  
Run the precheck on your primary DB instance. Running prechecks on a read replica isn't supported.

**Topics**
+ [Running a minor version upgrade precheck](#USER_UpgradeDBInstance.Oracle.Precheck.Running)
+ [Viewing the precheck results](#USER_UpgradeDBInstance.Oracle.Precheck.Viewing)
+ [Interpreting the precheck results](#USER_UpgradeDBInstance.Oracle.Precheck.Interpreting)
+ [What the precheck checks](#USER_UpgradeDBInstance.Oracle.Precheck.Checks)
+ [When to run the precheck](#USER_UpgradeDBInstance.Oracle.Precheck.When)

## Running a minor version upgrade precheck
<a name="USER_UpgradeDBInstance.Oracle.Precheck.Running"></a>

To check whether your DB instance is ready for a DB minor version upgrade, run the procedure `rdsadmin.rdsadmin_precheck_tasks.precheck_minor_upgrade`. The procedure takes no parameters. The following query starts the precheck and returns the task ID.

```
SQL> SELECT rdsadmin.rdsadmin_precheck_tasks.precheck_minor_upgrade() AS task_id FROM DUAL;

TASK_ID
------------------
1784924903020-9
```

You can also store the task ID in a SQL client variable and use the variable in other statements.

```
SQL> VAR task_id VARCHAR2(80);
SQL> EXEC :task_id := rdsadmin.rdsadmin_precheck_tasks.precheck_minor_upgrade();

PL/SQL procedure successfully completed.
```

The precheck runs in the background. It's finished when the last line of the log is `The task finished successfully.` or `The task failed.`

## Viewing the precheck results
<a name="USER_UpgradeDBInstance.Oracle.Precheck.Viewing"></a>

To read the log file, run the Amazon RDS procedure `rdsadmin.rds_file_util.read_text_file`. Include the task ID in the file name. The following example shows a precheck in which no check found a problem.

```
SQL> SELECT * FROM TABLE(rdsadmin.rds_file_util.read_text_file('BDUMP', 'dbtask-'||:task_id||'.log'));

TEXT
-------------------------------------------------------------------------------------------------------------------------
2026-08-28 18:30:20.461 UTC [INFO ] Starting minor version upgrade precheck...
2026-08-28 18:30:20.461 UTC [INFO ] NOTE: This precheck validates against the current engine version's known checks. Target-version-specific checks (e.g., autoupgrade) are not included.
2026-08-28 18:30:20.470 UTC [INFO ] CHECK: FreeStorageSpace - PASSED
2026-08-28 18:30:20.515 UTC [INFO ] CHECK: SystemTablespace - PASSED
2026-08-28 18:30:20.523 UTC [INFO ] CHECK: AuditTablespace - PASSED
2026-08-28 18:30:20.541 UTC [INFO ] CHECK: RedoApplyLag - SKIPPED: the DB instance has no read replicas
2026-08-28 18:30:20.612 UTC [INFO ] CHECK: MdsysUser - PASSED
2026-08-28 18:30:20.688 UTC [INFO ] CHECK: ConflictingSynonyms - PASSED
2026-08-28 18:30:20.731 UTC [INFO ] CHECK: WorkspaceManager - PASSED
2026-08-28 18:30:20.790 UTC [INFO ] CHECK: SchemaVersionRegistry - PASSED
2026-08-28 18:30:20.846 UTC [INFO ] CHECK: XmlDbSchema - PASSED
2026-08-28 18:30:20.903 UTC [INFO ] CHECK: ApexStatus - PASSED
2026-08-28 18:30:20.955 UTC [INFO ] CHECK: CtxsysSequences - PASSED
2026-08-28 18:30:21.304 UTC [INFO ] CHECK: InvalidSystemObjects - PASSED
2026-08-28 18:30:21.549 UTC [INFO ] CHECK: InvalidTriggers - PASSED
2026-08-28 18:30:21.601 UTC [INFO ] CHECK: PendingDistributedTransactions - PASSED
2026-08-28 18:30:21.602 UTC [INFO ] Summary: 13 passed, 1 skipped, 0 warnings, 0 errors, 0 blockers
2026-08-28 18:30:21.602 UTC [INFO ] Result: PASSED
2026-08-28 18:30:21.602 UTC [INFO ] The task finished successfully.
```

To list the files in the BDUMP directory, run the following query.

```
SELECT * FROM table(rdsadmin.rds_file_util.listdir('BDUMP')) order by mtime;
```

For more information about the procedure `rdsadmin.rds_file_util.read_text_file`, see [Reading files in a DB instance directory](Appendix.Oracle.CommonDBATasks.Misc.md#Appendix.Oracle.CommonDBATasks.ReadingFiles).

## Interpreting the precheck results
<a name="USER_UpgradeDBInstance.Oracle.Precheck.Interpreting"></a>

The log has one `CHECK:` line for each check, followed by a `Summary:` line and a `Result:` line. Which checks run depends on your engine version, your database architecture, and your DB instance configuration. Each check reports one of the following results.

`PASSED`  
The check found no problem.

`FAILED [BLOCKER]`  
The check found a problem that you must fix before the DB minor version upgrade. The line describes the problem and what to do.

`WARN`  
The check found something that you should review. A warning doesn't block the upgrade.

`SKIPPED`  
The check doesn't apply to your DB instance. The line gives the reason.

`ERROR`  
The check couldn't finish. Run the precheck again.

Every check runs, even when an earlier check fails, so one run reports every problem that the precheck finds. If any check reports `FAILED [BLOCKER]` or `ERROR`, the log shows `Result: FAILED`. Otherwise, it shows `Result: PASSED`.

The following example shows a precheck that found one problem.

```
SQL> SELECT * FROM TABLE(rdsadmin.rds_file_util.read_text_file('BDUMP', 'dbtask-'||:task_id||'.log'));

TEXT
-------------------------------------------------------------------------------------------------------------------------
2026-08-28 18:57:39.105 UTC [INFO ] Starting minor version upgrade precheck...
2026-08-28 18:57:39.105 UTC [INFO ] NOTE: This precheck validates against the current engine version's known checks. Target-version-specific checks (e.g., autoupgrade) are not included.
2026-08-28 18:57:39.112 UTC [INFO ] CHECK: FreeStorageSpace - PASSED
2026-08-28 18:57:39.125 UTC [INFO ] CHECK: SystemTablespace - PASSED
2026-08-28 18:57:39.133 UTC [INFO ] CHECK: AuditTablespace - PASSED
2026-08-28 18:57:39.150 UTC [INFO ] CHECK: RedoApplyLag - SKIPPED: the DB instance has no read replicas
2026-08-28 18:57:39.221 UTC [INFO ] CHECK: MdsysUser - PASSED
2026-08-28 18:57:39.297 UTC [INFO ] CHECK: ConflictingSynonyms - PASSED
2026-08-28 18:57:39.340 UTC [INFO ] CHECK: WorkspaceManager - PASSED
2026-08-28 18:57:39.399 UTC [INFO ] CHECK: SchemaVersionRegistry - PASSED
2026-08-28 18:57:39.455 UTC [INFO ] CHECK: XmlDbSchema - PASSED
2026-08-28 18:57:39.512 UTC [INFO ] CHECK: ApexStatus - PASSED
2026-08-28 18:57:39.564 UTC [INFO ] CHECK: CtxsysSequences - PASSED
2026-08-28 18:57:39.913 UTC [INFO ] CHECK: InvalidSystemObjects - PASSED
2026-08-28 18:57:40.097 UTC [ERROR] CHECK: InvalidTriggers - FAILED [BLOCKER]: The DB instance has triggers that aren't valid. Fix or disable them.
2026-08-28 18:57:40.151 UTC [INFO ] CHECK: PendingDistributedTransactions - PASSED
2026-08-28 18:57:40.152 UTC [INFO ] Summary: 12 passed, 1 skipped, 0 warnings, 0 errors, 1 blocker
2026-08-28 18:57:40.152 UTC [INFO ] RDS can't upgrade the DB instance. Resolve the blockers listed above, and then try again.
2026-08-28 18:57:40.152 UTC [INFO ] Result: FAILED
2026-08-28 18:57:40.152 UTC [INFO ] The task failed.
```

Fix each problem that the log reports, and then run the precheck again to confirm that your DB instance passes.

## What the precheck checks
<a name="USER_UpgradeDBInstance.Oracle.Precheck.Checks"></a>

The following table lists each check and the condition that makes it fail. When a check fails, its line in the log describes the problem and how to fix it.



| Check | Fails when | 
| --- | --- | 
| FreeStorageSpace | The DB instance has less than 768 MB of free storage. | 
| SystemTablespace | The SYSTEM or SYSAUX tablespace has less than 300 MB of free space, or isn't auto-extensible. For a CDB, the precheck checks each container. | 
| AuditTablespace | The audit tablespace has less than 300 MB of free space, or isn't auto-extensible. | 
| RedoApplyLag | A read replica's redo apply lag is more than 5 minutes. Skipped if the DB instance has no read replicas. | 
| MdsysUser | The MDSYS user isn't Oracle-maintained. | 
| ConflictingSynonyms | Synonyms use names that the new Oracle version reserves. | 
| WorkspaceManager | Workspace Manager (WMSYS) objects exist. | 
| SchemaVersionRegistry | One or more SCHEMA\_VERSION\_REGISTRY views aren't valid. | 
| XmlDbSchema | One or more XML DB schema objects aren't valid. | 
| ApexStatus | The APEX component isn't in a VALID state. | 
| CtxsysSequences | The CTXSYS schema doesn't have the 3 Oracle Text sequences (DR\_ID\_SEQ, MESG\_ID\_SEQ, THS\_SEQ). Skipped for a CDB. | 
| InvalidSystemObjects | Oracle-maintained objects aren't valid. | 
| InvalidTriggers | Triggers aren't valid. | 
| PendingDistributedTransactions | Distributed transactions are unresolved. | 

## When to run the precheck
<a name="USER_UpgradeDBInstance.Oracle.Precheck.When"></a>

Some conditions change over time, such as free storage and read replica lag. Run the precheck shortly before you upgrade. If your DB instance uses automatic minor version upgrades, run the precheck after you receive the pending maintenance notification and before your maintenance window.

If you make a change that affects a checked condition, run the precheck again. For example, run it again after you add storage, change a tablespace, drop or recompile objects, or resolve distributed transactions. Changes that don't affect these conditions don't change the result. For example, taking a backup or changing the DB instance class doesn't change the result.

**Note**  
The precheck runs the checks for your current engine version. It doesn't include checks that depend on the version that you upgrade to.