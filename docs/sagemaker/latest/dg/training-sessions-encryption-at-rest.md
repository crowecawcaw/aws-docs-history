

# Encryption at rest for SageMaker AI Training Sessions
<a name="training-sessions-encryption-at-rest"></a>

SageMaker AI Training Sessions encrypts all of your data at rest. Your training and sampling operation request and response data, and your training session checkpoints (including LoRA adapter weights), are stored in Amazon S3 using server-side encryption. You do not need to perform any additional configuration to ensure that your data is encrypted at rest.

## Options for encryption at rest
<a name="training-sessions-encryption-options"></a>

SageMaker AI Training Sessions supports the following encryption options:
+ **Server-side encryption with an AWS owned KMS key** – By default, Training Sessions encrypts your data using an AWS owned KMS key. You do not need to create or manage this key, and no additional configuration is required.
+ **Server-side encryption with a customer managed KMS key (SSE-KMS)** – You can optionally specify a customer managed KMS key to encrypt your training session data in Amazon S3. Choose this option if your security requirements call for control over the key lifecycle, key rotation, or key access auditing.

## Encrypting data at rest using a customer managed AWS KMS key
<a name="training-sessions-cmk"></a>

### How SageMaker AI Training Sessions uses a customer managed KMS key
<a name="training-sessions-cmk-how"></a>

When you specify a customer managed KMS key on a training session, Training Sessions uses that key to encrypt the following data in Amazon S3:
+ Training session checkpoints, including trained model artifacts (LoRA adapter weights).
+ Training and sampling operation request and response data.

When you specify a customer managed key, Training Sessions creates a single grant on the KMS key on your behalf when you create a training session. The grant lets the service call `kms:GenerateDataKey`, `kms:Decrypt`, and `kms:DescribeKey` for that session, and is constrained by an encryption context that binds it to the training session ARN.

Training Sessions retires the grant automatically when the session reaches a terminal state, so the service loses access to the key once the session lifecycle ends. The service does not cache data keys. It retires the grant using the `RetireGrant` privilege carried in the grant itself, so your key policy needs no statement for grant retirement.

During a training session, the following AWS KMS operations occur:
+ `kms:GenerateDataKey` – Called through Amazon S3 when writing encrypted data (checkpoints, model artifacts, and operation data).
+ `kms:Decrypt` – Called through Amazon S3 when reading encrypted data.
+ `kms:DescribeKey` – Called by the caller identity at session creation time to verify the KMS key configuration and state.
+ `kms:CreateGrant` – Called by the caller identity at session creation time to create the session grant described above.

### Configuring a customer managed AWS KMS key
<a name="training-sessions-cmk-configure"></a>

Training Sessions supports symmetric AWS KMS keys only. Multi-region keys are not supported. The key must be in the same AWS account and Region as the training session.

#### Configuring permissions to use a customer managed KMS key
<a name="training-sessions-cmk-permissions"></a>

To use a customer managed KMS key, configure permissions in three places: the IAM execution role, the caller identity IAM policy, and the AWS KMS key policy.

##### Execution role
<a name="training-sessions-cmk-execution-role"></a>

The IAM execution role you pass as `RoleArn` to `CreateTrainingSession` must have the following AWS KMS permissions. These allow the training session to encrypt and decrypt your data through Amazon S3.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "KMSPermissionsForS3Encryption",
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}",
      "Condition": {
        "StringLike": {
          "kms:ViaService": "s3.*.amazonaws.com"
        }
      }
    }
  ]
}
```

The `kms:ViaService` condition (`s3.*.amazonaws.com`) restricts the execution role use of the key to requests that come through Amazon S3. If your bucket is configured with default encryption under a different KMS key, also grant the execution role `kms:GenerateDataKey` and `kms:Decrypt` on that key so it can read and write objects in your bucket.

##### Caller identity
<a name="training-sessions-cmk-caller-identity"></a>

At session creation, and before it processes a training or sampling operation, Training Sessions verifies the caller identity is permitted to use the key. The identity that calls `CreateTrainingSession` and invokes these operations must be allowed the following actions, scoped with a `kms:ViaService` of `sagemaker.*.amazonaws.com`.

```
{
  "Sid": "KMSPermissionsForSessionCreation",
  "Effect": "Allow",
  "Action": [
    "kms:CreateGrant",
    "kms:DescribeKey"
  ],
  "Resource": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}",
  "Condition": {
    "StringLike": {
      "kms:ViaService": "sagemaker.*.amazonaws.com"
    }
  }
}
```

```
{
  "Sid": "KMSPermissionsForTrainingSessionsRuntime",
  "Effect": "Allow",
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}",
  "Condition": {
    "StringLike": {
      "kms:ViaService": "sagemaker.*.amazonaws.com",
      "kms:EncryptionContext:aws:sagemaker:training-session-arn": "arn:aws:sagemaker:{{region}}:{{account-id}}:training-session/*"
    }
  }
}
```

These permission verifications always include the training session ARN in the encryption context, so you can scope this statement with the `kms:EncryptionContext:aws:sagemaker:training-session-arn` condition shown above.

##### Key policy
<a name="training-sessions-cmk-key-policy"></a>

The default KMS key policy already allows IAM roles in the same account to use the key. Add the following statements to your key policy to allow the caller identity — through Training Sessions — to create the session grant and validate the key at `CreateTrainingSession` time. The two statements are separate because `kms:GrantIsForAWSResource` and `kms:GrantOperations` apply only to grant operations, not to `kms:DescribeKey`.

```
{
  "Sid": "AllowDescribeKeyForTrainingSession",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::{{account-id}}:role/{{CallerRole}}"
  },
  "Action": "kms:DescribeKey",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:CallerAccount": "{{account-id}}"
    },
    "StringLike": {
      "kms:ViaService": "sagemaker.*.amazonaws.com"
    }
  }
}
```

```
{
  "Sid": "AllowCreateGrantForTrainingSession",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::{{account-id}}:role/{{CallerRole}}"
  },
  "Action": "kms:CreateGrant",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:CallerAccount": "{{account-id}}"
    },
    "StringLike": {
      "kms:ViaService": "sagemaker.*.amazonaws.com"
    },
    "Bool": {
      "kms:GrantIsForAWSResource": "true"
    },
    "ForAllValues:StringEquals": {
      "kms:GrantOperations": [
        "GenerateDataKey",
        "Decrypt",
        "DescribeKey"
      ]
    }
  }
}
```

If your key policy does not delegate permissions to IAM (a locked-down key policy without the default *Enable IAM User Permissions* statement), also add the following two statements — one so the execution role can perform Amazon S3 SSE-KMS operations, and one so the identity that invokes runtime operations passes the service permission verification:

```
{
  "Sid": "AllowExecutionRoleS3Encryption",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::{{account-id}}:role/{{ExecutionRole}}"
  },
  "Action": [
    "kms:GenerateDataKey",
    "kms:Decrypt"
  ],
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "kms:ViaService": "s3.*.amazonaws.com"
    }
  }
}
```

```
{
  "Sid": "AllowCallerRuntimeAuthorization",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::{{account-id}}:role/{{CallerRole}}"
  },
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "kms:ViaService": "sagemaker.*.amazonaws.com"
    }
  }
}
```

#### Creating a training session with a customer managed KMS key
<a name="training-sessions-cmk-create"></a>

To encrypt your data with a customer managed KMS key, specify the key ARN in the `OutputConfig.S3Location.KmsKeyArn` field of your `CreateTrainingSession` request. `KmsKeyArn` accepts a key ID or key ARN; KMS aliases are not supported. For more information, see [CreateTrainingSession](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingSession.html) in the *SageMaker AI API Reference*.

```
{
  "OutputConfig": {
    "S3Location": {
      "Path": "s3://{{your-bucket}}/output/",
      "KmsKeyArn": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}"
    }
  }
}
```

You cannot change the customer managed key, or switch between an AWS owned key and a customer managed key, after a training session is created. To use a different key, create a new training session with the desired key configuration. Data encrypted under the original key remains encrypted under that key.

#### Scoping down access to the customer managed KMS key
<a name="training-sessions-cmk-scope-down"></a>

You can use the following mechanisms to restrict use of your customer managed KMS key:
+ **Encryption context** – The session grant is created with an encryption context constraint that binds every AWS KMS operation to the training session ARN.
+ **kms:ViaService** – The execution role permissions are scoped to `s3.*.amazonaws.com` (Amazon S3 SSE-KMS operations on your output bucket); the caller identity runtime permissions are scoped to `sagemaker.*.amazonaws.com` (service authorization checks).
+ **Confused-deputy protection** – Use the `aws:SourceArn` or `aws:SourceAccount` condition keys in your AWS KMS key policy to prevent the confused deputy problem. This ensures that only requests originating from your specific account or resource can use the key:

  ```
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "{{account-id}}"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:sagemaker:{{region}}:{{account-id}}:training-session/*"
    }
  }
  ```
+ **kms:GrantIsForAWSResource** – This condition on `kms:CreateGrant` restricts the caller grant-creation permission so it can be used only when an AWS service creates the grant on your behalf; the caller cannot use it to create arbitrary grants directly.

### Encryption context for training sessions
<a name="training-sessions-cmk-encryption-context"></a>

When Training Sessions encrypts data with your customer managed KMS key, it includes an encryption context in every AWS KMS request. An encryption context is a set of key-value pairs that provide additional authenticated data (AAD) for AWS KMS operations. The encryption context is logged in AWS CloudTrail and can be used in KMS key policies and grant constraints to further restrict access.

Training Sessions uses the following encryption context key-value pair:

```
{
  "aws:sagemaker:training-session-arn": "arn:aws:sagemaker:{{region}}:{{account-id}}:training-session/{{session-id}}"
}
```

The encryption context is enforced automatically through the grant constraint that Training Sessions applies at session creation time; the execution role Amazon S3 operations run within the grant scope, so its policy statement does not need to duplicate the encryption context condition. You do not need to add encryption context conditions to your key policy for encryption to work correctly. When you review CloudTrail logs, the encryption context appears in the `requestParameters` field and identifies the training session that performed each operation.

### Monitoring Training Sessions interaction with AWS KMS
<a name="training-sessions-cmk-monitoring"></a>

You can use AWS CloudTrail to monitor the AWS KMS API calls made on behalf of your training sessions. The `userIdentity.invokedBy` field shows the service that made each call on your behalf. The following CloudTrail event names are relevant for monitoring:
+ `CreateGrant` – Logged when the session grant is created at `CreateTrainingSession`; `invokedBy` shows `sagemaker.amazonaws.com`.
+ `RetireGrant` – Logged when the grant is retired as the session reaches a terminal state (stopped, failed, or deleted); `invokedBy` shows `training-session.sagemaker.amazonaws.com`.
+ `GenerateDataKey` – Logged when the service writes encrypted data to Amazon S3 (`invokedBy` shows the Amazon S3 service), and for authorization checks before runtime operations (`invokedBy` shows `training-session.sagemaker.amazonaws.com`).
+ `Decrypt` – Logged when the service reads encrypted data from Amazon S3 (`invokedBy` shows the Amazon S3 service), and for authorization checks before runtime operations (`invokedBy` shows `training-session.sagemaker.amazonaws.com`).
+ `DescribeKey` – Logged when the key is validated at session creation.

In the CloudTrail log entries, look for the following values:
+ `requestParameters.encryptionContext["aws:sagemaker:training-session-arn"]` – On `GenerateDataKey` and `Decrypt` events for Amazon S3 operations, identifies the training session that performed the operation. This is the authoritative field for attributing AWS KMS activity to a specific training session.
+ `requestParameters.granteePrincipal` – On `CreateGrant` events, shows the service principal that received the grant: `sagemaker.{{region}}.amazonaws.com` (for example, `sagemaker.us-west-2.amazonaws.com`). The `retiringPrincipal` shows the same value. On a denied `CreateGrant`, CloudTrail records no `requestParameters`, so this field is absent.

For guidance on searching AWS KMS CloudTrail events, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html#searching-kms-ct) in the *AWS KMS Developer Guide*.