

# Stack Status Change event detail
<a name="event-detail-stack-status-change"></a>

Below are the detail fields for Stack Status Change events.

The `source` and `detail-type` fields are included because they contain specific values for events.

```
{
  . . .,
  "detail-type":"CloudFormation Stack Status Change",
  "source":"aws.cloudformation",
  . . .,
  "detail":{
    "stack-id":"string",
    "status-details":{
      "status":"string",
      "status-reason":"string"
    },
    "client-request-token":"string"
  }
}
```

`detail-type`  <a name="stack-status-change-detail-type"></a>
Identifies the type of event.  
For stack status events, this value is `CloudFormation Stack Status Change`.

`source`  <a name="stack-status-change-source"></a>
Identifies the service that generated the event. For CloudFormation events, this value is `aws.cloudformation`.

`detail`  <a name="stack-status-change-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
For stack status events, this data includes:    
`stack-id`  <a name="stack-status-change-stack-id"></a>
The unique stack ID associated with the stack.  
`status-details`  <a name="stack-status-change-status-details"></a>  
`status`  <a name="stack-status-change-status"></a>
Status of the stack.  
For a complete list of stack status codes, see [Stack status codes](view-stack-events.md#cfn-console-view-stack-data-resources-status-codes).  
`status-reason`  <a name="stack-status-change-status-reason"></a>
Status reason of the resource.  
`client-request-token`  <a name="stack-status-change-client-request-token"></a>
An access token used to call the API. All events that are initiated by a given stack operation are assigned the same client request token, which you can use to track operations. Stack operations that are initiated from the console use the token format *Console-StackOperation-ID*, which helps you to easily identify the stack operation. For example, if you create a stack using the console, each resulting stack event would be assigned the same token in the following format: `Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`.

**Example: Stack Status event**  <a name="event-detail-stack-status-change.example"></a>
The following is an example stack status event, where CloudFormation has successfully created the requested stack, `teststack`.  

```
{
    "version":"0",
    "id":"6a7e8feb-b491-4cf7-a9f1-bf3703467718",
    "detail-type":"CloudFormation Stack Status Change",
    "source":"aws.cloudformation",
    "account":"111122223333",
    "time":"2017-12-22T18:43:48Z",
    "region":"us-west-1",
    "resources":[
        "arn:aws:cloudformation:us-west-1:111122223333:stack/teststack"
    ],
    "detail":{
        "stack-id":"arn:aws:cloudformation:us-west-1:111122223333:stack/teststack",
        "status-details":{
            "status":"CREATE_COMPLETE",
            "status-reason":""
        },
        "client-request-token":""
    }
}
```