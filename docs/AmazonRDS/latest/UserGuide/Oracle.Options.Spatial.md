# Oracle Spatial

Amazon RDS supports Oracle Spatial through the use of the `SPATIAL` option. Oracle
Spatial provides a SQL schema and functions that facilitate the storage, retrieval, update,
and query of collections of spatial data in an Oracle database. For more information, see
[Spatial Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/19/spatl/spatial-concepts.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/spatl/spatial-concepts.html") in the Oracle documentation. Amazon RDS supports Oracle Spatial in
all editions of all supported releases.

## How Supplemental Patch Bundles (SPBs) work

Every quarter, RDS for Oracle releases new minor engine versions for every supported major
engine. A Release Update (RU) engine version incorporates bug fixes from Oracle by
including the RU patches for the specified quarter. A Supplemental Patch Bundle (SPB)
engine version contains all of the RU patches plus additional supplemental patches. If
your DB instance uses Oracle Spatial and you require additional patches related to the
Spatial option, use the SPB release. For example, 19.0.0.0.ru-2026-04.spb-1.r1 is a
minor engine version that contains the RU patches in engine version
19.0.0.0.ru-2026-04.rur-2026-04.r1 plus supplemental patches. SPBs are supported
for Oracle Database 19c and Oracle Database 26ai.

###### Note

Spatial Patch Bundle has been renamed to Supplemental Patch Bundle (SPB). SPBs
now include additional bundle patches beyond Oracle Spatial such as Data Pump and
GoldenGate. The abbreviation "SPB" remains unchanged. All existing SPB engine
versions continue to work as before.

SPBs function in the same way as RUs, although they are named differently. An RU uses
the naming format 19.0.0.0.ru-2025-01.rur-2025-01.r1. An SPB name includes the text
"spb," as in 19.0.0.0.ru-2026-04.spb-1.r1. Typically, an SPB is released 2–3
weeks after its corresponding quarterly RU. For example, 19.0.0.0.ru-2026-04.spb-1.r1 is
released after 19.0.0.0.ru-2026-04.rur-2026-04.r1.

RDS for Oracle has separate paths for automatic minor version upgrades of RUs and
SPBs. If your DB instance uses an RU, then RDS automatically upgrades your instance to
an RU. If your DB instance uses an SPB, then RDS upgrades your instance to an SPB.

For more information about RUs and SPBs, see [Oracle minor version upgrades](USER_UpgradeDBInstance.Oracle.Minor.md "USER_UpgradeDBInstance.Oracle.Minor.md"). For a list of supported RUs
and SPBs for Oracle Database 19c, see [Amazon RDS for
Oracle Database 19c (19.0.0.0)](../OracleReleaseNotes/oracle-version-19-0.md "../OracleReleaseNotes/oracle-version-19-0.md") in _Amazon RDS for Oracle Release
Notes_.

## Prerequisites for Oracle Spatial

The following are prerequisites for using Oracle Spatial:

- Make sure that your DB instance is of a sufficient instance class. Oracle
  Spatial isn't supported for the db.t3.small DB instance
  classes. For more information, see [RDS for Oracle DB instance classes](Oracle.Concepts.InstanceClasses.md "Oracle.Concepts.InstanceClasses.md").
- Make sure that your DB instance has **Auto Minor Version
  Upgrade** enabled. This option enables your DB instance to receive
  minor DB engine version upgrades automatically when they become available and is
  required for any options that install the Oracle Java Virtual Machine (JVM).
  Amazon RDS uses this option to update your DB instance to the latest Oracle Patch Set
  Update (PSU) or Release Update (RU). For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md "Overview.DBInstance.Modifying.md").

## Best practices for Oracle Spatial

The following are best practices for using Oracle Spatial:

- For maximum security, use the `SPATIAL` option with Secure Sockets
  Layer (SSL). For more information, see [Oracle Secure Sockets Layer](Appendix.Oracle.Options.SSL.md "Appendix.Oracle.Options.SSL.md").
- Configure your DB instance to restrict access to your DB instance. For more
  information, see [Scenarios for accessing a DB instance in a VPC](USER_VPC.Scenarios.md "USER_VPC.Scenarios.md") and [Working with a DB instance in a VPC](USER_VPC.WorkingWithRDSInstanceinaVPC.md "USER_VPC.WorkingWithRDSInstanceinaVPC.md").

## Adding the Oracle Spatial option

The following is the general process for adding the `SPATIAL` option to a
DB instance:

1. Create a new option group, or copy or modify an existing option group.
2. Add the option to the option group.
3. Associate the option group with the DB instance.

If Oracle Java Virtual Machine (JVM) is _not_ installed on the DB instance, there is a brief
outage while the `SPATIAL` option is added. There is no outage if Oracle Java Virtual Machine (JVM) is
already installed on the DB instance. After you add the option, you don't need to restart your DB instance.
As soon as the option group is active, Oracle Spatial is available.

###### Note

During this outage, password verification functions are disabled briefly. You can
also expect to see events related to password verification functions during the
outage. Password verification functions are enabled again before the Oracle DB
instance is available.

###### To add the `SPATIAL` option to a DB instance

1. Determine the option group that you want to use. You can create a new option
   group or use an existing option group. If you want to use an existing option
   group, skip to the next step. Otherwise, create a custom DB option group with
   the following settings:

   1. For **Engine**, choose the Oracle edition for your DB
      instance.
   2. For **Major engine version**, choose the version of
      your DB instance.For more information, see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create").

2. Add the **SPATIAL** option to the option group. For more
   information about adding options, see [Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption").
3. Apply the option group to a new or existing DB instance:

   - For a new DB instance, you apply the option group when you launch the
     instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
   - For an existing DB instance, you apply the option group by modifying
     the instance and attaching the new option group. For more information,
     see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md "Overview.DBInstance.Modifying.md").

## Removing the Oracle Spatial option

After you drop all objects that use data types provided by the `SPATIAL` option, you can drop the
option from a DB instance. If Oracle Java Virtual Machine (JVM) is _not_ installed on the DB
instance, there is a brief outage while the `SPATIAL` option is removed. There is no outage if Oracle
Java Virtual Machine (JVM) is already installed on the DB instance. After you remove the `SPATIAL`
option, you don't need to restart your DB instance.

###### To drop the `SPATIAL` option

1. Back up your data.

###### Warning

If the instance uses data types that were enabled as part of the option, and if you remove the
`SPATIAL` option, you can lose data. For more information, see [Backing up, restoring, and exporting data](CHAP_CommonTasks.BackupRestore.md "CHAP_CommonTasks.BackupRestore.md"). 2. Check whether any existing objects reference data types or features of the `SPATIAL` option.

If `SPATIAL` options exist, the instance can get stuck when applying the new option group
that doesn't have the `SPATIAL` option. You can identify the objects by using the following
queries:

```
SELECT OWNER, SEGMENT_NAME, TABLESPACE_NAME, BYTES/1024/1024 mbytes
FROM   DBA_SEGMENTS
WHERE  SEGMENT_TYPE LIKE '%TABLE%'
AND    (OWNER, SEGMENT_NAME) IN
       (SELECT DISTINCT OWNER, TABLE_NAME
        FROM   DBA_TAB_COLUMNS
        WHERE  DATA_TYPE='SDO_GEOMETRY'
        AND    OWNER <> 'MDSYS')
ORDER BY 1,2,3,4;

SELECT OWNER, TABLE_NAME, COLUMN_NAME
FROM   DBA_TAB_COLUMNS
WHERE  DATA_TYPE = 'SDO_GEOMETRY'
AND    OWNER <> 'MDSYS'
ORDER BY 1,2,3;
```

3. Drop any objects that reference data types or features of the `SPATIAL` option.
4. Do one of the following:

   - Remove the `SPATIAL` option from the option group it belongs to. This change affects
     all DB instances that use the option group. For more information, see [Removing an option from an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption").
   - Modify the DB instance and specify a different option group that doesn't include the
     `SPATIAL` option. This change affects a single DB instance. You can specify the
     default (empty) option group, or a different custom option group. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md "Overview.DBInstance.Modifying.md").
