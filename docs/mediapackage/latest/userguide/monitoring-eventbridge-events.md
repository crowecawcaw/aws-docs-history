# Monitoring AWS Elemental MediaPackage with EventBridge

events

WIth Amazon EventBridge, you can automate your AWS services and respond automatically to system
events such as application availability issues or error conditions. AWS services deliver
events to EventBridge in near real-time. You can write simple rules to indicate which events are of
interest to you, and what automated actions to take when an event matches a rule. The actions
that can be automatically triggered include the following:

- Invoking an AWS Lambda function
- Invoking AWS Systems Manager Run Command
- Relaying the event to Amazon Kinesis Data Streams
- Activating an AWS Step Functions state machine
  For MediaPackage V2, you can use EventBridge and Amazon SNS to be automatically notified when a live-to-VOD
  harvest job succeeds or fails. MediaPackage emits events on a best-effort basis.

For more information about creating rules in EventBridge, see [Creating rules that react to events
in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the _Amazon EventBridge User Guide_.

The following sections describe MediaPackage V2 event types and how to set up notifications of
events.

## MediaPackage V2 events

The following topics describe the EventBridge events that MediaPackage V2 emits.

### Harvest job notification events

You get harvest job status events when you export a clip from a live stream to create a
live-to-VOD asset. MediaPackage creates notifications when the harvest job succeeds or
fails. For information about harvest jobs and live-to-VOD assets, see [Creating live-to-VOD assets with MediaPackage](live-to-vod.md "live-to-vod.md").

###### Example Successful harvest job event

```
{
   "id": "8f9b8e72-0b31-e883-f19c-aec84742f3ce",
   "detail-type": "MediaPackageV2 HarvestJob Notification",
   "source": "aws.mediapackagev2",
   "account": "739874020183",
   "time": "2024-11-07T17:32:36Z",
   "region": "us-west-2",
   "resources": [
       "arn:aws:mediapackagev2:us-west-2:111122223333:channelGroup/channel_group_name/channel/channel_name/originEndpoint/origin_endpoint_name/harvestJob/MyHarvestJob"
   ],
   "detail": {
       "harvestJob": {
           "harvestJobName": "MyHarvestJob",
           "arn": "arn:aws:mediapackagev2:us-west-2:111122223333:channelGroup/channel_group_name/channel/channel_name/originEndpoint/origin_endpoint_name/harvestJob/MyHarvestJob",
           "status": "COMPLETED",
           "channelGroupName": "channel_group_name",
           "channelName": "channel_name",
           "originEndpointName": "endpoint_name",
           "scheduleConfiguration": {
               "startTime": "2024-11-07T17:29:36Z",
               "endTime": "2024-11-07T17:32:36Z",
           },
           "destination": {
               "s3Destination": {
                   "bucketName": "amzn-s3-demo-bucket",
                   "destinationPath": "V2Harvests/my-event/"
               },
           },
           "harvestedManifests": {
               "hlsManifests": [
                   {
                       "manifestName": "examplemanifest.m3u8"
                   }
               ],
               "dashManifests": [
                   {
                       "manifestName": "examplemanifest2.mpd"
                   }
               ],
               "lowLatencyHlsManifests": [
                   {
                       "manifestName": "examplemanifest3.m3u8"
                   },
                   {
                       "manifestName": "examplemanifest4.m3u8"
                   }
               ]
           },
           "message": "Your harvest job is complete."
       }
   }
}
```

###### Example Failed harvest job event

```
{
   "id": "8f9b8e72-0b31-e883-f19c-aec84742f3ce",
   "detail-type": "MediaPackageV2 HarvestJob Notification",
   "source": "aws.mediapackagev2",
   "account": "111122223333",
   "time": "2024-11-07T17:32:36Z",
   "region": "us-west-2",
   "resources": [
       "arn:aws:mediapackagev2:us-west-2:111122223333:channelGroup/channel_group_name/channel/channel_name/originEndpoint/origin_endpoint_name/harvestJob/MyHarvestJob"
   ],
   "detail": {
       "harvestJob": {
           "harvestJobName": "MyHarvestJob",
           "arn": "arn:aws:mediapackagev2:us-west-2:111122223333:channelGroup/channel_group_name/channel/channel_name/originEndpoint/origin_endpoint_name/harvestJob/MyHarvestJob",
           "status": "FAILED",
           "channelGroupName": "channel_group_name",
           "channelName": "channel_name",
           "originEndpointName": "endpoint_name",
           "scheduleConfiguration": {
               "startTime": "2024-11-07T17:29:36Z",
               "endTime": "2024-11-07T17:32:36Z",
           },
           "destination": {
               "s3Destination": {
                   "bucketName": "amzn-s3-demo-bucket",
                   "destinationPath": "V2Harvests/my-event/"
               },
           },
           "harvestedManifests": {
               "hlsManifests": [
                   {
                       "manifestName": "manifestexample1.m3u8"
                   }
               ],
               "dashManifests": [
                   {
                       "manifestName": "manifestexample2.mpd"
                   }
               ],
               "lowLatencyHlsManifests": [
                   {
                       "manifestName": "manifestexample3.m3u8"
                   },
                   {
                       "manifestName": "manifestexample4.m3u8"
                   }
               ]
           },
           "message": "There was no content available for the specified time window."
       }
   }
}
```

## Creating event notifications

You can use Amazon EventBridge and Amazon Simple Notification Service (Amazon SNS) to notify you of new events. In EventBridge, the rule
describes which events you're notified about. In Amazon SNS, the topic describes what kind of
notification you receive. This section provides high-level steps for creating a topic and rule
for events from AWS Elemental MediaPackage. For detailed information about topics and rules, see the
following:

- [Create a topic](../../../sns/latest/dg/sns-getting-started.md#CreateTopic "../../../sns/latest/dg/sns-getting-started.md#CreateTopic") and
  [Subscribe to a topic](../../../sns/latest/dg/sns-getting-started.md#SubscribeTopic "../../../sns/latest/dg/sns-getting-started.md#SubscribeTopic")
  in the _Amazon Simple Notification Service Developer Guide_
- [Getting started with Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md")
  in the _Amazon EventBridge User Guide_

###### To create notifications of EventBridge events

1. Access [Amazon SNS](https://console.aws.amazon.com/sns/v2/home "https://console.aws.amazon.com/sns/v2/home") and create a topic.
   Give the topic a descriptive name that you will later recognize.
2. Subscribe to the topic that you just created. Choose what kind of notification you want
   to receive, and where that notification is sent. For example, for email notifications, choose
   the **Email** protocol and enter the email address to receive notifications
   for the endpoint.
3. Access [EventBridge](https://console.aws.amazon.com/eventbridge "https://console.aws.amazon.com/eventbridge") and create a rule that
   uses a **Custom event pattern**. In the pattern preview space, enter the
   following:

```
{
  "source": [
    "aws.mediapackagev2"
  ],
  "detail-type": [
    "`detail-type from event`"
  ]
}
```

For `detail-type`, enter the value for the `detail-type` field from
the event: `MediaPackageV2 HarvestJob Notification` 4. Add a target to the rule that you just created. Choose **SNS topic**,
and then choose the topic that you created in step 1. 5. Configure the details of the rule, and give it a descriptive name. To start using the
rule, make sure it's enabled, and then save it.
