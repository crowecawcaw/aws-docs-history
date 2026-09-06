

# Authenticating requests to Amazon S3 with SigV4
<a name="channel-assembly-access-configuration-sigv4"></a>

Signature Version 4 (SigV4) for Amazon S3 is a signing protocol used to authenticate requests to Amazon S3 over HTTPS. When you use SigV4 for Amazon S3, MediaTailor includes a signed authorization header in the HTTPS request to the Amazon S3 bucket used as your origin. If the signed authorization header is valid, your origin fulfills the request. If it isn't valid, the request fails.

 For general information about SigV4 for AWS Key Management Service, see the [Authenticating Requests (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) topic in the *Amazon S3 API reference*. 

**Note**  
MediaTailor always signs requests to these origins with SigV4.

## Requirements
<a name="channel-assembly-access-configuration-sigv4-how-to"></a>

 If you activate SigV4 for Amazon S3 authentication for your source location, you must meet these requirements: 
+ You must allow MediaTailor to access your Amazon S3 bucket by granting **mediatailor.amazonaws.com** principal access in IAM. For information about configuring access in IAM, see [Access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *AWS Identity and Access Management User Guide*.
+ The **mediatailor.amazonaws.com** service principal must have permissions to read all multivariant playlists referenced by the VOD source package configurations.
+ The caller of the API must have **s3:GetObject** IAM permissions to read all multivariant playlists referenced by your MediaTailor VOD source package configurations.
+ Your MediaTailor source location base URL must follow the Amazon S3 virtual hosted-style request URL format. For example, https://{{bucket-name}}.s3.{{Region}}.amazonaws.com/{{key-name}}. For information about Amazon S3 hosted virtual-style access, see [Virtual Hosted-Style Requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#virtual-hosted-style-access).