

# Create an Amazon Kinesis video stream
<a name="gs-createstream"></a>

This section describes how to create a Kinesis video stream.

This section contains the following procedures:
+ [Create a video stream using the console](#gs-createstream-console)
+ [Create a video stream using the AWS CLI](#gs-createstream-cli)

## Create a video stream using the console
<a name="gs-createstream-console"></a>

1. Open the console at [https://console.aws.amazon.com/kinesisvideo/home](https://console.aws.amazon.com/kinesisvideo/home).

1. On the **Video streams** page, choose **Create video stream**.

1. On the **Create a new video stream** page, enter {{YourStreamName}} for the stream name. Leave the **Default configuration** button selected. 

1. Choose **Create video stream**.

1. After Amazon Kinesis Video Streams creates the stream, review the details on the **YourStreamName** page.

## Create a video stream using the AWS CLI
<a name="gs-createstream-cli"></a>

1. Verify that you have the AWS CLI installed and configured. For more information, see the [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/) documentation.

1. Run the following `Create-Stream` command in the AWS CLI: 

   ```
   aws kinesisvideo create-stream --stream-name "{{YourStreamName}}" --data-retention-in-hours 24
   ```

   The response will look similar to the following:

   ```
   {
       "StreamARN": "arn:aws:kinesisvideo:{{us-west-2}}:{{123456789012}}:stream/{{YourStreamName}}/{{123456789012}}"
   }
   ```