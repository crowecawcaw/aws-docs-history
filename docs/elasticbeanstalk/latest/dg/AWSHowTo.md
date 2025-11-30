# Using Elastic Beanstalk with Amazon EventBridge

Using Amazon EventBridge, you can set up event-driven rules that monitor your Elastic Beanstalk resources and initiate target actions that use other AWS services. For
example, you can set a rule for sending out email notifications by signaling an Amazon SNS topic whenever the health of a production environment changes to a
_Warning_ status. Or, you can set a Lambda function to pass a notification to Slack whenever the health of your environment changes to
a _Degraded_ or _Severe_ status.

You can create rules in Amazon EventBridge to act on any of the following Elastic Beanstalk events:

- _State changes for environment operations (including create, update, and terminate operations)._ The event specifies if the state
  change has started, succeeded, or failed.
- _State changes for other resources._ Besides environments, other resources that are monitored include load balancers, auto
  scaling groups, and instances.
- _Health transition for environments._ The event states where the environment health has transitioned from one health status to
  another one.
- _State change for managed updates._ The event specifies if the state change has started, succeeded, or failed.
  To capture specific Elastic Beanstalk events that you're interested in, define event-specific patterns that EventBridge can use to detect the events. Event patterns have
  the same structure as the events they match. The pattern quotes the fields that you want to match and provides the values that you're looking for.
  Events are emitted on a best effort basis. They're delivered from Elastic Beanstalk to EventBridge in near real-time under normal operational circumstances.
  However, situations can arise that may delay or prevent delivery of an event.

For a list of fields that are contained in Elastic Beanstalk events and their possible string values, see [Elastic Beanstalk event field mapping](#eb-eventbridge-mapping "#eb-eventbridge-mapping"). For information about how EventBridge rules work with event patterns, see [Events and Event Patterns in EventBridge](../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md "../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md").

## Monitor an Elastic Beanstalk resource with EventBridge

With EventBridge, you can create rules that define actions to take when Elastic Beanstalk emits events for its resources. For example, you can create a rule that sends
you an email message whenever the status of an environment changes.

The EventBridge console has a **Pre-defined pattern** option for building Elastic Beanstalk event patterns. If you select this option in the EventBridge
console when you create a rule, you can build an Elastic Beanstalk event pattern quickly. You only need to select the event fields and values. As you make selections,
the console builds and displays the event pattern. Alternatively, you can manually edit the event pattern that you build and can save it as a custom
pattern. The console also provides you the option to display a detailed **Sample Event** that you can copy and paste to the event pattern
that you're building.

If you prefer to type or copy and paste an event pattern into the EventBridge console, you can select to use the **Custom pattern** option
in the console. By doing this, you don't need to go through the steps of selecting fields and values described earlier. This topic offers examples of both
[event-matching patterns](#eb-eventbridge-patterns "#eb-eventbridge-patterns") and [Elastic Beanstalk events](#eb-eventbridge-examples "#eb-eventbridge-examples") that you can
use.

###### To create a rule for a resource event

1. Log in to AWS using an account that has permissions to use EventBridge and Elastic Beanstalk.
2. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
3. In the navigation pane, choose **Rules**.
4. Choose **Create rule**.
5. Enter a **Name** for the rule, and, optionally, a description.
6. For **Event bus**, choose **default**. When an AWS service in your account emits an event, it always goes to
   your account’s default event bus.
7. For **Rule type**, choose **Rule with an event pattern**.
8. Choose **Next**.
9. For **Event source**, choose **AWS events or EventBridge partner events**.
10. (Optional) For **Sample event**, select **AWS events**. Enter _Elastic Beanstalk_ in the search
    field. This will provide a list of sample Elastic Beanstalk events from which you can choose to display. This step simply displays a sample event that you can
    reference. It doesn't affect the outcome of the rule creation. The [Example Elastic Beanstalk events](#eb-eventbridge-examples "#eb-eventbridge-examples")
    section later in this topic provides examples of the same type of events.
11. In the **Event pattern** section, choose **Event pattern form**.

###### Note

If you already have text for an event pattern and don't need the EventBridge console to build it for you, select **Custom pattern (JSON
editor)**. You can then either manually enter or copy and paste text into the **Event pattern** box. Choose
**Next**, and go to the step about entering a target. 12. For **Event source**, choose **AWS services**. 13. For **AWS service**, select **Elastic Beanstalk**. 14. For **Event type**, select **Status Change**. 15. This step covers how you can work with the **detail type**, **status**, and **severity** event
fields for Elastic Beanstalk. As you choose these fields and the values you want to match, the console builds and displays the event pattern.

    * If
     you select *only one* value for **Specific detail type(s)**, you can choose one or more values for the next
     field in the hierarchy.
    * If
     you choose *more than one* value for **Specific detail type(s)**, do not choose specific values for the next
     fields in the hierarchy. This prevents ambiguous matching logic across fields in your event pattern.

The **environment** event field isn't affected by this hierarchy, so it displays as described in the next step. 16. For environment, select **Any environment** or **Specific environment(s)**.

    * If you select **Specific environment(s)**, you can choose one or more environments from the dropdown list. EventBridge adds all of
     the environments that you select inside the *EnvironmentName[ ]* list in the *detail* section of the event
     pattern. Then, your rule filters all events to include only the specific environments that you choose.
    * If you select **Any environment**, then no environments are added to your event pattern. Because of this, your rule doesn't
     filter any of the Elastic Beanstalk events based on environment.

17. Choose **Next**.
18. For **Target types**, choose **AWS service**.
19. For **Select a target**, choose the target action to take when a resource state change event is received from Elastic Beanstalk.

For example, you can use an Amazon Simple Notification Service (SNS) topic to send an email or text message when an event occurs. To do this, you need to create an Amazon SNS
topic using the Amazon SNS console. To learn more, see [Using Amazon SNS for
user notifications](../../../sns/latest/dg/sns-user-notifications.md "../../../sns/latest/dg/sns-user-notifications.md").

###### Important

Some target actions might require the use of other services and incur additional charges, such as the Amazon SNS or Lambda service.
For more information about AWS pricing, see
[https://aws.amazon.com/pricing/](https://aws.amazon.com/pricing/ "https://aws.amazon.com/pricing/"). Some services are part of the AWS Free Usage Tier. If you are a new
customer, you can test drive
these services for free. See [https://aws.amazon.com/free/](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") for more information. 20. (Optional) Choose **Add another target** to specify an additional target action for the event rule. 21. Choose **Next**. 22. (Optional) Enter one or more tags for the rule. For more information, see [Amazon EventBridge tags](../../../eventbridge/latest/userguide/eb-tagging.md "../../../eventbridge/latest/userguide/eb-tagging.md") in the _Amazon EventBridge User Guide_. 23. Choose **Next**. 24. Review the details of the rule and choose **Create rule**.

## Example Elastic Beanstalk event patterns

Event patterns have the same structure as the events they match. The pattern quotes the fields that you want to match and provides the values that
you're looking for.

- _Health status change_ for all environments

```
{
   "source": [
    "aws.elasticbeanstalk"
  ],
  "detail-type": [
    "Health status change"
    ]
}
```

- _Health status change_ for the following environments: `myEnvironment1` and `myEnvironment2`. This event
  pattern filters for these two specific environments, whereas the previous _Health status change_ example that doesn't filter sends
  events for all environments.

```
{"source": [
    "aws.elasticbeanstalk"
    ],
    "detail-type": [
        "Health status change"
    ],
    "detail": {
        "EnvironmentName": [
            "myEnvironment1",
            "myEnvironment2"
        ]
    }
}
```

- _Elastic Beanstalk resource status change_ for all environments

```
{
  "source": [
    "aws.elasticbeanstalk"
  ],
  "detail-type": [
    "Elastic Beanstalk resource status change"
    ]
}
```

- _Elastic Beanstalk resource status change_ with `Status`
  _Environment update failed_ and `Severity`
  _ERROR_ for the following environments: `myEnvironment1` and `myEnvironment2`

```
{"source": [
    "aws.elasticbeanstalk"
    ],
    "detail-type": [
        "Elastic Beanstalk resource status change"
    ],
    "detail": {
        "Status": [
            "Environment update failed"
            ],
        "Severity": [
            "ERROR"
            ],
        "EnvironmentName": [
            "myEnvironment1",
            "myEnvironment2"
        ]
    }
}
```

- _Other resource status change_ for load balancers, auto scaling groups, and instances

```
{
   "source": [
    "aws.elasticbeanstalk"
  ],
  "detail-type": [
    "Other resource status change"
    ]
}
```

- _Managed update status change_ for all environments

```
{
   "source": [
    "aws.elasticbeanstalk"
  ],
  "detail-type": [
    "Managed update status change"
    ]
}
```

- To capture _all events_ from Elastic Beanstalk (exclude the `detail-type` section)

```
{
  "source": [
    "aws.elasticbeanstalk"
  ]
}
```

## Example Elastic Beanstalk events

The following is an example Elastic Beanstalk event for a _resource status change_:

```
{
   "version":"0",
   "id":"1234a678-1b23-c123-12fd3f456e78",
   "detail-type":"Elastic Beanstalk resource status change",
   "source":"aws.elasticbeanstalk",
   "account":"111122223333",
   "time":"2020-11-03T00:31:54Z",
   "region":"us-east-1",
   "resources":[
      "arn:was:elasticbeanstalk:us-east-1:111122223333:environment/myApplication/myEnvironment"
   ],
   "detail":{
      "Status":"Environment creation started",
      "EventDate":1604363513951,
      "ApplicationName":"myApplication",
      "Message":"createEnvironment is starting.",
      "EnvironmentName":"myEnvironment",
      "Severity":"INFO"
   }
}
```

The following is an example Elastic Beanstalk event for a _health status change_:

```
{
   "version":"0",
   "id":"1234a678-1b23-c123-12fd3f456e78",
   "detail-type":"Health status change",
   "source":"aws.elasticbeanstalk",
   "account":"111122223333",
   "time":"2020-11-03T00:34:48Z",
   "region":"us-east-1",
   "resources":[
      "arn:was:elasticbeanstalk:us-east-1:111122223333:environment/myApplication/myEnvironment"
   ],
   "detail":{
      "Status":"Environment health changed",
      "EventDate":1604363687870,
      "ApplicationName":"myApplication",
      "Message":"Environment health has transitioned from Pending to Ok. Initialization completed 1 second ago and took 2 minutes.",
      "EnvironmentName":"myEnvironment",
      "Severity":"INFO"
   }
}
```

## Elastic Beanstalk event field mapping

The following table maps Elastic Beanstalk event fields and their possible string values to the EventBridge `detail-type` field. For more information about
how EventBridge works with event patterns for a service, see [Events and Event Patterns in EventBridge](../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md "../../../eventbridge/latest/userguide/eventbridge-and-event-patterns.md").

| **EventBridge field _detail-type_**      | **Elastic Beanstalk field _Status_** | **Elastic Beanstalk field _Severity_**                                                                         | **Elastic Beanstalk field _Message_**                  |
| ---------------------------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Elastic Beanstalk resource status change | Environment creation started         | INFO                                                                                                           | createEnvironment is starting.                         |
| Environment creation successful          | INFO                                 | createEnvironment completed successfully.                                                                      |
| Environment creation successful          | INFO                                 | Launched environment: <Environment Name>. However, there were issues during launch. See event log for details. |
| Environment creation failed              | ERROR                                | Failed to launch environment.                                                                                  |
| Environment update started               | INFO                                 | Environment update is starting.                                                                                |
| Environment update successful            | INFO                                 | Environment update completed successfully.                                                                     |
| Environment update failed                | ERROR                                | Failed to deploy configuration.                                                                                |
| Environment termination started          | INFO                                 | terminateEnvironment is starting.                                                                              |
| Environment termination successful       | INFO                                 | terminateEnvironment completed successfully.                                                                   |
| Environment termination failed           | INFO                                 | The environment termination step failed because at least one of the environment termination workflows failed.  |
| Other resource status change             | Auto Scaling group created           | INFO                                                                                                           | createEnvironment is starting.                         |
| Auto Scaling group deleted               | INFO                                 | createEnvironment is starting.                                                                                 |
| Instance added                           | INFO                                 | Added instance [i-123456789a12b1234] to your environment.                                                      |
| Instance removed                         | INFO                                 | Removed instance [i-123456789a12b1234] from your environment.                                                  |
| Load balancer created                    | INFO                                 | Created load balancer named: <LB Name>                                                                         |
| Load balancer deleted                    | INFO                                 | Deleted load balancer named: <LB Name>                                                                         |
| Health status change                     | Environment health changed           | INFO/WARN                                                                                                      | Environment health has transitioned to <healthStatus>. |
| Environment health changed               | INFO/WARN                            | Environment health has transitioned from <healthStatus> to <healthStatus>.                                     |
| Managed update status change             | Managed updated started              | INFO                                                                                                           | Managed platform update is in-progress.                |
| Managed update failed                    | INFO                                 | Managed update failed, retrying in %s minutes.                                                                 |
