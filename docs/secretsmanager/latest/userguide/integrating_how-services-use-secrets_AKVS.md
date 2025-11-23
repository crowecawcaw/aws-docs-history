# How Amazon Kinesis Video Streams uses

AWS Secrets Manager

You can use Amazon Kinesis Video Streams to connect to IP cameras on customer premises, locally record
and store video from the cameras, and stream videos to the cloud for long-term storage,
playback, and analytical processing. To record and upload media from IP cameras, you
deploy the Kinesis Video Streams Edge Agent to AWS IoT Greengrass. You store the credentials required to access the
media files that are streamed to the camera in an Secrets Manager secret. For more information,
see [Deploy the Amazon Kinesis Video Streams Edge Agent to AWS IoT Greengrass](../../../kinesisvideostreams/latest/dg/gs-edge-gg.md "../../../kinesisvideostreams/latest/dg/gs-edge-gg.md") in the _Amazon Kinesis Video Streams
Developer Guide_.
