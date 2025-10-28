# CloudwatchLogsLogDestinationParameters

The Amazon CloudWatch Logs logging configuration settings for the pipe.

## Contents

**LogGroupArn**

The AWS Resource Name (ARN) for the CloudWatch log group to which EventBridge sends the log records.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `(^arn:aws([a-z]|\-)*:logs:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):log-group:[\.\-_/#A-Za-z0-9]{1,512}(:\*)?)`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/CloudwatchLogsLogDestinationParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/CloudwatchLogsLogDestinationParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/CloudwatchLogsLogDestinationParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/CloudwatchLogsLogDestinationParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/CloudwatchLogsLogDestinationParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/CloudwatchLogsLogDestinationParameters.md")
