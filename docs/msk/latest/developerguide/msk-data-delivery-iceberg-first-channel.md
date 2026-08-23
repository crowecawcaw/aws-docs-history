# Create your first Channel

1. Create the S3 Table bucket and the DLQ S3 bucket, and register your JSON schema in AWS Glue Schema Registry.
2. Create the IAM service role with the required permissions and trust policy (see [IAM permissions](msk-data-delivery-iceberg-iam.md "msk-data-delivery-iceberg-iam.md")).
3. In the Amazon MSK console, open your Express cluster, choose the **Channel** tab, and choose **Create Channel** (see [Manage Channels](msk-data-delivery-iceberg-manage.md "msk-data-delivery-iceberg-manage.md") for full steps).
4. Wait for the Channel to transition from **Creating** to **Active**.
5. Produce records to the topic and verify delivery by querying the Iceberg table in Athena or Spark.
