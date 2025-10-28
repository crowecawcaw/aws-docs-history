# Understanding Neptune Analytics log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.
CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes
information about the requested action, the date and time of the action, request parameters, and other information.
CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.

Every event or log entry contains information about who generated the request. The identity information helps
you determine the following:

- Whether the request was made with root or user credentials.
- Whether the request was made with temporary security credentials for a role or federated user.
- Whether the request was made by another AWS service.

For more information, see the CloudTrail userIdentity element.

The following examples demonstrate CloudTrail logs of these event types:

- [CreateGraph](../apiref/API_CreateGraph.md "../apiref/API_CreateGraph.md")

```
{
"eventVersion": "1.08",
"userIdentity": {
    "type": "AssumedRole",
    "principalId": "AKIAIOSFODNN7EXAMPLE:bob",
    "arn": "arn:aws:sts::111122223333:assumed-role/users/bob",
    "accountId": "111122223333",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
        "sessionIssuer": {
            "type": "Role",
            "principalId": "AKIAI44QH8DHBEXAMPLE",
            "arn": "arn:aws:iam::111122223333:role/admin-role",
            "accountId": "111122223333",
            "userName": "bob"
        },
        "webIdFederationData": {},
        "attributes": {
            "creationDate": "2023-11-22T13:45:16Z",
            "mfaAuthenticated": "false"
        }
    },
    "invokedBy": "AWS Internal"
},
"eventTime": "2023-11-22T13:53:45Z",
"eventSource": "neptune-graph.amazonaws.com",
"eventName": "CreateGraph",
"awsRegion": "us-east-1",
"sourceIPAddress": "192.0.2.0",
"userAgent": "aws-cli/1.15.64 Python/2.7.16 Darwin/17.7.0 botocore/1.10.63",
"requestParameters": {
    "graphName": "bobgraph",
    "provisionedMemory": 128,
    "clientToken": "bobtoken",
    "deletionProtection": false
},
"responseElements": {
    "graph": {
        "allowFromPublic": false,
        "arn": "arn:aws:neptune-graph:us-east-1:111122223333:graph/g-b52example",
        "createTime": 1700661225.003,
        "deletionProtection": false,
        "endpoint": "g-b52example.neptune-graph-gamma.us-east-1.amazonaws.com",
        "id": "g-b52example",
        "kmsKeyIdentifier": "AWS_OWNED_KEY",
        "name": "bobgraph",
        "provisionedMemory": 128,
        "replicaCount": 0,
        "status": "CREATING"
    }
},
"requestID": "4997ab5c-822d-4823-9c10-EXAMPLE",
"eventID": "58fc2480-7407-47f9-bc14-EXAMPLE",
"readOnly": false,
"eventType": "AwsApiCall",
"managementEvent": true,
"recipientAccountId": "111122223333",
"eventCategory": "Management"
}
```

- [CreateGraph (Access Denied)](../apiref/API_CreateGraph.md "../apiref/API_CreateGraph.md")

```
{
"eventVersion": "1.08",
"userIdentity": {
    "type": "AssumedRole",
    "principalId": "AKIAIOSFODNN7EXAMPLE:bob",
    "arn": "arn:aws:sts::111122223333:assumed-role/users/bob",
    "accountId": "111122223333",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
        "sessionIssuer": {
            "type": "Role",
            "principalId": "AKIAI44QH8DHBEXAMPLE",
            "arn": "arn:aws:iam::444455556666:role/admin-role",
            "accountId": "444455556666",
            "userName": "bob"
        },
        "webIdFederationData": {},
        "attributes": {
            "creationDate": "2023-11-22T13:36:22Z",
            "mfaAuthenticated": "false"
        }
    }
},
"eventTime": "2023-11-22T13:36:22Z",
"eventSource": "neptune-graph.amazonaws.com",
"eventName": "CreateGraph",
"awsRegion": "us-east-1",
"sourceIPAddress": "192.0.2.0",
"userAgent": "aws-cli/1.15.64 Python/2.7.16 Darwin/17.7.0 botocore/1.10.63",
"errorCode": "AccessDenied",
"requestParameters": {
    "graphName": "bobgraph",
    "replicaCount": 0,
    "clientToken": "2040f466-220d-49e5-a45c-EXAMPLE",
    "allowFromPublic": false,
    "provisionedMemory": 128,
    "deletionProtection": false
},
"responseElements": {
    "Message": "User: arn:aws:sts::444455556666:assumed-role/bobrole/bobsession is not authorized to perform: neptune-graph:CreateGraph on resource: arn:aws:neptune-graph:us-east-1:444455556666:graph/*"
},
"requestID": "89f04d5b-14d1-4c3a-b44d-EXAMPLE",
"eventID": "373c5468-99ac-4fed-9def-EXAMPLE",
"readOnly": false,
"eventType": "AwsApiCall",
"managementEvent": true,
"recipientAccountId": "111122223333",
"eventCategory": "Management"
```

- [ListGraphs](../apiref/API_ListGraphs.md "../apiref/API_ListGraphs.md")

```
{
"eventVersion": "1.08",
"userIdentity": {
    "type": "AssumedRole",
    "principalId": "AKIAIOSFODNN7EXAMPLE:bob",
    "arn": "arn:aws:sts::111122223333:assumed-role/users/bob",
    "accountId": "111122223333",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
        "sessionIssuer": {
            "type": "Role",
            "principalId": "AKIAI44QH8DHBEXAMPLE",
            "arn": "arn:aws:iam::111122223333:role/admin-role",
            "accountId": "111122223333",
            "userName": "bob"
        },
        "webIdFederationData": {},
        "attributes": {
            "creationDate": "2023-11-22T13:34:55Z",
            "mfaAuthenticated": "false"
        }
    }
},
"eventTime": "2023-11-22T13:42:56Z",
"eventSource": "neptune-graph.amazonaws.com",
"eventName": "ListGraphs",
"awsRegion": "us-east-1",
"sourceIPAddress": "192.0.2.0",
"userAgent": "aws-cli/1.15.64 Python/2.7.16 Darwin/17.7.0 botocore/1.10.63",
"requestParameters": null,
"responseElements": null,
"requestID": "fb7e8333-61a3-4bcd-a6d5-EXAMPLE",
"eventID": "85002909-acf5-499f-a814-EXAMPLE",
"readOnly": true,
"eventType": "AwsApiCall",
"managementEvent": true,
"recipientAccountId": "111122223333",
"eventCategory": "Management"
}
```

- [GetGraphSummary](../apiref/API_GetGraphSummary.md "../apiref/API_GetGraphSummary.md")

```
{
"eventVersion": "1.09",
"userIdentity": {
    "type": "AssumedRole",
    "principalId": "AKIAIOSFODNN7EXAMPLE:bob",
    "arn": "arn:aws:sts::111122223333:assumed-role/users/bob",
    "accountId": "111122223333",
    "sessionContext": {
        "sessionIssuer": {
            "type": "Role",
            "principalId": "AKIAI44QH8DHBEXAMPLE",
            "arn": "arn:aws:iam::111122223333:role/admin-role",
            "accountId": "111122223333",
            "userName": "bob"
        },
        "attributes": {
            "creationDate": "2023-11-22T13:34:55Z",
            "mfaAuthenticated": "false"
        }
    }
},
"eventTime": "2023-11-22T13:42:56Z",
"eventSource": "neptune-graph.amazonaws.com",
"eventName": "GetGraphSummary",
"awsRegion": "us-east-1",
"sourceIPAddress": "192.0.2.0",
"userAgent": "aws-cli/1.15.64 Python/2.7.16 Darwin/17.7.0 botocore/1.10.63",
"requestParameters": {
    "requestType": "GET",
    "requestParameters": {},
    "requestPayload": "/summary",
    "requestContentType": "application/json",
    "requestHeaders": {
        "content-length": "0",
        "Accept": "application/xml",
        "x-amz-date": "20231122T133455Z",
        "User-Agent": "aws-cli/1.15.64 Python/2.7.16 Darwin/17.7.0 botocore/1.10.63",
        "Connection": "keep-alive",
        "X-Forwarded-For": "192.0.2.0",
        "Host": "localhost:8080",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/json"
    },
    "authorizedIamActions": []
},
"responseElements": null,
"requestID": "fb7e8333-61a3-4bcd-a6d5-EXAMPLE",
"eventID": "85002909-acf5-499f-a814-EXAMPLE",
"readOnly": true,
"resources": [
    {
        "accountId": "111122223333",
        "type": "AWS::NeptuneGraph::Graph",
        "ARN": "arn:aws:neptune-graph:us-east-1:111122223333:graph/g-dbiexample"
    }
],
"eventType": "AwsApiCall",
"managementEvent": false,
"recipientAccountId": "111122223333",
"sharedEventID": "ce9ee550-df43-45a8-9445-EXAMPLE",
"eventCategory": "Data"
}
```

- [ExecuteQuery](../apiref/API_ExecuteQuery.md "../apiref/API_ExecuteQuery.md")

```
{
"eventVersion": "1.09",
"userIdentity": {
    "type": "AssumedRole",
    "principalId": "AKIAIOSFODNN7EXAMPLE:bob",
    "arn": "arn:aws:sts::111122223333:assumed-role/users/bob",
    "accountId": "111122223333",
    "sessionContext": {
        "sessionIssuer": {
            "type": "Role",
            "principalId": "AKIAI44QH8DHBEXAMPLE",
            "arn": "arn:aws:iam::111122223333:role/admin-role",
            "accountId": "111122223333",
            "userName": "bob"
        },
        "attributes": {
            "creationDate": "2023-11-22T14:04:45Z",
            "mfaAuthenticated": "false"
        }
    }
},
"eventTime": "2023-11-22T14:04:41Z",
"eventSource": "neptune-graph.amazonaws.com",
"eventName": "ExecuteQuery",
"awsRegion": "us-east-1",
"sourceIPAddress": "192.0.2.0",
"userAgent": "aws-cli/1.15.64 Python/2.7.16 Darwin/17.7.0 botocore/1.10.63",
"requestParameters": {
    "requestType": "POST",
    "requestPayload": "[Redacted]",
    "requestContentType": "application/x-www-form-urlencoded",
    "requestHeaders": {
        "X-Amz-Date": "20231122T140445Z",
        "x-triton-proxy-request-id": "9dece4eb-7018-429f-970f-EXAMPLE",
        "Connection": "Keep-Alive",
        "User-Agent": "aws-cli/1.15.64 Python/2.7.16 Darwin/17.7.0 botocore/1.10.63",
        "X-Forwarded-For": "192.0.2.0",
        "content-type": "application/x-www-form-urlencoded",
        "Host": "g-dbiexample.neptune-graph-gamma.us-east-1.amazonaws.com",
        "Accept-Encoding": "gzip,deflate",
        "Content-Length": "40"
    },
    "authorizedIamActions": []
},
"responseElements": {
    "responseTime": "2023-11-22T14:04:45.348Z",
    "responseCode": 200,
    "responseHeaders": {},
    "responseSize": "0",
    "responseContent": ""
},
"requestID": "37001a17-7d4e-4c34-9f3b-EXAMPLE",
"eventID": "5a6323fe-9ea2-4efe-81f0-EXAMPLE",
"readOnly": false,
"resources": [
    {
        "accountId": "111122223333",
        "type": "AWS::NeptuneGraph::Graph",
        "ARN": "arn:aws:neptune-graph:us-east-1:111122223333:graph/g-dbiexample"
    }
],
"eventType": "AwsApiCall",
"managementEvent": false,
"recipientAccountId": "111122223333",
"eventCategory": "Data"
}
```
