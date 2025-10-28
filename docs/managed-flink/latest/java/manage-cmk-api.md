Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Managing CMK using APIs

This topic describes how to create, and update your KMS CMKs using Amazon MSF APIs. To follow the procedures described in this topic, you must have permission to manage the KMS key and the Amazon MSF application. The procedures in this topic use a permissive key policy, which is for demonstration and testing purposes only. We **don't recommend** using such a permissive key policy for production workloads. In real-life scenarios for production workloads, roles, permissions, and workflows are isolated.

###### On this page

- [Create and assign KMS keys](#create-assign-cmk-api "#create-assign-cmk-api")
- [Update an existing application to use CMK](#update-existing-app-use-cmk-api "#update-existing-app-use-cmk-api")
- [Revert from CMK to AWS owned key](#revert-cmk-to-aok-api "#revert-cmk-to-aok-api")

## Create and assign KMS keys

Before you start, create a KMS key. For information about creating a KMS key, see [Create a KMS key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

###### In this section

- [Create a KMS key policy](#create-cmk-kms-key-policy "#create-cmk-kms-key-policy")
- [Application lifecycle operator (API caller) permissions](#create-cmk-kms-api-caller-permissions "#create-cmk-kms-api-caller-permissions")

### Create a KMS key policy

To use CMK in Amazon MSF, you must add the following service principals to your key policy: `kinesisanalytics.amazonaws.com` and `infrastructure.kinesisanalytics.amazonaws.com`. Amazon MSF uses these service principals for validation and resource access. If you don't include these service principals, Amazon MSF rejects the request.

The following KMS key policy enables Amazon MSF to use a CMK for the application, `MyCmkApplication`. This policy grants necessary permissions to both the `Operator` role and Amazon MSF service principals, `kinesisanalytics.amazonaws.com` and `infrastructure.kinesisanalytics.amazonaws.com`, to perform the following operations:

- Describe the CMK
- Encrypt the application data
- Decrypt the application data
- Create grants for the key

The following example uses IAM roles. You can create the key policy for the KMS key using the following example as template, but make sure to do the following:

- Replace `arn:aws:iam::`123456789012`:role/Operator` with the `Operator` role. You must create the `Operator` role or user before creating the key policy. Failing to do this will cause the failure of your request.
- Replace `arn:aws:kinesisanalytics:us-east-1:`123456789012`:application/`MyCmkApplication`` with your application's ARN.
- Replace `kinesisanalytics.`us-east-1`.amazonaws.com` with a service value for the corresponding Region.
- Replace `123456789012` with your account idKey policy for CMK.
- Add additional policy statements to [allow key administrators to administer the KMS key](../../../kms/latest/developerguide/key-policy-default.md#key-policy-default-allow-administrators "../../../kms/latest/developerguide/key-policy-default.md#key-policy-default-allow-administrators"). Failing to do this will cause loss of access to manage the key.

The following key policy statements are large because they are intended to be explicit and show the conditions that each action requires.

```
{
    "Version":"2012-10-17",
    "Id": "MyMsfCmkApplicationKeyPolicy",
    "Statement": [
        {
            "Sid": "AllowOperatorToDescribeKey",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`123456789012`:role/`Operator`"
            },
            "Action": "kms:DescribeKey",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "kinesisanalytics.`us-east-1`.amazonaws.com"
                }
            }
        },
        {
            "Sid": "AllowOperatorToConfigureAppToUseKeyForApplicationState",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`123456789012`:role/`Operator`"
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey",
                "kms:GenerateDataKeyWithoutPlaintext"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:EncryptionContext:aws:kinesisanalytics:arn":
                        "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/`MyCmkApplication`",
                    "kms:ViaService": "kinesisanalytics.`us-east-1`.amazonaws.com"
                }
            }
        },
        {
            "Sid": "AllowOperatorToConfigureAppToCreateGrantForRunningState",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`123456789012`:role/`Operator`"
            },
            "Action": "kms:CreateGrant",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:EncryptionContext:aws:kinesisanalytics:arn":
                        "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/`MyCmkApplication`",
                    "kms:ViaService": "kinesisanalytics.`us-east-1`.amazonaws.com",
                    "kms:GrantConstraintType": "EncryptionContextSubset"
                },
                "ForAllValues:StringEquals": {
                    "kms:GrantOperations": "Decrypt"
                }
            }
        },
        {
            "Sid": "AllowMSFServiceToDescribeKey",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "kinesisanalytics.amazonaws.com",
                    "infrastructure.kinesisanalytics.amazonaws.com"
                ]
            },
            "Action": "kms:DescribeKey",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceArn":
                        "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/`MyCmkApplication`",
                    "aws:SourceAccount": "`123456789012`"
                }
            }
        },
        {
            "Sid": "AllowMSFServiceToGenerateDataKeyForDurableState",
            "Effect": "Allow",
            "Principal": {
                "Service": "kinesisanalytics.amazonaws.com"
            },
            "Action": [
                "kms:GenerateDataKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceArn":
                        "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/`MyCmkApplication`",
                    "kms:EncryptionContext:aws:kinesisanalytics:arn":
                        "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/`MyCmkApplication`",
                    "aws:SourceAccount": "`123456789012`"
                }
            }
        },
        {
            "Sid": "AllowMSFServiceToDecryptForDurableState",
            "Effect": "Allow",
            "Principal": {
                "Service": "kinesisanalytics.amazonaws.com"
            },
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:EncryptionContext:aws:kinesisanalytics:arn":
                        "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/`MyCmkApplication`"
                }
            }
        },
        {
            "Sid": "AllowMSFServiceToUseKeyForRunningState",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "infrastructure.kinesisanalytics.amazonaws.com"
                ]
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKeyWithoutPlaintext"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:EncryptionContext:aws:kinesisanalytics:arn":
                        "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/`MyCmkApplication`"
                }
            }
        },
        {
            "Sid": "AllowMSFServiceToCreateGrantForRunningState",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "infrastructure.kinesisanalytics.amazonaws.com"
                ]
            },
            "Action": "kms:CreateGrant",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:EncryptionContext:aws:kinesisanalytics:arn":
                        "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/`MyCmkApplication`",
                    "kms:GrantConstraintType": "EncryptionContextSubset"
                },
                "ForAllValues:StringEquals": {
                    "kms:GrantOperations": "Decrypt"
                }
            }
        }
    ]
}
```

### Application lifecycle operator (API caller) permissions

The following IAM policy ensures that the application lifecycle operator has the necessary permissions to assign a KMS key to the application, `MyCmkApplication`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowMSFAPICalls",
 "Effect": "Allow",
 "Action": "kinesisanalytics:*",
 "Resource": "*"
 },
 {
 "Sid": "AllowPassingServiceExecutionRole",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`123456789012`:role/`MyCmkApplicationRole`"
 },
 {
 "Sid": "AllowDescribeKey",
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`123456789012`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "kinesisanalytics.`us-east-1`.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AllowMyCmkApplicationKeyOperationsForDurableState",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`123456789012`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "kinesisanalytics.`us-east-1`.amazonaws.com",
 "kms:EncryptionContext:aws:kinesisanalytics:arn":
 "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/`MyCmkApplication`"
 }
 }
 },
 {
 "Sid": "AllowMyCmkApplicationKeyOperationsForRunningState",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKeyWithoutPlaintext"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`123456789012`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "kinesisanalytics.`us-east-1`.amazonaws.com",
 "kms:EncryptionContext:aws:kinesisanalytics:arn":
 "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/`MyCmkApplication`"
 }
 }
 },
 {
 "Sid": "AllowMyCmkApplicationCreateGrantForRunningState",
 "Effect": "Allow",
 "Action": "kms:CreateGrant",
 "Resource": "arn:aws:kms:`us-east-1`:`123456789012`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`",
 "Condition": {
 "ForAllValues:StringEquals": {
 "kms:GrantOperations": "Decrypt"
 },
 "StringEquals": {
 "kms:ViaService": "kinesisanalytics.`us-east-1`.amazonaws.com",
 "kms:EncryptionContext:aws:kinesisanalytics:arn":
 "arn:aws:kinesisanalytics:`us-east-1`:`123456789012`:application/`MyCmkApplication`",
 "kms:GrantConstraintType": "EncryptionContextSubset"
 }
 }
 }
 ]
}`

```

## Update an existing application to use CMK

In Amazon MSF, you can apply a CMK policy to an existing application that uses AWS owned keys (AOKs).

By default, Amazon MSF uses AOKs to encrypt all your data in ephemeral (running application storage) and durable (durable application storage) storage. This means all data subject to a Flink [checkpoint](how-fault.md "how-fault.md") or [snapshot](how-snapshots.md "how-snapshots.md") are encrypted using AOKs by default. When you replace the AOK with a CMK, new checkpoints and snapshots are encrypted with CMK. However, historic snapshots will remain encrypted with the AOK.

###### To update an existing application to use CMK

1. Create a JSON file with the following configuration.

Make sure that you replace the value of `CurrentApplicationVersionId` to the current version number of the application. You can get the current version number of your application, using [DescribeApplication](../apiv2/API_DescribeApplication.md "../apiv2/API_DescribeApplication.md").

In this JSON configuration, remember to replace the `sample` values with the actual values.

```
{
    "ApplicationName": "`MyCmkApplication`",
    "CurrentApplicationVersionId": `1`,
    "ApplicationConfigurationUpdate": {
        "ApplicationEncryptionConfigurationUpdate": {
            "KeyTypeUpdate": "CUSTOMER_MANAGED_KEY",
            "KeyIdUpdate": "`arn:aws:kms:us-east-1:`123456789012`:key/`1234abcd-12ab-34cd-56ef-1234567890ab``"
        }
    }
}
```

2. Save this file. For example, save it with the name `enable-cmk.json`.
3. Run the [update-application](../../../cli/latest/reference/kinesisanalyticsv2/update-application.md "../../../cli/latest/reference/kinesisanalyticsv2/update-application.md") AWS CLI command as shown in the following example. In this command, provide the JSON configuration file you created in the previous steps as the file argument.

```
aws kinesisanalyticsv2 update-application \
    --cli-input-json file://`enable-cmk.json`
```

The preceding configuration is accepted to update the application for using CMK only if the following conditions are met:

- API caller has a policy statement that allows access to the key.
- Key policy has a policy statement that allows API caller access to the key.
- Key policy has a policy statement that allows the Amazon MSF service principal, for example, `kinesisanalytics.amazonaws.com` access to the key.

## Revert from CMK to AWS owned key

###### To revert from CMK to an AOK

1. Create a JSON file with the following configuration.

In this JSON configuration, remember to replace the `sample` values with the actual values.

```
{
    "ApplicationName": "`MyCmkApplication`",
    "CurrentApplicationVersionId": `1`,
    "ApplicationConfigurationUpdate": {
        "ApplicationEncryptionConfigurationUpdate": {
            "KeyTypeUpdate": "AWS_OWNED_KEY"
        }
    }
}
```

2. Save this file. For example, save it with the name `disable-cmk.json`.
3. Run the [update-application](../../../cli/latest/reference/kinesisanalyticsv2/update-application.md "../../../cli/latest/reference/kinesisanalyticsv2/update-application.md") AWS CLI command as shown in the following example. In this command, provide the JSON configuration file you created in the previous steps as the file argument.

```
aws kinesisanalyticsv2 update-application \
    --cli-input-json file://`disable-cmk.json`
```
