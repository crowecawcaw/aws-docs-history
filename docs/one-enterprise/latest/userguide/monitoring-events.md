# Monitoring Amazon One Enterprise events in Amazon EventBridge

You can monitor Amazon One Enterprise events in EventBridge, which delivers a stream of real-time data from
your own applications, software-as-a-service (SaaS) applications, and AWS services. EventBridge
routes that data to targets such as AWS Lambda and Amazon Simple Notification Service. These events deliver a near real-time
stream of system events that describe changes in AWS resources.

## Subscribe to Amazon One Enterprise events

Amazon One device and user profile status change events are published using EventBridge, and can be enabled
in the EventBridge console by creating a new rule. Although events are not ordered, they have a timestamp
which enables you to consume the data. Events are emitted on a [best effort](../../../eventbridge/latest/userguide/eb-service-event.md "../../../eventbridge/latest/userguide/eb-service-event.md") basis.

###### To subscribe to Amazon One Enterprise events

1. Log in to your AWS console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. Open the EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
3. In the navigation pane, under **Buses**, choose
   **Rules**.
4. Choose **Create rule**.
5. On the **Default rule detail** page, assign a name to the rule.
6. Choose **Rule with an event pattern**,
   and then choose **Next**.
7. On the **Build event pattern** page, under **Event
   source**, verify that **AWS events or EventBridge partner
   events** is selected.
8. Under **Sample event type**, choose **AWS Events**.
9. For **Creation method**, choose **Custom
   pattern**.
10. In the **Event pattern** section, add a JSON with
    event source as `aws:one` and the required detail-type:

```

       "
       source": ["aws.one"],
       "detail-type": ["New Successful Enrollment",
       "New Successful Un-enrollment",
       "Unsuccessful Enrollment",
       "Unsuccessful Un-enrollment",
       "Successful Recognition",
       "Unsuccessful Recognition",
       "New Alert(s) Detected",
       "Some Alert(s) Cleared"]
       }

```

You can choose the required detail type from the above list and remove what is not required. 11. Choose **Next**. 12. On the **Select target(s)** page, select a target of your choice,
which includes a Lambda function, SQS queue, or SNS topic. For information about
configuring targets, see [Amazon EventBridge targets](../../../eventbridge/latest/userguide/eb-targets.md "../../../eventbridge/latest/userguide/eb-targets.md").

For example, to view when someone clocks-in, choose **“Successful
Recognition”**. Then look at the event detail (given in Appendix) to see who clocked in.

To complete your workflow, you can execute an external API or another target. 13. Optionally, you can configure tags. 14. On the **Review and create** page, choose **Create
rule**. For more information about configuring rules, see [EventBridge
rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") in the EventBridge User Guide.

## Device status change event types

Device status change events are generated in JSON. For each event type, a JSON blob is sent to the target of your choice, as configured in the rule.
The following detail types are available:

**Some Alert(s) Cleared**

Device passed one or more health checks.

**New Alert(s) Detected**

Device failed one or more health checks.

###### Event Objects

**resources**

Contains the list of deviceInstance arn for which the Device Status Change event was published.

**data**

clearedAlerts

- Represents the health checks the deviceInstance was previously failing.
- Consists of a statusCode for the type of alert and a reportedAt timestamp.
- Possible statusCode values: NetworkDisconnected, USBDisconnected

currentAlerts

- Represents the current status of the deviceInstance.
- Consists of a statusCode for the type of alert and a reportedAt timestamp.
- Possible statusCode values: NetworkDisconnected, USBDisconnected

newAlerts

- Represents newly failed health checks of the deviceInstance.
- Consists of a statusCode for the type of alert and a reportedAt timestamp.
- Possible statusCode values: NetworkDisconnected, USBDisconnected

currentAlertsCount

- The count of health checks currently failing with the deviceInstance.

assetTagId

- The assetTagId of the device associated with the deviceInstance.

deviceInstanceName

- The name of the deviceInstance for which the Device Status Event was published.

siteName

- Name of the site where the deviceInstance is present.

siteArn

- Arn for the site where the deviceInstance is present.

## User profile event types

The User profile related event details types are:

**New Successful Enrollment**

When a user enrolled successfully.

**New Successful Un-enrollment**

When a user un-enrolled successfully.

**Unsuccessful Enrollment**

When a user failed to enroll.

**Unsuccessful Un-enrollment**

When a user failed to un-enroll.

**Successful Recognition**

When a user scans palm for authentication successfully.

**Unsuccessful Recognition**

When the recognition of a palm scan failed.

###### Event Objects

**resources**

Contains the list of user profile arn for which the user profile event was published.

**data**

accountId

- The relevant AWS account for the device that initiated the request.

requestSource

- This is the deviceInstanceId of the device that initiated the request.

createdTimestamp

- The time of event being created.

userStatus

- The current status of the user.
- Possible values: ACTIVE, DELETED

associatedId

- The associated id of the user, for example the badge id.

reason

- This value will present for unsuccessful events. It contains the reason why the
  event was unsuccessful.

## Sample events

The following examples show events for Amazon One Enterprise.

###### Topics

- [Device health status changed to healthy](#device-health-to-healthy "#device-health-to-healthy")
- [Device health status changed to critical](#device-health-to-critical "#device-health-to-critical")
- [Device connectivity changed to online](#device-connectivity-to-online "#device-connectivity-to-online")
- [Device connectivity changed to offline](#device-connectivity-to-offline "#device-connectivity-to-offline")

## Device health status changed to healthy

The device passed all the health checks.

```
{
        "version": "0",
        "id": "51e022b4-7ce6-34e0-264b-370948fc1123",
        "detail-type": "Some Alert(s) Cleared",
        "source": "aws.one",
        "account": "123456789012",
        "time": "2025-07-17T19:32:42Z",
        "region": "us-east-1",
        "resources":
        [
            "arn:aws:one:us-east-1:123456789012:deviceInstance/F5JRte5Jz21Tqx"
        ],
        "detail":
        {
            "version": "1.0.0",
            "data":
            {
                "clearedAlerts":
                [
                    {
                        "statusCode": "USBDisconnected",
                        "reportedAt": "Thu Jul 17 19:32:42 UTC 2025"
                    }
                ],
                "currentAlerts":
                [],
                "currentAlertsCount": 0,
                "assetTagId": "0000123456",
                "deviceInstanceName": "device_name",
                "siteName": "site_name",
                "siteArn": "arn:aws:one:us-east-1:123456789012:site/12345678901234"
            }
        }
      }
```

## Device health status changed to critical

The device failed one or more health checks.

```
{
        "version": "0",
        "id": "07af4893-ef9f-965a-d245-3f0c8bd3c123",
        "detail-type": "New Alert(s) Detected",
        "source": "aws.one",
        "account": "123456789012",
        "time": "2025-07-17T19:26:58Z",
        "region": "us-east-1",
        "resources":
        [
            "arn:aws:one:us-east-1:123456789012:deviceInstance/12345678901234"
        ],
        "detail":
        {
            "version": "1.0.0",
            "data":
            {
                "newAlerts":
                [
                    {
                        "statusCode": "USBDisconnected",
                        "reportedAt": "Thu Jul 17 19:26:58 UTC 2025"
                    }
                ],
                "currentAlerts":
                [
                    {
                        "statusCode": "USBDisconnected",
                        "reportedAt": "Thu Jul 17 19:26:58 UTC 2025"
                    }
                ],
                "currentAlertsCount": 1,
                "assetTagId": "0000123456",
                "deviceInstanceName": "device_name",
                "siteName": "site_name",
                "siteArn": "arn:aws:one:us-east-1:123456789012:site/12345678901234"
            }
        }
      }
```

## Device connectivity changed to online

The device is now connected to the internet.

```
{
        "version": "0",
        "id": "e6ecea28-dd60-5061-29f8-dfbc902f4123",
        "detail-type": "Some Alert(s) Cleared",
        "source": "aws.one",
        "account": "123456789012",
        "time": "2025-07-17T18:28:23Z",
        "region": "us-east-1",
        "resources":
        [
            "arn:aws:one:us-east-1:123456789012:deviceInstance/12345678901234"
        ],
        "detail":
        {
            "version": "1.0.0",
            "data":
            {
                "clearedAlerts":
                [
                    {
                        "statusCode": "NetworkDisconnected",
                        "reportedAt": "Thu Jul 17 18:28:23 UTC 2025"
                    }
                ],
                "currentAlerts":
                [],
                "currentAlertsCount": 0,
                "assetTagId": "0000123456",
                "deviceInstanceName": "device_name",
                "siteName": "site_name",
                "siteArn": "arn:aws:one:us-east-1:123456789012:site/12345678901234"
            }
        }
      }
```

## Device connectivity changed to offline

The device is no longer connected to the internet.

```
{
        "version": "0",
        "id": "e6ecea28-dd60-5061-29f8-dfbc902f4123",
        "detail-type": "New Alert(s) Detected",
        "source": "aws.one",
        "account": "123456789012",
        "time": "2025-07-17T18:28:23Z",
        "region": "us-east-1",
        "resources":
        [
            "arn:aws:one:us-east-1:123456789012:deviceInstance/12345678901234"
        ],
        "detail":
        {
            "version": "1.0.0",
            "data":
            {
                "newAlerts":
                [
                    {
                        "statusCode": "NetworkDisconnected",
                        "reportedAt": "Thu Jul 17 18:28:23 UTC 2025"
                    }
                ],
                "currentAlerts":
                [
                    {
                        "statusCode": "NetworkDisconnected",
                        "reportedAt": "Thu Jul 17 18:28:23 UTC 2025"
                    }
                ],
                "currentAlertsCount": 1,
                "assetTagId": "0000123456",
                "deviceInstanceName": "device_name",
                "siteName": "site_name",
                "siteArn": "arn:aws:one:us-east-1:123456789012:site/12345678901234"
            }
        }
      }
```
