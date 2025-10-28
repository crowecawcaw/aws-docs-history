# Getting item metadata with real-time recommendations

If you configured your campaign or recommender to return metadata for recommended items, you can specify the columns to
include in your [GetRecommendations](API_RS_GetRecommendations.md "API_RS_GetRecommendations.md") API operation. Or you
can specify the columns when you test the campaign with the Amazon Personalize console.

For information
about enabling metadata for a campaign, see [Item metadata in recommendations](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata"). For information about enabling metadata for a recommender, see [Enabling metadata in recommendations for a domain recommender in Amazon Personalize](create-recommender-return-metadata.md "create-recommender-return-metadata.md").

The following code samples show how to specify the metadata columns to include with the AWS CLI or the AWS SDKs. To do
this with the Amazon Personalize console, you specify the columns when you test your campaign. For more information, see [Getting item recommendations (console)](getting-real-time-item-recommendations.md#get-real-time-recommendations-console "getting-real-time-item-recommendations.md#get-real-time-recommendations-console").

###### Topics

- [Including item metadata with recommendations (AWS CLI)](#getting-recommendations-with-metadata-cli "#getting-recommendations-with-metadata-cli")
- [Including item metadata with recommendations (AWS SDKs)](#getting-recommendations-with-metadata-sdk "#getting-recommendations-with-metadata-sdk")

## Including item metadata with recommendations (AWS CLI)

If you enabled metadata in recommendations for your campaign or recommender, you can specify the Items dataset
metadata columns to include in the response. The following code sample shows how to specify the metadata columns as part of your request for
recommendations.

```
aws personalize-runtime get-recommendations \
--campaign-arn `campaign arn` \
--user-id `User ID` \
--num-results 10 \
--metadata-columns "{\"ITEMS\": ["\"`columnNameA`"\","\"`columnNameB`"\"]}"
```

## Including item metadata with recommendations (AWS SDKs)

If you enabled metadata in recommendations for your campaign or recommender, you can specify the Items dataset
metadata columns to include in the response. The following code sample shows how to specify the metadata columns as part of your request for recommendations.

```
import boto3

personalizeRt = boto3.client('personalize-runtime')

response = personalizeRt.get_recommendations(
  campaignArn = '`Campaign ARN`',
  userId = '`User ID`',
  numResults = 10
  metadataColumns = {
    "ITEMS": ['`columnNameA`','`columnNameB`']
  }
)

print("Recommended items")
for item in response['itemList']:
  print(item['itemId'])
  print(item['metadata'])
```
