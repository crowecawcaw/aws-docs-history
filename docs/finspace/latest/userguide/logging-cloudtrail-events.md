After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Querying AWS CloudTrail logs

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

Amazon FinSpace is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or AWS service in FinSpace. CloudTrail captures all API calls for FinSpace as
events. The events captured include calls from the FinSpace console, web application, and code
calls to the FinSpace APIs. You can use the information collected by CloudTrail to determine the
request that was made to FinSpace, the IP address of the requester, who made the request, when
the request was made, and additional details.

You can create a trail to enable continuous delivery of CloudTrail events to an Amazon Simple Storage Service
(Amazon S3) bucket, including events for FinSpace. If you don't configure a trail, you can still
view the most recent events in the CloudTrail console.

For more information about CloudTrail, see the [AWS CloudTrail User
Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## FinSpace information in

CloudTrail

CloudTrail is enabled on your AWS account when you create the account. In the CloudTrail
console in **Event history**, you can view, search, and
download recent events in your AWS account. For more information, see [Viewing events with CloudTrail event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the AWS CloudTrail User Guide.

For an ongoing record of events in your AWS account, including events for FinSpace,
create a trail. By default, when you create a trail in the console, the trail applies to
all AWS Regions. The trail logs events from all Regions in the AWS partition and
delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can
configure other AWS services to further analyze and act upon the event data collected
in CloudTrail logs. For more information, see the following in the _AWS CloudTrail User
Guide_:

- [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [AWS service integrations with CloudTrail logs](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

CloudTrail logs all FinSpace API operations including actions taken in the FinSpace web
application. These and other operations are documented in the API references:

- [Amazon FinSpace management
  API reference](../management-api/fs-api-welcome.md "../management-api/fs-api-welcome.md")
- [Amazon FinSpace data API reference](../data-api/fs-api-welcome.md "../data-api/fs-api-welcome.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine:

- The details of the user that made the request.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md") in the AWS CloudTrail User Guide.

## Understanding FinSpace log

file entries

CloudTrail delivers events as log files that contain one or more log entries. An event
represents a single request from any source and includes information about the requested
operation, the date and time of the operation, the request parameters, and so on.
Because these log files aren't an ordered stack trace of the public API calls, they
don't appear in any specific order.

The following example CloudTrail log entry demonstrates the `CreateEnvironment`
operation, which creates a new FinSpace environment.

```
{
  "eventVersion": "1.08",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "AROARFVIKXOEXAMPLE",
    "arn": "arn:aws:iam::123456789012:user/johndoe",
    "accountId": "123456789012",
    "accessKeyId": "AROARFVIKXOEXAMPLE",
    "userName": "johndoe"
  },
  "eventTime": "2021-03-16T17:14:44Z",
  "eventSource": "finspace.amazonaws.com",
  "eventName": "CreateEnvironment",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "72.21.197.99",
  "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0",
  "requestParameters": {
    "name": "TestEnv",
    "federationMode": "LOCAL",
    "kmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/d9610405-8674-450f-b8cd-e47999fdf2d",
    "tags": {}
  },
  "responseElements": {
    "environmentArn": "arn:aws:finspace:us-east-1:123456789012:environment/6c6b4bbnnxin774ruft2dr",
    "environmentId": "6c6b4bbnnxin774ruft2dr",
    "environmentUrl": "6c6b4bbnnxin774ruft2dr.us-east-1.amazonfinspace.com"
  },
  "requestID": "167148e31-951f-52a8-b9bd-be347ce7801f",
  "eventID": "c2949aca-8862-4903-970e-64ae7cc1ba6b",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "eventCategory": "Management",
  "recipientAccountId": "120345661733"
}
```

The following example CloudTrail log entry demonstrates the `GetEnvironment`
operation, which describes a FinSpace environment.

```
{
  "eventVersion": "1.08",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "AROARFVIKXOEXAMPLE",
    "arn": "arn:aws:iam::123456789012:user/johndoe",
    "accountId": "123456789012",
    "accessKeyId": "AROARFVIKXOEXAMPLE",
    "userName": "johndoe"
  },
  "eventTime": "2021-02-26T13:59:00Z",
  "eventSource": "finspace.amazonaws.com",
  "eventName": "GetEnvironment",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "72.22.198.64",
  "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0",
  "requestParameters": {
    "environmentId": "ks56piapqiwaqxwj4xsjxx"
  },
  "responseElements": null,
  "requestID": "94ac7fff-1aad-4470-b0d9-83d13432ae4b",
  "eventID": "d318ca50-c45e-4f2d-954e-d23bee29effa",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "eventCategory": "Management",
  "recipientAccountId": "123456789012"
}
```

The following example CloudTrail log entry demonstrates the `CreateUser`
operation, which creates a FinSpace user by using the FinSpace data API.

In this example, the value of the `principalId` element is the FinSpace user
ID of the user who accesses the web application.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "gmkd6xsrn9h7hfgxtnqlxw",
        "accountId": "123456789012"
    },
    "eventTime": "2022-12-12T19:57:48Z",
    "eventSource": "finspace-api.amazonaws.com",
    "eventName": "CreateUser",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "52.94.133.129",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101
    Firefox / 85.0 ",
    "requestParameters": {
        "emailAddress": "*** REDACTED ***",
        "firstName": "*** REDACTED ***",
        "lastName": "*** REDACTED ***",
        "type": "APP_USER"
    },
    "responseElements": {
        "userId": "tskd9r67fvb6yxtmda6wla"
    },
    "additionalEventData": {
        "finspaceDisplayableOperationName": "Create user",
        "finspaceEnvironmentId": "nlbapur76fhbij6oohyfyu"
    },
    "requestID": "771abcc3-0539-414e-9310-ec123eaa6d01",
    "eventID": "390f33ab-4396-4f18-8126-599016fe7280",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "apiVersion": "2020-07-13",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

The following example CloudTrail log entry demonstrates the `CreateDataset`
event generated by an action taken in the FinSpace web application.

In this example, the value of the `principalId` element is the FinSpace user
ID of the user who accesses the web application.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "gmkd6xsrn9h7hfgxtnqlxw",
        "accountId": "123456789012"
    },
    "eventTime": "2022-12-12T20:06:46Z",
    "eventSource": "finspace-api.amazonaws.com",
    "eventName": "CreateDataset",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "52.94.133.129",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X     10 _15_7) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 107.0 .0 .0 Safari / 537.36 ",
    "requestParameters": {
        "datasetDescription": "*** REDACTED ***",
        "datasetTitle": "Test Dataset",
        "kind": "TABULAR",
        "ownerInfo": {
            "name": "*** REDACTED ***",
            "email": "*** REDACTED ***"
        },
        "permissionGroupParams": {
            "permissionGroupId": "4MIH3qXyXX9aRhDpRIFRQg",
            "datasetPermissions": [{
                "permission": "ViewDatasetDetails"
            }, {
                "permission": "ReadDatasetData"
            }]
        },
        "schemaDefinition": {
            "tabularSchemaConfig": {
                "columns": [{
                    "dataType": "DATETIME",
                    "name": "timestamp",
                    "description": "*** REDACTED ***"
                }, {
                    "dataType": "STRING",
                    "name": "event_type",
                    "description": "*** REDACTED ***"
                }]
            }
        }
    },
    "responseElements": {
        "datasetId": "b3m7g70"
    },
    "additionalEventData": {
        "finspaceEnvironmentId": "nlbapur76fhbij6oohyfyu"
    },
    "requestID": "f74eda06-3937-4b74-aea7-3c1ae176b82f",
    "eventID": "5fb6113e-c3c9-4dd6-a50f-0500b8b90d5b",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "apiVersion": "2020-07-13",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

## FinSpace data plane events in CloudTrail

Data access logging helps to log actions taken against the managed S3 bucket in your
Amazon FinSpace environment's infrastructure account. The logging includes activity originating
from the FinSpace managed Apache Spark clusters, FinSpace managed SageMaker AI Studio Notebook, and the
FinSpace service itself. To enable logging of data access actions in FinSpace, you need to
enable logging of data activity in CloudTrail. For more information, see [Logging
data events for trails](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md").

The following example CloudTrail data event log entry demonstrates the event generated by
accessing a dataset from Amazon S3 CLI.

The `principalId` element contains details about the FinSpace user ID that
accesses a given FinSpace dataset ID. In this example, the user ID is the string **_jmiupn9hiyavwdw6pwdyva_** with
the prefix **_u\__** and the
dataset ID is the string **_64hzb00_** with the prefix **_ds\__**.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSAccount",
        "principalId": "AROA6J3NRQLZNQALLTUBQ:S3Read_u_jmiupn9hiyavwdw6pwdyva_ds_64hzb00",
        "accountId": "123456789012"
    },
    "eventTime": "2022-12-12T00:44:59Z",
    "eventSource": "finspace-api.amazonaws.com",
    "eventName": "GetObject",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "3.142.242.209",
    "userAgent": "[aws-internal/3 aws-sdk-java/1.12.348 Linux/4.14.296-222.539.amzn2.x86_64 OpenJDK_64-Bit_Server_VM/25.352-b09 java/1.8.0_352 vendor/Oracle_Corporation cfg/retry-mode/standard exec-env/AWS_ECS_FARGATE]",
    "requestParameters": {
        "bucketName": "finspace-us-east-2-hlbc5his5h6bgr3qgfstui",
        "Host": "finspace-us-east-2-hlbc5his5h6bgr3qgfstui.s3.us-east-2.amazonaws.com",
        "key": "ds/64hzb00/sn/gl/Global_Market_Holidays_and_Timings_autoupdate_QMIuqNmW6nAYEKDGTRXJAw/MMIuqQ20Kwku5t4fQuejUA/part-00000-4eff3050-b774-454b-9013-425840fb8057-c000.snappy.parquet"
    },
    "responseElements": null,
    "additionalEventData": {
        "SignatureVersion": "SigV4",
        "CipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
        "bytesTransferredIn": 0,
        "AuthenticationMethod": "AuthHeader",
        "x-amz-id-2": "7vrvbMFD5sIc/sdh9FHH2xxW5cY9ANw6J86lcszadwPaWusUAnhby2a45Hdw/yPlUyOBJSJvvq0=",
        "bytesTransferredOut": 167507
    },
    "requestID": "EFJT8ER65E6T17N7",
    "eventID": "675b77c4-fc8c-4083-8716-0e137f374848",
    "readOnly": true,
    "resources": [{
        "accountId": "123456789012",
        "type": "AWS::FinSpace::Environment",
        "ARN": "arn:aws:finspace:us-east-2:123456789012:environment/hlbc5his5h6bgr3qgfstui"
    }],
    "eventType": "AwsApiCall",
    "managementEvent": false,
    "recipientAccountId": "123456789012",
    "sharedEventID": "17bd447a-d738-4cab-8fd8-f820e2cf179b",
    "eventCategory": "Data"
}
```
