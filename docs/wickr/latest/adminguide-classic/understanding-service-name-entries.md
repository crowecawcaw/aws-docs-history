This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Understanding Wickr log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the
`CreateAdminSession` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "`<principal-id>`",
        "arn": "`<arn>`",
        "accountId": "`<account-id>`",
        "accessKeyId": "`<access-key-id>`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "`<principal-id>`",
                "arn": "`<arn>`",
                "accountId": "`<account-id>`",
                "userName": "`<user-name>`"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-03-10T07:53:17Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-03-10T08:19:24Z",
    "eventSource": "wickr.amazonaws.com",
    "eventName": "CreateAdminSession",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "`<ip-address>`",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "requestParameters": {
        "networkId": 56019692
    },
    "responseElements": {
        "sessionCookie": "***",
        "sessionNonce": "***"
    },
    "requestID": "39ed0e6f-36e9-460d-8a6e-f24be0ec11c5",
    "eventID": "98ccb633-0e6c-4325-8996-35c3043022ac",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`<account-id>`",
    "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry that demonstrates the
`CreateNetwork` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "`<principal-id>`",
        "arn": "`<arn>`",
        "accountId": "`<account-id>`",
        "accessKeyId": "`<access-key-id>`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "`<principal-id>`",
                "arn": "`<arn>`",
                "accountId": "`<account-id>`",
                "userName": "`<user-name>`"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-03-10T07:53:17Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-03-10T07:54:09Z",
    "eventSource": "wickr.amazonaws.com",
    "eventName": "CreateNetwork",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "`<ip-address>`",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "requestParameters": {
        "networkName": "BOT_Network",
        "accessLevel": "3000"
    },
    "responseElements": null,
    "requestID": "b83c0b6e-73ae-45b6-8c85-9910f64d33a1",
    "eventID": "551277bb-87e0-4e66-b2a0-3cc1eff303f3",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`<account-id>`",
    "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry that demonstrates the
`ListNetworks` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "`<principal-id>`",
        "arn": "`<arn>`",
        "accountId": "`<account-id>`",
        "accessKeyId": "`<access-key-id>`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "`<principal-id>`",
                "arn": "`<arn>`",
                "accountId": "`<account-id>`",
                "userName": "`<user-name>`"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-03-10T12:19:39Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-03-10T12:29:32Z",
    "eventSource": "wickr.amazonaws.com",
    "eventName": "ListNetworks",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "`<ip-address>`",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "b9800ba8-541a-43d1-9c8e-efd94d5f2115",
    "eventID": "5fbc83d7-771b-457d-9329-f85163a6a428",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`<account-id>`",
    "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry that demonstrates the
`UpdateNetworkdetails` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "`<principal-id>`",
        "arn": "`<arn>`",
        "accountId": "`<account-id>`",
        "accessKeyId": "`<access-key-id>`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "`<principal-id>`",
                "arn": "`<arn>`",
                "accountId": "`<account-id>`",
                "userName": "`<user-name>`"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-03-08T22:42:15Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-03-08T22:42:58Z",
    "eventSource": "wickr.amazonaws.com",
    "eventName": "UpdateNetworkDetails",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "`<ip-address>`",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "requestParameters": {
        "networkName": "CloudTrailTest1",
        "networkId": `<network-id>`
    },
    "responseElements": null,
    "requestID": "abced980-23c7-4de1-b3e3-56aaf0e1fdbb",
    "eventID": "a4dc3391-bdce-487d-b9b0-6f76cedbb198",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`<account-id>`",
    "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry that demonstrates the
`TagResource` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "`<principal-id>`",
        "arn": "`<arn>`",
        "accountId": "`<account-id>`",
        "accessKeyId": "`<access-key-id>`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "`<principal-id>`",
                "arn": "`<arn>`",
                "accountId": "`<account-id>`",
                "userName": "`<user-name>`"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-03-08T22:42:15Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-03-08T23:06:04Z",
    "eventSource": "wickr.amazonaws.com",
    "eventName": "TagResource",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "`<ip-address>`",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "requestParameters": {
        "resource-arn": "`<arn>`",
        "tags": {
            "some-existing-key-3": "value 1"
        }
    },
    "responseElements": null,
    "requestID": "4ff210e1-f69c-4058-8ac3-633fed546983",
    "eventID": "26147035-8130-4841-b908-4537845fac6a",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`<account-id>`",
    "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry that demonstrates the
`ListTagsForResource` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "`<principal-id>`",
        "arn": "`<arn>`",
        "accountId": "`<account-id>`",
        "accessKeyId": "`<access-key-id>`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "`<access-key-id>`",
                "arn": "`<arn>`",
                "accountId": "`<account-id>`",
                "userName": "`<user-name>`"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-03-08T18:50:37Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-03-08T18:50:37Z",
    "eventSource": "wickr.amazonaws.com",
    "eventName": "ListTagsForResource",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "`<ip-address>`",
    "userAgent": "axios/0.27.2",
    "errorCode": "AccessDenied",
    "requestParameters": {
        "resource-arn": "`<arn>`"
    },
    "responseElements": {
        "message": "User: `<arn>` is not authorized to perform: wickr:ListTagsForResource on resource: `<arn>` with an explicit deny"
    },
    "requestID": "c7488490-a987-4ca2-a686-b29d06db89ed",
    "eventID": "5699d5de-3c69-4fe8-b353-8ae62f249187",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`<account-id>`",
    "eventCategory": "Management"
}
```
