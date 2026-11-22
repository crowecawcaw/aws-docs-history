

# Encrypting AWS Lambda MicroVM data

AWS Lambda MicroVMs encrypts your data at rest. This section explains the encryption options available to you and how to configure a customer managed key.

## Options for encryption at rest
<a name="microvms-encryption-options"></a>

Lambda MicroVMs encrypts your MicroVM image environment variables, the MicroVM image, and the run hook payload passed to each MicroVM. At-rest encryption for this data is always enabled and cannot be turned off. You have two options for the AWS KMS key that is used to encrypt data at rest:

AWS owned key (default)  
By default, Lambda MicroVMs encrypts your data with an [AWS owned KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk). AWS owns and manages this key. You cannot view, manage, or audit its use. If this default behavior suits your needs, no additional setup is required.

Customer managed key  
You can optionally configure your own [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk). Use a customer managed key when you need to control key rotation, audit key use through CloudTrail, manage key access through a key policy, or meet organizational compliance requirements. With a customer managed key, only principals you authorize can read your encrypted data. Customer managed keys incur AWS KMS charges. For more information, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/).

## Encrypting data at rest using a customer managed key
<a name="microvms-encryption-cmk"></a>

The following sections explain what Lambda MicroVMs encrypts, how to configure the key and its permissions, and how to scope down access to it.

### What is encrypted
<a name="microvms-encryption-what-is-encrypted"></a>

When you specify a customer managed key, Lambda MicroVMs uses [envelope encryption](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#enveloping) to encrypt the following resources:


| Resource | What is encrypted | Encrypted on | Decrypted on | 
| --- | --- | --- | --- | 
| MicroVM image environment variables | The environment variables set on a MicroVM image version. | Create or update the image | Image build, image-version read or update | 
| MicroVM image | The MicroVM image artifact that Lambda MicroVMs builds and stores in Amazon S3. | Image build | MicroVM run | 
| Run hook payload | The per-MicroVM run configuration you pass when you run a MicroVM. | Run a MicroVM | MicroVM launch | 

Lambda MicroVMs doesn't use AWS KMS grants. Access is authorized through the key policy and the calling principal's IAM permissions.

Lambda MicroVMs binds the MicroVM image ARN into the encryption context on every AWS KMS operation, so you can scope access to specific images in your key policy:
+ `aws:lambda:MicrovmImageArn` – The Amazon Resource Name (ARN) of the MicroVM image. This appears in your key policy as the condition key `kms:EncryptionContext:aws:lambda:MicrovmImageArn` for all three resources.

For more information, see [Scoping down access to your KMS key](#microvms-encryption-scoping-down).

### Configuring a customer managed key
<a name="microvms-encryption-configuring-key"></a>

The AWS KMS key must be a symmetric encryption key (key spec `SYMMETRIC_DEFAULT`, key usage `ENCRYPT_DECRYPT`). You can't use asymmetric keys. The key must be in the same AWS Region as the MicroVM image, and you must identify it by its key ARN or alias ARN. A bare key ID or alias name is not accepted.

### Configuring permissions to use a customer managed key
<a name="microvms-encryption-permissions"></a>

Your AWS KMS key policy must grant access to the following [principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal). If the principal making the request cannot use the key, the request fails before Lambda MicroVMs stores any data.
+ **The principal that creates or updates an image.** It needs `kms:DescribeKey`, `kms:GenerateDataKey`, and `kms:Decrypt`. A principal that only reads or updates an image version needs `kms:Decrypt`.
+ **The principal that runs a MicroVM.** It needs `kms:DescribeKey`, `kms:GenerateDataKeyWithoutPlaintext`, `kms:ReEncryptFrom`, `kms:ReEncryptTo`, and `kms:Decrypt`.
+ **A principal that both manages MicroVM images and runs MicroVMs.** It needs the permissions of both principals: `kms:DescribeKey`, `kms:GenerateDataKey`, `kms:GenerateDataKeyWithoutPlaintext`, `kms:ReEncryptFrom`, `kms:ReEncryptTo`, and `kms:Decrypt`.
+ **The Lambda service principal** (`lambda.amazonaws.com`). Lambda MicroVMs uses this principal when it builds your image, when it decrypts the image to launch a MicroVM, and when it rotates the key material for the run hook payload. It needs `kms:GenerateDataKey`, `kms:Decrypt`, `kms:GenerateDataKeyWithoutPlaintext`, and `kms:ReEncrypt*`.

Grant the following AWS KMS actions in the key policy:
+ `kms:DescribeKey` – Lambda MicroVMs uses this to confirm the key exists in the Region and is a symmetric encryption key when you create or update an image, or run a MicroVM.
+ `kms:GenerateDataKey` – Lambda MicroVMs uses this to generate the data keys that encrypt your MicroVM image and its environment variables.
+ `kms:GenerateDataKeyWithoutPlaintext` – Lambda MicroVMs uses this to generate the key that encrypts the run hook payload, and to replace that key when it rotates.
+ `kms:ReEncryptFrom` and `kms:ReEncryptTo` – Lambda MicroVMs uses these to rotate the key that encrypts the run hook payload. In the key policy, `kms:ReEncrypt*` grants both.
+ `kms:Decrypt` – Lambda MicroVMs uses this to decrypt your data when it builds your image, launches your MicroVM, or returns an image version's environment variables to you.

The request fails if the key is missing, disabled, not a symmetric encryption key, or the caller does not have the required permissions.

**Note**  
You do not need `kms:Encrypt` permission. Lambda MicroVMs uses [envelope encryption](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#enveloping), generating data keys with `GenerateDataKey` or `GenerateDataKeyWithoutPlaintext` without requiring a separate encrypt call.

#### Example key policy
<a name="microvms-encryption-key-policy"></a>

The following key policy contains the statements that Lambda MicroVMs requires, each scoped down with the conditions described in [Scoping down access to your KMS key](#microvms-encryption-scoping-down).
+ **Allow image and MicroVM principals to describe this key.** Grants `kms:DescribeKey` to the principals that create images and run MicroVMs.
+ **Allow the image principal to use this key for MicroVM images.** Grants `kms:GenerateDataKey` and `kms:Decrypt` to the principal that creates and updates images.
+ **Allow the MicroVM principal to use this key for run hook payloads.** Grants `kms:GenerateDataKeyWithoutPlaintext`, `kms:ReEncryptFrom`, `kms:ReEncryptTo`, and `kms:Decrypt` to the principal that runs MicroVMs, so that it can encrypt and decrypt the run hook payload passed to the MicroVM.
+ **Allow Lambda MicroVMs to use this key for image builds and launches.** Grants `kms:GenerateDataKey` and `kms:Decrypt` to the Lambda service principal.
+ **Allow Lambda MicroVMs to rotate the run hook payload key.** Grants `kms:GenerateDataKeyWithoutPlaintext` and `kms:ReEncrypt*` to the Lambda service principal.

`kms:DescribeKey` is in its own statement because it is a metadata operation that carries no encryption context, so an encryption-context condition would never match it.

Add these statements to your existing key policy rather than replacing it, and keep the statement that grants your administrators access to manage the key.

**Example Key policy for Lambda MicroVMs**  

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Allow image and MicroVM principals to describe this key",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::111122223333:role/MicrovmImageAdminRole",
                    "arn:aws:iam::111122223333:role/RunMicrovmRole"
                ]
            },
            "Action": "kms:DescribeKey",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "lambda.us-east-1.amazonaws.com"
                }
            }
        },
        {
            "Sid": "Allow the image principal to use this key for MicroVM images",
            "Effect": "Allow",
            "Principal": { "AWS": "arn:aws:iam::111122223333:role/MicrovmImageAdminRole" },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "lambda.us-east-1.amazonaws.com"
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:lambda:MicrovmImageArn": "arn:aws:lambda:us-east-1:111122223333:microvm-image:*"
                }
            }
        },
        {
            "Sid": "Allow the MicroVM principal to use this key for run hook payloads",
            "Effect": "Allow",
            "Principal": { "AWS": "arn:aws:iam::111122223333:role/RunMicrovmRole" },
            "Action": [
                "kms:GenerateDataKeyWithoutPlaintext",
                "kms:ReEncryptFrom",
                "kms:ReEncryptTo",
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "lambda.us-east-1.amazonaws.com"
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:lambda:MicrovmImageArn": "arn:aws:lambda:us-east-1:111122223333:microvm-image:*"
                }
            }
        },
        {
            "Sid": "Allow Lambda MicroVMs to use this key for image builds and launches",
            "Effect": "Allow",
            "Principal": { "Service": "lambda.amazonaws.com" },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:lambda:us-east-1:111122223333:microvm-image:*"
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:lambda:MicrovmImageArn": "arn:aws:lambda:us-east-1:111122223333:microvm-image:*"
                }
            }
        },
        {
            "Sid": "Allow Lambda MicroVMs to rotate the run hook payload key",
            "Effect": "Allow",
            "Principal": { "Service": "lambda.amazonaws.com" },
            "Action": [
                "kms:GenerateDataKeyWithoutPlaintext",
                "kms:ReEncrypt*"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:lambda:us-east-1:111122223333:microvm-image:*"
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:lambda:MicrovmImageArn": "arn:aws:lambda:us-east-1:111122223333:microvm-image:*"
                }
            }
        }
    ]
}
```

For more information about AWS KMS key policies, see [Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *AWS Key Management Service Developer Guide*.

### Creating a MicroVM image with a customer managed key
<a name="microvms-encryption-create-image"></a>

To encrypt an image with a customer managed key, specify the key ARN or alias ARN in the `kmsKeyIdentifier` parameter when you create the image with `create-microvm-image`. If you omit `kmsKeyIdentifier`, Lambda MicroVMs encrypts the image with the AWS owned key. The same `kmsKeyIdentifier` parameter is available on `update-microvm-image`.

```bash
aws lambda-microvms create-microvm-image \
  --name my-microvm-image \
  --code-artifact uri=s3://{{my-bucket}}/app.zip \
  --base-image-arn arn:aws:lambda:{{us-east-1}}:aws:microvm-image:al2023-1 \
  --build-role-arn arn:aws:iam::111122223333:role/MicrovmImageAdminRole \
  --kms-key-identifier {{arn:aws:kms:us-east-1:111122223333:key/key-id}}
```

For more information, see [CreateMicrovmImage](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_CreateMicrovmImage.html) and [UpdateMicrovmImage](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_UpdateMicrovmImage.html) in the *AWS Lambda MicroVMs API Reference*.

### Changing the encryption configuration of an existing image
<a name="microvms-encryption-change-config"></a>

The `kmsKeyIdentifier` parameter is fixed for the life of an image version. Because image versions are immutable, you cannot change the key that protects an existing version. To change the encryption configuration, create a new image version that specifies the new key.

MicroVM images support the following key transitions:
+ **AWS owned key to customer managed key** – Create a new image version that specifies `kmsKeyIdentifier`.
+ **One customer managed key to a different customer managed key** – Create a new image version that specifies the new key ARN.
+ **Customer managed key to AWS owned key** – Create a new image version without `kmsKeyIdentifier`. Lambda MicroVMs then encrypts that version with the AWS owned key, which is the default.

Lambda MicroVMs does not re-encrypt existing image versions when you create a new version with a different key. Each version remains encrypted with the key that you specified when you created it. As long as an earlier version is still in use, its original key must remain enabled and accessible to the Lambda service principal. Before you disable or delete a key, confirm that no image version encrypted with that key is still in use.

### Running a MicroVM with a customer managed key
<a name="microvms-encryption-run-microvm"></a>

To encrypt the run hook payload with a customer managed key, specify the key ARN or alias ARN in the `kmsKeyIdentifier` parameter when you run the MicroVM with `run-microvm`. If you omit `kmsKeyIdentifier`, Lambda MicroVMs encrypts the run hook payload with the AWS owned key.

```bash
aws lambda-microvms run-microvm \
  --image-identifier arn:aws:lambda:{{us-east-1}}:111122223333:microvm-image:my-microvm-image \
  --run-hook-payload '{"sessionId": "example-session"}' \
  --kms-key-identifier {{arn:aws:kms:us-east-1:111122223333:key/key-id}}
```

For more information, see [RunMicrovm](https://docs.aws.amazon.com/lambda/latest/microvm-api/API_RunMicrovm.html) in the *AWS Lambda MicroVMs API Reference*.

### Scoping down access to your KMS key
<a name="microvms-encryption-scoping-down"></a>

The key policy in [Example key policy](#microvms-encryption-key-policy) restricts access with the following condition keys. Each one limits how the key can be used, so that access to the key is no broader than your MicroVMs need.

#### Encryption context
<a name="microvms-encryption-context"></a>

Lambda MicroVMs binds `aws:lambda:MicrovmImageArn` into the [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-encryption-context) on every AWS KMS request. We recommend a `StringLike` condition on `kms:EncryptionContext:aws:lambda:MicrovmImageArn` so the key can only be used for the MicroVM images you specify, such as the images in your account or a single image. Without it, any principal that your key policy allows can use the key for any MicroVM image. The same condition key applies to the image environment variables, the image, and the run hook payload, so add it to every statement in the [Example key policy](#microvms-encryption-key-policy) except the one that grants `kms:DescribeKey`.

**Important**  
Do not apply the encryption context condition to the statement that grants `kms:DescribeKey`. That operation carries no encryption context, so the condition would deny it.

#### kms:ViaService condition
<a name="microvms-encryption-via-service"></a>

The [kms:ViaService](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-via-service) condition restricts key use to requests routed through Lambda MicroVMs. The value is Region-specific: `lambda.{{us-east-1}}.amazonaws.com`. With this condition, AWS KMS denies direct calls made with the same credentials (for example, running `aws kms generate-data-key` yourself), but creating an image or running a MicroVM succeeds because Lambda MicroVMs makes the AWS KMS calls for you.

#### Confused deputy protection
<a name="microvms-encryption-confused-deputy"></a>

The confused deputy problem occurs when an entity without permission to perform an action coerces a more-privileged entity to perform it. Because the Lambda service principal can use your customer managed key, restrict that access to the MicroVM images that you own. For more information, see [The confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) in the *IAM User Guide*.

When Lambda MicroVMs calls AWS KMS with its own service credentials, it sends the image ARN as the source ARN and your AWS account ID as the source account. Use the [aws:SourceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) and [aws:SourceAccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) condition keys on the Lambda service principal statements.

Apply these conditions only to the Lambda service principal statements. The statements for the principals that create images and run MicroVMs call AWS KMS with the caller's credentials, which do not carry the source ARN and source account, so these conditions would deny those requests. The `kms:ViaService` condition restricts which service can use the key, but it does not provide confused deputy protection on its own.

### Data key caching
<a name="microvms-encryption-data-key-caching"></a>

To reduce AWS KMS call volume and improve availability, Lambda MicroVMs can cache the key material that protects the run hook payload. Cached key material is never shared between principals. The image environment variables and the MicroVM image are not cached: each request that reads them calls AWS KMS, and your key policy is evaluated at that moment.

For the run hook payload, revoking key access is therefore not an immediate containment mechanism: in-flight work can continue using cached material for an unspecified period. A key-policy change or a key disable takes effect on the next refresh.

When you perform an action that makes the KMS key unusable, there is no effect on running or suspended MicroVMs. This is because Lambda uses the data key, not the KMS key, to encrypt and decrypt snapshots.

### When the customer managed key is unavailable
<a name="microvms-encryption-key-unavailable"></a>

If the key an image or MicroVM depends on is disabled, scheduled for deletion, or has its access revoked, Lambda MicroVMs can no longer decrypt your data. Operations that read the image environment variables or the MicroVM image fail on the next request; operations that use cached run hook payload material fail once the cache refreshes. New image builds and MicroVM launches that need the key then fail with a non-retryable AWS KMS error. Restoring access to the key lets subsequent operations succeed again.

**Important**  
Deleting a KMS key that in-use images or MicroVMs still depend on permanently prevents Lambda MicroVMs from building or launching them. Before you disable or delete a key, confirm that no image version or running MicroVM still depends on it.

### Error behavior
<a name="microvms-encryption-errors"></a>

Lambda MicroVMs validates the AWS KMS key when you create or update an image or run a MicroVM. The following errors can occur:
+ **Validation error** – The key ARN is invalid or references a key that is disabled, in a different Region, or not a symmetric encryption key.
+ **Access denied error** – The calling principal or the Lambda service principal does not have the required AWS KMS permissions on the key, or the key does not exist. AWS KMS does not distinguish a key you cannot see from one that is not there, so both return access denied.

## Monitoring Lambda MicroVMs interaction with AWS KMS
<a name="microvms-encryption-monitoring"></a>

You can use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) to track the AWS KMS requests that Lambda MicroVMs makes on your behalf when you use a customer managed key with a MicroVM. For information about finding AWS KMS events in your CloudTrail logs, see [Searching CloudTrail logs for AWS KMS API calls](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html#searching-kms-ct) in the *AWS Key Management Service Developer Guide*.

To confirm that Lambda MicroVMs is using your key as intended, look for these fields in each event:
+ `eventSource`: `kms.amazonaws.com`
+ `userIdentity.invokedBy`: `lambda.amazonaws.com`
+ `requestParameters.encryptionContext`: contains `aws:lambda:MicrovmImageArn` with the image ARN.

The following table lists the AWS KMS events that Lambda MicroVMs generates.


| eventName | When it occurs | Values to audit | 
| --- | --- | --- | 
| DescribeKey | When you create or update an image, or run a MicroVM, with a customer managed key. | userIdentity is the calling principal. No encryption context (metadata operation). | 
| GenerateDataKey | When you create or update an image, and when Lambda MicroVMs builds it. Lambda MicroVMs generates the data keys that encrypt the image environment variables and the image. On create or update it also issues two dry-run GenerateDataKey calls before it stores anything: one using your credentials, to confirm you can use the KMS key, and one as the Lambda service principal, to confirm that the service principal can use the KMS key to build the image. | userIdentity is the principal that created the image for your dry run and for the environment-variable data key, and the Lambda service principal for its dry run and for the image data key. encryptionContext contains aws:lambda:MicrovmImageArn, plus aws-crypto-public-key on the environment-variable data key. | 
| GenerateDataKeyWithoutPlaintext | When you first run a MicroVM to encrypt the run hook payload. | userIdentity is the principal that ran the MicroVM. encryptionContext contains aws:lambda:MicrovmImageArn, plus additional pairs that Lambda MicroVMs adds. | 
| ReEncrypt | When Lambda MicroVMs creates the key material that protects the run hook payload, and when it later rotates that material. | userIdentity is the principal that ran the MicroVM when the material is created, or the Lambda service principal when it is rotated. sourceEncryptionContext and destinationEncryptionContext contain aws:lambda:MicrovmImageArn. | 
| Decrypt | When Lambda MicroVMs builds an image, launches a MicroVM, or a caller reads or updates an image version's environment variables. On create or update of an image, and on an image-version update, it also issues a dry-run Decrypt using your credentials before it changes anything. When the image has environment variables, create and update also issue a dry-run Decrypt as the Lambda service principal. A MicroVM launch produces two Decrypt events: one for the image's data key and one for the run hook payload. | userIdentity is the Lambda service principal for the image build, for its dry run, and for the image's data key at launch. It is the calling principal for your dry runs, for image-version reads and updates, and for the run hook payload at launch. encryptionContext contains aws:lambda:MicrovmImageArn with the image ARN. | 

Because Lambda MicroVMs caches the run hook payload's key material, you may see fewer `GenerateDataKeyWithoutPlaintext` events than you have MicroVMs.

## Related encryption topics
<a name="microvms-encryption-related"></a>
+ [Data encryption at rest for Lambda](security-encryption-at-rest.md)
+ [Encrypting AWS Lambda durable execution data](durable-encryption.md)
+ [Encryption at rest for Web Functions](web-functions-encryption.md)
+ [Security and permissions](microvms-security.md)