

# Streaming tables with Amazon MSK
<a name="s3-tables-streaming-msk"></a>

Streaming tables are Apache Iceberg tables in your table buckets that Amazon Managed Streaming for Apache Kafka (Amazon MSK) writes to continuously. Unlike tables that you create and write to directly, a streaming table is created and populated by Amazon MSK. Amazon MSK Express brokers deliver records from a Kafka topic as Apache Parquet data files and commit them to the table, making the data available to query within minutes of being produced. A single streaming table scales to Amazon MSK delivery throughput of up to 10 GBps without manual scaling.

Because Amazon MSK owns the writes, a streaming table is read-only. You have full read access from any Iceberg-compatible engine, and you control table maintenance and read access the same way as for other tables in your table bucket.

You create a streaming table by configuring an Amazon MSK delivery channel rather than by calling `CreateTable`. Amazon MSK creates the table on first delivery. For how to configure the channel, including the source topic, data freshness, dead-letter queue, and the AWS Glue Schema Registry, see [Amazon MSK data delivery](https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery.html) in the *Amazon Managed Streaming for Apache Kafka Developer Guide*.

## What you can and can't do with streaming tables
<a name="s3-tables-streaming-msk-capabilities"></a>

With a streaming table, you can do the following:
+ Query the table with Amazon Athena, Amazon Redshift, Amazon EMR, Apache Spark, or any other Iceberg-compatible query engine.
+ Grant read access with AWS Identity and Access Management (IAM) policies, table bucket policies, and AWS Lake Formation.
+ Configure the automated S3 Tables maintenance jobs: compaction, snapshot expiration, and unreferenced file removal.
+ Configure record expiration on the `timestamptz` partition column to automatically delete records older than a retention period that you specify.
+ Delete the table with `DeleteTable`. After you delete the table, Amazon MSK delivery fails. To resume delivery, recreate the Amazon MSK channel.

With a streaming table, you can't do the following:
+ Write to the table directly (`INSERT`, `UPDATE`, `MERGE`, `COPY INTO`, or Iceberg writes from your own engines).
+ Change the schema, partition spec, sort order, or table properties.
+ Delete individual rows outside of the record expiration job.
+ Backfill records that were produced to the Kafka topic before the Amazon MSK channel was enabled.

## Permissions to query streaming tables
<a name="s3-tables-streaming-msk-permissions"></a>

Read access to a streaming table works the same as for any other Amazon S3 table. You grant it with IAM policies, table bucket policies, and AWS Lake Formation. The following example policy allows you to query a streaming table. If the table is encrypted with an AWS AWS KMS key, the second statement grants the `kms:Decrypt` permission on that key.

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Sid":"PermissionsToQueryStreamingTables",
         "Effect":"Allow",
         "Action":[
             "s3tables:GetTable",
             "s3tables:GetTableData",
             "s3tables:GetTableMetadataLocation"
         ],
         "Resource":[
            "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/amzn-s3-demo-table-bucket",
            "arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/amzn-s3-demo-table-bucket/table/*"
         ]
      },
      {
         "Sid":"PermissionsToDecryptTableData",
         "Effect":"Allow",
         "Action":[
             "kms:Decrypt"
         ],
         "Resource":[
            "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{01234567-89ab-cdef-0123-456789abcdef}}"
         ]
       }
    ]
}
```

The permissions that Amazon MSK needs to create the table and write to it belong to the Amazon MSK service role. For those permissions, see [IAM permissions for Amazon MSK data delivery](https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iam.html) in the *Amazon Managed Streaming for Apache Kafka Developer Guide*. If your table bucket is in a different AWS account from the Amazon MSK cluster, the bucket owner must attach a table bucket policy that grants the Amazon MSK service role the actions it needs. For more information, see [Managing table bucket policies](s3-tables-bucket-policy.md).