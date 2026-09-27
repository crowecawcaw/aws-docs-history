

# What is the EventBridge Custom Event Bus?
<a name="eb-custom-bus-what-is"></a>

The EventBridge Custom Event Bus is a serverless event bus that one team runs and many teams and accounts use. You publish events to it with `PutEvents` or `PutRawEvents`. It routes each event to the subscribers whose filters match it, and it keeps a copy of every event for a retention period that you set on the bus. You share the bus with other accounts through AWS Resource Access Manager (AWS RAM), and each of those accounts attaches its own subscribers. The bus owner writes no routing on their behalf.

In the EventBridge console, the bus type is shown as **Custom Event Bus** for this bus and **Custom Event Bus - Classic** for the buses that use rules and targets. For the CLI, SDK, and IAM names, see [Names, endpoints, and IAM permissions for the Custom Event Bus](eb-custom-bus-names.md).

## Key features
<a name="eb-custom-bus-what-is-features"></a>
+ Cross-account sharing through AWS RAM, with four managed permissions that let a consumer account publish, subscribe, attach event sources, or all three.
+ Retention of every event for 1 to 365 days, set on the bus.
+ Ordered (FIFO) delivery within an event group, per subscriber.
+ A starting position for each subscriber, so a new subscriber can read retained events and a paused subscriber can resume without loss.
+ Deduplication at publish time, by content or by a key that you supply, within a 5-minute window.
+ `PutRawEvents` for JSON, Avro, Protobuf, or raw bytes, with schema registry deserialization for filtering.
+ Universal targets that call any state-changing AWS API action directly, alongside the bespoke targets.

## Resources
<a name="eb-custom-bus-what-is-resources"></a>

You work with three resources.

Event bus  
The event bus receives the events you publish with `PutEvents` or `PutRawEvents`, routes them to subscribers, and retains them. You set the retention period, an optional AWS KMS key, and optional cross-account sharing on the bus. For the states a bus moves through, see [Bus states and what each allows](eb-custom-bus-create.md#eb-custom-bus-lifecycle-states).

Subscriber  
A subscriber names the events you want, with filters, and the one target that receives them. You create it with `CreateSubscriber`. It watches one bus, keeps the events that match its filters, optionally transforms each one, and delivers it to exactly one target. To send an event to several targets, create one subscriber for each target.

Event source  
An event source ingests events onto a bus from an AWS service or from a software as a service (SaaS) partner. You create it with `CreateEventSource`, naming the origin and the destination bus, and EventBridge moves the events for you.

Bus and subscriber Amazon Resource Names (ARNs) end in an identifier that EventBridge generates, for example `arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef`. Store the full ARN rather than the name. If you delete a bus and create another with the same name, the new bus has a different identifier.

## One bus, many accounts
<a name="eb-custom-bus-what-is-sharing"></a>

To let another account use your bus, share it with AWS RAM and attach one of the managed permissions, for example `AWSRAMEventBridgeEventBusV2SubscribeOnly` to let that account attach subscribers. The account then creates and owns its own subscribers on your bus: it sees only its subscribers when it lists them, and you see all of them. A consumer account cannot change or delete the bus, and you can withdraw any of its subscribers with `RevokeResource`. For the permissions, resource policies, and revocation, see [Sharing a Custom Event Bus with other accounts](eb-custom-bus-sharing.md).

## How the Custom Event Bus routes and retains events
<a name="eb-custom-bus-what-is-retention"></a>

The bus routes each event to matching subscribers as it arrives. The bus also retains the event for the number of days that you configure. Retention makes two capabilities possible.
+ A subscriber can start from a point in the past. That is how you replay retained events, and how a subscriber that you create today reads events that were published yesterday.
+ A subscriber can pause and later resume without losing events.

For more information, see [Choosing the retention period](eb-custom-bus-create.md#eb-custom-bus-create-retention) and [Replaying retained events to a subscriber](eb-custom-bus-replay.md).

## How the Custom Event Bus differs from Custom Event Bus - Classic
<a name="eb-custom-bus-what-is-compare"></a>


| Capability | Custom Event Bus | Custom Event Bus - Classic | 
| --- | --- | --- | 
| Cross-account use | Share the bus with AWS RAM. Each consumer account creates and owns its subscribers on the bus. | Grant other accounts through the bus resource policy, or forward events to a bus in the other account. | 
| Retention | Built into the bus, for a period that you set. | Not retained. To keep events, add an archive. | 
| Ordering | FIFO delivery within an event group, per subscriber. | Not available. | 
| Replay | A subscriber's starting position over retained events. | Replay from an archive. | 
| Publish APIs | PutEvents for JSON and PutRawEvents for any format, including Avro and Protobuf. | PutEvents for JSON. | 
| Deduplication | At publish time, by content or by a key that you supply. | Not available. | 
| Targets per routing resource | One target per subscriber. | Up to five targets per rule. | 

## Use cases
<a name="eb-custom-bus-what-is-use-cases"></a>
+ A platform team runs one `orders` bus and shares it with the accounts of the fulfillment, billing, and analytics teams. Each team attaches its own subscribers; the platform team never edits routing for them.
+ A payments service publishes with an `EventGroupId` per account number and a FIFO subscriber delivers each account's events to a queue in order.
+ A new analytics consumer is created with a starting position 30 days back and reads a month of retained events before it catches up to live traffic.

## Pricing
<a name="eb-custom-bus-what-is-pricing"></a>

You pay for the events you publish, the deliveries to subscribers, and retention. For the rates, see [Amazon EventBridge pricing](https://aws.amazon.com/eventbridge/pricing/).

## Next steps
<a name="eb-custom-bus-what-is-next"></a>
+ Learn which names to use in the CLI, SDKs, and IAM: [Names, endpoints, and IAM permissions for the Custom Event Bus](eb-custom-bus-names.md).
+ Publish your first events: [Publishing events to a Custom Event Bus](eb-custom-bus-publish.md).
+ Create a subscriber that delivers them: [Subscribing to events on a Custom Event Bus](eb-custom-bus-subscribers.md).