# Getting a personalized ranking (AWS SDKs)

The following code samples show how different variations of how to get a personalized ranking with the AWS SDKs.

###### Topics

- [Getting a personalized ranking](#personalized-ranking-sdk-sample "#personalized-ranking-sdk-sample")
- [Including item metadata in a personalized ranking](#getting-personalized-ranking-with-metadata-sdk "#getting-personalized-ranking-with-metadata-sdk")
- [Getting a personalized ranking using contextual metadata](#personalized-ranking-contextual-metadata-example "#personalized-ranking-contextual-metadata-example")

## Getting a personalized ranking

The following code shows how to get a personalized ranking for a user. Specify the user's ID and a list of item IDs to be ranked for the user.
The item IDs must be
in the data that you used to train the solution version. A list of ranked recommendations is
returned. Amazon Personalize considers the first item in the list of most interest to the
user.

SDK for Python (Boto3)

```
import boto3

personalizeRt = boto3.client('personalize-runtime')

response = personalizeRt.get_personalized_ranking(
    campaignArn = "`Campaign arn`",
    userId = "`UserID`",
    inputList = ['`ItemID1`','`ItemID2`']
)

print("Personalized Ranking")
for item in response['personalizedRanking']:
    print (item['itemId'])
```

SDK for Java 2.x

```
public static List<PredictedItem> getRankedRecs(PersonalizeRuntimeClient personalizeRuntimeClient,
                                                String campaignArn,
                                                String userId,
                                                ArrayList<String> items) {

    try {
        GetPersonalizedRankingRequest rankingRecommendationsRequest = GetPersonalizedRankingRequest.builder()
                .campaignArn(campaignArn)
                .userId(userId)
                .inputList(items)
                .build();

        GetPersonalizedRankingResponse recommendationsResponse =
                personalizeRuntimeClient.getPersonalizedRanking(rankingRecommendationsRequest);
        List<PredictedItem> rankedItems = recommendationsResponse.personalizedRanking();
        int rank = 1;
        for (PredictedItem item : rankedItems) {
            System.out.println("Item ranked at position " + rank + " details");
            System.out.println("Item Id is : " + item.itemId());
            System.out.println("Item score is : " + item.score());
            System.out.println("---------------------------------------------");
            rank++;
        }
        return rankedItems;
    } catch (PersonalizeRuntimeException e) {
        System.err.println(e.awsErrorDetails().errorMessage());
        System.exit(1);
    }
    return null;
}
```

SDK for JavaScript v3

```
// Get service clients module and commands using ES6 syntax.
import { GetPersonalizedRankingCommand } from "@aws-sdk/client-personalize-runtime";
import { personalizeRuntimeClient } from "./libs/personalizeClients.js";
// Or, create the client here.
// const personalizeRuntimeClient = new PersonalizeRuntimeClient({ region: "REGION"});

// Set the ranking request parameters.
export const getPersonalizedRankingParam = {
  campaignArn: "CAMPAIGN_ARN" /* required */,
  userId: "USER_ID" /* required */,
  inputList: ["ITEM_ID_1", "ITEM_ID_2", "ITEM_ID_3", "ITEM_ID_4"],
};

export const run = async () => {
  try {
    const response = await personalizeRuntimeClient.send(
      new GetPersonalizedRankingCommand(getPersonalizedRankingParam),
    );
    console.log("Success!", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();


```

## Including item metadata in a personalized ranking

If you enabled metadata in recommendations for your campaign, you can specify the Items dataset metadata columns to
include in the response. For information about enabling metadata, see [Item metadata in recommendations](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata").

The following code sample shows how to specify the metadata columns as part of your request for a personalized ranking.

```
import boto3

personalizeRt = boto3.client('personalize-runtime')

response = personalizeRt.get_personalized_ranking(
    campaignArn = "`Campaign arn`",
    userId = "`UserID`",
    inputList = ['`ItemID1`','`ItemID2`'],
    metadataColumns = {
      "ITEMS": ['`columnNameA`','`columnNameB`']
    }
)

print("Personalized Ranking")
for item in response['personalizedRanking']:
    print (item['itemId'])
    print (item['metadata'])
```

## Getting a personalized ranking using contextual metadata

Use the following code to get a personalized ranking based on contextual metadata.
For `context`, for each key-value pair, provide the
metadata field as the key and the context data as the value. In the following sample code, the key is `DEVICE` and the
value is `mobile phone`. Replace these values and the `Campaign ARN` and `User ID` with your own.
Also change `inputList` to a list of item IDs that are
in the data that you used to train the solution.
Amazon Personalize considers the first item in the list of most interest
to the user.

```
import boto3

personalizeRt = boto3.client('personalize-runtime')

response = personalizeRt.get_personalized_ranking(
    campaignArn = "`Campaign ARN`",
    userId = "`User ID`",
    inputList = ['`ItemID1`', '`ItemID2`'],
    context = {
      '`DEVICE`': '`mobile phone`'
    }
)

print("Personalized Ranking")
for item in response['personalizedRanking']:
  print(item['itemId'])
```
