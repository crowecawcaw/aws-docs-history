

# Use AWS KMS permissions for MLflow Apps
<a name="mlflow-kms"></a>

You can protect your data at rest using encryption for MLflow Apps. By default, MLflow Apps use server-side encryption with an AWS owned key. SageMaker also supports an option for server-side encryption with a customer managed KMS key.

**Note**  
The customer managed key encrypts the data that SageMaker manages for the MLflow App. It does not encrypt the artifacts you store in your own Amazon S3 artifact store. That Amazon S3 bucket is created and owned by you, not managed by AWS, so you are responsible for configuring its encryption. To encrypt your artifacts with a customer managed key, set the default encryption on your Amazon S3 bucket. For more information, see [Setting default server-side encryption behavior for Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html) in the *Amazon Simple Storage Service User Guide*.

## Server-side encryption with AWS owned keys
<a name="mlflow-kms-managed-key"></a>

By default, MLflow Apps encrypt your data at rest using an AWS owned key.

## Server-side encryption with customer managed KMS keys
<a name="mlflow-kms-customer-managed-key"></a>

As an option, you can use a symmetric customer managed key that you create, own, and manage to replace the existing AWS owned encryption. Because you have full control of this layer of encryption, you can perform such tasks as:
+ Establishing and maintaining key policies
+ Establishing and maintaining IAM policies and grants
+ Enabling and disabling key policies
+ Rotating key cryptographic material
+ Adding tags
+ Creating key aliases
+ Scheduling keys for deletion

For more information, see [Customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in the *AWS Key Management Service Developer Guide*.

## How MLflow Apps use grants in AWS KMS
<a name="mlflow-kms-grants"></a>

To use your customer managed key, your MLflow App requires a grant. When you create an MLflow App encrypted with a customer managed key, SageMaker creates a grant on your behalf by sending a `CreateGrant` request to AWS KMS. AWS KMS grants give MLflow Apps access to your customer managed key. When you delete an MLflow App, SageMaker retires the grant.

You can revoke the grant, or remove the service's access to your customer managed key, at any time. Revoking access does not immediately interrupt a running MLflow App. The underlying storage layer continues to use the access granted when the app was created. After you revoke access, SageMaker can no longer use your key for subsequent operations that require it, such as scheduled maintenance. If your key becomes permanently unavailable — for example, if you disable it or schedule it for deletion — your data at rest can no longer be decrypted, and the MLflow App becomes unrecoverable.

## Configuring a customer managed KMS key for an MLflow App
<a name="mlflow-kms-configure"></a>

You can create a symmetric customer managed key by using the AWS Management Console or the AWS KMS APIs.

You can specify the customer managed key for an MLflow App only at creation time. You cannot change it for the lifetime of the app. MLflow Apps do not support switching an existing app between an AWS owned key and a customer managed key, or replacing one customer managed key with another. If you want to use a different key, delete the MLflow App and create a new one with the desired encryption configuration.

### Creating a symmetric customer managed key
<a name="mlflow-kms-configure-create-key"></a>

Follow the steps for [Creating symmetric encryption KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the *AWS Key Management Service Developer Guide*.

### Key policy
<a name="mlflow-kms-configure-key-policy"></a>

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it. When you create your customer managed key, you can specify a key policy. For more information, see [Determining access to AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/determining-access.html) in the *AWS Key Management Service Developer Guide*.

To use your customer managed key with your MLflow App, your key policy must permit the following API operations. The principal for these operations depends on whether the role is used to create or use the application.
+ Creating the application:
  + [kms:CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html)
  + [kms:DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html)
+ Using the application:
  + No AWS KMS permissions are required.

The following are policy statement examples you can add for MLflow Apps based on whether the persona is an administrator or a user. For more information about specifying permissions in a policy, see [AWS KMS permissions](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) in the *AWS Key Management Service Developer Guide*. For more information about troubleshooting, see [Troubleshooting key access](https://docs.aws.amazon.com/kms/latest/developerguide/policy-evaluation.html) in the *AWS Key Management Service Developer Guide*.

#### Administrator
<a name="mlflow-kms-configure-key-policy-administrator"></a>

The following policy can be used for the administrator who is creating MLflow Apps.

```
{
    "Sid": "AllowMLflowAppAdministratorAccess",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::{{111122223333}}:role/{{mlflow-app-admin-role}}"
    },
    "Action": [
        "kms:CreateGrant",
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "sagemaker.{{region}}.amazonaws.com"
        },
        "ForAllValues:StringEquals": {
            "kms:GrantOperations": [
                "CreateGrant",
                "Decrypt",
                "DescribeKey",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "RetireGrant"
            ]
        }
    }
}
```
+ `kms:ViaService` — Restricts use of the key to requests that originate from SageMaker in a specific Region. With `"kms:ViaService": "sagemaker.{{region}}.amazonaws.com"`, the `kms:CreateGrant` and `kms:DescribeKey` permissions can be exercised only when the request is made through SageMaker on your behalf — not directly by any other principal or service. This ensures your key is used only for your MLflow App.
+ `kms:GrantOperations` — Constrains the operations that the grant SageMaker creates is allowed to contain. When you create an MLflow App, SageMaker calls `CreateGrant` to allow its data plane to encrypt and decrypt your data at rest. Adding `kms:GrantOperations` to the `kms:CreateGrant` statement ensures SageMaker can only create a grant containing exactly the operations required for that purpose — `CreateGrant`, `Decrypt`, `DescribeKey`, `Encrypt`, `GenerateDataKey`, `GenerateDataKeyWithoutPlaintext`, `ReEncryptFrom`, `ReEncryptTo`, and `RetireGrant`.
+ Encryption context — Not applicable. MLflow Apps do not set a custom encryption context on the grant, so you cannot use the `kms:EncryptionContext` condition key to further scope down access.

#### User
<a name="mlflow-kms-configure-key-policy-user"></a>

Accessing an MLflow App — through the MLflow APIs or a presigned URL — does not involve AWS KMS. SageMaker encrypts and decrypts your data at rest for you, and no AWS KMS request is made when you access the app. As a result, if you access an MLflow App, you do not need any AWS KMS permissions. You do not need to account for AWS KMS access when you define security policies for your users.

## Creating a new MLflow App with a customer managed KMS key
<a name="mlflow-kms-create-app"></a>

To encrypt your MLflow App with a customer managed key, specify the key when you create the app by using the `--kms-key-id` parameter of the `create-mlflow-app` AWS CLI command. If you omit this parameter, SageMaker uses an AWS owned key. The role that calls `create-mlflow-app` must have `kms:CreateGrant` and `kms:DescribeKey` permissions on the customer managed key.

```
aws sagemaker create-mlflow-app \
  --name {{app-name}} \
  --artifact-store-uri s3://{{bucket-name}} \
  --role-arn {{role-arn}} \
  --kms-key-id {{your-kms-key-id}} \
  --region {{your-region}}
```

For more information about creating an MLflow App, see [Create MLflow App](mlflow-app-setup-create-app.md).

## Monitoring MLflow Apps interaction with AWS KMS
<a name="mlflow-kms-monitoring"></a>

You can use CloudTrail to track the requests that are made to AWS KMS on your behalf when your MLflow App uses a customer managed key. For more information about finding and interpreting AWS KMS events in CloudTrail, see [Logging AWS KMS API calls with CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html#searching-kms-ct) in the *AWS Key Management Service Developer Guide*.

The following AWS KMS CloudTrail events are recorded for an MLflow App encrypted with a customer managed key:
+ `DescribeKey` and `CreateGrant` — Recorded when you create an MLflow App. SageMaker validates your key and creates the grant that allows your data at rest to be encrypted and decrypted on your behalf.
+ `GenerateDataKeyWithoutPlaintext`, `Encrypt`, and `Decrypt` — Recorded while the MLflow App is being provisioned and while it operates. The SageMaker underlying storage layer uses your customer managed key to encrypt and decrypt your data at rest. These requests are made by AWS services acting on your behalf through the grant, so the CloudTrail `userIdentity` element shows an AWS service as the caller rather than an IAM principal from your account.
+ `RetireGrant` — Recorded when you delete an MLflow App. The grants created for the app are retired so that your customer managed key can no longer be used for it.