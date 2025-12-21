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

## Analysis Template Created event

Below are the detail fields for the `Analysis Template Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Analysis Template Created"]
}
```

## Analysis Template Updated event

Below are the detail fields for the `Analysis Template Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Analysis Template Updated"]
}
```

## Analysis Template Deleted event

Below are the detail fields for the `Analysis Template Deleted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Analysis Template Deleted"]
}
```

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

## Collaboration Change Request Created event

Below are the detail fields for the `Collaboration Change Request Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Collaboration Change Request Created"]
}
```

## Collaboration Change Request Approved event

Below are the detail fields for the `Collaboration Change Request Approved` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Collaboration Change Request Approved"]
}
```

## Collaboration Change Request Cancelled event

Below are the detail fields for the `Collaboration Change Request Cancelled` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Collaboration Change Request Cancelled"]
}
```

## Collaboration Change Request Committed event

Below are the detail fields for the `Collaboration Change Request Committed` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Collaboration Change Request Committed"]
}
```

## Configured Table Association Created event

Below are the detail fields for the `Configured Table Association Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Configured Table Association Created"]
}
```

## Configured Table Association Updated event

Below are the detail fields for the `Configured Table Association Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Configured Table Association Updated"]
}
```

## Configured Table Association Deleted event

Below are the detail fields for the `Configured Table Association Deleted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Configured Table Association Deleted"]
}
```

## Configured Table Association Analysis Rule Created event

Below are the detail fields for the `Configured Table Association Analysis Rule Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Configured Table Association Analysis Rule Created"]
}
```

## Configured Table Association Analysis Rule Updated event

Below are the detail fields for the `Configured Table Association Analysis Rule Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Configured Table Association Analysis Rule Updated"]
}
```

## Configured Table Association Analysis Rule Deleted event

Below are the detail fields for the `Configured Table Association Analysis Rule Deleted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Configured Table Association Analysis Rule Deleted"]
}
```

## Id Mapping Table Created event

Below are the detail fields for the `Id Mapping Table Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Mapping Table Created"]
}
```

## Id Mapping Table Updated event

Below are the detail fields for the `Id Mapping Table Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Mapping Table Updated"]
}
```

## Id Mapping Table Deleted event

Below are the detail fields for the `Id Mapping Table Deleted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Mapping Table Deleted"]
}
```

## Id Namespace Association Created event

Below are the detail fields for the `Id Namespace Association Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Namespace Association Created"]
}
```

## Id Namespace Association Updated event

Below are the detail fields for the `Id Namespace Association Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Namespace Association Updated"]
}
```

###### Note

When a collaboration is deleted, the event is captured in the Id Namespace Association Updated
event in the `detail.status` field.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Namespace Association Updated"],
  "detail": {
    "status": ["COLLABORATION_DELETED"]
}
```

## Id Namespace Association Deleted event

Below are the detail fields for the `Id Namespace Association Deleted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Namespace Association Deleted"]
}
```

## Invited To Collaboration event

Below are the detail fields for the `Invited To Collaboration` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Invited To Collaboration"]
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

## Membership Deleted event

Below are the detail fields for the `Membership Deleted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Membership Deleted"]
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

## Protected Job Started event

Below are the detail fields for the `Protected Job Started` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Job Started"]
}
```

## Protected Job Cancelling event

Below are the detail fields for the `Protected Job Cancelling` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Job Cancelling"]
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

## Protected Query Submitted event

Below are the detail fields for the `Protected Query Submitted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Submitted"]
}
```

## Protected Query Started event

Below are the detail fields for the `Protected Query Started` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Started"]
}
```

## Protected Query Cancelling event

Below are the detail fields for the `Protected Query Cancelling` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Cancelling"]
}
```

## Protected Query Cancelled event

Below are the detail fields for the `Protected Query Cancelled` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Cancelled"]
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
