Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Adding data lake tables to a

datashare

With a datashare, a data _producer_ can securely share database
objects of fine granularity, such as schemas and tables, with
_consumers_ in the same AWS account or in different accounts.
The producer can also share objects across regions. This topic describes how to add
objects from a data lake, specifically, from the AWS Glue data catalog, to a datashare.
It covers two use cases:

- _Adding a late-binding view to a datashare that references a table
  from a data lake_ – This is convenient for a consumer,
  because preliminary configuration, such as defining permissions on the external
  source data, for example with Lake Formation, is likely already completed. An additional
  benefit is that a view added to a datashare can join tables from the data lake
  with Redshift native tables.
- _Adding a table from an external schema to a datashare
  directly_ – This makes objects from the data lake available
  to consumers with no additional layers or logic. Consumers can query the table
  or join it with tables on the consumer.
  These cases apply after you reference a table from the AWS data catalog in
  Redshift using [CREATE
  EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md "r_CREATE_EXTERNAL_SCHEMA.md"). Any table from the AWS data catalog can be the
  source.

###### Note

Data lake tables that you add to a datashare can include tables registered with
Lake Formation and AWS Glue data catalog tables.

## Create an external

schema and an external table

You create an external schema and an external table in order to add them to the
datashare in the sections that follow. These are preliminary steps. If you have
already done this, you can skip this section.

1. On the producer, create an external schema that references the data lake
   data stored in Amazon S3. The external schema references the AWS Glue Data
   Catalog. The role and region in the sample are examples:

```
CREATE EXTERNAL SCHEMA external_schema_name FROM DATA CATALOG
DATABASE 'glue_database_name'
IAM_ROLE 'arn:aws:iam::123456789012:role/sample-role'
REGION 'us-east-1';
```

2. Create a data lake table in the external schema.

```
CREATE EXTERNAL TABLE external_schema_name.sales(
salesid INTEGER,
sellerid INTEGER,
buyerid INTEGER,
saledate DATE,
pricepaid DECIMAL(8,2))
ROW FORMAT delimited
FIELDS TERMINATED BY '\t'
STORED AS textfile
LOCATION 's3://redshift-downloads/tickit/spectrum/sales/';
```

The sample includes the `LOCATION`. It must be in the form
`s3://{bucket_name}/{folder}/`, where the folder is specified.
The folder must have a length of at least one character. You can optionally
include subfolders. To see additional examples for creating tables in a data
lake, see [Examples](r_CREATE_EXTERNAL_TABLE_examples.md "r_CREATE_EXTERNAL_TABLE_examples.md") for CREATE EXTERNAL TABLE.

###### Note

Sharing is supported only for tables where the IAM role on the
producer has SELECT access on the table.

## Add a

late-binding view that references a data lake table to a datashare

When you create tables based on an external schema from the AWS data catalog,
and you want to add them to a datashare, the most common way to do it is to add a
Redshift late-binding view that references the table you created, which contains
data from the data lake. The following procedure shows the steps:

1. Create a late-binding view that references the external table you created
   previously:

```
CREATE VIEW lbv AS
select * from external_schema_name.sales, other_schema.t1
WITH NO SCHEMA BINDING;
```

2. Add the view schema to the datashare. This is the local schema that
   contains the late-binding view.

```
ALTER DATASHARE dsx_datashare ADD SCHEMA public;
```

3. Add the schema that contains the table referenced by the late-binding
   view to the datashare. Adding the schema is required for any base tables
   referenced in a view that's added to a datashare, whether the schema
   contains local database objects or objects from a data lake. Note that you
   must add this schema before you add the late-binding view.

```
ALTER DATASHARE dsx_datashare ADD SCHEMA external_schema_name;
ALTER DATASHARE dsx_datashare ADD SCHEMA other_schema;
```

4. Add the view to the datashare, using a SQL command. Note that the table
   name includes the schema prefix.

```
ALTER DATASHARE my_datashare ADD TABLE public.lbv;
```

5. Confirm that the view and schemas are successfully added to the
   datashare:

```
SELECT * FROM svv_datashare_objects WHERE share_name = 'my_datashare';
```

6. The consumer administrator creates a database from the datashare and then
   grants usage to consumer users.

After you complete the steps, database consumer users with access to the
datashare view can query the data.

## Add a data

lake table directly to a datashare

Adding a table in an external schema to a datashare is similar to adding a
view. This works well for a case where a consumer wants to query the data lake
table in its original state, or if a consumer wants to join it to tables in the
consumer data warehouse. The steps that follow show you how to add a data lake
table to a datashare, using SQL.

1. Create an external schema and an external table, as described in the
   first section of this topic.
2. Discover existing tables in the external schema, to confirm that the
   table you created is available:

```
SELECT * FROM svv_external_tables WHERE schemaname = 'external_schema_name';
```

3. Add the external schema to the datashare:

```
ALTER DATASHARE my_datashare ADD SCHEMA external_schema_name;
```

4. Add the external table to the datashare. Note that the table name
   includes the schema prefix:

```
ALTER DATASHARE my_datashare ADD TABLE external_schema_name.sales;
```

5. Confirm that the table is successfully added to the datashare:

```
SELECT * FROM svv_datashare_objects WHERE share_name = 'my_datashare';
```

For more detailed instruction, see [Sharing read access to data within
an AWS account](within-account.md "within-account.md"). 6. On the consumer, which is the database receiving the shared data, the
administrator associates the datashare to make shared tables available for
users to query. For more information regarding how to perform this step, see
[Managing datashares from
other accounts as a consumer](manage-datashare-other-console.md "manage-datashare-other-console.md").

After administrators complete the steps, database users on the consumer can
write queries to retrieve data from the shared table and join it with other tables
on the consumer.

## Usage

notes for adding data lake objects to a datashare

There are several items to note when you use tables and views from a data lake
in a datashare:

- **Logging with AWS CloudTrail**
  – The data producer account can use AWS CloudTrail logs to
  audit when data lake tables shared through a datashare are accessed:
  - **Using log data to control data
    access** – The CloudTrail logs record details about who
    accesses shared tables, including both Redshift datashare producers
    and consumers. The identifiers are available in the
    `ExternalId` field under the `AssumeRole`
    CloudTrail logs. The data owner can configure additional limitations on data
    access in an IAM policy by means of actions. For more information
    about defining data access through policies, see [Access to AWS accounts owned by third parties](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md").

- **Security and consumer permissions**
  – For Lake Formation registered tables, Amazon S3 resources are secured by Lake Formation and
  made available using the credentials provided by Lake Formation.

## Billing

considerations for adding data lake objects to a datashare

The following details how costs are attributed for storing and scanning data
lake objects in a datashare:

- When a consumer queries shared objects from a data lake, the cost of
  scanning is billed to the consumer.
  - When the consumer is a provisioned cluster, Redshift uses
    Redshift Spectrum to scan Amazon S3 data. Therefore, the Spectrum cost is
    billed to the consumer account.
  - When the consumer is an Amazon Redshift Serverless workgroup, there is no
    separate charge for Spectrum.

- Amazon S3 costs for storage and operations, such as listing buckets, is billed
  to the account that owns each Amazon S3 bucket.

For additional details regarding billing for Amazon Redshift Serverless, see [Billing for
Amazon Redshift Serverless](../mgmt/serverless-billing.md "../mgmt/serverless-billing.md"). More billing and pricing information is available at
[Amazon Redshift
pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").
