

# Setting up Amazon Redshift Spectrum

With Amazon Redshift Spectrum, you can query data registered in the AWS Glue Data Catalog from Amazon Redshift, and join it with the data in your warehouse. Redshift Spectrum reads the HealthLake tables in place through the resource link that HealthLake shares into your account. Lake Formation gives Redshift Spectrum temporary credentials for the tables that you grant to the IAM role associated with your Amazon Redshift Serverless workgroup.

Before you begin, grant access to the IAM role associated with your Amazon Redshift Serverless workgroup by following Step 2 in [Getting started with HealthLake analytics](integrating-analytics-getting-started.md).

## Prerequisites
<a name="integrating-redshift-spectrum-prerequisites"></a>

Before you query HealthLake data with Redshift Spectrum, make sure that you have the following:
+ An Amazon Redshift Serverless workgroup, in the same AWS account and Region as your HealthLake data store.
+ An IAM role associated with the workgroup. This is the principal that you grant access to in Lake Formation.
+ The resource link name for your data store, which ends in `_healthlake_view`. To find it, see [Step 1: Find the resource links](integrating-analytics-getting-started.md#integrating-analytics-granting-find).

This topic covers Redshift Spectrum queries from Amazon Redshift Serverless.

The IAM role needs read access to the table metadata in the AWS Glue Data Catalog and permission to request credentials from Lake Formation. Attach the following permissions policy to the role.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadCatalog",
      "Effect": "Allow",
      "Action": [
        "glue:GetDatabase",
        "glue:GetDatabases",
        "glue:GetTable",
        "glue:GetTables",
        "glue:GetPartitions"
      ],
      "Resource": [
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}:catalog",
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}:database/{{resource-link-name}}",
        "arn:aws:glue:{{us-east-1}}:{{111122223333}}:table/{{resource-link-name}}/*",
        "arn:aws:glue:{{us-east-1}}:{{444455556666}}:catalog",
        "arn:aws:glue:{{us-east-1}}:{{444455556666}}:database/{{target-database-name}}",
        "arn:aws:glue:{{us-east-1}}:{{444455556666}}:table/{{target-database-name}}/*"
      ]
    },
    {
      "Sid": "RequestLakeFormationCredentials",
      "Effect": "Allow",
      "Action": "lakeformation:GetDataAccess",
      "Resource": "*"
    }
  ]
}
```

Replace {{resource-link-name}} with your resource link name and {{target-database-name}} with its target database. You can find both in Step 1 of [Getting started with HealthLake analytics](integrating-analytics-getting-started.md). The role doesn't need Amazon S3 permissions for the HealthLake data, because Lake Formation issues the credentials.

In the commands in this topic, replace {{us-east-1}} with the AWS Region of your data store.

## Step 1: Create an external schema
<a name="integrating-redshift-spectrum-schema"></a>

Create an external schema in Amazon Redshift that points to the resource link database.

**To create an external schema for the resource link**
+ In the Amazon Redshift query editor, run the following statement.

  ```SQL
  CREATE EXTERNAL SCHEMA healthlake
  FROM DATA CATALOG
  DATABASE '{{resource-link-name}}'
  IAM_ROLE 'arn:aws:iam::{{111122223333}}:role/{{redshift-role-name}}'
  REGION '{{us-east-1}}';
  ```

Replace the following:
+ {{resource-link-name}} with the resource link to the HealthLake database in your account, which ends in `_healthlake_view`. To find it, see [Step 1: Find the resource links](integrating-analytics-getting-started.md#integrating-analytics-granting-find).
+ {{111122223333}} with your AWS account ID, where your workgroup runs.
+ {{redshift-role-name}} with the name of the IAM role associated with your workgroup, which you grant access to in Lake Formation.

**Result:** Amazon Redshift creates the `healthlake` external schema, which exposes the HealthLake tables for querying. You query it in Step 2.

## Step 2: Run a test query
<a name="integrating-redshift-spectrum-query"></a>

Run a row count on the `patient` table to confirm access.

**To run a test query**
+ In the query editor, run the following statement.

  ```SQL
  SELECT COUNT(*) FROM healthlake.patient;
  ```

**Result:** The query returns the number of rows in the `patient` table. The count includes every version of each resource, not the number of patients. For more information, see [Resource versions](integrating-analytics.md#integrating-analytics-tables-versions).

## SQL differences in Redshift Spectrum
<a name="integrating-redshift-spectrum-sql"></a>

Redshift Spectrum reads the HealthLake tables as nested data. Adjust queries as follows:
+ Nested fields need the table alias, for example `p.meta.lastupdated`. Without the alias, Amazon Redshift reads `meta` as a table name.
+ Arrays are 0-based, for example `p.name[0]`. You can use an array element only in the `SELECT` list. To filter on array elements, unnest the array in the `FROM` clause:

  ```SQL
  SELECT COUNT(*) FROM healthlake.patient p, p.name n WHERE n.family IS NOT NULL;
  ```
+ Array elements return the `SUPER` type. Cast them to `VARCHAR` before you use JSON functions:

  ```SQL
  SELECT COUNT(NULLIF(JSON_EXTRACT_PATH_TEXT(p.extension[0]::varchar(65535), 'url'), '')) FROM healthlake.patient p;
  ```
+ Struct fields keep their type, for example `p.maritalstatus.text` is a `VARCHAR`, and `CAST(birthdate AS DATE)` works as in other engines.

To count current resources, Redshift Spectrum can't run a window function in a subquery that reads a nested table. Copy the columns that you need into a temporary table first, and run both statements in the same session:

```SQL
CREATE TEMP TABLE versions AS
SELECT p.id, p.isdelete, p.meta.lastupdated AS last_updated
FROM healthlake.patient p;

SELECT COUNT(*) FROM (
  SELECT id, isdelete,
         ROW_NUMBER() OVER (PARTITION BY id ORDER BY last_updated DESC) AS row_num
  FROM versions
) AS latest
WHERE row_num = 1
  AND coalesce(isdelete, false) = false;
```

The query returns the number of current, non-deleted patients. To learn why you need this pattern, see [Resource versions](integrating-analytics.md#integrating-analytics-tables-versions).

## Querying the tables
<a name="integrating-redshift-spectrum-querying"></a>

For the table structure, nested data, resource versions, and data freshness, see [Understanding the analytics tables](integrating-analytics.md#integrating-analytics-tables).

For more information, see [CREATE EXTERNAL SCHEMA](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_SCHEMA.html) and [Redshift Spectrum and AWS Lake Formation](https://docs.aws.amazon.com/redshift/latest/dg/spectrum-lake-formation.html) in the *Amazon Redshift Database Developer Guide*.