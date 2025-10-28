Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

#

Registering namespaces to the AWS Glue Data Catalog

You can register entire namespaces to the AWS Glue Data Catalog and create catalogs managed by AWS Glue.
You can access these catalogs with any SQL engine that supports the Apache Iceberg REST API.
For more information on creating Apache Iceberg-compatible catalogs from Amazon Redshift
see [Apache Iceberg compatibility for Amazon Redshift](../dg/iceberg-integration_overview.md "../dg/iceberg-integration_overview.md") in the
Amazon Redshift Database Developer Guide.

###### To register a serverless namespace to the AWS Glue Data Catalog

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Redshift Serverless**. The Serverless dashboard appears.
   In the **Namespaces/Workgroups** section is the list of namespaces and workgroups
   for your account in the current AWS Region. If you don't have any namespaces, choose
   **Create workgroup** to create a workgroup and its corresponding namespace.
3. Choose the name of the namespace that you want to register.
4. From **Actions**, choose **Register to AWS Glue Data Catalog**.
   The **Register to AWS Glue Data Catalog** pop-up box appears.
5. Enter the AWS account ID that you want to register the namespace to under
   **Destination account ID**. This is the account ID that
   will hold the catalog in the AWS Glue Data Catalog.
6. Enter a name under **Register namespace as**.
   This will be the namespace’s name in the Data Catalog.
7. Choose **Register**. You’ll be taken to the AWS Lake Formation console.
8. Follow the catalog creation process in AWS Lake Formation. For information about creating
   a catalog, see [Bringing Amazon Redshift data into the AWS Glue Data Catalog](../../../lake-formation/latest/dg/managing-namespaces-datacatalog.md "../../../lake-formation/latest/dg/managing-namespaces-datacatalog.md") in the
   AWS Lake Formation Developer Guide.
