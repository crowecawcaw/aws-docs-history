# Create your first Channel

1. Create the destination (S3 Table bucket or general-purpose S3 bucket) and the DLQ S3 bucket. For Iceberg, also register your JSON schema in AWS Glue Schema Registry.
2. Create the IAM service role with the required permissions and trust policy (see [IAM permissions for Channel](msk-data-delivery-iam.md "msk-data-delivery-iam.md")).
3. In the Amazon MSK console, open your Express cluster, choose the **Channel** tab, and choose **Create Channel** (see [Manage Channels](msk-data-delivery-manage.md "msk-data-delivery-manage.md") for full steps).
4. Wait for the Channel to transition from **Creating** to **Active**.
5. Produce records to the topic and verify delivery (query the Iceberg table in Athena or Spark, or inspect objects in the S3 bucket).
