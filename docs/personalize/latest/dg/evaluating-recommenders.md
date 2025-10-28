# Evaluating an Amazon Personalize domain recommender

You can evaluate the performance of your recommender through offline and online metrics. _Online metrics_ are the empirical results
you observe in your users' interactions with real-time recommendations. For example, you might record your users' click-through rate
as they browse your catalog. You are responsible for generating and recording any online metrics.

_Offline metrics_ are the metrics Amazon Personalize generates when you create a recommender.
With offline metrics, you can evaluate the performance of the models backing your recommender.
You can view the effects of modifying a recommender's configuration,
and you can compare results from recommenders trained with different use cases with the
_same data_ in the same dataset group.

Avoid comparing metrics of different recommenders trained with different data. The difference in metrics might
be from the difference in data rather than model performance. For example, you might have a
dataset group with sparse `purchase` event data for each user, and another with robust `view` event data.
Based on metrics like `precision at K`, the recommender trained on the view event data
might incorrectly appear to perform better due to the higher number of interactions.

To get performance metrics, Amazon Personalize splits the input interactions data into a training set and a testing set. The training
set consists of 90% of your users and their interactions data. The testing set consists of the remaining 10% of users and
their interactions data.

Amazon Personalize then creates the recommender using the training set. After training completes, Amazon Personalize gives the new recommender
the oldest 90% of each user’s data from the testing set as input. Amazon Personalize then calculates metrics by comparing the
recommendations the recommender generates to the actual interactions in the newest 10% of each user’s data from the testing
set.

###### Topics

- [Retrieving
  metrics](#retrieving-recommender-metrics "#retrieving-recommender-metrics")
- [Metric definitions](#metric-definitions-recommenders "#metric-definitions-recommenders")
- [Example](#working-with-recommender-metrics-example "#working-with-recommender-metrics-example")
- [Additional resources](#additional-metrics-resources-recommenders "#additional-metrics-resources-recommenders")

## Retrieving

metrics

After your recommender is active, you can view the metrics for the
recommender in the Amazon Personalize console or retrieve metrics by calling the [DescribeRecommender](API_DescribeRecommender.md "API_DescribeRecommender.md") operation.

###### Topics

- [Viewing metrics
  (console)](#retrieving-recommender-metrics-console "#retrieving-recommender-metrics-console")
- [Retrieving metrics
  (AWS CLI)](#retrieving-recommender-metrics-cli "#retrieving-recommender-metrics-cli")
- [Retrieving metrics
  (AWS SDKs)](#retrieving-recommender-metrics-sdk "#retrieving-recommender-metrics-sdk")

### Viewing metrics

(console)

To view recommender metrics in the console, you navigate to the
details page for your recommender.

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to
   your account.
2. On the **Dataset groups** page, choose your
   Domain dataset group.
3. From the navigation pane, choose
   **Recommenders**.
4. From the list of recommenders, choose the one to view its
   metrics.

### Retrieving metrics

(AWS CLI)

The following code shows how to get metrics for a recommender with
the AWS CLI.

```
aws personalize describe-recommender \
--recommender-arn `recommender arn`
```

The following is an example of the metrics output from a recommender
created for the _Top picks for you_
use case for the VIDEO_ON_DEMAND domain.

```
{
    "recommender": {
        "recommenderArn": "arn:aws:personalize:region:acct-id:recommender/recommenderName",
        "datasetGroupArn": "arn:aws:personalize:region:acct-id:dataset-group/dsGroupName",
        "name": "name123",
        "recipeArn": "arn:aws:personalize:::recipe/aws-vod-top-picks",
        "modelMetrics": {
            "coverage": 0.27,
            "mean_reciprocal_rank_at_25": 0.0379,
            "normalized_discounted_cumulative_gain_at_5": 0.0405,
            "normalized_discounted_cumulative_gain_at_10": 0.0513,
            "normalized_discounted_cumulative_gain_at_25": 0.0828,
            "precision_at_5": 0.0136,
            "precision_at_10": 0.0102,
            "precision_at_25": 0.0091,
        }
        "recommenderConfig": {},
        "creationDateTime": "2022-05-06T10:11:24.589000-07:00",
        "lastUpdatedDateTime": "2022-05-06T10:34:33.270000-07:00",
        "status": "ACTIVE",
    }
}
```

### Retrieving metrics

(AWS SDKs)

The following code shows how to get metrics for a recommender with
the SDK for Python (Boto3).

```
import boto3

personalize = boto3.client('personalize')

response = personalize.describe_recommender(
    recommenderArn = '`recommender_arn`'
)
print(response['recommender']['modelMetrics'])
```

The following is an example the metrics output from a recommender
created for the _Top picks for you_
use case for the VIDEO_ON_DEMAND domain.

```
{
    "recommender": {
        "recommenderArn": "arn:aws:personalize:region:acct-id:recommender/recommenderName",
        "datasetGroupArn": "arn:aws:personalize:region:acct-id:dataset-group/dsGroupName",
        "name": "name123",
        "recipeArn": "arn:aws:personalize:::recipe/aws-vod-top-picks",
        "modelMetrics": {
            "coverage": 0.27,
            "mean_reciprocal_rank_at_25": 0.0379,
            "normalized_discounted_cumulative_gain_at_5": 0.0405,
            "normalized_discounted_cumulative_gain_at_10": 0.0513,
            "normalized_discounted_cumulative_gain_at_25": 0.0828,
            "precision_at_5": 0.0136,
            "precision_at_10": 0.0102,
            "precision_at_25": 0.0091,
        }
        "recommenderConfig": {},
        "creationDateTime": "2022-05-06T10:11:24.589000-07:00",
        "lastUpdatedDateTime": "2022-05-06T10:34:33.270000-07:00",
        "status": "ACTIVE",
    }
}
```

## Metric definitions

The metrics Amazon Personalize generates for recommenders are described below using the following
terms:

- _Relevant recommendation_ is a recommendation for an item
  that the user actually interacted with. These items are from the newest 10% of each user’s interactions data from the
  testing set.
- _Rank_ refers to the position of a recommended
  item in the list of recommendations. Position 1 (the top of the list)
  is presumed to be the most relevant to the user.

For each metric, higher numbers (closer to 1) are better. To dive deeper, see the resources listed in [Additional resources](#additional-metrics-resources-recommenders "#additional-metrics-resources-recommenders").

**coverage**

The value for _coverage_ tells you the
proportion of unique items that Amazon Personalize might recommend out of the
total number of unique items in Interactions and Items datasets. A
higher coverage score means Amazon Personalize recommends more of your items,
rather than the same few items repeatedly for different users. Use
cases that feature item exploration, such as the _Top picks
for you_ (VIDEO_ON_DEMAND) and _Recommended for
you_ (ECOMMERCE), have higher coverage than those that
don’t.

**mean reciprocal rank at 25**

This metric tells you about a model's ability to generate a relevant recommendation
at the top ranked position. You might choose a model with a high _mean reciprocal rank
at 25_ if you are generating relevant search results for a user,
and don't expect the user to choose an item lower on the list.
For example, users frequently choose the first
cooking recipe in search results.

Amazon Personalize calculates this metric using the average reciprocal rank score
for requests for recommendations. Each reciprocal rank score
is calculated as follows: `1 / the rank of the highest item interacted with by the user`, where
the total possible rankings is 25. Other lower ranked items the user interacts with are ignored. If the user chose the first item, the score is 1. If they
don't choose any items, the score is 0.

For example, you might show three different users 25 recommendations each:

- If User 1 clicks the item at rank _4_ and the item at rank _10_,
  their reciprocal rank score is _1/4_.
- If User 2 clicks an item at rank _2_, an
  item at rank _4_, and an item at rank _12_,
  their reciprocal rank score is 1/2.
- If User 3 clicks on a single item at rank _6_,
  their reciprocal rank score is 1/6.

The mean reciprocal rank
over all requests for recommendations (in this case 3) is calculated as
`(1/4 + 1/2 + 1/6) / 3 = .3056`.

**normalized discounted cumulative gain (NDCG) at K (5, 10, or 25)**

This metric tells you about how well your model ranks recommendations, where K is a sample size of
5, 10, or 25 recommendations.
This metric is useful if you are most interested in the ranking of recommendations beyond just
the highest ranked item (for this, see `mean reciprocal rank at 25`).
For example, the score for `NDCG at 10` would be useful if you have an
application that shows up to 10 movies in a carousel at a time.

Amazon Personalize calculates the NDCG by assigning
weight to recommendations based on their ranking position for each user in the testing set.
Each recommendation is discounted (given a lower weight) by a
factor dependent on its position. The final metric is the average of all users in the testing set.
The normalized discounted
cumulative gain at K assumes that recommendations that are lower on
a list are less relevant than recommendations higher on the
list.

Amazon Personalize uses a weighting factor of `1/log(1 +
 position)`, where the top of the list is position
`1`.

**precision at K**

This metric tells you how relevant your model’s
recommendations are based on a sample size of K (5, 10, or 25)
recommendations.

Amazon Personalize calculates this metric based on the number
of relevant recommendations out of the top K recommendations for each user in the testing set,
divided by K, where K is 5, 10, or 25. The final metric is the average across all users
in the testing set.

For example, if you recommend 10 items to a user, and the user interacts with 3 of them,
the precision at K is 3 correctly predicted items divided by the total 10 recommended items:
`3 / 10 = .30`.

This metric rewards precise recommendation of relevant
items. The closer the score is to one, the more precise the model.

## Example

The following is a simple example for a recommender
that produces a list of recommendations for a specific user. The
second and fifth recommendations match records in the testing data for
this user. These are the relevant recommendations. If `K` is
set at `5`, the following metrics are generated for the
user.

**reciprocal_rank**

Calculation: 1/2

Result: 0.5000

**normalized_discounted_cumulative_gain_at_5**

Calculation: (1/log(1 + 2) + 1/log(1 + 5)) / (1/log(1 + 1) +
1/log(1 + 2))

Result: 0.6241

**precision_at_5**

Calculation: 2/5

Result: 0.4000

## Additional resources

To dive deeper in different types of metrics for recommender systems,
see the following external resources:

- [MRR vs MAP vs NDCG: Rank-Aware Evaluation Metrics And When To Use Them](https://medium.com/swlh/rank-aware-recsys-evaluation-metrics-5191bba16832/ "https://medium.com/swlh/rank-aware-recsys-evaluation-metrics-5191bba16832/")
- [Discounted Cumulative Gain: the ranking metrics you should know about](https://medium.com/@maeliza.seymour/discounted-cumulative-gain-the-ranking-metrics-you-should-know-about-e1d1623f8cd9 "https://medium.com/@maeliza.seymour/discounted-cumulative-gain-the-ranking-metrics-you-should-know-about-e1d1623f8cd9")
- [Recall and Precision at k for Recommender Systems](https://medium.com/@bond.kirill.alexandrovich/precision-and-recall-in-recommender-systems-and-some-metrics-stuff-ca2ad385c5f8 "https://medium.com/@bond.kirill.alexandrovich/precision-and-recall-in-recommender-systems-and-some-metrics-stuff-ca2ad385c5f8")
- [Ranking Evaluation Metrics for Recommender Systems](https://towardsdatascience.com/ranking-evaluation-metrics-for-recommender-systems-263d0a66ef54 "https://towardsdatascience.com/ranking-evaluation-metrics-for-recommender-systems-263d0a66ef54")
