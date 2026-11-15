

# Game session placement insights
<a name="queues-placement-insights"></a>

Game session placement insights give you detailed logs about how Amazon GameLift Servers processes game session placement requests through a game session queue. The logs show how Amazon GameLift Servers applied the queue's priority configuration, along with player latency and cost data, to each game session placement request. Use game session placement insights to diagnose why game session placements succeed, fail, or time out.

## Enable game session placement insights
<a name="queues-placement-insights-enable"></a>

You turn on game session placement insight logging in the game session queue's log configuration when you create or update a game session queue. When logging is enabled, Amazon GameLift Servers delivers a set of log records for each game session placement. You can deliver logs to Amazon CloudWatch Logs, Amazon S3, and Amazon Data Firehose. Set 1 to 3 destinations in the game session queue's log configuration `DeliveryDestinations` list. Each destination has a `LogDestination` (`CLOUDWATCH`, `S3`, or `FIREHOSE`) and an optional `DestinationArn`. For more information about log destination fields, see [CreateGameSessionQueue](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateGameSessionQueue.html) and [UpdateGameSessionQueue](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateGameSessionQueue.html) in the *Amazon GameLift Servers API Reference*.

The following rules apply to delivery destinations:
+ A `DestinationArn` must be in the same AWS account and AWS Region as the game session queue.
+ If you choose a `CLOUDWATCH` destination and don't specify a `DestinationArn`, Amazon GameLift Servers delivers logs to a default log group named `gameliftservers/queueplacement`.
+ If you choose an `S3` destination and don't specify a `DestinationArn`, Amazon GameLift Servers creates a bucket on your behalf. To get the bucket name, call `DescribeGameSessionQueues`.
+ A `FIREHOSE` destination requires the ARN of an existing delivery stream. Amazon GameLift Servers doesn't create delivery streams.
+ To change the destinations of an existing game session queue, use `AddLogDeliveryDestinations` and `RemoveLogDeliveryDestinations`. Each entry in `RemoveLogDeliveryDestinations` requires a `DestinationArn`. If you remove every destination, Amazon GameLift Servers turns off logging for the game session queue.
+ When you delete a game session queue, Amazon GameLift Servers deletes the CloudWatch Logs delivery source, delivery destinations, and deliveries that it created for the queue. It doesn't delete log groups, buckets, delivery streams, or delivered logs.

**Note**  
Amazon CloudWatch Logs vended log charges apply to each destination. Amazon S3 and Amazon Data Firehose destinations also incur their own service charges. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

### Set up log delivery
<a name="queues-placement-insights-enable-paths"></a>

Amazon GameLift Servers delivers game session placement insight logs through Amazon CloudWatch Logs vended log delivery. A delivery uses three CloudWatch Logs resources: a delivery source (the game session queue), a delivery destination, and a delivery that connects them. You can set up these resources in either of the following ways:
+ **Through Amazon GameLift Servers** – Set the game session queue's log configuration with the Amazon GameLift Servers API operations or the Amazon GameLift Servers console. Amazon GameLift Servers creates and manages the delivery resources. If you change these resources outside Amazon GameLift Servers, for example, with the CloudWatch Logs API operations, Amazon GameLift Servers doesn't detect the change.
+ **Through Amazon CloudWatch Logs** – Call `PutDeliverySource` with the game session queue ARN as the resource ARN and `QUEUE_PLACEMENT_LOGS` as the log type. Then call `PutDeliveryDestination` and `CreateDelivery`. Amazon GameLift Servers doesn't track these resources, so `DescribeGameSessionQueues` doesn't return them in the queue's `LogConfiguration`. For more information about enabling logging from AWS services, see [Enable logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) in the *Amazon CloudWatch Logs User Guide*.

Use only one of these methods for each game session queue.

### IAM permissions for log delivery
<a name="queues-placement-insights-enable-permissions"></a>

When you set a log configuration through Amazon GameLift Servers, Amazon GameLift Servers uses your credentials to create and delete CloudWatch Logs delivery resources in your account. The AWS Identity and Access Management (IAM) identity that calls Amazon GameLift Servers must have the CloudWatch Logs permissions for each destination type that you use. For the required permissions, see the following topics in the *Amazon CloudWatch Logs User Guide*:
+ [Logs sent to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-CloudWatchLogs.html)
+ [Logs sent to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.html)
+ [Logs sent to Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-Firehose.html)

In addition, the IAM identity must have the `gamelift:AllowVendedLogDeliveryForResource` permission for the game session queue. If you add a destination without a `DestinationArn`, the identity must also have the following permission for the destination type:
+ `CLOUDWATCH` – `logs:CreateLogGroup`
+ `S3` – `s3:CreateBucket`, `s3:PutBucketPolicy`, and `s3:GetBucketPolicy`

The following example policy grants the permissions that Amazon GameLift Servers needs for log delivery for one game session queue. Replace {{region}}, {{account-id}}, {{queue-name}}, {{bucket-name}}, and {{stream-name}} with your values. {{bucket-name}} and {{stream-name}} are the bucket and delivery stream that you specify in `DestinationArn`. Remove the statements for destinations that you don't use. The `CreateDefaultDestinations` statement is needed only if you omit `DestinationArn` for a `CLOUDWATCH` or `S3` destination.

------
#### [ JSON ]

****  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ServiceLevelAccessForLogDelivery",
            "Effect": "Allow",
            "Action": [
                "gamelift:AllowVendedLogDeliveryForResource"
            ],
            "Resource": "arn:aws:gamelift:{{region}}:{{account-id}}:gamesessionqueue/{{queue-name}}"
        },
        {
            "Sid": "ReadWriteAccessForLogDeliveryActions",
            "Effect": "Allow",
            "Action": [
                "logs:GetDelivery",
                "logs:GetDeliverySource",
                "logs:PutDeliveryDestination",
                "logs:GetDeliveryDestinationPolicy",
                "logs:DeleteDeliverySource",
                "logs:PutDeliveryDestinationPolicy",
                "logs:CreateDelivery",
                "logs:GetDeliveryDestination",
                "logs:PutDeliverySource",
                "logs:DeleteDeliveryDestination",
                "logs:DeleteDeliveryDestinationPolicy",
                "logs:DeleteDelivery",
                "logs:UpdateDeliveryConfiguration"
            ],
            "Resource": [
                "arn:aws:logs:{{region}}:{{account-id}}:delivery:*",
                "arn:aws:logs:{{region}}:{{account-id}}:delivery-source:*",
                "arn:aws:logs:{{region}}:{{account-id}}:delivery-destination:*"
            ]
        },
        {
            "Sid": "AllowUpdatesToResourcePolicyCWL",
            "Effect": "Allow",
            "Action": [
                "logs:PutResourcePolicy",
                "logs:DescribeResourcePolicies",
                "logs:DescribeLogGroups"
            ],
            "Resource": "arn:aws:logs:{{region}}:{{account-id}}:*"
        },
        {
            "Sid": "AllowUpdatesToResourcePolicyS3",
            "Effect": "Allow",
            "Action": [
                "s3:PutBucketPolicy",
                "s3:GetBucketPolicy"
            ],
            "Resource": "arn:aws:s3:::{{bucket-name}}"
        },
        {
            "Sid": "AllowUpdatesToResourcePolicyFH",
            "Effect": "Allow",
            "Action": [
                "firehose:TagDeliveryStream"
            ],
            "Resource": "arn:aws:firehose:{{region}}:{{account-id}}:deliverystream/{{stream-name}}"
        },
        {
            "Sid": "CreateServiceLinkedRoleFH",
            "Effect": "Allow",
            "Action": [
                "iam:CreateServiceLinkedRole"
            ],
            "Resource": "arn:aws:iam::{{account-id}}:role/aws-service-role/delivery.logs.amazonaws.com/AWSServiceRoleForLogDelivery"
        },
        {
            "Sid": "CreateDefaultDestinations",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "s3:CreateBucket",
                "s3:PutBucketPolicy",
                "s3:GetBucketPolicy"
            ],
            "Resource": [
                "arn:aws:logs:{{region}}:{{account-id}}:log-group:gameliftservers/queueplacement",
                "arn:aws:s3:::gameliftservers-*-{{account-id}}-{{region}}"
            ]
        }
    ]
}
```

------

## Understand game session placement insight logs
<a name="queues-placement-insights-schema"></a>

Amazon GameLift Servers emits multiple log records over the lifecycle of a single game session placement. All records for one game session placement share the same `placement_id`, so you can group and order the records to reconstruct the full history of a game session placement.

### Common log record fields
<a name="queues-placement-insights-fields"></a>

Every game session placement insight log record includes the following fields.


| Field | Description | 
| --- | --- | 
| `resource_arn` | The Amazon Resource Name (ARN) of the game session queue that processed the game session placement. | 
| `event_timestamp` | The time at which the event occurred. | 
| `placement_id` | The identifier of the game session placement. All records for the same game session placement share this value. | 
| `event_type` | The type of event that the record describes. See the event types table that follows. | 
| `summary` | A human-readable summary of the event. | 
| `data` | An event-specific payload. The contents depend on the `event_type`. | 

### Event types
<a name="queues-placement-insights-event-types"></a>

The `event_type` field identifies the stage of game session placement that a record describes.


| Event type | Description | 
| --- | --- | 
| `placement_started` | A game session placement request began. | 
| `destinations_evaluated` | Amazon GameLift Servers evaluated and prioritized candidate fleet locations. | 
| `game_session_creation` | Amazon GameLift Servers attempted to create the game session on a destination. | 
| `latency_policy_updated` | The active player-latency limit changed during the game session placement. | 
| `placement_ended` | The game session placement reached a terminal state. | 

When a game session placement ends, the `placement_ended` record reports one of the following terminal `status` values in `data.status`.
+ `FULFILLED` – The game session placement created a game session on a destination.
+ `TIMED_OUT` – The game session placement reached the game session queue's timeout limit before a game session could be created.
+ `FAILED` – The game session placement could not be completed.
+ `CANCELLED` – The game session placement was canceled before it reached another terminal state.

### Event data fields
<a name="queues-placement-insights-data-fields"></a>

The `data` payload carries event-specific diagnostic detail. The following list describes the `data` fields for each event type, in the order that the events typically occur during a game session placement.

`placement_started`.`data`  
+ `player_count` – The number of players in the game session placement request.
+ `regional_latencies_ms` – The player latency reported for each AWS Region, as `avg` and `max` values in milliseconds. Amazon GameLift Servers uses these values to prioritize destinations.
+ `priority_configuration_override` – Present when the request overrides the game session queue's priority configuration. Includes `location_order` (the ordered list of locations) and `placement_fallback_strategy`.

`destinations_evaluated`.`data`  
+ `round` – The evaluation round. Amazon GameLift Servers re-evaluates destinations as conditions change during a game session placement.
+ `total_destinations` – The number of destinations considered in this round.
+ `viable_destinations` – The number of destinations that passed filtering in this round.
+ `sorted_destinations` – Every destination that Amazon GameLift Servers considered in this round, including the ones it filtered out. Each entry is a location destination object.
+ `filtered_out_reasons` – A map of `viability_reason` to the destinations that were excluded for that reason. Each excluded destination lists its `fleet_arn` and `location_name`.
+ `active_player_latency_threshold_ms` – The player-latency limit in effect for this round, if a latency policy applies.

`game_session_creation`.`data`  
+ `attempt` – The sequence number of this creation attempt within the game session placement.
+ `fleet_arn` – The ARN of the fleet that the attempt targeted.
+ `location_name` – The fleet location that the attempt targeted.
+ `compute_type` – The compute type of the destination (`EC2`, `Anywhere`, or `Container`).
+ `billing_type` – The billing type of the destination (`ON_DEMAND` or `SPOT`).
+ `instance_type` – The instance type of the destination.
+ `result` – The outcome of the attempt (`ACTIVE`, `ERROR`, or `TERMINATED`).
+ `failure_reason` – Present when the result is `ERROR`. Describes why the attempt failed.
+ `game_session_arn` – Present when the result is `ACTIVE` or `TERMINATED`. The ARN of the game session that was created.
+ `active_player_latency_threshold_ms` – The player-latency limit in effect for the attempt.

`latency_policy_updated`.`data`  
+ `max_player_latency_ms` – The new active player-latency limit, in milliseconds.
+ `period_start_timestamp` – When the limit takes effect.
+ `period_end_timestamp` – When the limit stops applying. A `null` value means the limit applies until the game session queue times out.

`placement_ended`.`data`  
+ `status` – The terminal status of the game session placement (`FULFILLED`, `TIMED_OUT`, `FAILED`, or `CANCELLED`).
+ `duration` – An object that breaks down the game session placement time, in milliseconds:
  + `total_ms` – The total time for the game session placement.
  + `fleet_capacity_wait_ms` – The time spent waiting for available fleet capacity.
  + `failed_activation_ms` – The time spent retrying failed game server process activations.
  + `activation_wait_ms` – The time spent waiting for the successful game server process to activate.
+ `fulfilled_destination` – Present when the status is `FULFILLED`. A location destination object plus the `game_session_arn` of the game session that was created.
+ `location_destinations` – The list of location destinations that were evaluated for the game session placement.

A location destination object appears in `location_destinations` and in `fulfilled_destination`. It describes a single evaluated fleet location.


| Field | Description | 
| --- | --- | 
| `fleet_arn` | The ARN of the fleet. | 
| `location_name` | The fleet location. | 
| `viability_reason` | Why the location was or wasn't used. See the viability reasons that follow. | 
| `average_player_latency` | The average player latency for the location, when player latency data is included in the placement request. | 
| `max_player_latency` | The maximum player latency for the location, when player latency data is included in the placement request. | 
| `cost` | The estimated cost per server process for the destination. Amazon GameLift Servers prioritizes lower-cost destinations. | 
| `compute_type` | The compute type of the destination (`EC2`, `Anywhere`, or `Container`). | 
| `billing_type` | The billing type of the destination (`ON_DEMAND` or `SPOT`). | 
| `instance_type` | The instance type of the destination. | 

A field is `null` when it doesn't apply to the destination. For example, an Anywhere fleet reports `null` for latency, cost, and instance type.

The `viability_reason` field explains the disposition of each evaluated location destination.


| Viability reason | Description | 
| --- | --- | 
| `PLACEMENT_SUCCEEDED` | The game session was placed on this destination. | 
| `VIABLE_NOT_ATTEMPTED` | The destination was viable but wasn't attempted, because the game session placement was fulfilled or stopped on a higher-priority destination first. | 
| `GAME_SESSION_ACTIVATION_FAILED` | Amazon GameLift Servers created a game session on this destination, but the game session didn't activate. The game session ended or the game session placement timed out. | 
| `DESTINATION_NOT_ACTIVE` | The destination fleet wasn't in an `ACTIVE` status. | 
| `DESTINATION_CAPACITY_EXCEEDED` | The destination had no available capacity for the game session. | 
| `DESTINATION_THROTTLED` | The Amazon GameLift Servers request to create the game session in this destination was throttled, so Amazon GameLift Servers moved on to the next destination. | 
| `DESTINATION_NOT_IN_ALLOWED_LOCATIONS` | The destination's location wasn't among the locations allowed for the game session placement request. | 
| `DESTINATION_NOT_IN_PRIORITY_CONFIGURATION_OVERRIDE_LOCATION_ORDER` | The destination's location wasn't included in the priority configuration override's location order. | 
| `SKIPPED_RECENTLY_NOT_AVAILABLE` | The destination was skipped because of recent repeated failures that marked it temporarily unavailable. | 
| `SKIPPED_SPOT_INSTANCE_VIABILITY_BELOW_THRESHOLD` | The Spot destination was skipped because its instance viability rating was below the required threshold. | 
| `SKIPPED_MAXIMUM_LATENCY_EXCEEDED_THRESHOLD` | The destination was skipped because its player latency exceeded the game session queue's latency policy limit. | 
| `ERROR_DESTINATION_NOT_FOUND` | The destination fleet or its location couldn't be found during the game session placement attempt. | 
| `ERROR_INTERNAL` | An internal Amazon GameLift Servers error prevented the game session placement in this destination. | 

**Log delivery**  
Amazon GameLift Servers delivers game session placement insight logs asynchronously after a game session placement reaches a terminal state. The logs don't affect the game session placement itself. If you deliver logs to Amazon CloudWatch Logs, individual log events are subject to the CloudWatch Logs limit of 1 MB per event.

## Diagnose game session placement with CloudWatch Logs Insights
<a name="queues-placement-insights-queries"></a>

After you deliver game session placement insight logs to Amazon CloudWatch Logs, use CloudWatch Logs Insights to run queries against them. For more information about running queries, see [Analyze log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) in the *Amazon CloudWatch Logs User Guide*. The `data` payload is a structured object, so you can reference its fields directly with dot notation, such as `data.status` or `data.duration.total_ms`. Run the following queries against the log group where you deliver the game session queue's logs.

View the full timeline of a single game session placement, in the order that the events occurred.

```
filter placement_id = "{{placement-id}}"
| sort event_timestamp asc
| display event_timestamp, event_type, summary
```

View the most recent records for a game session queue. Records don't include a queue name field, so the query matches the end of `resource_arn`.

```
filter resource_arn like /:gamesessionqueue\/{{queue-name}}$/
| sort event_timestamp desc
| display event_timestamp, placement_id, event_type, summary
```

Find game session placements that timed out.

```
filter event_type = "placement_ended" and data.status = "TIMED_OUT"
| sort event_timestamp desc
```

See which fleet location each fulfilled game session placement landed on, including the billing type and total placement time.

```
filter event_type = "placement_ended" and data.status = "FULFILLED"
| display event_timestamp, placement_id, data.fulfilled_destination.location_name, data.fulfilled_destination.billing_type, data.duration.total_ms
```

Find the most common game session creation failure reasons.

```
filter event_type = "game_session_creation" and data.result = "ERROR"
| stats count(*) as failures by data.failure_reason
| sort failures desc
```

Measure game session placement duration for fulfilled game session placements, including the average and the 95th and 99th percentiles.

```
filter event_type = "placement_ended" and data.status = "FULFILLED"
| stats avg(data.duration.total_ms) as avg_ms, pct(data.duration.total_ms, 95) as p95_ms, pct(data.duration.total_ms, 99) as p99_ms
```

Find game session placements that required multiple game session creation attempts.

```
filter event_type = "game_session_creation"
| stats count(*) as attempts by placement_id
| filter attempts > 1
| sort attempts desc
```