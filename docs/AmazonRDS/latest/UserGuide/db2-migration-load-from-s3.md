# Migrating Db2 data through Amazon S3 to Amazon RDS for Db2

With this migration approach, you first save data from a single table into a data file
that you place in an Amazon S3 bucket. Then, you use the [LOAD command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-load "https://www.ibm.com/docs/en/db2/11.5?topic=commands-load")
to load the data from that data file into a table in your Amazon RDS for Db2 database. For more
information about using Amazon S3, see [Integrating an Amazon RDS for Db2 DB instance with Amazon S3](db2-s3-integration.md "db2-s3-integration.md").

###### Topics

- [Saving your data to Amazon S3](#db2-migration-load-from-s3-saving-data-file "#db2-migration-load-from-s3-saving-data-file")
- [Loading your data into RDS for Db2 tables](#db2-migration-load-from-s3-into-db-table "#db2-migration-load-from-s3-into-db-table")

## Saving your data to Amazon S3

To save data from a single table to Amazon S3, use a database utility to extract the data
from your database management system (DBMS) into a CSV file. Then, upload the data file
to Amazon S3.

For storing data files on Amazon S3, you need the following AWS components:

- _An Amazon S3 bucket to store your backup files_:
  If you already have an S3 bucket, you can use that bucket. If you don't have an
  S3 bucket, see [Creating a
  bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.
- _An IAM role to access the S3 bucket_: If
  you already have an IAM role, you can use that role. If you don't have a role,
  see [Step 2: Create an IAM role and attach your IAM policy](db2-s3-integration.md#db2-creating-iam-role "db2-s3-integration.md#db2-creating-iam-role").
- _An IAM policy with trust relationships and
  permissions attached to your IAM role_: For more information,
  see [Step 1: Create an IAM policy](db2-s3-integration.md#db2-creating-iam-policy "db2-s3-integration.md#db2-creating-iam-policy").
- _The IAM role added to your RDS for Db2 DB
  instance_: For more information, see [Step 3: Add your IAM role to your RDS for Db2 DB instance](db2-s3-integration.md#db2-adding-iam-role "db2-s3-integration.md#db2-adding-iam-role").

## Loading your data into RDS for Db2 tables

After you save your data files to Amazon S3, you can load the data from these files into
individual tables on your RDS for Db2 DB instance.

###### To load your Db2 table data into your RDS for Db2 DB database table

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 connect to rdsadmin user `master_username` using `master_password`
```

2. Catalog a storage access alias that points to the Amazon S3 bucket where your saved
   files are stored. Take note of the name of this alias for use in the next step. You only need to perform this step once if you
   plan to load multiple tables from data files stored in the same Amazon S3
   bucket.

The following example catalogs an alias named
`my_s3_alias` that grants a user named `jorge_souza` access to a bucket named
`amzn-s3-demo-bucket`.

```
db2 "call rdsadmin.catalog_storage_access(?, '`my_s3_alias`', '`amzn-s3-demo-bucket`', 'USER', '`jorge_souza`')"
```

For more information about this stored procedure, See [rdsadmin.catalog_storage_access](db2-sp-managing-storage-access.md#db2-sp-catalog-storage-access "db2-sp-managing-storage-access.md#db2-sp-catalog-storage-access"). 3. Run the `LOAD` command using the storage access alias that points
to your Amazon S3 bucket.

###### Note

If the `LOAD` command returns an error, then you might need to
create a VPC gateway endpoint for Amazon S3 and add outbound rules to the
security group. For more information, see [File I/O error](db2-troubleshooting.md#db2-file-input-output-error "db2-troubleshooting.md#db2-file-input-output-error").

The following example loads data from a data file named
`my_s3_datafile.csv` into a table named
`my_db2_table`. The example assumes that the data
file is in the Amazon S3 bucket that the alias named
`my_s3_alias` points to.

```
db2 "load from db2remote://`my_s3_alias`//`my_s3_datafile.csv` of DEL insert into `my_db2_table`";
```

The following example loads LOBs from a data file named
`my_table1_export.ixf` into a table named
`my_db2_table`. The example assumes that the data
file is in the Amazon S3 bucket that the alias named
`my_s3_alias` points to.

```
db2 "call sysproc.admin_cmd('load from "db2remote://`my_s3_alias`//`my_table1_export.ixf`" of ixf
        lobs from "db2remote://`my_s3_alias`//" xml from "db2remote://`my_s3_alias`//"
        modified by lobsinfile implicitlyhiddeninclude identityoverride generatedoverride periodoverride transactionidoverride
        messages on server
        replace into "`my_schema`"."`my_db2_table`"
                               nonrecoverable
        indexing mode incremental allow no access')"
```

Repeat this step for each data file in the Amazon S3 bucket that you want to load
into a table in your RDS for Db2 DB instance.

For more information about the `LOAD` command, see [LOAD
command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-load "https://www.ibm.com/docs/en/db2/11.5?topic=commands-load").
