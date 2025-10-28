# EventParameters

Describes the parameters of events, which are used in solution creation.

## Contents

**eventType**

The name of the event type to be considered for solution creation.

Type: String

Length Constraints: Maximum length of 256.

Required: No

**eventValueThreshold**

The threshold of the event type. Only events with a value greater or equal to this threshold will be considered for solution creation.

Type: Double

Required: No

**weight**

The weight of the event type. A higher weight means higher importance of the event type for the created solution.

Type: Double

Valid Range: Minimum value of 0. Maximum value of 1.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/EventParameters.md "../../../goto/SdkForCpp/personalize-2018-05-22/EventParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/EventParameters.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/EventParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/EventParameters.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/EventParameters.md")
