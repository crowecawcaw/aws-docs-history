# Authenticating requests to Amazon S3 with SigV4

Signature Version 4 (SigV4) for Amazon S3 is a signing protocol used to authenticate
requests to Amazon S3 over HTTPS. When you use SigV4 for Amazon S3, MediaTailor includes
a signed authorization header in the HTTPS request to the Amazon S3 bucket used as your
origin. If the signed authorization header is valid, your origin fulfills the
request. If it isn't valid, the request fails.

For general information about SigV4 for AWS Key Management Service, see the [Authenticating
Requests (AWS Signature Version 4)](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md") topic in the _Amazon S3 API reference_.

###### Note

MediaTailor always signs requests to these origins with SigV4.

## Requirements

If you activate SigV4 for Amazon S3 authentication for your source
location, you must meet these requirements:

- You must allow MediaTailor to access your Amazon S3 bucket by granting
  **mediatailor.amazonaws.com** principal access in
  IAM. For information about configuring access in IAM, see [Access
  management](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the _AWS Identity and Access Management User
  Guide_.
- The **mediatailor.amazonaws.com** service principal
  must have permissions to read all multivariant playlists referenced by the
  VOD source package configurations.
- The caller of the API must have **s3:GetObject** IAM
  permissions to read all multivariant playlists referenced by your MediaTailor VOD
  source package configurations.
- Your MediaTailor source location base URL must follow the Amazon S3 virtual
  hosted-style request URL format. For example,
  https://`bucket-name`.s3.`Region`.amazonaws.com/`key-name`.
  For information about Amazon S3 hosted virtual-style access, see [Virtual Hosted-Style Requests](../../../AmazonS3/latest/userguide/VirtualHosting.md#virtual-hosted-style-access "../../../AmazonS3/latest/userguide/VirtualHosting.md#virtual-hosted-style-access").
