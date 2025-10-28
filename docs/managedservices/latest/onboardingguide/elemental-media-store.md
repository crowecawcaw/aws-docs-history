# Use AMS SSP to provision AWS Elemental MediaStore in your AMS account

###### Note

After careful consideration, AWS has made the decision to discontinue MediaStore, effective November 13, 2025. If you are an active customer of
MediaStore, you can use MediaStore as normal until November 13, 2025, when support for the service will end. After this date, you will no longer be able to use
MediaStore or any of the capabilities provided by this service.

Use AMS Self-Service Provisioning (SSP) mode to access AWS Elemental MediaStore capabilities directly in your AMS managed account. AWS Elemental MediaStore is an AWS storage service optimized for media. It gives you the performance, consistency, and
low latency required to deliver live streaming video content. AWS Elemental MediaStore acts as the origin store in your
video workflow. Its high performance capabilities meet the needs of the most demanding media delivery
workloads, combined with long-term, cost-effective storage.
To learn more, see [AWS Elemental MediaStore](https://aws.amazon.com/mediastore/ "https://aws.amazon.com/mediastore/").

## MediaStore in AWS Managed Services FAQ

**Q: How do I request access to MediaStore in my AMS account?**

Request access to MediaStore by submitting an RFC with the Management | AWS
service | Self-provisioned service | Add (ct-1w8z66n899dct) change type.
This RFC provisions the following IAM role to your account:
`customer_mediastore_author_role`. As a part of this RFC, a
second role is deployed into your account; `MediaStoreAccessLogs`
role, which is used by the MediaStore service to log activity in CloudWatch, if
you choose to enable that feature. After it's provisioned in your account,
you must onboard the roles in your federation solution.

At this time, AMS Operations will also deploy this service role in your account:
`aws_code_pipeline_service_role_policy`.

**Q: What are the restrictions to using MediaStore in my AMS account?**

There are no restrictions for the use of MediaStore in AMS.

**Q: What are the prerequisites or dependencies to using MediaStore in my AMS account?**

There are no prerequisites or dependencies to use MediaStore in your AMS account.
