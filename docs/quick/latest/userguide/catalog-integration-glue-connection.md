

# Setting up the Data Catalog connection
<a name="catalog-integration-glue-connection"></a>

Connecting to AWS Glue Data Catalog involves two steps: connecting to the catalog for metadata access and connecting to Amazon Athena for data queries.

## Prerequisites
<a name="catalog-integration-glue-prerequisites"></a>
+ An administrator must enable the AWS Glue Data Catalog connector. To do this, go to **AWS resources** under the **Manage Account** page in Quick and select **Glue Data Catalog**.

**Important**  
If an author attempts to create an AWS Glue Data Catalog data source before the administrator enables it under **AWS resources** on the **Manage Account** page, the operation fails with an error. Ensure that the administrator enables AWS Glue Data Catalog for the Quick account before authors attempt to create the data source.
+ The connector uses service role permissions for Glue metadata access. Attach the following IAM policy to the Quick service role:

  ```
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "glue:GetCatalog",
                  "glue:GetCatalogs",
                  "glue:GetDatabases",
                  "glue:GetDatabase",
                  "glue:GetTables",
                  "glue:GetTable",
                  "glue:ListDataQualityResults",
                  "glue:GetDataQualityResult",
                  "lakeformation:GetTemporaryGlueTableCredentials",
                  "lakeformation:GetDataAccess",
                  "glue:GetConnection",
                  "glue:GetConnections",
                  "glue:GetTags"
              ],
              "Resource": [
                  "arn:aws:glue:*:{{account-id}}:catalog",
                  "arn:aws:glue:*:{{account-id}}:catalog/*",
                  "arn:aws:glue:*:{{account-id}}:database/*",
                  "arn:aws:glue:*:{{account-id}}:table/*/*",
                  "arn:aws:glue:*:{{account-id}}:dataQualityRuleset/*",
                  "arn:aws:glue:*:{{account-id}}:connection/*"
              ]
          }
      ]
  }
  ```

  Replace {{account-id}} with your AWS account ID.
**Note**  
This policy grants access to all Glue Data Catalog resources in your account. To follow the principle of least privilege, replace the wildcard (`*`) resource ARNs with ARNs for the specific catalogs, databases, and tables that you want to expose in Quick.
+ If you are not using AWS IAM Identity Center, all data source creators have the same access to catalog metadata as the Quick service role.

## Two-step connection process
<a name="catalog-integration-glue-two-step"></a>

Because AWS Glue Data Catalog provides metadata and Amazon Athena provides query execution, authors complete two connections:

1. **Connect to AWS Glue Data Catalog for metadata** – Navigate to **Create Data Source** and select **Glue Data Catalog**. This connection provides access to table names, table descriptions, column information, and other catalog metadata.

1. **Connect to Amazon Athena for data queries** – Select **Athena** and configure the primary workgroup. This connection enables queries against the underlying Amazon S3 and Apache Iceberg tables. The supported underlying data store is Amazon S3.