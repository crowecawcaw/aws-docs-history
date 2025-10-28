# Image

A structure that contains the `Timestamp`, `Error`, and `ImageContent`.

## Contents

**Error**

The error message shown when the image for the provided timestamp was not extracted due to a non-tryable error. An error will be returned if:

- There is no media that exists for the specified `Timestamp`.

- The media for the specified time does not allow an image to be extracted. In this case the media is audio only, or the incorrect
  media has been ingested.

Type: String

Valid Values: `NO_MEDIA | MEDIA_ERROR`

Required: No

**ImageContent**

An attribute of the `Image` object that is Base64 encoded.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 6291456.

Required: No

**TimeStamp**

An attribute of the `Image` object that is used to extract an image from the video stream. This field is used to manage gaps on images or to better understand the pagination
window.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/Image.md "../../../goto/SdkForCpp/kinesis-video-reader-data-2017-09-30/Image.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/Image.md "../../../goto/SdkForJavaV2/kinesis-video-reader-data-2017-09-30/Image.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/Image.md "../../../goto/SdkForRubyV3/kinesis-video-reader-data-2017-09-30/Image.md")
