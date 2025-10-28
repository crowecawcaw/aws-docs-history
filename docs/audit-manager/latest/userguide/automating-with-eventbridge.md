# Monitoring AWS Audit Manager with Amazon EventBridge

Amazon EventBridge helps you automate your AWS services and respond automatically to system events
such as application availability issues or resource changes.

You can use EventBridge
rules to detect and react to Audit Manager events. Based on the rules that you create, EventBridge invokes one
or more target actions when an event matches the values that you specify in a rule. Depending
on the type of event, you might want to send notifications, capture event information, take
corrective action, initiate events, or take other actions.

For example, you can detect whenever the following Audit Manager events occur in your account:

- An audit owner creates, updates, or deletes an assessment
- An audit owner delegates a control set for review
- A delegate completes their review and submits the reviewed control set back to the
  audit owner
- An audit owner updates the status of an assessment control
  The actions that can be automatically triggered include the following:

- Use an AWS Lambda function to pass a notification to a Slack channel.
- Push data about the check to an Amazon Kinesis Data Streams to support comprehensive and real-time
  status monitoring.
- Send an Amazon Simple Notification Service (Amazon SNS) topic to your email.
- Get notified with an Amazon CloudWatch alarm action.

###### Note

Audit Manager delivers events on a _durable_ basis. This means
that Audit Manager will successfully attempt to deliver events to EventBridge at least once. In cases
where events can't be delivered because of an EventBridge service disruption, they will be retried
again later by Audit Manager for up to 24 hours.

## EventBridge example format for Audit Manager

The following JSON code shows an example of an assessment creation event in Audit Manager. For
information on any of the fields in this event, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md").

```
{
    "version": "0",
    "id": "55c5a6f3-6183-3989-49ec-a3c998857644",
    "detail-type": "Assessment Created",
    "source": "aws.auditmanager",
    "account": "111122223333",
    "time": "2023-07-27T00:38:33Z",
    "region": "us-west-2",
    "resources":
        [
            "arn:aws:auditmanager:us-west-2:111122223333:assessment/a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6"
        ],
    "detail":
    {
        "eventID": "4e939b2f-9429-3141-beec-d640d83ef68e",
        "author": "arn:aws:sts::111122223333:assumed-role/roleName/role-session-name",
        "assessmentTenantId": "111122223333",
        "assessmentName": "myAssessment",
        "eventTime": 1690418289068,
        "eventName": "CREATE",
        "eventType": "ASSESSMENT",
        "assessmentID": "a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6"
    }
}
```

## Prerequisites for creating an EventBridge rule

Before you create rules for Audit Manager events, we recommend that you do the following:

- Familiarize yourself with events, rules, and targets in EventBridge. For more
  information, see [What is Amazon EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") in the _Amazon EventBridge User Guide_.
- Create a target to use in your event rule. For example, you can create an Amazon SNS
  topic so that whenever a control set review is completed, you'll receive a text
  message or email. For more information, see [EventBridge targets](../../../eventbridge/latest/userguide/eb-targets.md "../../../eventbridge/latest/userguide/eb-targets.md").

## Creating an EventBridge rule for Audit Manager

Follow these steps to create an EventBridge rule that triggers on an event emitted by Audit Manager.
Events are emitted on a best effort basis.

###### To create an EventBridge rule for Audit Manager

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. On the **Define rule detail** page, enter a name and description
   for the rule.
5. Keep the default values for **Event bus** and **Rule
   type**, and then choose **Next**.
6. On the **Build event pattern** page, for **Event
   source**, choose **AWS events or EventBridge partner
   events**.
7. For **Creation method**, choose **Custom pattern (JSON
   editor)**.
8. Under **Event pattern**, write an event pattern in JSON and specify
   the fields that you want to use for matching.

To match an Audit Manager event, you can use the following simple pattern:

```
{
  "detail-type": ["`Event`"]
}
```

Replace `Event` with one of the following supported
values:

    1. Enter `Assessment Created` to get notifications when an assessment is
     created.
    2. Enter `Assessment Updated` to get notifications when an assessment is
     updated.
    3. Enter `Assessment Deleted` to get notifications when an assessment is
     deleted.
    4. Enter `Assessment ControlSet Delegation Created` to get notifications
     when a control set is delegated for review.
    5. Enter `Assessment ControlSet Reviewed` to get notifications when an
     assessment control set is reviewed.
    6. Enter `Assessment Control Reviewed` to get notifications when an
     assessment control is reviewed.###### Tip

Add more fields to your event pattern as needed. For more information about available fields,
see [Amazon EventBridge event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md"). 9. Choose **Next**. 10. On the **Select target(s)** page, choose the target that you
created for this rule, and then configure any additional options that are required for
that type. For example, if you choose Amazon SNS, make sure that your SNS topic is configured
correctly so that you'll be notified by email or SMS.

###### Tip

The fields displayed vary depending on the service selected. For more
information about available targets, see [Targets available in the EventBridge console](../../../eventbridge/latest/userguide/eb-targets.md#eb-console-targets "../../../eventbridge/latest/userguide/eb-targets.md#eb-console-targets"). 11. For many target types, EventBridge needs permissions to send events to the target. In these
cases, EventBridge can create the IAM role that's needed for your rule to run.

    1. To create an IAM role automatically, choose **Create a new role for
     this specific resource**.
    2. To use an IAM role that you created earlier, choose **Use existing
     role**.

12. (Optional) Choose **Add another target** to add another target for
    this rule.
13. Choose **Next**.
14. (Optional) On the **Configure tags** page, add any tags and then
    choose **Next**.
15. On the **Review and create** page, review your rule setup and
    ensure that it meets your event monitoring requirements.
16. Choose **Create rule**. Your rule will now monitor for Audit Manager events and then send them to the target that you specified.
