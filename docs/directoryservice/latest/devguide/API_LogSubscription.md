# LogSubscription

Represents a log subscription, which tracks real-time data from a chosen log group to a
specified destination.

## Contents

**DirectoryId**

Identifier (ID) of the directory that you want to associate with the log
subscription.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**LogGroupName**

The name of the log group.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 512.

Pattern: `[-._/#A-Za-z0-9]+`

Required: No

**SubscriptionCreatedDateTime**

The date and time that the log subscription was created.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/LogSubscription.md "../../../goto/SdkForCpp/ds-2015-04-16/LogSubscription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/LogSubscription.md "../../../goto/SdkForJavaV2/ds-2015-04-16/LogSubscription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/LogSubscription.md "../../../goto/SdkForRubyV3/ds-2015-04-16/LogSubscription.md")
