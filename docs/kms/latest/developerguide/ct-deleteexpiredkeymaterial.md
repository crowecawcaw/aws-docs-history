# DeleteExpiredKeyMaterial

When you import key material into an AWS KMS key (KMS key), you can set an expiration date and
time for that key material. AWS KMS records an entry in your CloudTrail log when you [import the key material](ct-importkeymaterial.md "ct-importkeymaterial.md") (with the expiration
settings) and when AWS KMS deletes the expired key material. For information about creating
KMS key with imported key material, see [Importing key material for AWS KMS keys](importing-keys.md "importing-keys.md").

The following example shows an AWS CloudTrail log entry generated when AWS KMS deletes the expired
key material.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "accountId": "111122223333",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2025-05-22T19:55:11Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "DeleteExpiredKeyMaterial",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "cfa932fd-0d3a-4a76-a8b8-616863a2b547",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    ],
    "eventType": "AwsServiceEvent",
    "recipientAccountId": "111122223333",
    "serviceEventDetails": {
        "keyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "keyMaterialId": "123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0"
    },
    "eventCategory": "Management"
}
```
