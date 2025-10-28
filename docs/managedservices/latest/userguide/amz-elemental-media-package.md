# Use AMS SSP to provision AWS Elemental MediaPackage in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS Elemental MediaPackage capabilities directly in your AMS managed account. AWS Elemental MediaPackage reliably prepares and protects your video for delivery over the internet. From a single video input,
AWS Elemental MediaPackage creates video streams formatted to play on connected TVs, mobile phones,
computers, tablets, and game consoles. It makes it easy to implement popular video features for viewers
(start-over, pause, rewind, and so on.), like those commonly found on DVRs. AWS Elemental MediaPackage can also
protect your content using Digital Rights Management (DRM). AWS Elemental MediaPackage scales automatically
in response to load, so your viewers will always get a great experience without you having to accurately
predict in advance the capacity you’ll need.

To learn more, see [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/ "https://aws.amazon.com/mediapackage/").

## MediaPackage in AWS Managed Services FAQ

**Q: How do I request access to AWS Elemental MediaPackage in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account:
`customer_mediapackage_author_role`. After it's provisioned
in your account, you must onboard the role in your federation
solution.

A second role will be provided, `customer_mediapackage_service_role`, that can be
assigned to your Media Live channels and inputs to interact with other services such as S3 and Secrets Manager.

**Q: What are the restrictions to using MediaPackage in my AMS account?**

There are no restrictions for the use of MediaPackage in AMS.

**Q: What are the prerequisites or dependencies to using MediaPackage in my AMS account?**

There are no prerequisites or dependencies to use MediaPackage in your AMS account.
