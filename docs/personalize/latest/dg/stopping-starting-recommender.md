# Stopping a recommender

After your recommender is active, you can stop a recommender and start it later. This way, you can pause recommender
billing and only pay for it when you use it. For example, you might need to get recommendations only on certain days
of the week. You can stop the recommender on the days you don't need it, and then start the recommender on the days
you do.

After you stop a recommender, you can't use it to get recommendations. Stopping a recommender halts recommender
billing and retraining. However, stopping a recommender doesn't delete the recommender. You can restart it at any time
and resume getting recommendations. Starting a recommender doesn't create a new recommender with your data. Rather, it
resumes recommender billing and retraining every 7 days.

You can stop and start a recommender with the Amazon Personalize console, AWS Command Line Interface (AWS CLI), AWS SDKs.

**Recommender states**

When you stop a recommender, the recommender state changes from ACTIVE to INACTIVE in the following sequence:

ACTIVE > STOP PENDING > STOP IN PROGRESS > INACTIVE

When you start a recommender, the recommender state changes from INACTIVE to ACTIVE in the following sequence:

INACTIVE > START PENDING > START IN PROGRESS > ACTIVE

###### Topics

- [Stopping a recommender (console)](#stop-start-recommender-console "#stop-start-recommender-console")
- [Stopping a recommender (AWS CLI)](#stop-start-recommender-cli "#stop-start-recommender-cli")
- [Stopping a recommender (AWS SDKs)](#stop-start-recommender-sdks "#stop-start-recommender-sdks")

## Stopping a recommender (console)

You can stop a recommender from the details page for the recommender in the Amazon Personalize console.

###### To stop a recommender

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign in to your account.
2. On the **Dataset groups** page, choose your Domain dataset group.
3. From the navigation pane, choose **Recommenders**.
4. On the **Recommenders** page, choose the recommender that you want to stop.
5. On the details page for the recommender, choose **Stop recommender** at the top right and confirm on the window that
   displays. When the recommender status is inactive, your recommender has stopped. You can start it again
   from the same page.

## Stopping a recommender (AWS CLI)

To stop an active recommender with the AWS CLI, use the `stop-recommender` command, which uses the [StopRecommender](API_StopRecommender.md "API_StopRecommender.md") API operation, and provide the Amazon
Resource Name (ARN) for the recommender. To restart it, you can use `start-recommender` command, which
use the [StartRecommender](API_StartRecommender.md "API_StartRecommender.md"). The following code shows
how to stop a recommender:

```
aws personalize stop-recommender --recommender-arn "`recommender arn`"
```

## Stopping a recommender (AWS SDKs)

To stop an active recommender with the AWS SDKs, use the [StopRecommender](API_StopRecommender.md "API_StopRecommender.md") API operation, and provide the Amazon
Resource Name (ARN) for the recommender. To restart it, you use
the [StartRecommender](API_StartRecommender.md "API_StartRecommender.md"). The following code shows
how to stop a recommender:

SDK for Python (Boto3)
To stop an active recommender with the SDK for Python (Boto3), use the `stop_recommender` method
and provide the Amazon Resource Name (ARN) for the recommender as follows.

```
import boto3
personalize = boto3.client('personalize')

stop_recommender_response = personalize.stop_recommender(
    recommenderArn = "`recommenderARN`"
)
print(stop_recommender_response)
```

SDK for Java 2.x
To stop an active recommender with the SDK for Java 2.x, use the `stopRecommender` method and
provide the ARN for the recommender as follows.

```
public static void stopRecommender(PersonalizeClient personalizeClient,
                                              String datasetGroupArn) {

    try {

        StopRecommenderRequest stopRecommenderRequest = StopRecommenderRequest.builder()
                .recommenderArn(recommenderArn)
                .build();
        personalizeClient.stopRecommender(stopRecommenderRequest);
    } catch (PersonalizeException e) {
        System.out.println(e.awsErrorDetails().errorMessage());
    }
    return "";
}
```

SDK for JavaScript v3

```
// Get service clients and commands using ES6 syntax.
import { StopRecommenderCommand, PersonalizeClient } from
  "@aws-sdk/client-personalize";

// create personalizeClient
const personalizeClient = new PersonalizeClient({
  region: "REGION"
});

// set the request params
export const stopRecommenderParam = {
  recommenderArn: "RECOMMENDER_ARN" /* required */
};

export const run = async () => {
  try {
    const response = await personalizeClient.send(
      new StopRecommenderCommand(stopRecommenderParam)
    );
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();
```
