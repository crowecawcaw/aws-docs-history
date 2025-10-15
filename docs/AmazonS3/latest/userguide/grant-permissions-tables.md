# Managing access to a table or database with Lake Formation

After your table buckets are integrated with the AWS analytics services, Lake Formation manages access
 to your table resources. Lake Formation uses its own permissions model (Lake Formation permissions) that enables
 fine-grained access control for Data Catalog resources. Lake Formation requires that each IAM principal (user or
 role) be authorized to perform actions on Lake Formation–managed resources. For more information, see [Overview of Lake Formation
 permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-overview.html "https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-overview.html") in the *AWS Lake Formation Developer Guide*. For
 information about cross-account data sharing, see [Cross-account data sharing in
 Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-permissions.html "https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-permissions.html") in the *AWS Lake Formation Developer Guide*. 

Before IAM principals can access tables in AWS analytics services, you must grant them Lake Formation
 permissions on those resources.

###### Note

If you're the user who performed the table bucket integration, you already have Lake Formation permissions
 to your tables. If you're the only principal who will access your tables, you can skip this step. You
 only need to grant Lake Formation permissions on your tables to other IAM principals. This allows other
 principals to access the table when running queries. For more information, see [Granting Lake Formation permission on a table or database](#grant-lf-table "#grant-lf-table"). 

You must grant other IAM principals Lake Formation permissions on your table resources to work with them
 in the following services:


* Amazon Redshift
* Amazon Data Firehose
* Amazon QuickSight
* Amazon Athena

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
 see [Cross-account data sharing in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-permissions.html "https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-permissions.html") in the *AWS Lake Formation Developer
 Guide*.


Console1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"), and
 sign in as a data lake administrator. For more information about how to create a data lake
 administrator, see [Create a data
 lake administrator](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin "https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin") in the *AWS Lake Formation Developer
 Guide*.
2. In the navigation pane, choose **Data permissions**, and then choose
 **Grant**.
3. On the **Grant Permissions** page, under **Principals**,
 do one of the following:


	* For Amazon Athena or Amazon Redshift, choose **IAM users and roles**, and select the IAM
	 principal you use for queries.
	* For Amazon Data Firehose, choose **IAM users and roles**, and select the service role that you
	 created to stream to tables.
	* For QuickSight, choose **SAML users and groups**, and enter the Amazon Resource Name (ARN) of
	 your QuickSight admin user.
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

If you're creating a new table in the Athena query editor, don't select a table.
8. Do one of the following:


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
 data lake administrator](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin "https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin") in the *AWS Lake Formation Developer
 Guide*.
2. Run the following command to grant Lake Formation permissions on table in S3 table bucket to an IAM principal to
 access the table. To use this example, replace the ``user input
 placeholders`` with your own information. 



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
