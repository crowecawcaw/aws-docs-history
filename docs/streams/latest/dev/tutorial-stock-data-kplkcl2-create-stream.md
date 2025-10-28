# Create a data stream

First, you must create the data stream that you will use in subsequent steps of this
tutorial.

###### To create a stream

1. Sign in to the AWS Management Console and open the Kinesis console at
   [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
2. Choose **Data Streams** in the navigation pane.
3. In the navigation bar, expand the Region selector and choose a Region.
4. Choose **Create Kinesis stream**.
5. Enter a name for your data stream (for example,
   `StockTradeStream`).
6. Enter `1` for the number of shards, but keep
   **Estimate the number of shards you'll need**
   collapsed.
7. Choose **Create Kinesis stream**.
   On the **Kinesis streams** list page, the status of your stream appears
   as `CREATING` while the stream is being created. When the stream is ready to
   use, the status changes to `ACTIVE`.

If you choose the name of your stream, in the page that appears, the
**Details** tab displays a summary of your data stream
configuration. The **Monitoring** section displays monitoring
information for the stream.

## Next steps

[Create an IAM policy and
user](tutorial-stock-data-kplkcl2-iam.md "tutorial-stock-data-kplkcl2-iam.md")
