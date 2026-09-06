

# Adding databases and tables to the S3 Tables catalog
<a name="create-databases-tables-s3-catalog"></a>

Ensure that you have the necessary permissions to list and create catalogs, databases, and tables in the Data Catalog in your Region. Ensure that S3 Tables integration is enabled in your AWS account and Region.

## Adding a database to the S3 Tables catalog
<a name="add-database-s3-tables-catalog"></a>

### Adding a database (console)
<a name="add-database-s3-tables-console"></a>

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/home](https://console.aws.amazon.com/glue/home).

1. In the left navigation pane, choose **Databases**.

1. Choose **Add Database**.

1. Choose **Glue Database in S3 Tables Federated Catalog**.

1. Enter a unique name for the database.

1. Select the target catalog which maps to a table bucket in S3 Tables.

1. Choose **Create Database**.

### Adding a database (AWS CLI)
<a name="add-database-s3-tables-cli"></a>

```
aws glue create-database \
  --region {{region}} \
  --catalog-id "{{account-id}}:s3tablescatalog/{{my-catalog}}" \
  --database-input '{"Name": "{{my-database}}"}'
```

## Adding a table to the S3 Tables catalog
<a name="add-table-s3-tables-catalog"></a>

### Adding a table (console)
<a name="add-table-s3-tables-console"></a>

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/home](https://console.aws.amazon.com/glue/home).

1. In the left navigation pane, choose **Tables**.

1. Select the appropriate S3 Tables catalog in the catalog dropdown.

1. Choose **Add Table**.

1. Enter a unique name for your table.

1. Confirm the correct S3 Tables catalog is selected in the catalog dropdown.

1. Select the database in the database dropdown.

1. Enter the table schema by either inputting a JSON or adding each column individually.

1. Choose **Create table**.

### Adding a table (AWS CLI)
<a name="add-table-s3-tables-cli"></a>

```
aws glue create-table \
  --region {{region}} \
  --catalog-id "{{account-id}}:s3tablescatalog/{{my-catalog}}" \
  --database-name "{{my-database}}" \
  --table-input '{
    "Name": "{{my-table}}",
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