# Adding databases and tables to the S3 Tables catalog

Ensure that you have the necessary permissions to list and create catalogs, databases,
and tables in the Data Catalog in your Region. Ensure that S3 Tables integration is enabled
in your AWS account and Region.

## Adding a database to the S3 Tables catalog

### Adding a database (console)

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/home](https://console.aws.amazon.com/glue/home "https://console.aws.amazon.com/glue/home").
2. In the left navigation pane, choose
   **Databases**.
3. Choose **Add Database**.
4. Choose **Glue Database in S3 Tables Federated
   Catalog**.
5. Enter a unique name for the database.
6. Select the target catalog which maps to a table bucket in S3
   Tables.
7. Choose **Create Database**.

### Adding a database (AWS CLI)

```
aws glue create-database \
  --region `region` \
  --catalog-id "`account-id`:s3tablescatalog/`my-catalog`" \
  --database-input '{"Name": "`my-database`"}'
```

## Adding a table to the S3 Tables catalog

### Adding a table (console)

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/home](https://console.aws.amazon.com/glue/home "https://console.aws.amazon.com/glue/home").
2. In the left navigation pane, choose
   **Tables**.
3. Select the appropriate S3 Tables catalog in the catalog
   dropdown.
4. Choose **Add Table**.
5. Enter a unique name for your table.
6. Confirm the correct S3 Tables catalog is selected in the catalog
   dropdown.
7. Select the database in the database dropdown.
8. Enter the table schema by either inputting a JSON or adding each column
   individually.
9. Choose **Create table**.

### Adding a table (AWS CLI)

```
aws glue create-table \
  --region `region` \
  --catalog-id "`account-id`:s3tablescatalog/`my-catalog`" \
  --database-name "`my-database`" \
  --table-input '{
    "Name": "`my-table`",
    "Parameters": {
      "classification": "",
      "format": "ICEBERG"
    },
    "StorageDescriptor": {
      "Columns": [
        {"Name": "id", "Type": "int", "Parameters": {}},
        {"Name": "val", "Type": "string", "Parameters": {}}
      ]
    }
  }'
```
