# Event structure

Events are represented as JSON objects, and they all have a similar structure, and the
same top-level fields. These top-level fields contain the event's metadata, such as the
source of the event, the account and region in which it occurred, and the time at which
it occurred. For more information about event metadata, see [AWS service event
metadata](../userguide/eb-events-structure.md "../userguide/eb-events-structure.md") in the _EventBridge User Guide_.

The combination of the **source** and
**detail-type** fields identify the service that has generated the event, and the type of event, respectively.
For example, in the following event snippet, `source` identifies the originating AWS service as CloudFormation, while `detail-type` shows that the event represent a change in a stack's status.

```
{
  . . .
  "source": "aws.cloudformation",
  . . .
  "detail-type": "CloudFormation Stack Status Change",
  }
}
```

The contents of the **detail** field are different depending on which
service generated the event, and what the event is. If we examine the complete event, we
can see the specific stack involved, and that the event was generated when its status
became `CREATE_COMPLETE`.

```
{
  "version": "0",
  "source": "aws.cloudformation",
  "account": "123456789012",
  "id": "12345678-1234-1234-1234-111122223333",
  "region": "us-east-1",
  "detail-type": "CloudFormation Stack Status Change",
  "time": "2022-04-31T17:00:00Z",
  "resources": ["arn:aws:cloudformation:us-east-1:123456789012:stack/teststack"],
  "detail": {
    "stack-id": "arn:aws:cloudformation:us-west-1:123456789012:stack/teststack",
    "status-details": {
      "status": "CREATE_COMPLETE",
      "status-reason": ""
    }
  }
}
```

Knowing the structure and fields present in an event enables you to create an event pattern to match against that event. For more information, see
[Event patterns](../userguide/eb-event-patterns.md "../userguide/eb-event-patterns.md") in the _EventBridge User Guide_
