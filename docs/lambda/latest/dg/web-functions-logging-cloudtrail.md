

# Logging Web Function API calls using AWS CloudTrail
<a name="web-functions-logging-cloudtrail"></a>

With [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), you can track the actions taken by a user, role, or AWS service in AWS Lambda Web Functions. CloudTrail provides a record of these actions. CloudTrail captures Web Function invocations as data events. You can use this information to determine who invoked a Web Function, when, and from where, which helps with security analysis and operational auditing.

## Web Function data events in CloudTrail
<a name="web-functions-cloudtrail-data-events"></a>

Data events provide information about operations performed on a resource. For example, invoking a Web Function endpoint is a data event. These operations are also known as data-plane operations, and they are often high-volume. By default, CloudTrail doesn't log data events, and the CloudTrail **Event history** doesn't record them.

Additional charges apply for data events. For more information, see [CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/).

You can log data events for the `AWS::Lambda::WebFunction` resource type by using the CloudTrail console, AWS CLI, or CloudTrail API operations. CloudTrail records each invocation in the AWS Region that served the request, and `awsRegion` identifies that Region. Unlike logs and metrics, invocation events are not centralized into the home Region. For a `MultiRegion` or `PerRegion` endpoint, use a multi-Region trail or event data store so that invocations in every Region that the endpoint serves are recorded.

The following table shows the data event type for Web Functions.


| Data event type (console) | resources.type value | Data APIs logged to CloudTrail | 
| --- | --- | --- | 
| Lambda Web Function | AWS::Lambda::WebFunction | InvokeWebFunctionEndpoint | 

CloudTrail records the following key identifiers for a Web Function invocation:


| Identifier | Value | 
| --- | --- | 
| eventSource | lambda.amazonaws.com | 
| eventName | InvokeWebFunctionEndpoint. This is the value to filter on. | 
| IAM action | lambda:InvokeWebFunctionEndpoint | 
| readOnly | false, because an invocation runs your function code. | 
| resources.type | AWS::Lambda::WebFunction | 
| resources.ARN | The function ARN, not the endpoint ARN. Trail selectors therefore work at the function level. | 

The following advanced event selector logs invocations for a single Web Function only.

```
[
    {
        "Name": "web-function-invokes",
        "FieldSelectors": [
            { "Field": "eventCategory", "Equals": ["Data"] },
            { "Field": "resources.type", "Equals": ["AWS::Lambda::WebFunction"] },
            { "Field": "resources.ARN", "Equals": ["arn:aws:lambda:us-east-1:111122223333:web-function/hello-world"] }
        ]
    }
]
```

To turn on data events on a trail, use the following procedure.

**To turn on and verify Web Function data events (AWS CLI)**

1. Create or choose the trail that will record the data events. For instructions, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*.

1. Save the following advanced event selector as `web-function-data-events.json`. It records invocations for one Web Function. To record invocations for every Web Function in the account, remove the `resources.ARN` field selector.

   ```
   [
     {
       "Name": "web-function-invocations",
       "FieldSelectors": [
         {
           "Field": "eventCategory",
           "Equals": ["Data"]
         },
         {
           "Field": "resources.type",
           "Equals": ["AWS::Lambda::WebFunction"]
         },
         {
           "Field": "resources.ARN",
           "Equals": [
             "arn:aws:lambda:us-east-1:111122223333:web-function/my-web-app"
           ]
         }
       ]
     }
   ]
   ```

1. Apply the selector to the trail:

   ```
   aws cloudtrail put-event-selectors \
       --trail-name {{my-trail}} \
       --advanced-event-selectors file://web-function-data-events.json
   ```
**Important**  
`put-event-selectors` replaces the trail’s existing event selectors. If the trail already records other events, include their selectors in the same file.

1. Invoke the endpoint with a test request.

1. Query the trail destination for `eventName = InvokeWebFunctionEndpoint`. Verify the function ARN, event time, request ID, caller information available for the authentication path, and any conditional error fields. If the selector works, the query returns an `InvokeWebFunctionEndpoint` event for your test request, similar to the example in [Example: successful invocation (unauthenticated caller)](#web-functions-cloudtrail-example-success).

To record data events in a CloudTrail Lake event data store instead, add the same field selectors to the event data store. For more information, see the *AWS CloudTrail User Guide*.

## Fields in an InvokeWebFunctionEndpoint event
<a name="web-functions-cloudtrail-event-fields"></a>

The following table describes the fields in an `InvokeWebFunctionEndpoint` event.


| Field | Notes | 
| --- | --- | 
| eventVersion | The version of the event format. | 
| eventSource | Always lambda.amazonaws.com. | 
| eventName | Always InvokeWebFunctionEndpoint. | 
| eventCategory | Always Data. | 
| eventType | The event type, for example AwsApiCall. | 
| readOnly | Always false, because an invocation runs your function code. | 
| managementEvent | Always false. | 
| eventTime | The date and time, in UTC, that Lambda recorded the event. For a successful invocation, Lambda records the event when your function starts its response, so eventTime can be later than the time the request arrived. | 
| sourceIPAddress | The IP address that the request was made from. | 
| userAgent | The agent the caller used to make the request. Present when the caller sends a User-Agent header. | 
| requestParameters | Contains endpointArn, the ARN of the invoked endpoint. The request payload is not logged. | 
| responseElements | Always null. | 
| resources | Contains one entry with the accountId, type, and ARN of the function. | 
| additionalEventData | Contains functionRevisionArn, the ARN of the revision that served the request. This field is present on every event, including denials. | 
| tlsDetails | The TLS version, cipher suite, and host header of the request. | 
| userIdentity | The identity of the caller. For details, see the following list. | 
| sharedEventID | Present when CloudTrail delivers the same event to more than one AWS account. | 
| errorCode, errorMessage | Present only on an error event. | 
| requestID, eventID, recipientAccountId, awsRegion | Standard CloudTrail fields that identify the request, the event, the recipient AWS account, and the AWS Region. | 

Web Function events use the following ARN shapes:
+ Function (`resources[].ARN`) – `arn:aws:lambda:us-east-1:123456789012:web-function/my-fn`
+ Endpoint (`requestParameters.endpointArn`) – `arn:aws:lambda:us-east-1:123456789012:web-function/my-fn/endpoint/my-endpoint`
+ Revision (`additionalEventData.functionRevisionArn`) – `arn:aws:lambda:us-east-1:123456789012:web-function/my-fn/revision/rev-a1b2c`

The `userIdentity` field depends on how the caller authenticated:
+ Unauthenticated invocations are recorded with `userIdentity` type `Unknown`.
+ IAM-authenticated callers are logged with their own principal. For example, a caller using temporary credentials appears with type `AssumedRole`, an `arn`, and a `sessionContext`.
+ The `accessKeyId` field is not populated.

## Error events
<a name="web-functions-cloudtrail-error-events"></a>

CloudTrail also logs invocation attempts that fail after the caller is authenticated. The following table describes these error events.


| Scenario | errorCode | errorMessage | 
| --- | --- | --- | 
| Caller not authorized | AccessDenied | User is not authorized to perform: lambda:InvokeWebFunctionEndpoint | 
| Request rate, concurrency, or vCPU limit reached (endpoint or account) | ThrottlingException | Rate exceeded | 
| Service fault | ServiceException | Service error | 
| Application error or invalid client request | Not applicable | Treated as a successful API call. The invocation reached and ran the function. | 

A successful invocation has no `errorCode` or `errorMessage`. Authorization denials are logged as `AccessDenied`. CloudTrail does not record requests that fail authentication, such as requests with a missing, malformed, invalid, or expired signature, and does not record requests that Lambda rejects before authentication, such as requests to an endpoint whose `rateLimit` is 0. Internal authentication infrastructure failures are also not recorded. To detect a spike in rejected requests, alarm on `HTTPResponseStatusClass4XX` in the `AWS/Lambda/Web` namespace.

## Example: successful invocation (unauthenticated caller)
<a name="web-functions-cloudtrail-example-success"></a>

The following example shows a successful invocation by an unauthenticated caller.

```
{
    "Records": [
        {
            "eventVersion": "1.11",
            "userIdentity": {
                "type": "Unknown"
            },
            "eventTime": "2026-09-22T18:41:07Z",
            "eventSource": "lambda.amazonaws.com",
            "eventName": "InvokeWebFunctionEndpoint",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "203.0.113.42",
            "userAgent": "curl/8.4.0",
            "requestParameters": {
                "endpointArn": "arn:aws:lambda:us-east-1:123456789012:web-function/my-fn/endpoint/my-endpoint"
            },
            "responseElements": null,
            "additionalEventData": {
                "functionRevisionArn": "arn:aws:lambda:us-east-1:123456789012:web-function/my-fn/revision/rev-a1b2c"
            },
            "requestID": "b1f8a4c2-7e3d-4a19-9f6b-2c5d8e0a1234",
            "eventID": "d4c3b2a1-5f6e-7a8b-9c0d-1e2f3a4b5c6d",
            "readOnly": false,
            "resources": [
                {
                    "accountId": "123456789012",
                    "type": "AWS::Lambda::WebFunction",
                    "ARN": "arn:aws:lambda:us-east-1:123456789012:web-function/my-fn"
                }
            ],
            "eventType": "AwsApiCall",
            "managementEvent": false,
            "recipientAccountId": "123456789012",
            "eventCategory": "Data",
            "tlsDetails": {
                "tlsVersion": "TLSv1.3",
                "cipherSuite": "TLS_AES_128_GCM_SHA256",
                "clientProvidedHostHeader": "bcdfghjklmnpqrst.b7t.lambda-web.us-east-1.on.aws"
            }
        }
    ]
}
```

For an IAM-authenticated caller, the `userIdentity` field instead carries the caller's principal, for example type `AssumedRole` with an `arn` and a `sessionContext`, and the remaining fields are unchanged.

## Example: denied invocation
<a name="web-functions-cloudtrail-example-denied"></a>

Error events carry `errorCode` and `errorMessage`. The following example shows a denied invocation.

```
{
    "Records": [
        {
            "eventVersion": "1.11",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "ARO01EXAMPLEID:session-name",
                "arn": "arn:aws:sts::123456789012:assumed-role/app-invoke-role/session-name",
                "accountId": "123456789012",
                "sessionContext": {
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "ARO01EXAMPLEID",
                        "arn": "arn:aws:iam::123456789012:role/app-invoke-role",
                        "accountId": "123456789012",
                        "userName": "app-invoke-role"
                    },
                    "attributes": {
                        "creationDate": "2026-09-22T18:39:55Z",
                        "mfaAuthenticated": "false"
                    }
                }
            },
            "eventTime": "2026-09-22T18:42:13Z",
            "eventSource": "lambda.amazonaws.com",
            "eventName": "InvokeWebFunctionEndpoint",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "203.0.113.42",
            "userAgent": "aws-sdk-python/1.34.0",
            "errorCode": "AccessDenied",
            "errorMessage": "User is not authorized to perform: lambda:InvokeWebFunctionEndpoint",
            "requestParameters": {
                "endpointArn": "arn:aws:lambda:us-east-1:123456789012:web-function/my-fn/endpoint/my-endpoint"
            },
            "responseElements": null,
            "additionalEventData": {
                "functionRevisionArn": "arn:aws:lambda:us-east-1:123456789012:web-function/my-fn/revision/rev-a1b2c"
            },
            "requestID": "c2e9b5d3-8f4e-4b2a-a07c-3d6e9f1b2345",
            "eventID": "e5d4c3b2-6a7f-8b9c-0d1e-2f3a4b5c6d7e",
            "readOnly": false,
            "resources": [
                {
                    "accountId": "123456789012",
                    "type": "AWS::Lambda::WebFunction",
                    "ARN": "arn:aws:lambda:us-east-1:123456789012:web-function/my-fn"
                }
            ],
            "eventType": "AwsApiCall",
            "managementEvent": false,
            "recipientAccountId": "123456789012",
            "eventCategory": "Data",
            "tlsDetails": {
                "tlsVersion": "TLSv1.3",
                "cipherSuite": "TLS_AES_128_GCM_SHA256",
                "clientProvidedHostHeader": "bcdfghjklmnpqrst.b7t.lambda-web.us-east-1.on.aws"
            }
        }
    ]
}
```

## Management events in CloudTrail
<a name="web-functions-cloudtrail-management-events"></a>

CloudTrail records Web Function management events by default. You can view the last 90 days of management events in the CloudTrail **Event history** without creating a trail. To keep them longer, create a trail or CloudTrail Lake event data store. For more information, see [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*.

CloudTrail records the following Web Function operations as management events. The `eventName` field of each event is the same as the operation name.


| Resource or task | Operations | 
| --- | --- | 
| Web Functions | CreateWebFunction, GetWebFunction, ListWebFunctions, DeleteWebFunction | 
| Revisions | CreateWebFunctionRevision, GetWebFunctionRevision, ListWebFunctionRevisions, DeleteWebFunctionRevision | 
| Endpoints | CreateWebFunctionEndpoint, GetWebFunctionEndpoint, ListWebFunctionEndpoints, UpdateWebFunctionEndpoint, DeleteWebFunctionEndpoint | 
| Account settings | GetWebAccountSettings | 
| Resource policies | PutResourcePolicy, GetResourcePolicy, DeleteResourcePolicy | 
| Tags | TagResource, UntagResource, ListTags | 

Web Function invocation is a data-plane operation. CloudTrail logs it only as a data event, as described in [Web Function data events in CloudTrail](#web-functions-cloudtrail-data-events).

## Related resources
<a name="web-functions-cloudtrail-related"></a>

For more information, see the following resources:
+ [Logging AWS Lambda API calls using AWS CloudTrail](logging-using-cloudtrail.md)
+ [Lambda Web Function permissions](web-functions-permissions.md)
+ [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)