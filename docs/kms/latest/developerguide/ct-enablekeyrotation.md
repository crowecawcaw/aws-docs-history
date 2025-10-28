# EnableKeyRotation

The following example shows an AWS CloudTrail log entry of a call to the [EnableKeyRotation](../APIReference/API_EnableKeyRotation.md "../APIReference/API_EnableKeyRotation.md") operation. For
an example of the CloudTrail log entry that is written when the key is rotated, see [RotateKey](ct-rotatekey.md "ct-rotatekey.md"). For information about rotating
AWS KMS keys, see [Rotate AWS KMS keys](rotate-keys.md "rotate-keys.md").

###### Note

The [rotation-period](rotate-keys.md#rotation-period "rotate-keys.md#rotation-period") is an optional request parameter. If you do not
specify a rotation period when you enable automatic key rotation, the default
value is 365 days.

CloudTrail log entries for this operation recorded on or after December 2022 include the key ARN of the affected KMS key in the `responseElements.keyId` value, even though this operation does not return the key ARN.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::111122223333:user/Alice",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "userName": "Alice"
    },
    "eventTime": "2020-07-25T23:41:56Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "EnableKeyRotation",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "keyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "rotationPeriodInDays": 180
    },
    "responseElements": {
        "keyId":"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    },
    "requestID": "81f5b794-452b-4d6a-932b-68c188165273",
    "eventID": "fefc43a7-8e06-419f-bcab-b3bf18d6a401",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    ],
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```
