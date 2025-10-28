# Configure destination

Once you've created the Kinesis Video Streams resources, you need to tell the signaling channel which stream to save it to.

If you want to delete a signaling channel or stream, you must unlink them first. See [Unlink signaling channel and stream](#ingest-unlink "#ingest-unlink").

## Link signaling channel and stream

Use the [UpdateMediaStorageConfiguration](../../../kinesisvideostreams/latest/dg/API_UpdateMediaStorageConfiguration.md "../../../kinesisvideostreams/latest/dg/API_UpdateMediaStorageConfiguration.md") API and input the ARNs for the Kinesis Video Streams resources that you want to link.

###### Important

Once `StorageStatus` is enabled, direct peer-to-peer
(master-viewer) connections no longer occur. Peers connect directly to
the storage session. You must call the `JoinStorageSession`
API to trigger an SDP offer send and establish a connection between a
peer and the storage session.

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

Run the `Update-Media-Storage-Configuration` command in the
AWS CLI:

```
aws kinesisvideo update-media-storage-configuration \
  --channel-arn arn:aws:kinesisvideo:`us-west-2`:`123456789012`:channel/`YourChannelName`/`1234567890123` \
  --media-storage-configuration \
    StreamARN="arn:aws:kinesisvideo:`us-west-2`:`123456789012`:stream/`YourStreamName`/`1234567890123`",Status="ENABLED" \
  --region "`us-west-2`"
```

AWS SDK
This code snippet shows you how to configure the signaling channel to
ingest media to the specified Kinesis video stream using the AWS SDK for JavaScript
v2. The syntax will differ from other AWS SDKs, but the general flow will
be the same. View a complete code example on [GitHub](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/updateMediaStorageConfiguration.js "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/updateMediaStorageConfiguration.js").

Create the Kinesis Video Streams client. This is the client used to call the [UpdateMediaStorageConfiguration](../../../kinesisvideostreams/latest/dg/API_UpdateMediaStorageConfiguration.md "../../../kinesisvideostreams/latest/dg/API_UpdateMediaStorageConfiguration.md") API.

```
const clientConfig = {
    accessKeyId: '`YourAccessKey`',
    secretAccessKey: '`YourSecretKey`',
    region: '`us-west-2`'
};
const kinesisVideoClient = new AWS.KinesisVideo(clientConfig);
```

Use the client to call the `UpdateMediaStorageConfiguration`
API.

```
await kinesisVideoClient
    .updateMediaStorageConfiguration({
        ChannelARN: '`YourChannelARN`',
        MediaStorageConfiguration: {
            Status: 'ENABLED',
            StreamARN: '`YourStreamARN`',
        },
    })
    .promise();
```

The live web page with this code sample is available for use on [GitHub](https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html "https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html"). Input your region, AWS credentials, and the name of
your signaling channel.

Expand the **WebRTC Ingestion and Storage** node, type
the name of your stream, then choose **Update Media Storage
Configuration**. The channel will be configured to ingest media
to the specified stream.

## Unlink signaling channel and stream

###### Important

You can't delete a signaling channel or stream until they are unlinked from each
other.

If you don't want the signaling channel's media ingested to the stream, use the
[UpdateMediaStorageConfiguration](../../../kinesisvideostreams/latest/dg/API_UpdateMediaStorageConfiguration.md "../../../kinesisvideostreams/latest/dg/API_UpdateMediaStorageConfiguration.md") API to unlink the Kinesis Video Streams resources. After
the channel is unlinked, direct peer-to-peer connections can resume.

AWS Management Console

###### Note

This operation isn't currently supported in the Kinesis Video Streams AWS Management Console.

Open the AWS CloudShell terminal, which has the AWS CLI installed and configured.
See the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md#how-to-get-started "../../../cloudshell/latest/userguide/welcome.md#how-to-get-started") for more information.

Follow the instructions in the AWS CLI tab.

AWS CLI
Verify that you have the AWS CLI installed and configured. For more
information, see the [AWS Command Line Interface](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") documentation.

For installation instructions, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions "../../../cli/latest/userguide/getting-started-install.md#getting-started-install-instructions"). After installation, [configure the AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new "../../../cli/latest/userguide/getting-started-quickstart.md#getting-started-quickstart-new") with credentials and region.

Alternatively, open the AWS CloudShell terminal, which has the AWS CLI installed
and configured. See the [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md#how-to-get-started "../../../cloudshell/latest/userguide/welcome.md#how-to-get-started") for more information.

Run the `Update-Media-Storage-Configuration` command in the
AWS CLI:

```
aws kinesisvideo update-media-storage-configuration \
  --channel-arn arn:aws:kinesisvideo:`us-west-2`:`123456789012`:channel/`YourChannelName`/`1234567890123` \
  --media-storage-configuration \
    StreamARN="null",Status="DISABLED" \
  --region "`us-west-2`"
```

AWS SDK
This code snippet shows you how to configure the signaling channel to
ingest media to the specified Kinesis video stream using the AWS SDK for JavaScript
v2. The syntax will differ from other AWS SDKs, but the general flow will
be the same. View a complete code example on [GitHub](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/updateMediaStorageConfiguration.js "https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-js/blob/master/examples/updateMediaStorageConfiguration.js").

Create the Kinesis Video Streams client. This is the client used to call the [UpdateMediaStorageConfiguration](../../../kinesisvideostreams/latest/dg/API_UpdateMediaStorageConfiguration.md "../../../kinesisvideostreams/latest/dg/API_UpdateMediaStorageConfiguration.md") API.

```
const clientConfig = {
    accessKeyId: '`YourAccessKey`',
    secretAccessKey: '`YourSecretKey`',
    region: '`us-west-2`'
};
const kinesisVideoClient = new AWS.KinesisVideo(clientConfig);
```

Use the client to call the `UpdateMediaStorageConfiguration`
API.

```
await kinesisVideoClient
    .updateMediaStorageConfiguration({
        ChannelARN: '`YourChannelARN`',
        MediaStorageConfiguration: {
            Status: 'DISABLED',
            StreamARN: 'null',
        },
    })
    .promise();
```

The live web page with this code sample is available for use on [GitHub](https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html "https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html"). Input your region, AWS credentials, and the name of
your signaling channel.

Expand the **WebRTC Ingestion and Storage** node, verify
that the **Stream Name** field is empty, then choose
**Update Media Storage Configuration**. The channel
will no longer be configured to ingest media to the specified stream.
