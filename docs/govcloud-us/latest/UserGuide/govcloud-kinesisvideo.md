# Amazon Kinesis Video Streams in AWS GovCloud (US)

Amazon Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for analytics, machine learning (ML), playback, and other processing. Kinesis Video Streams automatically provisions and elastically scales all the infrastructure needed to ingest streaming video data from millions of devices. It durably stores, encrypts, and indexes video data in your streams, and allows you to access your data through easy-to-use APIs. Kinesis Video Streams enables you to playback video for live and on-demand viewing, and quickly build applications that take advantage of computer vision and video analytics through integration with Amazon Rekognition Video, and libraries for ML frameworks such as Apache MxNet, TensorFlow, and OpenCV.

## How Amazon Kinesis Video Streams differs for AWS GovCloud (US)

The following features are not yet supported in AWS GovCloud (US):

- Kinesis Video Streams with WebRTC
- Kinesis Video Streams Edge Agent

In addition, the Amazon SNS
`Publish` action has a default quota of 300 messages per second in the AWS GovCloud (US-East) and AWS GovCloud (US-West) regions. When notifications are enabled, one message is published per fragment per stream. If you need a higher quota limit for your account, request through the Service Quotas console.

## Documentation for Amazon Kinesis Video Streams

[Kinesis Video Streams documentation](../../../kinesisvideostreams/latest/dg/what-is-kinesis-video.md "../../../kinesisvideostreams/latest/dg/what-is-kinesis-video.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- No data will leave the AWS GovCloud (US) Regions for this service.
