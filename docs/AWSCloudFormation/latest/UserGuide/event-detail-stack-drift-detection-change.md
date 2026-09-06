

# Drift Detection Status Change event detail
<a name="event-detail-stack-drift-detection-change"></a>

Below are the detail fields for stack drift detection events.

The `source` and `detail-type` fields are included because they contain specific values for events.

```
{
  . . .,
  "detail-type":"CloudFormation Drift Detection Status Change",
  "source":"aws.cloudformation",
  . . .,
  "detail":{
    "stack-id":"string",
    "stack-drift-detection-id":"string",
    "status-details":{
      "stack-drift-status":"string",
      "detection-status":"string"
    },
      "drift-detection-details":{
        "drifted-stack-resource-count":integer
      },
    "client-request-token":"string"
  }
}
```

`detail-type`  <a name="drift-detection-status-change-detail-type"></a>
Identifies the type of event.  
For stack drift detection events, this value is `CloudFormation Drift Detection Status Change`.

`source`  <a name="drift-detection-status-change-source"></a>
Identifies the service that generated the event. For CloudFormation events, this value is `aws.cloudformation`.

`detail`  <a name="drift-detection-status-change-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
For stack drift detection events, this data includes:    
`stack-id`  <a name="drift-detection-status-change-stack-id"></a>
The unique stack ID that's associated with the stack.  
`stack-drift-detection-id`  <a name="drift-detection-status-change-stack-drift-detection-id"></a>
The stack drift detection Id.  
`status-details`  <a name="drift-detection-status-change-status-details"></a>  
`stack-drift-status`  <a name="drift-detection-status-change-stack-drift-status"></a>
Drift status of the stack.  
`detection-status`  <a name="drift-detection-status-change-detection-status"></a>
Status of drift detection operation.  
`drift-detection-details`  <a name="drift-detection-status-change-drift-detection-details"></a>  
`drifted-stack-resource-count`  <a name="drift-detection-status-change-drifted-stack-resource-count"></a>
Number of resources drifted. When the value is `-1`, the drift detection is in progress. All other non--negative integers represent the actual number of drifted resources.  
`client-request-token`  <a name="drift-detection-status-change-client-request-token"></a>
An access token used to call the API. All events that are initiated by a given stack operation are assigned the same client request token, which you can use to track operations. Stack operations that are initiated from the console use the token format *Console-StackOperation-ID*, which helps you to easily identify the stack operation. For example, if you create a stack using the console, each resulting stack event would be assigned the same token in the following format: `Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`.

**Example: Stack Drift Detection event**  <a name="event-detail-stack-drift-detection-change.example"></a>
The following is an example Stack Drift Detection event. This event details that CloudFormation has completed drift detection on the specified stack, and that the stack currently has a drift status of `DRIFTED` due to one drifted resource.  

```
{
    "version":"0",
    "id":"6a7e8feb-b491-4cf7-a9f1-bf3703467718",
    "detail-type":"CloudFormation Drift Detection Status Change",
    "source":"aws.cloudformation",
    "account":"111122223333",
    "time":"2017-12-22T18:43:48Z",
    "region":"us-west-1",
    "resources": ["string"],
    "detail":{
        "stack-id":"arn:aws:cloudformation:us-west-1:111122223333:stack/teststack",
        "stack-drift-detection-id":"624af370-311a-11e8-b6b7-500cexample",
        "status-details":{
            "stack-drift-status":"DRIFTED",
            "detection-status":"DETECTION_COMPLETE"
        },
        "drift-detection-details":{
            "drifted-stack-resource-count":1
        },
    "client-request-token":""
    }
}
```