# FirehoseLogDestination

The Amazon Data Firehose logging configuration settings for the pipe.

## Contents

**DeliveryStreamArn**

The Amazon Resource Name (ARN) of the Firehose delivery stream to which EventBridge delivers the pipe log records.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `(^arn:aws([a-z]|\-)*:firehose:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):deliverystream/[a-zA-Z0-9_.-]{1,64})`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/FirehoseLogDestination.md "../../../goto/SdkForCpp/pipes-2015-10-07/FirehoseLogDestination.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/FirehoseLogDestination.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/FirehoseLogDestination.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/FirehoseLogDestination.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/FirehoseLogDestination.md")
