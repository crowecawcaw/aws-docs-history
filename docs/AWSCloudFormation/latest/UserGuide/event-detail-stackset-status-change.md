# StackSet Status Change event

detail

Below are the detail fields for StackSet Status Change events.

The `source` and `detail-type` fields are included
because they contain specific values for CloudFormation events.

```
{
  . . .,
  "detail-type": "CloudFormation StackSet Status Change",
  "source": "aws.cloudformation",
  . . .,
  "detail": {
    "stack-set-arn" : "string",
    "status-details": {
        "status":"string"
    }
  }
}
```

`detail-type`

Identifies the type of event.

For StackSet status event events, this value is `CloudFormation
 StackSet Status Change`.

`source`

Identifies the service that generated the event. For CloudFormation
events, this value is `aws.cloudformation`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For StackSet status event events, this data includes:

`stack-set-arn`

The Amazon Resource Name (ARN) associated with the stack
set.

`status-details`

`status`

The StackSet status.

_Valid values_:
`ACTIVE` | `DELETED`

###### Example: StackSet

Status Change event

The following is an example StackSet Status Change event. This event details
that CloudFormation has deleted the specified stack set.

```
{
  "version": "0",
  "id": "42h6hb90-hg0w-11op-b01v-0xhnh0934z09",
  "detail-type": "CloudFormation StackSet Status Change",
  "source": "aws.cloudformation",
  "account": "111122223333",
  "time": "2021-09-23T17:06:18Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:cloudformation:us-east-1:111122223333:stackset/test12345:3f3a3fbe-c937-4eb3-a87d-e36a0af3f663"
  ],
  "detail": {
    "stack-set-arn" : "arn:aws:cloudformation:us-east-1:111122223333:stackset/test12345:3f3a3fbe-c937-4eb3-a87d-e36a0af3f663",
    "status-details": {
        "status":"DELETED"
    }
  }
}
```
