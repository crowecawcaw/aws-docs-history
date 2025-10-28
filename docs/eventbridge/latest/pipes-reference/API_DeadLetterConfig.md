# DeadLetterConfig

A `DeadLetterConfig` object that contains information about a dead-letter
queue configuration.

## Contents

**Arn**

The ARN of the specified target for the dead-letter queue.

For Amazon Kinesis stream and Amazon DynamoDB stream sources, specify
either an Amazon SNS topic or Amazon SQS queue ARN.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/DeadLetterConfig.md "../../../goto/SdkForCpp/pipes-2015-10-07/DeadLetterConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/DeadLetterConfig.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/DeadLetterConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/DeadLetterConfig.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/DeadLetterConfig.md")
