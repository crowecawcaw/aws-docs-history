

# Sharing S3 Tables catalog objects
<a name="share-s3-tables-catalog"></a>

When using IAM access control, you can share S3 Tables catalog objects with other users using AWS Glue resource links for same-account sharing. For cross-account sharing, you can share S3 table buckets with another AWS account and the IAM role or user in the recipient account can create a AWS Glue catalog object using the shared table bucket.

## Sharing within the same account using resource links
<a name="share-s3-tables-resource-links"></a>

Resource links allow you to create references to AWS Glue databases and tables in the `s3tablescatalog` that appear in your AWS Glue default catalog. This is useful for organizing data access or creating logical groupings of tables.

### Create a resource link (console)
<a name="share-s3-tables-resource-link-console"></a>

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. In the navigation pane, choose **Catalogs**.

1. In the **Catalog** list, select **s3tablescatalog**.

1. Select the table you want to share from the `s3tablescatalog`.

1. Choose **Actions**, then choose **Create resource link**.

1. For **Resource link name**, enter a name for the resource link.

1. For **Target database**, select the database where you want to create the resource link.

1. (Optional) For **Description**, enter a description.

1. Choose **Create**.

The resource link appears in the target database and points to the original table in `s3tablescatalog`.

### Create resource links (AWS CLI)
<a name="share-s3-tables-resource-link-cli"></a>

Create a database resource link:

```
aws glue create-database \
  --database-name "{{my-database-resource-link}}" \
  --database-input '{
    "Name": "{{sales_data_link}}",
    "TargetDatabase": {
      "CatalogId": "{{account-id}}:s3tablescatalog/{{analytics-bucket}}",
      "DatabaseName": "{{sales}}"
    }
  }'
```

Create a table resource link:

```
aws glue create-table \
  --table-name "{{my-table-resource-link}}" \
  --table-input '{
    "Name": "{{sales_data_link}}",
    "TargetTable": {
      "CatalogId": "{{account-id}}:s3tablescatalog/{{analytics-bucket}}",
      "DatabaseName": "{{sales}}",
      "Name": "{{transactions}}"
    }
  }'
```