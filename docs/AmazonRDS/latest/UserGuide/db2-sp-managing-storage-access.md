# Stored procedures for storage access for RDS for Db2

The built-in stored procedures described in this topic manage storage access for RDS for Db2
databases that use Amazon S3 for migrating data. For more information, see [Migrating Db2 data through Amazon S3 to Amazon RDS for Db2](db2-migration-load-from-s3.md "db2-migration-load-from-s3.md").

Refer to the following built-in stored procedures for information about their syntax,
parameters, usage notes, and examples.

###### Stored procedures

- [rdsadmin.catalog_storage_access](#db2-sp-catalog-storage-access "#db2-sp-catalog-storage-access")
- [rdsadmin.uncatalog_storage_access](#db2-sp-uncatalog-storage-access "#db2-sp-uncatalog-storage-access")

## rdsadmin.catalog_storage_access

Catalogs a storage alias for accessing an Amazon S3 bucket with Db2 data files.

### Syntax

```
db2 "call rdsadmin.catalog_storage_access(
    ?,
    '`alias`',
    '`s3_bucket_name`',
    '`grantee_type`',
    '`grantee`'
    )"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. The datatype is
`varchar`.

The following input parameters are required:

`alias`

The alias name for accessing remote storage in an Amazon S3 bucket. The
datatype is `varchar`.

`s3_bucket_name`

The name of the Amazon S3 bucket where your data resides. The data type is
`varchar`.

`grantee_type`

The type of grantee to receive authorization. The data type is
`varchar`. Valid values: `USER`,
`GROUP`.

`grantee`

The user or group to receive authorization. The data type is
`varchar`.

### Usage notes

Amazon RDS includes the cataloged alias in the IAM role that you added to your
RDS for Db2 DB instance. If you remove the IAM role from your DB instance, then Amazon RDS
deletes the alias. For more information, see [Migrating Db2 data through Amazon S3 to Amazon RDS for Db2](db2-migration-load-from-s3.md "db2-migration-load-from-s3.md").

For information about checking the status of cataloging your alias, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

### Examples

The following example registers an alias called `SAMPLE`. The user
`jorge_souza` is granted access to the Amazon S3 bucket called
`amzn-s3-demo-bucket`.

```
db2 "call rdsadmin.catalog_storage_access(
    ?,
    'SAMPLE',
    'amzn-s3-demo-bucket',
    'USER',
    'jorge_souza')"
```

## rdsadmin.uncatalog_storage_access

Removes a storage access alias.

### Syntax

```
db2 "call rdsadmin.uncatalog_storage_access(
    ?,
    '`alias`')"
```

### Parameters

The following output parameter is required:

?

A parameter marker that outputs an error message. The datatype is
`varchar`.

The following input parameter is required:

`alias`

The name of the storage alias to remove. The datatype is
`varchar`.

### Usage notes

For information about checking the status of removing your alias, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

### Examples

The following example removes an alias called `SAMPLE`. This alias no
longer provides access to the Amazon S3 bucket it was associated with.

```
db2 "call rdsadmin.uncatalog_storage_access(
    ?,
    'SAMPLE')"
```
