

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Registering namespaces to the AWS Glue Data Catalog
<a name="serverless_datasharing-register-namespace"></a>

You can register entire namespaces to the AWS Glue Data Catalog and create catalogs managed by AWS Glue. You can access these catalogs with any SQL engine that supports the Apache Iceberg REST API. For more information on creating Apache Iceberg-compatible catalogs from Amazon Redshift see [ Apache Iceberg compatibility for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/iceberg-integration_overview.html) in the Amazon Redshift Database Developer Guide.

**To register a serverless namespace to the AWS Glue Data Catalog**

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Redshift Serverless**. The Serverless dashboard appears. In the **Namespaces/Workgroups **section is the list of namespaces and workgroups for your account in the current AWS Region. If you don't have any namespaces, choose **Create workgroup** to create a workgroup and its corresponding namespace.

1. Choose the name of the namespace that you want to register.

1.  From **Actions**, choose **Register to AWS Glue Data Catalog**. The **Register to AWS Glue Data Catalog** pop-up box appears. 

1. Enter the AWS account ID that you want to register the namespace to under **Destination account ID**. This is the account ID that will hold the catalog in the AWS Glue Data Catalog.

1.  Enter a name under **Register namespace as**. This will be the namespace’s name in the Data Catalog. 

1.  Choose **Register**. You’ll be taken to the AWS Lake Formation console. 

1.  Follow the catalog creation process in AWS Lake Formation. For information about creating a catalog, see [ Bringing Amazon Redshift data into the AWS Glue Data Catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-namespaces-datacatalog.html) in the AWS Lake Formation Developer Guide. 