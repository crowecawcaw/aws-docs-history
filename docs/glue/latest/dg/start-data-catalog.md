# Getting

started
with the AWS Glue Data Catalog

The AWS Glue Data Catalog is your persistent technical metadata store. It is a managed service that
you can use to store, annotate, and share metadata in the AWS Cloud. For more information,
see [AWS Glue Data Catalog](components-overview.md#data-catalog-intro "components-overview.md#data-catalog-intro").

|                                                                      |
| -------------------------------------------------------------------- |
| The AWS Glue console and some user interfaces were recently updated. |

## Overview

You can use this tutorial to create your first AWS Glue Data Catalog, which
uses an Amazon S3 bucket as your data source.

In this tutorial, you'll do the following using the AWS Glue console:

1. Create a database
2. Create a table
3. Use an Amazon S3 bucket as a data source

After completing these steps, you will have successfully used an Amazon S3 bucket as the data
source to populate the AWS Glue Data Catalog.

## Step 1: Create a

database

To get started, sign in to the AWS Management Console and open the
[AWS Glue console](https://console.aws.amazon.com/glue "https://console.aws.amazon.com/glue").

**To create a database using the AWS Glue console:**

1. In the AWS Glue console, choose **Databases** under **Data catalog** from the left-hand menu.
2. Choose **Add database**.
3. In the Create a database page, enter a name for the database.
   In the **Location - _optional_** section,
   set the URI location for use by clients of the Data Catalog. If you don't know this, you can
   continue with creating the database.
4. (Optional). Enter a description for the database.
5. Choose **Create database**.

Congratulations, you've just set up your first database using the
AWS Glue console. Your new database will appear in the list of available
databases. You can edit the database by choosing the database's name from the **Databases**
dashboard.

**Next steps**

**Other ways to create a database:**

You just created a database using the AWS Glue console, but there are other ways
to create a database:

- You can use crawlers to create a database and tables for you automatically. To
  set up a database using crawlers, see [Working with Crawlers in the
  AWS Glue Console](console-crawlers.md "console-crawlers.md").
- You can use AWS CloudFormation templates. See [Creating
  AWS Glue Resources Using AWS Glue Data Catalog Templates](populate-with-cloudformation-templates.md "populate-with-cloudformation-templates.md").
- You can also create a database using the AWS Glue Database API operations.

To create a database using the `create` operation, structure the
request by including the `DatabaseInput` (required) parameters.

For example:

The following are examples of how you can use the CLI, Boto3, or
DDL to define a table based on the same flights_data.csv file from
the S3 bucket that you used in the tutorial.

CLI

```
aws glue create-database --database-input "{\"Name\":\"clidb\"}"

```

Boto3

```
glueClient = boto3.client('glue')

response = glueClient.create_database(
    DatabaseInput={
        'Name': 'boto3db'
    }
)

```

For more information about the Database API data types, structure, and operations,
see [Database API](aws-glue-api-catalog-databases.md "aws-glue-api-catalog-databases.md").

**Next Steps**

In the next section, you'll create a table and add that table to your database.

You can also explore the settings and permissions for your Data Catalog. See [Working with Data Catalog
Settings in the AWS Glue Console](console-data-catalog-settings.md "console-data-catalog-settings.md").

## Step 2. Create a table

In this step, you create a table using the AWS Glue console.

1. In the AWS Glue console, choose **Tables** in the left-hand menu.
2. Choose **Add table**.
3. Set your table's properties by entering a name for your table in **Table details**.
4. In the **Databases** section, choose the database that you
   created in Step 1 from the drop-down menu.
5. In **Add a data store** section, **S3** will be selected
   by default as the type of source.
6. For **Data is located in** , choose
   **Specified path in another account**.
7. Copy and paste the path for the **Include path** input field:

`s3://crawler-public-us-west-2/flight/2016/csv/` 8. In the section **Data format**, for **Classification**,
choose **CSV**. and for **Delimiter**, choose
**comma (,)**. Choose **Next**. 9. You are asked to define a schema. A schema defines the structure and format of
a data record. Choose **Add column**. (For more information,
see See [Schema
registries](schema-registry.md#schema-registry-schemas.html "schema-registry.md#schema-registry-schemas.html")). 10. Specify the column properties:

    1. Enter a column name.
    2. For **Column type**, 'string' is already selected by
     default.
    3. For **Column number**, '1' is already selected by
     default.
    4. Choose **Add**.

11. You are asked to add partition
    indexes.
    This is optional. To skip this step, choose **Next**.
12. A summary of the table properties is displayed. If everything looks as
    expected, choose **Create**. Otherwise, choose
    **Back** and make edits as needed.

Congratulations, you've successfully created a table manually and associated it to a
database. Your newly created table will appear in the Tables dashboard. From the
dashboard, you can modify and manage all your tables.

For more information, see [Working with
Tables in the AWS Glue Console](console-tables.md "console-tables.md").

## Next steps

**Next steps**

Now that the Data Catalog is populated, you can begin authoring jobs in
AWS Glue. See [Building visual ETL jobs with AWS Glue Studio](author-job-glue.md "author-job-glue.md").

In addition to using the console, there are other ways to define tables in the Data
Catalog
including:

- [Creating and running a crawler](add-crawler.md "add-crawler.md")
- [Adding classifiers to a crawler in AWS Glue](add-classifier.md "add-classifier.md")
- [Using the
  AWS Glue Table API](aws-glue-api-catalog-tables.md "aws-glue-api-catalog-tables.md")
- [Using the
  AWS Glue Data Catalog template](populate-with-cloudformation-templates.md "populate-with-cloudformation-templates.md")
- [Migrating an Apache Hive metastore](https://github.com/aws-samples/aws-glue-samples/tree/master/utilities/Hive_metastore_migration "https://github.com/aws-samples/aws-glue-samples/tree/master/utilities/Hive_metastore_migration")
- [Using the AWS CLI](../../../cli/latest/reference/glue/create-table.md "../../../cli/latest/reference/glue/create-table.md"),
  Boto3, or data definition language (DDL)

The following are examples of how you can use the CLI, Boto3, or
DDL to define a table based on the same flights_data.csv file from
the S3 bucket that you used in the tutorial.

See the documentation on how to structure an AWS CLI command.
The CLI example contains the JSON syntax for the 'aws glue create-table --table-input' value.

CLI

```
{
        "Name": "flights_data_cli",
        "StorageDescriptor": {
            "Columns": [
                {
                    "Name": "year",
                    "Type": "bigint"
                },
                {
                    "Name": "quarter",
                    "Type": "bigint"
                }
            ],
            "Location": "s3://crawler-public-us-west-2/flight/2016/csv",
            "InputFormat": "org.apache.hadoop.mapred.TextInputFormat",
            "OutputFormat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
            "Compressed": false,
            "NumberOfBuckets": -1,
            "SerdeInfo": {
                "SerializationLibrary": "org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe",
                "Parameters": {
                    "field.delim": ",",
                    "serialization.format": ","
                }
            }
        },
        "PartitionKeys": [
            {
                "Name": "mon",
                "Type": "string"
            }
        ],
        "TableType": "EXTERNAL_TABLE",
        "Parameters": {
            "EXTERNAL": "TRUE",
            "classification": "csv",
            "columnsOrdered": "true",
            "compressionType": "none",
            "delimiter": ",",
            "skip.header.line.count": "1",
            "typeOfData": "file"
        }
    }

```

Boto3

```
import boto3

glue_client = boto3.client("glue")

response = glue_client.create_table(
    DatabaseName='sampledb',
    TableInput={
        'Name': 'flights_data_manual',
    'StorageDescriptor': {
      'Columns': [{
        'Name': 'year',
        'Type': 'bigint'
      }, {
        'Name': 'quarter',
        'Type': 'bigint'
      }],
      'Location': 's3://crawler-public-us-west-2/flight/2016/csv',
      'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
      'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
      'Compressed': False,
      'NumberOfBuckets': -1,
      'SerdeInfo': {
        'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
        'Parameters': {
          'field.delim': ',',
          'serialization.format': ','
        }
      },
    },
    'PartitionKeys': [{
      'Name': 'mon',
      'Type': 'string'
    }],
    'TableType': 'EXTERNAL_TABLE',
    'Parameters': {
      'EXTERNAL': 'TRUE',
      'classification': 'csv',
      'columnsOrdered': 'true',
      'compressionType': 'none',
      'delimiter': ',',
      'skip.header.line.count': '1',
      'typeOfData': 'file'
    }
    }
)

```

DDL

```
CREATE EXTERNAL TABLE `sampledb`.`flights_data` (
  `year` bigint,
  `quarter` bigint)
PARTITIONED BY (
  `mon` string)
ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://crawler-public-us-west-2/flight/2016/csv/'
TBLPROPERTIES (
  'classification'='csv',
  'columnsOrdered'='true',
  'compressionType'='none',
  'delimiter'=',',
  'skip.header.line.count'='1',
  'typeOfData'='file')

```
