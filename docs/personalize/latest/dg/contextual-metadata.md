# Increasing recommendation relevance with contextual metadata

To increase recommendation relevance, include contextual metadata for a
user, such as their device type or the time of day, when you get item recommendations or get a personalized ranking.

To use contextual metadata, the schema of the Item interactions dataset must have
metadata fields
for the contextual data. For example, a DEVICE field (see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md")).
When considering fields
to use for contextual metadata, select fields where the values are available for historical
data in the Item interactions dataset, and when you get item recommendations or get a
personalized ranking of items.

For Domain dataset groups, the following recommender use cases can use contextual metadata:

- [Recommended for
  you](ECOMMERCE-use-cases.md#recommended-for-you-use-case "ECOMMERCE-use-cases.md#recommended-for-you-use-case") (ECOMMERCE domain)
- [Top picks for you](VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case "VIDEO_ON_DEMAND-use-cases.md#top-picks-use-case") (VIDEO_ON_DEMAND domain)

For custom resources, recipes that use contextual metadata include the following:

- [User-Personalization-v2](native-recipe-user-personalization-v2.md "native-recipe-user-personalization-v2.md") and [User-Personalization](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md")
- [Personalized-Ranking-v2](native-recipe-personalized-ranking-v2.md "native-recipe-personalized-ranking-v2.md") and [Personalized-Ranking](native-recipe-search.md "native-recipe-search.md")

For more information on contextual information, see the following AWS Machine Learning Blog post:
[Increasing the relevance of your Amazon Personalize recommendations by leveraging contextual information](https://aws.amazon.com/blogs/machine-learning/increasing-the-relevance-of-your-amazon-personalize-recommendations-by-leveraging-contextual-information/ "https://aws.amazon.com/blogs/machine-learning/increasing-the-relevance-of-your-amazon-personalize-recommendations-by-leveraging-contextual-information/").

You can get recommendations with contextual metadata with
the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

## Getting recommendations using contextual metadata (AWS Python SDK)

To increase recommendation relevance, include contextual metadata for a
user, such as their device type or the time of day, when you get item recommendations or get a personalized ranking.

Use the following code to get a recommendation based on contextual metadata. For `context`, for each key-value pair, provide the
metadata field as the key and the context data as the value. In the following sample code, the key is `DEVICE` and the
value is `mobile phone`. Replace these values and the `Campaign ARN` and `User ID` with your own.
If you created a recommender, replace `campaignArn` with `recommenderArn`.
A list of recommended items for the user displays.

```
import boto3

personalizeRt = boto3.client('personalize-runtime')

response = personalizeRt.get_recommendations(
    campaignArn = '`Campaign ARN`',
    userId = '`User ID`',
    context = {
      '`DEVICE`': '`mobile phone`'
    }
)

print("Recommended items")
for item in response['itemList']:
    print (item['itemId'])
```
