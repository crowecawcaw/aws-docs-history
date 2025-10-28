# Use AMS SSP to provision AWS Elemental MediaLive in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Elemental MediaLive capabilities directly in your AMS managed account. AWS Elemental MediaLive is a broadcast-grade live video processing service. It enables you to create high-quality
video streams for delivery to broadcast televisions and internet-connected multiscreen devices,
like connected TVs, tablets, smartphones, and set-top boxes. The service works by encoding your
live video streams in real-time, taking a larger-sized live video source and compressing it into
smaller versions for distribution to your viewers. With AWS Elemental MediaLive, you can easily
set up streams for both live events and 24x7 channels with advanced broadcasting features, high
availability, and pay-as-you-go pricing. AWS Elemental MediaLive lets you focus on creating compelling
live video experiences for your viewers without the complexity of building and operating
broadcast-grade video processing infrastructure.

To learn more, see [AWS Elemental MediaLive](https://aws.amazon.com/medialive/ "https://aws.amazon.com/medialive/").

## MediaLive in AWS Managed Services FAQ

**Q: How do I request access to MediaLive in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account:
`customer_medialive_author_role`.

As a part of this RFC, a second role is deployed into your account;
`customer_medialive_service_role` role, this role can be
assigned to your Media Live channels and inputs to interact with other
services such as Amazon S3, MediaStore, and CloudWatch Logs.

After the roles are provisioned in your account, you must onboard the
roles in your federation solution.

**Q: What are the restrictions to using MediaLive in my AMS account?**

There are no restrictions for the use of MediaLive in AMS.

**Q: What are the prerequisites or dependencies to using MediaLive in my AMS account?**

There are no prerequisites or dependencies to use MediaLive in your AMS account.
