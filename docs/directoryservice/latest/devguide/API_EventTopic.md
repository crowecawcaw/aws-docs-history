# EventTopic

Information about Amazon SNS topic and AWS Directory Service directory associations.

## Contents

**CreatedDateTime**

The date and time of when you associated your directory with the Amazon SNS topic.

Type: Timestamp

Required: No

**DirectoryId**

The Directory ID of an AWS Directory Service directory that will publish status messages to an Amazon SNS
topic.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**Status**

The topic registration status.

Type: String

Valid Values: `Registered | Topic not found | Failed | Deleted`

Required: No

**TopicArn**

The Amazon SNS topic ARN (Amazon Resource Name).

Type: String

Required: No

**TopicName**

The name of an Amazon SNS topic the receives status messages from the directory.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_-]+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/EventTopic.md "../../../goto/SdkForCpp/ds-2015-04-16/EventTopic.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/EventTopic.md "../../../goto/SdkForJavaV2/ds-2015-04-16/EventTopic.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/EventTopic.md "../../../goto/SdkForRubyV3/ds-2015-04-16/EventTopic.md")
