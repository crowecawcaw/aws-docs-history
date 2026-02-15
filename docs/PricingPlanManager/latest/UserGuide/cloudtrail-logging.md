# Logging AWS Flat-Rate Plans Activity Using AWS CloudTrail

AWS Flat-Rate Plans is integrated with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") to record all console actions as events. CloudTrail captures details about each action, including the source IP address, timestamp, and user identity. Each CloudTrail event identifies whether the action was performed by:

- Root user or IAM user credentials
- IAM Identity Center user
- Temporary security credentials (role or federated user)
- Another AWS service
  For flat-rate plans, the `eventSource` is `pricingplanmanager.amazonaws.com`.

## Example CloudTrail Event for CreateSubscription

The following example shows a CloudTrail log entry that demonstrates the action.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE:role-session-name",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/role-session-name",
        "accountId": "111122223333",
        "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/Admin",
                "accountId": "111122223333",
                "userName": "Admin"
            },
            "attributes": {
                "creationDate": "2025-11-20T10:15:30Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-11-20T10:20:45Z",
    "eventSource": "pricingplanmanager.amazonaws.com",
    "eventName": "CreateSubscription",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "203.0.113.12",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "requestParameters": {
        "planName": "CF_FRP",
        "planTier": "PRO",
        "resourceArns": [
            "arn:aws:cloudfront::111122223333:distribution/d111111abcdef8",
            "arn:aws:wafv2:us-east-1:111122223333:global/webacl/CreatedByCloudFront-example/example-id"
         ]
    },
    "responseElements": {
        "Access-Control-Expose-Headers": "ETag",
        "lastModifiedTime": "2025-11-20T14:35:22.512142957Z",
        "ETag": "3",
        "createdTime": "2025-11-20T14:30:00.388318680Z",
        "planName": "CF_FRP",
        "resourceArns": [
            "arn:aws:cloudfront::111122223333:distribution/d111111abcdef8",
            "arn:aws:wafv2:us-east-1:111122223333:global/webacl/CreatedByCloudFront-example/example-id"
         ],
         "planTier": "PRO",
         "arn": "arn:aws:pricingplanmanager::111122223333:subscription:sub_123",
         "status": "SYNC_IN_PROGRESS"
    },
    "requestID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "eventID": "12345678-abcd-ef12-3456-7890abcdef12",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

For more information about CloudTrail, including how to view and manage event logs, see [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

###### Example
