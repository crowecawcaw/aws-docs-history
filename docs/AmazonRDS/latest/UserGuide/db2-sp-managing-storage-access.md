

# Stored procedures for storage access for RDS for Db2
<a name="db2-sp-managing-storage-access"></a>

The built-in stored procedures described in this topic manage storage access for RDS for Db2 databases that use Amazon S3 for migrating data. For more information, see [Migrating Db2 data through Amazon S3 to Amazon RDS for Db2](db2-migration-load-from-s3.md).

Refer to the following built-in stored procedures for information about their syntax, parameters, usage notes, and examples.

**Topics**
+ [rdsadmin.catalog\_storage\_access](#db2-sp-catalog-storage-access)
+ [rdsadmin.uncatalog\_storage\_access](#db2-sp-uncatalog-storage-access)

## rdsadmin.catalog\_storage\_access
<a name="db2-sp-catalog-storage-access"></a>

Catalogs a storage alias for accessing an Amazon S3 bucket with Db2 data files.

### Syntax
<a name="db2-sp-catalog-storage-access-syntax"></a>

```
db2 "call rdsadmin.catalog_storage_access(
    ?,
    '{{alias}}',
    '{{s3_bucket_name}}',
    '{{grantee_type}}',
    '{{grantee}}'
    )"
```

### Parameters
<a name="db2-sp-catalog-storage-access-parameters"></a>

The following output parameter is required:

?  
A parameter marker that outputs an error message. The datatype is `varchar`.

The following input parameters are required:

{{alias}}  
The alias name for accessing remote storage in an Amazon S3 bucket. The datatype is `varchar`.

{{s3\_bucket\_name}}  
The name of the Amazon S3 bucket where your data resides. The data type is `varchar`.

{{grantee\_type}}  
The type of grantee to receive authorization. The data type is `varchar`. Valid values: `USER`, `GROUP`.

{{grantee}}  
The user or group to receive authorization. The data type is `varchar`. 

### Usage notes
<a name="db2-sp-catalog-storage-access-usage-notes"></a>

Amazon RDS includes the cataloged alias in the IAM role that you added to your RDS for Db2 DB instance. If you remove the IAM role from your DB instance, then Amazon RDS deletes the alias. For more information, see [Migrating Db2 data through Amazon S3 to Amazon RDS for Db2](db2-migration-load-from-s3.md).

For information about checking the status of cataloging your alias, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

### Examples
<a name="db2-sp-catalog-storage-access-examples"></a>

The following example registers an alias called `SAMPLE`. The user `jorge_souza` is granted access to the Amazon S3 bucket called `amzn-s3-demo-bucket`.

```
db2 "call rdsadmin.catalog_storage_access(
    ?,
    'SAMPLE', 
    'amzn-s3-demo-bucket', 
    'USER', 
    'jorge_souza')"
```

## rdsadmin.uncatalog\_storage\_access
<a name="db2-sp-uncatalog-storage-access"></a>

Removes a storage access alias.

### Syntax
<a name="db2-sp-uncatalog-storage-access-syntax"></a>

```
db2 "call rdsadmin.uncatalog_storage_access(
    ?,
    '{{alias}}')"
```

### Parameters
<a name="db2-sp-uncatalog-storage-access-parameters"></a>

The following output parameter is required:

?  
A parameter marker that outputs an error message. The datatype is `varchar`.

The following input parameter is required:

{{alias}}  
The name of the storage alias to remove. The datatype is `varchar`.

### Usage notes
<a name="db2-sp-uncatalog-storage-access-usage-notes"></a>

For information about checking the status of removing your alias, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

### Examples
<a name="db2-sp-uncatalog-storage-access-examples"></a>

The following example removes an alias called `SAMPLE`. This alias no longer provides access to the Amazon S3 bucket it was associated with.

```
db2 "call rdsadmin.uncatalog_storage_access(
    ?,
    'SAMPLE')"
```