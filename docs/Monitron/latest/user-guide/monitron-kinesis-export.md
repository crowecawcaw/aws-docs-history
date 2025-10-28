Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Amazon Monitron Kinesis data export v1

###### Note

Amazon Monitron Kinesis data export schema v1 has been deprecated. Learn more about the [v2 data export schema](monitron-kinesis-export-v2.md "monitron-kinesis-export-v2.md").

You can export incoming measurement data and the corresponding inference results from
Amazon Monitron and perform real-time analysis. Data export streams live data to
Kinesis.

###### Topics

- [Exporting your data to a Kinesis
  stream](#exporting-stream-procedure "#exporting-stream-procedure")
- [Editing live data export settings](#edit-live-export "#edit-live-export")
- [Stopping a live data export](#stop-kinesis-export "#stop-kinesis-export")
- [Viewing data export errors](#viewing-kinesis-export-errors "#viewing-kinesis-export-errors")
- [Using server-side encryption for the Kinesis stream](#data-export-server-side-encryption "#data-export-server-side-encryption")
- [Monitoring with Amazon CloudWatch Logs](data-export-cloudwatch-logs.md "data-export-cloudwatch-logs.md")
- [Storing exported data in Amazon S3](kinesis-store-S3.md "kinesis-store-S3.md")
- [Processing data with Lambda](data-export-lambda.md "data-export-lambda.md")
- [Understanding the v1 data export schema](data-export-schema.md "data-export-schema.md")

## Exporting your data to a Kinesis

stream

1. From your project's main page, near the bottom of the page, on the right,
   choose **Start live data export**.
2. Under **Select Amazon Kinesis data stream**, do one of
   the following:
   - Enter the name of an existing stream in the search box. Then skip
     to Step 5.
   - Choose **Create a new data stream**.

3. On the **Create data stream** page, under **Data
   stream configuration**, enter your data stream name.
4. Under Data stream capacity, choose your capacity mode:
   - If your data stream’s throughput requirements are unpredictable
     and variable, choose **On-demand**.
   - If you can reliably estimate the throughput requirements of your
     data stream, choose **Provisioned**. Then, under
     provisioned shards, enter the number of shards you want to create,
     or choose the **Shard estimator**.

5. Choose **Create data stream**.

## Editing live data export settings

To edit your live data export settings:

1. Open the Amazon Monitron console.
2. Choose **Projects** from the navigation pane.
3. If you have multiple projects, choose the project for which you want to
   edit the export settings.
4. From the main page for your project, under **Live data
   export**, from the **Actions** dropdown menu,
   choose **Edit live data export settings**.

## Stopping a live data export

1. Open the Amazon Monitron console.
2. Choose **Projects** from the navigation pane.
3. If you have multiple projects, choose the project for which you want to
   edit the export settings.
4. From the main page for your project, under **Live data
   export**, from the **Actions** dropdown menu,
   choose **Stop live data export**.
5. In the pop-up window, choose **Stop**.

## Viewing data export errors

To view the error messages in the CloudWatch Logs interface:

- On the Amazon Monitron console, from the main page for your project, under
  **Live data export**, choose **CloudWatch log
  group**.

## Using server-side encryption for the Kinesis stream

You can enable server-side encryption for your Kinesis stream before setting up Kinesis
data export. However, if server-side encryption is enabled after Kinesis data export is
set up, Amazon Monitron will not be able to publish to the stream. That's because Amazon Monitron will
not have permission to call [kms:GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") so that it can encrypt data sent to Kinesis.

To work around this, follow the instructions under [Editing live data export settings](#edit-live-export "#edit-live-export"), but without changing the configuration. This will
associate the encryption you have set up with your export configuration.
