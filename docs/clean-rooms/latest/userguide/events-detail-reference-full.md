# AWS Clean Rooms events detail reference

All events from AWS services have a common set of fields containing metadata about
the event, such as the AWS service that is the source of the event, the time the event
was generated, the account and region in which the event took place, and others. For
definitions of these general fields, see [Event structure](../../../eventbridge/latest/ref/overiew-event-structure.md "../../../eventbridge/latest/ref/overiew-event-structure.md") in
the _Amazon EventBridge Events Reference_.

In addition, each event has a `detail` field that contains data specific to
that particular event. The reference below defines the detail fields for the various
AWS Clean Rooms events.

When using EventBridge to select and manage AWS Clean Rooms events, it's useful to keep the
following in mind:

- The `source` field for all events from AWS Clean Rooms is set to
  `aws.cleanrooms`.
- The `detail-type` field specifies the event type.

For example, `Collaboration Created`.

- The `detail` field contains the data that is specific to that
  particular event.
  For information on constructing event patterns that enable rules to match AWS Clean Rooms
  events, see [Event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in
  the _Amazon EventBridge User Guide_.

## Collaboration Created event

Below are the detail fields for the `Collaboration Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Collaboration Created"]
}
```

## Collaboration Updated event

Below are the detail fields for the `Collaboration Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Collaboration Updated"]
}
```

## Membership Created event

Below are the detail fields for the `Membership Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Membership Created"]
}
```

## Membership Updated event

Below are the detail fields for the `Membership Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Membership Updated"]
}
```

###### Note

When a collaboration is deleted, the event is captured in the Membership Updated
event in the `detail.status` field.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Membership Updated"],
  "detail": {
    "status": ["COLLABORATION_DELETED"]
}
```

## Membership Deleted event

Below are the detail fields for the `Membership Deleted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Membership Deleted"]
}
```

## Protected Query Submitted event

Below are the detail fields for the `Protected Query Submitted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Submitted"]
}
```

## Protected Query Succeeded event

Below are the detail fields for the `Protected Query Succeeded` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Succeeded"]
}
```

## Protected Query Failed event

Below are the detail fields for the `Protected Query Failed` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Failed"]
}
```

## Protected Query Timed Out event

Below are the detail fields for the `Protected Query Timed Out` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Timed Out"]
}
```

## Protected Job Submitted event

Below are the detail fields for the `Protected Job Submitted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Job Submitted"]
}
```

## Protected Job Succeeded event

Below are the detail fields for the `Protected Job Succeeded` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Job Succeeded"]
}
```

## Protected Job Failed event

Below are the detail fields for the `Protected Job Failed` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Job Failed"]
}
```

## Protected Job Cancelled event

Below are the detail fields for the `Protected Job Cancelled` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Job Cancelled"]
}
```
