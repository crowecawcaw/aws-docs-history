# Getting real-time item recommendations

You can get real-time item recommendations from an Amazon Personalize recommender or custom campaign with the Amazon Personalize console, AWS Command Line Interface
(AWS CLI), or AWS SDKs.

###### Topics

- [Getting item recommendations (console)](#get-real-time-recommendations-console "#get-real-time-recommendations-console")
- [Getting item recommendations (AWS CLI)](#get-item-rec-cli "#get-item-rec-cli")
- [Getting item recommendations (AWS SDKs)](#get-item-rec-sdk "#get-item-rec-sdk")

## Getting item recommendations (console)

To get recommendations with the Amazon Personalize console, you provide the request information on the details page of either a
recommender (Domain dataset group) or a custom campaign.

###### To get recommendations

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign into your account.
2. Choose the dataset group that contains the campaign or recommender you are using.
3. In the navigation pane, choose **Campaigns** or **Recommenders**.
4. Choose the target campaign or recommender.
5. For a campaigns, under **Test campaign results**, enter your recommendation request details
   based on the recipe you used. For a recommenders choose **Test recommender** and enter your
   recommendation request details based on your use case.

If you recorded events for a user before they logged in (an anonymous user), you can get recommendations for this user by providing the `sessionId` from those events
as if it is their `userId`. For more information about recording events for anonymous users, see [Recording events for
anonymous users](recording-events.md#recording-anonymous-user-events "recording-events.md#recording-anonymous-user-events"). 6. Optionally choose a filter. For more information, see [Filtering recommendations and user segments](filter.md "filter.md"). 7. If you use contextual metadata, provide data for each context. For each context, for the **Key** enter the metadata field. For the **Value** enter the context data. For
more information, see [Increasing recommendation relevance with contextual metadata](contextual-metadata.md "contextual-metadata.md"). 8. If you enabled metadata in recommendations for your campaign or recommender, for **Items dataset
columns**, choose the metadata columns that you want to include in recommendation results. For information
about enabling metadata for a campaign, see [Item metadata in recommendations](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata"). For information about enabling metadata for a recommender, see
[Enabling metadata in recommendations for a domain recommender in Amazon Personalize](create-recommender-return-metadata.md "create-recommender-return-metadata.md"). 9. If you want to promote a subset of items, optionally complete the **Promotion** fields. For more
information see [Promoting items in real-time recommendations](promoting-items.md "promoting-items.md"). 10. Choose **Get recommendations**. A table containing the user’s top 25 recommended
items displays. If you use User-Personalization-v2, each recommended item includes a list of reasons for why the item was included in recommendations. For more information, see
[Recommendation reasons with User-Personalization-v2](recommendations.md#recommendation-reasons "recommendations.md#recommendation-reasons").

## Getting item recommendations (AWS CLI)

Use the following code to get recommendations from a campaign. To get recommendations from a recommender, replace the
`campaign-arn` parameter with the `recommender-arn`.

Specify the ID of the user you want to get recommendations for, and the Amazon Resource Name (ARN) of your campaign
or recommender. A list of the top 10 recommended items for the user displays. If you use User-Personalization-v2, each recommended item includes a list of reasons for why the item was included in recommendations. For more information, see
[Recommendation reasons with User-Personalization-v2](recommendations.md#recommendation-reasons "recommendations.md#recommendation-reasons").

To change the number of recommended items, change the value for `numResults`. The default is 25 items. The
maximum is 500 items. If you used a RELATED_ITEMS recipe to train the solution version backing the campaign, replace the
`user-id` parameter with `item-id` and specify the item ID.

If you recorded events for a user before they logged in (an anonymous user), you can get recommendations for this user by providing the `sessionId` from those events
as if it is their `userId`. For more information about recording events for anonymous users, see [Recording events for
anonymous users](recording-events.md#recording-anonymous-user-events "recording-events.md#recording-anonymous-user-events").

```
aws personalize-runtime get-recommendations \
--campaign-arn `campaign arn` \
--user-id `User ID` \
--num-results 10
```

## Getting item recommendations (AWS SDKs)

The following code shows how to get Amazon Personalize recommendations for a user from a campaign with the AWS SDKs. To get
recommendations from a recommender, replace the `campaignArn` parameter with the `recommenderArn`.

Specify the ID of the user you want to get recommendations for, and the Amazon Resource Name (ARN) of your campaign or
recommender. A list of the top 10 recommended items for the user displays. If you use User-Personalization-v2, each recommended item includes a list of reasons for why the item was included in recommendations. For more information, see
[Recommendation reasons with User-Personalization-v2](recommendations.md#recommendation-reasons "recommendations.md#recommendation-reasons").

To change the number of recommended items, change the value for `numResults`. The default is 25 items. The
maximum is 500 items. If you used a RELATED_ITEMS recipe to train the solution version backing the campaign, replace the
`userId` parameter with `itemId` and specify the item ID.

If you enabled metadata in recommendations for your campaign or recommender, you can specify the Items dataset
metadata columns to include in the response. For a code sample, see [Including item metadata with recommendations (AWS SDKs)](getting-recommendations-with-metadata.md#getting-recommendations-with-metadata-sdk "getting-recommendations-with-metadata.md#getting-recommendations-with-metadata-sdk"). For
information about enabling metadata, see [Item metadata in recommendations](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata").

If you recorded events for a user before they logged in (an anonymous user), you can get recommendations for this user by providing the `sessionId` from those events
as if it is their `userId`. For more information about recording events for anonymous users, see [Recording events for
anonymous users](recording-events.md#recording-anonymous-user-events "recording-events.md#recording-anonymous-user-events").

SDK for Python (Boto3)

```
import boto3

personalizeRt = boto3.client('personalize-runtime')

response = personalizeRt.get_recommendations(
    campaignArn = '`Campaign ARN`',
    userId = '`User ID`',
    numResults = 10
)

print("Recommended items")
for item in response['itemList']:
    print (item['itemId'])
```

SDK for Java 2.x

```
    public static void getRecs(PersonalizeRuntimeClient personalizeRuntimeClient, String campaignArn, String userId) {

        try {
            GetRecommendationsRequest recommendationsRequest = GetRecommendationsRequest.builder()
                    .campaignArn(campaignArn)
                    .numResults(20)
                    .userId(userId)
                    .build();

            GetRecommendationsResponse recommendationsResponse = personalizeRuntimeClient
                    .getRecommendations(recommendationsRequest);
            List<PredictedItem> items = recommendationsResponse.itemList();
            for (PredictedItem item : items) {
                System.out.println("Item Id is : " + item.itemId());
                System.out.println("Item score is : " + item.score());
            }

        } catch (AwsServiceException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }

```

SDK for JavaScript v3

```
// Get service clients module and commands using ES6 syntax.
import { GetRecommendationsCommand } from "@aws-sdk/client-personalize-runtime";

import { personalizeRuntimeClient } from "./libs/personalizeClients.js";
// Or, create the client here.
// const personalizeRuntimeClient = new PersonalizeRuntimeClient({ region: "REGION"});

// Set the recommendation request parameters.
export const getRecommendationsParam = {
  campaignArn: "CAMPAIGN_ARN" /* required */,
  userId: "USER_ID" /* required */,
  numResults: 15 /* optional */,
};

export const run = async () => {
  try {
    const response = await personalizeRuntimeClient.send(
      new GetRecommendationsCommand(getRecommendationsParam),
    );
    console.log("Success!", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();


```
