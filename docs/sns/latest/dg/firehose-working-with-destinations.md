

# Managing Amazon SNS messages across multiple delivery stream destinations
<a name="firehose-working-with-destinations"></a>

[ delivery streams](sns-firehose-as-subscriber.md) let you manage Amazon SNS messages across multiple destinations. You can integrate with Amazon S3, Amazon OpenSearch Service, Amazon Redshift, and HTTP endpoints for storage, indexing, and analysis.

With proper message formatting and delivery configuration, you can:
+ Store Amazon SNS notifications in Amazon S3 for later processing
+ Analyze structured message data using Amazon Athena
+ Index messages in OpenSearch for real-time search and visualization
+ Structure archives in Amazon Redshift for advanced querying