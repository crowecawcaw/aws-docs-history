

# Video Stream from Cloud to Satellite and Internet
<a name="video-stream-cloud-satellite-internet"></a>

Publication date: **March 28, 2023 ([Diagram history](#video-sat-history))**

With this architecture, you can build a highly reliable, available, scalable, and secure video workflow with AWS managed services. The solution uses [AWS Elemental MediaConnect](https://docs.aws.amazon.com/mediaconnect/latest/ug/) and [AWS Elemental MediaLive](https://docs.aws.amazon.com/medialive/latest/ug/) to distribute high-quality video content over satellite and internet.

## Video stream from cloud to satellite diagram
<a name="video-sat-diagram"></a>

![Reference architecture diagram showing how to build a cloud-based video headend by using AWS Elemental MediaConnect, AWS Elemental MediaLive, CloudFront, and IAM.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/video-stream-cloud-satellite-internet/images/video-stream-cloud-satellite-internet.png)


The following steps describe the data flow and key configuration points for this architecture:

1. Ingest video streams into the AWS Cloud by using AWS Direct Connect. AWS Elemental MediaConnect supports multiple streaming protocols and can also be sourced through MediaConnect entitlements granted by other AWS accounts. MediaConnect supports the private Elastic IP address from your Amazon VPC.

1. Use [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/) roles with appropriate policies and [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/) to store the passwords to decrypt the video stream.

1. Forward the video stream to AWS Elemental MediaLive to transcode the Single Program Transport Stream (SPTS).

1. Use AWS Elemental MediaLive StatMux to multiplex multiple SPTS streams and deliver a single Multiple Program Transport Stream (MPTS) through AWS Elemental MediaConnect.

1. Deliver the single MPTS stream by using AWS Direct Connect from the AWS Region to the satellite teleport.

1. Uplink the MPTS stream by using the Digital Video Broadcast (DVB S/S2) standard to the satellite with C-Band or Ku Band frequencies.

1. Monitor the quality of your video streams by using customized dashboards on [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

1. Configure alarm thresholds to monitor alarms and send notifications to operators by using [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/).

1. Use [AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/) and AWS Elemental MediaTailor to deliver video on demand through a streaming application.

1. Use [AWS Elemental MediaConvert](https://docs.aws.amazon.com/mediaconvert/latest/ug/) to deliver video on demand from [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Run the Over The Top (OTT) streaming application in [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) containers.

1. Use [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/) for user authentication and authorization to manage user subscriptions to the OTT streaming service.

1. Use [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) to deliver a low-latency, high-speed video viewing experience to end users on the streaming application.

## Further reading
<a name="video-sat-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="video-sat-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#video-sat-history) | Reference architecture diagram first published. | March 28, 2023 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.