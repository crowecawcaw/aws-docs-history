# Backing up and restoring a

CDB

You can back up and restore your CDB using either RDS DB snapshots or Recovery Manager
(RMAN).

## Backing up and restoring a CDB using

DB snapshots

DB snapshots work similarly in the CDB and non-CDB architectures. The principal differences
are as follows:

- When you restore a DB snapshot of a CDB, you can't rename the CDB. The CDB is named
  `RDSCDB` and can't be changed.
- When you restore a DB snapshot of a CDB, you can't rename PDBs. You can modify the
  PDB name by using the [modify-tenant-database](../APIReference/API_ModifyTenantDatabase.md "../APIReference/API_ModifyTenantDatabase.md") command.
- To find tenant databases in a snapshot, use the CLI command [describe-db-snapshot-tenant-databases](../APIReference/API_DescribeDBSnapshotTenantDatabases.md "../APIReference/API_DescribeDBSnapshotTenantDatabases.md").
- You can't directly interact with the tenant databases in a CDB snapshot that
  uses the multi-tenant architecture configuration. If you restore the DB snapshot, you
  restore all its tenant databases.
- RDS for Oracle implicitly copies tags on a tenant database to the tenant database in
  a DB snapshot. When you restore a tenant database, the tags appear in the restored
  database.
- If you restore a DB snapshot and specify new tags using the `--tags`
  parameter, the new tags overwrite all existing tags.
- If you take a DB snapshot of a CDB instance that has tags, and you specify
  `--copy-tags-to-snapshot`, RDS for Oracle copies tags from the tenant
  databases to the tenant databases in the snapshot.

For more information, see [Oracle Database considerations](USER_RestoreFromSnapshot.md#USER_RestoreFromSnapshot.Oracle "USER_RestoreFromSnapshot.md#USER_RestoreFromSnapshot.Oracle").

## Backing up and restoring a CDB using RMAN

To learn how to back up and restore a CDB or individual tenant database using RMAN,
see [Performing common RMAN tasks for
Oracle DB instances](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md").
