# MSCK Optimization

Hive stores a list of partitions for each table in its metastore. However, when
partitions are directly added to or removed from the file system, the Hive metastore
is unaware of these changes. The [MSCK command](<https://cwiki.apache.org/confluence/display/hive/languagemanual+ddl#LanguageManualDDL-RecoverPartitions(MSCKREPAIRTABLE)> "https://cwiki.apache.org/confluence/display/hive/languagemanual+ddl#LanguageManualDDL-RecoverPartitions(MSCKREPAIRTABLE)") updates the partition metadata in the Hive metastore for
partitions that were directly added to or removed from the file system. The syntax
for the command is:

```
MSCK [REPAIR] TABLE table_name [ADD/DROP/SYNC PARTITIONS];
```

Hive implements this command as follows:

1. Hive retrieves all the partitions for the table from the metastore. From
   the list of partition paths that do not exist in the file system then
   creates a list of partitions to drop from the metastore.
2. Hive gathers the partition paths present in the file system, compares them
   with the list of partitions from the metastore, and generates a list of
   partitions that need to be added to the metastore.
3. Hive updates the metastore using `ADD`, `DROP`, or
   `SYNC` mode.

###### Note

When there are many partitions in the metastore, the step to check if a
partition does not exist in the file system takes a long time to run because the
file system's `exists` API call must be made for each
partition.

In Amazon EMR 6.5.0, Hive introduced a flag called
`hive.emr.optimize.msck.fs.check`. When enabled, this flag causes
Hive to check for the presence of a partition from the list of partition paths from
the file system that is generated in step 2 above instead of making file system API
calls. In Amazon EMR 6.8.0, Hive enabled this optimization by default, eliminating the
need to set the flag `hive.emr.optimize.msck.fs.check`.
