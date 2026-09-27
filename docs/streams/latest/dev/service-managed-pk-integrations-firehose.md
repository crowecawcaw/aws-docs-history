

# Amazon Data Firehose consuming from service-managed streams
<a name="service-managed-pk-integrations-firehose"></a>

Amazon Data Firehose delivery streams that source data from a Kinesis Data Streams stream configured with service-managed record distribution continue to work without changes. Firehose reads records from shards and delivers them to destinations regardless of how records were distributed across shards. No configuration changes are required.

When records are written to a service-managed stream without a partition key, Amazon Data Firehose surfaces the partition key as an *empty string* (`""`) rather than `null` in the following customer-facing cases:
+ **Transformation Lambda function input** – If you use a Lambda function to transform records, the `partitionKey` field in the Lambda input event is an empty string for records written without a partition key. This avoids compatibility issues with common parsing libraries (such as AWS Lambda Powertools) that perform non-null validation on the `partitionKey` field.
+ **Snowflake destination metadata** – If you deliver to a Snowflake destination, the partition key metadata column contains an empty string for records written without a partition key.

**Note**  
If you opt into service-managed record distribution and do not provide partition keys, expect an empty string (`""`) rather than your previously supplied partition key value in these locations. Do not rely on the partition key value for business logic when using service-managed record distribution.