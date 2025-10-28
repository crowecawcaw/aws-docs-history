# Filtering your DevOps Guru notifications

You can filter your DevOps Guru notifications by [Updating Amazon SNS notification configurations](update-notifications.md#update-notification-configurations "update-notifications.md#update-notification-configurations") or by using a Amazon SNS subscription
filter policy.

###### Topics

- [Filtering notifications with a Amazon SNS subscription filter policy](#use-subscription-filter-policy "#use-subscription-filter-policy")
- [Example filtered Amazon SNS notification
  for Amazon DevOps Guru](#sample-filtered-notification "#sample-filtered-notification")

## Filtering notifications with a Amazon SNS subscription filter policy

You can create an Amazon Simple Notification Service (Amazon SNS) subscription filter policy to reduce the number of
notifications you receive from Amazon DevOps Guru.

Use a filter policy to specify the types of notifications you receive. You can filter
your Amazon SNS messages using the following keywords.

- `NEW_INSIGHT` — Receive a notification when a new insight is
  created.
- `CLOSED_INSIGHT` — Receive a notification when an existing
  insight is closed.
- `NEW_RECOMMENDATION` — Receive a notification when a new
  recommendation is created from an insight.
- `NEW_ASSOCIATION` — Receive a notification when a new
  anomaly is detected from an insight.
- `CLOSED_ASSOCIATION` — Receive a notification when an
  existing anomaly is closed.
- `SEVERITY_UPGRADED` — Receive a notification when the
  severity of an insight is upgraded

For information about how to create an Amazon SNS subscription filter policy, see [Amazon SNS
subscription filter policies](../../../sns/latest/dg/sns-subscription-filter-policies.md "../../../sns/latest/dg/sns-subscription-filter-policies.md") in the _Amazon Simple Notification Service Developer
Guide_. In your filter policy, you specify one of the keywords with the
policy's `MessageType`. For example, the following would appear in a filter
that specifies the Amazon SNS topic only deliver notifications when a new anomaly is detected
from an insight.

```
{
  "MessageType":["NEW_ ASSOCIATION"]
}
```

## Example filtered Amazon SNS notification

for Amazon DevOps Guru

The following is an example of an Amazon Simple Notification Service (Amazon SNS) notification from an Amazon SNS
topic with a filter policy. Its `MessageType` is set to
`NEW_ASSOCIATION`, so it sends notifications only when a new anomaly
is detected from an insight.

```
{
      "accountId": "123456789012",
      "region": "us-east-1",
      "messageType": "NEW_ASSOCIATION",
      "insightId": "ADyf4FvaVNDzu9MA2-IgFDkAAAAAAAAAEGpJd5sjicgauU2wmAlnWUyyI2hiO5it",
      "insightName": "Repeated Insight: Anomalous increase in Lambda ApigwLambdaDdbStack-22-Function duration due to increased number of invocations",
      "insightUrl": "https://us-east-1.console.aws.amazon.com/devops-guru/insight/reactive/ADyf4FvaVNDzu9MA2-IgFDkAAAAAAAAAEGpJd5sjicgauU2wmAlnWUyyI2hiO5it",
      "insightType": "REACTIVE",
      "insightDescription": "At March 29, 2023 22:02 GMT, Lambda function ApigwLambdaDdbStack-22-Function had\n an increased duration anomaly possibly caused by the Lambda function invocation increase. DevOps Guru has detected this is a repeated insight. DevOps Guru treats repeated insights as 'Low Severity'.",
      "startTime": 1628767500000,
      "startTimeISO": "2023-03-29T22:00:00Z",
      "anomalies": [
        {
          "id": "AG2n8ljW74BoI1CHu-m_oAgAAAF7Ohu24N4Yro69ZSdUtn_alzPH7VTpaL30JXiF",
          "startTime": 1628767500000,
          "startTimeISO": "2023-03-29T22:00:00Z",
          "openTime": 1680127740000,
          "openTimeISO": "2023-03-29T22:09:00Z",
          "sourceDetails": [
            {
              "dataSource": "CW_METRICS",
              "dataIdentifiers": {
                "namespace": "AWS/SQS",
                "name": "ApproximateAgeOfOldestMessage",
                "stat": "Maximum",
                "unit": "None",
                "period": "60",
                "dimensions": "{\"QueueName\":\"FindingNotificationsDLQ\"}"
              }
            }
          ],
          "associatedResourceArns":[
          	"arn:aws:sns:us-east-1:123456789012:DevOpsGuru-insights-sns"
          ]
        }
      ],
      "resourceCollection":{
      "cloudFormation":{
         "stackNames":[
            "CapstoneNotificationPublisherEcsApplicationInfrastructure"
          ]
        }
      }
}
```
