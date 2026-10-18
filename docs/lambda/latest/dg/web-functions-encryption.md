

# Encryption at rest for Web Functions
<a name="web-functions-encryption"></a>

AWS Lambda encrypts the data for your Lambda Web Functions at rest on the server side. This page explains the encryption options available to you and how to configure a customer managed key.

## Options for encryption at rest
<a name="web-functions-encryption-options"></a>

Encryption at rest is always on. Lambda encrypts your Web Function code artifact and environment variables on the server side, and you cannot turn this encryption off. By default, Lambda uses an AWS owned key. You can configure a customer managed key instead.

You have two options for the AWS KMS key that protects your data:

**AWS owned key (default)**  
By default, Lambda encrypts your data with an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk). AWS owns and manages this key. You cannot view, manage, or audit its use. If this default behavior suits your needs, no additional setup is required.

**Customer managed key**  
You can optionally configure your own AWS KMS customer managed key. Use a customer managed key when you need to control key rotation, audit key use through CloudTrail, manage key access through a key policy, or meet organizational compliance requirements. With a customer managed key, only principals you authorize can access the encrypted code and environment variables. Customer managed keys incur AWS KMS charges. For more information, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/).

## Encrypting data at rest using a customer managed key
<a name="web-functions-encryption-cmk"></a>

The following sections explain how Web Functions use a customer managed key, how to configure the key and its permissions, and how to scope down access to it.

### How Web Functions use a customer managed key
<a name="web-functions-encryption-how-it-works"></a>

When you specify a customer managed key, Lambda uses [envelope encryption](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping). This means that Lambda encrypts the revision's data with a data key, and your KMS key encrypts that data key. Lambda gets the data key from AWS KMS and decrypts it with your KMS key when it needs to read the data. Only principals with access to the KMS key can access the revision's code and environment variables.

Lambda encrypts the following Web Function resources with your customer managed key:


| Resource | What is encrypted | 
| --- | --- | 
| Revision | The code artifact built from your Amazon S3 deployment package, and the revision's environment variables. | 

Lambda doesn't use AWS KMS grants for Web Functions. Access is authorized through the key policy and the calling principal's IAM permissions.

Lambda calls AWS KMS while creating and launching revision resources and can cache decrypted material in active execution environments. Revoking key access is not an immediate traffic-containment mechanism because existing environments can continue using cached material for an unspecified period.

After a key-policy change, test the expected behavior and monitor revision and endpoint health. For emergency containment, stop routing traffic to affected revisions or disable the endpoint rather than relying only on key revocation.

Lambda sets the following encryption context on all AWS KMS operations for Web Functions:
+ `aws:lambda:WebFunctionRevisionArn` – The Amazon Resource Name (ARN) of the Web Function revision.

You can use this encryption context in key policies to scope access to specific Web Functions or revisions. For more information, see [Scoping down access to your KMS key](#web-functions-encryption-scope-down).

### Configuring a customer managed key
<a name="web-functions-encryption-key-requirements"></a>

The AWS KMS key must be a symmetric encryption key (key spec `SYMMETRIC_DEFAULT`, key usage `ENCRYPT_DECRYPT`). You can't use asymmetric keys.

Web Functions support multi-Region keys. The type of key you need depends on your endpoint configuration:
+ **HomeRegion endpoint** – You can use a single-Region key or a multi-Region key.
+ **MultiRegion or PerRegion endpoint** – You must use a multi-Region key with replicas in every AWS Region that the endpoint serves. If a Region lacks a replica of the key, replication to that Region fails.

For information about creating multi-Region keys, see [Create multi-Region primary keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-primary-keys.html) in the *AWS Key Management Service Developer Guide*.

Because AWS KMS does not copy or synchronize key policies between related multi-Region keys, you must configure each key policy separately. Configure the key policy on the primary key and on every replica key. At minimum, every replica key's policy must allow the Lambda service principal to call `kms:Decrypt`. This permission allows Lambda to decrypt the data key in that Region. For more information, see [Authorizing use of multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-auth.html) in the *AWS Key Management Service Developer Guide*.

**Note**  
When you create multi-Region replica keys, they can take from a few seconds to a few minutes to become available in all Regions. Confirm that the replica key is available in every target Region before you create the revision or endpoint.

### Configuring permissions to use a customer managed key
<a name="web-functions-encryption-permissions"></a>

To create a revision with a customer managed key, you need the following permissions on the AWS KMS key:
+ `kms:DescribeKey` – Required when you create a Web Function or revision with the key.
+ `kms:GenerateDataKey` – Lambda calls this operation to generate the data key that encrypts the revision's code artifact and environment variables.
+ `kms:Decrypt` – Lambda calls this operation to validate that the key is usable when you create the revision. Principals that read a revision with `GetWebFunctionRevision` also need `kms:Decrypt` on the key to see its environment variables.

The creation request fails if the key is missing, disabled, not a symmetric encryption key, or inaccessible with the required permissions.

**Note**  
You do not need `kms:Encrypt` permission. Lambda uses envelope encryption with `GenerateDataKey`, which returns both a plaintext and encrypted copy of the data key without requiring a separate encrypt call.

The AWS KMS key policy must also allow the Lambda service principal (`lambda.amazonaws.com`) to call `kms:Decrypt`. Lambda uses this permission to decrypt the data key when it launches execution environments for the revision. The service principal does not need `kms:DescribeKey`. The principal that creates the Web Function or revision needs that permission.

#### Example key policy
<a name="web-functions-encryption-key-policy"></a>

The following key policy contains the three statements that Web Functions require, each scoped down with the conditions described in [Scoping down access to your KMS key](#web-functions-encryption-scope-down). The first statement grants the Lambda service principal the permissions it needs when it launches execution environments. The second and third grant the principal that creates revisions the permissions it needs at creation time.

`kms:DescribeKey` is in a separate statement because it is a metadata operation that carries no encryption context. An encryption context condition would never match a `DescribeKey` request, so that condition applies only to the statement that grants `kms:GenerateDataKey` and `kms:Decrypt`.

This example shows only the statements that Lambda requires for Web Functions. Add these statements to your existing key policy rather than replacing it, and keep the statements that grant your administrators access to manage the key.

**Example Key policy for Web Function encryption**  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Allow Lambda to decrypt the data key for Web Function revisions",
            "Effect": "Allow",
            "Principal": { "Service": "lambda.amazonaws.com" },
            "Action": "kms:Decrypt",
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:EncryptionContext:aws:lambda:WebFunctionRevisionArn": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:web-function/{{my-function}}/revision/*",
                    "aws:SourceArn": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:web-function/{{my-function}}/revision/*"
                }
            }
        },
        {
            "Sid": "Allow the revision creator to generate and validate data keys",
            "Effect": "Allow",
            "Principal": { "AWS": "arn:aws:iam::{{111122223333}}:role/{{MyWebFunctionDeployRole}}" },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:EncryptionContext:aws:lambda:WebFunctionRevisionArn": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:web-function/{{my-function}}/revision/*"
                },
                "StringEquals": {
                    "kms:ViaService": "lambda.{{us-east-1}}.amazonaws.com"
                }
            }
        },
        {
            "Sid": "Allow the revision creator to describe the key",
            "Effect": "Allow",
            "Principal": { "AWS": "arn:aws:iam::{{111122223333}}:role/{{MyWebFunctionDeployRole}}" },
            "Action": "kms:DescribeKey",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "lambda.{{us-east-1}}.amazonaws.com"
                }
            }
        }
    ]
}
```

For more information about AWS KMS key policies, see [Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *AWS Key Management Service Developer Guide*.

### Creating a Web Function revision with a customer managed key
<a name="web-functions-encryption-specifying-key"></a>

To encrypt a revision with a customer managed key, specify the key ARN in the `kmsKeyArn` parameter of the revision configuration. You can set this parameter when you call [CreateWebFunction](https://docs.aws.amazon.com/lambda/latest/lambda-web/API_CreateWebFunction.html) or [CreateWebFunctionRevision](https://docs.aws.amazon.com/lambda/latest/lambda-web/API_CreateWebFunctionRevision.html). If you omit `kmsKeyArn`, Lambda encrypts the revision with the AWS owned key.

**To create a Web Function with a customer managed key (AWS CLI)**
+ Run the following command to create a Web Function with a customer managed key.

  ```
  aws lambda-web create-web-function \
      --function-name {{my-web-app}} \
      --revision-config '{
        "kmsKeyArn": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{key-id}}",
        "buildConfig": {
          "codeConfig": {
            "s3Object": { "bucket": "{{amzn-s3-demo-bucket}}", "key": "{{my-app.zip}}" }
          },
          "runtimeConfig": { "runtime": "nodejs24.x" }
        },
        "serviceConfig": {
          "executionRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-web-function-role}}"
        }
      }' \
      --endpoint-config '{
        "endpointName": "{{my-endpoint}}",
        "endpointType": "HomeRegion",
        "authType": "ApplicationManaged"
      }'
  ```

### Changing the encryption configuration of an existing Web Function
<a name="web-functions-encryption-changing-key"></a>

The `kmsKeyArn` parameter is fixed for the life of a revision. Because revisions are immutable, you cannot change the key that protects an existing revision. To change the encryption configuration, create a new revision that specifies the new key, and then route traffic to that revision.

Web Functions support the following key transitions:
+ **AWS owned key to customer managed key** – Create a new revision that specifies `kmsKeyArn`.
+ **One customer managed key to a different customer managed key** – Create a new revision that specifies the new key ARN.
+ **Customer managed key to AWS owned key** – Create a new revision without `kmsKeyArn`. Lambda then protects that revision with the AWS owned key, which is the default.

Lambda does not re-encrypt existing revisions when you create a new revision with a different key. Each revision remains encrypted with the key that you specified when you created it. This means that as long as an earlier revision can still receive traffic, its original key must remain enabled and accessible to the Lambda service principal. Before you disable or delete a key, confirm that no revision encrypted with that key is still referenced by an endpoint's revision weights.

**To create a new revision with a different customer managed key (AWS CLI)**

1. Run the following command to create a revision that uses a different key.

   ```
   aws lambda-web create-web-function-revision \
       --function-name {{my-web-app}} \
       --kms-key-arn arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{new-key-id}} \
       --build-config '{
         "codeConfig": { "s3Object": { "bucket": "{{my-bucket}}", "key": "{{my-app-v2.zip}}" } },
         "runtimeConfig": { "runtime": "nodejs24.x" }
       }' \
       --service-config '{
         "executionRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-web-function-role}}"
       }'
   ```

1. Update the endpoint's revision weights to route traffic to the new revision. For more information, see [Deployment patterns](web-functions-deployment.md).

### Scoping down access to your KMS key
<a name="web-functions-encryption-scope-down"></a>

The key policy in [Example key policy](#web-functions-encryption-key-policy) restricts access with the following condition keys. Each one limits how the key can be used, so that access to the key is no broader than the Web Function needs.

#### Encryption context
<a name="web-functions-encryption-scope-down-context"></a>

Lambda sets the encryption context `aws:lambda:WebFunctionRevisionArn` on every AWS KMS request for a revision. Use a `StringLike` condition on `kms:EncryptionContext:aws:lambda:WebFunctionRevisionArn` to restrict the key to revisions of a specific Web Function. Apply this condition to both the creator statement and the Lambda service principal statement.

Do not apply this condition to a statement that grants `kms:DescribeKey`. That operation carries no encryption context, so the condition would deny it.

The following example shows the creator statement with the encryption context condition.

```
{
    "Sid": "Allow the revision creator to generate and validate data keys",
    "Effect": "Allow",
    "Principal": { "AWS": "arn:aws:iam::{{111122223333}}:role/{{MyWebFunctionDeployRole}}" },
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
        "StringLike": {
            "kms:EncryptionContext:aws:lambda:WebFunctionRevisionArn": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:web-function/{{my-function}}/revision/*"
        }
    }
}
```

#### kms:ViaService condition
<a name="web-functions-encryption-scope-down-viaservice"></a>

The `kms:ViaService` condition restricts the key so that only requests that Lambda makes on your behalf can use it. The value is Region-specific: `lambda.{{us-east-1}}.amazonaws.com`.

With this condition, AWS KMS denies direct calls made with the same credentials (for example, running `aws kms generate-data-key` yourself), but creating a Web Function succeeds because Lambda makes the AWS KMS calls for you.

AWS KMS does not share key policies between related multi-Region keys. Each replica key has its own policy. When you use the `kms:ViaService` condition with a multi-Region key, use the Regional service name that matches each key's Region (for example, `lambda.us-east-1.amazonaws.com` in the us-east-1 key policy and `lambda.us-west-2.amazonaws.com` in the us-west-2 replica key policy). You can also list multiple Regional values in one condition because `StringEquals` accepts an array of values.

The following example shows the creator statement with both the `kms:ViaService` condition and the encryption context condition.

```
{
    "Sid": "Allow the revision creator to generate and validate data keys",
    "Effect": "Allow",
    "Principal": { "AWS": "arn:aws:iam::{{111122223333}}:role/{{MyWebFunctionDeployRole}}" },
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
        "StringLike": {
            "kms:EncryptionContext:aws:lambda:WebFunctionRevisionArn": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:web-function/{{my-function}}/revision/*"
        },
        "StringEquals": {
            "kms:ViaService": "lambda.{{us-east-1}}.amazonaws.com"
        }
    }
}
```

#### Confused deputy protection
<a name="web-functions-encryption-scope-down-confused-deputy"></a>

The confused deputy problem occurs when an entity without permission to perform an action coerces a more-privileged entity to perform it. Because the Lambda service principal can use your customer managed key, restrict that access to the Web Function revisions that you own. For more information, see [The confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) in the *IAM User Guide*.

When Lambda calls AWS KMS with its own service credentials to launch an execution environment, it sends the revision ARN as the source ARN and your AWS account ID as the source account. Use the [aws:SourceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) condition key on the Lambda service principal statement to restrict the key to revisions of a specific Web Function.

```
{
    "Sid": "Allow Lambda to decrypt the data key for Web Function revisions",
    "Effect": "Allow",
    "Principal": { "Service": "lambda.amazonaws.com" },
    "Action": "kms:Decrypt",
    "Resource": "*",
    "Condition": {
        "StringLike": {
            "aws:SourceArn": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:web-function/{{my-function}}/revision/*"
        }
    }
}
```

To restrict the key to your account instead of to a specific Web Function, use the [aws:SourceAccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) condition key with your AWS account ID.

Apply this condition to the Lambda service principal statement. The `kms:ViaService` condition described in [kms:ViaService condition](#web-functions-encryption-scope-down-viaservice) restricts which service can use the key, but it does not provide confused deputy protection.

### Error behavior
<a name="web-functions-encryption-errors"></a>

Lambda validates the AWS KMS key when you create a revision. The following errors can occur at creation time:
+ **Validation error** – The key ARN is invalid, the key does not exist, the key is disabled, or the key is not a symmetric encryption key.
+ **Access denied error** – The calling principal or the Lambda service principal does not have the required AWS KMS permissions on the key.

**Do not disable or revoke access to an active revision's key**  
If you disable the AWS KMS key or revoke the Lambda service principal's access after a revision is `Active`, Lambda can no longer decrypt the data key. This prevents Lambda from launching new execution environments for that revision, which breaks invocations. Also do not delete replica keys in Regions where the revision is still deployed. This has the same effect (Lambda cannot launch new execution environments in that Region). To restore service, create a new revision with an accessible key, or re-enable the original key and restore the key policy.

### Encryption with MultiRegion and PerRegion endpoints
<a name="web-functions-encryption-multi-region"></a>

For Web Functions with MultiRegion or PerRegion endpoints, Lambda checks key availability in each Region during replication. If the multi-Region key replica is missing or inaccessible in a target Region, replication fails only for that Region. Other Regions continue to operate normally.

You can view each Region's state and update status by calling `GetWebFunctionEndpoint`. Each Region's entry in `regionalEndpoints` contains `state` and `stateReason` (the Region's deployment state) and `updateStatus` and `updateStatusReason` (the result of the most recent update). The behavior differs depending on whether the endpoint is being created or updated:
+ **During endpoint creation** – The Region's entry in `regionalEndpoints` shows a `state` of `Failed` with a `stateReason` that describes the key issue. The overall endpoint `state` also shows `Failed`, and its `stateReason` directs you to the Regional entries.
+ **During an endpoint update** – The Region's `updateStatus` shows `Failed` with an `updateStatusReason` that describes the key issue. The overall endpoint `updateStatus` also shows `Failed`, and its `updateStatusReason` directs you to the Regional entries.

To resolve a failed Region, create a key replica in that Region or restore access to the existing replica, and then update the endpoint to retry replication.

## Monitoring Web Functions interaction with AWS KMS
<a name="web-functions-encryption-monitoring"></a>

You can use CloudTrail to track the AWS KMS requests that Lambda makes on your behalf when you use a customer managed key with a Web Function. For information about finding AWS KMS events in your CloudTrail logs, see [Searching CloudTrail logs for AWS KMS API calls](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html#searching-kms-ct) in the *AWS Key Management Service Developer Guide*.

The following table lists the AWS KMS events that Web Functions generate and the values you can audit in each event.


| eventName | When it occurs | Values to audit | 
| --- | --- | --- | 
| DescribeKey | When you create a Web Function or revision with a customer managed key. | userIdentity is the IAM principal that created the revision. This event has no encryption context, because DescribeKey is a metadata operation. | 
| GenerateDataKey | When you create a Web Function or revision. Lambda generates the data key that encrypts the revision's code artifact and environment variables. | userIdentity is the IAM principal that created the revision. encryptionContext contains aws:lambda:WebFunctionRevisionArn. | 
| Decrypt | When you create a Web Function or revision, Lambda validates key access. Lambda also calls this operation when it deploys the revision to a replica Region, when it launches a new execution environment, and when a caller reads the revision's environment variables with GetWebFunctionRevision. | For creation-time calls, userIdentity is the IAM principal that created the revision. Lambda also makes a dry-run Decrypt call as lambda.amazonaws.com to confirm the service principal can use the key. For runtime calls, userIdentity is the Lambda service principal (lambda.amazonaws.com). For GetWebFunctionRevision, Lambda calls Decrypt with the caller's credentials. encryptionContext contains aws:lambda:WebFunctionRevisionArn. | 

The `GenerateDataKey` and `Decrypt` events include the encryption context `aws:lambda:WebFunctionRevisionArn` with the revision ARN. Use this value to identify AWS KMS requests for a specific Web Function revision.