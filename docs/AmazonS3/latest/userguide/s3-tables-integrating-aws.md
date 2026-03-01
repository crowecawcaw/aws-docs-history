# Integrating Amazon S3 Tables with AWS analytics services

This topic covers the prerequisites and procedures needed to integrate your Amazon S3 table buckets with AWS analytics services. For an overview of how the integration works, see [S3 Tables integration overview](s3-tables-integration-overview.md "s3-tables-integration-overview.md").

###### Note

This integration uses the AWS Glue and AWS Lake Formation services and might incur AWS Glue request and storage costs. For more information,
see [AWS Glue Pricing.](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/")

Additional pricing applies for running queries on your S3 tables. For more information, see
pricing information for the query engine that you're using.

## Prerequisites for integration

The following prerequisites are required to integrate table buckets with AWS analytics
services:

- [Create a table
  bucket.](s3-tables-buckets-create.md "s3-tables-buckets-create.md")
- Attach the [AWSLakeFormationDataAdmin](../../../aws-managed-policy/latest/reference/AWSLakeFormationDataAdmin.md "../../../aws-managed-policy/latest/reference/AWSLakeFormationDataAdmin.md") AWS managed policy to your AWS Identity and Access Management (IAM)
  principal to make that user a data lake administrator. For more information about how to create a
  data lake administrator, see [Create a data lake
  administrator](../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin "../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin") in the _AWS Lake Formation Developer Guide_.
- Add permissions for the `glue:PassConnection` operation to
  your IAM principal.
- Add permissions for the `lakeformation:RegisterResource` and
  `lakeformation:RegisterResourceWithPrivilegedAccess` operations to your IAM
  principal.
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

Amazon S3 Tables integrates with AWS Glue Data Catalog (Data Catalog) and registers the catalog as a Lake Formation data location. You can set up
this registration from the Lake Formation console or by using the service APIs. When you register the location, you must specify an IAM role that grants
read/write permissions to the Lake Formation registered role to access that location. Lake Formation assumes that role when supplying temporary
credentials to integrated AWS services.

If you have an IAM or S3 Tables resource-based policy that restricts IAM users and
IAM roles based on principal tags, you must attach the same principal tags to the IAM role
that Lake Formation uses to access your Amazon S3 data (for example, LakeFormationDataAccessRole) and
grant this role the necessary permissions. This is required for your tag-based access control
policy to work correctly with your S3 Tables analytics integration.

This integration must be configured once per AWS Region.

###### Important

The AWS analytics services integration now uses the `WithPrivilegedAccess` option
in the `registerResource` Lake Formation API operation to register S3 table buckets. The integration
also now creates the `s3tablescatalog` catalog in the AWS Glue Data Catalog by using the
`AllowFullTableExternalDataAccess` option in the `CreateCatalog` AWS Glue API
operation.

If you set up the integration with the preview release, you can continue to use your current
integration. However, the updated integration process provides performance improvements, so we
recommend migrating. To migrate to the updated integration, see [Migrating to the updated integration process](#migrate-integrate-console "#migrate-integrate-console").

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. Choose **Create table bucket**.

The **Create table bucket** page opens. 4. Enter a **Table bucket name** and make sure that the **Enable
integration** checkbox is selected. 5. Choose **Create table bucket**. Amazon S3 will attempt to automatically integrate your table buckets in that
Region.
The first time that you integrate table buckets in any Region, Amazon S3 creates a new
IAM service role on your behalf. This role allows Lake Formation to access all table buckets in your account
and federate access to your tables in AWS Glue Data Catalog.

###### To integrate table buckets using the AWS CLI

The following steps show how to use the AWS CLI to integrate table buckets. To use
these steps, replace the `user input placeholders` with your
own information.

1. Create a table bucket.

```
aws s3tables create-table-bucket \
--region `us-east-1` \
--name `amzn-s3-demo-table-bucket`
```

2. Create an IAM service role that allows Lake Formation to access your table
   resources.
   1. Create a file called `Role-Trust-Policy.json` that
      contains the following trust policy:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "LakeFormationDataAccessPolicy",
    "Effect": "Allow",
    "Principal": {
    "Service": "lakeformation.amazonaws.com"
    },
    "Action": [
    "sts:AssumeRole",
    "sts:SetContext",
    "sts:SetSourceIdentity"
    ],
    "Condition": {
    "StringEquals": {
    "aws:SourceAccount": "`111122223333`"
    }
    }
    }
    ]
   }`

   ```

   Create the IAM service role by using the following command:

   ```
   aws iam create-role \
   --role-name `S3TablesRoleForLakeFormation` \
   --assume-role-policy-document file://`Role-Trust-Policy.json`
   ```

   2. Create a file called `LF-GluePolicy.json` that
      contains the following policy:

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "LakeFormationPermissionsForS3ListTableBucket",
    "Effect": "Allow",
    "Action": [
    "s3tables:ListTableBuckets"
    ],
    "Resource": [
    "*"
    ]
    },
    {
    "Sid": "LakeFormationDataAccessPermissionsForS3TableBucket",
    "Effect": "Allow",
    "Action": [
    "s3tables:CreateTableBucket",
    "s3tables:GetTableBucket",
    "s3tables:CreateNamespace",
    "s3tables:GetNamespace",
    "s3tables:ListNamespaces",
    "s3tables:DeleteNamespace",
    "s3tables:DeleteTableBucket",
    "s3tables:CreateTable",
    "s3tables:DeleteTable",
    "s3tables:GetTable",
    "s3tables:ListTables",
    "s3tables:RenameTable",
    "s3tables:UpdateTableMetadataLocation",
    "s3tables:GetTableMetadataLocation",
    "s3tables:GetTableData",
    "s3tables:PutTableData"
    ],
    "Resource": [
    "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/*"
    ]
    }
    ]
   }`

   ```

   Attach the policy to the role by using the following command:

   ```
   aws iam put-role-policy \
   --role-name `S3TablesRoleForLakeFormation`  \
   --policy-name LakeFormationDataAccessPermissionsForS3TableBucket \
   --policy-document file://`LF-GluePolicy.json`
   ```

3. Create a file called `input.json` that contains the following:

```
{
    "ResourceArn": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/*",

    "WithFederation": true,
    "RoleArn": "arn:aws:iam::`111122223333`:role/`S3TablesRoleForLakeFormation`"
}
```

Register table buckets with Lake Formation by using the following command:

```
aws lakeformation register-resource \
--region `us-east-1` \
--with-privileged-access \
--cli-input-json file://`input.json`
```

4. Create a file called `catalog.json` that contains the following
   catalog:

```
{
   "Name": "s3tablescatalog",
   "CatalogInput": {
      "FederatedCatalog": {
          "Identifier": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/*",
          "ConnectionName": "aws:s3tables"
       },
       "CreateDatabaseDefaultPermissions":[],
       "CreateTableDefaultPermissions":[],
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

5. Verify that the `s3tablescatalog` catalog was added in AWS Glue by using the following
   command:

```
aws glue get-catalog --catalog-id s3tablescatalog
```

The AWS analytics services integration process has been updated. If you've set up the
integration with the preview release, you can continue to use your current integration. However, the
updated integration process provides performance improvements, so we recommend migrating by using
the following steps. For more information about the migration or integration process, see [Creating an Amazon S3
Tables catalog in the AWS Glue Data Catalog](../../../lake-formation/latest/dg/create-s3-tables-catalog.md "../../../lake-formation/latest/dg/create-s3-tables-catalog.md") in the _AWS Lake Formation Developer
Guide_.

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

After you integrate your IAM principal is granted Lake Formation permissions to access your tables, if you want to allow other IAM principals to access tables, you need to grant Lake Formation permissions on your tables to those principals. For more information, see [Managing access to a table or database with Lake Formation](grant-permissions-tables.md "grant-permissions-tables.md").

###### Next steps

- [Create a namespace](s3-tables-namespace-create.md "s3-tables-namespace-create.md").
- [Create a table](s3-tables-create.md "s3-tables-create.md").
