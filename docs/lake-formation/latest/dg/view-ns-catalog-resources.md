# Viewing catalog objects

After you create the federated catalog, you can view the objects in the catalog using the Lake Formation console or AWS CLI.

AWS Management Console

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. Choose **Catalogs** under Data Catalog.
3. Choose a federated catalog from the list on the **Catalogs** page.
4. The catalog summary page shows the catalog objects (databases and tables) that you have permissions on. The **Permissions** tab shows the IAM principals who has been granted permissions on these objects.

AWS CLI

- The following AWS CLI example shows how to request the top-level catalog.

```
aws glue get-catalog \
--catalog-id 123456789012:nscatalog
```

_Response_

```
{
    "Catalog": {
        "CatalogId": "123456789012:nscatalog",
        "Name": "nscatalog",
        "ResourceArn": "arn:aws:glue:us-east-1:123456789012:catalog/nscatalog",
        "Description": "Redshift published Catalog",
        "CreateTime": "2024-09-05T14:49:16-07:00",
        "FederatedCatalog": {
            "Identifier": "arn:aws:redshift:us-east-1:123456789012:datashare:b1234589-e823-4a14-ad8e-077085540a50/ds_internal_namespace",
            "ConnectionName": "aws:redshift"
        },
        "CatalogProperties": {
            "DataLakeAccessProperties": {
                "DataLakeAccess": true,
                "DataTransferRole": "arn:aws:iam::123456789012:role/DataTransferRole",
                "KmsKey": "AWS_OWNED_KMS_KEY",
                "ManagedWorkgroupName": "123456789012:nscatalog",
                "ManagedWorkgroupStatus": "AVAILABLE",
                "RedshiftDatabaseName": "dev"
            }
        },
        "CatalogIdentifier": "e2309c2c2fb048f1a3069dfdc1c7883e",
        "CreateTableDefaultPermissions": [],
        "CreateDatabaseDefaultPermissions": []
    }
}
```

- The following example shows how to request all catalogs in the account.

```
aws glue get-catalogs \
  --recursive
```

- The following example request shows how to get a Amazon Redshift database-level catalog.

```
aws glue get-catlog \
 --catalog-id 123456789012:`namespace catalog name`/`redshift database name`
```

- The following example request shows how to get the databases in the Amazon Redshift database-level catalog.

```
aws glue get-databases \
--catalog-id 123456789012:`namespace catalog name`/`redshift database name`
```

- The following example request shows how to get a Amazon Redshift table in the catalog.

```
aws glue get-table \
  --catalog-id 123456789012:`parent catalog name`/`redshift database` \
  --database-name `redshift schema name` \
  --name `table name`
```

- Following example shows how to get all tables from the Amazon Redshift database.

```
aws glue get-tables \
 --catalog-id 123456789012:`namespace catalog name`/`redshift database name` \
 --database-name `RS schema name`
```
