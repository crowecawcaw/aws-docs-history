

# Amazon Kinesis Video Streams in AWS GovCloud (US)
<a name="govcloud-kinesisvideo"></a>

Amazon Kinesis Video Streams makes it easy to securely stream video from connected devices to AWS for analytics, machine learning (ML), playback, and other processing. Kinesis Video Streams automatically provisions and elastically scales all the infrastructure needed to ingest streaming video data from millions of devices. It durably stores, encrypts, and indexes video data in your streams, and allows you to access your data through easy-to-use APIs. Kinesis Video Streams enables you to playback video for live and on-demand viewing, and quickly build applications that take advantage of computer vision and video analytics through integration with Amazon Rekognition Video, and libraries for ML frameworks such as Apache MxNet, TensorFlow, and OpenCV.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon Kinesis Video Streams differs
<a name="govcloud-diffs-31"></a>

The following differences apply to Amazon Kinesis Video Streams:
+ The following features are not yet available:
  + WebRTC Ingestion and Storage
  + Kinesis Video Streams Edge Agent
  + Kinesis Video Streams Multiviewer
+ Unencrypted STUN and TURN connections are not available.
+ The Amazon SNS `Publish` action has a default quota of 300 messages per second in the AWS GovCloud (US-East) and AWS GovCloud (US-West) regions. When notifications are enabled, one message is published per fragment per stream. If you need a higher quota limit for your account, request through the Service Quotas console.

## Documentation
<a name="govcloud-docs-70"></a>
+  [Kinesis Video Streams documentation](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html) 
+  [Kinesis Video Streams with WebRTC documentation](https://docs.aws.amazon.com/kinesisvideostreams-webrtc-dg/latest/devguide/webrtc-ingestion.html) 

## Export-controlled content
<a name="govcloud-itar-content-109"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ No data will leave the AWS GovCloud (US) Regions for this service.