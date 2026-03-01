# Logging AWS AppSync API calls using AWS CloudTrail

AWS AppSync is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
user, role, or AWS service in AWS AppSync. CloudTrail captures all API calls for AWS AppSync as events. The
calls captured include calls from the AWS AppSync console and from code calls to the AWS AppSync APIs. You
can use the information collected by CloudTrail to determine the request that was made to AWS AppSync, the
IP address of the requester, who made the request, when the request was made, and additional
details.

You can create a _trail_ to enable continuous delivery of CloudTrail events to
an Amazon Simple Storage Service (Amazon S3) bucket, including events for AWS AppSync. If you don't configure a trail, you can
still view the most recent events in the CloudTrail console.

For more information about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## AWS AppSync information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. In the CloudTrail console in
**Event history**, you can view, search, and download recent events in your
AWS account. For more information, see [Viewing Events with CloudTrail
Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_.

For an ongoing record of events in your AWS account, including events for AWS AppSync, create
a trail. By default, when you create a trail in the console, the trail applies to all AWS
Regions. The trail logs events from all Regions in the AWS partition and delivers the log
files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following in the _AWS CloudTrail User Guide_:

- [Creating
  a Trail For Your AWS Account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [AWS Service Integrations With CloudTrail Logs](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [Receiving CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

CloudTrail logs all AWS AppSync API operations. For example, calls to the
`CreateGraphqlApi`, `CreateDataSource`, and `ListResolvers`
APIs generate entries in the CloudTrail log files. These and other operations are documented in the
[AWS AppSync API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

Every event or log entry contains information about who generated the request. The
identity information helps you determine:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see [CloudTrail userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md") in the _AWS CloudTrail User Guide_.

## AWS AppSync data events in CloudTrail

[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") provide information about the resource operations performed on or in a
resource (for example, reading or writing to an Amazon S3 object). These are also known as data
plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log
data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

You can log data events for the `AWS::AppSync::GraphQLApi` resource type
by using the CloudTrail console, AWS CLI, or CloudTrail API operations (these include query, mutation, and
subscription operations, connect operations to your real-time WebSocket endpoint, but not
messages sent over your real-time WebSocket endpoint.) For more information about how to log
data events, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console") and [Logging data events with the AWS Command Line Interface](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI") in the
_AWS CloudTrail User Guide_.

The following table lists the AWS AppSync resource type for which you can log data events. The
**Data event type (console)** column shows the value to choose
from the **Data event type** list in the CloudTrail console. The **resources.type value** column shows the `resources.type`
value, which you would specify when configuring advanced event selectors using the AWS CLI or
CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API
calls logged to CloudTrail for the resource type.

| Data event type (console) | resources.type value       | Data APIs logged to CloudTrail                                                   |
| ------------------------- | -------------------------- | -------------------------------------------------------------------------------- |
| **AppSync GraphQL**       | `AWS::AppSync::GraphQLApi` | [GraphQL](../APIReference/API_GraphqlApi.md "../APIReference/API_GraphqlApi.md") |

You can configure advanced event selectors to filter on the `eventName`,
`readOnly`, and `resources.ARN` fields to log only those events that
are important to you. For more information about these fields, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") in the
_AWS CloudTrail API Reference_.

```
[
  {
    "name": "Only 1 AppSync API",
    "fieldSelectors": [
      {
        "field": "eventCategory",
        "equals": [
          "Data"
        ]
      },
      {
        "field": "resources.type",
        "equals": [
          "AWS::AppSync::GraphQLApi"
        ]
      },
      {
        "field": "resources.ARN",
        "equals": [
          "arn:aws:appsync:us-east-1:111122223333:apis/YourGraphQLApiId"
        ]
      }
    ]
  }
]
```

## Understanding AWS AppSync log file entries

CloudTrail delivers events as log files that contain one or more log entries. An event
represents a single request from any source and includes information about the requested
operation, the date and time of the operation, the request parameters, and so on. Because
these log files aren't an ordered stack trace of the public API calls, they don't appear in
any specific order.

###### Note

The `requestID` isn't an authoritative unique ID for logs emitted from
AWS AppSync. The `requestID` can be overwritten by the client. Therefore, you should
use caution when making decisions based on this information.

The following example CloudTrail log entry demonstrates the `CreateApiKey`
operation.

```
{
  "Records": [{
    "eventVersion": "1.05",
    "userIdentity": {
      "type": "IAMUser",
      "principalId": "A1B2C3D4E5F6G7EXAMPLE",
      "arn": "arn:aws:iam::111122223333:user/Alice",
      "accountId": "111122223333",
      "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
      "userName": "diego_ramirez"
    },
    "eventTime": "2018-01-31T21:49:09Z",
    "eventSource": "appsync.amazonaws.com",
    "eventName": "CreateApiKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.2.0.1",
    "userAgent": "aws-cli/1.11.72 Python/2.7.11 Darwin/16.7.0 botocore/1.5.35",
    "requestParameters": {
      "apiId": "a1b2c3d4e5f6g7h8i9jexample"
    },
    "responseElements": {
      "apiKey": {
      "id": "***",
      "expires": 1518037200000
      }
    },
    "requestID": "99999999-9999-9999-9999-999999999999",
    "eventID": "99999999-9999-9999-9999-999999999999",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
    }
  ]
}
```

The following example CloudTrail log entry demonstrates the `ListApiKeys`
operation.

```
{
  "Records": [{
    "eventVersion": "1.05",
    "userIdentity": {
      "type": "IAMUser",
      "principalId": "A1B2C3D4E5F6G7EXAMPLE",
      "arn": "arn:aws:iam::111122223333:user/diego_ramirez",
      "accountId": "111122223333",
      "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
      "userName": "diego_ramirez"
    },
    "eventTime": "2018-01-31T21:49:09Z",
    "eventSource": "appsync.amazonaws.com",
    "eventName": "ListApiKeys",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.2.0.1",
    "userAgent": "aws-cli/1.11.72 Python/2.7.11 Darwin/16.7.0 botocore/1.5.35",
    "requestParameters": {
      "apiId": "a1b2c3d4e5f6g7h8i9jexample"
    },
    "responseElements": {
      "apiKeys": [
              {
                    "id": "***",
                    "expires": 1517954400000
              },
              {
                    "id": "***",
                    "expires": 1518037200000
              },
            ]
    },
    "requestID": "99999999-9999-9999-9999-999999999999",
    "eventID": "99999999-9999-9999-9999-999999999999",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
    }
  ]
}
```

The following example CloudTrail log entry demonstrates the `DeleteApiKey`
operation.

```
{
  "Records": [{
    "eventVersion": "1.05",
    "userIdentity": {
      "type": "IAMUser",
      "principalId": "A1B2C3D4E5F6G7EXAMPLE",
      "arn": "arn:aws:iam::111122223333:user/diego_ramirez",
      "accountId": "111122223333",
      "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
      "userName": "diego_ramirez"
    },
    "eventTime": "2018-01-31T21:49:09Z",
    "eventSource": "appsync.amazonaws.com",
    "eventName": "DeleteApiKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.2.0.1",
    "userAgent": "aws-cli/1.11.72 Python/2.7.11 Darwin/16.7.0 botocore/1.5.35",
    "requestParameters": {
      "id": "***",
      "apiId": "a1b2c3d4e5f6g7h8i9jexample"
    },
    "responseElements": null,
    "requestID": "99999999-9999-9999-9999-999999999999",
    "eventID": "99999999-9999-9999-9999-999999999999",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
    }
  ]
}
```

The following example CloudTrail log entry demonstrates a successful GraphQL mutation authorized
with a custom Lambda function authorizer.

```
{
  "eventVersion": "1.10",
    "userIdentity": {
      "type": "Unknown"
    },
    "eventTime": "2024-11-06T15:42:30Z",
    "eventSource": "appsync.amazonaws.com",
    "eventName": "GraphQL",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "15.248.1.214",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0",
    "requestParameters": null,
    "responseElements": null,
    "additionalEventData": {
      "operationName": "MyMutation",
      "authType": [
        "AWS_LAMBDA"
      ],
      "fieldAuthorizationResults": {
        "deniedFields": []
      }
    },
    "requestID": "c2d3768b-3446-40a1-bd95-8399fe776f96",
    "eventID": "21568be1-a1a8-4f43-b978-63cb4cc02a96",
    "readOnly": false,
    "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::AppSync::GraphQLApi",
      "ARN": "arn:aws:appsync:us-west-2:123456789012:apis/rxfqcxzi3nbvza2hsq4njqqq6u"
    }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": false,
    "recipientAccountId": "123456789012",
    "eventCategory": "Data"
}
```

The following example CloudTrail log entry demonstrates a partially successful GraphQL operation
authorized with a custom Lambda function authorizer. Note the
`fieldAuthorizationResults.deniedFields` property that specifies the denied
fields.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "Unknown"
  },
  "eventTime": "2024-11-06T16:11:49Z",
  "eventSource": "appsync.amazonaws.com",
  "eventName": "GraphQL",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "15.248.1.214",
  "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0",
  "requestParameters": null,
  "responseElements": null,
  "additionalEventData": {
    "operationName": "MyMutation",
    "authType": [
      "AWS_LAMBDA"
    ],
    "fieldAuthorizationResults": {
      "deniedFields": [
        "arn:aws:appsync:us-west-2:123456789012:apis/rxfqcxzi3nbvza2hsq4njqqq6u/types/Mutation/fields/createPost",
        "arn:aws:appsync:us-west-2:123456789012:apis/rxfqcxzi3nbvza2hsq4njqqq6u/types/Subscription/fields/onCreatePost",
        "arn:aws:appsync:us-west-2:123456789012:apis/rxfqcxzi3nbvza2hsq4njqqq6u/types/Post/fields/status"
      ]
    }
  },
  "requestID": "ae817c4c-66ba-4f64-92a5-ba9c9c341dcd",
  "eventID": "30109698-7605-476a-9dff-b7ed78d134dc",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::AppSync::GraphQLApi",
      "ARN": "arn:aws:appsync:us-west-2:123456789012:apis/rxfqcxzi3nbvza2hsq4njqqq6u"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "123456789012",
  "eventCategory": "Data"
}
```

The following example CloudTrail log entry demonstrates a failed GraphQL operation.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "Unknown"
  },
  "eventTime": "2024-11-06T15:51:11Z",
  "eventSource": "appsync.amazonaws.com",
  "eventName": "GraphQL",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "15.248.1.214",
  "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0",
  "errorCode": "AccessDenied",
  "errorMessage": "{\n \"errors\" : [ {\n \"errorType\" : \"UnauthorizedException\",\n \"message\" : \"You are not authorized to make this call.\"\n } ]\n}",
  "requestParameters": null,
  "responseElements": null,
  "additionalEventData": {
    "operationName": "MyFullyDeniedLambdaMutation"
  },
  "requestID": "0bef3cf3-a48b-4de9-8b1f-038afb563516",
  "eventID": "b738651f-4ec0-4548-8fec-200c6b42842b",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::AppSync::GraphQLApi",
      "ARN": "arn:aws:appsync:us-west-2:123456789012:apis/rxfqcxzi3nbvza2hsq4njqqq6u"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "123456789012",
  "eventCategory": "Data"
}
```

The following example demonstrates a successful GraphQL request.

```
{
  "eventVersion": "1.10",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AIDACKCEVSQ6C2EXAMPLE:jane_doe",
    "arn": "arn:aws:sts::123456789012:assumed-role/admin/jane_doe",
    "accountId": "123456789012",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::123456789012:role/admin",
        "accountId": "123456789012",
        "userName": "jane_doe"
      },
      "attributes": {
        "creationDate": "2024-11-06T15:40:09Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2024-11-06T16:03:43Z",
  "eventSource": "appsync.amazonaws.com",
  "eventName": "GraphQL",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "15.248.1.214",
  "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:131.0) Gecko/20100101 Firefox/131.0",
  "requestParameters": null,
  "responseElements": null,
  "additionalEventData": {
    "operationName": "IamFullSuccess",
    "authType": [
      "AWS_IAM"
    ],
    "fieldAuthorizationResults": {
      "allowedFields": [
        "arn:aws:appsync:us-west-2:123456789012:apis/rxfqcxzi3nbvza2hsq4njqqq6u/types/Mutation/fields/createSecondPostAllowed"
      ],
      "deniedFields": []
    }
  },
  "requestID": "edc6bbbf-6bf2-40f5-820f-ef444f12e0c1",
  "eventID": "524656a5-0925-4370-9e7e-08888e9c299f",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::AppSync::GraphQLApi",
      "ARN": "arn:aws:appsync:us-west-2:123456789012:apis/rxfqcxzi3nbvza2hsq4njqqq6u"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "123456789012",
  "eventCategory": "Data"
}
```
