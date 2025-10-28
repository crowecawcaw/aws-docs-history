# Using AWS User Notifications with

Cost Anomaly Detection

You can use [AWS User Notifications](../../../notifications/latest/userguide/what-is-service.md "../../../notifications/latest/userguide/what-is-service.md") to set up delivery channels
that notify you about Cost Anomaly Detection events. You will receive a notification when an event matches
a specified rule. You can receive notifications for events through multiple channels,
including email, [Amazon Q Developer in chat applications](../../../chatbot/latest/adminguide/what-is.md "../../../chatbot/latest/adminguide/what-is.md") such as Amazon
Chime, Microsoft Teams, and Slack, or [AWS Console Mobile Application](../../../consolemobileapp/latest/userguide/what-is-consolemobileapp.md "../../../consolemobileapp/latest/userguide/what-is-consolemobileapp.md") push notifications.
You can also see notifications using the [Console Notifications Center](https://console.aws.amazon.com/notifications/ "https://console.aws.amazon.com/notifications/") in the AWS User Notifications
console.

AWS User Notifications also supports aggregation, which can reduce the number of
notifications you receive during specific events. For more information, see the [AWS
User Notifications User Guide](../../../notifications/latest/userguide/what-is-service.md "../../../notifications/latest/userguide/what-is-service.md").

To use AWS User Notifications, you must have the correct AWS Identity and Access
Management (IAM) permissions. For more information about configuring your IAM
permissions, see [Creating a notification configuration](../../../notifications/latest/userguide/getting-started.md#getting-started-step1 "../../../notifications/latest/userguide/getting-started.md#getting-started-step1") in the
_AWS User Notifications User Guide_.

## Example: EventBridge event for

`Anomaly Detected`

The following is a generalized example event for `Anomaly Detected`.
You can subscribe to EventBridge events (such as this one) using AWS User
Notifications.

```
{
    "version": "0",
    "id": "<id>", // alphanumeric string
    "source": "aws.ce",
    "detail-type": "Anomaly Detected",
    "account": "<account ID>", // 12 digit account id.
    "region": "<region>", // Cost Anomaly Detection home region.
    "time": "<date>", // Format: yyyy-MM-dd'T'hh:mm:ssZ
    "resources": [
         "arn:aws:ce::123456789012:anomalymonitor/abcdef12-1234-4ea0-84cc-918a97d736ef"
    ],
    "detail": {
         "accountName": "<account name>",
         "anomalyEndDate": "2021-05-25T00:00:00Z",
         "anomalyId": "12345678-abcd-ef12-3456-987654321a12",
         "anomalyScore": {
            "currentScore": 0.47,
            "maxScore": 0.47
         },
         "anomalyStartDate": "2021-05-25T00:00:00Z",
         "dimensionValue": "<dimension value>", // service name for AWS Service Monitor
         "feedback": "string",
         "impact": {
            "maxImpact": 151,
            "totalActualSpend": 1301,
            "totalExpectedSpend": 300,
            "totalImpact": 1001,
            "totalImpactPercentage": 333.67
         },
         "rootCauses": [
            {
                "linkedAccount": "<linked account ID>", // 12 digit account id.
                "linkedAccountName": "<linked account name>",
                "region": "<region>",
                "service": "<service name>", // AWS service name
                "usageType": "<usage type>", // AWS service usage type
                "impact": {
                    "contribution": 601,
                }
            }
        ],
        "accountId": "<account ID>", // 12 digit account id.
        "monitorArn": "arn:aws:ce::123456789012:anomalymonitor/abcdef12-1234-4ea0-84cc-918a97d736ef",
        "monitorName": "<your monitor name>",
        "anomalyDetailsLink": "https://console.aws.amazon.com/cost-management/home#/anomaly-detection/monitors/abcdef12-1234-4ea0-84cc-918a97d736ef/anomalies/12345678-abcd-ef12-3456-987654321a12"
    }
}
```

## Filtering events

You can filter events either by service and name using the filters available in
the AWS User Notifications console, or by specific properties if you create your
own EventBridge filter from JSON code.

###### Topics

- [Example: Filter by impact](#example-filter-by-impact "#example-filter-by-impact")
- [Example: Filter by service
  dimension](#example-filter-by-service-dimension "#example-filter-by-service-dimension")
- [Example: Filter by cost
  allocation tag](#example-filter-by-cost-allocation-tag "#example-filter-by-cost-allocation-tag")
- [Example: Filter by Region
  root cause](#example-filter-by-region-root-cause "#example-filter-by-region-root-cause")
- [Example: Filter by multiple
  criteria](#example-filter-composition "#example-filter-composition")

### Example: Filter by impact

The following filter captures any anomaly with a total impact greater than
$100 and a percentage impact greater than 10%.

```
{
    "detail": {
        "impact": {
            "totalImpact": [{
                "numeric": [">", 100]
            }],
            "totalImpactPercentage": [{
                "numeric": [">", 10]
            }]
        }
    }
}
```

### Example: Filter by service

dimension

The following filter captures anomalies specific to the EC2 service, detected
by the AWS services monitor.

```
{
    "detail": {
        "dimensionValue": ["Amazon Elastic Compute Cloud - Compute"],
        "monitorName": ["aws-services-monitor"]
    }
}
```

### Example: Filter by cost

allocation tag

The following filter captures anomalies for the Frontend application team,
detected by a dimensional cost allocation tag monitor.

```
{
  "detail": {
    "dimensionValue": ["ApplicationTeam:Frontend"],
    "monitorName": ["dimensional-CAT-monitor"]
  }
}
```

### Example: Filter by Region

root cause

The following filter captures anomalies that have root causes in the US East
(N. Virginia) Region.

```
{
  "detail": {
    "rootCauses": {
      "region": ["us-east-1"]
    }
  }
}
```

### Example: Filter by multiple

criteria

The following complex filter captures anomalies for the Frontend application
team with a total impact greater than $100, a percentage impact greater than
10%, and root causes in the US East (N. Virginia) Region.

```
{
  "detail": {
    "dimensionValue": ["ApplicationTeam:Frontend"],
    "monitorName": ["dimensional-CAT-monitor"],
    "impact": {
        "totalImpact": [{ "numeric": [">", 100] }],
        "totalImpactPercentage": [{ "numeric": [">", 10] }]
    },
    "rootCauses": {
        "region": ["us-east-1"]
    }
  }
}
```
