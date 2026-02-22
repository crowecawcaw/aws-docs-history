# Installing the aws_s3 extension

Before you can use Amazon S3 with your Aurora PostgreSQL DB cluster,
you need to install the
`aws_s3` extension. This extension provides functions for importing data from an Amazon S3. It also provides
functions for exporting data from an instance of an
Aurora PostgreSQL DB cluster
to an Amazon S3 bucket. For more information, see
[Exporting data from an Aurora PostgreSQL DB cluster to Amazon S3](postgresql-s3-export.md "postgresql-s3-export.md").

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
