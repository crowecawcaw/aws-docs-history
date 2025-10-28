# Testing Firehose stream with sample data

You can use the AWS Management Console to ingest simulated stock ticker data. The console runs a
script in your browser to put sample records in your Firehose stream.
This enables you to test the configuration of your Firehose stream
without having to generate your own test data.

The following is an example from the simulated data:

```
{"TICKER_SYMBOL":"QXZ","SECTOR":"HEALTHCARE","CHANGE":-0.05,"PRICE":84.51}
```

Note that standard Amazon Data Firehose charges apply when your Firehose stream transmits the data,
but there is no charge when the data is generated. To stop incurring these charges,
you can stop the sample stream from the console at any time.

## Prerequisites

Before you begin, create a Firehose stream. For more information, see
[Tutorial: Create a Firehose stream from console](basic-create.md "basic-create.md").

## Test with Amazon S3

Use the following procedure to test your Firehose stream with Amazon Simple Storage Service (Amazon S3) as the
destination.

###### To test a Firehose stream using Amazon S3

1. Open the Firehose console at
   [https://console.aws.amazon.com/firehose/](https://console.aws.amazon.com/firehose/ "https://console.aws.amazon.com/firehose/").
2. Choose an active Firehose stream. The Firehose stream must be in **Active** status before you can start sending data.
3. Under **Test with demo data**, choose **Start sending demo data**
   to generate sample stock ticker data.
4. Follow the onscreen instructions to verify that data is being delivered to
   your S3 bucket. Note that it might take a few minutes for new objects to appear
   in your bucket, based on the buffering configuration of your bucket.
5. When the test is complete, choose **Stop sending demo data** to stop incurring
   usage charges.

## Test with Amazon Redshift

Use the following procedure to test your Firehose stream with Amazon Redshift as the
destination.

###### To test a Firehose stream using Amazon Redshift

1. Your Firehose stream expects a table to be present in your Amazon Redshift cluster.
   [Connect to Amazon Redshift through
   a SQL interface](../../../redshift/latest/mgmt/connecting-to-cluster.md "../../../redshift/latest/mgmt/connecting-to-cluster.md") and run the following statement to create a table
   that accepts the sample data.

```
create table firehose_test_table
(
	TICKER_SYMBOL varchar(4),
	SECTOR varchar(16),
	CHANGE float,
	PRICE float
);
```

2. Open the Firehose console at
   [https://console.aws.amazon.com/firehose/](https://console.aws.amazon.com/firehose/ "https://console.aws.amazon.com/firehose/").
3. Choose an active Firehose stream. The Firehose stream must be in **Active** status before you can start sending data.
4. Edit the destination details for your Firehose stream to point to the newly created
   `firehose_test_table` table.
5. Under **Test with demo data**, choose **Start sending demo data**
   to generate sample stock ticker data.
6. Follow the onscreen instructions to verify that data is being delivered to
   your table. Note that it might take a few minutes for new rows to appear in your
   table, based on the buffering configuration.
7. When the test is complete, choose **Stop sending demo data** to stop incurring
   usage charges.
8. Edit the destination details for your Firehose stream to point to another table.
9. (Optional) Delete the `firehose_test_table` table.

## Test with OpenSearch Service

Use the following procedure to test your Firehose stream using Amazon OpenSearch Service as the destination.

###### To test a Firehose stream using OpenSearch Service

1. Open the Firehose console at
   [https://console.aws.amazon.com/firehose/](https://console.aws.amazon.com/firehose/ "https://console.aws.amazon.com/firehose/").
2. Choose an active Firehose stream. The Firehose stream must be in **Active** status before you can start sending data.
3. Under **Test with demo data**, choose **Start sending demo data**
   to generate sample stock ticker data.
4. Follow the onscreen instructions to verify that data is being delivered to
   your OpenSearch Service domain. For more information, see [Searching Documents in an OpenSearch Service
   Domain](../../../opensearch-service/latest/developerguide/es-gsg-search.md "../../../opensearch-service/latest/developerguide/es-gsg-search.md") in the _Amazon OpenSearch Service Developer Guide_.
5. When the test is complete, choose **Stop sending demo data** to stop incurring
   usage charges.

## Test with Splunk

Use the following procedure to test your Firehose stream using Splunk as the destination.

###### To test a Firehose stream using Splunk

1. Open the Firehose console at
   [https://console.aws.amazon.com/firehose/](https://console.aws.amazon.com/firehose/ "https://console.aws.amazon.com/firehose/").
2. Choose an active Firehose stream. The Firehose stream must be in **Active** status before you can start sending data.
3. Under **Test with demo data**, choose **Start sending
   demo data** to generate sample stock ticker data.
4. Check whether the data is being delivered to your Splunk index. Example search
   terms in Splunk are `sourcetype="aws:firehose:json"` and
   `index="`name-of-your-splunk-index`"`.
   For more information about how to search for events in Splunk, see [Search Manual](http://docs.splunk.com/Documentation/Splunk/latest/Search/GetstartedwithSearch "http://docs.splunk.com/Documentation/Splunk/latest/Search/GetstartedwithSearch") in the Splunk documentation.

If the test data doesn't appear in your Splunk index, check your Amazon S3 bucket
for failed events. Also see [Data Not Delivered to Splunk](troubleshooting.md#data-not-delivered-to-splunk "troubleshooting.md#data-not-delivered-to-splunk"). 5. When you finish testing, choose **Stop sending demo data** to
stop incurring usage charges.

## Test with Apache Iceberg Tables

Use the following procedure to test your Firehose stream with Apache Iceberg Tables as the
destination.

###### To test a Firehose stream using Apache Iceberg Tables

1. Open the Firehose console at
   [https://console.aws.amazon.com/firehose/](https://console.aws.amazon.com/firehose/ "https://console.aws.amazon.com/firehose/").
2. Choose an active Firehose stream. The Firehose stream must be in **Active** status before you can start sending data.
3. Under **Test with demo data**, choose **Start sending
   demo data** to generate sample stock ticker data.
4. Follow the instructions on screen to verify that data is being delivered to
   your Apache Iceberg Tables. Note that it might take a few minutes for new
   objects to appear in your bucket, based on its buffering configuration.
5. If the test data doesn't appear in your Apache Iceberg Tables, check your Amazon S3 bucket for
   failed
   events.
6. When you finish testing, choose **Stop sending demo data** to
   stop incurring usage charges.
