# CloudTrail logging for Transfer Family web apps

CloudTrail is an AWS service that creates a record of actions taken within your AWS account.
It continuously monitors and records API operations for activities like console sign-ins,
AWS Command Line Interface commands, and SDK/API operations. This allows you to keep a log of who took what
action, when, and from where. CloudTrail helps with auditing, access management, and regulatory
compliance by providing a history of all activity in your AWS environment.

For Transfer Family web apps, you can track both authentication events and data access operations
performed by your users. To enable comprehensive logging, you need to:

1. Configure CloudTrail to log management events for tracking authentication
   activities.
2. Enable Amazon S3 data events to track file operations performed through your web
   app.

See also

- [CloudTrail use cases
  for IAM Identity Center](../../../singlesignon/latest/userguide/sso-cloudtrail-use-cases.md "../../../singlesignon/latest/userguide/sso-cloudtrail-use-cases.md")
- [Understanding IAM Identity Center sign-in events](../../../singlesignon/latest/userguide/understanding-sign-in-events.md "../../../singlesignon/latest/userguide/understanding-sign-in-events.md")
- [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md")
- [Enabling
  CloudTrail event logging for S3 buckets and objects](../../../AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.md "../../../AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.md")
- [Amazon S3 CloudTrail
  events](../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md "../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md")

## Enabling Amazon S3 data events

To track file operations performed through Transfer Family web apps on your Amazon S3 buckets, you
need to enable data events for those buckets. Data events provide object-level API
activity and are particularly useful for tracking file uploads, downloads, and other
operations performed by web app users.

To enable Amazon S3 data events for your Transfer Family web app:

1. Open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, choose **Trails**, and then select an
   existing trail or create a new one.
3. Under **Advanced event selectors**, choose
   **Edit**.
4. Choose **Add advanced event selector**.
5. For the first field selector:
   - Set **Field** to `eventCategory`
   - Set **Operator** to
     **Equals**
   - Set **Value** to `Data`

6. Choose **Add field** and for the second field
   selector:
   - Set **Field** to `resources.type`
   - Set **Operator** to
     **Equals**
   - Set **Value** to `AWS::S3::Object`

7. (Optional) To log events for specific buckets only, choose **Add
   field** and add:
   - Set **Field** to `resources.ARN`
   - Set **Operator** to **Starts
     with**
   - Set **Value** to
     `arn:aws:s3:::your-bucket-name/`

8. Choose **Save changes**.

Alternatively, you can use the legacy data events configuration:

1. Under **Data events**, choose
   **Edit**.
2. For **Data event type**, select **S3 bucket and
   object events**.
3. Choose the Amazon S3 buckets to log data events for. You can select **All
   current and future S3 buckets** or specify individual
   buckets.
4. Choose whether to log **Read** events,
   **Write** events, or both.
5. Choose **Save changes**.

After enabling data events, you can access these logs in the Amazon S3 bucket configured
for CloudTrail. The logs include details such as the user who performed the action, the action
timestamp, the specific object affected, and the `onBehalfOf` field that
helps trace the `userId` for actions performed through Transfer Family web apps.

### Finding and viewing your logs

There are several ways to find and view CloudTrail logs for your Transfer Family web app:

#### Using the CloudTrail console

The fastest way to view recent events:

1. Open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. Choose **Event history**.
3. Filter events by:
   - **Event source**:
     `signin.amazonaws.com` for web app events
   - **Event source**:
     `s3.amazonaws.com` for file operations

4. Click any event to view detailed information.

#### Accessing logs in Amazon S3

To access the complete log files stored in Amazon S3:

1. Identify your CloudTrail trail's Amazon S3 bucket:

```
aws cloudtrail describe-trails --query 'trailList[*].[Name,S3BucketName]' --output table
```

2. Navigate to the log files in Amazon S3:

```
aws s3 ls s3://your-cloudtrail-bucket/AWSLogs/account-id/CloudTrail/region/YYYY/MM/DD/
```

3. Download and search log files for your web app ID:

```
aws s3 cp s3://your-cloudtrail-bucket/AWSLogs/account-id/CloudTrail/region/YYYY/MM/DD/ . --recursive
gunzip *.json.gz
grep -l "webapp-1a2b3c4d5e6f7g8h9" *.json
```

#### Using AWS CLI to search events

Search for specific web app events using the AWS CLI:

```
aws logs filter-log-events \
  --log-group-name /aws/cloudtrail/your-trail-name \
  --filter-pattern "webapp-1a2b3c4d5e6f7g8h9" \
  --start-time $(date -d "1 day ago" +%s)000
```

Or search for authentication events:

```
aws logs filter-log-events \
  --log-group-name /aws/cloudtrail/your-trail-name \
  --filter-pattern "UserAuthentication" \
  --start-time $(date -d "1 day ago" +%s)000
```

## Authentication log examples

CloudTrail logs authentication events for Transfer Family web apps, which can help you track successful
and failed sign-in attempts. These logs are particularly useful for security monitoring
and compliance purposes.

###### Topics

- [Example log entry for
  credential verification](#webapp-credential-verification-example "#webapp-credential-verification-example")
- [Example log entry for sign-in
  authentication](#webapp-signin-authentication-example "#webapp-signin-authentication-example")
- [Example log entry for
  ListCallerAccessGrants](#webapp-list-caller-access-grants-example "#webapp-list-caller-access-grants-example")
- [Example log entry for GetDataAccess
  event](#webapp-get-data-access-example "#webapp-get-data-access-example")

### Example log entry for

credential verification

The following example shows a CloudTrail log entry for a credential verification event
that occurs during the authentication process.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "123456789012",
        "arn": "",
        "accountId": "123456789012",
        "accessKeyId": "",
        "userName": "demo-user-2",
        "onBehalfOf": {
            "userId": "f12bb510-a011-702f-10dd-5607e2776dbc",
            "identityStoreArn": "arn:aws:identitystore::123456789012:identitystore/d-9a670c546e"
        },
        "credentialId": "58138a11-87e5-401d-8f0b-7161c9389112"
    },
    "eventTime": "2025-08-08T15:29:30Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "CredentialVerification",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "192.0.2.224",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "requestParameters": null,
    "responseElements": null,
    "additionalEventData": {
        "AuthWorkflowID": "f304a48b-7b6d-41c8-b136-4f49c91c1f31",
        "CredentialType": "PASSWORD"
    },
    "requestID": "ff936828-4a81-453c-802d-81368b6bca1a",
    "eventID": "70cb7008-493d-42c2-a9eb-38bf168af6a8",
    "readOnly": false,
    "eventType": "AWSServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "serviceEventDetails": {
        "CredentialVerification": "Success"
    },
    "eventCategory": "Management"
}
```

This event provides additional detail about the credential verification step in
the authentication process, showing the specific credential ID and authentication
workflow ID used.

### Example log entry for sign-in

authentication

The following example shows a CloudTrail log entry for a successful user authentication
event during web app sign-in using IAM Identity Center.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "123456789012",
        "arn": "",
        "accountId": "123456789012",
        "accessKeyId": "",
        "userName": "demo-user-2",
        "onBehalfOf": {
            "userId": "f12bb510-a011-702f-10dd-5607e2776dbc",
            "identityStoreArn": "arn:aws:identitystore::123456789012:identitystore/d-9a670c546e"
        },
        "credentialId": "b41f0a02-1635-4d07-a414-aecf9e14b906"
    },
    "eventTime": "2025-08-07T14:09:07Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "UserAuthentication",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "192.0.2.14",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "requestParameters": null,
    "responseElements": null,
    "additionalEventData": {
        "AuthWorkflowID": "7a4ef12c-7c4b-4bc3-b5bd-c2469afcc795",
        "LoginTo": "https://example.awsapps.com/start/",
        "CredentialType": "PASSWORD"
    },
    "requestID": "fc91bcf0-ac53-4454-a1a0-fb911eacc095",
    "eventID": "18522007-1e60-4a71-b2b5-150baf504ab3",
    "readOnly": false,
    "eventType": "AWSServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "serviceEventDetails": {
        "UserAuthentication": "Success"
    },
    "eventCategory": "Management"
}
```

In this example, note the following important fields:

- `eventSource`: Shows "signin.amazonaws.com", indicating this is
  an IAM Identity Center authentication event.
- `userIdentity.onBehalfOf`: Contains the user ID and identity
  store ARN for the web app user.
- `additionalEventData.LoginTo`: Shows the IAM Identity Center application URL
  being accessed.
- `additionalEventData.CredentialType`: Indicates the
  authentication method used (PASSWORD).
- `serviceEventDetails`: Shows the authentication result
  (Success).

### Example log entry for

ListCallerAccessGrants

The following example shows a CloudTrail log entry for a ListCallerAccessGrants event,
which occurs when Transfer Family web app queries available access grants for a user.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLEID:aws-transfer",
        "arn": "arn:aws:sts::123456789012:assumed-role/AWSTransferWebAppIdentityBearer-us-east-2/aws-transfer",
        "accountId": "123456789012",
        "accessKeyId": "ASIAEXAMPLEKEY",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAEXAMPLEID",
                "arn": "arn:aws:iam::123456789012:role/service-role/AWSTransferWebAppIdentityBearer-us-east-2",
                "accountId": "123456789012",
                "userName": "AWSTransferWebAppIdentityBearer-us-east-2"
            },
            "attributes": {
                "creationDate": "2025-08-08T15:29:34Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "transfer.amazonaws.com",
        "onBehalfOf": {
            "userId": "f12bb510-a011-702f-10dd-5607e2776dbc",
            "identityStoreArn": "arn:aws:identitystore::123456789012:identitystore/d-9a670c546e"
        }
    },
    "eventTime": "2025-08-08T15:29:35Z",
    "eventSource": "s3.amazonaws.com",
    "eventName": "ListCallerAccessGrants",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "transfer.amazonaws.com",
    "userAgent": "transfer.amazonaws.com",
    "requestParameters": {
        "Host": "123456789012.s3-control.dualstack.us-east-2.amazonaws.com",
        "allowedByApplication": "true",
        "maxResults": "100"
    },
    "responseElements": null,
    "additionalEventData": {
        "SignatureVersion": "SigV4",
        "CipherSuite": "TLS_AES_128_GCM_SHA256",
        "bytesTransferredIn": 0,
        "AuthenticationMethod": "AuthHeader",
        "x-amz-id-2": "1g34AaAELn/fntxwrifVsr41VDl8dp5ygWFasHJFNVq5FDCWYfX0ye7s4tWHEJC8ppI5lLePYLIcw3iTXAgn5Q==",
        "bytesTransferredOut": 462
    },
    "requestID": "48485MTZEDWT0ANT",
    "eventID": "3de5dd60-b7cf-474c-a1ab-631467c1a5c3",
    "readOnly": true,
    "resources": [
        {
            "accountId": "123456789012",
            "type": "AWS:S3::AccessGrantsInstance",
            "ARN": "arn:aws:s3:us-east-2:123456789012:access-grants/default"
        }
    ],
    "eventType": "AWSApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

In this example, note the following important fields:

- `eventName`: Shows this is a ListCallerAccessGrants event,
  which queries available S3 access grants.
- `requestParameters.allowedByApplication`: Indicates the query
  is filtered to grants allowed by the application.
- `requestParameters.maxResults`: Shows the maximum number of
  grants to return in the response.
- `userIdentity.onBehalfOf`: Links the request to the specific
  web app user.

This event helps track when Transfer Family web app queries what S3 resources a user has
access to, providing visibility into access grant discovery operations.

### Example log entry for GetDataAccess

event

The following example shows a CloudTrail log entry for a GetDataAccess event, which
occurs when Transfer Family web app requests access permissions for S3 resources on behalf of a
user.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROASEQRAEABP7ADWEZA5:aws-transfer",
        "arn": "arn:aws:sts::123456789012:assumed-role/AWSTransferWebAppIdentityBearer-ap-southeast-1/aws-transfer",
        "accountId": "123456789012",
        "accessKeyId": "ASIAEXAMPLEKEY",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROASEQRAEABP7ADWEZA5",
                "arn": "arn:aws:iam::123456789012:role/service-role/AWSTransferWebAppIdentityBearer-ap-southeast-1",
                "accountId": "123456789012",
                "userName": "AWSTransferWebAppIdentityBearer-ap-southeast-1"
            },
            "attributes": {
                "creationDate": "2025-05-08T16:09:05Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "transfer.amazonaws.com",
        "onBehalfOf": {
            "identityStoreArn": "arn:aws:identitystore::123456789012:identitystore/d-9667b0da7a",
            "userId": "191a35ec-10a1-70c1-e4ab-e2802411e13e"
        }
    },
    "eventTime": "2025-05-08T16:10:25Z",
    "eventSource": "s3.amazonaws.com",
    "eventName": "GetDataAccess",
    "awsRegion": "ap-southeast-1",
    "sourceIPAddress": "transfer.amazonaws.com",
    "userAgent": "transfer.amazonaws.com",
    "requestParameters": {
        "Host": "123456789012.s3-control.dualstack.ap-southeast-1.amazonaws.com",
        "durationSeconds": 900,
        "permission": "READWRITE",
        "target": "s3://amzn-s3-demo-bucket/users/john.doe/documents/*"
    },
    "responseElements": null,
    "additionalEventData": {
        "AuthenticationMethod": "AuthHeader",
        "CipherSuite": "TLS_AES_128_GCM_SHA256",
        "SignatureVersion": "SigV4",
        "bytesTransferredIn": 0,
        "bytesTransferredOut": 2244,
        "x-amz-id-2": "8ce8sZOgNwsaj9w1mzagyA+csONjYl8FgEw4FGpE8DARi90aNC0RFWlTYNEn7ChqE9RCJrTzMvS+ru7Vz2xXHrkQt/1uQ9exZTZdlhX+/fM="
    },
    "requestID": "BXGSKKQXCWS5RAHB",
    "eventID": "c11db1d1-dfb8-431e-8625-48eba2ebadfe",
    "readOnly": true,
    "resources": [
        {
            "type": "AWS:S3::AccessGrantsInstance",
            "ARN": "arn:aws:s3:ap-southeast-1:123456789012:access-grants/default",
            "accountId": "123456789012"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

In this example, note the following important fields:

- `eventName`: Shows this is a GetDataAccess event, which occurs
  when Transfer Family requests access permissions for S3 resources.
- `userIdentity.onBehalfOf`: Contains the identity store ARN and
  user ID, linking the access request to the specific web app user.
- `requestParameters.target`: Shows the S3 path pattern for which
  access was requested.
- `requestParameters.permission`: Indicates the type of access
  requested (READWRITE, READ, or WRITE).
- `requestParameters.durationSeconds`: Shows how long the access
  grant is valid (typically 900 seconds/15 minutes).
- `sourceIPAddress` and `userAgent`: Both show
  "transfer.amazonaws.com", indicating this is an internal service
  request.

GetDataAccess events are particularly useful for tracking when Transfer Family web app users
are granted access to specific S3 resources, helping you monitor access patterns and
ensure proper authorization.

## Viewing CloudTrail log entries

There are several ways to view and analyze CloudTrail log entries for your Transfer Family web
app:

### Using the CloudTrail console

The CloudTrail console provides a user-friendly interface for viewing and filtering log
entries:

1. Open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, choose **Event history**.
3. Use the filter options to narrow down the events:
   - Set **Event source** to
     `transfer.amazonaws.com` to view only Transfer Family
     events.
   - Filter by **Event name** to see specific
     operations like `UserAuthentication`.
   - Use **Time range** to focus on events within a
     specific period.

4. Click on any event to view its detailed information.

### Accessing logs in Amazon S3

If you've configured a CloudTrail trail to deliver logs to an Amazon S3 bucket, you can
access the raw log files directly:

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Navigate to the bucket and prefix where your CloudTrail logs are stored.
3. The logs are organized by year, month, day, and region. Navigate to the
   appropriate directory.
4. Download and open the log files, which are in JSON format.
