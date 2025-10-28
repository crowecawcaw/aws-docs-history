# Using EventBridge with Cost Anomaly Detection

AWS Cost Anomaly Detection is integrated with EventBridge, an event bus service that you can use to
connect your applications with data from a variety of sources. For more information, see
the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

You can use EventBridge to detect and react to Cost Anomaly Detection events. Then, based on rules that
you create, EventBridge invokes one or more target actions when an event matches the
values that you specify in a rule. Depending on the type of event, you can capture event
information, initiate additional events, send notifications, take corrective action, or
perform other actions. To set up an EventBridge rule for Cost Anomaly Detection events, see [Create a rule in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md#eb-gs-create-rule "../../../eventbridge/latest/userguide/eb-get-started.md#eb-gs-create-rule") in the
_Amazon EventBridge User Guide_.

## Example: EventBridge event for

Cost Anomaly Detection

When an immediate alert is detected, the subscriber receives an event with the
`Anomaly Detected` detail type. The following example shows the event
body for the detail type:

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
