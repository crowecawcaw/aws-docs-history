# Enabling S3 Tables integration with the Data Catalog

You can enable S3 Tables integration with the AWS Glue Data Catalog using the Amazon S3 management
console or AWS CLI. When you enable the integration using the console, AWS creates a
federated catalog named `s3tablescatalog` that automatically discovers and
mounts all S3 table buckets in your AWS account and Region.

## Enable S3 Tables integration using the Amazon S3 management console

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. Choose **Create table bucket**.
4. Enter a **Table bucket name** and make sure that the
   **Enable integration** checkbox is selected.
5. Choose **Create table bucket**.

Amazon S3 automatically integrates your table buckets in that Region. The first time
that you integrate table buckets in any Region, Amazon S3 creates
`s3tablescatalog` in the Data Catalog in that Region.

After the catalog is created, all S3 table buckets in your account and Region are
automatically mounted as child catalogs. You can view the databases (namespaces) and
tables by navigating to the catalog in the Data Catalog.

## Enable S3 Tables integration using AWS CLI

Use the `glue create-catalog` command to create the
`s3tablescatalog` catalog.

```
aws glue create-catalog \
  --name "s3tablescatalog" \
  --catalog-input '{
    "Description": "Federated catalog for S3 Tables",
    "FederatedCatalog": {
      "Identifier": "arn:aws:s3tables:`region`:`account-id`:bucket/*",
      "ConnectionName": "aws:s3tables"
    },
    "CreateDatabaseDefaultPermissions": [{
      "Principal": {
        "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS"
      },
      "Permissions": ["ALL"]
    }],
    "CreateTableDefaultPermissions": [{
      "Principal": {
        "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS"
      },
      "Permissions": ["ALL"]
    }]
  }'
```

Replace `region` with your AWS Region and
`account-id` with your AWS account ID.

## Verifying the integration

After creating the catalog, you can verify that S3 table buckets are mounted by
listing the child catalogs:

```
aws glue get-catalogs \
  --parent-catalog-id s3tablescatalog
```
