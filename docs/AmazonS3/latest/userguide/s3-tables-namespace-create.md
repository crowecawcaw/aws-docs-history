# Creating a namespace

A table namespace is a logical construct that you group tables under within an Amazon S3 table
 bucket. Each table belongs to a single namespace. Before creating a table in a table bucket, you must
 create a namespace to group tables under. You can create a namespace by using the Amazon S3 console,
 AWS Command Line Interface (AWS CLI), Amazon S3 REST API, AWS SDKs, or integrated query engines.


###### Namespace names


The following naming rules apply to namespaces:


* Names must be between 1 and 255 characters long.
* Names can consist only of lowercase letters, numbers, and underscores (`_`).
 Underscores aren't allowed at the start or end of namespace names.
* Names must begin and end with a letter or number.
* Names must not contain hyphens (`-`) or periods (`.`).
* A namespace must be unique within a table bucket.
* Namespace names must not start with the reserved prefix `aws`.
For more information about valid namespace names, see [Naming rules for tables and namespaces](s3-tables-buckets-naming.md#naming-rules-table "s3-tables-buckets-naming.md#naming-rules-table").

The following procedure uses the **Create table with Athena** workflow to
 create a namespace in the Amazon S3 console. If you don't want to also use Amazon Athena to create a table in
 your namespace, you can cancel the workflow after creating your namespace. 

###### To create a namespace

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. On the **Table buckets** page, choose the bucket that you want to create a
 namespace in.
4. On the bucket details page, choose **Create table with Athena**.
5. In the **Create table with Athena** dialog box, choose **Create a
 namespace**, and then choose **Create namespace**.
6. Enter a name in the **Namespace name** field. Namespace names must be 1 to
 255 characters and unique within the table bucket. Valid characters are a–z, 0–9,
 and underscores (`_`). Underscores aren't allowed at the start or end of namespace
 names.
7. Choose **Create namespace**.
8. If you also want to create a table, choose **Create table with Athena**.
 For more information about creating a table with Athena, see [Using the S3 console and Amazon Athena](s3-tables-create.md#create-table-console "s3-tables-create.md#create-table-console"). If you don't want to create a table right now, choose **Cancel**.
This example shows how to create a table namespace by using the AWS CLI. To use this
 example, replace the ``user input placeholders`` with your own
 information.


```
aws s3tables create-namespace \
    --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket1` \ 
    --namespace `example_namespace`
```
You can create a namespace in an Apache Spark session connected
 to your Amazon S3 table buckets.

This example shows you how to create a table by using `CREATE`
 statements in a query engine integrated with S3 Tables. To use this example,
 replace the `user input placeholders` with your own
 information.


```
spark.sql("CREATE NAMESPACE IF NOT EXISTS s3tablesbucket.`my_namespace`")
```
