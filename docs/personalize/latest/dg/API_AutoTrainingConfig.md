# AutoTrainingConfig

The automatic training configuration to use when `performAutoTraining` is true.

## Contents

**schedulingExpression**

Specifies how often to automatically train new solution versions. Specify a rate expression in rate(_value_
_unit_) format.
For value, specify a number between 1 and 30. For unit, specify `day` or `days`.
For example, to automatically create a new solution version every 5 days, specify `rate(5 days)`. The default is every 7 days.

For more information about auto training, see [Creating and configuring a solution](customizing-solution-config.md "customizing-solution-config.md").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 16.

Pattern: `rate\(\d+ days?\)`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/AutoTrainingConfig.md "../../../goto/SdkForCpp/personalize-2018-05-22/AutoTrainingConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/AutoTrainingConfig.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/AutoTrainingConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/AutoTrainingConfig.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/AutoTrainingConfig.md")
