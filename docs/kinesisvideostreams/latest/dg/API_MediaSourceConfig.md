# MediaSourceConfig

The configuration details that consist of the credentials required
(`MediaUriSecretArn` and `MediaUriType`) to access the media files that are
streamed to the camera.

## Contents

**MediaUriSecretArn**

The AWS Secrets Manager ARN for the username and password of the camera, or a local media file location.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:[a-z\d-]+:secretsmanager:[a-z0-9-]+:[0-9]+:secret:[a-zA-Z0-9_.-]+`

Required: Yes

**MediaUriType**

The Uniform Resource Identifier (URI) type. The `FILE_URI` value can be used to stream
local media files.

###### Note

Preview only supports the `RTSP_URI` media source URI format .

Type: String

Valid Values: `RTSP_URI | FILE_URI`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/MediaSourceConfig.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/MediaSourceConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/MediaSourceConfig.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/MediaSourceConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/MediaSourceConfig.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/MediaSourceConfig.md")
