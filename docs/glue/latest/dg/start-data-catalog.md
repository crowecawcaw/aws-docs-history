

# Getting started with the AWS Glue Data Catalog
<a name="start-data-catalog"></a>

 The AWS Glue Data Catalog is your persistent technical metadata store. It is a managed service that you can use to store, annotate, and share metadata in the AWS Cloud. For more information, see [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro). 


|  | 
| --- |
| The AWS Glue console and some user interfaces were recently updated. | 

## Overview
<a name="start-data-catalog-overview"></a>

 You can use this tutorial to create your first AWS Glue Data Catalog, which uses an Amazon S3 bucket as your data source. 

 In this tutorial, you'll do the following using the AWS Glue console: 

1.  Create a database 

1.  Create a table 

1.  Use an Amazon S3 bucket as a data source 

 After completing these steps, you will have successfully used an Amazon S3 bucket as the data source to populate the AWS Glue Data Catalog. 

## Step 1: Create a database
<a name="start-data-catalog-database"></a>

 To get started, sign in to the AWS Management Console and open the [AWS Glue console](https://console.aws.amazon.com/glue). 

 ** To create a database using the AWS Glue console: ** 

1.  In the AWS Glue console, choose **Databases** under ** Data catalog** from the left-hand menu. 

1.  Choose **Add database**. 

1.  In the Create a database page, enter a name for the database. In the **Location - *optional*** section, set the URI location for use by clients of the Data Catalog. If you don't know this, you can continue with creating the database. 

1.  (Optional). Enter a description for the database. 

1.  Choose **Create database**. 

 Congratulations, you've just set up your first database using the AWS Glue console. Your new database will appear in the list of available databases. You can edit the database by choosing the database's name from the ** Databases** dashboard. 

 **Next steps** 

 ** Other ways to create a database: ** 

 You just created a database using the AWS Glue console, but there are other ways to create a database: 
+ You can use crawlers to create a database and tables for you automatically. To set up a database using crawlers, see [Working with Crawlers in the AWS Glue Console](https://docs.aws.amazon.com/glue/latest/dg/console-crawlers.html). 
+  You can use CloudFormation templates. See [Creating AWS Glue Resources Using AWS Glue Data Catalog Templates](https://docs.aws.amazon.com/glue/latest/dg/populate-with-cloudformation-templates.html). 
+  You can also create a database using the AWS Glue Database API operations. 

   To create a database using the `create` operation, structure the request by including the `DatabaseInput` (required) parameters. 

   For example:   
****  
 The following are examples of how you can use the CLI, Boto3, or DDL to define a table based on the same flights\_data.csv file from the S3 bucket that you used in the tutorial.   

  ```
  aws glue create-database --database-input "{\"Name\":\"clidb\"}"                                              
  ```

  ```
  glueClient = boto3.client('glue')
  
  response = glueClient.create_database(
      DatabaseInput={
          'Name': 'boto3db'
      }
  )
  ```

 For more information about the Database API data types, structure, and operations, see [Database API](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-databases.html). 

 **Next Steps** 

 In the next section, you'll create a table and add that table to your database. 

You can also explore the settings and permissions for your Data Catalog. See [Working with Data Catalog Settings in the AWS Glue Console](https://docs.aws.amazon.com/glue/latest/dg/console-data-catalog-settings.html). 

## Step 2. Create a table
<a name="start-data-catalog-table"></a>

 In this step, you create a table using the AWS Glue console. 

1.  In the AWS Glue console, choose **Tables** in the left-hand menu. 

1.  Choose **Add table**. 

1.  Set your table's properties by entering a name for your table in **Table details**. 

1.  In the **Databases** section, choose the database that you created in Step 1 from the drop-down menu. 

1.  In **Add a data store** section, **S3** will be selected by default as the type of source. 

1.  For **Data is located in **, choose **Specified path in another account**. 

1. Copy and paste the path for the **Include path** input field:

   `s3://crawler-public-us-west-2/flight/2016/csv/`

1.  In the section **Data format**, for **Classification**, choose **CSV**. and for **Delimiter**, choose **comma (,)**. Choose **Next**. 

1. You are asked to define a schema. A schema defines the structure and format of a data record. Choose **Add column**. (For more information, see See [Schema registries](https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html#schema-registry-schemas.html)).

1.  Specify the column properties: 

   1. Enter a column name. 

   1. For **Column type**, 'string' is already selected by default.

   1. For **Column number**, '1' is already selected by default.

   1. Choose **Add**.

1.  You are asked to add partition indexes. This is optional. To skip this step, choose **Next**. 

1.  A summary of the table properties is displayed. If everything looks as expected, choose **Create**. Otherwise, choose **Back** and make edits as needed. 

 Congratulations, you've successfully created a table manually and associated it to a database. Your newly created table will appear in the Tables dashboard. From the dashboard, you can modify and manage all your tables. 

 For more information, see [Working with Tables in the AWS Glue Console](https://docs.aws.amazon.com/glue/latest/dg/console-tables.html). 

## Next steps
<a name="start-data-catalog-next-steps"></a>

 **Next steps** 

 Now that the Data Catalog is populated, you can begin authoring jobs in AWS Glue. See [ Building visual ETL jobs with AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/author-job-glue.html). 

 In addition to using the console, there are other ways to define tables in the Data Catalog including:
+  [Creating and running a crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) 
+  [Adding classifiers to a crawler in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/add-classifier.html) 
+  [Using the AWS Glue Table API](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html) 
+  [ Using the AWS Glue Data Catalog template](https://docs.aws.amazon.com/glue/latest/dg/populate-with-cloudformation-templates.html) 
+  [ Migrating an Apache Hive metastore](https://github.com/aws-samples/aws-glue-samples/tree/master/utilities/Hive_metastore_migration) 
+  [Using the AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/glue/create-table.html), Boto3, or data definition language (DDL)   
****  
 The following are examples of how you can use the CLI, Boto3, or DDL to define a table based on the same flights\_data.csv file from the S3 bucket that you used in the tutorial.   
 See the documentation on how to structure an AWS CLI command. The CLI example contains the JSON syntax for the 'aws glue create-table --table-input' value.   

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