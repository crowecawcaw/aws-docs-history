# Tutorial: Getting started with S3 Tables

In this tutorial, you create a table bucket and integrate table buckets in your Region
with AWS analytics services. Next, you will use the AWS CLI to create your first namespace and table in your table bucket. Then, you use AWS Lake Formation to grant permission on your table, so you can begin querying your table with Athena.

###### Tip

If you're migrating tabular data from general purpose buckets to table buckets, the
AWS Solutions Library has a guided solution to assist you. This solution automates
moving Apache Iceberg and Apache Hive tables that are
registered in AWS Glue Data Catalog and stored in general purpose buckets to table buckets by
using AWS Step Functions and Amazon EMR with Apache Spark. For more information, see
[Guidance for Migrating Tabular Data from Amazon S3 to S3 Tables](https://aws.amazon.com/solutions/guidance/migrating-tabular-data-from-amazon-s3-to-s3-tables/ "https://aws.amazon.com/solutions/guidance/migrating-tabular-data-from-amazon-s3-to-s3-tables/") in the AWS
Solutions Library.

###### Topics

- [Step 1: Create a table bucket and integrate it with AWS analytics services](#s1-tables-tutorial-create-bucket "#s1-tables-tutorial-create-bucket")
- [Step 2: Create a table namespace and a table](#s2-tables-tutorial-create-namespace-and-table "#s2-tables-tutorial-create-namespace-and-table")
- [(Optional) Step 3: Grant Lake Formation permissions on your
  table](#s3-tables-tutorial-create-table "#s3-tables-tutorial-create-table")
- [Step 4: Query data with SQL in Athena](#s4-query-tables "#s4-query-tables")

## Step 1: Create a table bucket and integrate it with AWS analytics services

In this step, you use the Amazon S3 console to create your first table bucket. For other ways to
create a table bucket, see [Creating a table bucket](s3-tables-buckets-create.md "s3-tables-buckets-create.md").

###### Note

By default, the Amazon S3 console automatically integrates your table buckets with Amazon SageMaker Lakehouse, which allows AWS analytics services to automatically discover and access your S3 Tables
data. If you create your first table bucket programmatically by using the AWS Command Line Interface (AWS CLI), AWS SDKs,
or REST API, you must manually complete the AWS analytics services integration. For more
information, see [Integrating Amazon S3 Tables with AWS analytics
services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the currently displayed AWS Region.
   Next, choose the Region in which you want to create the table bucket.
3. In the left navigation pane, choose **Table buckets**.
4. Choose **Create table bucket**.
5. Under **General configuration**, enter a name for your table bucket.

The table bucket name must:

    * Be unique within for your AWS account in the current Region.
    * Be between 3 and 63 characters long.
    * Consist only of lowercase letters, numbers, and hyphens (`-`).
    * Begin and end with a letter or number.

After you create the table bucket, you can't change its name. The AWS account that
creates the table bucket owns it. For more information about naming table buckets, see [Table bucket naming rules](s3-tables-buckets-naming.md#table-buckets-naming-rules "s3-tables-buckets-naming.md#table-buckets-naming-rules"). 6. In the **Integration with AWS analytics services** section, make sure that
the **Enable integration** checkbox is selected.

If **Enable integration** is selected when you create your first table bucket
by using the console, Amazon S3 attempts to integrate your table bucket with AWS analytics services.
This integration allows you to use AWS analytics services to access all tables in the current
Region. For more information, see [Integrating Amazon S3 Tables with AWS analytics
services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md"). 7. Choose **Create bucket**.

## Step 2: Create a table namespace and a table

For this step, you create a namespace in your table bucket, and then create a new table under that
namespace. You can create a table namespace and a table by using either the console or the AWS CLI.

###### Important

When creating tables, make sure that you use all lowercase letters in your table names and table
definitions. For example, make sure that your column names are all lowercase. If your table name or
table definition contains capital letters, the table isn't supported by AWS Lake Formation or the AWS Glue Data Catalog.
In this case, your table won't be visible to AWS analytics services such as Amazon Athena, even if your
table buckets are integrated with AWS analytics services.

If your table definition contains capital letters, you receive the following error message when
running a `SELECT` query in Athena: **`"GENERIC_INTERNAL_ERROR: Get table request
 failed: com.amazonaws.services.glue.model.ValidationException: Unsupported Federation Resource -
 Invalid table or column names."`**

The following procedure uses the Amazon S3 console to create a namespace and a table with
Amazon Athena.

###### To create a table namespace and a table

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. On the **Table buckets** page, choose the table bucket that you want to
   create a table in.
4. On the table bucket details page, choose **Create table with Athena**.
5. In the **Create table with Athena** dialog box, choose **Create a
   namespace**, and then enter a name in the **Namespace name** field.
   Namespace names must be 1 to 255 characters and unique within the table bucket. Valid characters
   are a–z, 0–9, and underscores (`_`). Underscores aren't allowed at the
   start of namespace names.
6. Choose **Create namespace**.
7. Choose **Create table with Athena**.
8. The Amazon Athena console opens and the Athena query editor appears. The query editor is
   populated with a sample query that you can use to create a table. Modify the query to specify
   the table name and columns that you want your table to have.
9. When you're finished modifying the query, choose **Run** to create your
   table.
   If your table creation was successful, the name of your new table appears in the list of
   tables in Athena. When you navigate back to the Amazon S3 console, your new table appears in the
   **Tables** list on the details page for your table bucket after you refresh the
   list.

To use the following AWS CLI example commands to create a namespace in your table bucket, and then
create a new table with a schema under that namespace, replace the `user input
 placeholder` values with your own.

###### Prerequisites

- Attach the [`AmazonS3TablesFullAccess`](../../../aws-managed-policy/latest/reference/AmazonS3TablesFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonS3TablesFullAccess.md") policy to
  your IAM identity.
- Install AWS CLI version 2.23.10 or higher. For more information, see [Installing or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

1. Create a new namespace in your table bucket by running the following command:

```
aws s3tables create-namespace \
--table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket` \
--namespace `my_namespace`
```

    1. Confirm that your namespace was created successfully by running the following command:



    ```
    aws s3tables list-namespaces \
    --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`
    ```

2. Create a new table with a table schema by running the following command:

```
aws s3tables create-table --cli-input-json file://`mytabledefinition.json`
```

For the `mytabledefinition.json` file, use the following example table
definition:

```
{
    "tableBucketARN": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`",
    "namespace": "`my_namespace`",
    "name": "`my_table`",
    "format": "ICEBERG",
    "metadata": {
        "iceberg": {
            "schema": {
                "fields": [
                     `{"name": "id", "type": "int","required": true},
 {"name": "name", "type": "string"},
 {"name": "value", "type": "int"}`
                ]
            }
        }
    }
}
```

## (Optional) Step 3: Grant Lake Formation permissions on your

table

For this step, you grant Lake Formation permissions on your new table to other IAM principals. These
permissions allow principals other than you to access table bucket resources by using Athena and other
AWS analytics services. For more information, see [Granting Lake Formation permission on a table or database](grant-permissions-tables.md#grant-lf-table "grant-permissions-tables.md#grant-lf-table"). If you're the only user who will access your tables, you can skip
this step.

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"), and sign in as a
   data lake administrator. For more information about how to create a data lake administrator, see
   [Create a data lake
   administrator](../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin "../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin").
2. In the navigation pane, choose **Data permissions** and then choose
   **Grant**.
3. On the **Grant Permissions** page, under **Principals**, choose
   **IAM users and roles** and choose the IAM user or role that you want to allow
   to run queries on your table.
4. Under **LF-Tags or catalog resources**, choose **Named Data Catalog
   resources**.
5. Do one of the following, depending on whether you want to grant access to all of the
   tables in your account or whether you want to grant access to only the resources within the table
   bucket that you created:
   - For **Catalogs**, choose the account-level catalog that you created when
     you integrated your table bucket. For example, ``111122223333`:s3tablescatalog`.
   - For **Catalogs**, choose the subcatalog for your table bucket. For example,
     ``111122223333`:s3tablescatalog/`amzn-s3-demo-table-bucket``.

6. (Optional) If you chose the subcatalog for your table bucket, do one or both of the
   following:
   - For **Databases**, choose the table bucket namespace that you created.
   - For **Tables**, choose the table that you created in your table bucket, or choose
     **All tables**.

7. Depending on whether you chose a catalog or subcatalog and depending on whether you then chose a
   database or a table, you can set permissions at the catalog, database, or table level. For more
   information about Lake Formation permissions, see [Managing Lake Formation permissions](../../../lake-formation/latest/dg/managing-permissions.md "../../../lake-formation/latest/dg/managing-permissions.md") in the
   _AWS Lake Formation Developer Guide_.

Do one of the following:

    * For **Catalog permissions**, choose **Super** to grant the
     other principal all permissions on your catalog, or choose more fine-grained permissions, such
     as **Describe**.
    * For **Database permissions**, you can't choose **Super**
     to grant the other principal all permissions on your database. Instead, choose more fine-grained
     permissions, such as **Describe**.
    * For **Table permissions**, choose **Super** to grant the
     other principal all permissions on your table, or choose more fine-grained permissions, such as
     **Select** or **Describe**.


    ###### Note

    When you grant Lake Formation permissions on a Data Catalog resource to an external account or directly
     to an IAM principal in another account, Lake Formation uses the AWS Resource Access Manager (AWS RAM) service to share the
     resource. If the grantee account is in the same organization as the grantor account, the
     shared resource is available immediately to the grantee. If the grantee account is not in the
     same organization, AWS RAM sends an invitation to the grantee account to accept or reject the
     resource grant. Then, to make the shared resource available, the data lake administrator in
     the grantee account must use the AWS RAM console or AWS CLI to accept the invitation. For more
     information about cross-account data sharing, see [Cross-account data sharing in
     Lake Formation](../../../lake-formation/latest/dg/cross-account-permissions.md "../../../lake-formation/latest/dg/cross-account-permissions.md") in the *AWS Lake Formation Developer Guide*.

8. Choose **Grant**.

## Step 4: Query data with SQL in Athena

You can query your table with SQL in Athena. Athena supports Data Definition Language (DDL), Data
Manipulation Language (DML), and Data Query Language (DQL) queries for S3 Tables.

You can access the Athena query either from the Amazon S3 console or through the Amazon Athena console.

The following procedure uses the Amazon S3 console to access the Athena query editor so that you can
query a table with Amazon Athena.

###### To query a table

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. On the **Table buckets** page, choose the table bucket that contains the
   table that you want to query.
4. On the table bucket details page, choose the option button next to the name of the table
   that you want to query.
5. Choose **Query table with Athena**.
6. The Amazon Athena console opens and the Athena query editor appears with a sample
   `SELECT` query loaded for you. Modify this query as needed for your use case.
7. To run the query, choose **Run**.

###### To query a table

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. Query your table. The following is a sample query that you can modify. Make sure to replace
   the `user input placeholders` with your own
   information.

```
SELECT * FROM "s3tablescatalog/`amzn-s3-demo-table-bucket`"."`my_namespace`"."`my_table`" LIMIT 10
```

3. To run the query, choose **Run**.
