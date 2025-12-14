# Setting LOB support for source databases in

an AWS DMS task

Large binary objects (LOBs) can sometimes be difficult to migrate between systems.
AWS DMS offers a number of options to help with the tuning of LOB columns. To see
which and when data types are considered LOBs by AWS DMS, see the AWS DMS
documentation.

When you migrate data from one database to another, you might take the opportunity
to rethink how your LOBs are stored, especially for heterogeneous migrations. If you
want to do so, there's no need to migrate the LOB data.

If you decide to include LOBs, you can then decide the other LOB settings:

- The LOB mode determines how LOBs are handled:
  - **Full LOB mode** – In full
    LOB mode AWS DMS migrates all LOBs from source to target regardless of
    size. In this configuration, AWS DMS has no information about the
    maximum size of LOBs to expect. Thus, LOBs are migrated one at a
    time, piece by piece. Full LOB mode can be quite slow.
  - **Limited LOB mode** – In
    limited LOB mode, you set a maximum LOB size for DMS to accept. That
    enables DMS to pre-allocate memory and load the LOB data in bulk. LOBs
    that exceed the maximum LOB size are truncated, and a warning is issued
    to the log file. In limited LOB mode, you can gain significant
    performance over full LOB mode. We recommend that you use limited LOB
    mode whenever possible. The maximum value for this parameter is 102400 KB (100 MB).

  ###### Note

  Using the Max LOB size (K) option with a value greater than 63KB
  impacts the performance of a full load configured to run in limited
  LOB mode. During a full load, DMS allocates memory by multiplying
  the Max LOB size (k) value by the Commit rate, and the product is
  multiplied by the number of LOB columns. When DMS cannot
  pre-allocate that memory, it consumes SWAP memory which negatively
  impacts performance of the full load tasks. If you experience
  performance issues when using limited LOB mode, consider decreasing
  the commit rate until you achieve an acceptable level of
  performance. During a CDC mode, DMS allocates memory by multiplying
  the number of LOB Columns by the Max LOB Size parameter specified in
  the Limited LOB task settings, and then by the record size. DMS CDC
  process is single threaded per DMS task. For more information, see
  [Change processing tuning
  settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").

  To validate limited LOB size, you must set
  `ValidationPartialLobSize` to the same value as
  `LobMaxSize` (K).
  - **Inline LOB mode** –
    In inline LOB mode, you set the maximum LOB size that DMS transfers inline.
    LOBs smaller than the specified size are transferred inline. LOBs larger than the
    specified size are replicated using full LOB mode. You can select this option to replicate
    both small and large LOBs when most of the LOBs are small. DMS doesn’t support
    inline LOB mode for endpoints that don’t support Full LOB mode, like S3 and Redshift.

###### Note

With Oracle, LOBs are treated as VARCHAR data types whenever possible.
This approach means that AWS DMS fetches them from the database in bulk,
which is significantly faster than other methods. The maximum size of a
VARCHAR in Oracle is 32 K. Therefore, a limited LOB size of less than 32
K is optimal when Oracle is your source database.

- When a task is configured to run in limited LOB mode, the **Max
  LOB size (K)** option sets the maximum size LOB that AWS DMS
  accepts. Any LOBs that are larger than this value is truncated to this
  value.
- When a task is configured to use full LOB mode, AWS DMS retrieves LOBs in
  pieces. The **LOB chunk size (K)** option determines the
  size of each piece. When setting this option, pay particular attention to
  the maximum packet size allowed by your network configuration. If the LOB
  chunk size exceeds your maximum allowed packet size, you might see
  disconnect errors. The recommended value for
  `LobChunkSize` is 64 kilobytes. Increasing the value
  for `LobChunkSize` above 64 kilobytes can cause task
  failures.
- When a task is configured to run in inline LOB mode, the `InlineLobMaxSize` setting
  determines which LOBs DMS transfers inline.

###### Note

A primary key is mandatory for tables containing LOB columns during Change Data Capture (CDC)
operations. DMS uses this key to look up LOB values in the source table.
This requirement only applies to CDC tasks - full-load tasks can read and
copy entire LOB columns directly from source to target without
restrictions.
For information on the task settings to specify these options, see [Target
metadata task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")

## SQL Commands to check max LOB

column length on source table

Use the following SQL commands to check the Max LOB column length and accordingly
configure the DMS limited LOB settings to avoid any data truncation in the
migration:

**Oracle**

```
SELECT dbms_lob.getlength(<COL_NAME>) as LOB_LENGTH
FROM <TABLE_NAME>
ORDER BY dbms_lob.getlength(<COL_NAME>) DESC
FETCH FIRST 10 ROWS ONLY;

Select ((max(length(<COL_NAME>)))/(1024)) from <TABLE_NAME>
```

**SQL Server**

```
Select top 10 datalength(<COL_NAME>) as fieldsize from <TABLE_NAME> order by datalength(<COL_NAME>) desc;
```

**MySQL**

```
Select (max(length(<COL_NAME>))/(1024)) as "Size in KB" from <TABLE_NAME>;
```

**PostgreSQL**

```
Select max((octet_length(<COL_NAME>))/(1024.0)) as "Size in KB" from <TABLE_NAME>;

```

**Db2 LUW**

```
-- Method 1: Using SYSCAT.COLUMNS (converting to KB)

SELECT TABSCHEMA, TABNAME, COLNAME, LENGTH/1024 as LENGTH_KB, TYPENAME FROM SYSCAT.COLUMNS WHERE TYPENAME IN ('BLOB', 'CLOB', 'DBCLOB') ORDER BY LENGTH DESC;

-- Method 2: For specific table with KB conversion

  SELECT COLNAME, LENGTH/1024 as LENGTH_KB, TYPENAME FROM SYSCAT.COLUMNS WHERE TABSCHEMA = 'YOUR_SCHEMA'AND TABNAME = 'YOUR_TABLE'AND TYPENAME IN ('BLOB', 'CLOB', 'DBCLOB');

-- Method 3: Using SYSIBM.SYSCOLUMNS

SELECT TBCREATOR, TBNAME, NAME, LENGTH/1024 as LENGTH_KB, COLTYPE FROM SYSIBM.SYSCOLUMNS WHERE COLTYPE IN ('BLOB', 'CLOB', 'DBCLOB') ORDER BY LENGTH DESC;

SYBASE :

SELECT c.name as column_name, t.name as data_type, (c.length)/1024 as length_KB FROM syscolumns c JOIN systypes t ON c.usertype = t.usertype WHERE object_name(c.id) = 'YOUR_TABLE_NAME'AND t.name IN ('text', 'image', 'unitext') ORDER BY c.length DESC;
```
