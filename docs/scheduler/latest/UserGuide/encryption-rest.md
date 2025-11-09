# Encryption at rest in EventBridge Scheduler

This section describes how Amazon EventBridge Scheduler encrypts and decrypts your data at rest. Data at rest is data stored in EventBridge Scheduler and the service's underlying components.
EventBridge Scheduler integrates with AWS Key Management Service (AWS KMS) to encrypt and decrypt your data using an [AWS KMS key](../../../kms/latest/developerguide/concepts.md#kms_keys "../../../kms/latest/developerguide/concepts.md#kms_keys").
EventBridge Scheduler supports two types of KMS keys: [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk"), and
[customer managed keys](../../../customer managed KMS key.md "../../../customer managed KMS key.md").

###### Note

EventBridge Scheduler only supports using [symmetric](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks") encryption KMS keys.

_AWS owned keys_ are KMS keys that an AWS service owns and manages for use in multiple AWS accounts. Although the AWS owned keys EventBridge Scheduler uses are not stored in your AWS account,
EventBridge Scheduler uses them to protect your data and resources. By default, EventBridge Scheduler encrypts and decrypts all of your data using an AWS owned key. You do not need to manage your
AWS owned key or its access policy. You do not incur any fees when EventBridge Scheduler uses AWS owned keys to protect your data, and their usage does not count as part of your AWS KMS quotas in your account.

_Customer managed keys_ are KMS keys stored in your AWS account that you create, own, and manage. If your specific use case requires that you control and audit the encryption keys that
protect your data on EventBridge Scheduler, you can use a customer managed key. If you choose a customer managed key, you must manage your key policy. Customer managed keys incur a monthly fee and a fee for use in excess of the free tier. Using
a customer managed key also counts as part of your [AWS KMS quota](../../../kms/latest/developerguide/limits.md "../../../kms/latest/developerguide/limits.md"). For more information on pricing, see
[AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

###### Topics

- [Encryption artifacts](#encryption-rest-artifacts "#encryption-rest-artifacts")
- [Managing KMS keys](#key-management "#key-management")
- [CloudTrail event example](#key-management-cloud-trail "#key-management-cloud-trail")

## Encryption artifacts

The following table describes the different types of data that EventBridge Scheduler encrypts at rest, and which type of KMS key it supports for each category.

| Data type                                     | Description                                                                                                                                                                                        | AWS owned key | customer managed key |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | -------------------- |
| Payload (up to 256KB)                         | The data that you specify in the schedule's `TargetInput` parameter when you configure the schedule to be delivered to the target.                                                                 | Supported     | Supported            |
| Identifier and state                          | The unique name and the state (enable, disable) of the schedule.                                                                                                                                   | Supported     | Not supported        |
| Scheduling configuration                      | The scheduling expression, such as the rate or cron expression for recurring schedules, and the timestamp for one-time invocations, as well as the schedule's start date, end date, and time zone. | Supported     | Not supported        |
| Target configuration                          | The target's Amazon Resource Name (ARN), and other target related configuration details.                                                                                                           | Supported     | Not supported        |
| Invocation and failure behavior configuration | Flexible time window configuration, the schedule's retry policy, and the dead-letter queue details used for failed deliveries.                                                                     | Supported     | Not supported        |

EventBridge Scheduler uses your customer managed keys only when encrypting and decrypting the target payload, as described in the previous table. If you choose to use a customer managed key, EventBridge Scheduler encrypts and decrypts the payload twice: once using the default AWS owned key,
and another time using the customer managed key that you specify. For all other data types, EventBridge Scheduler only uses the default AWS owned key to protect your data at rest.

Use the following [Managing KMS keys](#key-management "#key-management") section to learn how you must manage your IAM resources and key policies in order to use a customer managed key with EventBridge Scheduler.

## Managing KMS keys

You can optionally provide a customer managed key to encrypt and decrypt the payload that your schedule delivers to its target. EventBridge Scheduler encrypts and decrypts your payload up to
256KB of data. Using a customer managed key incurs a monthly fee and a fee in excess of the free tier. Using a customer managed key counts as part of your
[AWS KMS quota](../../../kms/latest/developerguide/limits.md "../../../kms/latest/developerguide/limits.md"). For more information on pricing, see
[AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/")

EventBridge Scheduler uses IAM permissions associated with the principal that creates a schedule to encrypt your data. This means you must attach the required AWS KMS related permissions
to the user, or role, that calls the EventBridge Scheduler API. In addition, EventBridge Scheduler uses resource-based policies to decrypt your data. This means that the execution role associated with
your schedule must also have the required AWS KMS related permissions to call the AWS KMS API when decrypting data.

###### Note

EventBridge Scheduler does not support using [grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md")
for temporary permissions.

Use the following section to learn how you can manage your AWS KMS [key policy](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") and
required IAM permissions to use a customer managed key on EventBridge Scheduler.

###### Topics

- [Add IAM permissions](#key-management-iam-permissions "#key-management-iam-permissions")
- [Manage the key policy](#key-management-key-policy "#key-management-key-policy")

### Add IAM permissions

To use a customer managed key, you must add the following permissions to the identity-based IAM principal that creates a schedule, as well as the execution role you
associate with the schedule.

#### Identity-based permissions for customer managed keys

You must add the following AWS KMS actions to the permission policy associated with any principal (users, groups, or roles) that calls the EventBridge Scheduler
API when creating a schedule.

- **`kms:DescribeKey`** – Required in order to validate that the key you provide is a
  [symmetric](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks") encryption KMS key.
- **`kms:GenerateDataKey`** – Required in order to generate the data key that EventBridge Scheduler uses to perform client side encryption.
- **`kms:Decrypt`** – Required decrypt the encrypted data key that EventBridge Scheduler stores together with your encrypted data.

These are in addition to the following actions:

- **`scheduler:*`**
- **`iam:PassRole`** – Required to pass the execution role.

#### Execution role permissions for customer managed keys

You must add the following action to your schedule's execution role permissions policy to provide access to EventBridge Scheduler to call the AWS KMS API when decrypting your data.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowEventBridgeSchedulerToDecryptDataUsingCMKMS",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:123456789012:key/`your-key-id`"
 }
 ]
}`

```

- **`kms:Decrypt`** – Required decrypt the encrypted data key that EventBridge Scheduler stores together with your encrypted data.

If you use the EventBridge Scheduler console to create a new execution role when you create a new schedule, EventBridge Scheduler will automatically attach the required permission to your
execution role. However, if you choose an existing execution role, you must add the required permissions to the role to be able to use your customer managed keys.

### Manage the key policy

When you create a customer managed key using AWS KMS, by default, your key has the following key policy to provide access to your schedules' execution roles.

Optionally, you can limit the scope of your key policy to only provide access to the execution role. You might do this if you want to use your customer managed key only with your EventBridge Scheduler resources. Use the following
[key policy](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") example to limit which EventBridge Scheduler resources can use your key.

## CloudTrail event example

AWS CloudTrail captures all API calls _events_. This includes API calls whenever EventBridge Scheduler uses your customer managed key to decrypt your data. The following example shows a CloudTrail event entry that
demonstrates EventBridge Scheduler using the `kms:Decrypt` action using a customer managed key.

```
{
  "eventVersion": "1.08",
  "userIdentity": {
      "type": "AssumedRole",
      "principalId": "ABCDEABCD1AB12ABABAB0:70abcd123a123a12345a1aa12aa1bc12",
      "arn": "arn:aws:sts::123456789012:assumed-role/`execution-role`/70abcd123a123a12345a1aa12aa1bc12",
      "accountId": "123456789012",
      "accessKeyId": "ABCDEFGHI1JKLMNOP2Q3",
      "sessionContext": {
          "sessionIssuer": {
              "type": "Role",
              "principalId": "ABCDEABCD1AB12ABABAB0",
              "arn": "arn:aws:iam::123456789012:role/`execution-role`",
              "accountId": "123456789012",
              "userName": "`execution-role`"
          },
          "webIdFederationData": {},
          "attributes": {
              "creationDate": "2022-10-31T21:03:15Z",
              "mfaAuthenticated": "false"
          }
      }
    },
    "eventTime": "2022-10-31T21:03:15Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "eu-north-1",
    "sourceIPAddress": "13.50.87.173",
    "userAgent": "aws-sdk-java/2.17.295 Linux/4.14.291-218.527.amzn2.x86_64 OpenJDK_64-Bit_Server_VM/11.0.17+9-LTS Java/11.0.17 kotlin/1.3.72-release-468 (1.3.72) vendor/Amazon.com_Inc. md/internal exec-env/AWS_ECS_FARGATE io/sync http/Apache cfg/retry-mode/standard AwsCrypto/2.4.0",
    "requestParameters": {
        "keyId": "arn:aws:kms:us-west-2:123456789012:key/2321abab-2110-12ab-a123-a2b34c5abc67",
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "encryptionContext": {
            "aws:scheduler:schedule:arn": "arn:aws:scheduler:us-west-2:123456789012:schedule/default/`execution-role`"
        }
    },
    "responseElements": null,
    "requestID": "`request-id`",
    "eventID": "`event-id`",
    "readOnly": true,
    "resources": [
        {
            "accountId": "123456789012",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:123456789012:key/2321abab-2110-12ab-a123-a2b34c5abc67"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management",
    "tlsDetails": {
      "tlsVersion": "TLSv1.3",
      "cipherSuite": "TLS_AES_256_GCM_SHA384",
      "clientProvidedHostHeader": "kms.us-west-2.amazonaws.com"
  }
}
```
