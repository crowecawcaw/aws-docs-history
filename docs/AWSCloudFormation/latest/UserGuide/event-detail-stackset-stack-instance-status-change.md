# StackSet Stack

Instance Status Change event detail

Below are the detail fields for StackSet stack instance status events.

The `source` and `detail-type` fields are included
because they contain specific values for events.

```
{
  . . .,
  "detail-type": "CloudFormation StackSet StackInstance Status Change",
  "source": "aws.cloudformation",
  . . .,
  "detail": {
    "stack-set-arn" : "string",
    "stack-id" : "string",
    "action" : "string",
    "status-details": {
        "status": "string",
        "status-reason": "string",
        "detailed-status": "string"
      }
    }
  }
}
```

`detail-type`

Identifies the type of event.

For StackSet stack instance status events, this value is
`CloudFormation StackSet StackInstance Status Change`.

`source`

Identifies the service that generated the event. For CloudFormation
events, this value is `aws.cloudformation`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For StackSet stack instance status events, this data includes:

`stack-set-arn`

The Amazon Resource Name (ARN) associated with the
StackSet.

`stack-id`

The unique stack ID that's associated with the stack
instance.

`action`

The type of stack set operation.

_Valid values_:
`CREATE` | `UPDATE`|
`DELETE` | `DETECT_DRIFT`

`status-details`

`status`

The StackSet instance status.

For more details, see [Stack instance status codes](stacksets-concepts.md#stack-instance-status-codes "stacksets-concepts.md#stack-instance-status-codes").

_Valid values_:
`CURRENT` | `OUTDATED`|
`INOPERABLE`

`status-reason`

Status reason of the StackSet instance.

`detailed-status`

The detailed StackSet instance detailed
status.

_Valid values_:
`CANCELLED` | `FAILED` |
`FAILED_IMPORT` |
`INOPERABLE` | `PENDING` |
`RUNNING` |
`SKIPPED_SUSPENDED_ACCOUNT` |
`SUCCEEDED`

###### Example: StackSet Stack Instance Status Change event

The following is an example StackSet Stack Instance Status Change event.

```
{
  "version": "0",
  "id": "42h6hb90-hg0w-11op-b01v-0xhnh0934z09",
  "detail-type": "CloudFormation StackSet StackInstance Status Change",
  "source": "aws.cloudformation",
  "account": "111122223333",
  "time": "2021-09-22T19:19:23Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:cloudformation:us-east-1:111122223333:stackset/test1234:e5f54eea-d041-44ad-94f8-b8268aca1e59"
  ],
  "detail": {
     "stack-set-arn": "arn:aws:cloudformation:us-east-1:111122223333:stackset/test1234:e5f54eea-d041-44ad-94f8-b8268aca1e59",
    "stack-id": "arn:aws:cloudformation:us-west-1:111122223333:stack/teststack",
    "status-details": {
        "status": "OUTDATED",
        "status-reason": "User Initiated",
        "detailed-status": "PENDING"
    }
  }
}
```
