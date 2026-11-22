

# Logging Amazon Textract API calls with AWS CloudTrail

Amazon Textract Core is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Textract Core. CloudTrail captures all API calls for Amazon Textract Core as events. The calls captured include calls from the Amazon Textract Core console and code calls to the Amazon Textract Core API operations. 

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon Textract Core. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Amazon Textract Core, the IP address that the request was made from, who made the request, when it was made, and additional details. 

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## Amazon Textract information in CloudTrail
<a name="textract-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in Amazon Textract Core, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for Amazon Textract Core, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data that's collected in CloudTrail logs. For more information, see the following: 
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All Amazon Textract operations, including the Amazon Textract Insights operations, are logged by CloudTrail and are documented in the [API Reference](https://docs.aws.amazon.com/textract/latest/dg/API_Operations.html). For example, calls to the `DetectDocumentText`, `AnalyzeDocument`, `GetDocumentTextDetection`, and `StartDocumentInsights` actions generate entries in the CloudTrail log files. 

Amazon Textract logs `StartDocumentInsights` and `GetDocumentInsights` as data events. CloudTrail doesn't log data events by default, and they don't appear in Event history. To log them, add an advanced event selector to a trail or event data store with `eventCategory` equal to `Data` and `resources.type` equal to `AWS::Textract::Job`. Additional charges apply for data events. For more information, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html). All other Amazon Textract operations are management events.

CloudTrail records Amazon Textract Insights events in the AWS Region that you call, including when the request is processed in another AWS Region. AWS Key Management Service (AWS KMS) calls that Amazon Textract Insights makes for a job appear in your account with `invokedBy` set to `textract.amazonaws.com`.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root or user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

### Request parameters and response fields that aren't logged
<a name="redacted-items"></a>

For privacy purposes, certain request parameters and response fields aren't logged—for example, request image bytes or response bounding box information. Amazon S3 bucket names and file names supplied in request parameters are provided in CloudTrail log entries. No information about image bytes passed in a request is provided in a CloudTrail log. The following table shows the input parameters and response parameters that aren't logged for each Amazon Textract operation. 


| **Operation** | **Request Parameters** | **Response Fields** | 
| --- | --- | --- | 
| AnalyzeDocument | `Bytes` | All | 
| DetectDocumentText | `Bytes` | All | 
| StartDocumentAnalysis | None | None | 
| GetDocumentAnalysis | None | All | 
| StartDocumentTextDetection | None | None | 
| GetDocumentTextDetection | None | All | 
| CreateProject | `ProjectName`, `ProjectDescription`, `Tags` | None | 
| UpdateProject | `ProjectDescription` | None | 
| GetProject | None | All | 
| CreateBlueprint | `Schema`, `Tags` | None | 
| UpdateBlueprint | `Schema` | None | 
| CreateBlueprintVersion | None | None | 
| GetBlueprint | None | All | 
| StartDocumentInsights | None | None | 
| GetDocumentInsights | None | All | 
| ListProjects | None | All | 
| ListBlueprints | None | All | 
| DeleteProject | None | None | 
| DeleteBlueprint | None | None | 
| TagResource | None | None | 
| UntagResource | None | None | 
| ListTagsForResource | None | All | 

**Note**  
When you tag or untag a resource, the request parameters of the CloudTrail event identify the resource ARN.

## Understanding Amazon Textract log file entries
<a name="understanding-textract-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the `AnalyzeDocument` operation. The image bytes for the input `document` and the analysis results (`responseElements`) aren't logged.

```json
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111111111111:user/janedoe",
        "accountId": "111111111111",
        "accessKeyId": "AIDACKCEVSQ6C2EXAMPLE",
        "userName": "janedoe"
    },
    "eventTime": "2019-04-03T23:56:31Z",
    "eventSource": "textract.amazonaws.com",
    "eventName": "AnalyzeDocument",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "198.51.100.0",
    "userAgent": "",
    "requestParameters": {
        "document": {},
        "featureTypes": [
            "TABLES"
        ]
    },
    "responseElements": null,
    "requestID": "e387676b-d1f0-4ea7-85d6-f5a344052dce",
    "eventID": "c5db79ce-e4ea-4401-8517-784481d559f7",
    "eventType": "AwsApiCall",
    "recipientAccountId": "111111111111"
}
```

The following example shows a CloudTrail log entry for the `StartDocumentAnalysis` operation. The log entry includes the Amazon S3 bucket name and image file name in `documentLocation`. The log also includes the operation response. 

```json
{
    "Records": [
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "IAMUser",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::111111111111:user/janedoe",
                "accountId": "11111111111",
                "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
                "userName": "janedoe"
            },
            "eventTime": "2019-04-04T01:42:24Z",
            "eventSource": "textract.amazonaws.com",
            "eventName": "StartDocumentAnalysis",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "198.51.100.0",
            "userAgent": "",
            "requestParameters": {
                "documentLocation": {
                    "s3Object": {
                        "bucket": "bucket",
                        "name": "document.png"
                    }
                },
                "featureTypes": [
                    "TABLES"
                ]
            },
            "responseElements": {
                "jobId": "f3c718b444fa603d5d625ab967008f4b620d4650c9db8ca1cae01ef7efe51373"
            },
            "requestID": "9ae352e8-9de1-41ad-b77b-85aa348c2e82",
            "eventID": "f741bca0-c3cb-4805-82ea-baf76439deef",
            "eventType": "AwsApiCall",
            "recipientAccountId": "111111111111"
        }

    ]
}
```

The following example shows a CloudTrail log entry for the `StartDocumentInsights` operation. The request includes the input and output Amazon S3 locations and the project ARN in `requestParameters`, and the response includes the job ARN in `responseElements`.

```json
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROA123456789EXAMPLE:my-session",
        "arn": "arn:aws:sts::111122223333:assumed-role/TextractInsightsRole/my-session",
        "accountId": "111122223333",
        "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROA123456789EXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/TextractInsightsRole",
                "accountId": "111122223333",
                "userName": "TextractInsightsRole"
            },
            "attributes": {
                "creationDate": "2026-12-01T18:00:00Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2026-12-01T18:04:12Z",
    "eventSource": "textract.amazonaws.com",
    "eventName": "StartDocumentInsights",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "198.51.100.0",
    "userAgent": "aws-cli/2.0.0",
    "requestParameters": {
        "projectArn": "arn:aws:textract:us-east-1:111122223333:project/abcd1234efgh",
        "inputConfiguration": {
            "s3Uri": "s3://amzn-s3-demo-bucket/documents/invoice.pdf"
        },
        "outputConfiguration": {
            "s3Uri": "s3://amzn-s3-demo-destination-bucket/results/"
        }
    },
    "responseElements": {
        "jobArn": "arn:aws:textract:us-east-1:111122223333:job/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::Textract::Job",
            "ARN": "arn:aws:textract:us-east-1:111122223333:job/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": false,
    "recipientAccountId": "111122223333",
    "eventCategory": "Data",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "textract.us-east-1.amazonaws.com"
    }
}
```