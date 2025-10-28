# Recommender

Describes a recommendation generator for a Domain dataset group. You create a recommender in a Domain dataset group
for a specific domain use case (domain recipe), and specify the recommender in a [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md") request.

## Contents

**creationDateTime**

The date and time (in Unix format) that the recommender was created.

Type: Timestamp

Required: No

**datasetGroupArn**

The Amazon Resource Name (ARN) of the Domain dataset group that contains the recommender.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**failureReason**

If a recommender fails, the reason behind the failure.

Type: String

Required: No

**lastUpdatedDateTime**

The date and time (in Unix format) that the recommender was last updated.

Type: Timestamp

Required: No

**latestRecommenderUpdate**

Provides a summary of the latest updates to the recommender.

Type: [RecommenderUpdateSummary](API_RecommenderUpdateSummary.md "API_RecommenderUpdateSummary.md") object

Required: No

**modelMetrics**

Provides evaluation metrics that help you determine the performance
of a recommender. For more information, see
[Evaluating a recommender](evaluating-recommenders.md "evaluating-recommenders.md").

Type: String to double map

Map Entries: Maximum number of 100 items.

Key Length Constraints: Maximum length of 256.

Required: No

**name**

The name of the recommender.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`

Required: No

**recipeArn**

The Amazon Resource Name (ARN) of the recipe (Domain dataset group use case) that the recommender was created for.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**recommenderArn**

The Amazon Resource Name (ARN) of the recommender.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**recommenderConfig**

The configuration details of the recommender.

Type: [RecommenderConfig](API_RecommenderConfig.md "API_RecommenderConfig.md") object

Required: No

**status**

The status of the recommender.

A recommender can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- STOP PENDING > STOP IN_PROGRESS > INACTIVE > START PENDING > START IN_PROGRESS > ACTIVE
- DELETE PENDING > DELETE IN_PROGRESS

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/Recommender.md "../../../goto/SdkForCpp/personalize-2018-05-22/Recommender.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/Recommender.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/Recommender.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/Recommender.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/Recommender.md")
