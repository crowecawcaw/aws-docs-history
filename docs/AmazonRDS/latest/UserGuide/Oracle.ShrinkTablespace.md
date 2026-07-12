# Shrinking tablespaces in RDS for Oracle

Starting with Oracle Database 26ai (26.0.0.0), Amazon RDS for Oracle supports tablespace shrinking with the
`rdsadmin.rdsadmin_util.shrink_tablespace` procedure. Use this procedure to
reclaim unused space in a tablespace by shrinking its datafiles. Shrinking reduces storage
consumption without data migration or tablespace recreation.

###### Topics

- [Overview](#Oracle.ShrinkTablespace.Overview "#Oracle.ShrinkTablespace.Overview")
- [Requirements](#Oracle.ShrinkTablespace.Requirements "#Oracle.ShrinkTablespace.Requirements")
- [Syntax](#Oracle.ShrinkTablespace.Syntax "#Oracle.ShrinkTablespace.Syntax")
- [Parameters](#Oracle.ShrinkTablespace.Parameters "#Oracle.ShrinkTablespace.Parameters")
- [Examples](#Oracle.ShrinkTablespace.Examples "#Oracle.ShrinkTablespace.Examples")
- [Considerations](#Oracle.ShrinkTablespace.Considerations "#Oracle.ShrinkTablespace.Considerations")
- [Related resources](#Oracle.ShrinkTablespace.Resources "#Oracle.ShrinkTablespace.Resources")

## Overview

Over time, tablespaces in an Oracle database can accumulate unused space from deleted
or reorganized data. The `rdsadmin.rdsadmin_util.shrink_tablespace` procedure
wraps the Oracle `DBMS_SPACE.SHRINK_TABLESPACE` functionality and handles the
required internal privileges for you.

Tablespace shrinking supports the following modes:

- **Analyze mode**
  (`DBMS_SPACE.TS_MODE_ANALYZE`) – Evaluates the tablespace
  and reports how much space you can reclaim, without making changes.
- **Shrink mode**
  (`DBMS_SPACE.TS_MODE_SHRINK`) – Moves objects and resizes
  the datafiles in the tablespace to reclaim unused space. This is the default
  mode.

## Requirements

To use tablespace shrinking, your DB instance must meet the following requirements:

- Oracle Database 26ai or higher
- Oracle Enterprise Edition

## Syntax

```
EXEC rdsadmin.rdsadmin_util.shrink_tablespace(
  p_tablespace_name => '`tablespace_name`',
  p_shrink_mode     => `mode`,
  p_target_size     => `target_bytes`);
```

## Parameters

shrink\_tablespace parameters| Parameter name | Data type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| `p_tablespace_name` | `VARCHAR2` | — | Yes | The name of the tablespace to shrink. |
| `p_shrink_mode` | `NUMBER` | `2` (`TS_MODE_SHRINK`) | No | The shrink mode. Use `DBMS_SPACE.TS_MODE_ANALYZE`<br>(`1`) to analyze only, or<br>`DBMS_SPACE.TS_MODE_SHRINK` (`2`) to<br>perform the shrink. |
| `p_target_size` | `NUMBER` | `0` | No | The target size, in bytes. Use `0` (the default) to<br>shrink to the minimum possible size. Specify a positive value to<br>shrink to a specific target. |

## Examples

### Analyzing a tablespace for reclaimable space

To analyze a tablespace without making changes, run the following command:

```
EXEC rdsadmin.rdsadmin_util.shrink_tablespace('USERS', DBMS_SPACE.TS_MODE_ANALYZE);
```

The following is example output:

```
-------------------ANALYZE RESULT-------------------
Total Movable Objects: 0
Total Movable Size(GB): 0
Original Datafile Size(GB): .1
Suggested Target Size(GB): .06
Process Time: +00 00:00:00.021513
```

### Shrinking a tablespace to the minimum size

To shrink a tablespace and reclaim all unused space, run the following
command:

```
EXEC rdsadmin.rdsadmin_util.shrink_tablespace('USERS');
```

The following is example output:

```
-------------------SHRINK RESULT-------------------
Total Moved Objects: 0
Total Moved Size(GB): 0
Original Datafile Size(GB): .1
New Datafile Size(GB): .05
Process Time: +00 00:00:00.281151
```

### Shrinking a tablespace to a specific target size

To shrink a tablespace to a target size in bytes, specify the
`p_target_size` parameter. If the target is smaller than the minimum
achievable size, Oracle adjusts it upward automatically:

```
EXEC rdsadmin.rdsadmin_util.shrink_tablespace('USERS', DBMS_SPACE.TS_MODE_SHRINK, 52428800);
```

## Considerations

Consider the following when you shrink a tablespace:

- Tablespace shrinking is an online operation. Objects in the tablespace remain
  accessible during the shrink.
- The shrink operation might move objects, such as tables and indexes, within
  the tablespace to consolidate free space before it resizes the datafiles.
- Indexes remain valid after the shrink operation, and data integrity is
  preserved.
- If the value of `p_target_size` is smaller than the space that
  objects currently occupy, Oracle adjusts the target to the minimum achievable
  size.
- The value of `p_target_size` must not exceed the current tablespace
  size. Specify a target that is smaller than or equal to the current size.
- Active transactions on objects in the tablespace might prevent the operation
  from reclaiming all available space. For best results, run the shrink during a
  period of low activity.
- Calling `DBMS_SPACE.SHRINK_TABLESPACE` directly without the
  `rdsadmin_util` wrapper isn't supported. Always use the
  `rdsadmin.rdsadmin_util.shrink_tablespace` wrapper.

## Related resources

- [DBMS\_SPACE.SHRINK\_TABLESPACE](https://docs.oracle.com/en/database/oracle/oracle-database/26/arpls/DBMS_SPACE.html "https://docs.oracle.com/en/database/oracle/oracle-database/26/arpls/DBMS_SPACE.html") in the Oracle Database
  documentation
- For more information, see [Performing common database tasks for Oracle DB instances](Appendix.Oracle.CommonDBATasks.Database.md "Appendix.Oracle.CommonDBATasks.Database.md").
