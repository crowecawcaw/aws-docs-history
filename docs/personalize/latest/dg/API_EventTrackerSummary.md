# EventTrackerSummary

Provides a summary of the properties of an event tracker. For a complete listing, call the
[DescribeEventTracker](API_DescribeEventTracker.md "API_DescribeEventTracker.md") API.

## Contents

**creationDateTime**

The date and time (in Unix time) that the event tracker was created.

Type: Timestamp

Required: No

**eventTrackerArn**

The Amazon Resource Name (ARN) of the event tracker.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**lastUpdatedDateTime**

The date and time (in Unix time) that the event tracker was last updated.

Type: Timestamp

Required: No

**name**

The name of the event tracker.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**status**

The status of the event tracker.

An event tracker can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- DELETE PENDING > DELETE IN_PROGRESS

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/EventTrackerSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/EventTrackerSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/EventTrackerSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/EventTrackerSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/EventTrackerSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/EventTrackerSummary.md")
