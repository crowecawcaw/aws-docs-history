# Use AMS SSP to provision AWS Elemental MediaConvert in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Elemental MediaConvert capabilities directly in your AMS managed account. AWS Elemental MediaConvert is a file-based video transcoding service with broadcast-grade features. It enables you to
create video-on-demand (VOD) content for broadcast and multiscreen delivery at scale.
The service combines advanced video and audio capabilities with a simple web services interface and
pay-as-you-go pricing. With AWS Elemental MediaConvert, you can focus on delivering compelling media
experiences without having to worry about the complexity of building and operating your own video
processing infrastructure.

To learn more, see [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/ "https://aws.amazon.com/mediaconvert/").

## MediaConvert in AWS Managed Services FAQ

**Q: How do I request access to MediaConvert in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account: `customer_mediaconvert_author_role`.
Once provisioned in your account, you must onboard the role in your federation solution.

A second role will be provided, `customer_MediaConvert_Default_Role`, that is used
by MediaConvert in order to read from the source S3 bucket and write the output to the destination
S3 bucket, and also to invoke the API gateway in case you need digital rights management (DRM).

**Q: What are the restrictions to using MediaConvert in my AMS account?**

There are no restrictions for the use of MediaConvert in AMS.

**Q: What are the prerequisites or dependencies to using MediaConvert in my AMS account?**

There are no prerequisites or dependencies to use MediaConvert in your AMS account.
