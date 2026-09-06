

# Stored procedures for buffer pools for RDS for Db2
<a name="db2-sp-managing-buffer-pools"></a>

The built-in stored procedures described in this topic manage buffer pools for Amazon RDS for Db2 databases. To run these procedures, the master user must first connect to the `rdsadmin` database. 

These stored procedures are used in a variety of tasks. This list isn't exhaustive.
+ [Common tasks for buffer pools](db2-managing-buffer-pools.md)
+ [Generating performance reports](db2-managing-databases.md#db2-generating-performance-reports)
+ [Copying database metadata with db2look](db2-native-db2-tools-db2look.md)
+ [Creating a repository database for IBM Db2 Data Management Console](db2-connecting-with-ibm-data-management-console.md#db2-creating-repo-db-monitoring-dmc)

Refer to the following built-in stored procedures for information about their syntax, parameters, usage notes, and examples.

**Topics**
+ [rdsadmin.create\_bufferpool](#db2-sp-create-buffer-pool)
+ [rdsadmin.alter\_bufferpool](#db2-sp-alter-buffer-pool)
+ [rdsadmin.drop\_bufferpool](#db2-sp-drop-buffer-pool)

## rdsadmin.create\_bufferpool
<a name="db2-sp-create-buffer-pool"></a>

Creates a buffer pool.

### Syntax
<a name="db2-sp-create-buffer-pool-syntax"></a>

```
db2 "call rdsadmin.create_bufferpool(
    '{{database_name}}', 
    '{{buffer_pool_name}}', 
    {{buffer_pool_size}}, 
    '{{immediate}}', 
    '{{automatic}}', 
    {{page_size}}, 
    {{number_block_pages}}, 
    {{block_size}})"
```

### Parameters
<a name="db2-sp-create-buffer-pool-parameters"></a>

The following parameters are required:

{{database\_name}}  
The name of the database to run the command on. The data type is `varchar`.

{{buffer\_pool\_name}}  
The name of the buffer pool to create. The data type is `varchar`.

The following parameters are optional:

{{buffer\_pool\_size}}  
The size of the buffer pool in number of pages. The data type is `integer`. The default is `-1`.

{{immediate}}  
Specifies whether the command runs immediately. The data type is `char`. The default is `Y`.

{{automatic}}  
Specifies whether to set the buffer pool to automatic. The data type is `char`. The default is `Y`.

{{page\_size}}  
The page size of the buffer pool. The data type is `integer`. Valid values: `4096`, `8192`, `16384`, `32768`. The default is `8192`.

{{number\_block\_pages}}  
The number of block pages in the buffer pools. The data type is `integer`. The default is `0`.

{{block\_size}}  
The block size for the block pages. The data type is `integer`. Valid values: `2` to `256`. The default is `32`.

### Usage notes
<a name="db2-sp-create-buffer-pool-usage-notes"></a>

For information about checking the status of creating a buffer pool, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

### Examples
<a name="db2-sp-create-buffer-pool-examples"></a>

**Example 1: Creating buffer pool with default parameters**

The following example creates a buffer pool called `BP8` for a database called `TESTDB` with default parameters, so the buffer pool uses an 8 KB page size. 

```
db2 "call rdsadmin.create_bufferpool(
    'TESTDB', 
    'BP8')"
```

**Example 2: Creating buffer pool to run immediately with automatic allocation**

The following example creates a buffer pool called `BP16` for a database called `TESTDB` that uses a 16 KB page size with an initial page count of 1,000 and is set to automatic. Db2 runs the command immediately. If you use an initial page count of -1, then Db2 will use automatic allocation of pages.

```
db2 "call rdsadmin.create_bufferpool(
    'TESTDB', 
    'BP16', 
    1000, 
    'Y', 
    'Y', 
    16384)"
```

**Example 3: Creating buffer pool to run immediately using block pages**

The following example creates a buffer pool called `BP16` for a database called `TESTDB`. This buffer pool has a 16 KB page size with an initial page count of 10,000. Db2 runs the command immediately using 500 block pages with a block size of 512.

```
db2 "call rdsadmin.create_bufferpool(
    'TESTDB', 
    'BP16',
    10000, 
    'Y', 
    'Y', 
    16384, 
    500, 
    512)"
```

## rdsadmin.alter\_bufferpool
<a name="db2-sp-alter-buffer-pool"></a>

Alters a buffer pool.

### Syntax
<a name="db2-sp-alter-buffer-pool-syntax"></a>

```
db2 "call rdsadmin.alter_bufferpool(
    '{{database_name}}', 
    '{{buffer_pool_name}}', 
    {{buffer_pool_size}}, 
    '{{immediate}}', 
    '{{automatic}}', 
    {{change_number_blocks}}, 
    {{number_block_pages}}, 
    {{block_size}})"
```

### Parameters
<a name="db2-sp-alter-buffer-pool-parameters"></a>

The following parameters are required:

{{database\_name}}  
The name of the database to run the command on. The data type is `varchar`.

{{buffer\_pool\_name}}  
The name of the buffer pool to alter. The data type is `varchar`.

{{buffer\_pool\_size}}  
The size of the buffer pool in number of pages. The data type is `integer`.

The following parameters are optional:

{{immediate}}  
Specifies whether the command runs immediately. The data type is `char`. The default is `Y`.

{{automatic}}  
Specifies whether to set the buffer pool to automatic. The data type is `char`. The default is `N`.

{{change\_number\_blocks}}  
Specifies whether there is a change to the number of block pages in the buffer pool. The data type is `char`. The default is `N`.

{{number\_block\_pages}}  
The number of block pages in the buffer pools. The data type is `integer`. The default is `0`.

{{block\_size}}  
The block size for the block pages. The data type is `integer`. Valid values: `2` to `256`. The default is `32`.

### Usage notes
<a name="db2-sp-alter-buffer-pool-usage-notes"></a>

For information about checking the status of altering a buffer pool, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

### Examples
<a name="db2-sp-alter-buffer-pool-examples"></a>

The following example alters a buffer pool called `BP16` for a database called `TESTDB` to non-automatic, and changes the size to 10,000 pages. Db2 runs this command immediately. 

```
db2 "call rdsadmin.alter_bufferpool(
    'TESTDB',
    'BP16', 
    10000, 
    'Y', 
    'N')"
```

## rdsadmin.drop\_bufferpool
<a name="db2-sp-drop-buffer-pool"></a>

Drops a buffer pool.

### Syntax
<a name="db2-sp-drop-buffer-pool-syntax"></a>

```
db2 "call rdsadmin.drop_bufferpool(
    '{{database_name}}', 
    '{{buffer_pool_name}}'"
```

### Parameters
<a name="db2-sp-drop-buffer-pool-parameters"></a>

The following parameters are required:

{{database\_name}}  
The name of the database that the buffer pool belongs to. The data type is `varchar`.

{{buffer\_pool\_name}}  
The name of the buffer pool to drop. The data type is `varchar`.

### Usage notes
<a name="db2-sp-drop-buffer-pool-usage-notes"></a>

For information about checking the status of dropping a buffer pool, see [rdsadmin.get\_task\_status](db2-user-defined-functions.md#db2-udf-get-task-status).

### Examples
<a name="db2-sp-drop-buffer-pool-examples"></a>

The following example drops a buffer pool called `BP16` for a database called `TESTDB`.

```
db2 "call rdsadmin.drop_bufferpool(
    'TESTDB',
    'BP16')"
```