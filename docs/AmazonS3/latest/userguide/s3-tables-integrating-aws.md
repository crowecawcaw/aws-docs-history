# Integrating Amazon S3 Tables with AWS analytics services

This topic covers the prerequisites and procedures needed to integrate your Amazon S3 table buckets with AWS analytics services. For an overview of how the integration works, see [S3 Tables integration overview](s3-tables-integration-overview.md "s3-tables-integration-overview.md").

###### Note

This integration uses the AWS Glue Data Catalog and might incur AWS Glue request and storage costs. For more information,
see [AWS Glue Pricing.](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/")

Additional pricing applies for running queries on S3 Tables. For more information, see
pricing information for the query engine that you're using.

## Prerequisites for integration

The following prerequisites are required to integrate table buckets with AWS analytics
services:

- [Create a table
  bucket.](s3-tables-buckets-create.md "s3-tables-buckets-create.md")
- Add the following AWS Glue permissions to your AWS Identity and Access Management (IAM)
  principal:
  - `glue:CreateCatalog` which is required to create `s3tablescatalog` federated catalog in the Data Catalog
  - `glue:PassConnection` grants the calling principal the right to delegate `aws:s3tables` connection creation to Amazon S3 service.

- [Update to the latest version of the AWS Command Line Interface (AWS CLI)](../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions "../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions").

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

## Integrating table buckets with AWS analytics services

You can integrate table buckets with Data Catalog and AWS analytics services using IAM access controls by default, or optionally use Lake Formation access controls.

When you integrate using IAM access controls, you require IAM privileges to access Amazon S3 table buckets and tables, Data Catalog objects, and the query engine you're using. If you choose to integrate using Lake Formation, then both IAM access controls and Lake Formation grants determine the access to Data Catalog resources. Please refer to [_AWS Lake Formation Developer Guide_](../../../lake-formation/latest/dg/create-s3-tables-catalog.md "../../../lake-formation/latest/dg/create-s3-tables-catalog.md") to learn more about Lake Formation integration.

The following sections describe how you could use Amazon S3 management console or AWS CLI to configure the integration with IAM access controls.

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. Choose **Create table bucket**.

The **Create table bucket** page opens. 4. Enter a **Table bucket name** and make sure that the **Enable
integration** checkbox is selected. 5. Choose **Create table bucket**. Amazon S3 will attempt to automatically integrate your table buckets in that
Region.

###### To integrate table buckets with IAM access controls using the AWS CLI

The following steps show how to use the AWS CLI to integrate table buckets. To use
these steps, replace the `user input placeholders` with your
own information.

1. Create a table bucket.

```
aws s3tables create-table-bucket \
--region `us-east-1` \
--name `amzn-s3-demo-table-bucket`
```

2. Create a file called `catalog.json` that contains the following
   catalog:

```
{
   "Name": "s3tablescatalog",
   "CatalogInput": {
      "FederatedCatalog": {
          "Identifier": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/*",
          "ConnectionName": "aws:s3tables"
       },
       "CreateDatabaseDefaultPermissions":[
       {
                "Principal": {
                    "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS"
                },
                "Permissions": ["ALL"]
            }
       ],
       "CreateTableDefaultPermissions":[
       {
                "Principal": {
                    "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS"
                },
                "Permissions": ["ALL"]
            }
       ],
       "AllowFullTableExternalDataAccess": "True"
   }
}
```

Create the `s3tablescatalog` catalog by using the following command. Creating
this catalog populates the AWS Glue Data Catalog with objects corresponding to table buckets, namespaces,
and tables.

```
aws glue create-catalog \
--region `us-east-1` \
--cli-input-json file://`catalog.json`
```

3. Verify that the `s3tablescatalog` catalog was added in AWS Glue by using the following
   command:

```
aws glue get-catalog --catalog-id s3tablescatalog
```

The AWS analytics services integration process has been updated to use IAM permissions by default. If you've already set up the integration, you can continue to use your current integration. However, if you want to change your existing integration to use IAM permissions instead, see [_AWS Lake Formation Developer Guide_](../../../lake-formation/latest/dg/create-s3-tables-catalog.md "../../../lake-formation/latest/dg/create-s3-tables-catalog.md"). You can also redo the integration to delete your existing setup in AWS Glue Data Catalog and AWS Lake Formation and re-run the integration. This will remove all existing Lake Formation grants and associated access permissions to the `s3tablescatalog`.

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"), and sign in as a
   data lake administrator. For more information about how to create a data lake administrator, see
   [Create a data
   lake administrator](../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin "../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin") in the _AWS Lake Formation Developer
   Guide_.
2. Delete your `s3tablescatalog` catalog by doing the following:
   - In the left navigation pane, choose **Catalogs**.
   - Select the option button next to the `s3tablescatalog` catalog in the
     **Catalogs** list. On the **Actions** menu, choose
     **Delete**.

3. Deregister the data location for the `s3tablescatalog` catalog by doing the
   following:
   - In the left navigation pane, go to the **Administration** section, and
     choose **Data lake locations**.
   - Select the option button next to the `s3tablescatalog` data lake location,
     for example,
     `s3://tables:`region`:`account-id`:bucket/*`.
   - On the **Actions** menu, choose **Remove**.
   - In the confirmation dialog box that appears, choose **Remove**.

4. Now that you've deleted your `s3tablescatalog` catalog and data lake location,
   you can follow the steps to [integrate your table
   buckets with AWS analytics services](#table-integration-procedures "#table-integration-procedures") by using the updated integration process.

###### Note

If you want to work with SSE-KMS encrypted tables in integrated AWS analytics services, the role you use needs to have permission to use your AWS KMS key for encryption operations. For more information, see [Granting IAM principals permissions to work with encrypted tables in integrated AWS analytics services](s3-tables-kms-permissions.md#tables-kms-integration-permissions "s3-tables-kms-permissions.md#tables-kms-integration-permissions").

###### Next steps

- [Create a namespace](s3-tables-namespace-create.md "s3-tables-namespace-create.md").
- [Create a table](s3-tables-create.md "s3-tables-create.md").
