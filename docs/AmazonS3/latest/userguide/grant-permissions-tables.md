# Managing access to a table or database with Lake Formation

After your table buckets are integrated with the AWS analytics services, Lake Formation manages access
to your tables and requires that each IAM principal (user or
role) be authorized to perform actions them. Lake Formation uses its own permissions model (Lake Formation permissions) that enables
fine-grained access control for Data Catalog resources.

For more information, see [Overview of Lake Formation
permissions](../../../lake-formation/latest/dg/lf-permissions-overview.md "../../../lake-formation/latest/dg/lf-permissions-overview.md") in the _AWS Lake Formation Developer Guide_.

There are two main types of permissions in AWS Lake Formation:

1. Metadata access permissions control the ability to create, read, update, and delete metadata
   databases and tables in the Data Catalog.
2. Underlying data access permissions control the ability to read and write data to the underlying
   Amazon S3 locations that the Data Catalog resources point to.
   Lake Formation uses a combination of its own permissions model and the IAM permissions model to control
   access to Data Catalog resources and underlying data:

- For a request to access Data Catalog resources or underlying data to succeed, the request must pass
  permission checks by both IAM and Lake Formation.
- IAM permissions control access to the Lake Formation and AWS Glue APIs and resources, whereas Lake Formation
  permissions control access to the Data Catalog resources, Amazon S3 locations, and the underlying data.
  Lake Formation permissions apply only in the Region in which they were granted, and a principal must be
  authorized by a data lake administrator or another principal with the necessary permissions in order to
  be granted Lake Formation permissions.

###### Note

If you're the user who performed the table bucket integration, you already have Lake Formation permissions
to your tables. If you're the only principal who will access your tables, you can skip this step. You
only need to grant Lake Formation permissions on your tables to other IAM principals. This allows other
principals to access the table when running queries. For more information, see [Granting Lake Formation permission on a table or database](#grant-lf-table "#grant-lf-table").

## Granting Lake Formation permission on a table or database

You can grant a principal Lake Formation permissions on a table or database in a table bucket, either
through the Lake Formation console or the AWS CLI.

###### Note

When you grant Lake Formation permissions on a Data Catalog resource to an external account or directly to an
IAM principal in another account, Lake Formation uses the AWS Resource Access Manager (AWS RAM) service to share the resource.
If the grantee account is in the same organization as the grantor account, the shared resource is
available immediately to the grantee. If the grantee account is not in the same organization, AWS RAM
sends an invitation to the grantee account to accept or reject the resource grant. Then, to make the
shared resource available, the data lake administrator in the grantee account must use the AWS RAM
console or AWS CLI to accept the invitation. For more information about cross-account data sharing,
see [Cross-account data sharing in Lake Formation](../../../lake-formation/latest/dg/cross-account-permissions.md "../../../lake-formation/latest/dg/cross-account-permissions.md") in the _AWS Lake Formation Developer
Guide_.

Console1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"), and
sign in as a data lake administrator. For more information about how to create a data lake
administrator, see [Create a data
lake administrator](../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin "../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin") in the _AWS Lake Formation Developer
Guide_. 2. In the navigation pane, choose **Data permissions**, and then choose
**Grant**. 3. On the **Grant Permissions** page, under **Principals**,
do one of the following:

    * For Amazon Athena or Amazon Redshift, choose **IAM users and roles**, and select the IAM
     principal you use for queries.
    * For Amazon Data Firehose, choose **IAM users and roles**, and select the service role that you
     created to stream to tables.
    * For Quick, choose **SAML users and groups**, and enter the Amazon Resource Name (ARN) of
     your Quick admin user.
    * For AWS Glue Iceberg REST endpoint access, choose **IAM users and roles** then select the IAM role you created for you client. For more information, see [Create an IAM role for your client](s3-tables-integrating-glue-endpoint.md#glue-endpoint-create-iam-role "s3-tables-integrating-glue-endpoint.md#glue-endpoint-create-iam-role")

4. Under **LF-Tags or catalog resources**, choose **Named Data Catalog
   resources**.
5. For **Catalogs**, choose the subcatalog that you created when you integrated your table
   bucket, for example,
   ``account-id`:s3tablescatalog/`amzn-s3-demo-bucket``.
6. For **Databases**, choose the S3
   table bucket namespace that you created.
7. (Optional) For **Tables**, choose the S3 table that you created
   in your table bucket.

###### Note

If you're creating a new table in the Athena query editor, don't select a table. 8. Do one of the following:

    * If you specified a table in the prior step, for **Table
     permissions**, choose **Super**.
    * If you didn't specify a table in the prior step, go to **Database
     permissions**. For cross-account data sharing, you can't choose
     **Super** to grant the other principal all permissions on your
     database. Instead, choose more fine-grained permissions, such as
     **Describe**.

9. Choose **Grant**.

CLI

1. Make sure that you're running the following AWS CLI commands as a data lake administrator. For more
   information, see [Create a
   data lake administrator](../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin "../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin") in the _AWS Lake Formation Developer
   Guide_.
2. Run the following command to grant Lake Formation permissions on table in S3 table bucket to an IAM principal to
   access the table. To use this example, replace the `user input
placeholders` with your own information.

```
aws lakeformation grant-permissions \
--region `us-east-1` \
--cli-input-json \
'{
    "Principal": {
        "DataLakePrincipalIdentifier": "`user or role ARN, for example, arn:aws:iam::account-id:role/example-role`"
    },
    "Resource": {
        "Table": {
            "CatalogId": "`account-id`:s3tablescatalog/``amzn-s3-demo-bucket``",
            "DatabaseName": "`S3 table bucket namespace, for example, test_namespace`",
            "Name": "`S3 table bucket table name, for example test_table`"
        }
    },
    "Permissions": [
        "ALL"
    ]
}'
```
