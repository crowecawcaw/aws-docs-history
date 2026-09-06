

# Encryption at rest for multi-turn reinforcement learning
<a name="model-customize-mtrl-encryption-at-rest"></a>

## Options for encryption at rest
<a name="model-customize-mtrl-encryption-options"></a>

Multi-turn reinforcement learning jobs in Amazon SageMaker AI encrypt all data at rest. Your training input data, output data (including model checkpoints and trained model artifacts), and intermediate data stored in Amazon S3 are encrypted using server-side encryption. You do not need to perform any additional configuration to ensure that your data is encrypted at rest.

Amazon SageMaker AI supports the following encryption options for multi-turn RL jobs:
+ **Server-side encryption with AWS owned KMS key** – By default, Amazon SageMaker AI encrypts all training output and intermediate data using an AWS owned KMS key. No additional configuration is required.
+ **Server-side encryption with AWS KMS keys (SSE-KMS)** – You can optionally specify a customer managed KMS key to encrypt your training output data in Amazon S3. If your input data in Amazon S3 is already encrypted with a customer managed key, the execution role must have permission to decrypt that data.

## Encrypting data at rest using customer managed AWS KMS keys
<a name="model-customize-mtrl-cmk"></a>

### How multi-turn RL uses a customer managed KMS key
<a name="model-customize-mtrl-cmk-how"></a>

When you specify a customer managed KMS key in the output configuration of your multi-turn RL job, Amazon SageMaker AI uses that key to encrypt the following resources in Amazon S3:
+ Training output data, including trained model artifacts (LoRA adapter weights)
+ Intermediate model input/output (resumable model checkpoints and trajectory data)
+ MLflow experiment data and traces

When you specify a customer managed KMS key, Amazon SageMaker AI uses two mechanisms to encrypt your data:
+ **Grants** – At job creation time, Amazon SageMaker AI uses the caller's credentials to create one or two grants on the KMS key:
  + **Write grant** – Created for every job that specifies a customer managed key. Allows the service to encrypt and decrypt the current job's checkpoint and temporary data stored within the platform during training.
  + **Read grant** – Created only for iterative jobs that resume from a previous job's checkpoint when the previous job also used a customer managed key. Allows the service to decrypt the previous job's checkpoint data. This grant permits decryption only and does not allow writing new data.

  All grants are retired automatically when the job completes, ensuring that the service no longer has access to the key after the job lifecycle ends.
+ **Execution role** – When saving output data (model artifacts, checkpoints) to your Amazon S3 bucket, Amazon SageMaker AI uses the execution role you provide. The execution role must have permissions to use the KMS key for encryption and decryption through Amazon S3.

During a training job, the following AWS KMS operations occur:
+ `kms:GenerateDataKey` – Called through Amazon S3 when writing encrypted output data (model artifacts, checkpoints, and logs).
+ `kms:Decrypt` – Called through Amazon S3 when reading encrypted input data or previously written output data.
+ `kms:DescribeKey` – Called by the caller identity at job creation time to verify the KMS key configuration and state.
+ `kms:CreateGrant` – Called by the caller identity at job creation time to give permission to the service to store temporary data within the platform for the lifecycle of the job.

The service does not cache data keys. Each Amazon S3 read or write operation calls AWS KMS independently through the Amazon S3 service integration.

### Configuring a customer managed KMS key
<a name="model-customize-mtrl-cmk-configure"></a>

Multi-turn RL jobs support symmetric AWS KMS keys only. Multi-region keys are not supported.

#### Configuring permissions to use a customer managed KMS key
<a name="model-customize-mtrl-cmk-permissions"></a>

To use a customer managed KMS key with multi-turn RL jobs, you must configure permissions on both the IAM execution role and the KMS key policy.

The IAM execution role that you pass to the `CreateJob` API must have the following AWS KMS permissions. These permissions allow the training job to encrypt output data and decrypt input data through Amazon S3.

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
+ `kms:Decrypt` – Required to read encrypted input data and previously written output data from Amazon S3.
+ `kms:GenerateDataKey` – Required to encrypt output data (model artifacts, checkpoints) written to Amazon S3.

The `kms:ViaService` condition restricts use of the key to requests that come through Amazon S3, preventing the key from being used for other purposes.

The agent runtime role that your Amazon Bedrock AgentCore agent or AWS Lambda forwarder assumes must have the following AWS KMS permissions. SageMaker AI checks that the caller has these permissions before using the KMS key during a multi-turn reinforcement learning (RL) job.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "KMSPermissionsForMTRLRuntime",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "sagemaker.*.amazonaws.com"
                }
            }
        }
    ]
}
```

The `kms:ViaService` condition for the agent runtime role specifies `sagemaker.*.amazonaws.com` because the SageMaker AI runtime service performs the AWS KMS operations on behalf of the caller. In contrast, the execution role uses `s3.*.amazonaws.com` because it accesses the key through Amazon S3.

The default KMS key policy already allows IAM roles in the same account to use the key. Optionally, you can add the following statement to further restrict access to only the execution role and agent runtime role:

```
{
    "Sid": "AllowMTRLJobEncryption",
    "Effect": "Allow",
    "Principal": {
        "AWS": [
            "arn:aws:iam::{{account-id}}:role/{{SageMakerExecutionRole}}",
            "arn:aws:iam::{{account-id}}:role/{{AgentRuntimeRole}}"
        ]
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringLike": {
            "kms:ViaService": [
                "s3.*.amazonaws.com",
                "sagemaker.*.amazonaws.com"
            ]
        }
    }
}
```

To allow the caller to create grants and describe the key, add the following statement to the key policy:

```
{
    "Sid": "AllowCreateGrantForCaller",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::{{account-id}}:role/{{CallerRole}}"
    },
    "Action": [
        "kms:CreateGrant",
        "kms:DescribeKey"
    ],
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
        }
    }
}
```

#### Creating a multi-turn RL job with a customer managed KMS key
<a name="model-customize-mtrl-cmk-create-job"></a>

To encrypt output data with your customer managed KMS key, specify the key ARN in the `KmsKeyArn` field of the `OutputDataConfig` in your `CreateJob` request. For more information, see [CreateJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateJob.html) in the *SageMaker AI API Reference*.

The following example shows how to specify a KMS key in the `OutputDataConfig`:

```
{
    "OutputDataConfig": {
        "S3OutputPath": "s3://{{your-bucket}}/output/",
        "KmsKeyArn": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}"
    }
}
```

If your input data in Amazon S3 is encrypted with a customer managed key (SSE-KMS), ensure that the execution role has `kms:Decrypt` permission for that key. You can use the same key for both input and output encryption, or different keys.

#### Scoping down access to the customer managed KMS key
<a name="model-customize-mtrl-cmk-scope-down"></a>

You can use the following mechanisms to restrict access to your customer managed KMS key:

sagemaker:OutputKmsKeyArn condition key  
Use the `sagemaker:OutputKmsKeyArn` condition key in the caller's IAM policy to control which KMS key can be specified for job output encryption. This allows administrators to enforce that only approved keys are used when creating multi-turn RL jobs. For the full list of SageMaker AI condition keys, see [Actions, resources, and condition keys for Amazon SageMaker AI](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonsagemaker.html).  

```
"Condition": {
    "ArnEquals": {
        "sagemaker:OutputKmsKeyArn": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}"
    }
}
```

Confused deputy protection  
Use the `aws:SourceArn` or `aws:SourceAccount` condition keys in your KMS key policy to prevent the confused deputy problem. This ensures that only requests originating from your specific account or resource can use the key.  

```
"Condition": {
    "StringEquals": {
        "aws:SourceAccount": "{{account-id}}"
    },
    "ArnLike": {
        "aws:SourceArn": "arn:aws:sagemaker:{{region}}:{{account-id}}:job/*"
    }
}
```

## Encryption context for multi-turn RL jobs
<a name="model-customize-mtrl-cmk-encryption-context"></a>

When a multi-turn RL job encrypts data using your customer managed KMS key, Amazon SageMaker AI includes an *encryption context* in every AWS KMS request made through Amazon S3. An encryption context is a set of key-value pairs that provide additional authenticated data (AAD) for AWS KMS operations. The encryption context is logged in AWS CloudTrail and can be used in KMS key policies and grant constraints to further restrict access.

Amazon SageMaker AI uses the following encryption context key-value pair for multi-turn RL training jobs:

```
{
    "aws:sagemaker:finetuning-job-arn": "arn:aws:sagemaker:{{region}}:{{account-id}}:job/AgentRFT/{{job-name}}"
}
```

For multi-turn RL evaluation jobs, the encryption context uses:

```
{
    "aws:sagemaker:agent-rft-evaluation-job-arn": "arn:aws:sagemaker:{{region}}:{{account-id}}:job/AgentRFTEvaluation/{{job-name}}"
}
```

The encryption context is bound to the specific job that creates the encrypted data. Each job encrypts its own output with its own ARN in the encryption context. This provides cryptographic binding between the encrypted data and the job that produced it.

The encryption context is enforced automatically through the grant constraints that Amazon SageMaker AI creates at job creation time. You do not need to add encryption context conditions to your KMS key policy for encryption to work correctly.

If you add encryption context conditions to the `kms:CreateGrant` statement in your KMS key policy, you must allow grants for both the current job and the previous job in iterative training chains. The following example allows Amazon SageMaker AI to create grants with any training job ARN in the encryption context:

```
{
    "Sid": "AllowCreateGrantForCaller",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::{{account-id}}:role/{{CallerRole}}"
    },
    "Action": [
        "kms:CreateGrant",
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringLike": {
            "kms:ViaService": "sagemaker.*.amazonaws.com",
            "kms:EncryptionContext:aws:sagemaker:finetuning-job-arn": "arn:aws:sagemaker:{{region}}:{{account-id}}:job/AgentRFT/*"
        },
        "Bool": {
            "kms:GrantIsForAWSResource": "true"
        }
    }
}
```

**Note**  
If you restrict `kms:CreateGrant` to a single specific job ARN in the encryption context, iterative training will fail because Amazon SageMaker AI also creates a read grant with the previous job's ARN as the encryption context. Use a wildcard pattern to allow grants for any job in your account.

When you run iterative training jobs (where a subsequent job resumes from a previous job's checkpoint), the encryption context for each job contains that job's own ARN. Amazon SageMaker AI automatically manages two AWS KMS grants to support iterative training:
+ **Write grant** – Allows the current job to encrypt its own checkpoint data using the current job's ARN as the encryption context.
+ **Read grant** – Allows the current job to decrypt checkpoint data from the previous job using the previous job's ARN as the encryption context.

Both grants are automatically retired when the job completes. You do not need to add any additional key policy statements for iterative training to work with customer managed keys.

When you review CloudTrail logs for AWS KMS API calls made by multi-turn RL jobs, the encryption context appears in the `requestParameters` field of the log entry. You can use this information to determine which job performed a specific encryption or decryption operation on your data.

## Monitoring multi-turn RL interaction with AWS KMS
<a name="model-customize-mtrl-cmk-monitoring"></a>

You can use AWS CloudTrail to monitor AWS KMS API calls made on behalf of your multi-turn RL jobs. The following CloudTrail event names are relevant for monitoring KMS key usage:
+ `Decrypt` – Logged when the job reads encrypted data from Amazon S3.
+ `GenerateDataKey` – Logged when the job writes encrypted data to Amazon S3.
+ `CreateGrant` – Logged when the caller creates a grant at job creation time.
+ `DescribeKey` – Logged when the job describes the KMS key for validation.

In the CloudTrail log entries for these events, look for the following values:
+ **requestParameters.granteePrincipal** – For `CreateGrant` events, shows the service principal that received the grant (`job.sagemaker.amazonaws.com`).

For more information about logging AWS KMS API calls, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html#searching-kms-ct) in the *AWS KMS Developer Guide*.