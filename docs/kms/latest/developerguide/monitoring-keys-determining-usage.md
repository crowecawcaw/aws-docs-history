

# Determine past usage of a KMS key
<a name="monitoring-keys-determining-usage"></a>

For monitoring and auditing purposes, you may want to know how a KMS key has been used in the past. For example, you may want to determine whether a KMS key is still actively used before disabling or scheduling it for deletion, or identify unused keys in your account. The following strategies can help you determine the past usage of a KMS key.

**Warning**  
These strategies for determining past usage are effective only for AWS principals and AWS KMS operations. They cannot detect use of the key that does not involve API calls to AWS KMS. After a data key is generated from a symmetric KMS key, its subsequent use for local encryption or decryption outside of AWS KMS is not reflected in the last usage information. Similarly, these strategies cannot detect the use of the public key of an asymmetric KMS key outside of AWS KMS. For details about the special risks of deleting asymmetric KMS keys used for public key cryptography, including creating ciphertexts that cannot be decrypted, see [Deleting asymmetric KMS keys](deleting-keys.md#deleting-asymmetric-cmks).

**Topics**
+ [Examine KMS key permissions to determine the scope of potential usage](#monitoring-keys-usage-key-permissions)
+ [Examine the last cryptographic operation performed with a KMS key](#examine-last-usage)
+ [Examine AWS CloudTrail logs to check past usage](#deleting-keys-usage-cloudtrail)

## Examine KMS key permissions to determine the scope of potential usage
<a name="monitoring-keys-usage-key-permissions"></a>

Determining who or what currently has access to a KMS key can help you determine how widely the KMS key is in use and whether it is still needed. To determine who or what currently has access to a KMS key, see [Determining access to AWS KMS keys](determining-access.md).

## Examine the last cryptographic operation performed with a KMS key
<a name="examine-last-usage"></a>

AWS KMS provides usage information on the last successful cryptographic operation performed with each KMS key along with the associated CloudTrail event ID. This can ease the process of identifying unused KMS keys. You can also use the [kms:TrailingDaysWithoutKeyUsage](conditions-kms.md#conditions-kms-trailing-days-without-key-usage) condition key in key policies to prevent recently used keys from accidental disablement or scheduling for deletion.

You can view the last successful cryptographic operation performed with a KMS key using the AWS Management Console, AWS CLI, or AWS KMS API.

**Note**  
Certain AWS services create resources that depend on a KMS key for data protection but do not invoke cryptographic operations on that key frequently. For example, the Amazon EC2 service calls AWS KMS to decrypt the data key for an encrypted Amazon EBS volume only when the volume is attached to an instance. In these cases, you must not rely on the last usage information alone to determine if a KMS key can be deleted. If the KMS key protecting an Amazon EBS volume is deleted, there will be no disruption to the Amazon EBS volume that's already attached, but subsequent attempts to attach that encrypted Amazon EBS volume to another Amazon EC2 instance would fail.

### Understanding the usage tracking period
<a name="understanding-tracking-period"></a>

AWS KMS tracks only the last successful cryptographic operation performed with each KMS key. There may be a delay of up to one hour between the time a cryptographic operation occurs and the time that usage is recorded.

When you check the last usage information for a KMS key, the response includes a tracking start date. The `TrackingStartDate` is the date from which AWS KMS began recording cryptographic activity for that key. Use this date together with the key's creation date to determine its usage history by comparing the key's creation date with the tracking start date:
+ If last usage information is **present**, the key has been used for a cryptographic operation since tracking began. The response includes the operation type, timestamp, and associated AWS CloudTrail event ID.
+ If last usage information is **empty**, the key has no recorded cryptographic operations since tracking began. Compare the key's creation date with the `TrackingStartDate` to determine what this means:
  + If the key was created *on or after* the `TrackingStartDate` , the key has not been used for a cryptographic operation since it was created.
  + If the key was created *before* the `TrackingStartDate`, there is no record of the key being used since tracking began. However, the key may have been used before tracking began. To determine whether the key was used before, examine your past AWS CloudTrail logs.

**Warning**  
Do not solely rely on last usage information when deleting unused keys. Instead, [disable the key](enabling-keys.md) first and monitor AWS CloudTrail for `DisabledException` entries, which indicate attempts to use the key while disabled. This helps identify potential dependencies and workload failures. AWS CloudTrail remains the authoritative source for all API calls made to your key.

### Tracked cryptographic operations
<a name="tracked-crypto-operations"></a>

Only the following successful cryptographic operations are tracked and recorded for reporting the last usage information. Non-cryptographic operations are excluded.
+ `Decrypt`
+ `DeriveSharedSecret`
+ `Encrypt`
+ `GenerateDataKey`
+ `GenerateDataKeyPair`
+ `GenerateDataKeyPairWithoutPlaintext`
+ `GenerateDataKeyWithoutPlaintext`
+ `GenerateMac`
+ `ReEncrypt`
+ `Sign`
+ `Verify`
+ `VerifyMac`

### Other considerations
<a name="last-usage-considerations"></a>

Keep the following in mind when you use the usage information:
+ **Multi-Region KMS keys** — For multi-Region KMS keys, primary and replica keys track last usage information independently. Each key in a multi-Region key set maintains its own last usage information.
+ **ReEncrypt operations** — The `ReEncrypt` operation uses two keys: a source key for decryption and a destination key for encryption. Last usage information is recorded for both keys independently, each with the CloudTrail event ID from the respective key owner's account.

You can view the last usage information using the following methods:

### Using AWS KMS console
<a name="key-last-usage-using-console"></a>

You can view the last successful cryptographic operation performed with a KMS key on the details page for each KMS key. For procedures on how to view the details page for a KMS key, see [Access and list KMS key details](finding-keys.md).

### Using AWS KMS API
<a name="key-last-usage-using-api"></a>

The [GetKeyLastUsage](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyLastUsage.html) operation returns usage information on the last cryptographic operation performed with the specified KMS key. To identify the KMS key, use the [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) or [key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN).

For example, the following call to `GetKeyLastUsage` retrieves usage information about a KMS key with the key ID {{1234abcd-12ab-34cd-56ef-1234567890ab}}.

```
$ aws kms get-key-last-usage --key-id "{{1234abcd-12ab-34cd-56ef-1234567890ab}}"
{
    "KeyCreationDate": 1773253425.56,
    "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "TrackingStartDate": 1773253425.56,
    "KeyLastUsage": {
        "Timestamp": 1773253497.0,
        "Operation": "Encrypt",
        "KmsRequestId": "040cce3e-9ef3-4651-b8cf-e47c9bafdc9b",
        "CloudTrailEventId": "2cfd5892-ea8c-4342-ad49-4b9594b06a8b"
    }
}
```

In contrast, the following call to `GetKeyLastUsage` reveals no usage information for a KMS key with the key ID {{0987dcba-09fe-87dc-65ba-ab0987654321}}.

```
$ aws kms get-key-last-usage --key-id "{{0987dcba-09fe-87dc-65ba-ab0987654321}}"
{
    "KeyCreationDate": 1672531200.0,
    "KeyId": "0987dcba-09fe-87dc-65ba-ab0987654321",
    "TrackingStartDate": 1773253425.56,
    "KeyLastUsage": {}
}
```

## Examine AWS CloudTrail logs to check past usage
<a name="deleting-keys-usage-cloudtrail"></a>

You can use a KMS key's usage history to help you determine whether you have ciphertexts encrypted under a particular KMS key. 

All AWS KMS API activity is recorded in AWS CloudTrail log files. If you have [created a CloudTrail trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) in the region where your KMS key is located, you can examine your CloudTrail log files to view a history of all AWS KMS API activity for a particular KMS key. If you don't have a trail, you can still view recent events in your [CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). For details about how AWS KMS uses CloudTrail, see [Logging AWS KMS API calls with AWS CloudTrail](logging-using-cloudtrail.md).

The following examples show CloudTrail log entries that are generated when a KMS key is used to protect an object stored in Amazon Simple Storage Service (Amazon S3). In this example, the object is uploaded to Amazon S3 using [Protecting data using server-side encryption with KMS keys (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html). When you upload an object to Amazon S3 with SSE-KMS, you specify the KMS key to use for protecting the object. Amazon S3 uses the AWS KMS [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) operation to request a unique data key for the object, and this request event is logged in CloudTrail with an entry similar to the following:

```
{
  "eventVersion": "1.02",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROACKCEVSQ6C2EXAMPLE:example-user",
    "arn": "arn:aws:sts::111122223333:assumed-role/Admins/example-user",
    "accountId": "111122223333",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2015-09-10T23:12:48Z"
      },
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/Admins",
        "accountId": "111122223333",
        "userName": "Admins"
      }
    },
    "invokedBy": "internal.amazonaws.com"
  },
  "eventTime": "2015-09-10T23:58:18Z",
  "eventSource": "kms.amazonaws.com",
  "eventName": "GenerateDataKey",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "internal.amazonaws.com",
  "userAgent": "internal.amazonaws.com",
  "requestParameters": {
    "encryptionContext": {"aws:s3:arn": "arn:aws:s3:::example_bucket/example_object"},
    "keySpec": "AES_256",
    "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
  },
  "responseElements": null,
  "requestID": "cea04450-5817-11e5-85aa-97ce46071236",
  "eventID": "80721262-21a5-49b9-8b63-28740e7ce9c9",
  "readOnly": true,
  "resources": [{
    "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "accountId": "111122223333"
  }],
  "eventType": "AwsApiCall",
  "recipientAccountId": "111122223333"
}
```

When you later download this object from Amazon S3, Amazon S3 sends a `Decrypt` request to AWS KMS to decrypt the object's data key using the specified KMS key. When you do this, your CloudTrail log files include an entry similar to the following:

```
{
  "eventVersion": "1.02",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROACKCEVSQ6C2EXAMPLE:example-user",
    "arn": "arn:aws:sts::111122223333:assumed-role/Admins/example-user",
    "accountId": "111122223333",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2015-09-10T23:12:48Z"
      },
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:role/Admins",
        "accountId": "111122223333",
        "userName": "Admins"
      }
    },
    "invokedBy": "internal.amazonaws.com"
  },
  "eventTime": "2015-09-10T23:58:39Z",
  "eventSource": "kms.amazonaws.com",
  "eventName": "Decrypt",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "internal.amazonaws.com",
  "userAgent": "internal.amazonaws.com",
  "requestParameters": {
    "encryptionContext": {"aws:s3:arn": "arn:aws:s3:::example_bucket/example_object"}},
  "responseElements": null,
  "requestID": "db750745-5817-11e5-93a6-5b87e27d91a0",
  "eventID": "ae551b19-8a09-4cfc-a249-205ddba330e3",
  "readOnly": true,
  "resources": [{
    "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "accountId": "111122223333"
  }],
  "eventType": "AwsApiCall",
  "recipientAccountId": "111122223333"
}
```

By evaluating these log entries, you might be able to determine the past usage of a particular KMS key, and this might help you determine whether or not you want to delete it.

To see more examples of how AWS KMS API activity appears in your CloudTrail log files, go to [Logging AWS KMS API calls with AWS CloudTrail](logging-using-cloudtrail.md). For more information about CloudTrail go to the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

### Cost considerations for CloudTrail queries
<a name="cloudtrail-query-cost-considerations"></a>

When you query CloudTrail logs using Amazon CloudWatch Logs Insights, Amazon CloudWatch Logs Insights charges you based on the amount of data scanned. Large, unbounded queries can result in unexpectedly high costs. To manage costs, scope every query to the narrowest relevant time range. Filter by event name, resource ARN, or principal ID. Before attempting to query, consider [examining the last successful cryptographic operation performed with a KMS key](#examine-last-usage) first to avoid incurring unnecessary query cost. You can also set budget alerts in AWS Budgets to catch unexpected query volume. For more information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/) on the Amazon Web Services website.