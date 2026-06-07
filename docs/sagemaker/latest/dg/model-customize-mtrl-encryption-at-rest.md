# Encryption at rest for multi-turn reinforcement learning

## Options for encryption at rest

Multi-turn reinforcement learning jobs in Amazon SageMaker AI encrypt all data at rest.
Your training input data, output data (including model checkpoints and trained
model artifacts), and intermediate data stored in Amazon S3 are encrypted using
server-side encryption. You do not need to perform any additional configuration
to ensure that your data is encrypted at rest.

Amazon SageMaker AI supports the following encryption options for multi-turn RL
jobs:

- **Server-side encryption with AWS owned KMS key** – By default, Amazon SageMaker AI encrypts all
  training output and intermediate data using an AWS owned KMS key.
  No additional configuration is required.
- **Server-side encryption with AWS KMS keys
  (SSE-KMS)** – You can optionally specify a customer
  managed KMS key to encrypt your training output data in Amazon S3. If your
  input data in Amazon S3 is already encrypted with a customer managed key, the
  execution role must have permission to decrypt that data.

## Encrypting data at rest using customer managed AWS KMS keys

### How multi-turn RL uses a customer managed KMS key

When you specify a customer managed KMS key in the output configuration
of your multi-turn RL job, Amazon SageMaker AI uses that key to encrypt the following
resources in Amazon S3:

- Training output data, including trained model artifacts (LoRA
  adapter weights)
- Intermediate model input/output (resumable model checkpoints
  and trajectory data)
- MLflow experiment data and traces

When you specify a customer managed KMS key, Amazon SageMaker AI uses two
mechanisms to encrypt your data:

- **Grant** – At job creation
  time, Amazon SageMaker AI uses the caller's credentials to create a grant on
  the KMS key. This grant allows the service to encrypt all
  temporary data stored within the platform during training. The
  grant is retired automatically when the job completes, ensuring
  that the service no longer has access to the key after the job
  lifecycle ends.
- **Execution role** – When
  saving output data (model artifacts, checkpoints) to your Amazon S3
  bucket, Amazon SageMaker AI uses the execution role you provide. The execution
  role must have permissions to use the KMS key for encryption and
  decryption through Amazon S3.

During a training job, the following AWS KMS operations occur:

- `kms:GenerateDataKey` – Called through Amazon S3 when
  writing encrypted output data (model artifacts, checkpoints, and
  logs).
- `kms:Decrypt` – Called through Amazon S3 when reading
  encrypted input data or previously written output data.
- `kms:DescribeKey` – Called to verify the
  KMS key configuration and state.
- `kms:CreateGrant` – Called by the caller identity
  at job creation time to give permission to the service to store
  temporary data within the platform for the lifecycle of the
  job.

The service does not cache data keys. Each Amazon S3 read or write operation
calls AWS KMS independently through the Amazon S3 service integration.

### Configuring a customer managed KMS key

Multi-turn RL jobs support symmetric AWS KMS keys only. Multi-region keys
are not supported.

#### Configuring permissions to use a customer managed KMS key

To use a customer managed KMS key with multi-turn RL jobs, you must
configure permissions on both the IAM execution role and the KMS key
policy.

###### Execution role permissions

The IAM execution role that you pass to the `CreateJob`
API must have the following AWS KMS permissions. These permissions allow
the training job to encrypt output data and decrypt input data through
Amazon S3.

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
            "Resource": "arn:aws:kms:`region`:`account-id`:key/`key-id`",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "s3.*.amazonaws.com"
                }
            }
        }
    ]
}
```

- `kms:Decrypt` – Required to read encrypted
  input data and previously written output data from Amazon S3.
- `kms:GenerateDataKey` – Required to encrypt
  output data (model artifacts, checkpoints) written to
  Amazon S3.

The `kms:ViaService` condition restricts use of the key to
requests that come through Amazon S3, preventing the key from being used for
other purposes.

###### KMS key policy

Your KMS key policy must allow the execution role to use the key
for encryption and decryption through Amazon S3. The following example shows
a least-privilege key policy statement:

```
{
    "Sid": "AllowMTRLJobEncryption",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::`account-id`:role/`SageMakerExecutionRole`"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringLike": {
            "kms:ViaService": "s3.*.amazonaws.com"
        }
    }
}
```

To allow the caller to create grants and describe the key, add the
following statement to the key policy:

```
{
    "Sid": "AllowCreateGrantForCaller",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::`account-id`:role/`CallerRole`"
    },
    "Action": [
        "kms:CreateGrant",
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:CallerAccount": "`account-id`"
        },
        "StringLike": {
            "kms:ViaService": "sagemaker.*.amazonaws.com"
        },
        "Bool": {
            "kms:GrantIsForAWSResource": "true"
        }
    }
}
```

#### Creating a multi-turn RL job with a customer managed KMS key

To encrypt output data with your customer managed KMS key, specify
the key ARN in the `KmsKeyArn` field of the
`OutputDataConfig` in your `CreateJob` request.
For more information, see [CreateJob](../APIReference/API_CreateJob.md "../APIReference/API_CreateJob.md") in the _SageMaker AI API
Reference_.

The following example shows how to specify a KMS key in the
`OutputDataConfig`:

```
{
    "OutputDataConfig": {
        "S3OutputPath": "s3://`your-bucket`/output/",
        "KmsKeyArn": "arn:aws:kms:`region`:`account-id`:key/`key-id`"
    }
}
```

If your input data in Amazon S3 is encrypted with a customer managed key
(SSE-KMS), ensure that the execution role has
`kms:Decrypt` permission for that key. You can use the same
key for both input and output encryption, or different keys.

#### Scoping down access to the customer managed KMS key

You can use the following mechanisms to restrict access to your
customer managed KMS key:

sagemaker:OutputKmsKeyArn condition key

Use the `sagemaker:OutputKmsKeyArn` condition
key in the caller's IAM policy to control which KMS key
can be specified for job output encryption. This allows
administrators to enforce that only approved keys are used
when creating multi-turn RL jobs. For the full list of SageMaker AI
condition keys, see [Actions, resources, and condition keys for Amazon SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md "../../../service-authorization/latest/reference/list_amazonsagemaker.md").

```
"Condition": {
    "ArnEquals": {
        "sagemaker:OutputKmsKeyArn": "arn:aws:kms:`region`:`account-id`:key/`key-id`"
    }
}
```

Confused deputy protection

Use the `aws:SourceArn` or
`aws:SourceAccount` condition keys in your
KMS key policy to prevent the confused deputy problem.
This ensures that only requests originating from your
specific account or resource can use the key.

```
"Condition": {
    "StringEquals": {
        "aws:SourceAccount": "`account-id`"
    },
    "ArnLike": {
        "aws:SourceArn": "arn:aws:sagemaker:`region`:`account-id`:job/*"
    }
}
```

## Monitoring multi-turn RL interaction with AWS KMS

You can use AWS CloudTrail to monitor AWS KMS API calls made on behalf of your
multi-turn RL jobs. The following CloudTrail event names are relevant for monitoring
KMS key usage:

- `Decrypt` – Logged when the job reads encrypted data
  from Amazon S3.
- `GenerateDataKey` – Logged when the job writes
  encrypted data to Amazon S3.
- `CreateGrant` – Logged when the caller creates a
  grant at job creation time.
- `DescribeKey` – Logged when the job describes the
  KMS key for validation.

In the CloudTrail log entries for these events, look for the following
values:

- **requestParameters.granteePrincipal**
  – For `CreateGrant` events, shows the service
  principal that received the grant
  (`job.sagemaker.amazonaws.com`).

For more information about logging AWS KMS API calls, see [Logging AWS KMS API calls with AWS CloudTrail](../../../kms/latest/developerguide/logging-using-cloudtrail.md#searching-kms-ct "../../../kms/latest/developerguide/logging-using-cloudtrail.md#searching-kms-ct") in the _AWS KMS Developer Guide_.
