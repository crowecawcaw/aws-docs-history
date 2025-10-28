# Use AMS SSP to provision Amazon Kinesis Video Streams in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Kinesis Video Streams (KVS) capabilities directly in your AMS managed account. Amazon Kinesis Video Streams helps you to securely stream video from connected devices to AWS for analytics, machine learning (ML), playback,
and other processing. Kinesis Video Streams automatically provisions, and elastically scales, all the infrastructure needed to ingest
streaming video data from millions of devices. It also durably stores, encrypts, and indexes video data in your streams,
and allows you to access your data through easy-to-use APIs. Kinesis Video Streams enables you to playback video for live and on-demand viewing,
and quickly build applications that take advantage of computer vision and video analytics through integration with Amazon Rekognition Video,
and libraries for ML frameworks such as Apache MxNet, TensorFlow, and OpenCV. To learn more, see
[Amazon Kinesis Video Streams](https://aws.amazon.com/kinesis/video-streams/ "https://aws.amazon.com/kinesis/video-streams/").

## Amazon Kinesis Video Streams in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Amazon Kinesis Video Streams in my AMS account?**

Request access to Amazon Kinesis Video Streams by submitting an RFC with the Management |
AWS service | Self-provisioned service | Add change type (ct-1w8z66n899dct).
This RFC provisions the following IAM role to your account:
`customer_kinesis_video_streaming_user_role`. After it's
provisioned in your account, you must onboard the role in your federation
solution.

**Q: What are the restrictions to using Amazon Kinesis Video Streams in my AMS account?**

There are no restrictions. Full functionality of Amazon Kinesis Video Streams is available in your AMS account.

**Q: What are the prerequisites or dependencies to using Amazon Kinesis Video Streams in my AMS account?**

There are no prerequisites or dependencies to use Amazon Kinesis Video Streams in your AMS account.
