# Connect to the storage session

Follow these procedures to create the storage session and start the WebRTC connection
process. The master participant should call [JoinStorageSession](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md"). Viewer participants
should call [JoinStorageSessionAsViewer](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md").

This will have the storage session send an SDP offer and ICE candidates through
signaling to the master participant connected through [ConnectAsMaster](ConnectAsMaster.md "ConnectAsMaster.md"), or the
specified viewer participant connected through [ConnectAsViewer](ConnectAsViewer.md "ConnectAsViewer.md").

1. Obtain the ARN of the signaling channel, as it is a required input for the next step. If you already know the ARN, continue with the next step.

AWS Management Console 1. Open the [Kinesis Video Streams Signaling Channels console](https://console.aws.amazon.com/kinesisvideo/home/#/signalingChannels "https://console.aws.amazon.com/kinesisvideo/home/#/signalingChannels"). 2. Choose the name of your signaling channel. 3. Under the **Signaling channel info** tab, locate the ARN for your signaling channel.

AWS CLIVerify that you have the AWS CLI installed and configured. For more
information, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

For installation instructions, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions "../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions"). After installation,
[configure the AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new "../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new") with credentials and region.

Alternatively, open the AWS CloudShell terminal, which has the AWS CLI
installed and configured. See the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md#how-to-get-started "../../../cloudshell/latest/userguide/welcome.md#how-to-get-started") for more information.

Run the following [Describe-Signaling-Channel](../../../cli/latest/reference/kinesisvideo/describe-signaling-channel.md "../../../cli/latest/reference/kinesisvideo/describe-signaling-channel.md") command using the
AWS CLI:

```
aws kinesisvideo describe-signaling-channel \
  --channel-name "`YourChannelName`" \
```

The response will look like the following:

```
{
    "ChannelInfo": {
        "ChannelName": "`YourChannelName`",
        "ChannelARN": "arn:aws:kinesisvideo:`us-west-2`:`123456789012`:channel/`YourChannelName`/`1234567890123`",
        "ChannelType": "SINGLE_MASTER",
        "ChannelStatus": "ACTIVE",
        "CreationTime": "`2024-07-07T23:28:24.941000-07:00`",
        "SingleMasterConfiguration": {
        "MessageTtlSeconds": 60
    },
    "Version": "`Ws0fZvFGXzEpuZ2CE1s9`"
    }
}

```

You'll find the signaling channel ARN in the `ChannelInfo` object.

AWS SDKThis code snippet shows you how to create a Kinesis Video Streams with WebRTC signaling channel using the
AWS SDK for JavaScript v2. The syntax will differ from other AWS
SDKs, but the general flow will be the same.

You can view the complete code example for [JoinStorageSession](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/joinStorageSession.js "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/joinStorageSession.js")
or [JoinStorageSessionAsViewer](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/joinStorageSessionAsViewer.js "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/joinStorageSessionAsViewer.js").

Create the Kinesis Video Streams client. This is used to call the [DescribeSignalingChannel API](../../../kinesisvideostreams/latest/dg/API_DescribeSignalingChannel.md "../../../kinesisvideostreams/latest/dg/API_DescribeSignalingChannel.md").

```
const clientConfig = {
    accessKeyId: '`YourAccessKey`',
    secretAccessKey: '`YourSecretKey`',
    region: '`us-west-2`'
};
const kinesisVideoClient = new AWS.KinesisVideo(clientConfig);
```

Use the client to call the `DescribeSignalingChannel` API.

```
const describeSignalingChannelResponse = await kinesisVideoClient
    .describeSignalingChannel({
        ChannelName: '`YourChannelName'`,
    })
    .promise();
```

Save the response.

```
const channelARN =
    describeSignalingChannelResponse.ChannelInfo.ChannelARN;
```

2. Obtain the WEBRTC endpoint. Requests to [JoinStorageSession](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md") or
   [JoinStorageSessionAsViewer](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md") for a particular signaling channel must be made
   to its designated endpoint.

AWS Management Console

###### Note

This operation isn't currently supported in the Kinesis Video Streams
AWS Management Console.

Open the AWS CloudShell terminal, which has the AWS CLI installed and configured.
See the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md#how-to-get-started "../../../cloudshell/latest/userguide/welcome.md#how-to-get-started") for more information.

Follow the instructions in the AWS CLI tab.

AWS CLI
Verify that you have the AWS CLI installed and configured. For more
information, see the [AWS Command Line Interface](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") documentation.

For installation instructions, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions "../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions"). After installation,
[configure the AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new "../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new") with credentials and region.

Alternatively, open the AWS CloudShell terminal, which has the AWS CLI
installed and configured. See the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md#how-to-get-started "../../../cloudshell/latest/userguide/welcome.md#how-to-get-started") for more information.

Run the `Get-Signaling-Channel-Endpoint` command in the
AWS CLI:

```
aws kinesisvideo get-signaling-channel-endpoint \
  --channel-arn "arn:aws:kinesisvideo:`us-west-2`:`123456789012`:channel/`YourChannelName`/`1234567890123`" \
  --single-master-channel-endpoint-configuration "Protocols=['WEBRTC'],Role=`MASTER`" \
  --region "`us-west-2`"
```

The response looks similar to the following:

```
{
    "ResourceEndpointList": [
        {
            "Protocol": "WEBRTC",
            "ResourceEndpoint": "https://w-`abcd1234`.kinesisvideo.`aws-region`.amazonaws.com"
        }
    ]
}

```

AWS SDK
This code snippet shows you how to call the
`GetSignalingChannelEndpoint` API for a Kinesis Video Streams with
WebRTC signaling channel using the AWS SDK for JavaScript v2. The
syntax will differ from other AWS SDKs, but the general flow will
be the same. View a complete code example for [JoinStorageSession](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/joinStorageSession.js "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/joinStorageSession.js") or [JoinStorageSessionAsViewer](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/joinStorageSessionAsViewer.js "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/joinStorageSessionAsViewer.js").

Create the Kinesis Video Streams client. This is the client used to call the
[DescribeSignalingChannel API](../../../kinesisvideostreams/latest/dg/API_DescribeSignalingChannel.md "../../../kinesisvideostreams/latest/dg/API_DescribeSignalingChannel.md").

If you
created a Kinesis Video Streams client earlier to call
`DescribeSignalingChannel`, you can reuse the same
client.

```
const clientConfig = {
    accessKeyId: '`YourAccessKey`',
    secretAccessKey: '`YourSecretKey`',
    region: '`us-west-2`'
};
const kinesisVideoClient = new AWS.KinesisVideo(clientConfig);
```

Use the client to call the `GetSignalingChannelEndpoint` API.

```
const getSignalingChannelEndpointResponse = await kinesisVideoClient
    .getSignalingChannelEndpoint({
        ChannelARN: `channelARN`,
        SingleMasterChannelEndpointConfiguration: {
            Protocols: ['WEBRTC'],
            Role: '`MASTER'`,
        },
    })
    .promise();
```

Save the response:

```
const webrtcEndpoint = getSignalingChannelEndpointResponse.ResourceEndpointList[0].ResourceEndpoint;
```

3. Use the channel ARN and WEBRTC endpoints to make the API call. If the participants are
   correctly connected to Kinesis Video Streams with WebRTC Signaling via the
   `ConnectAsMaster` or `ConnectAsViewer` WebSocket APIs, an SDP offer and a stream of
   ICE candidate messages will be sent along the WebSocket from the storage session
   to the participants.

AWS Management Console

###### Note

This operation isn't currently supported in the Kinesis Video Streams
AWS Management Console.

Open the AWS CloudShell terminal, which has the AWS CLI installed and
configured. See the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md#how-to-get-started "../../../cloudshell/latest/userguide/welcome.md#how-to-get-started") for more information.

Follow the instructions in the AWS CLI tab.

AWS CLI
Verify that you have the AWS CLI installed and configured. For more
information, see the [AWS Command Line Interface](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md")
documentation.

For installation instructions, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions "../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions"). After installation, [configure the AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new "../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new") with credentials and region.

Alternatively, open the AWS CloudShell terminal, which has the AWS CLI
installed and configured. See the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md#how-to-get-started "../../../cloudshell/latest/userguide/welcome.md#how-to-get-started") for more information.

Run the `Join-Storage-Session` command for master
participants in the AWS CLI using the channel ARN and WEBRTC endpoint
from previous steps:

```
aws kinesis-video-webrtc-storage join-storage-session \
  --endpoint-url https://w-`abcd1234`.kinesisvideo.`us-west-2`.amazonaws.com \
  --channel-arn arn:aws:kinesisvideo:`us-west-2`:`123456789012`:channel/`YourChannelName`/`1234567890123` \
  --region "`us-west-2`"
```

After a successful run, an empty response is returned and nothing is
printed.

In the case of a viewer participant, run the following
`Join-Storage-Session-As-Viewer` command in the AWS CLI
using the channel ARN and WEBRTC endpoint from before:

```
aws kinesis-video-webrtc-storage join-storage-session-as-viewer \
  --endpoint-url https://w-`abcd1234`.kinesisvideo.`us-west-2`.amazonaws.com \
  --channel-arn arn:aws:kinesisvideo:`us-west-2`:`123456789012`:channel/`YourChannelName`/`1234567890123` \
  --client-id "`ExampleViewerClientID`"
  --region "`us-west-2`"
```

After a successful run, an empty response is returned and nothing is printed.

AWS SDK
This code snippet shows you how to call the
`JoinStorageSession` or
`JoinStorageSessionAsViewer` API for a Kinesis Video Streams with
WebRTC signaling channel using the AWS SDK for JavaScript v2. The
syntax will differ from other AWS SDKs, but the general flow will
be the same. View a complete code example for [JoinStorageSession](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/joinStorageSession.js "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/joinStorageSession.js") or [JoinStorageSessionAsViewer](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/joinStorageSessionAsViewer.js "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/joinStorageSessionAsViewer.js").

Create the Kinesis Video Streams WebRTC storage client. This is the client used
to call `JoinStorageSession` or
`JoinStorageSessionAsViewer` and is different than
the Kinesis Video Streams client created in earlier steps.

```
const webrtcStorageClientConfig = {
    accessKeyId: '`YourAccessKey`',
    secretAccessKey: '`YourSecretKey`',
    region: '`us-west-2`',
    endpoint: `webrtcEndpoint`
};
const kinesisVideoWebRTCStorageClient = new AWS.KinesisVideoWebRTCStorage(clientConfig);
```

Use the client to call the `JoinStorageSession` API for
master participants.

```
await kinesisVideoWebRTCStorageClient
    .joinStorageSession({
        channelArn: `channelARN`,
    })
    .promise();
```

In the case of a viewer participant, use the client to call the
`JoinStorageSessionAsViewer` API.

```
await kinesisVideoWebRTCStorageClient
    .joinStorageSessionAsViewer({
        channelArn: `channelARN`,
        clientId: "`ExampleViewerClientID`",
    })
    .promise();
```

The live web page with this code sample is available on [GitHub](https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html "https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html"). Input your region, AWS credentials, and the name of your signaling channel. Expand the **WebRTC
Ingestion and Storage** node, and uncheck
**Automatically determine ingestion mode**.

Switch the manual override to **ON** and select
**Show button to manually call JoinStorageSession
API** and/or **Show button to manually call
JoinStorageSessionAsViewer API**.

When you select **Start Master** or
**Start Viewer**, after the application
connects to signaling via `ConnectAsMaster` or
`ConnectAsViewer`, a button will appear to have the
storage session initiate the WebRTC connection with the peer instead
of the application calling the API immediately after connecting to
signaling.
