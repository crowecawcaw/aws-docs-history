# RotateKey

These examples show the AWS CloudTrail log entries for the operations that rotate
AWS KMS keys. For information about rotating KMS keys, see [Rotate AWS KMS keys](rotate-keys.md "rotate-keys.md").

The following example shows a CloudTrail log entry for the operation that rotates a symmetric
encryption KMS key on which automatic key rotation is enabled. For information about
enabling automatic rotation, see
[Rotate AWS KMS keys](rotate-keys.md "rotate-keys.md").

For an example of the CloudTrail log entry that records the `EnableKeyRotation`
operation, see [EnableKeyRotation](ct-enablekeyrotation.md "ct-enablekeyrotation.md").

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "accountId": "111122223333",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2025-05-20T20:44:37Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "RotateKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "a24b3967-ddad-417f-9b22-2332b918db06",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    ],
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "rotationType": "AUTOMATIC",
        "keyOrigin": "AWS_KMS",
        "previousKeyMaterialId": "123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0",
        "currentKeyMaterialId": "96083e4fb6dbc41d77578a213a6b6669c044dd4c143e96755396d2bf11fd6068",
        "keyId": "1234abcd-12ab-34cd-56ef-1234567890ab"
    },
    "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry for an on-demand rotation initiated by the
[RotateKeyOnDemand](../APIReference/API_RotateKeyOnDemand.md "../APIReference/API_RotateKeyOnDemand.md") operation. For information
about rotating symmetric encryption KMS keys on demand, see
[Perform on-demand key
rotation](rotating-keys-on-demand.md "rotating-keys-on-demand.md").

For an example of the CloudTrail log entry that records the `RotateKeyOnDemand`
operation, see [RotateKeyOnDemand](ct-rotatekeyondemand.md "ct-rotatekeyondemand.md").

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "accountId": "111122223333",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2025-05-20T20:44:37Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "RotateKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "a24b3967-ddad-417f-9b22-2332b918db06",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    ],
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "rotationType": "ON_DEMAND",
        "keyOrigin": "EXTERNAL",
        "previousKeyMaterialId": "123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0",
        "currentKeyMaterialId": "96083e4fb6dbc41d77578a213a6b6669c044dd4c143e96755396d2bf11fd6068",
        "keyId": "1234abcd-12ab-34cd-56ef-1234567890ab"
    },
    "eventCategory": "Management"
}
```
