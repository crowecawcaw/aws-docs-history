# RecommenderUpdateSummary

Provides a summary of the properties of a recommender update. For a complete listing, call the
[DescribeRecommender](API_DescribeRecommender.md "API_DescribeRecommender.md") API.

## Contents

**creationDateTime**

The date and time (in Unix format) that the recommender update was created.

Type: Timestamp

Required: No

**failureReason**

If a recommender update fails, the reason behind the failure.

Type: String

Required: No

**lastUpdatedDateTime**

The date and time (in Unix time) that the recommender update was last updated.

Type: Timestamp

Required: No

**recommenderConfig**

The configuration details of the recommender update.

Type: [RecommenderConfig](API_RecommenderConfig.md "API_RecommenderConfig.md") object

Required: No

**status**

The status of the recommender update. A recommender update can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/RecommenderUpdateSummary.md "../../../goto/SdkForCpp/personalize-2018-05-22/RecommenderUpdateSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/RecommenderUpdateSummary.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/RecommenderUpdateSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/RecommenderUpdateSummary.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/RecommenderUpdateSummary.md")
