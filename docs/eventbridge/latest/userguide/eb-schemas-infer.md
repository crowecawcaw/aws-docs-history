

# Inferring schemas from event bus events in EventBridge
<a name="eb-schemas-infer"></a>

Amazon EventBridge can infer schemas by discovering events. To infer schemas, you turn on event discovery on an event bus and every unique schema is added to the schema registry, including those for cross-account events. Schemas discovered by EventBridge appear in **Discovered schemas registry** on the **Schemas** page.

If the contents of events on the event bus change, EventBridge creates new versions of the related EventBridge schema.

## Considerations when starting schema discovery on an event bus
<a name="eb-schemas-infer-considerations"></a>

Take into account the following considerations before enabling schema discover on an event bus:
+ Enabling event discovery on an event bus can incur a cost. The first five million processed events in each month are free.
+ EventBridge infers schemas from cross-account events by default but you can disable it by updating the `cross-account` property. For more information, see [Discoverers](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discoverers.html) in the EventBridge Schema Registry API Reference.

**Note**  
Schema discovery is not supported for event buses encrypted using a customer managed key. To enable schema discovery on an event bus, choose to use an AWS owned key. For more information, see [KMS key options](eb-encryption-at-rest-key-options.md).

**To start or stop schema discovery on an event bus (console)**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. In the navigation pane, choose **Event buses**.

1. Select the event bus on which you want to start or stop schema discovery.

1. Do one of the following: 
   + To start schema discovery, choose **Start discovery**.
   + To stop schema discovery, choose **Delete discovery**.

**To start or stop schema discovery on an event bus (AWS CLI)**
+ To start schema discovery, use [create-discoverer](https://docs.aws.amazon.com/cli/latest/reference/schemas/create-discoverer.html).

  To stop schema discovery, use [delete-discoverer](https://docs.aws.amazon.com/cli/latest/reference/schemas/delete-discoverer.html).

**Note**  
Schema discovery does not support events larger than 1000 KiB. These events will not be discovered and no error notification will be generated. To track schemas for larger events, you must manually create schemas using the schema registry.