# Known issues and limitations for Amazon RDS for Db2

The following items are known issues and limitations for working with Amazon RDS for Db2:

###### Topics

- [Authentication limitation](#db2-known-issues-limitations-authentication-limit "#db2-known-issues-limitations-authentication-limit")
- [Non-fenced routines](#db2-known-issues-limitations-non-fenced-routines "#db2-known-issues-limitations-non-fenced-routines")
- [Non-automatic storage tablespaces during migration](#db2-known-issues-limitations-non-automatic-storage-tablespaces "#db2-known-issues-limitations-non-automatic-storage-tablespaces")
- [Setting the db2_compatibility_vector parameter](#db2-known-issues-limitations-db2-compatibility-vector "#db2-known-issues-limitations-db2-compatibility-vector")
- [Migrating databases that contain INVALID packages](#db2-known-issues-limitations-invalid-packages-migrating "#db2-known-issues-limitations-invalid-packages-migrating")

## Authentication limitation

Amazon RDS sets `db2auth` to `JCC_ENFORCE_SECMEC` by default.
However, if you don't want to enforce userid and password encryption over the wire, you
can override this setting by changing the `db2auth` parameter to
`CLEAR_TEXT` in the parameter group. For more information, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

## Non-fenced routines

RDS for Db2 doesn't support the creation of non-fenced routines and the migration of
these routines by backing up and restoring data. To check if your database contains any
non-fenced routines, run the following SQL command:

```
SELECT 'COUNT:' || count(*) FROM SYSCAT.ROUTINES where fenced='N' and routineschema not in ('SQLJ','SYSCAT','SYSFUN','SYSIBM','SYSIBMADM','SYSPROC','SYSTOOLS')
```

## Non-automatic storage tablespaces during migration

RDS for Db2 doesn't support the creation of new non-automatic storage tablespaces. When
you use native restore for a one-time migration of your database, RDS for Db2 automatically
converts your non-automatic storage tablespaces to automatic ones, and then restores
your database to RDS for Db2. For information about one-time migrations, see [Migrating from Linux to Linux for Amazon RDS for Db2](db2-one-time-migration-linux.md "db2-one-time-migration-linux.md") and [Migrating from AIX or Windows to Linux for Amazon RDS for Db2](db2-one-time-migration-aix-windows-linux.md "db2-one-time-migration-aix-windows-linux.md").

## Setting the db2_compatibility_vector parameter

With Amazon RDS, you can create an initial database when you create the DB instance and
then modify parameters in an associated parameter group. However, for Db2, if you want
to set the `db2_compatibility_vector` parameter in a parameter group, you
must first modify the parameter in a custom parameter group, create the DB instance
without a database, and then create a database using the
`rdsadmin.create_database` stored procedure.

###### To set the `db2_compatibility_vector` parameter

1. [Create a custom parameter
   group](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). (You can't modify parameters in default parameter
   groups.)
2. [Modify the
   parameter](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
3. [Create a DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
4. [Create a database](db2-managing-databases.md#db2-creating-database "db2-managing-databases.md#db2-creating-database") using the
   `rdsadmin.create_database` stored procedure.
5. [Associate the
   parameter group](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md") with the DB instance that contains the database.

## Migrating databases that contain INVALID packages

If you migrate Db2 databases that contain `INVALID` packages to RDS for Db2 by
using the `RESTORE` command, you could encounter issues when you start to use
the databases. `INVALID` packages can cause issues because of the
authorization setup for the DB instance user `rdsdb` and the removal of
authorization from `PUBLIC`. `INVALID` packages cause the
following commands to fail:

- `db2updv115`
- `db2 "call SYSPROC.ADMIN_REVALIDATE_DB_OBJECTS()"`

Before migrating your database with the `RESTORE` command, ensure that your
database doesn't contain `INVALID` packages by running the following
command:

```
db2 "SELECT 'COUNT:' || count(*) FROM SYSCAT.INVALIDOBJECTS"
```

If the command returns a count greater than zero, then call the following
command:

```
db2 "call SYSPROC.ADMIN_REVALIDATE_DB_OBJECTS()"
```

Afterwards, call the previous command to confirm that your database no longer contains
`INVALID` packages.

```
db2 "SELECT 'COUNT:' || count(*) FROM SYSCAT.INVALIDOBJECTS"
```

Now you are ready to make a backup of your database and restore it to your RDS for Db2 DB
instance.
