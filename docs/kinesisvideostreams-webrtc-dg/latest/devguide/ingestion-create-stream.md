# Create a video stream

Follow these procedures to create a stream that the media will be ingested to. If you have already created the destination stream, skip this
step.

###### Important

WebRTC Ingestion requires a Kinesis video stream with data retention greater than 0. The
minimum is 1 hour.

To create a stream, call the [CreateStream](../../../kinesisvideostreams/latest/dg/API_CreateStream.md "../../../kinesisvideostreams/latest/dg/API_CreateStream.md") API using the
AWS Management Console, AWS CLI, or one of the AWS SDK’s.

###### Important

Make note of the stream ARN, you'll need it later.

AWS Management Console
Do the following:

1. Open the **Kinesis Video Streams** console at
   [https://console.aws.amazon.com/kinesisvideo/home/](https://console.aws.amazon.com//kinesisvideo/home/ "https://console.aws.amazon.com//kinesisvideo/home/").
2. On the **Video streams** page, choose
   **Create video stream**.
3. On the **Create a new video stream** page,
   enter `YourStreamName` for the
   stream name. Leave the **Default configuration**
   button selected.

This will create a stream with a greater than 0 data
retention.

Choose **Create video stream**. 4. After Kinesis Video Streams creates the stream, review the details on the
`YourStreamName`
page.

AWS CLI
Verify that you have the AWS CLI installed and configured. For more
information, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

For installation instructions, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions "../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions"). After installation,
[configure the AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new "../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new") with credentials and region.

Alternatively, open the AWS CloudShell terminal, which has the AWS CLI
installed and configured. See the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md#how-to-get-started "../../../cloudshell/latest/userguide/welcome.md#how-to-get-started") for more information.

Run the following `Create-Stream` command using the
AWS CLI:

```
aws kinesisvideo create-stream \
  --stream-name "`YourStreamName`" \
  --data-retention-in-hours `24` \
  --region "`us-west-2`"
```

The response will look like the following:

```
{
    "StreamARN": "arn:aws:kinesisvideo:`us-west-2`:`123456789012`:stream/`YourStreamName`/`1234567890123`"
}
```

AWS SDK
This code snippet shows you how to create a Kinesis video stream using the AWS
SDK for JavaScript v2. The syntax will differ from other AWS SDKs, but the
general flow will be the same. View a complete code example on [GitHub](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/createStream.js "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/createStream.js").

Create the Kinesis Video Streams client. This is the client used to call the
[CreateStream](../../../kinesisvideostreams/latest/dg/API_CreateStream.md "../../../kinesisvideostreams/latest/dg/API_CreateStream.md") API.

```
const clientConfig = {
    accessKeyId: '`YourAccessKey`',
    secretAccessKey: '`YourSecretKey`',
    region: '`us-west-2`'
};
const kinesisVideoClient = new AWS.KinesisVideo(clientConfig);
```

Use the client to call the `CreateStream` API.

```
const createStreamResponse = await kinesisVideoClient
    .createStream({
        StreamName: '`YourStreamName`',
        DataRetentionInHours: `48`,
    })
    .promise();
```

Print the response.

```
console.log(createStreamResponse.StreamARN);
```

The live web page with this code sample is available for use on [GitHub](https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html "https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html"). Input your region, AWS credentials, and the name of
your signaling channel.

Expand the **WebRTC Ingestion and Storage** node, type
the name of your stream, then choose **Create Stream**. A
pop-up asks for the number of hours you'd like to persist the stream's data.
Enter a value greater than 0, then choose **Create
Stream**.
