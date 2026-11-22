

# Amazon MSK cluster target

To deliver to an Amazon MSK cluster, set `TargetArn` to the cluster ARN and add `MskParameters` with the topic to produce to. EventBridge produces one Kafka record per delivered event: the event is the record value. `MskParameters` sets each record's topic, key, and headers, and the producer's compression and acknowledgement mode. The cluster must have the connectivity path you name turned on, with IAM access control. For more information about connectivity, see [Public and private connectivity](#eb-custom-bus-target-msk-connectivity).

## Parameters
<a name="eb-custom-bus-target-msk-parameters"></a>

The following table describes the `MskParameters` fields.


| Parameter | What it sets | 
| --- | --- | 
| TopicName | Required. The Kafka topic EventBridge produces to. A literal, or a JSONata expression resolved once per delivered event. Every resolved value must be a valid Kafka topic name. | 
| Connectivity | Required. PUBLIC to reach the cluster over its public access, or PRIVATE over a private connection EventBridge establishes. A provisioned cluster can have both turned on, so you name the one to use. An Amazon MSK Serverless cluster supports only PRIVATE. See [Public and private connectivity](#eb-custom-bus-target-msk-connectivity). | 
| PartitionKey | The Kafka record key. A literal, or a JSONata expression resolved once per delivered event; the resolved value selects the partition. If you omit it, a FIFO subscriber uses the event's event group ID as the record key, so events in a group share a partition; a standard subscriber lets the producer choose. | 
| Compression | The producer compression codec applied to the record batch: NONE (the default), GZIP, SNAPPY, LZ4, or ZSTD. | 
| Acks | The producer acknowledgement mode. ALL (the default) waits for all in-sync replicas; LEADER waits for the partition leader only. | 
| Headers | Kafka record headers attached to each record, up to 100. Each header has a key and an optional value, each a literal or a JSONata expression resolved once per delivered event. | 
| ClientId | The producer client.id sent to the broker, which identifies the producer in broker-side logs, metrics, and quotas. A literal, set once when the producer connects. | 

## Public and private connectivity
<a name="eb-custom-bus-target-msk-connectivity"></a>

EventBridge reaches the cluster over the path you name in `Connectivity`. Before you create the subscriber, turn on IAM access control on the cluster, and set up the path you name:
+ For `PUBLIC`, turn on the cluster's public access. This option applies to provisioned clusters only.
+ For `PRIVATE` on a provisioned cluster, turn on the cluster's multi-VPC private connectivity with IAM, and add a cluster policy that allows EventBridge to connect.
+ For `PRIVATE` on an Amazon MSK Serverless cluster, add a cluster policy that allows EventBridge to connect. Serverless clusters have no multi-VPC setting to turn on.

In both `PRIVATE` cases, EventBridge establishes the private connection to your cluster. Private connectivity creates an AWS PrivateLink VPC endpoint to connect to the cluster, billed to the AWS account that owns the cluster. Subscribers that target the same cluster share one endpoint. You do not create or manage any networking resources for it.

Amazon MSK Serverless clusters have no public access, so `CreateSubscriber` and `UpdateSubscriber` reject `PUBLIC` connectivity for them. Private delivery to a Serverless cluster is available only in Regions where Amazon MSK Serverless is available; in other Regions, the subscriber's `ConnectivityState` becomes `PROVISION_FAILED`.

For the `PRIVATE` path, attach a cluster policy that lets EventBridge set up and use the private connection to your cluster, scoped with `aws:SourceAccount` and `aws:SourceArn` to the subscribers that deliver to it. The following example grants that access. In the example, replace the account ID, cluster name, and subscriber name with your own values.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowEventBridgePrivateConnectivity",
            "Effect": "Allow",
            "Principal": {
                "Service": "events.amazonaws.com"
            },
            "Action": [
                "kafka:CreateVpcConnection",
                "kafka:GetBootstrapBrokers",
                "kafka:DescribeClusterV2"
            ],
            "Resource": "arn:aws:kafka:us-east-1:111122223333:cluster/MyCluster/abcd1234-0abc-def0-1234-abcd1234abcd-25",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:events:us-east-1:111122223333:subscriber/my-subscriber/*"
                }
            }
        }
    ]
}
```

The condition uses `ArnLike` with a trailing wildcard because the subscriber ARN that EventBridge sends carries a generated ID you cannot know before `CreateSubscriber`. Each `PRIVATE` subscriber's creation is authorized against the cluster policy with its own ARN, even when it joins an existing shared connection. The condition must therefore match every `PRIVATE` subscriber that targets the cluster. Use `subscriber/*` to match all of your subscribers, or, for each subscriber, add a `subscriber/{{subscriber-name}}/*` pattern, replacing {{subscriber-name}} with the name of your subscriber.

## Provisioning and delivery lifecycle
<a name="eb-custom-bus-target-msk-lifecycle"></a>

An Amazon MSK subscriber has two states that you read with `DescribeSubscriber`. `State` is `RUNNING` or `STOPPED` and you control it. `SubscriberDetails.MskDetails.ConnectivityState` is `PROVISIONING`, `ACTIVE`, or `PROVISION_FAILED` and EventBridge manages it: it tracks the connectivity EventBridge sets up to the cluster. `SubscriberDetails.MskDetails.StateReason` explains a failure and is present only when `ConnectivityState` is `PROVISION_FAILED`.
+ **While `PROVISIONING`** – after you create a `PRIVATE` subscriber, it does not match or deliver events while EventBridge establishes the private connection for the first time. When `ConnectivityState` first becomes `ACTIVE`, it begins matching and delivering. A subscriber that has not yet been `ACTIVE` retains no events, unlike one that re-provisions after having been `ACTIVE` (described following). A `PUBLIC` subscriber has no connection to establish and becomes `ACTIVE` without a provisioning step.
+ **If the cluster or connection breaks** while the subscriber is delivering (for example, you change the cluster so EventBridge can no longer reach it) EventBridge keeps matching events and attempting delivery. The attempts fail and are retried; events that exhaust the retry policy go to the dead-letter queue, or are dropped if none is configured. For more information about dead-letter queues, see [Subscribing to events on a Custom Event Bus](eb-custom-bus-subscribers.md).
+ **To repair a `PRIVATE` subscriber's connectivity**, fix the cluster and then call `UpdateSubscriber` with the subscriber's `InvokeConfiguration` (the same `MskParameters`). A `PUBLIC` subscriber has no connection to re-establish, and updating it with the same `MskParameters` does not re-provision. An update that omits the invoke configuration does not re-establish the connection. You can update a subscriber only from `ACTIVE` or `PROVISION_FAILED`; an update while it is already `PROVISIONING` is rejected and can be retried. `ConnectivityState` returns to `PROVISIONING` while EventBridge re-establishes the connection. Because the subscriber has already been `ACTIVE`, it keeps matching and attempting delivery throughout, so deliveries continue to fail until the connection is restored. When it reaches `ACTIVE`, delivery of the retained events resumes. If provisioning fails, `ConnectivityState` becomes `PROVISION_FAILED`: EventBridge pauses delivery and keeps matching, so matched events are retained for delivery once you repair the cluster and update the subscriber again.

### Subscribers that share a cluster connection
<a name="eb-custom-bus-target-msk-lifecycle-shared"></a>

Private subscribers that deliver to the same cluster ARN share one connection to that cluster, so a connection problem affects them together. A shared connection behaves as follows:
+ If the connection breaks, every subscriber that uses it has the same delivery failures, retries, and dead-letter or drop behavior.
+ After you fix the cluster, call `UpdateSubscriber` with its `InvokeConfiguration` on any one of those subscribers. When that update rebuilds the connection, EventBridge also returns the other `PROVISION_FAILED` subscribers on that cluster to `ACTIVE`, provided the cluster policy still allows each one; subscribers already `ACTIVE` stay `ACTIVE`.
+ If an update fails because the cluster or its connection is unusable, EventBridge sets this subscriber and the other `ACTIVE` subscribers on that cluster to `PROVISION_FAILED`. Delivery pauses for those subscribers, but EventBridge keeps matching and retaining their events. A failure caused by one subscriber alone (for example its own `aws:SourceAccount` or `aws:SourceArn` condition) does not move the others.

## Delivery role
<a name="eb-custom-bus-target-msk-role"></a>

EventBridge assumes the subscriber's delivery role to produce to your cluster, so the role needs IAM access control permissions to look up the cluster's bootstrap brokers, connect to the cluster, and write to the topic, and must trust EventBridge to assume it (see [Subscribing to events on a Custom Event Bus](eb-custom-bus-subscribers.md)). The following example grants that access for one topic. In the example, replace the account ID, cluster name, and topic name with your own values.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "LookupBrokers",
            "Effect": "Allow",
            "Action": "kafka:GetBootstrapBrokers",
            "Resource": "arn:aws:kafka:us-east-1:111122223333:cluster/MyCluster/abcd1234-0abc-def0-1234-abcd1234abcd-25"
        },
        {
            "Sid": "Connect",
            "Effect": "Allow",
            "Action": "kafka-cluster:Connect",
            "Resource": "arn:aws:kafka:us-east-1:111122223333:cluster/MyCluster/abcd1234-0abc-def0-1234-abcd1234abcd-25"
        },
        {
            "Sid": "Produce",
            "Effect": "Allow",
            "Action": [
                "kafka-cluster:DescribeTopic",
                "kafka-cluster:WriteData"
            ],
            "Resource": "arn:aws:kafka:us-east-1:111122223333:topic/MyCluster/abcd1234-0abc-def0-1234-abcd1234abcd-25/my-topic"
        }
    ]
}
```

## Batching and ordering
<a name="eb-custom-bus-target-msk-batching"></a>

EventBridge produces one Kafka record per event. `BatchConfiguration` bounds how many records EventBridge puts into one delivery attempt; the Kafka producer then groups those records into per-partition broker requests, so one delivery attempt is not a single network call. On a FIFO subscriber, EventBridge produces an event group's records in the order they were published; set `PartitionKey` to keep related events on the same partition. For more information about batching, see [Batching deliveries to a target](eb-custom-bus-batching.md).