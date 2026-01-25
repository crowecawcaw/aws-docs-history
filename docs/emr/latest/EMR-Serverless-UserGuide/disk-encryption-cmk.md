# Disk Encryption with KMS CMK

EMR Serverless encrypts all disks attached to workers by default using service-owned encryption keys. You can optionally choose to encrypt these disks using your own AWS KMS customer managed keys (CMKs). This provides you with more control over your encryption keys, including the ability to establish and maintain key policies, and audit key usage.

You can configure disk encryption either when creating an application or when submitting individual jobs. When enabled at the application level, all jobs on that application inherit the encryption settings. You can also override the application's default by specifying a disk encryption configuration when submitting a job.

###### Note

EMR Serverless disk encryption only supports symmetric KMS keys. Asymmetric KMS keys are not supported. You must use a symmetric encryption KMS key that was created in AWS KMS. For more information on AWS KMS, see [What is AWS KMS?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")

## Using Encryption Context

Optionally, EMR Serverless uses encryption context to provide additional authenticated data for encryption operations. The encryption context is a set of key-value pairs that can contain non-secret additional authenticated data. The encryption context is cryptographically bound to the encrypted data, so the same encryption context is required to decrypt the data.

In EMR Serverless, you can specify the custom encryption context when configuring disk encryption. This encryption context is included in AWS CloudTrail logs to help you identify and understand your KMS operations.

###### Note

Do not store sensitive information in encryption context as it appears in plaintext in AWS CloudTrail logs.

## Configuring Disk Encryption with Customer Managed Keys

### CreateApplication

To encrypt disks with your own KMS key, include the `diskEncryptionConfiguration` parameter when creating an EMR Serverless application.

```
aws emr-serverless create-application \
  --type TYPE \
  --name APPLICATION_ID \
  --release-label RELEASE_LABEL \
  --region AWS_REGION \
  --disk-encryption-configuration '{
        "encryptionKeyArn": "key-arn",
        "encryptionContext": {
            "key": "value"
        }
  }'
```

### UpdateApplication

To update the KMS key ARN and/or encryption context, specify the `diskEncryptionConfiguration` parameter with the new values when updating an application.

```
aws emr-serverless update-application \
  --name APPLICATION_ID \
  --region AWS_REGION \
  --disk-encryption-configuration '{
        "encryptionKeyArn": "key-arn",
        "encryptionContext": {
            "key": "value"
        }
  }'
```

###### Note

To unset configured disk encryption on an application, pass an empty `diskEncryptionConfiguration` during update application.

### StartJobRun

To encrypt disks with your own KMS key, use the `diskEncryptionConfiguration` configuration when you submit a job run.

```
--configuration-overrides '{
        "diskEncryptionConfiguration": {
            "encryptionKeyArn": "key-arn",
            "encryptionContext": {
                "key": "value"
            }
        }
    }'
```

### Public Livy endpoints

To encrypt disks with your own KMS key when creating Spark sessions through public Livy endpoints, specify the encryption configuration in the session's `conf` object.

```
data = {
    "kind": "pyspark",
    "heartbeatTimeoutInSecond": 60,
    "conf": {
        "emr-serverless.session.executionRoleArn": "role_arn",
        "spark.emr-serverless.disk.encryptionKeyArn": "key-arn",
        "spark.emr-serverless.disk.encryptionContext": "key1:value1,key2:value2"  # Optional
    }
}

# Send request to create a session with the Livy API endpoint
request = AWSRequest(method='POST', url=endpoint + "/sessions", data=json.dumps(data), headers=headers)
```

## Required permissions for disk encryption

### Encryption key permissions for EMR Serverless

When you encrypt disks with your own encryption key, you must configure the following KMS key permissions for the `emr-serverless.amazonaws.com` principal:

- `kms:GenerateDataKey` : To generate data keys for encrypting disk volumes
- `kms:Decrypt` : To decrypt data keys when accessing encrypted disk contents

```
{
    "Effect": "Allow",
    "Principal":{
        "Service": "emr-serverless.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringLike": {
            "aws:SourceArn": "arn:aws:emr-serverless:region:aws-account-id:/applications/application-id"
        },
        "StringEquals": {
            "kms:EncryptionContext:applicationId": "application-id",
            "aws:SourceAccount": "aws-account-id"
        }
    }
}
```

As a security best practice, we recommend that you add an `aws:SourceArn` condition key to the KMS key policy. The IAM global condition key `aws:SourceArn` helps ensure that EMR Serverless uses the KMS key only for an application ARN. Additionally, including the `aws:SourceAccount` condition key provides another layer of security by restricting the use of your KMS key to requests originating from the AWS account ID specified in the condition.

The job runtime role must have the following permissions in its IAM policy:

```
{
    "Sid": "Enable GDK and Decrypt",
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": [
            "kms:GenerateDataKey",
            "kms:Decrypt"
        ],
        "Resource": "key-arn"
    }
}
```

### Required user permissions

The user who submits the job must have permissions to use the key. You can specify the permissions in either the KMS key policy or the IAM policy for the user, group, or role. If the user who submits the job lacks the KMS key permissions, EMR Serverless rejects the job run submission.

#### Example key policy

The following key policy provides the permissions to `kms:DescribeKey`, `kms:GenerateDataKey` and `kms:Decrypt`:

- `kms:DescribeKey` : To verify that the customer managed KMS key is enabled and SYMMETRIC before using it.

```
{
    "Sid": "Enable DescribeKey",
    "Effect": "Allow",
    "Principal":{
        "AWS": "arn:aws:iam::111122223333:user/user-name"
    },
    "Action": [
        "kms:DescribeKey"
    ],
    "Resource": "*"
},
{
    "Sid": "Enable GDK and Decrypt",
    "Effect": "Allow",
    "Principal":{
        "AWS": "arn:aws:iam::111122223333:user/user-name"
    },
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "emr-serverless.region.amazonaws.com",
            "kms:EncryptionContext:key": "value"
        }
    }
}
```

As a security best practice, we recommend that you add an `kms:viaService` condition key to the KMS key policy. It limits use of the KMS key to validation requests from just emr-serverless.

#### Example IAM policy

The following IAM policy provides the permissions to `kms:DescribeKey`, `kms:GenerateDataKey` and `kms:Decrypt`.

```
{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": [
            "kms:DescribeKey",
            "kms:GenerateDataKey",
            "kms:Decrypt"
        ],
        "Resource": "key-arn"
    }
}
```

## Monitoring Key Usage

You can monitor the use of your customer managed keys in EMR Serverless through AWS CloudTrail. AWS CloudTrail captures all API calls to AWS KMS as events, including calls from the EMR Serverless console, EMR Serverless API, AWS CLI, or AWS SDK.

The information captured includes the encryption context you specified, which can help you identify and audit the specific EMR Serverless resources that used your KMS key. For example, you might see events similar to the following in AWS CloudTrail. For more information about using AWS CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

### GenerateDataKey

Sample event for GenerateDataKey operations when EMR Serverless is creating encrypted disk volumes

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AWSService",
        "principalId": "user",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2025-07-28T21:43:51Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "ipAddress",
    "userAgent": "userAgent",
    "requestParameters": {
        "encryptionContext": {
            "applicationId": "test"
        },
        "keyId": "arn:aws:kms:region:accountId:key/ffffffff-fffff-aaaaa-eeee-sample",
        "keySpec": "AES_256"
    },
    "responseElements": null,
    "additionalEventData": {
        "keyMaterialId": "145c963debe558dfb01848d2a4539da940f3478852f86cfe2f52d5df796a5a02"
    },
    "requestID": "cc9d1c5e-97c4-4a4f-ae7a-e576sample",
    "eventID": "0b0fef09-f28d-4da8-a5a1-17b74sample",
    "readOnly": true,
    "resources": [
        {
            "accountId": "account",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:region:accountId:key/ffffffff-fffff-aaaaa-eeee-sample"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "accountId",
    "eventCategory": "Management"
}
```

### Decrypt

Sample event for Decrypt operations when EMR Serverless is accessing encrypted data.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AWSService",
        "principalId": "user",
        "invokedBy": "AWS Internal"
    },
    "eventTime": "2025-07-28T21:43:51Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "ipAddress",
    "userAgent": "userAgent",
    "requestParameters": {
        "encryptionContext": {
            "applicationId": "test"
        },
        "keyId": "arn:aws:kms:region:accountId:key/ffffffff-fffff-aaaaa-eeee-sample",
        "keySpec": "AES_256"
    },
    "responseElements": null,
    "additionalEventData": {
        "keyMaterialId": "145c963debe558dfb01848d2a4539da940f3478852f86cfe2f52d5df796a5a02"
    },
    "requestID": "cc9d1c5e-97c4-4a4f-ae7a-e576sample",
    "eventID": "0b0fef09-f28d-4da8-a5a1-17b74sample",
    "readOnly": true,
    "resources": [
        {
            "accountId": "account",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:region:accountId:key/ffffffff-fffff-aaaaa-eeee-sample"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "accountId",
    "eventCategory": "Management"
}
```

## Learn More

The following resources provide more information about data encryption at rest.

- For more information about AWS KMS basic concepts, see the [AWS KMS Developer Guide](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").
- For more information about Security best practices for AWS KMS, see the [AWS KMS Developer Guide](../../../kms/latest/developerguide/best-practices.md "../../../kms/latest/developerguide/best-practices.md").
