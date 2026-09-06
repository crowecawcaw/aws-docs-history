

# Table type
<a name="msk-data-delivery-iceberg-table-type"></a>

The Iceberg table that a Channel creates in S3 Tables is managed by the Amazon MSK service. You can query the table using AWS analytics services and any compatible query engine, but you should not update its schema, modify its table properties, or write and delete its data directly. For more information about managed table buckets, see [Using AWS managed table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-aws-managed-buckets.html) in the *Amazon S3 User Guide*.