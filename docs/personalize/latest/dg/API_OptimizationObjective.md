# OptimizationObjective

Describes the additional objective for the solution, such as maximizing streaming
minutes or increasing revenue. For more information see [Optimizing a solution](optimizing-solution-for-objective.md "optimizing-solution-for-objective.md").

## Contents

**itemAttribute**

The numerical metadata column in an Items dataset related to the optimization objective. For example, VIDEO_LENGTH (to maximize streaming minutes), or PRICE (to maximize revenue).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 150.

Required: No

**objectiveSensitivity**

Specifies how Amazon Personalize balances the importance of your optimization objective versus relevance.

Type: String

Valid Values: `LOW | MEDIUM | HIGH | OFF`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/OptimizationObjective.md "../../../goto/SdkForCpp/personalize-2018-05-22/OptimizationObjective.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/OptimizationObjective.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/OptimizationObjective.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/OptimizationObjective.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/OptimizationObjective.md")
