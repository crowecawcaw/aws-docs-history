# Create a signaling channel

A Kinesis Video Streams with WebRTC signaling channel facilitates the exchange of signaling messages
required to establish and maintain peer-to-peer connections between WebRTC clients. It
handles the negotiation of Session Description Protocol (SDP) offers and answers for
session parameters, as well as the exchange of Interactive Connectivity Establishment
(ICE) candidates for network information.

To create a signaling channel, call the [CreateSignalingChannel](../../../kinesisvideostreams/latest/dg/API_CreateSignalingChannel.md "../../../kinesisvideostreams/latest/dg/API_CreateSignalingChannel.md") API. This page will show you how to invoke that API
using the AWS Management Console, AWS CLI, and one of the AWS SDKs.

###### Important

Make note of the channel ARN, you'll need it later.

AWS Management Console
Do the following:

1. Open the **Kinesis Video Streams Signaling
   Channels** console at [https://console.aws.amazon.com/kinesisvideo/home/#/signalingChannels](https://console.aws.amazon.com/kinesisvideo/home/#/signalingChannels "https://console.aws.amazon.com/kinesisvideo/home/#/signalingChannels").
2. Choose **Create signaling channel**.
3. On the **Create a new signaling channel** page,
   type the name for the signaling channel.

Leave the default **Time-to-live (Ttl)** value as
60 seconds.

Choose **Create signaling channel**. 4. Once the signaling channel is created, review the details on the
channel's details page.

AWS CLI
Verify that you have the AWS CLI installed and configured. For more
information, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

For installation instructions, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions "../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions"). After installation,
[configure the AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new "../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new") with credentials and region.

Alternatively, open the AWS CloudShell terminal, which has the AWS CLI
installed and configured. See the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md#how-to-get-started "../../../cloudshell/latest/userguide/welcome.md#how-to-get-started") for more information.

Run the following [Create-Signaling-Channel](../../../cli/latest/reference/kinesisvideo/create-signaling-channel.md "../../../cli/latest/reference/kinesisvideo/create-signaling-channel.md") command using the AWS CLI:

```
aws kinesisvideo create-signaling-channel \
  --channel-name "`YourChannelName`" \
  --region "`us-west-2`"
```

The response will look like the following:

```
{
    "ChannelARN": "arn:aws:kinesisvideo:`us-west-2`:`123456789012`:channel/`YourChannelName`/`1234567890123`"
}
```

AWS SDK
This code snippet shows you how to create a Kinesis Video Streams with
WebRTC signaling channel using the AWS SDK for JavaScript v2. The syntax
will differ from other AWS SDKs, but the general flow will be
the same. View a complete code example on [GitHub](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/createSignalingChannel.js "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/createSignalingChannel.js").

Create the Kinesis Video Streams client. This is the client used to
call the `CreateSignalingChannel` API.

```
const clientConfig = {
    accessKeyId: '`YourAccessKey`',
    secretAccessKey: '`YourSecretKey`',
    region: '`us-west-2`'
};
const kinesisVideoClient = new AWS.KinesisVideo(clientConfig);
```

Use the client to call the `CreateSignalingChannel` API.

```
const createSignalingChannelResponse = await kinesisVideoClient
    .createSignalingChannel({
        ChannelName: '`YourChannelName`',
    })
    .promise();
```

Print the response.

```
console.log(createSignalingChannelResponse.ChannelARN);
```

The live web page with this code sample is available for use on [GitHub](https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html "https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html"). Input your region, AWS credentials, and the name of
your signaling channel.

Select **Create Channel**.
