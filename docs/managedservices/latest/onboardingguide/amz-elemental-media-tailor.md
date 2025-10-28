# Use AMS SSP to provision AWS Elemental MediaTailor in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Elemental MediaTailor capabilities directly in your AMS managed account. AWS Elemental MediaTailor lets video providers insert individually targeted advertising into their
video streams without sacrificing broadcast-level quality-of-service. With AWS Elemental MediaTailor,
viewers of your live or on-demand video each receive a stream that combines your content with ads
personalized to them. But unlike other personalized ad solutions, with AWS Elemental MediaTailor your
entire stream – video and ads – is delivered with broadcast-grade video quality to improve the experience
for your viewers. AWS Elemental MediaTailor delivers automated reporting based on both client and
server-side ad delivery metrics, to accurately measure advertising impressions and viewer behavior.
You can easily monetize unexpected high-demand viewing events with no up-front costs using
AWS Elemental MediaTailor. It also improves ad delivery rates, helping you make more money from every video,
and it works with a wider variety of content delivery networks, ad decision servers, and client devices.

To learn more, see [AWS Elemental MediaTailor](https://aws.amazon.com/mediatailor/ "https://aws.amazon.com/mediatailor/").

## MediaTailor in AWS Managed Services FAQ

**Q: How do I request access to MediaTailor in my AMS account?**

Request access to MediaTailor by submitting an RFC with the Management | AWS
service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM role to your account:
`customer-mediatailor-role`. After it's provisioned in your
account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using MediaTailor in my AMS account?**

There are no restrictions for the use of MediaTailor in AMS.

**Q: What are the prerequisites or dependencies to using MediaTailor in my AMS account?**

There are no prerequisites or dependencies to use MediaTailor in your AMS account.
