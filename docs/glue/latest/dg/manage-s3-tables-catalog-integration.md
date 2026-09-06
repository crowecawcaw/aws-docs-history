

# Managing S3 Tables integration
<a name="manage-s3-tables-catalog-integration"></a>

## Enable AWS Lake Formation
<a name="manage-s3-tables-enable-lf"></a>

You can enable AWS Lake Formation for your S3 Tables catalog when you want to scale your data governance requirements. AWS Lake Formation provides database-style grants to manage fine-grained access, scale permissions using tag-based access, and grant permissions based on user attributes such as group associations to your tables in S3 Tables.

Go to the AWS Lake Formation management console to enable AWS Lake Formation for your S3 Tables catalog in AWS Glue. For more information, see [Creating an S3 Tables catalog](https://docs.aws.amazon.com/lake-formation/latest/dg/create-s3-tables-catalog.html) in the *AWS Lake Formation Developer Guide*.

## Delete S3 Tables integration
<a name="manage-s3-tables-delete-integration"></a>

You can delete S3 Tables integration by deleting the catalog integration in the Data Catalog. This operation only deletes the metadata in the Data Catalog and not the resources in S3 Tables.

Ensure that you have the necessary permissions to list, edit, and delete catalog objects in AWS Glue.

### Delete integration (console)
<a name="delete-s3-tables-console"></a>

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/home](https://console.aws.amazon.com/glue/home).

1. In the navigation pane, choose **Catalogs**.

1. In the **Catalog** list, select **s3tablescatalog**.

1. Choose **Delete**.

1. Confirm that deleting the catalog also deletes all associated catalog objects in the Data Catalog.

1. Choose **Delete**.

### Delete integration (AWS CLI)
<a name="delete-s3-tables-cli"></a>

```
aws glue delete-catalog \
  --region {{region}} \
  --catalog-id "s3tablescatalog"
```