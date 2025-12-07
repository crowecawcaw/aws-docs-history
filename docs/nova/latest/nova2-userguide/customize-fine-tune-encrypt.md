# Encryption of Amazon Nova model customization jobs and artifacts

For information regarding encryption of your model customization jobs and artifacts in Amazon Bedrock, see [Encryption of model customization jobs and artifacts](../../../bedrock/latest/userguide/encryption-custom-job.md "../../../bedrock/latest/userguide/encryption-custom-job.md").

###### Topics

- [Permissions and key policies for custom Amazon Nova models](#customize-fine-tune-encrypt-allow "#customize-fine-tune-encrypt-allow")
- [Set up key permissions for encrypting and invoking custom models](#customize-fine-tune-encrypt-permissions "#customize-fine-tune-encrypt-permissions")

## Permissions and key policies for custom Amazon Nova models

The following statements are necessary to establish permissions for your KMS key.

**PermissionsModelCustomization statement**

In the `Principal` field, add accounts that you want to allow the `Decrypt`, `GenerateDataKey`, `DescribeKey` and `CreateGrant` operations to the list that the `AWS` subfield maps to. If you use the `kms:ViaService` condition key, you can add a line for each region, or use `*` in place of `${region}` to allow all regions that support Amazon Bedrock.

```
{
    "Sid": "PermissionsModelCustomization",
    "Effect": "Allow",
    "Principal": {
        "AWS": [
            "arn:aws:iam::${account-id}:role/${customization-role}"
        ]
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:DescribeKey",
        "kms:CreateGrant"
    ],
    "Resource": "*",
    "Condition": {
        "StringLike": {
            "kms:ViaService": [
                "bedrock.${region}.amazonaws.com"
            ]
        }
    }
}
```

**PermissionsModelInvocation statement**

In the `Principal` field, add accounts that you want to allow the `Decrypt` and `GenerateDataKey` operations to the list that the `AWS` subfield maps to. If you use the `kms:ViaService` condition key, you can add a line for each region, or use `*` in place of `${region}` to allow all regions that support Amazon Bedrock.

```
{
    "Sid": "PermissionsModelInvocation",
    "Effect": "Allow",
    "Principal": {
        "AWS": [
            "arn:aws:iam::${account-id}:user/${invocation-role}"
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
                "bedrock.${region}.amazonaws.com"
            ]
        }
    }
}
```

**PermissionsNovaProvisionedThroughput statement**

When you create provisioned throughput for your custom Amazon Nova model, Amazon Bedrock performs inference and deployment optimizations on the model. In this process, Amazon Bedrock uses the same KMS key used to create the custom model to maintain the highest level of security as that of the custom model itself.

```
{
    "Sid": "PermissionsNovaProvisionedThroughput",
    "Effect": "Allow",
    "Principal": {
        "Service": [
            "bedrock.amazonaws.com"
        ]
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
    ],
    "Resource": "*",
    "Condition": {
        "ForAnyValue:StringEquals": {
            "kms:EncryptionContextKeys": "aws:bedrock:custom-model"
        }
    }
 }
```

## Set up key permissions for encrypting and invoking custom models

If you plan to encrypt a model that you customize with a KMS key, the key policy for the key will depend on your use case. Expand the section that corresponds to your use case:

If the roles that will invoke the custom model are the same as the roles that will customize the model, you only need the `PermissionsModelCustomization` and `PermissionsNovaProvisionedThroughput` statements from permission statements.

1. In the `Principal` field, add accounts that you want to allow to customize and invoke the custom model to the list that the `AWS` subfield maps to in the `PermissionsModelCustomization` statement.
2. The `PermissionsNovaProvisionedThroughput` statement should be added by default to the key policy with `bedrock.amazonaws.com` as an allowed service principal with a condition that `kms:EncryptionContextKeys` are used.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "PermissionsCustomModelKey",
 "Statement": [
 {
 "Sid": "PermissionsModelCustomization",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:role/`customize-and-invoke-role`"
 ]
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:DescribeKey",
 "kms:CreateGrant"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "bedrock.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "PermissionsNovaProvisionedThroughput",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "bedrock.amazonaws.com"
 ]
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "kms:EncryptionContextKeys": "aws:bedrock:custom-model"
 }
 }
 }
 ]
}`

```

If the roles that will invoke the custom model are different from the role that will customize the model, you need all three of the permission statements. Modify the statements in the following policy template as follows:

1. In the `Principal` field, add accounts that you want to allow to only customize the custom model to the list that the `AWS` subfield maps to in the `PermissionsModelCustomization` statement.
2. In the `Principal` field, add accounts that you want to allow to only invoke the custom model to the list that the `AWS` subfield maps to in the `PermissionsModelInvocation` statement.
3. The `PermissionsNovaProvisionedThroughput` statement should be added by default to the key policy with `bedrock.amazonaws.com` as allowed service principal with a condition that `kms:EncryptionContextKeys` are used.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "PermissionsCustomModelKey",
 "Statement": [
 {
 "Sid": "PermissionsModelCustomization",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:user/`customization-role`"
 ]
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:DescribeKey",
 "kms:CreateGrant"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "bedrock.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "PermissionsModelInvocation",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:user/`invocation-role`"
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
 "bedrock.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "PermissionsNovaPermissionedThroughput",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "bedrock.amazonaws.com"
 ]
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "kms:EncryptionContextKeys": "aws:bedrock:custom-model"
 }
 }
 }
 ]
}`

```
