

# Managing CMK using APIs

This topic describes how to create, and update your KMS CMKs using Amazon MSF APIs. To follow the procedures described in this topic, you must have permission to manage the KMS key and the Amazon MSF application. The procedures in this topic use a permissive key policy, which is for demonstration and testing purposes only. We **don't recommend** using such a permissive key policy for production workloads. In real-life scenarios for production workloads, roles, permissions, and workflows are isolated.

**Topics**
+ [Create and assign KMS keys](#create-assign-cmk-api)
+ [Update an existing application to use CMK](#update-existing-app-use-cmk-api)
+ [Revert from CMK to AWS owned key](#revert-cmk-to-aok-api)
+ [Restore from an enhanced snapshot that uses a different key](#manage-cmk-api-restore-different-key)

## Create and assign KMS keys
<a name="create-assign-cmk-api"></a>

Before you start, create a KMS key. For information about creating a KMS key, see [Create a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.

**Topics**
+ [Create a KMS key policy](#create-cmk-kms-key-policy)
+ [Key policy for enhanced snapshot import and export](#create-cmk-kms-key-policy-snapshot-transfer)
+ [Application lifecycle operator (API caller) permissions](#create-cmk-kms-api-caller-permissions)

### Create a KMS key policy
<a name="create-cmk-kms-key-policy"></a>

To use CMK in Amazon MSF, you must add the following service principals to your key policy: `kinesisanalytics.amazonaws.com` and `infrastructure.kinesisanalytics.amazonaws.com`. Amazon MSF uses these service principals for validation and resource access. If you don't include these service principals, Amazon MSF rejects the request.

The following KMS key policy enables Amazon MSF to use a CMK for the application, {{MyCmkApplication}}. This policy grants necessary permissions to both the **Operator** role and Amazon MSF service principals, `kinesisanalytics.amazonaws.com` and `infrastructure.kinesisanalytics.amazonaws.com`, to perform the following operations:
+ Describe the CMK
+ Encrypt the application data
+ Decrypt the application data
+ Create grants for the key

The following example uses IAM roles. You can create the key policy for the KMS key using the following example as template, but make sure to do the following: 
+ Replace `arn:aws:iam::{{123456789012}}:role/Operator` with the **Operator** role. You must create the **Operator** role or user before creating the key policy. Failing to do this will cause the failure of your request.
+ Replace `arn:aws:kinesisanalytics:us-east-1:{{123456789012}}:application/{{MyCmkApplication}}` with your application's ARN.
+ Replace `kinesisanalytics.{{us-east-1}}.amazonaws.com` with a service value for the corresponding Region.
+ Replace {{123456789012}} with your account idKey policy for CMK.
+ Add additional policy statements to [allow key administrators to administer the KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#key-policy-default-allow-administrators). Failing to do this will cause loss of access to manage the key.

The following key policy statements are large because they are intended to be explicit and show the conditions that each action requires.

```json
{
    "Version":"2012-10-17",			 	 	 	 	 	 
    "Id": "MyMsfCmkApplicationKeyPolicy",
    "Statement": [
        {
            "Sid": "AllowOperatorToDescribeKey",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{123456789012}}:role/Operator"
            },
            "Action": "kms:DescribeKey",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "kinesisanalytics.{{us-east-1}}.amazonaws.com"
                }
            }
        },
        {
            "Sid": "AllowOperatorToConfigureAppToUseKeyForApplicationState",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{123456789012}}:role/Operator"
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
                        "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:application/{{MyCmkApplication}}",
                    "kms:ViaService": "kinesisanalytics.{{us-east-1}}.amazonaws.com"
                }
            }
        },
        {
            "Sid": "AllowOperatorToConfigureAppToCreateGrantForRunningState",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{123456789012}}:role/Operator"
            },
            "Action": "kms:CreateGrant",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:EncryptionContext:aws:kinesisanalytics:arn": 
                        "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:application/{{MyCmkApplication}}",
                    "kms:ViaService": "kinesisanalytics.{{us-east-1}}.amazonaws.com",
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
                        "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:application/{{MyCmkApplication}}",
                    "aws:SourceAccount": "{{123456789012}}"
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
                        "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:application/{{MyCmkApplication}}",
                    "kms:EncryptionContext:aws:kinesisanalytics:arn": 
                        "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:application/{{MyCmkApplication}}",
                    "aws:SourceAccount": "{{123456789012}}"
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
                        "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:application/{{MyCmkApplication}}"
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
                        "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:application/{{MyCmkApplication}}"
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
                        "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:application/{{MyCmkApplication}}",
                    "kms:GrantConstraintType": "EncryptionContextSubset"
                },
                "ForAllValues:StringEquals": {
                    "kms:GrantOperations": "Decrypt"
                }
            }
        },
        {
            "Sid": "OptionalAllowOperatorToUseKeyForImportedSnapshots",
            "Effect": "Allow",
            "Principal": { "AWS": "arn:aws:iam::{{123456789012}}:role/Operator" },
            "Action": [ "kms:Decrypt", "kms:GenerateDataKey" ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:EncryptionContext:aws:kinesisanalytics:arn": "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:snapshot/*"
                },
                "StringEquals": {
                    "kms:ViaService": "kinesisanalytics.{{us-east-1}}.amazonaws.com"
                }
            }
        },
        {
            "Sid": "OptionalAllowServiceToDescribeKeyForImportedSnapshots",
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
                "StringLike": {
                    "aws:SourceArn": "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:snapshot/*"
                },
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                }
            }
        },
        {
            "Sid": "OptionalAllowServiceToUseKeyForImportedSnapshots",
            "Effect": "Allow",
            "Principal": { "Service": "kinesisanalytics.amazonaws.com" },
            "Action": [ "kms:Decrypt", "kms:GenerateDataKey" ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:EncryptionContext:aws:kinesisanalytics:arn": "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:snapshot/*"
                }
            }
        }
    ]
}
```

The statements whose `Sid` starts with `Optional` are for imported enhanced snapshots. Keep them if you import enhanced snapshots with this key. Otherwise, remove them.

Replace the example values in the `aws:SourceArn`, `aws:SourceAccount`, and `kms:EncryptionContext:aws:kinesisanalytics:arn` conditions with your own values. Use the ARN of your application. For the optional statements, use `arn:aws:kinesisanalytics:{{region}}:{{account-id}}:snapshot/*` or the ARN of a specific enhanced snapshot.

Leave `OptionalAllowServiceToUseKeyForImportedSnapshots` without an `aws:SourceArn` condition. AWS KMS does not always receive `aws:SourceArn` when Managed Service for Apache Flink reads and writes the data of an enhanced snapshot.

### Key policy for enhanced snapshot import and export
<a name="create-cmk-kms-key-policy-snapshot-transfer"></a>

You can use a separate customer managed key for imported enhanced snapshots. Name the key in the `DestinationEncryptionConfiguration` of the `ImportSnapshot` request. Managed Service for Apache Flink encrypts the new enhanced snapshot with this key. For the key policy, use the policy in [Create a KMS key policy](#create-cmk-kms-key-policy) with the optional statements. `ImportSnapshot` does not use `kms:DescribeKey`. Restore and `ExportSnapshot` use it.

To export an enhanced snapshot, the key that encrypts the enhanced snapshot must allow the following:
+ The caller: `kms:DescribeKey`, `kms:Decrypt`, and `kms:GenerateDataKey`, with `kms:ViaService`.
+ `kinesisanalytics.amazonaws.com` and `infrastructure.kinesisanalytics.amazonaws.com`: `kms:DescribeKey`, with `aws:SourceArn` and `aws:SourceAccount`.
+ `kinesisanalytics.amazonaws.com`: `kms:Decrypt` and `kms:GenerateDataKey`, with the encryption context.

For an enhanced snapshot that an application created, use the ARN of that application in each condition. The application key policy earlier in this section already has these statements. For an imported enhanced snapshot, use the snapshot ARN. The preceding key policy for imported enhanced snapshots already allows it.

The key in the `DestinationEncryptionConfiguration` of an `ExportSnapshot` request encrypts the exported Amazon S3 objects. The export role uses that key, not Managed Service for Apache Flink. For the export role policy, see [Export KMS permissions policy](security-iam-snapshots.md#security-iam-snapshots-transfer-role-export-kms).

### Application lifecycle operator (API caller) permissions
<a name="create-cmk-kms-api-caller-permissions"></a>

The following IAM policy ensures that the application lifecycle operator has the necessary permissions to assign a KMS key to the application, {{MyCmkApplication}}.

------
#### [ JSON ]

****  

```json
{
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
            "Resource": "arn:aws:iam::{{123456789012}}:role/{{MyCmkApplicationRole}}"
        },
        {
            "Sid": "AllowDescribeKey",
            "Effect": "Allow",
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": "arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "kinesisanalytics.{{us-east-1}}.amazonaws.com"
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
            "Resource": "arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "kinesisanalytics.{{us-east-1}}.amazonaws.com",
                    "kms:EncryptionContext:aws:kinesisanalytics:arn": 
                        "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:application/{{MyCmkApplication}}"
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
            "Resource": "arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "kinesisanalytics.{{us-east-1}}.amazonaws.com",
                    "kms:EncryptionContext:aws:kinesisanalytics:arn": 
                        "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:application/{{MyCmkApplication}}"
                }
            }
        },
        {
            "Sid": "AllowMyCmkApplicationCreateGrantForRunningState",
            "Effect": "Allow",
            "Action": "kms:CreateGrant",
            "Resource": "arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}",
            "Condition": {
                "ForAllValues:StringEquals": {
                    "kms:GrantOperations": "Decrypt"
                },
                "StringEquals": {
                    "kms:ViaService": "kinesisanalytics.{{us-east-1}}.amazonaws.com",
                    "kms:EncryptionContext:aws:kinesisanalytics:arn": 
                        "arn:aws:kinesisanalytics:{{us-east-1}}:{{123456789012}}:application/{{MyCmkApplication}}",
                    "kms:GrantConstraintType": "EncryptionContextSubset"
                }
            }
        }
    ]
}
```

------

## Update an existing application to use CMK
<a name="update-existing-app-use-cmk-api"></a>

In Amazon MSF, you can apply a CMK policy to an existing application that uses AWS owned keys (AOKs).

By default, Amazon MSF uses AOKs to encrypt all your data in ephemeral (running application storage) and durable (durable application storage) storage. This means all data subject to a Flink [checkpoint](how-fault.md) or [snapshot](how-snapshots.md) are encrypted using AOKs by default. When you replace the AOK with a CMK, new checkpoints and snapshots are encrypted with CMK. However, historic snapshots will remain encrypted with the AOK.

For an application in enhanced snapshot mode, each existing enhanced snapshot keeps the key that Managed Service for Apache Flink used to create it. The key change applies only to enhanced snapshots that Managed Service for Apache Flink creates after the update. To restore from an older enhanced snapshot, the caller needs `kms:DescribeKey`, `kms:Decrypt`, and `kms:GenerateDataKey` on the key of that enhanced snapshot. For more information, see [Restore from an enhanced snapshot that uses a different key](#manage-cmk-api-restore-different-key).

**To update an existing application to use CMK**

1. Create a JSON file with the following configuration. 

   Make sure that you replace the value of `CurrentApplicationVersionId` to the current version number of the application. You can get the current version number of your application, using [DescribeApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeApplication.html).

   In this JSON configuration, remember to replace the {{sample}} values with the actual values.

   ```json
   {
       "ApplicationName": "{{MyCmkApplication}}",
       "CurrentApplicationVersionId": {{1}},
       "ApplicationConfigurationUpdate": {
           "ApplicationEncryptionConfigurationUpdate": {
               "KeyTypeUpdate": "CUSTOMER_MANAGED_KEY",
               "KeyIdUpdate": "{{arn:aws:kms:us-east-1:{{123456789012}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}}}"
           }
       }
   }
   ```

1. Save this file. For example, save it with the name **enable-cmk.json**.

1. Run the [update-application](https://docs.aws.amazon.com/cli/latest/reference/kinesisanalyticsv2/update-application.html) AWS CLI command as shown in the following example. In this command, provide the JSON configuration file you created in the previous steps as the file argument.

   ```
   aws kinesisanalyticsv2 update-application \
       --cli-input-json file://enable-cmk.json
   ```

The preceding configuration is accepted to update the application for using CMK only if the following conditions are met:
+ API caller has a policy statement that allows access to the key.
+ Key policy has a policy statement that allows API caller access to the key.
+ Key policy has a policy statement that allows the Amazon MSF service principal, for example, `kinesisanalytics.amazonaws.com` access to the key.

## Revert from CMK to AWS owned key
<a name="revert-cmk-to-aok-api"></a>

**To revert from CMK to an AOK**

1. Create a JSON file with the following configuration.

   In this JSON configuration, remember to replace the {{sample}} values with the actual values.

   ```json
   {
       "ApplicationName": "{{MyCmkApplication}}",
       "CurrentApplicationVersionId": {{1}},
       "ApplicationConfigurationUpdate": {
           "ApplicationEncryptionConfigurationUpdate": {
               "KeyTypeUpdate": "AWS_OWNED_KEY"
           }
       }
   }
   ```

1. Save this file. For example, save it with the name **disable-cmk.json**.

1. Run the [update-application](https://docs.aws.amazon.com/cli/latest/reference/kinesisanalyticsv2/update-application.html) AWS CLI command as shown in the following example. In this command, provide the JSON configuration file you created in the previous steps as the file argument.

   ```
   aws kinesisanalyticsv2 update-application \
       --cli-input-json file://disable-cmk.json
   ```

## Restore from an enhanced snapshot that uses a different key
<a name="manage-cmk-api-restore-different-key"></a>

An application can restore from an enhanced snapshot that a different key encrypts. The restore uses the key of the enhanced snapshot, not the key of the application. The following rules apply:
+ The caller needs `kms:DescribeKey`, `kms:Decrypt`, and `kms:GenerateDataKey` on the key of the enhanced snapshot. Without this permission, the restore returns `AccessDeniedException`.
+ The policy of the enhanced snapshot key must allow the encryption context of the enhanced snapshot. For the values, see [KMS encryption context and constraints](key-management-flink.md#kms-encryption-context-constraints).

For the restore procedure, see [Restore an application from an enhanced snapshot](snapshots-restore.md).