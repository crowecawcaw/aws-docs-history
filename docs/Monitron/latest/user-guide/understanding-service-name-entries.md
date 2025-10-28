Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Example: Amazon Monitron log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket that you specify. CloudTrail log files contain one or more log entries. An event
represents a single request from any source and includes information about the requested
action, the date and time of the action, request parameters, and so on. CloudTrail log files
aren't an ordered stack trace of the public API calls, so they don't appear in any
specific order.

The following examples show CloudTrail log entries that demonstrate the project deletion
(`DeleteProject`) action.

###### Topics

- [Successful DeleteProject action](#collapsible-section-1 "#collapsible-section-1")
- [Failed DeleteProject action (authorization
  error)](#collapsible-section-2 "#collapsible-section-2")
- [Failed DeleteProject action (conflict
  exception error)](#collapsible-section-3 "#collapsible-section-3")

## Successful DeleteProject action

The following example show what might appear in the CloudTrail log following a
successful `DeleteProject` action.

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "`principal ID`",
    "arn": "`ARN`",
    "accountId": "`account ID`",
    "accessKeyId": "`access key ID`",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "`principal ID`",
        "arn": "`ARN`",
        "accountId": "`account ID`",
        "userName": "`user name`"
      },
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "`timestamp`"
      }
    }
  },
  "eventTime": "`timestamp`",
  "eventSource": "monitron.amazonaws.com",
  "eventName": "DeleteProject",
  "awsRegion": "`region`",
  "sourceIPAddress": "`source IP address`",
  "userAgent": "`user agent`",
  "requestParameters": {
    "Name": "`name`"
  },
  "responseElements": {
    "Name": "`name`"
  },
  "requestID": "`request ID`",
  "eventID": "`event ID`",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "recipientAccountId": "`account ID`"
}
```

[Show moreShow less](# "#")

## Failed DeleteProject action (authorization

error)

The following example shows what might appear in the CloudTrail log following a
failed `DeleteProject` action due to an error occurring. In this
case, the error is an authorization error, where the user does not have
permission to delete the specified project.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "`principal ID`",
        "arn": "`ARN`",
        "accountId": "`account ID`",
        "accessKeyId": "`access key ID`",
        "userName": "`user name`",
        "sessionContext": {
            "sessionIssuer": {},
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "`timestamp`"
            }
        }
    },
    "eventTime": "`timestamp`",
    "eventSource": "monitron.amazonaws.com",
    "eventName": "DeleteProject",
    "awsRegion": "`region`",
    "sourceIPAddress": "`source IP address`",
    "userAgent": "`user agent`",
    "errorCode": "AccessDenied",
    "requestParameters": {
        "Name": "`name`"
    },
    "responseElements": {
        "Message": "User: `user ARN` is not authorized to perform: monitron:DeleteProject on resource: `resource ARN`"
    },
    "requestID": "`request ID`",
    "eventID": "`event ID`",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "`account ID`"
}
```

[Show moreShow less](# "#")

## Failed DeleteProject action (conflict

exception error)

The following example shows what might appear in the CloudTrail log following a
failed `DeleteProject` action due to an error occurring. In this
case, the error is a conflict exception, where sensors are still present when
Amazon Monitron attempts to delete a project.

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "`principal ID`",
    "arn": "`ARN`",
    "accountId": "`account ID`",
    "accessKeyId": "`access key ID`",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "`principal ID`",
        "arn": "`ARN`",
        "accountId": "`account ID`",
        "userName": "`user name`"
      },
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "`timestamp`"
      }
    }
  },
  "eventTime": "`timestamp`",
  "eventSource": "monitron.amazonaws.com",
  "eventName": "DeleteProject",
  "awsRegion": "`region`",
  "sourceIPAddress": "`source IP address`",
  "userAgent": "`user agent`",
  "errorCode": "ConflictException",
  "requestParameters": {
    "Name": "`name`"
  },
  "responseElements": {
    "message": "This project still has sensors associated to it and cannot be deleted."
  },
  "requestID": "`request ID`",
  "eventID": "`event ID`",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "recipientAccountId": "`account ID`"
}
```

[Show moreShow less](# "#")
