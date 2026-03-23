# Managing S3 Tables integration

## Enable AWS Lake Formation

You can enable AWS Lake Formation for your S3 Tables catalog when you want to scale your data
governance requirements. AWS Lake Formation provides database-style grants to manage fine-grained
access, scale permissions using tag-based access, and grant permissions based on user
attributes such as group associations to your tables in S3 Tables.

Go to the AWS Lake Formation management console to enable AWS Lake Formation for your S3 Tables catalog
in AWS Glue. For more information, see [Creating an S3 Tables catalog](../../../lake-formation/latest/dg/create-s3-tables-catalog.md "../../../lake-formation/latest/dg/create-s3-tables-catalog.md") in the _AWS Lake Formation Developer
Guide_.

## Delete S3 Tables integration

You can delete S3 Tables integration by deleting the catalog integration in the
Data Catalog. This operation only deletes the metadata in the Data Catalog and not the resources
in S3 Tables.

Ensure that you have the necessary permissions to list, edit, and delete catalog
objects in AWS Glue.

### Delete integration (console)

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/home](https://console.aws.amazon.com/glue/home "https://console.aws.amazon.com/glue/home").
2. In the navigation pane, choose
   **Catalogs**.
3. In the **Catalog** list, select
   **s3tablescatalog**.
4. Choose **Delete**.
5. Confirm that deleting the catalog also deletes all associated catalog
   objects in the Data Catalog.
6. Choose **Delete**.

### Delete integration (AWS CLI)

```
aws glue delete-catalog \
  --region `region` \
  --catalog-id "s3tablescatalog"
```
