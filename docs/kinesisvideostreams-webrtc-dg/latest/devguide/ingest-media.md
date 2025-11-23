# Ingest media

The following limits are in place:

- **Session duration:** one hour,
  maximum
- **Signaling channels:** maximum of 100 per
  account with storage configuration enabled

###### Topics

- [Ingest media from a browser](#ingest-browser "#ingest-browser")
- [Ingest media from WebRTC C SDK](#ingest-webrtc-sdk "#ingest-webrtc-sdk")
- [Add viewers to the ingestion session](#ingest-add-viewers "#ingest-add-viewers")

## Ingest media from a browser

###### Important

Chrome is currently the only supported browser.

1.  Open the Amazon Kinesis Video Streams with WebRTC SDK in the JavaScript [sample page](https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html "https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html").
2.  Complete the following information:
    - **KVS Endpoint** - In the
      **Region** field, select your region.

    For example, `us-west-2`.
    - **AWS Credentials**

    Complete the following fields:

        + **Access Key ID**
        + **Secret Access Key**
        + **Session Token** - The sample
         application supports both temporary and long-term
         credentials. Leave this field blank if you're using
         long-term IAM credentials. See [Temporary security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") for
         more information.

    - **Signaling Channel** - In the **Channel Name** field, type
      the name of the signaling channel you configured earlier. For more
      information, see [Configure destination](configure-ingestion.md "configure-ingestion.md").
    - **Tracks** - Select **Send
      Video** and **Send Audio**.
    - **WebRTC Ingestion and Storage** - Expand the node and select
      **Automatically determine ingestion mode**.
      This option makes the sample application call the [DescribeMediaStorageConfiguration](../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md "../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md") API to determine in
      which mode to run.

3.  Select **Start Master**.

If the signaling channel is configured for ingestion using the [DescribeMediaStorageConfiguration](../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md "../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md") API, the sample application
will automatically invoke the [JoinStorageSession](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.md") API immediately after connecting to the
Signaling channel to start the WebRTC ingestion workflow.

## Ingest media from WebRTC C SDK

Follow the [Amazon Kinesis Video Streams with WebRTC SDK in C for embedded devices](kvswebrtc-sdk-c.md "kvswebrtc-sdk-c.md") procedures to build the sample
application.

1. Setup your environment with your AWS account credentials:

```
export AWS_ACCESS_KEY_ID=`YourAccessKey`
export AWS_SECRET_ACCESS_KEY=`YourSecretKey`
export AWS_DEFAULT_REGION=`YourAWSRegion`
```

If you're using temporary AWS credentials, also export your session token:

```
export AWS_SESSION_TOKEN=`YourSessionToken`
```

2. Run the samples:

**Master sample**

Navigate to the `build` folder and use "1" as the second
argument. Type:

```
./`samples`/kvsWebrtcClientMaster `channel-name` 1
```

**GStreamer master sample**

Navigate to the `build` folder and use "audio-video-storage" as
the second argument. Type:

```
./`samples`/kvsWebrtcClientMasterGstSample `channel-name` audio-video-storage `testsrc`
```

This starts WebRTC ingestion.

###### Note

Your supplied signaling channel must be configured for storage. Use the
[DescribeMediaStorageConfiguration](../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md "../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md") API to confirm.

## Add viewers to the ingestion session

Once the signaling channel is in WebRTC Ingestion mode, viewer participants no
longer connect directly to the master participant. Viewer participants connect
directly to the storage session. Viewer participants receive the media sent by the
master participants, and viewer participants can send back optional audio to the
master participant. Any audio sent back by viewers will be sent to all other peers
connected to the storage session and ingested to the Kinesis Video Stream, as long
as the master participant is connected to the storage session.

The following limits are in place:

- **Maximum number of viewers:** 3
- **Maximum time viewer participants can be connected to
  the storage session without a master participant present:** 3
  minutes

###### Important

If a viewer disconnects from the storage session (closes the peer connection), their quota
(viewer limit) remains consumed for 1 minute. During this 1-minute period, the viewer can
invoke this API with the same Client ID to rejoin the session without consuming an
additional viewer quota. After 1 minute, the viewer quota is released and available for
other viewers to join.

**Browser**

###### Important

Chrome is the only supported browser.

1.  Open another tab in the Amazon Kinesis Video Streams with WebRTC SDK in the JavaScript [sample page](https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html "https://awslabs.github.io/amazon-kinesis-video-streams-webrtc-sdk-js/examples/index.html"). All the information from the previous page will be
    automatically populated. If not, complete the following information:
    - **KVS Endpoint** - In the
      **Region** field, select your region.

    For example, `us-west-2`.
    - **AWS Credentials**

    Complete the following fields:

        + **Access Key ID**
        + **Secret Access Key**
        + **Session Token** - The sample
         application supports both temporary and long-term
         credentials. Leave this field blank if you're using
         long-term IAM credentials. See [Temporary security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") for
         more information.

    - **Signaling Channel** - In the **Channel
      Name** field, type the name of the signaling channel
      you configured earlier. For more information, see [Configure destination](configure-ingestion.md "configure-ingestion.md").
    - **Tracks** - Select **Send
      Audio**. Note that if **Send
      Video** is checked, it will automatically be unchecked
      when choosing **Start Viewer**.
    - **WebRTC Ingestion and Storage** - Expand the
      node and select **Automatically determine ingestion
      mode**. This option makes the sample application call
      the [DescribeMediaStorageConfiguration](../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md "../../../kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.md") API to determine in
      which mode to run.

2.  Select **Start Viewer**.

The application automatically calls the [JoinStorageSessionAsViewer](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md") API immediately after connecting to
the signaling channel to trigger an SDP offer send to the viewer from the
session.

###### Note

With peer-to-peer WebRTC, the viewer participant is the controlling peer and
the master participant is the controlled peer. In WebRTC ingestion mode, the
storage session is now the controlling peer. After connecting to signaling and
invoking [JoinStorageSessionAsViewer](../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md "../../../kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.md"), the viewer will need to respond to the
SDP offer and establish a connection to the storage session through
WebRTC.

###### Note

The storage session will only send `TURN` candidates. When nominating an ICE candidate pair from the perspective of participants, the remote candidate will always be of type `relay`.
