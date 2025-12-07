# SolutionUpdateSummary

Provides a summary of the properties of a solution update. For a complete listing, call the
[DescribeSolution](API_DescribeSolution.md "API_DescribeSolution.md") API.

## Contents

**creationDateTime**

The date and time (in Unix format) that the solution update was created.

Type: Timestamp

Required: No

**failureReason**

If a solution update fails, the reason behind the failure.

Type: String

Required: No

**lastUpdatedDateTime**

The date and time (in Unix time) that the solution update was last updated.

Type: Timestamp

Required: No

**performAutoTraining**

Whether the solution automatically creates solution versions.

Type: Boolean

Required: No

**performIncrementalUpdate**

A Boolean value that indicates whether incremental training updates are performed on the
model. When enabled, incremental training is performed for solution versions with active
campaigns and allows the model to learn from new data more frequently without requiring full
retraining, which enables near real-time personalization. This parameter is supported only for
solutions that use the semantic-similarity recipe. The default is `true`.

Note that certain scores and attributes (like updates to item popularity and freshness
used for ranking influence with aws-semantic-similarity recipe) may not update until the next
full training occurs.

Type: Boolean

Required: No

**solutionUpdateConfig**

The configuration details of the solution.

Type: [SolutionUpdateConfig](API_SolutionUpdateConfig.md "API_SolutionUpdateConfig.md") object

Required: No

**status**

The status of the solution update. A solution update can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/SolutionUpdateSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/SolutionUpdateSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/SolutionUpdateSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/SolutionUpdateSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/SolutionUpdateSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/SolutionUpdateSummary.md")
