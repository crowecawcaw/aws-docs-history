# ImageGenerationDestinationConfig

The structure that contains the information required to deliver images to a customer.

## Contents

**DestinationRegion**

The AWS Region of the S3 bucket where images will be delivered. This `DestinationRegion` must match the Region where the stream is located.

Type: String

Length Constraints: Minimum length of 9. Maximum length of 14.

Pattern: `^[a-z]+(-[a-z]+)?-[a-z]+-[0-9]$`

Required: Yes

**Uri**

The Uniform Resource Identifier (URI) that identifies where the images will be delivered.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^[a-zA-Z_0-9]+:(//)?([^/]+)/?([^*]*)$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ImageGenerationDestinationConfig.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ImageGenerationDestinationConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ImageGenerationDestinationConfig.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ImageGenerationDestinationConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ImageGenerationDestinationConfig.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ImageGenerationDestinationConfig.md")
