

# AWS Clean Rooms events detail reference
<a name="events-detail-reference-full"></a>

All events from AWS services have a common set of fields containing metadata about the event, such as the AWS service that is the source of the event, the time the event was generated, the account and region in which the event took place, and others. For definitions of these general fields, see [Event structure](https://docs.aws.amazon.com/eventbridge/latest/ref/overiew-event-structure.html) in the *Amazon EventBridge Events Reference*. 

In addition, each event has a `detail` field that contains data specific to that particular event. The reference below defines the detail fields for the various AWS Clean Rooms events.

When using EventBridge to select and manage AWS Clean Rooms events, it's useful to keep the following in mind:
+ The `source` field for all events from AWS Clean Rooms is set to `aws.cleanrooms`.
+ The `detail-type` field specifies the event type. 

  For example, `Collaboration Created`.
+ The `detail` field contains the data that is specific to that particular event. 

For information on constructing event patterns that enable rules to match AWS Clean Rooms events, see [Event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *Amazon EventBridge User Guide*.

## Analysis Template Created event
<a name="event-detail-analysis-template-created"></a>

Below are the detail fields for the `Analysis Template Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Analysis Template Created"]
}
```

## Analysis Template Updated event
<a name="event-detail-analysis-template-updated"></a>

Below are the detail fields for the `Analysis Template Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Analysis Template Updated"]
}
```

## Analysis Template Deleted event
<a name="event-detail-analysis-template-deleted"></a>

Below are the detail fields for the `Analysis Template Deleted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Analysis Template Deleted"]
}
```

## Collaboration Created event
<a name="event-detail-collaboration-created"></a>

Below are the detail fields for the `Collaboration Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Collaboration Created"]
}
```

## Collaboration Updated event
<a name="event-detail-collaboration-updated"></a>

Below are the detail fields for the `Collaboration Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Collaboration Updated"]
}
```

## Collaboration Change Request Created event
<a name="event-detail-collaboration-change-request-created"></a>

Below are the detail fields for the `Collaboration Change Request Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Collaboration Change Request Created"]
}
```

## Collaboration Change Request Approved event
<a name="event-detail-collaboration-change-request-approved"></a>

Below are the detail fields for the `Collaboration Change Request Approved` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Collaboration Change Request Approved"]
}
```

## Collaboration Change Request Cancelled event
<a name="event-detail-collaboration-change-request-cancelled"></a>

Below are the detail fields for the `Collaboration Change Request Cancelled` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Collaboration Change Request Cancelled"]
}
```

## Collaboration Change Request Committed event
<a name="event-detail-collaboration-change-request-committed"></a>

Below are the detail fields for the `Collaboration Change Request Committed` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Collaboration Change Request Committed"]
}
```

## Configured Table Association Created event
<a name="event-detail-configured-table-association-created"></a>

Below are the detail fields for the `Configured Table Association Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Configured Table Association Created"]
}
```

## Configured Table Association Updated event
<a name="event-detail-configured-table-association-updated"></a>

Below are the detail fields for the `Configured Table Association Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Configured Table Association Updated"]
}
```

## Configured Table Association Deleted event
<a name="event-detail-configured-table-association-deleted"></a>

Below are the detail fields for the `Configured Table Association Deleted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Configured Table Association Deleted"]
}
```

## Configured Table Association Analysis Rule Created event
<a name="event-detail-configured-table-association-analysis-rule-created"></a>

Below are the detail fields for the `Configured Table Association Analysis Rule Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Configured Table Association Analysis Rule Created"]
}
```

## Configured Table Association Analysis Rule Updated event
<a name="event-detail-configured-table-association-analysis-rule-updated"></a>

Below are the detail fields for the `Configured Table Association Analysis Rule Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Configured Table Association Analysis Rule Updated"]
}
```

## Configured Table Association Analysis Rule Deleted event
<a name="event-detail-configured-table-association-analysis-rule-deleted"></a>

Below are the detail fields for the `Configured Table Association Analysis Rule Deleted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Configured Table Association Analysis Rule Deleted"]
}
```

## Id Mapping Table Created event
<a name="event-detail-id-mapping-table-created"></a>

Below are the detail fields for the `Id Mapping Table Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Mapping Table Created"]
}
```

## Id Mapping Table Updated event
<a name="event-detail-id-mapping-table-updated"></a>

Below are the detail fields for the `Id Mapping Table Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Mapping Table Updated"]
}
```

## Id Mapping Table Deleted event
<a name="event-detail-id-mapping-table-deleted"></a>

Below are the detail fields for the `Id Mapping Table Deleted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Mapping Table Deleted"]
}
```

## Id Namespace Association Created event
<a name="event-detail-id-namespace-association-created"></a>

Below are the detail fields for the `Id Namespace Association Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Namespace Association Created"]
}
```

## Id Namespace Association Updated event
<a name="event-detail-id-namespace-association-updated"></a>

Below are the detail fields for the `Id Namespace Association Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Namespace Association Updated"]
}
```

**Note**  
When a collaboration is deleted, the event is captured in the Id Namespace Association Updated event in the `detail.status` field.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Namespace Association Updated"],
  "detail": {
    "status": ["COLLABORATION_DELETED"]
}
```

## Id Namespace Association Deleted event
<a name="event-detail-id-namespace-association-deleted"></a>

Below are the detail fields for the `Id Namespace Association Deleted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Id Namespace Association Deleted"]
}
```

## Invited To Collaboration event
<a name="event-detail-invited-to-collaboration"></a>

Below are the detail fields for the `Invited To Collaboration` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Invited To Collaboration"]
}
```

## Membership Created event
<a name="event-detail-membership-created"></a>

Below are the detail fields for the `Membership Created` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Membership Created"]
}
```

## Membership Updated event
<a name="event-detail-membership-updated"></a>

Below are the detail fields for the `Membership Updated` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Membership Updated"]
}
```

## Membership Deleted event
<a name="event-detail-membership-deleted"></a>

Below are the detail fields for the `Membership Deleted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Membership Deleted"]
}
```

## Protected Job Submitted event
<a name="event-detail-protected-job-submitted"></a>

Below are the detail fields for the `Protected Job Submitted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Job Submitted"]
}
```

## Protected Job Started event
<a name="event-detail-protected-job-started"></a>

Below are the detail fields for the `Protected Job Started` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Job Started"]
}
```

## Protected Job Cancelling event
<a name="event-detail-protected-job-cancelling"></a>

Below are the detail fields for the `Protected Job Cancelling` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Job Cancelling"]
}
```

## Protected Job Cancelled event
<a name="event-detail-protected-job-cancelled"></a>

Below are the detail fields for the `Protected Job Cancelled` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Job Cancelled"]
}
```

## Protected Job Succeeded event
<a name="event-detail-protected-job-succeeded"></a>

Below are the detail fields for the `Protected Job Succeeded` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Job Succeeded"]
}
```

## Protected Job Failed event
<a name="event-detail-protected-job-failed"></a>

Below are the detail fields for the `Protected Job Failed` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Job Failed"]
}
```

## Protected Query Submitted event
<a name="event-detail-protected-query-submitted"></a>

Below are the detail fields for the `Protected Query Submitted` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Submitted"]
}
```

## Protected Query Started event
<a name="event-detail-protected-query-started"></a>

Below are the detail fields for the `Protected Query Started` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Started"]
}
```

## Protected Query Cancelling event
<a name="event-detail-protected-query-cancelling"></a>

Below are the detail fields for the `Protected Query Cancelling` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Cancelling"]
}
```

## Protected Query Cancelled event
<a name="event-detail-protected-query-cancelled"></a>

Below are the detail fields for the `Protected Query Cancelled` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Cancelled"]
}
```

## Protected Query Succeeded event
<a name="event-detail-protected-query-succeeded"></a>

Below are the detail fields for the `Protected Query Succeeded` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Succeeded"]
}
```

## Protected Query Failed event
<a name="event-detail-protected-query-failed"></a>

Below are the detail fields for the `Protected Query Failed` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Failed"]
}
```

## Protected Query Timed Out event
<a name="event-detail-protected-query-timed-out"></a>

Below are the detail fields for the `Protected Query Timed Out` event.

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["Protected Query Timed Out"]
}
```