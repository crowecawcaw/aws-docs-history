# StackSet Operation
 Status Change event detail

Below are the detail fields for StackSet Operation Status Change events.

The `source` and `detail-type` fields are included
 because they contain specific values for AWS CloudFormation events.


```
{
  . . .,
  "detail-type": "CloudFormation StackSet Operation Status Change",
  "source": "aws.cloudformation",
  . . .,
  "detail": {
    "stack-set-arn" : "string",
    "stack-set-operation-id" : "string",
    "status-details": {
        "status": "string"
      }
    }
  }
}
```


`detail-type`

Identifies the type of event.


For StackSet operation status events, this value is `CloudFormation
 StackSet Operation Status Change`.



`source`

Identifies the service that generated the event. For CloudFormation
 events, this value is `aws.cloudformation`.



`detail`

A JSON object that contains information about the event. The service
 generating the event determines the content of this field.


For StackSet operation status events, this data includes:




`stack-set-arn`

The Amazon Resource Name (ARN) associated with the
 StackSet.



`stack-set-operation-id`

The unique ID that's associated with the StackSet
 operation.



`status-details`



`status`

The StackSet operation status.


For more details, see [StackSets status codes](stacksets-concepts.md#stackset-status-codes "stacksets-concepts.md#stackset-status-codes").


*Valid values*:
 `RUNNING` | `SUCCEEDED` |
 `FAILED` | `STOPPING` |
 `STOPPED` | `QUEUED`







###### Example:
 StackSet Operation Status Change event

The following is an example StackSet Operation Status Change event. The event
 details that CloudFormation has successfully completed the requested operation on
 the specified stack set.


```
{
  "version": "0",
  "id": "4de89905-fd92-6a6b-9509-23c04bcb6a21",
  "detail-type": "CloudFormation StackSet Operation Status Change",
  "source": "aws.cloudformation",
  "account": "111122223333",
  "time": "2021-09-22T05:46:24Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:cloudformation:us-east-1:111122223333:stackset/test1234:e5f54eea-d041-44ad-94f8-b8268aca1e59"
  ],
  "detail": {
    "stack-set-arn": "arn:aws:cloudformation:us-east-1:111122223333:stackset/test1234:e5f54eea-d041-44ad-94f8-b8268aca1e59",
    "stack-set-operation-id": "ce69adce-2221-4483-8c4b-c51f284f25e8",
    "status-details": {
        "status": "SUCCEEDED"
    }
  }
}
```
