# AWS Health Dashboard notfication for Rekognition

Your AWS Health Dashboard provides support for notifications that come from Rekognition.
These notifications provide awareness and remediation guidance on scheduled changes in Rekognition Models
that may affect your applications. Only events that are specific to the Rekognition Content Moderation feature are currently available.

The AWS Health Dashboard is part of the AWS Health service. It requires no set up and can be viewed
by any user that is authenticated in your account. For more information, see
[Getting started wtih the AWS Health Dashboard](../../../health/latest/ug/getting-started-phd.md "../../../health/latest/ug/getting-started-phd.md").

If you receive a notification message similar to the following messages, it should be treated as an alarm to take action.

**Example notification: A new model version is available for
Rekognition Content Moderation.**

Rekognition publishes the `AWS_MODERATION_MODEL_VERSION_UPDATE_NOTIFICATION`
event to the AWS Health Dashboard to indicate that a new version of the moderation
model has been released. This event is important if you are using the
DetectModerationLabels API and adapters with this API. New models can impact quality
depending on your use case, and will eventually replace previous model versions. It
is recommended to validate your model quality and be aware of model update timelines
when you get this alert.

If you receive a model version update notification, you should treat it as an
alarm to take action. If you don't use adapters, you should evaluate the quality of
the updated model on your existing use case. If you use adapters, you should train
new adapters with the updated model and evaluate their quality. If you have
auto-train set, new adapters will be trained automatically, and then you can
evaluate their quality.

```

{
   "version": "0",
    "id": "id-number",
    "detail-type": "AWS Health Event",
    "source": "aws.health",
    "account": "123456789012",
    "time": "2023-10-06T06:27:57Z",
    "region": "region",
    "resources": [],
    "detail": {
        "eventArn": "arn:aws:health:us-east-1::event/AWS_MODERATION_MODEL_UPDATE_NOTIFICATION_event-number",
        "service": "Rekognition",
        "eventTypeCode": "AWS_MODERATION_MODEL_VERSION_UPDATE_NOTIFICATION",
        "eventScopeCode": "ACCOUNT_SPECIFIC",
        "communicationId": "communication-id-number",
        "eventTypeCategory": "scheduledChange",
        "startTime": "Fri, 05 Apr 2023 12:00:00 GMT",
        "lastUpdatedTime": "Fri, 05 Apr 2023 12:00:00 GMT",
        "statusCode": "open",
        "eventRegion": "us-east-1",
        "eventDescription": [
            {
                "language": "en_US",
                "latestDescription": "A new model version is available for Rekognition Content Moderation."
            }
        ]
    }
}

```

See [Monitoring AWS Health events with Amazon EventBridge](../../../health/latest/ug/cloudwatch-events-health.md "../../../health/latest/ug/cloudwatch-events-health.md") to detect and react to AWS Health events using EventBridge.
