# Accessing online and

archived redo logs

You might want to access your online and archived redo log files for mining with
external tools such as GoldenGate, Attunity, Informatica, and others. To access
these files, do the following:

1. Create directory objects that provide read-only access to the physical
   file paths.

Use `rdsadmin.rdsadmin_master_util.create_archivelog_dir` and
`rdsadmin.rdsadmin_master_util.create_onlinelog_dir`. 2. Read the files using PL/SQL.

You can read the files by using PL/SQL. For more information about reading
files from directory objects, see [Listing files in a
DB instance directory](Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.ListDirectories "Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.ListDirectories") and
[Reading files in a DB
instance directory](Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.ReadingFiles "Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.ReadingFiles").
Accessing transaction logs is supported for the following releases:

- Oracle Database 21c
- Oracle Database 19c
  The following code creates directories that provide read-only access to your
  online and archived redo log files:

###### Important

This code also revokes the `DROP ANY DIRECTORY` privilege.

```
EXEC rdsadmin.rdsadmin_master_util.create_archivelog_dir;
EXEC rdsadmin.rdsadmin_master_util.create_onlinelog_dir;
```

The following code drops the directories for your online and archived redo log
files.

```
EXEC rdsadmin.rdsadmin_master_util.drop_archivelog_dir;
EXEC rdsadmin.rdsadmin_master_util.drop_onlinelog_dir;
```

The following code grants and revokes the `DROP ANY DIRECTORY`
privilege.

```
EXEC rdsadmin.rdsadmin_master_util.revoke_drop_any_directory;
EXEC rdsadmin.rdsadmin_master_util.grant_drop_any_directory;
```
