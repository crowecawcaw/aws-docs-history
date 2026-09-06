

# Disable decompression on Firehose stream
<a name="writing-with-cloudwatch-logs-decompression-disabling-console"></a>

To disable decompression on a data stream using the AWS Management Console

1. Sign in to the AWS Management Console and open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. Choose **Amazon Data Firehose** in the navigation pane.

1. Choose the Firehose stream you wish to edit.

1. On **Firehose stream details** page, choose the **Configuration** tab.

1. In the **Transform and convert records** section, choose **Edit**.

1. Under **Decompress source records from Amazon CloudWatch Logs**, clear **Turn on decompression** and then choose **Save changes**.