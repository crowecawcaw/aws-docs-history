

# Virtual mode for offline source and virtual target
<a name="virtual-data-provider"></a>

AWS Database Migration Service (DMS) offers **Virtual Mode** for data providers in schema conversion. **Virtual Mode** supports two use cases:
+ Offline source – Convert schemas from exported script files without connecting to your source database. Use this when direct connectivity to your source database is not available. **Virtual Mode** for offline source is currently available for Microsoft SQL Server source databases.
+ Virtual target – Convert schemas without provisioning a target database. You can evaluate compatibility, convert and review schema code, and test different target options before provisioning target infrastructure. **Virtual Mode** is available for all supported target databases. For more information about supported target databases, see [Creating and setting target data providers in DMS Schema Conversion](data-providers-target.md).

## Create a data provider in Virtual Mode
<a name="create-virtual-data-provider"></a>

To create a data provider in **Virtual Mode**, turn on **Virtual Mode** on the **Create data provider** page. For more information, see [Create data providers for DMS Schema Conversion](getting-started-data-providers.md).

## Work with a data provider in Virtual Mode
<a name="virtual-data-provider-usage"></a>

**To use a data provider in Virtual Mode in a migration project**

1. Create a new migration project, or choose an existing one and then choose **Modify**.

1. For the source or target data provider, choose the data provider with **Virtual Mode** turned on.

1. For **Secret**, choose any existing valid secret.
**Note**  
When you create or modify a migration project, you specify a Secret and an IAM role for all data providers, including data providers with **Virtual Mode** turned on. For data providers in **Virtual Mode**, these credentials are not used to connect to a database.

1. For **IAM role**, choose the IAM role that has read access to the secret.

1. Choose **Save changes**.

1. Choose the **Schema conversion** tab.

1. Choose **Launch schema conversion**. Wait until the project starts.

Schema conversion works with a data provider in **Virtual Mode** the same way as with a direct connection. DMS Schema Conversion disables actions that require a database connection.

For an offline source, **Refresh from database** is available on the **Databases** node of the source tree. This action clears the object tree and reloads the metadata from the data definition language (DDL) scripts in the S3 bucket.

For a virtual target, use **Save as SQL** on the target tree to export the converted schema code.

## Offline source
<a name="virtual-source-data-provider"></a>

When you turn on **Virtual Mode** for a source data provider, you can convert schemas from exported script files without connecting to your source database. Use this when direct connectivity to your source database is not available. You provide DDL scripts that describe your source database objects. Before you begin, make sure the following requirements are met.

### Prerequisites for an offline source
<a name="virtual-source-prerequisites"></a>

Supported source databases dialects  
+ DDL scripts exported from Microsoft SQL Server
**Note**  
You can export database objects using SQL Server Management Studio (SSMS) or SQL Server Management Objects (SMO). For more information, see [Export SQL Server database objects](export-sql-server-database-objects.md).

DDL scripts requirements  
+ Each database object is stored as a separate `.sql` file with Unicode encoding.
+ Include a separate `.sql` file with a `CREATE DATABASE` statement for each database.
+ Each object file starts with a `USE [{{database_name}}]` statement that identifies which source database the object belongs to.
+ Each file contains one `CREATE` statement for the database object.
+ Database objects referenced in the script use schema-qualified names (for example, `dbo.TableName`). If no schema is specified, `dbo` is used.
+ Any `ALTER` and `DROP` statements in the file are skipped.
When exporting, SQL Server may include additional statements in the same file alongside the primary `CREATE` statement. DMS Schema Conversion processes the following:  
+ `CREATE INDEX` – indexes defined on the table
+ `CREATE TRIGGER` – triggers associated with the table
+ `ALTER TABLE ... ADD DEFAULT` – default values for columns
+ `ALTER TABLE ... ADD CONSTRAINT DEFAULT` – named default constraints
+ `ALTER TABLE ... ALTER COLUMN ... NOT FOR REPLICATION` – column replication settings
All other `ALTER` and `DROP` statements in the file are skipped.

S3 folder structure  
DMS Schema Conversion scans all folders under the S3 path that you specify. It searches for `.sql` files to load database objects. The S3 path can point to a bucket or any prefix in the bucket. The `USE [{{database_name}}]` statement in each file identifies the source database for that object.  
Store the scripts for each database in a separate folder to avoid file name and object name collisions.

S3 bucket configuration  
+ Upload the DDL scripts to an Amazon S3 bucket.
+ Create an IAM role that allows the DMS service principal (`dms.amazonaws.com`) to assume it, and attach a policy granting `s3:GetObject` and `s3:ListBucket` permissions scoped to your S3 bucket. For more information, see [Configure S3 access permissions for an offline source](virtual-source-s3-permissions.md).

## Virtual target
<a name="virtual-target-data-provider"></a>

**Virtual Mode** in a target data provider lets you perform schema conversion without provisioning a target database. When you are ready to migrate, you can switch to a direct database connection.

### Switch a target data provider from virtual mode to a direct database connection
<a name="transition-virtual-to-real-data-provider"></a>

When you are ready to proceed with the migration, modify the data provider to clear **Virtual Mode** and use a direct database connection.

**Important**  
After you turn off **Virtual Mode** and save the data provider, you can't turn it back on. You must provide database connection details for the data provider and a valid secret and IAM role in the associated migration project.

**To switch from **Virtual Mode** to a direct database connection**

1. Sign in to the AWS Management Console, and open the AWS DMS console.

1. In the navigation pane, choose **Data providers**. Then choose the data provider to modify.

1. In the **Associated migration projects** section, review all migration projects that use this data provider.

1. Choose the first associated project.

1. Choose the **Schema conversion** tab.

1. Check the option **Details section** - **Status**.

1. If the status is **Open** and the button **Close schema conversion** is not greyed out, choose it and wait until the project is closed.

1. Repeat the previous steps for all remaining associated migration projects.

1. Confirm that there are no remaining open projects.

1. Return to the data provider and choose **Modify**.

1. Turn off **Virtual Mode**.

1. Enter the connection settings for the database. The connection parameters depend on the database engine. For more information, see [Creating data providers](https://docs.aws.amazon.com/dms/latest/userguide/data-providers-create.html).

1. Choose **Save changes**.
**Note**  
After you save the changes, you can't turn **Virtual Mode** back on.

1. Return to the AWS DMS console.

1. In the navigation pane, choose **Migration Projects**. Then choose the migration project to change the data provider for.

1. Choose **Modify**.

1. For **Secret**, choose the secret that contains the credentials for the database.

1. For **IAM role**, choose the IAM role to use to read the secret. Check that the IAM role specified here is correct, is granted read on the connection credentials secret, and is available to AWS DMS Schema Conversion service.

1. Choose **Save changes**.

1. Choose the **Schema conversion** tab.

1. Choose **Launch schema conversion**. Wait until the project is started.

When you first start the project after transitioning the data provider, you can view the conversion results. You can perform only the following actions:
+ **On node schemas** - Refresh from database.
+ **On database objects** - Apply changes, then save as SQL.

The **Apply** action will apply converted objects to the database.

The **Refresh from database** action loads database objects from the real database. Any unsaved conversion objects will be lost.