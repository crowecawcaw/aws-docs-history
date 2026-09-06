

# Monitor Athena query events with EventBridge
<a name="athena-events"></a>

You can use Amazon Athena with Amazon EventBridge to receive real-time notifications regarding the state of your queries. When a query you have submitted transitions states, Athena publishes an event to EventBridge containing information about that query state transition. You can write simple rules for events that are of interest to you and take automated actions when an event matches a rule. For example, you can create a rule that invokes an AWS Lambda function when a query reaches a terminal state. Events are emitted on a best effort basis.

Before you create event rules for Athena, you should do the following:
+ Familiarize yourself with events, rules, and targets in EventBridge. For more information, see [What Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) For more information about how to set up rules, see [Getting started with Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html).
+ Create the target or targets to use in your event rules.

**Note**  
Athena currently offers one type of event, Athena Query State Change, but may add other event types and details. If you are programmatically deserializing event JSON data, make sure that your application is prepared to handle unknown properties if additional properties are added.

## Athena event format
<a name="athena-events-pattern"></a>

The following is the basic pattern for an Amazon Athena event.

```
{
    "source":[
        "aws.athena"
    ],
    "detail-type":[
        "Athena Query State Change"
    ],
    "detail":{
        "currentState":[
            "SUCCEEDED"
        ]
    }
}
```

## Athena query state change event
<a name="athena-events-athena-query-state-change"></a>

The following example shows an Athena Query State Change event with the `currentState` value of `SUCCEEDED`.

```
{
    "version":"0",
    "id":"abcdef00-1234-5678-9abc-def012345678",
    "detail-type":"Athena Query State Change",
    "source":"aws.athena",
    "account":"123456789012",
    "time":"2019-10-06T09:30:10Z",
    "region":"us-east-1",
    "resources":[

    ],
    "detail":{
        "versionId":"0",
        "currentState":"SUCCEEDED",
        "previousState":"RUNNING",
        "statementType":"DDL",
        "queryExecutionId":"01234567-0123-0123-0123-012345678901",
        "workgroupName":"primary",
        "sequenceNumber":"3"
    }
}
```

The following example shows an Athena Query State Change event with the `currentState` value of `FAILED`. The `athenaError` block appears only when `currentState` is `FAILED`. For information about the values for `errorCategory` and `errorType`, see [Athena error catalog](error-reference.md).

```
{
    "version":"0",
    "id":"abcdef00-1234-5678-9abc-def012345678",
    "detail-type":"Athena Query State Change",
    "source":"aws.athena",
    "account":"123456789012",
    "time":"2019-10-06T09:30:10Z",
    "region":"us-east-1",
    "resources":[ 
    ],
    "detail":{
        "athenaError": {
            "errorCategory": 2.0, //Value depends on nature of exception
            "errorType": 1306.0, //Type depends on nature of exception
            "errorMessage": "Amazon S3 bucket not found", //Message depends on nature of exception
            "retryable":false //Retryable value depends on nature of exception
        },
        "versionId":"0",
        "currentState": "FAILED",
        "previousState": "RUNNING",
        "statementType":"DML",
        "queryExecutionId":"01234567-0123-0123-0123-012345678901",
        "workgroupName":"primary",
        "sequenceNumber":"3"
    }
}
```

### Output properties
<a name="athena-events-query-state-change-output-properties"></a>

The JSON output includes the following properties.



| Property | Description | 
| --- | --- | 
| athenaError | Appears only when currentState is FAILED. Contains information about the error that occurred, including the error category, error type, error message, and whether the action that led to the error can be retried. Values for each of these fields depend on the nature of the error. For information about the values for errorCategory and errorType, see [Athena error catalog](error-reference.md). | 
| versionId | The version number for the detail object's schema. | 
| currentState | The state that the query transitioned to at the time of the event. | 
| previousState | The state that the query transitioned from at the time of the event. | 
| statementType | The type of query statement that was run. | 
| queryExecutionId | The unique identifier for the query that ran. | 
| workgroupName | The name of the workgroup in which the query ran. | 
| sequenceNumber | A monotonically increasing number that allows for deduplication and ordering of incoming events that involve a single query that ran. When duplicate events are published for the same state transition, the sequenceNumber value is the same. When a query experiences a state transition more than once, such as queries that experience rare requeuing, you can use sequenceNumber to order events with identical currentState and previousState values. | 

## Example
<a name="athena-events-examples"></a>

The following example publishes events to an Amazon SNS topic to which you have subscribed. When Athena is queried, you receive an email. The example assumes that the Amazon SNS topic exists and that you have subscribed to it.

**To publish Athena events to an Amazon SNS topic**

1. Create the target for your Amazon SNS topic. Give the EventBridge events Service Principal `events.amazonaws.com` permission to publish to your Amazon SNS topic, as in the following example.

   ```
   {
       "Effect":"Allow",
       "Principal":{
           "Service":"events.amazonaws.com"
       },
       "Action":"sns:Publish",
       "Resource":"arn:aws:sns:us-east-1:111111111111:your-sns-topic"
   }
   ```

1. Use the AWS CLI `events put-rule` command to create a rule for Athena events, as in the following example.

   ```
   aws events put-rule --name {{{ruleName}}} --event-pattern '{"source": ["aws.athena"]}'
   ```

1. Use the AWS CLI `events put-targets` command to attach the Amazon SNS topic target to the rule, as in the following example.

   ```
   aws events put-targets --rule {{{ruleName}}} --targets Id=1,Arn=arn:aws:sns:us-east-1:111111111111:your-sns-topic
   ```

1. Query Athena and observe the target being invoked. You should receive corresponding emails from the Amazon SNS topic.

## Use AWS User Notifications with Amazon Athena
<a name="monitoring-user-notifications"></a>

You can use [AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/what-is.html) to set up delivery channels to get notified about Amazon Athena events. You receive a notification when an event matches a rule that you specify. You can receive notifications for events through multiple channels, including email, [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) chat notifications, or [AWS Console Mobile Application](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/what-is-consolemobileapp.html) push notifications. You can also see notifications in the [Console Notifications Center](https://console.aws.amazon.com/notifications/). User Notifications supports aggregation, which can reduce the number of notifications you receive during specific events. 

For more information, see the [*AWS User Notifications User Guide*](https://docs.aws.amazon.com/notifications/latest/userguide/what-is.html).