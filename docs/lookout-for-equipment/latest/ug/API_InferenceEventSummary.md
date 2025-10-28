On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# InferenceEventSummary

Contains information about the specific inference event, including start and end time,
diagnostics information, event duration and so on.

## Contents

**Diagnostics**

An array which specifies the names and values of all sensors contributing to an
inference event.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50000.

Required: No

**EventDurationInSeconds**

Indicates the size of an inference event in seconds.

Type: Long

Valid Range: Minimum value of 0.

Required: No

**EventEndTime**

Indicates the ending time of an inference event.

Type: Timestamp

Required: No

**EventStartTime**

Indicates the starting time of an inference event.

Type: Timestamp

Required: No

**InferenceSchedulerArn**

The Amazon Resource Name (ARN) of the inference scheduler being used for the inference
event.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:inference-scheduler\/.+`

Required: No

**InferenceSchedulerName**

The name of the inference scheduler being used for the inference events.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `^[0-9a-zA-Z_-]{1,200}$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceEventSummary.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/InferenceEventSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceEventSummary.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/InferenceEventSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceEventSummary.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/InferenceEventSummary.md")
