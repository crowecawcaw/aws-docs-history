

# Logging Amazon GameLift Streams API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Amazon GameLift Streams is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all API calls for Amazon GameLift Streams as events. The calls captured include calls from the Amazon GameLift Streams console and code calls to the Amazon GameLift Streams API operations. Using the information collected by CloudTrail, you can determine the request that was made to Amazon GameLift Streams, the IP address from which the request was made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root user or user credentials.
+ Whether the request was made on behalf of an IAM Identity Center user.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

CloudTrail is active in your AWS account when you create the account and you automatically have access to the CloudTrail **Event history**. The CloudTrail **Event history** provides a viewable, searchable, downloadable, and immutable record of the past 90 days of recorded management events in an AWS Region. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*. There are no CloudTrail charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a [CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) event data store.

**CloudTrail trails**  
A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) and [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) in the *AWS CloudTrail User Guide*.  
You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/).

**CloudTrail Lake event data stores**  
*CloudTrail Lake* lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [ Apache ORC](https://orc.apache.org/) format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into *event data stores*, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-concepts.html#adv-event-selectors). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) in the *AWS CloudTrail User Guide*.  
CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html#cloudtrail-lake-manage-costs-pricing-option) you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

## Amazon GameLift Streams data events in CloudTrail
<a name="cloudtrail-data-events"></a>

[Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) provide information about the resource operations performed on or in a resource (for example, starting a stream session in a stream group). These are also known as data plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

You can log data events for the Amazon GameLift Streams resource types by using the CloudTrail console, AWS CLI, or CloudTrail API operations. For more information about how to log data events, see [Logging data events with the AWS Management Console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-console) and [Logging data events with the AWS Command Line Interface](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-with-the-AWS-CLI) in the *AWS CloudTrail User Guide*.

The following table lists the Amazon GameLift Streams resource types for which you can log data events. The **Resource type (console)** column shows the value to choose from the **Resource type** list on the CloudTrail console. The **resources.type value** column shows the `resources.type` value, which you would specify when configuring advanced event selectors using the AWS CLI or CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API calls logged to CloudTrail for the resource type.


| Resource type (console) | resources.type value | Data APIs logged to CloudTrail | 
| --- | --- | --- | 
| GameLift Streams application |  AWS::GameLiftStreams::Application  |  +  [CreateStreamUrl](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamUrl.html) <br />+  [GetStreamUrl](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamUrl.html) <br />+  [RevokeStreamUrl](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_RevokeStreamUrl.html) <br />+  [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html)   | 
| GameLift Streams stream group |  AWS::GameLiftStreams::StreamGroup  |  +  [CreateStreamSessionAdminShell](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionAdminShell.html) <br />+  [CreateStreamSessionConnection](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionConnection.html) <br />+  [CreateStreamUrl](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamUrl.html) <br />+  [ExportStreamSessionFiles](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ExportStreamSessionFiles.html) <br />+  [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html) <br />+  [GetStreamUrl](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamUrl.html) <br />+  [ListStreamSessions](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessions.html) <br />+  [ListStreamSessionsByAccount](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessionsByAccount.html) <br />+  [ListStreamUrls](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamUrls.html) <br />+  [RevokeStreamUrl](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_RevokeStreamUrl.html) <br />+  [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html) <br />+  [TerminateStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html)   | 

CloudTrail logs the stream URL API operations (`CreateStreamUrl`, `GetStreamUrl`, `ListStreamUrls`, and `RevokeStreamUrl`) as data events, the same way it logs other stream session operations. When an end user activates a stream URL to start a stream session, Amazon GameLift Streams handles that activation on the end user's behalf so it does not log the activation as a customer API call. Your auditable record of stream URL activity is the `CreateStreamUrl` call that created the stream URL and the `RevokeStreamUrl` call that revoked it. To see the sessions started from a stream URL, use `GetStreamUrl`.

You can configure advanced event selectors to filter on the `eventName`, `readOnly`, and `resources.ARN` fields to log only those events that are important to you. For more information about these fields, see [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) in the *AWS CloudTrail API Reference*.

## Amazon GameLift Streams management events in CloudTrail
<a name="cloudtrail-management-events"></a>

[Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

Amazon GameLift Streams logs the following Amazon GameLift Streams control plane operations to CloudTrail as *management events*.
+ [AddStreamGroupLocations](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AddStreamGroupLocations.html)
+ [AssociateApplications](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html)
+ [CreateApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateApplication.html)
+ [CreateStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamGroup.html)
+ [DeleteApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DeleteApplication.html)
+ [DeleteStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DeleteStreamGroup.html)
+ [DisassociateApplications](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DisassociateApplications.html)
+ [GetApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetApplication.html)
+ [GetStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamGroup.html)
+ [ListApplications](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListApplications.html)
+ [ListStreamGroups](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamGroups.html)
+ [ListTagsForResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html)
+ [RemoveStreamGroupLocations](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_RemoveStreamGroupLocations.html)
+ [TagResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html)
+ [UntagResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html)
+ [UpdateApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateApplication.html)
+ [UpdateStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html)

## Amazon GameLift Streams event examples
<a name="cloudtrail-event-examples"></a>

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail management event that demonstrates the [CreateApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateApplication.html) operation.

```
{
      "eventVersion": "1.09",
      "userIdentity": {
         "type": "AssumedRole",
         "principalId": "AROA123456789EXAMPLE:assume-temporary-gameliftstreams-access-role",
         "arn": "arn:aws:sts::111122223333:assumed-role/GameLiftStreamsTestRole/assume-temporary-gameliftstreams-access-role",
         "accountId": "111122223333",
         "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
         "sessionContext": {
               "sessionIssuer": {
                  "type": "Role",
                  "principalId": "AROA123456789EXAMPLE",
                  "arn": "arn:aws:iam::111122223333:role/GameLiftStreamsTestRole",
                  "accountId": "111122223333",
                  "userName": "GameLiftStreamsTestRole"
               },
               "webIdFederationData": {},
               "attributes": {
                  "creationDate": "2025-07-23T21:18:19Z",
                  "mfaAuthenticated": "false"
               }
         }
      },
      "eventTime": "2025-07-23T21:58:54Z",
      "eventSource": "gameliftstreams.amazonaws.com",
      "eventName": "CreateApplication",
      "awsRegion": "us-west-2",
      "sourceIPAddress": "203.0.113.0",
      "userAgent": "aws-sdk-javascript/2.0.0 Linux/4.14.291-218.527.amzn2.x86_64 OpenJDK_64-Bit_Server_VM/11.0.17+9-LTS Java/11.0.17 vendor/Amazon.com_Inc. exec-env/AWS_ECS_FARGATE io/sync http/Apache cfg/retry-mode/legacy",
      "requestParameters": {
         "ApplicationSourceUri": "s3://amzn-s3-demo-bucket/MyGame",
         "Description": "MyGame canary - Proton 8",
         "RuntimeEnvironment": {
               "Type": "PROTON",
               "Version": "20230704"
         },
         "ClientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
         "ExecutablePath": "MyGame100.exe"
      },
      "responseElements": {
         "Status": "INITIALIZED",
         "ApplicationSourceUri": "s3://amzn-s3-demo-bucket/MyGame",
         "Description": "MyGame canary - Proton 8",
         "RuntimeEnvironment": {
               "Type": "PROTON",
               "Version": "20230704"
         },
         "LastUpdatedAt": 1753307934.293,
         "CreatedAt": 1753307934.293,
         "Id": "a-9ZY8X7Wv6",
         "Arn": "arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6",
         "ExecutablePath": "MyGame100.exe"
      },
      "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
      "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
      "readOnly": false,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111122223333",
      "eventCategory": "Management"
}
```

The following example shows a CloudTrail data event from a trail log that demonstrates the [StartStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html) operation.

```
{
    "Records": [
        {
            "eventVersion": "1.09",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "AROA123456789EXAMPLE:assume-temporary-gameliftstreams-access-role",
                "arn": "arn:aws:sts::111122223333:assumed-role/GameLiftStreamsTestRole/assume-temporary-gameliftstreams-access-role",
                "accountId": "111122223333",
                "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
                "sessionContext": {
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "AROA123456789EXAMPLE",
                        "arn": "arn:aws:iam::111122223333:role/GameLiftStreamsTestRole",
                        "accountId": "111122223333",
                        "userName": "GameLiftStreamsTestRole"
                    },
                    "attributes": {
                        "creationDate": "2025-07-23T21:18:19Z",
                        "mfaAuthenticated": "false"
                    }
                }
            },
            "eventTime": "2025-07-23T23:43:46Z",
            "eventSource": "gameliftstreams.amazonaws.com",
            "eventName": "StartStreamSession",
            "awsRegion": "us-east-2",
            "sourceIPAddress": "203.0.113.0",
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "requestParameters": {
                "Identifier": "sg-1AB2C3De4",
                "Description": "StreamGroup sg-1AB2C3De4 Application a-9ZY8X7Wv6 Console stream",
                "AdditionalLaunchArgs": [],
                "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
                "Locations": [
                    "us-east-2"
                ],
                "SignalRequest": "***",
                "Protocol": "WebRTC",
                "ApplicationIdentifier": "a-9ZY8X7Wv6",
                "ClientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
                "ConnectionTimeoutSeconds": 100,
                "AdditionalEnvironmentVariables": {}
            },
            "responseElements": {
                "Status": "ACTIVATING",
                "ApplicationArn": "arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6",
                "Description": "StreamGroup sg-1AB2C3De4 Application a-9ZY8X7Wv6 Console stream",
                "LastUpdatedAt": 1.753314225925E9,
                "CreatedAt": 1.753314225925E9,
                "AdditionalEnvironmentVariables": {},
                "ConnectionTimeoutSeconds": 100,
                "AdditionalLaunchArgs": [],
                "StreamGroupId": "sg-1AB2C3De4",
                "UserId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
                "SessionLengthSeconds": 43200,
                "SignalRequest": "***",
                "Arn": "arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567",
                "Protocol": "WebRTC",
                "WebSdkProtocolUrl": "https://123456789012.cloudfront.net/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.js"
            },
            "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
            "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
            "readOnly": false,
            "resources": [
                {
                    "accountId": "111122223333",
                    "type": "AWS::GameLiftStreams::StreamGroup",
                    "ARN": "arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4"
                },
                {
                    "accountId": "111122223333",
                    "type": "AWS::GameLiftStreams::Application",
                    "ARN": "arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6"
                }
            ],
            "eventType": "AwsApiCall",
            "managementEvent": false,
            "recipientAccountId": "111122223333",
            "eventCategory": "Data"
        }
    ]
}
```

For information about CloudTrail record contents, see [CloudTrail record contents](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html) in the *AWS CloudTrail User Guide*.