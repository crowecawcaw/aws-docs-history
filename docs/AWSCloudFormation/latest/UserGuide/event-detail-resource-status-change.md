

# Resource Status Change event detail
<a name="event-detail-resource-status-change"></a>

Below are the detail fields for Resource Status Change events.

The `source` and `detail-type` fields are included because they contain specific values for events.

```
{
  . . .,
  "detail-type": "CloudFormation Resource Status Change",
  "source": "aws.cloudformation",
  . . .,
  "detail": {
    "stack-id" : "string",
    "logical-resource-id" : "string",
    "physical-resource-id": "string",
    "status-details": {
        "status": "string",
        "status-reason": "string"
    },
     "resource-type": "string",
     "client-request-token": "string"
  }
}
```

`detail-type`  <a name="resource-status-change-detail-type"></a>
Identifies the type of event.  
For resource status events, this value is `CloudFormation Resource Status Change`.

`source`  <a name="resource-status-change-source"></a>
Identifies the service that generated the event. For CloudFormation events, this value is `aws.cloudformation`.

`detail`  <a name="resource-status-change-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
For resource status events, this data includes:    
`stack-id`  <a name="resource-status-change-stack-id"></a>
The unique stack ID that's associated with the stack.  
`logical-resource-id`  <a name="resource-status-change-logical-resource-id"></a>
The logical name of the resource as specified in the template.  
`physical-resource-id`  <a name="resource-status-change-physical-resource-id"></a>
The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.  
`status-details`  <a name="resource-status-change-status-details"></a>  
`status`  <a name="resource-status-change-status"></a>
Status of the resource.  
`status-reason`  <a name="resource-status-change-status-reason"></a>
Status reason of the resource.  
`resource-type`  <a name="resource-status-change-resource-type"></a>
Type of resource. For example, `AWS::S3::Bucket`.  
`client-request-token`  <a name="resource-status-change-client-request-token"></a>
An access token used to call the API. All events that are initiated by a given stack operation are assigned the same client request token, which you can use to track operations. Stack operations that are initiated from the console use the token format *Console-StackOperation-ID*, which helps you to easily identify the stack operation. For example, if you create a stack using the console, each resulting stack event would be assigned the same token in the following format: `Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`.

**Example: Resource Status Change event**  <a name="event-detail-resource-status-change.example"></a>
The following is an example resource status event. This event details that CloudFormation has successfully created the requested resource, an Amazon S3 bucket, in the specified stack.  

```
{
    "version":"0",
    "id":"6a7e8feb-b491-4cf7-a9f1-bf3703467718",
    "detail-type":"CloudFormation Resource Status Change",
    "source":"aws.cloudformation",
    "account":"111122223333",
    "time":"2017-12-22T18:43:48Z",
    "region":"us-west-1",
    "resources":[
        "arn:aws:cloudformation:us-west-1:111122223333:stack/teststack"
    ],
    "detail":{
        "stack-id":"arn:aws:cloudformation:us-west-1:111122223333:stack/teststack",
        "logical-resource-id":"my-s3-bucket",
        "physical-resource-id":"arn:aws:s3:::my-s3-bucket-us-east-1",
        "status-details":{
            "status":"CREATE_COMPLETE",
            "status-reason":""
        },
        "resource-type":"AWS::S3::Bucket",
        "client-request-token":""
    }
}
```