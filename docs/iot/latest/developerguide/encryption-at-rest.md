# Data encryption at rest in AWS IoT Core

By default, all AWS IoT Core data at rest is encrypted using AWS owned keys. AWS IoT Core also supports symmetric customer managed keys
from AWS Key Management Service (AWS KMS). With customer managed keys, you can create, own, and manage the AWS KMS keys in your AWS account. AWS IoT Core
will use your KMS keys to encrypt your data at rest. You have full control over these KMS keys, including creating and maintaining
their key policies. You can also configure IAM policies for the roles that access AWS KMS to control permissions for these keys.

## AWS owned keys

AWS owned keys are a collection of KMS keys that an AWS service owns and manages for use in multiple AWS accounts.
AWS services can use AWS owned keys to protect your data. By default, AWS IoT Core encrypts data at rest using AWS owned keys. These keys are managed by
the service. You can't view, manage, or use AWS owned keys. However, you don't need to take any actions to protect these keys.

For more information about AWS owned keys, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-key "../../../kms/latest/developerguide/concepts.md#aws-owned-key") in the _AWS Key Management Service Developer Guide_.

## Customer managed keys

Customer managed keys are KMS keys in your AWS account that you create, own, and manage. You have full control over these
AWS KMS keys, including creating and maintaining their key policies. You can also configure IAM policies for the roles that access AWS KMS to control permissions for these keys. You can configure AWS IoT Core to use customer
managed KMS keys to encrypt your data.

For more information about customer managed keys, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_.

To opt in to customer managed keys in AWS IoT Core, follow these steps:

###### Topics

- [Step 1: Create a customer managed key](#encryption-at-rest-cmk-create "#encryption-at-rest-cmk-create")
- [Step 2: Create an IAM role to grant AWS IoT Core permissions to use the KMS key](#create-an-iam-role "#create-an-iam-role")
- [Step 3: Opt in to customer managed keys in AWS IoT Core](#opt-in-customer-managed-keys "#opt-in-customer-managed-keys")
- [Step 4: Additional permissions required for AWS IoT Core control plane operations](#cmk-control-plane-permissions "#cmk-control-plane-permissions")
- [Step 5: Managing keys](#understanding-key-health "#understanding-key-health")
- [Step 6: Monitoring key health](#health-status-monitoring "#health-status-monitoring")

### Step 1: Create a customer managed key

You can create a symmetric customer managed key by using the AWS KMS console or the AWS KMS CLI commands. The `keySpec` must be `SYMMETRIC_DEFAULT` and the `keyUsage` must be `ENCRYPT_DECRYPT`.

###### Note

AWS IoT Core only supports AWS KMS keys with `SYMMETRIC_DEFAULT` key spec and `ENCRYPT_DECRYPT` key usage for customer managed keys.

The following is an example AWS CLI command to create a KMS key which can be used with AWS IoT Core for customer managed keys.

```
aws kms create-key --key-spec SYMMETRIC_DEFAULT --key-usage ENCRYPT_DECRYPT --region us-west-2
```

The following is an example output of the command.

```
{
    "KeyMetadata": {
        "AWSAccountId": "111122223333",
        "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "Arn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "CreationDate": "2024-09-19T11:45:23.982000-07:00",
        "Enabled": true,
        "Description": "",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "KeyState": "Enabled",
        "Origin": "AWS_KMS",
        "KeyManager": "CUSTOMER",
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "KeySpec": "SYMMETRIC_DEFAULT",
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ],
        "MultiRegion": false
    }
}
```

For more information, see [Creating a symmetric customer managed key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer Guide_.

#### Key policy

When creating a customer managed key, you can specify a key policy. Key policies control access to your customer managed key. Every customer
managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it. For more information, see [Key policies](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

AWS IoT Core uses an IAM role in your account to access your customer managed key. If you're using a custom key policy, make sure the IAM role created
on this key has the following permissions:

- `kms:DescribeKey`
- `kms:Decrypt`
- `kms:Encrypt`
- `kms:GenerateDataKeyWithoutPlaintext`
- `kms:ReEncryptTo`
- `kms:ReEncryptFrom`

### Step 2: Create an IAM role to grant AWS IoT Core permissions to use the KMS key

For AWS IoT Core to use the KMS key you created to encrypt your data at rest, you also need to create an IAM role in your account, which AWS IoT Core can assume to access the KMS key.

The role must have the following trust policy to allow AWS IoT Core to assume the role.

```
{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Principal": {
            "Service": "iot.amazonaws.com"
        },
        "Action": "sts:AssumeRole",
        "Condition": {
            "StringEquals": {
                "aws:SourceAccount": "111122223333"
            },
            "ArnLike": {
                "aws:SourceArn": "arn:aws:iot:us-west-2:111122223333:*"
            }
        }
    }
}
```

Ensure the IAM policies attached to the IAM role have the following permissions on the KMS key:

- `kms:DescribeKey`
- `kms:Decrypt`
- `kms:Encrypt`
- `kms:GenerateDataKeyWithoutPlaintext`
- `kms:ReEncryptTo`
- `kms:ReEncryptFrom`

The following is an example IAM policy with the required permissions for customer managed keys.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowIoTToAccessKMSResource",
            "Effect": "Allow",
            "Action": [
                "kms:DescribeKey",
                "kms:Decrypt",
                "kms:Encrypt",
                "kms:ReEncryptTo",
                "kms:ReEncryptFrom",
                "kms:GenerateDataKeyWithoutPlaintext"
            ],
            "Resource": [
                "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
            ],
            "Condition": {
                "StringEquals": {
                    "kms:EncryptionContext:aws-crypto-ec:vendor": "iot.amazonaws.com"
                }
            }
        }
    ]
}
```

For more information, see [Create a role to delegate permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _AWS Identity and Access Management User Guide_.

### Step 3: Opt in to customer managed keys in AWS IoT Core

After you complete all the previous steps, run the `update-encryption-configuration` CLI command to opt in using customer managed keys in
AWS IoT Core. When you opt in to customer managed keys, all AWS IoT Core resources in your AWS account will be encrypted using the specified AWS KMS key.

1. To opt in to customer managed keys in AWS IoT Core using AWS CLI, run the `update-encryption-configuration` CLI command.

```
aws iot update-encryption-configuration --encryption-type "CUSTOMER_MANAGED_KMS_KEY" \
--kms-access-role-arn "arn:aws:iam::111122223333:role/myrole" \
--kms-key-arn "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab" --region us-west-2
```

2. To verify customer managed keys in AWS IoT Core using AWS CLI, run the `describe-encryption-configuration` CLI command:

```
aws iot describe-encryption-configuration --region us-west-2
```

If you have enabled customer managed keys in AWS IoT Core, the output can look like the following:

```
{
    "encryptionType": "CUSTOMER_MANAGED_KMS_KEY",
    "kmsKeyArn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "kmsAccessRoleArn": "arn:aws:iam::111122223333:role/myrole",
    "configurationDetails": {
        "configurationStatus": "HEALTHY"
    },
    "lastModifiedDate": "2024-09-26T22:01:02.365000-07:00"
}
```

The `lastModifiedDate` field indicates the date when the encryption configuration was last updated.

If you haven't enabled customer managed keys, the output can look like the following:

```
{
    "encryptionType": "AWS_OWNED_KMS_KEY",
    "lastModifiedDate": "2024-09-26T22:01:02.365000-07:00"
}
```

### Step 4: Additional permissions required for AWS IoT Core control plane operations

After you opt in to customer managed keys, all the AWS IoT Core resources belonging to your AWS account are encrypted with the provided KMS key. All control plane operations now require the caller to have `kms:Decrypt` permissions on the KMS key in addition to the permissions required for the specific operation on the AWS IoT Core resource. If the caller does not have `kms:Decrypt` permission and they make an API call that requires encryption or decryption of data (for example, `GetPolicy`), they will receive an `UnauthorizedException`.

For example, when you call `GetPolicy`, you need both `iot:GetPolicy` and `kms:Decrypt` permissions on your customer managed KMS key for the API call to succeed.

###### Note

When updating IAM users or roles to grant AWS KMS permissions on the key used for your encryption configuration, ensure the KMS key policy
also grants the required permissions to the respective IAM users or roles.

#### AWS KMS permissions for `UpdateEncryptionConfiguration`

The `UpdateEncryptionConfiguration` API call needs the following AWS KMS permissions on the KMS key to be able to opt in to customer managed keys or to modify the key configuration:

- `kms:DescribeKey`
- `kms:Decrypt`
- `kms:Encrypt`
- `kms:GenerateDataKeyWithoutPlaintext`
- `kms:ReEncryptTo`
- `kms:ReEncryptFrom`

#### AWS KMS permissions for all other control plane APIs

Most control plane APIs require `kms:Decrypt` permissions when customer managed keys are enabled. However, certain APIs do not require these additional permissions:

APIs that do not require AWS KMS permissions

The `List*` and `Delete*` APIs do not fall into this bucket. Customers can always invoke any `List*` or `Delete*` control plane API and those API calls would succeed even if the caller does not have `kms:Decrypt` permission. These API calls will succeed even if your customer managed key is unhealthy as `List*` and `Delete*` APIs do not do any decryption.

- **List\* APIs** – All listing operations (for example, `ListThings`, `ListPolicies`, `ListCertificates`)
- **Delete\* APIs** – All deletion operations (for example, `DeleteThing`, `DeletePolicy`, `DeleteCertificate`)

### Step 5: Managing keys

AWS IoT Core runs periodic checks on your customer managed key configuration to ensure encrypt and decrypt operations are not impacted. These health checks run once every minute and verify AWS IoT Core's ability to access and use both the AWS KMS key and the associated IAM role for encrypt and decrypt operations.

HEALTHY

AWS IoT Core can successfully access the AWS KMS key through the specified IAM role and perform encryption/decryption
operations. All components function correctly.

UNHEALTHY

AWS IoT Core can't access or use the AWS KMS key. This prevents new encryption operations and may impact service
functionality. The `errorCode` field indicates whether the issue is with the key or the IAM role.

#### Customer actions that can impact key health

Several customer actions can cause the key health status to change from `HEALTHY` to `UNHEALTHY`:

Key-related actions

- **Deleting an AWS KMS key** – When you schedule a key deletion, it's in a `Pending deletion` status and can't be used
- **Disabling an AWS KMS key** – When you disable a KMS key, it can no longer be used for encrypt / decrypt operations
- **Scheduling key for deletion** – Key becomes unusable when deletion completes
- **Modifying key policy** – Removing necessary permissions for AWS IoT Core access
- **Changing key usage permissions** – Restricting required AWS KMS actions

IAM role-related actions

- **Deleting the IAM role** – AWS IoT Core can't assume the role to access the key
- **Modifying role permissions** – Removing required AWS KMS permissions from the role policy
- **Changing trust policy** – Preventing AWS IoT Core service from assuming the role
- **Adding restrictive conditions** – Conditions that prevent AWS IoT Core from using the role

Account-level actions

- **Cross-account key access changes** – Modifying permissions for keys in different accounts
- **Service Control Policies (SCPs)** – Organization-level policies that restrict AWS KMS access
- **Account-level IAM policies** – Policies that override or conflict with key access

###### Important

Any changes to AWS KMS keys, IAM roles, or policies used by AWS IoT Core should be tested in development environments
first. Monitor the key health status closely after making any changes to ensure AWS IoT Core functionality is not impacted.

#### Updating encryption configuration

Update your encryption configuration in AWS IoT Core to change from one customer
managed key to another, or between AWS owned keys and customer managed keys.

To change the configuration to a different customer managed key:

1. Create a new customer managed key following the steps in [Step 1: Create a customer managed key](#encryption-at-rest-cmk-create "#encryption-at-rest-cmk-create").
2. Update your IAM role policy to include permissions for both the old and new keys during the update period.
3. Update your encryption configuration to use the new key:

```
aws iot update-encryption-configuration --encryption-type "CUSTOMER_MANAGED_KMS_KEY" \
--kms-access-role-arn "arn:aws:iam::111122223333:role/myrole" \
--kms-key-arn "arn:aws:kms:us-west-2:111122223333:key/new-key-id"
```

To change the configuration from customer managed keys back to AWS owned keys:

```
aws iot update-encryption-configuration --encryption-type "AWS_OWNED_KMS_KEY"
```

###### Note

When updating the encryption configuration for new customer managed keys, ensure both the old and new keys remain accessible for the operation to succeed.

##### Common failure scenarios and impacts

The following table describes common failure scenarios when keys are deleted or deactivated:

| Scenario                         | Immediate Impact                                                                             | Long-term Consequences                                      |
| -------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Key disabled                     | All new encryption/decryption operations fail immediately                                    | Service disruption until the key is re-enabled or replaced  |
| Key scheduled for deletion       | Key status is changed to pending deletion and all encryption/decryption operations will fail | Automatic service failure when deletion completes           |
| Key permanently deleted          | Immediate and permanent failure of all operations                                            | Permanent data loss and inability to recover encrypted data |
| Key policy modified incorrectly  | AWS IoT Core loses access permissions to the key                                             | Service failures until policy is corrected                  |
| IAM role deleted                 | AWS IoT Core can't assume role to access key                                                 | Complete encryption service failure                         |
| IAM role is modified incorrectly | AWS IoT Core can't assume role or use role to access key                                     | Service failures until IAM role is corrected                |

##### Prevention and best practices

To prevent accidental key deletion or deactivation and minimize the risk of service failures:

Implement key lifecycle policies

Establish clear procedures for key creation, rotation, and retirement. Document which keys are used by
which AWS IoT Core resources and maintain an inventory of active keys.

Use IAM policies to restrict key deletion

Create IAM policies that prevent unauthorized users from deleting or disabling critical encryption keys.
Use conditions to require additional approval for key deletion operations.

Enable CloudTrail logging

Monitor all AWS KMS key operations through CloudTrail to detect unauthorized or accidental key management activities.
Set up alerts for key deletion, disabling, or policy changes.

Test key replacement procedures

Regularly test your key replacement procedures in non-production environments to ensure
you can quickly recover from key-related failures.

Maintain key backups

While you can't export AWS KMS key material, maintain detailed records of key ARNs, policies, and
associated AWS IoT Core configurations to facilitate rapid key replacement if needed.

Monitor key health

Continuously monitor the `CMK.Health` metric and set up automated alerts for key health
status changes. Implement automated responses to quickly address key-related issues.

###### Important

Always test key update procedures in development environments before implementing them in
production. Have a documented rollback plan and ensure that key replacement procedures can be executed quickly
in case of emergencies.

### Step 6: Monitoring key health

As part of the periodic checks AWS IoT Core runs, CloudWatch metrics and logs are emitted to provide visibility on the health status of your customer managed key configuration

AWS IoT Core emits the `CMK.Health` metric to CloudWatch at least once every minute. The metric provides information about the health status of the customer managed keys used by AWS IoT Core for encrypting and decrypting your data.

The `CMK.Health` metric can have the following values:

- The value is `1`: AWS IoT Core is able to use the encryption keys successfully for encrypting and decrypting your data.
- The value is `0`: AWS IoT Core is unable to use the encryption keys for encrypting and decrypting your data.

AWS IoT Core also emits AWS IoT V2 logs when the health status of the encryption keys changes. These logs provide additional details about the health status
update. To view these logs, you must enable AWS IoT V2 logs. The `HEALTHY` logs are emitted at `INFO` level, and the `UNHEALTHY`
logs are emitted at `ERROR` level. For more information about the log levels, see [Log levels](configure-logging.md#log-level "configure-logging.md#log-level").

The following examples are CloudWatch log entries emitted by AWS IoT Core to indicate the health status update of the customer managed keys.

To effectively monitor and respond to key health status changes:

1. **Set up CloudWatch alarms** for the `CMK.Health` metric:

```
aws cloudwatch put-metric-alarm --region us-west-2 \
  --alarm-name "IoTCore-CMK-Health-Alert" \
  --alarm-description "Alert when IoT Core CMK health is unhealthy" \
  --metric-name "CMK.Health" \
  --namespace "AWS/IoT" \
  --statistic "Minimum" \
  --period 300 \
  --evaluation-periods 1 \
  --threshold 1 \
  --comparison-operator "LessThanThreshold" \
  --alarm-actions "arn:aws:sns:us-west-2:111122223333:iot-alerts"
```

2. **Enable AWS IoT V2 logging** to capture detailed health status change events with error codes and messages.
3. **Check configuration status** for troubleshooting:

```
aws iot describe-encryption-configuration --region us-west-2
```

4. **Investigate UNHEALTHY status** by examining the `errorCode` field:
   - `KMS_KEY_VALIDATION_ERROR` – Issue with the AWS KMS key (disabled, deleted, or policy problems)
   - `ROLE_VALIDATION_ERROR` – Issue with the IAM role (deleted, policy problems, or trust issues)

#### From UNHEALTHY to HEALTHY

When the status of the encryption keys is updated from `UNHEALTHY` to `HEALTHY`, AWS IoT Core will emit an AWS IoT V2 log message in the following format.

```
{
    "timestamp": "2017-08-10 15:37:23.476",
    "logLevel": "INFO",
    "traceId": "8421693b-f4f0-4e4a-9235-0cff8bab897d",
    "accountId": "111122223333",
    "status": "SUCCESS",
    "cmkStatus": "HEALTHY",
    "kmsKeyArn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "kmsAccessRoleArn": "arn:aws:iam::111122223333:role/myrole",
    "eventType": "CmkHealthCheck"
}
```

#### From HEALTHY to UNHEALTHY

When the status of the encryption keys is updated from `HEALTHY` to `UNHEALTHY`, AWS IoT Core will emit an AWS IoT V2 log message in the following format.

```
{
    "timestamp": "2017-08-10 15:37:23.476",
    "logLevel": "ERROR",
    "traceId": "8421693b-f4f0-4e4a-9235-0cff8bab897d",
    "accountId": "111122223333",
    "status": "FAILURE",
    "cmkStatus": "UNHEALTHY",
    "errorCode": "KMS_KEY_VALIDATION_ERROR / ROLE_VALIDATION_ERROR",
    "errorMessage": "Error message on why there was a failure",
    "kmsKeyArn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "kmsAccessRoleArn": "arn:aws:iam::111122223333:role/myrole",
    "eventType": "CmkHealthCheck"
}
```

###### Warning

When key health becomes `UNHEALTHY`, AWS IoT Core operations fail immediately. If this occurs, review your key configurations, IAM role
permissions, and policies. Monitor the `CMK.Health` metric for status changes. If operations continue to fail after reviewing your
configurations, contact your account manager or the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") for additional assistance.

#### AWS CloudTrail events

You can also monitor AWS IoT Core's usage of the KMS key for encrypt decrypt operations. AWS IoT Core will make `DescribeKey`, `Decrypt`, `ReEncrypt`, and `GenerateDataKeyWithoutPlaintext` operations on your KMS key to encrypt / decrypt data belonging to your AWS account stored at rest.

There are CloudTrail events for `DescribeKey`, `Decrypt`, `ReEncrypt`, and `GenerateDataKeyWithoutPlaintext`. These events monitor AWS KMS operations called by AWS IoT Core to access data encrypted by your customer managed key.

##### `Decrypt` example

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
        "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
        "accountId": "111122223333",
        "accessKeyId": "*********************",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAIGDTESTANDEXAMPLE:Sampleuser01",
                "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Sampleuser01",
                "accountId": "111122223333",
                "userName": "*****"
            },
            "attributes": {
                "creationDate": "2024-09-16T20:23:39Z",
                "mfaAuthenticated": "false"
            }
        },
        "invokedBy": "iot.amazonaws.com"
    },
    "eventTime": "2024-09-16T20:32:48Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "iot.amazonaws.com",
    "userAgent": "iot.amazonaws.com",
    "requestParameters": {
        "encryptionContext": {
            "kms-arn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
            "aws-crypto-ec:vendor": "iot.amazonaws.com",
            "branch-key-id": "111122223333",
            "type": "branch:ACTIVE"
        },
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    },
    "responseElements": null,
    "requestID": "1afb6d98-8388-455d-8b48-e62c9e0cf7f4",
    "eventID": "b59a5f16-0d98-46d8-a590-0e040a48b39b",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}

```
