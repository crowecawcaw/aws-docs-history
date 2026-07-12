# Real-time SQL plan management in RDS for Oracle

Starting with Oracle Database 26ai (26.0.0.0), Amazon RDS for Oracle supports real-time SQL plan management.
This feature prevents SQL performance regressions by detecting execution plan changes,
evaluating them against earlier plans, and selecting the best-performing plan from a SQL
plan baseline as needed. This process is transparent and doesn't require manual
intervention.

To enable real-time SQL plan management on RDS for Oracle, you use
`DBMS_SPM.CONFIGURE` to turn on the auto evolve task. You then use the
`rdsadmin.rdsadmin_spm_util` package to configure the SYS-owned task
parameters.

###### Topics

- [Overview](#Oracle.RealTimeSPM.Overview "#Oracle.RealTimeSPM.Overview")
- [Requirements](#Oracle.RealTimeSPM.Requirements "#Oracle.RealTimeSPM.Requirements")
- [Enabling real-time SQL plan management](#Oracle.RealTimeSPM.Enabling "#Oracle.RealTimeSPM.Enabling")
- [Verifying the configuration](#Oracle.RealTimeSPM.Verifying "#Oracle.RealTimeSPM.Verifying")
- [Disabling real-time SQL plan management](#Oracle.RealTimeSPM.Disabling "#Oracle.RealTimeSPM.Disabling")
- [rdsadmin\_spm\_util procedures](#Oracle.RealTimeSPM.Procedures "#Oracle.RealTimeSPM.Procedures")
- [Monitoring SQL plan baselines](#Oracle.RealTimeSPM.Monitoring "#Oracle.RealTimeSPM.Monitoring")
- [Considerations](#Oracle.RealTimeSPM.Considerations "#Oracle.RealTimeSPM.Considerations")
- [Related resources](#Oracle.RealTimeSPM.Resources "#Oracle.RealTimeSPM.Resources")

## Overview

A SQL performance regression occurs when the Oracle optimizer chooses a new execution
plan that performs worse than a previous plan. Real-time SQL plan management automates
the detection and prevention of these regressions.

When real-time SQL plan management is enabled, the database does the following:

1. Detects execution plan changes in real time.
2. Evaluates the performance of the new plan against earlier plans.
3. Creates or updates SQL plan baselines automatically.
4. Selects the best-performing plan to prevent regressions.

## Requirements

To use real-time SQL plan management, your DB instance must meet the following
requirements:

- Oracle Database 26ai or higher
- Oracle Enterprise Edition

## Enabling real-time SQL plan management

To enable real-time SQL plan management, complete the following two steps.

### Step 1: Turn on the auto SPM evolve task

Run the following statement as the master user or as a user with the DBA
role:

```
BEGIN
  DBMS_SPM.CONFIGURE('AUTO_SPM_EVOLVE_TASK', 'AUTO');
END;
/
```

### Step 2: Configure the SYS-owned task parameters

The `SYS_AUTO_SPM_EVOLVE_TASK` task is owned by SYS. RDS for Oracle provides
the `rdsadmin.rdsadmin_spm_util` package for this purpose.

Set `ACCEPT_PLANS` to `TRUE` so that the database accepts
evolved plans automatically:

```
EXEC rdsadmin.rdsadmin_spm_util.set_evolve_task_accept_plans('TRUE');
```

(Optional) Set the alternate plan source to `AUTO`:

```
EXEC rdsadmin.rdsadmin_spm_util.set_evolve_task_alternate_plan_source('AUTO');
```

## Verifying the configuration

To verify that real-time SQL plan management is enabled, run the following
query:

```
SELECT parameter_value
FROM DBA_SQL_MANAGEMENT_CONFIG
WHERE parameter_name = 'AUTO_SPM_EVOLVE_TASK';
```

The query returns `AUTO`.

To verify the task parameter settings, run the following query:

```
SELECT parameter_name, parameter_value
FROM DBA_ADVISOR_PARAMETERS
WHERE task_name = 'SYS_AUTO_SPM_EVOLVE_TASK'
  AND parameter_name IN ('ACCEPT_PLANS', 'ALTERNATE_PLAN_SOURCE');
```

## Disabling real-time SQL plan management

To disable real-time SQL plan management, run the following statement:

```
BEGIN
  DBMS_SPM.CONFIGURE('AUTO_SPM_EVOLVE_TASK', 'OFF');
END;
/
```

## rdsadmin\_spm\_util procedures

The `rdsadmin.rdsadmin_spm_util` package provides the following
procedures.

rdsadmin\_spm\_util procedures| Procedure | Parameter | Default | Description |
| --- | --- | --- | --- |
| `set_evolve_task_accept_plans` | `p_value` | `'TRUE'` | Sets the `ACCEPT_PLANS` parameter for<br>`SYS_AUTO_SPM_EVOLVE_TASK`. Valid values are<br>`'TRUE'` and `'FALSE'`. |
| `set_evolve_task_alternate_plan_source` | `p_value` | `'AUTO'` | Sets the `ALTERNATE_PLAN_SOURCE` parameter for<br>`SYS_AUTO_SPM_EVOLVE_TASK`. Valid values are<br>`'AUTO'`, `'CURSOR_CACHE'`,<br>`'AUTOMATIC_WORKLOAD_REPOSITORY'`, and<br>`'SQL_TUNING_SET'`. |

## Monitoring SQL plan baselines

After you enable real-time SQL plan management, you can monitor the plan baselines that
the database manages automatically:

```
SELECT SQL_HANDLE, PLAN_NAME, ENABLED, ACCEPTED, AUTOPURGE
FROM DBA_SQL_PLAN_BASELINES
ORDER BY LAST_MODIFIED DESC;
```

## Considerations

Consider the following when you use real-time SQL plan management:

- Users with the DBA role can call `DBMS_SPM.CONFIGURE` directly.
  This step doesn't require a wrapper.
- The `rdsadmin.rdsadmin_spm_util` procedures are required to
  configure task parameters on the SYS-owned `SYS_AUTO_SPM_EVOLVE_TASK`
  task, because the master user doesn't have direct access to SYS-owned
  advisor tasks.
- Real-time SQL plan management operates transparently. You don't need to
  change your application code.
- SQL plan baselines consume space in the SYSAUX tablespace. Monitor SYSAUX
  usage after you enable the feature.
- The parameter values passed to `DBMS_SPM.CONFIGURE` (such as
  `'AUTO'` and `'OFF'`) are case-sensitive. Use uppercase
  values.

## Related resources

- [DBMS\_SPM](https://docs.oracle.com/en/database/oracle/oracle-database/26/arpls/DBMS_SPM.html "https://docs.oracle.com/en/database/oracle/oracle-database/26/arpls/DBMS_SPM.html") in the Oracle Database documentation
- [Managing SQL plan baselines](https://docs.oracle.com/en/database/oracle/oracle-database/26/tgsql/managing-sql-plan-baselines.html "https://docs.oracle.com/en/database/oracle/oracle-database/26/tgsql/managing-sql-plan-baselines.html") in the Oracle Database
  documentation
