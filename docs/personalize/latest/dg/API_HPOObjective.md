# HPOObjective

The metric to optimize during hyperparameter optimization (HPO).

###### Note

Amazon Personalize doesn't support configuring the `hpoObjective`
at this time.

## Contents

**metricName**

The name of the metric.

Type: String

Length Constraints: Maximum length of 256.

Required: No

**metricRegex**

A regular expression for finding the metric in the training job logs.

Type: String

Length Constraints: Maximum length of 256.

Required: No

**type**

The type of the metric. Valid values are `Maximize` and `Minimize`.

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/HPOObjective.md "../../../goto/SdkForCpp/personalize-2018-05-22/HPOObjective.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/HPOObjective.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/HPOObjective.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/HPOObjective.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/HPOObjective.md")
