# Track privileged tasks in

AWS CloudTrail

The AWS Organizations management account or a delegated administrator account for IAM can perform
some root user tasks on member accounts using short-term root access. Short-term privileged
sessions give you temporary credentials that you can scope to [take privileged actions](id_root-user-privileged-task.md "id_root-user-privileged-task.md") on a member
account in your organization. You can use the following steps to identify the actions taken
by the management account or a delegated administrator during the [`sts:AssumeRoot`](../../../STS/latest/APIReference/API_AssumeRoot.md "../../../STS/latest/APIReference/API_AssumeRoot.md") session.

###### Note

The global endpoint is not supported for `sts:AssumeRoot`. CloudTrail records
`ConsoleLogin` events in the Region specified for the endpoint.

###### To track actions performed by a privileged session in CloudTrail logs

1. Find the `AssumeRoot` event in your CloudTrail logs. This event is generated
   when your management account or the delegated administrator for IAM gets a set of
   short term credentials from `sts:AssumeRoot`.

In the following example, the CloudTrail event for AssumeRoot is logged in the
`eventName` field.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE:JohnRole1",
        "arn": "arn:aws:sts::111111111111:assumed-role/John/JohnRole1",
        "accountId": "111111111111",
        "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::111111111111:role/John",
                "accountId": "111111111111",
                "userName": "Admin2"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2024-10-25T20:45:28Z",
                "mfaAuthenticated": "false"
            },
            "**assumedRoot**": "**true**"
        }
    },
    "eventTime": "2024-10-25T20:52:11Z",
    "eventSource": "sts.amazonaws.com",
    "**eventName**": "**AssumeRoot**",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.1",
    "requestParameters": {
        "targetPrincipal": "222222222222",
        "taskPolicyArn": {
            "arn": "arn:aws:iam::aws:policy/root-task/S3UnlockBucketPolicy"
        }
    },
    "responseElements": {
        "credentials": {
            "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
            "sessionToken": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "expiration": "Oct 25, 2024, 9:07:11 PM"
        }
    }
}
```

For steps to access your CloudTrail logs, see [Getting and
viewing your CloudTrail log files](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the
_AWS CloudTrail User Guide_. 2. In the CloudTrail event log, locate the `targetPrincipal` that specifies the
member account actions were taken on, and the `accessKeyId` that is
unique to the `AssumeRoot` session.

In the following example, the `targetPrincipal` is 222222222222 and the
`accessKeyId` is ASIAIOSFODNN7EXAMPLE.

```
"eventTime": "2024-10-25T20:52:11Z",
    "eventSource": "sts.amazonaws.com",
    "eventName": "AssumeRoot",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.1",
    "requestParameters": {
        "**targetPrincipal**": "`222222222222`",
        "taskPolicyArn": {
            "arn": "arn:aws:iam::aws:policy/root-task/S3UnlockBucketPolicy"
        }
    },
    "responseElements": {
        "credentials": {
            "**accessKeyId**": "`ASIAIOSFODNN7EXAMPLE`",
            "sessionToken": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "expiration": "Oct 25, 2024, 9:07:11 PM"
    }
}
```

3. In the CloudTrail logs for the target principal, search for the access key ID that
   corresponds to the `accessKeyId` value from the `AssumeRoot`
   event. Use the `eventName` field values to determine the privileged tasks
   performed during the `AssumeRoot` session. There may be multiple
   privileged tasks performed in a single session. The maximum session duration for
   `AssumeRoot` is 900 seconds (15 minutes).

In the following example, the management account or delegated administrator
deleted the resource-based policy for an Amazon S3 bucket.

```
{
    "eventVersion": "1.10",
    "userIdentity": {
        "type": "Root",
        "principalId": "`222222222222`",
        "arn": "arn:aws:iam::222222222222:root",
        "accountId": "222222222222",
        "accessKeyId": "`ASIAIOSFODNN7EXAMPLE`",
        "sessionContext": {
            "attributes": {
                "creationDate": "2024-10-25T20:52:11Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2024-10-25T20:53:47Z",
    "eventSource": "s3.amazonaws.com",
    "**eventName**": "**DeleteBucketPolicy**",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.1",
    "requestParameters": {
        "bucketName": "resource-policy-John",
        "Host": "resource-policy-John.s3.amazonaws.com",
        "policy": ""
    },
    "responseElements": null,
    "requestID": "1234567890abcdef0",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "readOnly": false,
    "resources": [
        {
            "accountId": "222222222222",
            "type": "AWS::S3::Bucket",
            "ARN": "arn:aws:s3:::resource-policy-John"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "222222222222",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "resource-policy-John.s3.amazonaws.com"
    }
}
```
