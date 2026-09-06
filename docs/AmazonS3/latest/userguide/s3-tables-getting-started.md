

# Tutorial: Getting started with S3 Tables
<a name="s3-tables-getting-started"></a>

In this tutorial, you create a table bucket and integrate table buckets in your Region with AWS analytics services. Next, you will use the AWS CLI or console to create your first namespace and table in your table bucket. Then, you can begin querying your table with Athena.

**Tip**  
If you're migrating tabular data from general purpose buckets to table buckets, the AWS Solutions Library has a guided solution to assist you. This solution automates moving Apache Iceberg and Apache Hive tables that are registered in AWS Glue Data Catalog and stored in general purpose buckets to table buckets by using AWS Step Functions and Amazon EMR with Apache Spark. For more information, see [Guidance for Migrating Tabular Data from Amazon S3 to S3 Tables](https://aws.amazon.com/solutions/guidance/migrating-tabular-data-from-amazon-s3-to-s3-tables/) in the AWS Solutions Library.

**Topics**
+ [Step 1: Create a table bucket and integrate it with AWS analytics services](#s1-tables-tutorial-create-bucket)
+ [Step 2: Create a table namespace and a table](#s2-tables-tutorial-create-namespace-and-table)
+ [Step 3: Query data with SQL in Athena](#s4-query-tables)

## Step 1: Create a table bucket and integrate it with AWS analytics services
<a name="s1-tables-tutorial-create-bucket"></a>

In this step, you use the Amazon S3 console to create your first table bucket. For other ways to create a table bucket, see [Creating a table bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-create.html).

**Note**  
By default, the Amazon S3 console automatically integrates your table buckets with AWS Glue Data Catalog, which allows AWS analytics services to automatically discover and access your S3 Tables data. If you create your first table bucket programmatically by using the AWS Command Line Interface (AWS CLI), AWS SDKs, or REST API, you must manually complete the AWS analytics services integration. For more information, see [Integrating Amazon S3 Tables with AWS analytics services](s3-tables-integrating-aws.md).

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation bar, choose the name of the currently displayed AWS Region. Next, choose the Region in which you want to create the table bucket.

1. In the left navigation pane, choose **Table buckets**.

1. Choose **Create table bucket**.

1. Under **General configuration**, enter a name for your table bucket.

   The table bucket name must: 
   + Be unique within for your AWS account in the current Region.
   + Be between 3 and 63 characters long.
   + Consist only of lowercase letters, numbers, and hyphens (`-`).
   + Begin and end with a letter or number.

   After you create the table bucket, you can't change its name. The AWS account that creates the table bucket owns it. For more information about naming table buckets, see [Table bucket naming rules](s3-tables-buckets-naming.md#table-buckets-naming-rules).

1. In the **Integration with AWS analytics services** section, make sure that the **Enable integration** checkbox is selected. 

   If **Enable integration** is selected when you create your first table bucket by using the console, Amazon S3 attempts to integrate your table bucket with AWS analytics services. This integration allows you to use AWS analytics services to access all tables in the current Region. For more information, see [Integrating Amazon S3 Tables with AWS analytics services](s3-tables-integrating-aws.md).

1. Choose **Create bucket**.

## Step 2: Create a table namespace and a table
<a name="s2-tables-tutorial-create-namespace-and-table"></a>

For this step, you create a namespace in your table bucket, and then create a new table under that namespace. You can create a table namespace and a table by using either the console or the AWS CLI. 

**Important**  
When creating tables, make sure that you use all lowercase letters in your table names and table definitions. For example, make sure that your column names are all lowercase. If your table name or table definition contains capital letters, the table isn't supported by AWS Lake Formation or the AWS Glue Data Catalog. In this case, your table won't be visible to AWS analytics services such as Amazon Athena, even if your table buckets are integrated with AWS analytics services.   
If your table definition contains capital letters, you receive the following error message when running a `SELECT` query in Athena: "GENERIC\_INTERNAL\_ERROR: Get table request failed: com.amazonaws.services.glue.model.ValidationException: Unsupported Federation Resource - Invalid table or column names."

### Using the S3 console and Amazon Athena
<a name="s3-tables-tutorial-create-table-console"></a>

The following procedure uses the Amazon S3 console to create a namespace and a table with Amazon Athena. 

**To create a table namespace and a table**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Table buckets**.

1. On the **Table buckets** page, choose the table bucket that you want to create a table in.

1. On the table bucket details page, choose **Create table with Athena**. 

1. In the **Create table with Athena** dialog box, choose **Create a namespace**, and then enter a name in the **Namespace name** field. Namespace names must be 1 to 255 characters and unique within the table bucket. Valid characters are a–z, 0–9, and underscores (`_`). Underscores aren't allowed at the start of namespace names.

1. Choose **Create namespace**.

1. Choose **Create table with Athena**.

1. The Amazon Athena console opens and the Athena query editor appears. The query editor is populated with a sample query that you can use to create a table. Modify the query to specify the table name and columns that you want your table to have. 

1. When you're finished modifying the query, choose **Run** to create your table. 

If your table creation was successful, the name of your new table appears in the list of tables in Athena. When you navigate back to the Amazon S3 console, your new table appears in the **Tables** list on the details page for your table bucket after you refresh the list. 

### Using the AWS CLI
<a name="s3-tables-tutorial-create-table-CLI"></a>

To use the following AWS CLI example commands to create a namespace in your table bucket, and then create a new table with a schema under that namespace, replace the `{{user input placeholder}}` values with your own.

**Prerequisites**
+ Attach the [`AmazonS3TablesFullAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonS3TablesFullAccess.html) policy to your IAM identity. 
+ Install AWS CLI version 2.23.10 or higher. For more information, see [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

1. Create a new namespace in your table bucket by running the following command:

   ```
   aws s3tables create-namespace \
   --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}} \
   --namespace {{my_namespace}}
   ```

   1. Confirm that your namespace was created successfully by running the following command: 

     ```
     aws s3tables list-namespaces \
     --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}
     ```

1. Create a new table with a table schema by running the following command:

   ```
   aws s3tables create-table --cli-input-json file://{{mytabledefinition.json}}
   ```

   For the `mytabledefinition.json` file, use the following example table definition:

   ```
   {
       "tableBucketARN": "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/{{amzn-s3-demo-table-bucket}}",
       "namespace": "{{my_namespace}}",
       "name": "{{my_table}}",
       "format": "ICEBERG",
       "metadata": {
           "iceberg": {
               "schema": {
                   "fields": [
                        {{{"name": "id", "type": "int","required": true},
                        {"name": "name", "type": "string"},
                        {"name": "value", "type": "int"}}}
                   ]
               }
           }
       }
   }
   ```

## Step 3: Query data with SQL in Athena
<a name="s4-query-tables"></a>

You can query your table with SQL in Athena. Athena supports Data Definition Language (DDL), Data Manipulation Language (DML), and Data Query Language (DQL) queries for S3 Tables.

You can access the Athena query either from the Amazon S3 console or through the Amazon Athena console. 

### Using the S3 console and Amazon Athena
<a name="s4-query-tables-query-table-s3-console"></a>

The following procedure uses the Amazon S3 console to access the Athena query editor so that you can query a table with Amazon Athena. 

**To query a table**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Table buckets**.

1. On the **Table buckets** page, choose the table bucket that contains the table that you want to query.

1. On the table bucket details page, choose the option button next to the name of the table that you want to query. 

1. Choose **Query table with Athena**.

1. The Amazon Athena console opens and the Athena query editor appears with a sample `SELECT` query loaded for you. Modify this query as needed for your use case. 

1. To run the query, choose **Run**.

### Using the Amazon Athena console
<a name="s4-query-tables-query-table-athena-console"></a>

**To query a table**

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. Query your table. The following is a sample query that you can modify. Make sure to replace the `{{user input placeholders}}` with your own information.

   ```
   SELECT * FROM "s3tablescatalog/{{amzn-s3-demo-table-bucket}}"."{{my_namespace}}"."{{my_table}}" LIMIT 10
   ```

1. To run the query, choose **Run**. 