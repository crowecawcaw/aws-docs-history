# Integrating DynamoDB with Amazon EventBridge

Amazon DynamoDB offers DynamoDB Streams for change data capture, enabling the capture of item-level changes
in DynamoDB tables. DynamoDB Streams can invoke Lambda functions to process those changes, allowing event
driven integration with other services and applications. DynamoDB Streams also supports filtering, which
allows for efficient and targeted event processing.

DynamoDB Streams supports up to [two simultaneous
consumers](ServiceQuotas.md#limits-dynamodb-streams "ServiceQuotas.md#limits-dynamodb-streams") per shard and supports filtering through [Lambda event filtering](../../../lambda/latest/dg/invocation-eventfiltering.md "../../../lambda/latest/dg/invocation-eventfiltering.md") so
that only items which match specific criteria are processed. Some customers may have
requirements to support more than two consumers. Others may need to enrich change events
before they are processed, or use more advanced filtering and routing.

Integrating DynamoDB with EventBridge can support those requirements.

Amazon EventBridge is a serverless service that uses events to connect application components
together, making it easier for you to build scalable event-driven applications. EventBridge offers
native integration with Amazon DynamoDB through EventBridge Pipes, enabling seamless data flow from DynamoDB
to an EventBridge bus. That bus can then fan-out to multiple applications and services through a set of
rules and targets.

###### Topics

- [How it works](#eventbridge-for-dynamodb-how-it-works "#eventbridge-for-dynamodb-how-it-works")
- [Creating an integration through the console](#eventbridge-for-dynamodb-create-integration-console "#eventbridge-for-dynamodb-create-integration-console")
- [Next steps](#eventbridge-for-dynamodb-next-steps "#eventbridge-for-dynamodb-next-steps")

## How it works

The integration between DynamoDB and EventBridge pipes uses DynamoDB Streams to capture a time-ordered
sequence of item-level changes in a DynamoDB table. Each record captured this way contains
the data modified in the table.

![Image showing how DynamoDB Streams integrate with an Amazon EventBridge bus.](images/eventbridge-dynamodb.png)

An EventBridge pipe consumes events from DynamoDB Streams and routes them to a target such as an EventBridge bus
(an event bus is a router that receives events and delivers them to destinations, also
called targets). Delivery is based on which rules match the contents of the event.
Optionally, the pipe also includes the ability to filter for specific events and perform
enrichments on the event data before sending it to the target.

While EventBridge supports [multiple target types](../../../eventbridge/latest/userguide/eb-targets.md "../../../eventbridge/latest/userguide/eb-targets.md"), a
common choice when implementing a fan-out design is to use a Lambda function as the
target. The following example demonstrates an integration with a Lambda function
target.

## Creating an integration through the console

Follow the steps below to create an integration through the AWS Management Console.

1. Enable DynamoDB Streams on the source table by following the steps in the
   [Enabling a stream](Streams.md#Streams.Enabling "Streams.md#Streams.Enabling") section
   of the DynamoDB developer guide. If DynamoDB Streams is already enabled on the source table,
   verify that there are currently fewer than two consumers. Consumers could be
   Lambda functions, DynamoDB Global Tables, Amazon DynamoDB zero-ETL integrations with
   Amazon OpenSearch Service, or applications that read directly from streams such as through the
   DynamoDB Streams Kinesis adapter.
2. Create an EventBridge event bus by following the steps in the [Creating an
   Amazon EventBridge event bus](../../../eventbridge/latest/userguide/eb-create-event-bus.md "../../../eventbridge/latest/userguide/eb-create-event-bus.md") section of the EventBridge user guide.
   1. When creating the event bus, enable **Schema
      discovery**.

3. Create an EventBridge pipe by following the steps in the [Creating an Amazon EventBridge pipe](../../../eventbridge/latest/userguide/eb-pipes-create.md "../../../eventbridge/latest/userguide/eb-pipes-create.md") section of the EventBridge user guide.
   1. When configuring the source, in the **Source** field select _DynamoDB_ and in
      the **DynamoDB Streams** field select the name of the
      source table stream.
   2. When configuring the target, in the **Target
      service** field select _EventBridge event
      bus_ and in the **Event bus as target** field select the event bus created in step 2.

4. Write an example item to the source DynamoDB table to trigger an event. This will
   allow EventBridge to infer schema from the example item. This schema can be used to
   create rules for routing events. For example, if you are implementing a design
   pattern that involves [overloading
   attributes](bp-gsi-overloading.md "bp-gsi-overloading.md"), you may want to trigger different rules depending on the
   value of your sort key. Details on how to write an item to DynamoDB can be found in
   the [Working with items and
   attributes](WorkingWithItems.md#WorkingWithItems.WritingData "WorkingWithItems.md#WorkingWithItems.WritingData") section of the DynamoDB developer guide.
5. Create an example Python Lambda function to be used as a target by following
   the steps in the [Building Lambda functions with
   Python](../../../lambda/latest/dg/lambda-python.md "../../../lambda/latest/dg/lambda-python.md") section of the Lambda developer guide. When creating your
   function, you can use the below example code to demonstrate the integration.
   When invoked, it will print the `NewImage` and `OldImage`
   received with the event which can be viewed in CloudWatch Logs.

```
import json

def lambda_handler(event, context):
    dynamodb = event.get('detail', {}).get('dynamodb', {})
    new_image = dynamodb.get('NewImage')
    old_image = dynamodb.get('OldImage')

    if new_image:
        print("NewImage:", json.dumps(new_image, indent=2))
    if old_image:
        print("OldImage:", json.dumps(old_image, indent=2))

    return {'statusCode': 200, 'body': json.dumps(event)}

```

6. Create an EventBridge rule that will route events to your new Lambda function by
   following the steps in the [Create a rule](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md")
   section that reacts to events EventBridge user guide.
   1. When defining the rule detail, select the name of the event bus you
      created in step 2 as the **Event
      bus**.
   2. When building the event pattern, follow the guide for **Existing schema**. Here, you can select the
      _discovered-schemas_ registry and the discovered
      schema for your event. This allows you to configure an event pattern
      specific to your use case that only routes messages that match specific
      attributes. For example, if you wanted to match only on DynamoDB items
      where the SK begins with `“user#”`, you’d use a configuration
      like this.

   ![Image showing an EventBridge rule where only DynamoDB items that have a sort key beginning with "user#" is displayed.](images/eventbridge-rule-example.png) 3. Click **Generate event pattern in JSON**
   after you’ve finished designing a pattern against your schema. If you
   instead want to match all events that appear on DynamoDB Streams, use the following
   JSON for the event pattern.

   ```
   {
     "source": ["aws.dynamodb"]
   }

   ```

   4. When selecting targets, follow the guide for AWS service. In the
      Select a target field, choose “Lambda function”. In the Function field,
      select the Lambda function you created in step 5.

7. You can now stop schema discovery on your event bus by following the steps in
   the [Starting or stopping schema discovery on event buses](../../../eventbridge/latest/userguide/event-bus-update.md#event-bus-update-schema "../../../eventbridge/latest/userguide/event-bus-update.md#event-bus-update-schema") section of the
   EventBridge user guide.
8. Write a second example item to the source DynamoDB table to trigger an event.
   Validate that the event was successfully processed at each step.
   1. View the CloudWatch metric **PutEventsApproximateSuccessCount** for your event bus by
      following the [Monitoring
      Amazon EventBridge](../../../eventbridge/latest/userguide/eb-monitoring.md "../../../eventbridge/latest/userguide/eb-monitoring.md") section of the EventBridge user guide.
   2. View function logs for your Lambda function by following the [Monitoring and troubleshooting Lambda functions](../../../lambda/latest/dg/lambda-monitoring.md "../../../lambda/latest/dg/lambda-monitoring.md") section of
      the Lambda developer guide. If your Lambda function uses the example code
      provided, you should see the `NewImage` and
      `OldImage` from DynamoDB Streams printed in the CloudWatch Logs log
      group.
   3. View the **Error count and success rate
      (%)** metric for your Lambda function by following the
      [Monitoring and
      troubleshooting Lambda functions](../../../lambda/latest/dg/lambda-monitoring.md "../../../lambda/latest/dg/lambda-monitoring.md") section of the Lambda
      developer guide.

## Next steps

This example provides a basic integration with a single Lambda function as a target.
For a better understanding of more complex configurations, such as creating multiple
rules, creating multiple targets, integrating with other services, and enriching events
see the complete EventBridge user guide: [Getting started with
EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md").

###### Note

Be aware of any EventBridge quotas that might be relevant to your application. While DynamoDB Streams
capacity scales with your table, EventBridge quotas are separate. Common quotas to be aware
of in a large application would be **Invocations throttle limit
in transactions per second** and **PutEvents
throttle limit in transactions per second**. These quotas specify the
number of invocations that can be sent to targets and the number of events that can
be put into the bus per second.
