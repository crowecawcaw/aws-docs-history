

# Event sources for a Custom Event Bus
<a name="eb-custom-bus-event-sources"></a>

An event source ingests events from an AWS service or a SaaS partner onto a Custom Event Bus. You create it with `CreateEventSource`, naming a destination bus and one origin, for example `aws.s3`, and EventBridge delivers events from the origin to the bus. Your own applications publish to the bus directly, so you need an event source only for events you do not produce yourself.

Ingested events arrive on the destination bus in the EventBridge envelope, with content type `application/eventbridge+json`. The event data holds the envelope fields: `source`, `detail-type`, `account`, `time`, `region`, `resources`, and `detail`. EventBridge also sets the `aws:Source` and `aws:DetailType` system metadata fields from the envelope's `source` and `detail-type`. See [Event structure: data, metadata, and system metadata](eb-custom-bus-addressing.md).

## How the events are moved
<a name="eb-custom-bus-event-sources-how"></a>

When you create an event source, EventBridge creates a managed rule and a target in your account, on your Custom Event Bus - Classic, and they carry events from the origin to your Custom Event Bus. Both appear in your account with `ManagedBy` set to `events.amazonaws.com`. You do not manage them; deleting or revoking the event source removes them. The events therefore still appear in the Custom Event Bus - Classic's metrics.

## AWS service event sources
<a name="eb-custom-bus-event-sources-aws"></a>

An AWS service event source ingests the events that one AWS service, such as `aws.s3` or `aws.ec2`, emits for your account. By default every event from that service arrives on the bus; to narrow that down, add a `Pattern`. The following example creates an event source that admits only Amazon S3 Object Created events.

```
aws eventsv2 create-event-source \
    --name s3-object-created \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --configuration '{"AwsServiceEventsConfiguration":{"AwsService":"aws.s3","Pattern":"{\"detail-type\":[\"Object Created\"]}"}}'
```

The event source's pattern decides what crosses onto the bus. A subscriber's filter decides what that subscriber receives from the events flowing through the bus; see [Filtering events for a subscriber](eb-custom-bus-filtering.md). Write the pattern in EventBridge event pattern syntax ([Amazon EventBridge event patterns](eb-event-patterns.md)), and EventBridge evaluates it against the envelope. Leave the `source` key and the top-level `account` and `region` keys out of the pattern: EventBridge adds those conditions itself, from your account and Region and the service you selected, and rejects a pattern that supplies them.

## Partner event sources
<a name="eb-custom-bus-event-sources-partner"></a>

A partner event source ingests the events a SaaS partner sends to your account. Before you create one, the partner must offer a partner event source to your account (see [Receiving events from a SaaS partner with Amazon EventBridge](eb-saas.md)), and that source must be in the `PENDING` state. The following example creates an event source for it.

```
aws eventsv2 create-event-source \
    --name example-partner-events \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --configuration '{"PartnerEventsConfiguration":{"PartnerEventSourceArn":"arn:aws:events:us-east-1::event-source/aws.partner/example.com/12345"}}'
```

When you create the event source, EventBridge creates a managed partner event bus (a Custom Event Bus - Classic) in your account to activate the partner source. When you delete the event source, EventBridge deletes that bus and returns the partner source to `PENDING`. To encrypt that bus with a customer managed key, set `PartnerBusKmsKeyIdentifier` to a key in your account and Region; otherwise EventBridge uses an AWS owned key.

## Dead-letter queue
<a name="eb-custom-bus-event-sources-dlq"></a>

To capture events that fail to reach the bus, set `OnFailureConfiguration.Arn` to a standard Amazon SQS queue in your account and Region; a FIFO queue is rejected. Messages arrive on the queue from the `events.amazonaws.com` service principal, not from a role you supply, so grant that principal `sqs:SendMessage` in the queue's resource policy.

```
{
    "Effect": "Allow",
    "Principal": { "Service": "events.amazonaws.com" },
    "Action": "sqs:SendMessage",
    "Resource": "arn:aws:sqs:us-east-1:111122223333:my-event-source-dlq",
    "Condition": { "StringEquals": { "aws:SourceAccount": "111122223333" } }
}
```

A partner event source sends to the queue under two source ARNs: the managed rule, for delivery failures, and the managed partner event bus, for encryption failures. A policy that conditions on `aws:SourceArn` must allow both.

## Permissions
<a name="eb-custom-bus-event-sources-access"></a>

To create an event source on a bus in another account, the bus owner must grant you `events:CreateEventSource`, through an AWS RAM share (`AWSRAMEventBridgeEventBusV2EventSourceAccess` or `FullAccess`) or with a `PutResourcePolicy` statement on the bus. The `events:source` condition key carries the AWS service name or the partner event source name, so a bus owner can allow or deny specific origins. See [Sharing a Custom Event Bus with other accounts](eb-custom-bus-sharing.md).

To encrypt the managed partner event bus, your identity needs `kms:DescribeKey` and `kms:Decrypt` on the key you name in `PartnerBusKmsKeyIdentifier`; without them, `CreateEventSource` fails with `AccessDeniedException`.

```
{
    "Effect": "Allow",
    "Action": ["kms:DescribeKey", "kms:Decrypt"],
    "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
}
```

If another account owns the destination bus and encrypts it with a customer managed key, that key's policy must also admit your account; otherwise create, update, and describe of the event source fail.

## Subscribing to ingested events
<a name="eb-custom-bus-event-sources-shape"></a>

To match AWS service or partner events on a subscriber, filter on the `aws:Source` system metadata field. EventBridge writes this field and no publish call can set a value that begins with `aws.`, so a match on its value is the only match that proves the origin of an event. For AWS service events, match the service name; for partner events, match the partner event source name.

```
{ "Scope": "SYSTEM_METADATA", "Pattern": "{\"aws:Source\":[\"aws.s3\"]}" }

{ "Scope": "SYSTEM_METADATA", "Pattern": "{\"aws:Source\":[{\"prefix\":\"aws.partner/example.com\"}]}" }
```

To filter on the event content, add a `DATA` filter. The envelope carries the content under `detail`.

```
{ "Scope": "DATA", "Pattern": "{\"detail\":{\"bucket\":{\"name\":[\"amzn-s3-demo-bucket\"]}}}" }
```

The event data also carries `source` and `detail-type`, and any publisher can write those values into a payload, so they do not prove the origin. Match `aws:Source` by value, not by presence: a direct `PutEvents` call also sets `aws:Source`, from its own `Source`, which never starts with `aws.`.

## Permanently stopping an event source
<a name="eb-custom-bus-event-sources-revoke"></a>

The bus owner can permanently stop an event source from ingesting by calling `RevokeResource` with its ARN; see [Revoking a subscriber or an event source](eb-custom-bus-access-revoke.md). A revoked event source cannot be restored. Revocation covers the one resource you name, so pair it with a bus resource policy that stops the same account from creating another. To block the account from creating any event source on the bus:

```
{
    "Effect": "Deny",
    "Principal": { "AWS": "arn:aws:iam::444455556666:root" },
    "Action": "events:CreateEventSource",
    "Resource": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef"
}
```

To block one origin while allowing others, condition the deny on `events:source`.

```
{
    "Effect": "Deny",
    "Principal": { "AWS": "arn:aws:iam::444455556666:root" },
    "Action": "events:CreateEventSource",
    "Resource": "arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef",
    "Condition": { "StringEquals": { "events:source": "aws.partner/example.com/12345" } }
}
```

## Confirming that events cross onto the bus
<a name="eb-custom-bus-event-sources-troubleshooting"></a>

Two sets of metrics show whether ingested events reach the Custom Event Bus. The managed rule reports the usual rule metrics in your account, under `AWS/Events`. The destination bus's publish metrics carry an `EventSource` dimension, which gives a per-event-source breakdown of inbound traffic; see [Observability for the Custom Event Bus: metrics, logs, and CloudTrail](eb-custom-bus-observability.md).

When a subscriber carries events from one Custom Event Bus to another across accounts, AWS service and partner events keep their `aws:Source` and `aws:DetailType` as long as the event's structure and content stay intact. EventBridge authorizes their arrival on the destination bus with `events:PutEvents`, so the destination bus's resource policy must grant that action to the forwarding role. Events your applications published take `events:PutRawEvents`, so a stream that mixes both needs both actions; see [Event bus target: bus to bus](eb-custom-bus-target-bus.md).