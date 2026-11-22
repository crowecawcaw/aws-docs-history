

# Encryption at rest

This topic applies only to custom voices. Speech synthesis with the voices that Amazon Polly provides doesn't use the keys described here.

When you create a custom voice with [CreateVoice](https://docs.aws.amazon.com/polly/latest/APIReference/API_CreateVoice.html), Amazon Polly stores the following data:
+ Copies of your recordings, only while Amazon Polly creates the voice. Amazon Polly deletes the copies when creation finishes, whether creation succeeds or fails.
+ Voice data that Amazon Polly derives from the recordings, for the life of the voice.
+ Voice metadata: the name, language, and status of the voice, and the Amazon Simple Storage Service (Amazon S3) URLs of the recordings.

Amazon Polly doesn't store synthesized speech for later retrieval. The encryption settings of the Amazon S3 bucket that you specify for [StartSpeechSynthesisTask](https://docs.aws.amazon.com/polly/latest/APIReference/API_StartSpeechSynthesisTask.html) protect the output of the task.

Amazon Polly always encrypts this data on the server side with AWS Key Management Service (AWS KMS) before it writes the data to storage, and you can't turn this encryption off. Amazon Polly always encrypts the metadata with an AWS owned key. This topic calls the copies of the recordings and the derived data *voice data*. For the voice data, you choose one of the following types of AWS KMS key when you create the voice. You can't change the key later.
+ **AWS owned key (default)** – If you don't specify a key, Amazon Polly uses an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-key). You can't view or manage the key, and there is no charge for its use.
+ **Customer managed key** – To control or audit the key that protects a voice, specify a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-mgn-key). You pay AWS KMS charges for the key and for each request that Amazon Polly makes with it. If the key is in another account, that account pays for the key and your account pays for the requests. These requests count toward the AWS KMS request quotas of your account. For the number of requests, see [How Amazon Polly uses your customer managed key](#encryption-at-rest-key-how). For more information, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing/) and [Request quotas](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html) in the *AWS Key Management Service Developer Guide*.

To find the key that protects a voice, call [GetVoice](https://docs.aws.amazon.com/polly/latest/APIReference/API_GetVoice.html) and check the `CustomerManagedEncryption` field. If the field is missing, the voice uses an AWS owned key. For information about data in transit, see [Encryption in Transit](encryption-in-transit.md).

## How Amazon Polly uses your customer managed key
<a name="encryption-at-rest-key-how"></a>

Amazon Polly uses [envelope encryption](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#enveloping): it encrypts the voice data with a data key that your KMS key protects, and it stores only the encrypted copy of the data key.

Amazon Polly makes the AWS KMS requests with the credentials of the IAM principal that calls Amazon Polly, through [forward access sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html). AWS KMS authorizes each request against the permissions of that principal. Amazon Polly doesn't use grants or a service-linked role, so your key policy needs no service principal for Amazon Polly.

Amazon Polly calls the following AWS KMS operations on your key:
+ `DescribeKey` – At `CreateVoice`, Amazon Polly checks that the key exists, is enabled, and is a symmetric encryption key. If the check fails, `CreateVoice` doesn't create a voice. It returns `AccessDeniedException` if the caller doesn't have `kms:DescribeKey` permission, and `ValidationException` with the `reason` `kmsKeyNotFound` or `kmsKeyUnusable` if the key doesn't exist or Amazon Polly can't use it. Before it calls AWS KMS, `CreateVoice` validates the key ARN and returns `ValidationException` with the `reason` `fieldValidationFailed` if the key is in a different Region.
+ `GenerateDataKey` and `Decrypt` – While Amazon Polly creates the voice, it encrypts and reads the voice data with the credentials of the `CreateVoice` caller. Creating one voice makes tens to hundreds of these requests. The requests continue after `CreateVoice` returns, until the voice status is `active` or `failed`. If AWS KMS denies a request after `CreateVoice` returned, the voice status changes to `failed` and `StatusReason` describes the AWS KMS error.
+ `Decrypt` – Each `SynthesizeSpeech` or `StartSpeechSynthesisStream` request makes one `Decrypt` request with the credentials of the caller. If AWS KMS denies or throttles the request, the operation returns `AccessDeniedException` or `ThrottlingException`. For `StartSpeechSynthesisTask`, Amazon Polly makes the request when the task runs, with the credentials of the principal that started the task. If the request fails, the task fails and `TaskStatusReason` gives the cause.

`GetVoice`, `DescribeVoices`, `DeleteVoice`, `TagResource`, `UntagResource`, and `ListTagsForResource` don't call AWS KMS. They succeed even if the key is disabled or deleted.

Amazon Polly doesn't cache data keys or decrypted voice data. After AWS KMS applies a change to the state or the key policy of the key, the change affects the next request that uses the voice. A speech synthesis stream that is already open continues until it ends.

## Key requirements
<a name="encryption-at-rest-key-requirements"></a>

The key that you specify must meet the following requirements. To create a key, see [Create an AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.
+ It must be a [symmetric encryption KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#symmetric-key-0ps).
+ It must be in the same AWS Region as the voice. It can be in your AWS account or in another AWS account. For a [multi-Region key](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html), specify the key that is in the Region of the voice, whether it is the primary key or a replica key.
+ It must be enabled when you create the voice and whenever you synthesize speech with the voice. See [Disabling or deleting the key of a voice](#encryption-at-rest-key-disabled).
+ You must specify it by its key ARN, for example `arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`. You can't use a key ID, an alias name, or an alias ARN.

## Configuring permissions to use a customer managed key
<a name="encryption-at-rest-key-permissions"></a>

To create a voice, a principal needs `kms:DescribeKey`, `kms:GenerateDataKey`, and `kms:Decrypt` permissions on the key. To synthesize speech with the voice, a principal needs `kms:Decrypt` permission, and it can be a different principal. Both principals also need permissions for the Amazon Polly operations. See [Identity and Access Management in Amazon Polly](security-iam.md).

The following key policy uses two example IAM roles for the principals in your account: `VoiceAdminRole` calls `CreateVoice`, and `SpeechSynthesisRole` calls the speech synthesis operations. The policy gives each role the minimum permissions for its task. Replace the role names, the account ID, and the Region with your own values. The Region appears in each `kms:ViaService` value and in each voice ARN.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Enable IAM User Permissions",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Allow Amazon Polly to check the key when a voice is created",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/VoiceAdminRole"
            },
            "Action": "kms:DescribeKey",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "polly.us-east-1.amazonaws.com"
                }
            }
        },
        {
            "Sid": "Allow Amazon Polly to encrypt and read the data of a new voice",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/VoiceAdminRole"
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "polly.us-east-1.amazonaws.com"
                },
                "ArnLike": {
                    "kms:EncryptionContext:aws:polly:arn": "arn:aws:polly:us-east-1:111122223333:voice/*"
                }
            }
        },
        {
            "Sid": "Allow Amazon Polly to decrypt a voice for speech synthesis",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:role/SpeechSynthesisRole"
            },
            "Action": "kms:Decrypt",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "polly.us-east-1.amazonaws.com"
                },
                "ArnLike": {
                    "kms:EncryptionContext:aws:polly:arn": "arn:aws:polly:us-east-1:111122223333:voice/*"
                }
            }
        }
    ]
}
```

The first statement is the [default statement](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html) that enables IAM policies, which can grant other access to the key, including direct use. The next two statements let the role that creates voices check the key and encrypt and read the data of new voices. The last statement lets the role that synthesizes speech decrypt that data. The `kms:ViaService` condition limits the use of the key to Amazon Polly in the Region, and the encryption context condition limits it to voices in the account. See [Limiting the use of your customer managed key](#encryption-at-rest-key-conditions).

If the key is in another AWS account, the key policy of that key must allow your roles as in this example, and the IAM policies of your roles must allow the same actions on the key ARN. In that key policy, the first statement names the account of the key, and the role ARNs and the voice ARNs name your account. For more information, see [Allowing users in other accounts to use a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html) in the *AWS Key Management Service Developer Guide*.

If the key policy includes the default statement, you can put the last three statements in the IAM policies of the roles instead. Remove the `Principal` element, set `Resource` to the key ARN, and remove the spaces from the `Sid` values, because an IAM policy `Sid` can contain only letters and numbers. With `"Resource": "*"`, the IAM policy applies to every KMS key in the account.

If AWS KMS denies a request that you expected to succeed, see [Troubleshooting AWS KMS permissions](https://docs.aws.amazon.com/kms/latest/developerguide/policy-evaluation.html) in the *AWS Key Management Service Developer Guide*.

**Note**  
If a recording is stored in Amazon S3 with server-side encryption with AWS KMS keys (SSE-KMS), the `CreateVoice` caller also needs `kms:Decrypt` permission on that KMS key, because Amazon Polly reads the recording with the credentials of the caller. Amazon S3 makes that `Decrypt` request, so a `kms:ViaService` condition on that key needs the value `s3.{{region}}.amazonaws.com`.

## Creating a voice with a customer managed key
<a name="encryption-at-rest-key-create"></a>

Specify the key ARN in the `KmsKeyArn` field of the [CustomerManagedEncryption](https://docs.aws.amazon.com/polly/latest/APIReference/API_CustomerManagedEncryption.html) parameter of `CreateVoice`. Optionally, add your own encryption context pairs in the `EncryptionContext` field; the `CustomerManagedEncryption` reference lists their limits. The following AWS CLI command creates a voice with a customer managed key and the pair `project=audiobooks`. Replace the example values with your own.

```
aws polly create-voice \
    --name "{{narrator}}" \
    --language-code en-US \
    --terms-accepted \
    --voice-creation-data '{
        "Recordings": [
            {"Format": "wav", "Data": {"S3Url": "{{s3://amzn-s3-demo-bucket/recordings/narrator-1.wav}}"}}
        ]}' \
    --customer-managed-encryption '{
        "KmsKeyArn": "{{arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab}}",
        "EncryptionContext": {"{{project}}": "{{audiobooks}}"}}'
```

The `CreateVoice` response also includes the `CustomerManagedEncryption` field, with the key ARN and your encryption context pairs. `DescribeVoices` doesn't return this field.

In the Amazon Polly console, you choose the key in the **Encryption** section of the **Create voice** page. The console also needs `kms:ListAliases` and `kms:DescribeKey` permissions. It calls AWS KMS directly, not through Amazon Polly, so a `kms:ViaService` condition doesn't cover these requests. You can add your own encryption context pairs only with the API, the AWS CLI, or an AWS SDK.

## Changing the key of a voice
<a name="encryption-at-rest-key-change"></a>

To protect a voice with a different key, create a new voice from the same recordings with the new key, and then delete the old voice. The new voice has a new ID and ARN, so update your applications to use it. Key rotation in AWS KMS doesn't affect your voices, because AWS KMS keeps the previous key material. See [Rotate AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) in the *AWS Key Management Service Developer Guide*.

## Disabling or deleting the key of a voice
<a name="encryption-at-rest-key-disabled"></a>

If you disable the key of a voice or schedule the key for deletion, the voice status stays `active`, but speech synthesis with the voice fails. `SynthesizeSpeech` and `StartSpeechSynthesisStream` return `ValidationException`, and a speech synthesis task fails with the cause in `TaskStatusReason`. Synthesis works again when you re-enable the key or cancel the deletion. After AWS KMS deletes the key, Amazon Polly can't decrypt the voice data. You can still delete the voice. See [Delete an AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html) in the *AWS Key Management Service Developer Guide*.

## Limiting the use of your customer managed key
<a name="encryption-at-rest-key-conditions"></a>

To limit the use of your key with Amazon Polly, use the following condition keys in your key policy and IAM policies.

### `kms:ViaService`
<a name="encryption-at-rest-key-conditions-viaservice"></a>

The [kms:ViaService](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-via-service) condition key limits the use of the key to requests from Amazon Polly in one Region. The value for Amazon Polly is `polly.{{region}}.amazonaws.com`. Because Amazon Polly uses your credentials, a principal that has permissions without this condition can also use the key directly with AWS KMS. The condition applies to all AWS KMS requests that Amazon Polly makes, including `DescribeKey`.

```json
"StringEquals": {
    "kms:ViaService": "polly.us-east-1.amazonaws.com"
}
```

### Encryption context
<a name="encryption-at-rest-key-conditions-context"></a>

In every `GenerateDataKey` and `Decrypt` request for a voice, Amazon Polly includes the encryption context pair `aws:polly:arn`, whose value is the ARN of the voice, and the pairs that you specified in `CreateVoice`. The [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) also adds an `aws-crypto-public-key` pair.

Use the [kms:EncryptionContext:context-key](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-encryption-context) condition key to restrict which voices can use the key. Any caller can supply an encryption context, so combine this condition with `kms:ViaService`. For example, the following condition limits a statement to one voice.

```json
"StringEquals": {
    "kms:EncryptionContext:aws:polly:arn": "arn:aws:polly:us-east-1:111122223333:voice/vc-9a8fa85dd3"
}
```

The encryption context appears in plaintext in AWS CloudTrail logs, so don't put sensitive information in it. See [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html) in the *AWS Key Management Service Developer Guide*.

## Monitoring the use of your key by Amazon Polly
<a name="encryption-at-rest-key-monitoring"></a>

AWS CloudTrail records every AWS KMS request that Amazon Polly makes on your behalf in your AWS account. If the key is in another AWS account, CloudTrail records the requests in both accounts. The event names are `DescribeKey`, `GenerateDataKey`, and `Decrypt`. In your account, the `userIdentity` element identifies the IAM principal that called Amazon Polly; in the account of a cross-account key, it has the type `AWSService` and doesn't name the principal. The `invokedBy`, `sourceIPAddress`, and `userAgent` fields are `AWS Internal`, and the event doesn't name Amazon Polly. To find the requests for a voice, look for the `aws:polly:arn` pair in the `requestParameters.encryptionContext` element of `GenerateDataKey` and `Decrypt` events. A `DescribeKey` event has no encryption context; match it to a `CreateVoice` request from the same principal at the same time. An event alone doesn't prove that Amazon Polly made the request. See [Finding AWS KMS log entries in CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html#searching-kms-ct) in the *AWS Key Management Service Developer Guide*.

The following example shows the CloudTrail event for the `Decrypt` request that Amazon Polly makes when you call `SynthesizeSpeech` with a custom voice.

```json
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROACKCEVSQ6C2EXAMPLE:my-session",
        "arn": "arn:aws:sts::111122223333:assumed-role/SpeechSynthesisRole/my-session",
        "accountId": "111122223333",
        "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::111122223333:role/SpeechSynthesisRole",
                "accountId": "111122223333",
                "userName": "SpeechSynthesisRole"
            },
            "attributes": {
                "creationDate": "2026-10-30T10:11:18Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2026-10-30T10:11:18Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "AWS Internal",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "keyId": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "encryptionContext": {
            "aws:polly:arn": "arn:aws:polly:us-east-1:111122223333:voice/vc-9a8fa85dd3",
            "project": "audiobooks",
            "aws-crypto-public-key": "A68c/m1sx0Utk0wtiNADhJSNva7FnemYVyVqsnZz0JLYxO0ISPhOYvEwwUswvW5Chw=="
        },
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
    },
    "responseElements": null,
    "additionalEventData": {
        "keyMaterialId": "0a1b2c3d4e5f60718293a4b5c6d7e8f90a1b2c3d4e5f60718293a4b5c6d7e8f9"
    },
    "requestID": "380f7667-fa2d-427c-8061-b99ae7480d5a",
    "eventID": "1cbbbdb3-24cb-359b-8265-a8e8c5fd93d1",
    "readOnly": true,
    "resources": [
        {
            "accountId": "AWS Internal",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "sharedEventID": "d893a79a-ce32-4ad9-ba8a-9170cd92ea59",
    "vpcEndpointId": "AWS Internal",
    "vpcEndpointAccountId": "AWS Internal",
    "eventCategory": "Management"
}
```

The `creationDate` value is the time of the Amazon Polly request, because Amazon Polly creates a new forward access session for each Amazon Polly API request.

For information about how CloudTrail logs Amazon Polly API calls, see [Logging Amazon Polly API calls with AWS CloudTrail](logging-using-cloudtrail.md).