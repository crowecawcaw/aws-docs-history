# Creating an Amazon S3 table

An Amazon S3 table is a subresource of a table bucket. Tables are stored in the Apache
 Iceberg format so that you can work with them by using query engines and other applications that
 support Apache Iceberg. Amazon S3 continuously optimizes your tables to help reduce storage
 costs and improve analytics query performance.

When you create a table, Amazon S3 automatically generates a *warehouse
 location* for the table. A warehouse location is a unique S3 location where you can read and
 write objects associated with the table. The following example shows the format of a warehouse
 location:


```
s3://63a8e430-6e0b-46f5-k833abtwr6s8tmtsycedn8s4yc3xhuse1b--table-s3
```
Tables have the following Amazon Resource Name (ARN) format:


```
arn:aws:s3tables:`region`:`owner-account-id`:bucket/`bucket-name`/table/`table-id`
```
By default, you can create up to 10,000 tables in a table bucket. To request a quota
 increase for table buckets or tables, contact [Support](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

You can create a table by using the Amazon S3 console, Amazon S3 REST API, AWS SDKs, AWS Command Line Interface (AWS CLI), or
 query engines connected to your table buckets.

When you create a table you can specify the encryption settings for that table, unless you
 are creating the table with Athena. If you don't specify encryption settings the table is
 encrypted with the default settings for the table bucket. For more information, see [Specifying encryption for tables](s3-tables-kms-specify.md#specify-kms-table "s3-tables-kms-specify.md#specify-kms-table").


###### Prerequisites for creating tables


To create a table, you must first do the following: 
 


* [Create a table bucket](s3-tables-buckets-create.md "s3-tables-buckets-create.md").
* [Create a namespace](s3-tables-namespace-create.md "s3-tables-namespace-create.md") in your table bucket.
* Make sure that you have AWS Identity and Access Management (IAM) permissions for `s3tables:CreateTable` and
 `s3tables:PutTableData`.
* ###### Note

If you are using SSE-KMS encryption for your table, you need permissions for
 `s3tables:PutTableEncryption`, and `DescribeKey` permission on the chosen AWS KMS key. Additionally the AWS KMS key you use needs to
 grant S3 Tables permission to perform automatic table maintenance. For more information,
 see [Permission requirements for S3 Tables SSE-KMS encryption](s3-tables-kms-permissions.md "s3-tables-kms-permissions.md")
For information about valid table names, see [Naming rules for tables and namespaces](s3-tables-buckets-naming.md#naming-rules-table "s3-tables-buckets-naming.md#naming-rules-table").

###### Important

When creating tables, make sure that you use all lowercase letters in your table names and table
 definitions. For example, make sure that your column names are all lowercase. If your table name or
 table definition contains capital letters, the table isn't supported by AWS Lake Formation or the AWS Glue Data Catalog. In
 this case, your table won't be visible to AWS analytics services such as Amazon Athena, even if your table
 buckets are integrated with AWS analytics services. 

If your table definition contains capital letters, you receive the following error message when
 running a `SELECT` query in Athena: **`"GENERIC_INTERNAL_ERROR: Get table request
 failed: com.amazonaws.services.glue.model.ValidationException: Unsupported Federation Resource -
 Invalid table or column names."`**

The following procedure uses the Amazon S3 console to create a table with Amazon Athena. If you haven't
 already created a namespace in your table bucket, you can do so as part of this process. Before performing the following steps, make sure that you've integrated your table buckets with
 AWS analytics services in this Region. For more information, see [Integrating Amazon S3 Tables with AWS analytics
 services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").

###### Note

When you create a table using Athena that table inherits the default encryption settings from the table bucket. If you want to use a different encryption type you need to create the table using another method.

###### To create a table

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. On the **Table buckets** page, choose the bucket that you want to create a
 table in.
4. On the bucket details page, choose **Create table with Athena**.
5. In the **Create table with Athena** dialog box, do one of the
 following:


	* Create a new namespace. Choose **Create a namespace**, and then enter a
	 name in the **Namespace name** field. Namespace names must be 1 to 255
	 characters and unique within the table bucket. Valid characters are a–z, 0–9,
	 and underscores (`_`). Underscores aren't allowed at the start of namespace names.
	* Choose **Create namespace**.
	* Specify an existing namespace. Choose **Specify an existing namespace within this
	 table bucket**. Then choose either **Choose from existing
	 namespaces** or **Enter an existing namespace name**. If you have
	 more than 1,000 namespaces in your bucket, you must enter the namespace name if it doesn't
	 appear in the list.
6. Choose **Create table with Athena**.
7. The Amazon Athena console opens and the Athena query editor appears. The
 **Catalog** field should be populated with
 **s3tablescatalog/** followed by the name of your table bucket, for example,
 **s3tablescatalog/`amzn-s3-demo-bucket`**. The **Database**
 field should be populated with the namespace that you created or selected earlier. 


###### Note

If you don't see these values in the **Catalog** and
 **Database** fields, make sure that you've integrated your table buckets with
 AWS analytics services in this Region. For more information, see [Integrating Amazon S3 Tables with AWS analytics
 services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").
8. The query editor is populated with a sample query that you can use to create a table. Modify
 the query to specify the table name and columns that you want your table to have.
9. When you're finished modifying the query, choose **Run** to create your
 table. 


###### Note



	* If you receive the error **`"Insufficient permissions to execute the query.
	 Principal does not have any privilege on specified resource"`** when you try to
	 run a query in Athena, you must be granted the necessary Lake Formation permissions on the table. For
	 more information, see [Granting Lake Formation permission on a table or database](grant-permissions-tables.md#grant-lf-table "grant-permissions-tables.md#grant-lf-table").
	* If you receive the error **`"Iceberg cannot access the requested resource"`**
	 when you try to run a query in Athena, go to the AWS Lake Formation console and make sure that you've granted
	 yourself permissions on the table bucket catalog and database (namespace) that you created. Don't
	 specify a table when granting these permissions. For more information, see [Granting Lake Formation permission on a table or database](grant-permissions-tables.md#grant-lf-table "grant-permissions-tables.md#grant-lf-table").
	* If you receive the following error message when running a `SELECT` query in
	 Athena, this message is caused by having capital letters in your table name or your column
	 names in your table definition: **`"GENERIC_INTERNAL_ERROR: Get table request
	 failed: com.amazonaws.services.glue.model.ValidationException: Unsupported Federation
	 Resource - Invalid table or column names."`** Make sure that your table and
	 column names are all lowercase.
If your table creation was successful, the name of your new table appears in the list of tables
 in Athena. When you navigate back to the Amazon S3 console, your new table appears in the
 **Tables** list on the bucket details page for your table bucket after you refresh
 the list. 

This example shows how to create a table with a schema by using the AWS CLI and specifying
 table metadata with JSON. To use this example, replace the ``user
 input placeholders`` with your own information.


```
aws s3tables create-table --cli-input-json file://`mytabledefinition.json`
```
For the `mytabledefinition.json` file, use the following example table
 definition. To use this example, replace the ``user input
 placeholders`` with your own information. 


```
{
    "tableBucketARN": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`",
    "namespace": "`your_namespace`",
    "name": "`example_table`",
    "format": "ICEBERG",
    "metadata": {
        "iceberg": {
            "schema": {
                "fields": [
                     {"name": "`id`", "type": "`int`",`"required": true`},
                     {"name": "`name`", "type": "`string`"},
                     {"name": "`value`", "type": "`int`"}
                ]
            }
        }
    }
}
```
You can create a table in a supported query engine that's connected to your table buckets,
 such as in an Apache Spark session on Amazon EMR.

The following example shows how to create a table with Spark by using
 `CREATE` statements, and add table data by using `INSERT` statements or by
 reading data from an existing file. To use this example, replace the ``user input
 placeholders`` with your own information.


```
spark.sql( 
" CREATE TABLE IF NOT EXISTS s3tablesbucket.`example_namespace`.``example_table`` ( 
    id INT, 
    name STRING, 
    value INT 
) 
USING iceberg "
)
```
After you create the table, you can load data into the table. Choose from the following
 methods:


* Add data into the table by using the `INSERT` statement.



```
spark.sql(
"""
    INSERT INTO s3tablesbucket.`my_namespace`.`my_table` 
    VALUES 
        (1, 'ABC', 100), 
        (2, 'XYZ', 200)
""")
```
* Load an existing data file.




	1. Read the data into Spark:
	
	
	
	```
	val data_file_location = "`Path such as S3 URI to data file`"
	val data_file = spark.read.parquet(`data_file_location`)
	```
	2. Write the data into an Iceberg table:
	
	
	
	```
	data_file.writeTo("s3tablesbucket.`my_namespace`.`my_table`").using("Iceberg").tableProperty ("format-version", "2").createOrReplace()
	```
