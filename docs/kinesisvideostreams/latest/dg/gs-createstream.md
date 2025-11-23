# Create an Amazon Kinesis video stream

This section describes how to create a Kinesis video stream.

This section contains the following procedures:

- [Create a video stream using the console](#gs-createstream-console "#gs-createstream-console")
- [Create a video stream using the AWS CLI](#gs-createstream-cli "#gs-createstream-cli")

## Create a video stream using the console

1. Open the console at [https://console.aws.amazon.com//kinesisvideo/home](https://console.aws.amazon.com//kinesisvideo/home "https://console.aws.amazon.com//kinesisvideo/home").
2. On the **Video streams** page, choose
   **Create video stream**.
3. On the **Create a new video stream** page, enter
   `YourStreamName` for
   the stream name. Leave the **Default configuration** button
   selected.
4. Choose **Create video stream**.
5. After Amazon Kinesis Video Streams creates the stream, review the details on the
   **YourStreamName** page.

## Create a video stream using the AWS CLI

1. Verify that you have the AWS CLI installed and configured. For more information, see the [AWS Command Line Interface](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") documentation.
2. Run the following `Create-Stream` command in the AWS CLI:

```
aws kinesisvideo create-stream --stream-name "`YourStreamName`" --data-retention-in-hours 24
```

The response will look similar to the following:

```
{
    "StreamARN": "arn:aws:kinesisvideo:`us-west-2`:`123456789012`:stream/`YourStreamName`/`123456789012`"
}
```
