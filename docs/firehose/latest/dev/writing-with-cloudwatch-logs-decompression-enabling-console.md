# Enable decompression

on a new Firehose stream from console

###### To enable decompression on a new Firehose stream using the AWS Management Console

1. Sign in to the AWS Management Console and open the Kinesis console at
   [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
2. Choose **Amazon Data Firehose** in the navigation pane.
3. Choose **Create Firehose stream**.
4. Under **Choose source and destination**

\***\*Source\*\***

The source of your Firehose stream. Choose one of the following sources:

    * **Direct PUT** –
     Choose this option to create a Firehose stream that producer
     applications write to directly. For a list of AWS
     services and agents and open source services that are
     integrated with Direct PUT in Firehose, see [this](create-name.md "create-name.md") section.
    * **Kinesis stream:** Choose this
     option to configure a Firehose stream that uses a Kinesis data stream as
     a data source. You can then use Firehose to read data easily from
     an existing Kinesis data stream and load it into destinations. For more information, see [Writing to Firehose Using Kinesis Data Streams](writing-with-kinesis-streams.md "writing-with-kinesis-streams.md")

\***\*Destination\*\***

The destination of your Firehose stream. Choose one of the following:

    * Amazon S3
    * Splunk

5. Under **Firehose stream name**, enter a name for your stream.
6. (Optional) Under **Transform records**:
   - In the **Decompress source records from Amazon CloudWatch Logs** section, choose **Turn on decompression**.
   - If you want to use message extraction after decompression, choose **Turn on message extraction**.
