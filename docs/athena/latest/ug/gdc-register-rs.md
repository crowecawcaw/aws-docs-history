

# Register Redshift data catalogs in Athena
<a name="gdc-register-rs"></a>

Athena can read and write data stored in Redshift clusters or serverless namespaces that have been registered in the AWS Glue Data Catalog. This works in tandem with AWS Lake Formation, which provides centralized security and governance, ensuring that data access is managed consistently across different query engines and maintaining fine-grained access controls for the shared Redshift data.

## Considerations and limitations
<a name="gdc-register-rs-considerations-and-limitations"></a>
+ **Materialized views** – Amazon Redshift materialized views are queryable from Athena but creating materialized views using Athena or Spark is not supported.
+ DDL operations, including setting AWS Glue Data Catalog configuration and operations on Amazon Redshift managed storage tables, are not supported.

## Prerequisites
<a name="gdc-register-rs-prerequisites"></a>

Before you can query a AWS Glue data catalog from Athena, complete the following tasks:

1. Create and register an Amazon Redshift cluster or serverless namespace to the AWS Glue Data Catalog. For more information, see [Registering a cluster to the AWS Glue Data Catalog](https://docs.aws.amazon.com/redshift/latest/mgmt/register-cluster.html) or [Registering namespaces to the AWS Glue Data Catalog](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless_datasharing-register-namespace.html) in the Amazon Redshift Management guide.

1. Create a data catalog in AWS Lake Formation from the registered namespace. For more information, see [Creating Amazon Redshift federated catalogs](https://docs.aws.amazon.com/lake-formation/latest/dg/create-ns-catalog.html) in the AWS Lake Formation Developer Guide.

1. (Optional) Use Lake Formation to set fine-grained access controls on the catalog. For more information, see [Bringing your data into the AWS Glue Data Catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/bring-your-data-overview.html) in the AWS Lake Formation Developer Guide.

## Register a Redshift data catalog with the Athena console
<a name="gdc-register-rs-console-steps"></a>

To register a Redshift data catalog with the Athena console, perform the following steps.

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/).

1. In the navigation pane, choose **Data sources and catalogs**.

1. On the **Data sources and catalogs** page, choose **Create data source**.

1. For **Choose a data source**, choose **Amazon S3 - AWS Glue Data Catalog**.

1. In the **AWS Glue Data Catalog** section, for **Data source account**, choose **AWS Glue Data Catalog in this account**.

1. For **Create a table or register a catalog**, choose **Register a new AWS Glue Catalog**.

1. In the **Data source details** section, for **Data source name**, enter the name that you want to use to specify the data source in your SQL queries or use the default name that is generated.

1. For **Catalog**, choose **Browse** to search for a list of AWS Glue catalogs in the same account. If you don't see any existing catalogs, create one in [AWS Glue console](https://console.aws.amazon.com/glue/). 

1. In the **Browse AWS Glue catalogs** dialog box, select the catalog that you want to use, and then choose **Choose**.

1. (Optional) For **Tags**, enter any key/value pairs that you want to associate with the data source.

1. Choose **Next**.

1. On the **Review and create** page, verify that the information that you entered is correct, and then choose **Create data source**.