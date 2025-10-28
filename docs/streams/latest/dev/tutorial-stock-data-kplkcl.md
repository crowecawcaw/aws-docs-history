# Tutorial: Process real-time stock data using

KPL and KCL 1.x

The scenario for this tutorial involves ingesting stock trades into a data stream and
writing a simple Amazon Kinesis Data Streams application that performs calculations on the stream. You will
learn how to send a stream of records to Kinesis Data Streams and implement an application that consumes
and processes the records in near real time.

###### Important

After you create a stream, your account incurs nominal charges for Kinesis Data Streams usage because
Kinesis Data Streams is not eligible for the AWS Free Tier. After the consumer application starts, it
also incurs nominal charges for Amazon DynamoDB usage. The consumer application uses DynamoDB to
track processing state. When you are finished with this application, delete your AWS
resources to stop incurring charges. For more information, see [Clean up resources](tutorial-stock-data-kplkcl-finish.md "tutorial-stock-data-kplkcl-finish.md").

The code does not access actual stock market data, but instead simulates the stream of
stock trades. It does so by using a random stock trade generator that has a starting point
of real market data for the top 25 stocks by market capitalization as of February 2015. If
you have access to a real-time stream of stock trades, you might be interested in deriving
useful, timely statistics from that stream. For example, you might want to perform a sliding
window analysis where you determine the most popular stock purchased in the last 5 minutes.
Or you might want a notification whenever there is a sell order that is too large (that is,
it has too many shares). You can extend the code in this series to provide such
functionality.

You can work through the steps in this tutorial on your desktop or laptop computer and run
both the producer and consumer code on the same machine or any platform that supports the
defined requirements, such as Amazon Elastic Compute Cloud (Amazon EC2).

The examples shown use the US West (Oregon) Region, but they work on any of the [AWS Regions that support Kinesis Data Streams](../../../general/latest/gr/rande.md#ak_region "../../../general/latest/gr/rande.md#ak_region").

###### Tasks

- [Complete prerequisites](tutorial-stock-data-kplkcl-begin.md "tutorial-stock-data-kplkcl-begin.md")
- [Create a data stream](tutorial-stock-data-kplkcl-create-stream.md "tutorial-stock-data-kplkcl-create-stream.md")
- [Create an IAM policy and user](tutorial-stock-data-kplkcl-iam.md "tutorial-stock-data-kplkcl-iam.md")
- [Download and build the
  implementation code](tutorial-stock-data-kplkcl-download.md "tutorial-stock-data-kplkcl-download.md")
- [Implement the producer](tutorial-stock-data-kplkcl-producer.md "tutorial-stock-data-kplkcl-producer.md")
- [Implement the consumer](tutorial-stock-data-kplkcl-consumer.md "tutorial-stock-data-kplkcl-consumer.md")
- [(Optional) Extend the
  consumer](tutorial-stock-data-kplkcl-consumer-extension.md "tutorial-stock-data-kplkcl-consumer-extension.md")
- [Clean up resources](tutorial-stock-data-kplkcl-finish.md "tutorial-stock-data-kplkcl-finish.md")
