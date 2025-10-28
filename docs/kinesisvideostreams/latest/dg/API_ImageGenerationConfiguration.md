# ImageGenerationConfiguration

The structure that contains the information required for the KVS images delivery. If null, the configuration will be deleted from the stream.

## Contents

**DestinationConfig**

The structure that contains the information required to deliver images to a customer.

Type: [ImageGenerationDestinationConfig](API_ImageGenerationDestinationConfig.md "API_ImageGenerationDestinationConfig.md") object

Required: Yes

**Format**

The accepted image format.

Type: String

Valid Values: `JPEG | PNG`

Required: Yes

**ImageSelectorType**

The origin of the Server or Producer timestamps to use to generate the images.

Type: String

Valid Values: `SERVER_TIMESTAMP | PRODUCER_TIMESTAMP`

Required: Yes

**SamplingInterval**

The time interval in milliseconds (ms) at which the images need to be generated from the stream. The minimum value that can be provided is 200 ms. If the timestamp range is less than the sampling interval, the
Image from the `StartTimestamp` will be returned if available.

Type: Integer

Required: Yes

**Status**

Indicates whether the `ContinuousImageGenerationConfigurations` API is enabled or disabled.

Type: String

Valid Values: `ENABLED | DISABLED`

Required: Yes

**FormatConfig**

The list of a key-value pair structure that contains extra parameters that can be applied when the image is generated.
The `FormatConfig` key is the `JPEGQuality`, which indicates the JPEG quality key to be used to generate the image.
The `FormatConfig` value accepts ints from 1 to 100. If the value is 1, the image will be generated with less quality and the best compression.
If the value is 100, the image will be generated with the best quality and less compression. If no value is provided, the default value of the `JPEGQuality`
key will be set to 80.

Type: String to string map

Map Entries: Maximum number of 1 item.

Valid Keys: `JPEGQuality`

Value Length Constraints: Minimum length of 0. Maximum length of 256.

Value Pattern: `^[a-zA-Z_0-9]+`

Required: No

**HeightPixels**

The height of the output image that is used in conjunction with the `WidthPixels` parameter. When both
`HeightPixels` and `WidthPixels` parameters are provided, the image will be stretched to fit the specified aspect ratio.
If only the `HeightPixels` parameter is provided, its original aspect ratio will be used to calculate the `WidthPixels` ratio.
If neither parameter is provided, the original image size will be returned.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 2160.

Required: No

**WidthPixels**

The width of the output image that is used in conjunction with the `HeightPixels` parameter. When both `WidthPixels` and
`HeightPixels` parameters are provided, the image will be stretched to fit the specified aspect ratio. If only the `WidthPixels` parameter is
provided, its original aspect ratio will be used to calculate the `HeightPixels` ratio. If neither parameter is provided, the original image size will be returned.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 3840.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ImageGenerationConfiguration.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ImageGenerationConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ImageGenerationConfiguration.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ImageGenerationConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ImageGenerationConfiguration.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ImageGenerationConfiguration.md")
