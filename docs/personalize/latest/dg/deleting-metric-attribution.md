# Deleting an Amazon Personalize metric attribution

If you no longer want to generate reports, you can delete a metric attribution.
Deleting a metric attribution deletes all of its metrics and output configuration.

If you delete a metric attribution, Amazon Personalize stops automatically sending reports related to PutEvents and incremental bulk
data to CloudWatch. Data already sent to CloudWatch or published to Amazon S3
is not affected.
You can delete a metric attribution with the Amazon Personalize console, AWS Command Line Interface, or AWS SDKS.

###### Topics

- [Deleting a metric attribution (console)](#deleting-metric-attribution-console "#deleting-metric-attribution-console")
- [Deleting a metric attribution (AWS CLI)](#deleting-metric-attribution-cli "#deleting-metric-attribution-cli")
- [Deleting a metric attribution (AWS SDKs)](#deleting-metric-attribution-sdk "#deleting-metric-attribution-sdk")

## Deleting a metric attribution (console)

You delete a metric attribution on the overview page for your metric attribution.

###### To delete a metric attribution

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign into your account.
2. Choose your dataset group.
3. In the navigation pane, choose **Metric attribution**.
4. Choose **Delete** and then confirm the deletion.

## Deleting a metric attribution (AWS CLI)

To delete a metric attribution with the AWS CLI, use the `delete-metric-attribution` command as follows.

```
aws personalize delete-metric-attribution --metric-attribution-arn `metric attribution ARN`
```

## Deleting a metric attribution (AWS SDKs)

The following code shows how to delete a metric attribution with the SDK for Python (Boto3):

SDK for Python (Boto3)

```
import boto3

personalize = boto3.client('personalize')

response = personalize.delete_metric_attribution(
  metricAttributionArn = '`metric attribution ARN`'
)
```

SDK for Java 2.x

```
public static void deleteMetricAttribution(PersonalizeClient client, String metricAttributionArn) {

    try {

        DeleteMetricAttributionRequest request = DeleteMetricAttributionRequest.builder()
                .metricAttributionArn(metricAttributionArn)
                .build();

        DeleteMetricAttributionResponse response = client.deleteMetricAttribution(request);
        if (response.sdkHttpResponse().statusCode() == 200) {
            System.out.println("Metric attribution deleted!");
        }

    } catch (PersonalizeException e) {
        System.out.println(e.awsErrorDetails().errorMessage());
    }
}
```

SDK for JavaScript v3

```
// Get service clients and commands using ES6 syntax.
import { DeleteMetricAttributionCommand, PersonalizeClient } from
  "@aws-sdk/client-personalize";

// create personalizeClient
const personalizeClient = new PersonalizeClient({
  region: "REGION"
});

export const deleteMetricAttributionParam = {
  metricAttributionArn: "METRIC_ATTRIBUTION_ARN",
};
export const run = async () => {
  try {
    const response = await personalizeClient.send(
      new DeleteMetricAttributionCommand(deleteMetricAttributionParam)
    );
    console.log("Success", response);
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();
```
