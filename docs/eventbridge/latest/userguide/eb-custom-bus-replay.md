

# Replaying retained events to a subscriber
<a name="eb-custom-bus-replay"></a>

To deliver events that the bus already holds, create a subscriber with `--starting-position POINT_IN_TIME` and a starting point inside the bus's retention window, for example `--point-in-time-configuration '{ "PointType": "TIMESTAMP", "StartingPoint": "2026-09-01T00:00:00Z" }'`. There is no separate replay API: a subscriber reads retained events from its starting position, so anything still inside the retention period can be delivered again. `DescribeEventBus` returns `RetentionWindowStartTime`, the earliest point a subscriber can read from; on a new bus that is the bus's creation time, so a recent timestamp can still fall outside the window. For the retention period itself, see [Choosing the retention period](eb-custom-bus-create.md#eb-custom-bus-create-retention).

## Starting position
<a name="eb-custom-bus-retention-start"></a>

When you create a subscriber, `--starting-position` is `LATEST` to receive only events published after the subscriber exists, or `POINT_IN_TIME` to read from retained history. With `POINT_IN_TIME`, `--point-in-time-configuration` sets `PointType` to `HORIZON`, the earliest retained event, or to `TIMESTAMP` with a `StartingPoint`. The starting point must fall inside the retention window: at or after `RetentionWindowStartTime` and not in the future. An optional `EndPoint` stops the subscriber at that time. Omit `EndPoint` and the subscriber reads through the retained events, catches up to live events, and keeps delivering.

```
aws eventsv2 create-subscriber \
    --name reprocess-september \
    --event-bus-arn arn:aws:events:us-east-1:111122223333:event-busv2/orders/EXAMPLE1234567890abcdef \
    --starting-position POINT_IN_TIME \
    --point-in-time-configuration '{ "PointType": "TIMESTAMP", "StartingPoint": "2026-09-01T00:00:00Z" }' \
    --invoke-configuration '{
        "TargetArn": "arn:aws:sqs:us-east-1:111122223333:reprocess",
        "RoleArn": "arn:aws:iam::111122223333:role/EventBusDeliveryRole"
    }'
```

A replay has a startup delay and then runs at live speed. Allow for the delay before you conclude that a replay is not working. To pause a subscriber and later resume it with or without the backlog, see [Pausing and resuming](eb-custom-bus-update.md#eb-custom-bus-update-pause).

## Telling replayed events apart
<a name="eb-custom-bus-retention-marked"></a>

Every delivered event carries `SystemMetadata."aws:DeliveryType"`, which is `LIVE` for an event delivered as it arrived and `REPLAY` for an event read from retained history. Use it to make consumers idempotent during a replay.