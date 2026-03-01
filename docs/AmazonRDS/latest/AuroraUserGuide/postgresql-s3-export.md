# Exporting data from an Aurora PostgreSQL DB cluster to Amazon S3

You can query data from an Aurora PostgreSQL DB cluster
and export it directly into files stored in an Amazon S3 bucket. To do this, you first install the Aurora PostgreSQL
`aws_s3` extension. This extension provides you with
the functions that you use to export the results of queries to Amazon S3. Following, you can find out how to install the extension and how to export data to Amazon S3.

You can export from a provisioned or an Aurora Serverless v2 DB instance. These steps aren't supported for Aurora Serverless v1.

###### Note

Cross-account export to Amazon S3 isn't supported.

All currently available versions of Aurora PostgreSQL support exporting data to Amazon Simple Storage Service. For detailed version information,
see [Amazon Aurora PostgreSQL updates](../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md "../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md")
in the _Release Notes for Aurora PostgreSQL_.

If you don't have a bucket set up for your export, see the following topics
the _Amazon Simple Storage Service User Guide_.

- [Setting up Amazon S3](../../../AmazonS3/latest/userguide/setting-up-s3.md "../../../AmazonS3/latest/userguide/setting-up-s3.md")
- [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md")
  By default, the data exported from Aurora PostgreSQL to Amazon S3 uses server-side encryption with AWS managed key. You can
  alternatively use customer managed key that you have already created. If you are using bucket encryption,
  the Amazon S3 bucket must be encrypted with AWS Key Management Service (AWS KMS) key (SSE-KMS). Currently, buckets encrypted with Amazon S3 managed keys (SSE-S3) are not supported.

###### Note

You can save DB and DB cluster snapshot data to Amazon S3 using the AWS Management Console, AWS CLI, or Amazon RDS
API. For more information, see [Exporting DB cluster snapshot data to Amazon S3](aurora-export-snapshot.md "aurora-export-snapshot.md").

###### Topics

- [Installing the aws_s3 extension](#USER_PostgreSQL.S3Export.InstallExtension "#USER_PostgreSQL.S3Export.InstallExtension")
- [Overview of exporting data to Amazon S3](#postgresql-s3-export-overview "#postgresql-s3-export-overview")
- [Specifying the Amazon S3 file path to export to](#postgresql-s3-export-file "#postgresql-s3-export-file")
- [Setting up access to an Amazon S3 bucket](postgresql-s3-export-access-bucket.md "postgresql-s3-export-access-bucket.md")
- [Exporting query data using the aws_s3.query_export_to_s3 function](postgresql-s3-export-examples.md "postgresql-s3-export-examples.md")
- [Function reference](postgresql-s3-export-functions.md "postgresql-s3-export-functions.md")
- [Troubleshooting access to Amazon S3](postgresql-s3-export-troubleshoot.md "postgresql-s3-export-troubleshoot.md")

## Installing the aws_s3 extension

Before you can use Amazon Simple Storage Service with your Aurora PostgreSQL DB cluster,
you need to install the
`aws_s3` extension. This extension provides functions for exporting data from
the writer instance of an
Aurora PostgreSQL DB cluster
to an Amazon S3 bucket. It also provides functions for importing data from an Amazon S3. For more information,
see [Importing data from Amazon S3 into an Aurora PostgreSQL DB cluster](USER_PostgreSQL.md "USER_PostgreSQL.md").
The `aws_s3` extension depends on some of the helper functions in the
`aws_commons` extension, which is installed automatically when needed.

###### To install the `aws_s3` extension

1. Use psql (or pgAdmin) to connect to the writer instance of your
   Aurora PostgreSQL DB cluster
   as a user that has `rds_superuser` privileges. If you kept the default name during the setup
   process, you connect as `postgres`.

```
psql --host=`111122223333`.`aws-region`.rds.amazonaws.com --port=5432 --username=postgres --password
```

2. To install the extension, run the following command.

```
`postgres=>` CREATE EXTENSION aws_s3 CASCADE;
`NOTICE: installing required extension "aws_commons"
CREATE EXTENSION`
```

3. To verify that the extension is installed, you can use the psql `\dx` metacommand.

```
`postgres=>` \dx
 `List of installed extensions
 Name | Version | Schema | Description
-------------+---------+------------+---------------------------------------------
 aws_commons | 1.2 | public | Common data types across AWS services
 aws_s3 | 1.1 | public | AWS S3 extension for importing data from S3
 plpgsql | 1.0 | pg_catalog | PL/pgSQL procedural language
(3 rows)`
```

The functions for importing data from Amazon S3 and exporting data to Amazon S3 are now available to use.

### Verify that your Aurora PostgreSQL version supports exports to Amazon S3

You can verify that your Aurora PostgreSQL version supports export to Amazon S3 by using the
`describe-db-engine-versions` command. The following example checks to see
if version 10.14 can export to Amazon S3.

```
aws rds describe-db-engine-versions --region us-east-1 \
--engine aurora-postgresql --engine-version 10.14 | grep s3Export
```

If the output includes the string `"s3Export"`, then the engine supports Amazon S3 exports. Otherwise,
the engine doesn't support them.

## Overview of exporting data to Amazon S3

To export data stored in an Aurora PostgreSQL database to an Amazon S3 bucket, use the
following procedure.

###### To export Aurora PostgreSQL data to S3

1. Identify an Amazon S3 file path to use for exporting data. For details about this
   process, see [Specifying the Amazon S3 file path to export to](#postgresql-s3-export-file "#postgresql-s3-export-file").
2. Provide permission to access the Amazon S3 bucket.

To export data to an Amazon S3 file, give the Aurora PostgreSQL DB cluster permission to access the Amazon S3 bucket that
the export will use for storage. Doing this includes the following steps:

    1. Create an IAM policy that provides access to an Amazon S3 bucket that you
     want to export to.
    2. Create an IAM role.
    3. Attach the policy you created to the role you created.
    4. Add this IAM role to your
     DB cluster
     .

For details about this process, see [Setting up access to an Amazon S3 bucket](postgresql-s3-export-access-bucket.md "postgresql-s3-export-access-bucket.md"). 3. Identify a database query to get the data. Export the query data by calling
the `aws_s3.query_export_to_s3` function.

After you complete the preceding preparation tasks, use the [aws_s3.query_export_to_s3](postgresql-s3-export-functions.md#aws_s3.export_query_to_s3 "postgresql-s3-export-functions.md#aws_s3.export_query_to_s3") function to export query
results to Amazon S3. For details about this process, see [Exporting query data using the aws_s3.query_export_to_s3 function](postgresql-s3-export-examples.md "postgresql-s3-export-examples.md").

## Specifying the Amazon S3 file path to export to

Specify the following information to identify the location in Amazon S3 where you want to
export data to:

- Bucket name – A _bucket_ is a
  container for Amazon S3 objects or files.

For more information on storing data with Amazon S3, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") and [Working with objects](../../../AmazonS3/latest/userguide/uploading-downloading-objects.md "../../../AmazonS3/latest/userguide/uploading-downloading-objects.md") in the
_Amazon Simple Storage Service User Guide_.

- File path – The file path identifies where the export is stored in the
  Amazon S3 bucket. The file path consists of the following:

      + An optional path prefix that identifies a virtual folder path.
      + A file prefix that identifies one or more files to be stored. Larger
       exports are stored in multiple files, each with a maximum size of
       approximately 6 GB. The additional file names have the same file prefix
       but with `_part`XX`` appended. The
       ``XX`` represents 2, then 3,
       and so on.

  For example, a file path with an `exports` folder and a
  `query-1-export` file prefix is
  `/exports/query-1-export`.

- AWS Region (optional) – The AWS Region where the Amazon S3 bucket is
  located. If you don't specify an AWS Region value, then Aurora saves your files into Amazon S3 in the same AWS Region as the
  exporting DB cluster.

###### Note

Currently, the AWS Region must be the same as the region of the exporting
DB cluster.

For a listing of AWS Region names and associated values, see [Regions and Availability Zones](Concepts.md "Concepts.md").

To hold the Amazon S3 file information about where the export is to be stored, you can use
the [aws_commons.create_s3_uri](postgresql-s3-export-functions.md#aws_commons.create_s3_uri "postgresql-s3-export-functions.md#aws_commons.create_s3_uri") function to create an
`aws_commons._s3_uri_1` composite structure as follows.

```
psql=> SELECT aws_commons.create_s3_uri(
   '`amzn-s3-demo-bucket`',
   'sample-filepath',
   'us-west-2'
) AS s3_uri_1 \gset
```

You later provide this `s3_uri_1` value as a parameter in the call to the
[aws_s3.query_export_to_s3](postgresql-s3-export-functions.md#aws_s3.export_query_to_s3 "postgresql-s3-export-functions.md#aws_s3.export_query_to_s3") function. For examples, see [Exporting query data using the aws_s3.query_export_to_s3 function](postgresql-s3-export-examples.md "postgresql-s3-export-examples.md").
