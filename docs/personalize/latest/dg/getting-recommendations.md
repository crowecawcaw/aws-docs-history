# Getting recommendations from Amazon Personalize

After you [create a recommender](creating-recommenders.md "creating-recommenders.md") or [create a campaign](campaigns.md "campaigns.md"),
you are ready to get recommendations. Depending on your resources, you can get recommendations in real time or with a batch workflow.

- With custom resources, you can get real-time recommendations or batch recommendations. For real-time recommendations,
  you must create a custom campaign before you get recommendations. For batch recommendations, you don't need to create a
  campaign.
- With recommenders in a Domain dataset group, you can get only real-time recommendations.

The following topics explain how and when to use each recommendation type. With both batch and real-time recommendations, you can filter
results. For more information see [Filtering recommendations and user segments](filter.md "filter.md").

###### Topics

- [Recommendation scores](#how-scores-work "#how-scores-work")
- [Real-time item recommendations in Amazon Personalize](recommendations.md "recommendations.md")
- [Real-time action recommendations in Amazon Personalize](get-action-recommendations.md "get-action-recommendations.md")
- [Getting a personalized ranking (custom resources)](rankings.md "rankings.md")
- [Increasing recommendation relevance with contextual metadata](contextual-metadata.md "contextual-metadata.md")
- [Getting batch item recommendations with custom resources](getting-batch-recommendations.md "getting-batch-recommendations.md")
- [Getting batch user segments with custom resources](getting-user-segments.md "getting-user-segments.md")

## Recommendation scores

With custom solutions created with the User-Personalization-v2, User-Personalization, Personalized-Ranking-v2, Personalized-Ranking, and PERSONALIZED_ACTIONS recipes, Amazon Personalize includes a score
for each item in recommendations. These scores represent the relative certainty that Amazon Personalize has about which item or action the user
will select next. Higher scores represent greater certainty.

- For information about scores for User-Personalization-v2 and User-Personalization, see [How recommendation scoring works (custom resources)](recommendations.md#how-recommendation-scoring-works "recommendations.md#how-recommendation-scoring-works").
- For information about scores for PERSONALIZED_ACTIONS recipes, see [How action recommendation scoring works](get-action-recommendations.md#how-action-recommendation-scoring-works "get-action-recommendations.md#how-action-recommendation-scoring-works").
- For information on scores for Personalized-Ranking-v2 and Personalized-Ranking recommendations, see [How personalized ranking scoring works](rankings.md#how-ranking-scoring-works "rankings.md#how-ranking-scoring-works").

For batch inference jobs, item scores are calculated just as
described in [How recommendation scoring works (custom resources)](recommendations.md#how-recommendation-scoring-works "recommendations.md#how-recommendation-scoring-works") and [How personalized ranking scoring works](rankings.md#how-ranking-scoring-works "rankings.md#how-ranking-scoring-works").
You can view scores in the batch inference job's output JSON file.
