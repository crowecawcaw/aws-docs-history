# Real-time action recommendations in Amazon Personalize

If you use a PERSONALIZED_ACTIONS recipe, you can get action recommendations from your campaign in real time. You can get action recommendations with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

###### Topics

- [How action recommendation scoring works](#how-action-recommendation-scoring-works "#how-action-recommendation-scoring-works")
- [Getting action recommendations (console)](#get-action-recommendations-console "#get-action-recommendations-console")
- [Getting action recommendations (AWS CLI)](#get-action-recommendations-cli-example "#get-action-recommendations-cli-example")
- [Getting action recommendations (AWS SDKs)](#get-action-recommendations-sdk-example "#get-action-recommendations-sdk-example")

## How action recommendation scoring works

With the Next-Best-Action recipe, Amazon Personalize generates scores for actions based on the likelihood that the user will
interact with the action. Scores can be between 0 – 1.0. The closer to 1.0, the more likely it is that the user will
interact with the action.

If you haven't imported any action interaction data, all recommended actions will have a score of 0.0. If Amazon Personalize
recommends an action as part of _exploration_, the item will have a score of 0.0. Amazon Personalize
uses exploration to recommend actions without action interaction data. For more information about exploration, see [Exploration](use-case-recipe-features.md#about-exploration "use-case-recipe-features.md#about-exploration").

## Getting action recommendations (console)

To get action recommendations with the Amazon Personalize console, you provide the request information on the details page of your custom campaign.

###### To get action recommendations

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign into your account.
2. Choose the dataset group that contains the campaign you're using.
3. In the navigation pane, under **Custom resources**, choose **Campaigns**.
4. Choose the target campaign.
5. Under **Test campaign results**, enter your recommendation request details.

If you recorded events for a user before they logged in (an anonymous user), you can get recommendations for this user by providing the `sessionId` from those events
as if it is their `userId`. For more information about recording events for anonymous users, see [Recording events for
anonymous users](recording-events.md#recording-anonymous-user-events "recording-events.md#recording-anonymous-user-events"). 6. Optionally choose a filter. For more information, see [Filtering recommendations and user segments](filter.md "filter.md"). 7. Choose **Get recommendations**. A table containing the user’s top 5 recommended actions
appears.

## Getting action recommendations (AWS CLI)

Use the following code to get action recommendations from a campaign. Specify the ID of the user that you want to get
recommendations for and the Amazon Resource Name (ARN) of your campaign.

To change the number of recommended actions, change the value for `numResults`. The
default is 5 actions. The maximum is 100 actions.

To filter actions recommendations by custom criteria, you can create a filter and apply it to the
`get-action-recommendations` operation. For more information, see [Filtering recommendations and user segments](filter.md "filter.md").

If you recorded events for a user before they logged in (an anonymous user), you can get recommendations for this user by providing the `sessionId` from those events
as if it is their `userId`. For more information about recording events for anonymous users, see [Recording events for
anonymous users](recording-events.md#recording-anonymous-user-events "recording-events.md#recording-anonymous-user-events").

```
aws personalize-runtime get-action-recommendations \
--campaign-arn `campaign arn` \
--user-id `User ID` \
--num-results 10
```

## Getting action recommendations (AWS SDKs)

The following code shows how to get Amazon Personalize recommendations for a user from a campaign. Specify the ID of the user you want
to get recommendations for, and the Amazon Resource Name (ARN) of your campaign.

To change the number of recommended actions, change the value for
`numResults`. The
default is 5 actions. The maximum is 100 actions.

To filter actions recommendations by custom criteria, you can create a filter and apply it to the [GetActionRecommendations](API_RS_GetActionRecommendations.md "API_RS_GetActionRecommendations.md") API request. For more
information, see [Filtering recommendations and user segments](filter.md "filter.md").

If you recorded events for a user before they logged in (an anonymous user), you can get recommendations for this user by providing the `sessionId` from those events
as if it is their `userId`. For more information about recording events for anonymous users, see [Recording events for
anonymous users](recording-events.md#recording-anonymous-user-events "recording-events.md#recording-anonymous-user-events").

```
import boto3

personalizeRt = boto3.client('personalize-runtime')

response = personalizeRt.get_action_recommendations(
    campaignArn = '`Campaign ARN`',
    userId = '`User ID`',
    numResults = 10
)

print("Recommended actions")
for item in response['actionList']:
    print (item['actionId'])
```
