# Choose source and destination for your Firehose stream

######

1. Open the Firehose console at
   [https://console.aws.amazon.com/firehose/](https://console.aws.amazon.com/firehose/ "https://console.aws.amazon.com/firehose/").
2. Choose **Create Firehose stream**.
3. On the **Create Firehose stream** page, choose a source for your
   Firehose stream from one of the following options.
   - **Direct PUT** – Choose this option to create a
     Firehose stream that producer applications write to directly. Here is a list of
     AWS services and agents and open source services that integrate with
     Direct PUT in Amazon Data Firehose. This list is not exhaustive, and there may be
     additional services that can be used to send data directly to Firehose.
     - AWS SDK
     - AWS Lambda
     - AWS CloudWatch Logs
     - AWS CloudWatch Events
     - AWS Cloud Metric Streams
     - AWS IoT
     - AWS Eventbridge
     - Amazon Simple Email Service
     - Amazon SNS
     - AWS WAF web ACL logs
     - Amazon API Gateway - Access logs
     - Amazon Pinpoint
     - Amazon MSK Broker Logs
     - Amazon Route 53 Resolver query logs
     - AWS Network Firewall Alerts Logs
     - AWS Network Firewall Flow Logs
     - Amazon Elasticache Redis SLOWLOG
     - Kinesis Agent (linux)
     - Kinesis Tap (windows)
     - Fluentbit
     - Fluentd
     - Apache Nifi
     - Snowflake

   - **Amazon Kinesis Data Streams** – Choose this option to configure a
     Firehose stream that uses a Kinesis data stream as a data source. You can then use
     Firehose to read data easily from an existing Kinesis data stream and load it into
     destinations. For more information about using Kinesis Data Streams as your data source,
     see [Sending data to a Firehose
     stream with Kinesis Data Streams](writing-with-kinesis-streams.md "writing-with-kinesis-streams.md").
   - **Amazon MSK** – Choose this option to configure a
     Firehose stream that uses Amazon MSK as a data source. You can then use Firehose to read
     data easily from an existing Amazon MSK clusters and load it into specified S3
     buckets. For more information, see [Sending
     data to a Firehose stream with Amazon MSK](writing-with-msk.md "writing-with-msk.md").

4. Choose a destination for your Firehose stream from one of the following destinations that Firehose supports.
   - Amazon OpenSearch Service
   - Amazon OpenSearch Serverless
   - Amazon Redshift
   - Amazon S3
   - Apache Iceberg Tables
   - Coralogix
   - Datadog
   - Dynatrace
   - Elastic
   - HTTP Endpoint
   - Honeycomb
   - Logic Monitor
   - Logz.io
   - MongoDB Cloud
   - New Relic
   - Splunk
   - Splunk Observability Cloud
   - Sumo Logic
   - Snowflake

5. For **Firehose stream name**, you can either use the name that the console
   generates for you or add a Firehose stream of your choice.
