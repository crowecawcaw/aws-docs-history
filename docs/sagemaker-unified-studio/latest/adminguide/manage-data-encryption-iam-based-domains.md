# Manage data encryption in

IAM-based domains

Data encryption in IAM-based domains protects your data at rest and in transit within
Amazon SageMaker Unified Studio. You can choose between AWS-managed encryption keys for simplified
management or customer-managed AWS KMS keys for enhanced control over encryption
operations. Encryption settings are configured during domain setup and cannot be changed
after domain creation.

AWS-managed encryption provides automatic key management with no additional
configuration required. Customer-managed encryption enables you to control key policies,
rotation schedules, and access permissions while requiring additional IAM policy
configuration for your roles.

All data stored in the default Amazon S3 bucket created by Amazon SageMaker Unified Studio is encrypted
according to your chosen encryption configuration. The encryption settings apply to all
projects and resources within the domain.

Prerequisites:

- Understanding of AWS KMS key management concepts
- Appropriate IAM permissions to use or create KMS keys
- Decision on encryption approach based on your security requirements
  Configure AWS-managed encryption (default):

1. During domain setup, leave the **Customize encryption settings
   (advanced)** option unchecked.
2. The system automatically configures encryption using AWS-owned and managed
   keys.
3. No additional IAM policy configuration is required for AWS-managed
   encryption.
   Configure customer-managed encryption:

4. During domain setup, check **Customize encryption settings
   (advanced)**.
5. Choose **Choose an AWS KMS key** and select one of the following
   options:
   - Select an existing KMS key from the dropdown menu
   - Enter a KMS key ARN directly in the text field
   - Choose **Create new KMS Key** to create a new key

6. If creating a new key, configure the key policy to allow access from your IAM
   roles.
7. Add the following inline policy to your Login and Execution IAM roles to enable KMS key
   usage.

```

{
    "Version": "2012-10-17",
    "Id": "key-consolepolicy",
    "Statement": [
        {
            "Sid": "ListAndDescribe",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account>:root"
            },
            "Action": [
                "kms:DescribeKey",
                "kms:ListAliases",
                "kms:ListGrants"
            ],
            "Resource": "*",
            "Condition": {
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::<account>:role/service-role/AmazonSageMaker*",
                        "arn:aws:iam::<account>:role/<role_name>"
                    ]
                }
            }
        },
        {
            "Sid": "CloudWatchLogs",
            "Effect": "Allow",
            "Principal": { "Service": "logs.<region>.amazonaws.com" },
            "Action": [
                "kms:Encrypt*",
                "kms:Decrypt*",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:Describe*"
            ],
            "Resource": "*",
            "Condition": {
                "ArnLike": {
                    "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:*:*:log-group:/aws/mwaa-serverless/*"
                }
            }
        },
        {
            "Sid": "S3Table",
            "Effect": "Allow",
            "Principal": {
                "Service": "maintenance.s3tables.amazonaws.com"
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*"
        },
        {
            "Sid": "DataZone",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account>:root"
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey",
                "kms:Encrypt",
                "kms:GenerateDataKeyWithoutPlaintext",
                "kms:ReEncryptTo",
                "kms:ReEncryptFrom"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "kms:EncryptionContextKeys": "aws:datazone:domainId"
                },
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::<account>:role/service-role/AmazonSageMaker*",
                        "arn:aws:iam::<account>:role/<role_name<"
                    ]
                }
            }
        },
        {
            "Sid": "S3Kms",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account>:root"
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "s3.*.amazonaws.com"
                },
                "Null": {
                    "kms:EncryptionContext:aws:s3:arn": "false"
                },
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::<account>:role/service-role/AmazonSageMaker*",
                        "arn:aws:iam::<account>:role/<role_name>"
                    ]
                }
            }
        },
        {
            "Sid": "SchedulerKms",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account>:root"
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "*",
            "Condition": {
                "Null": {
                    "kms:EncryptionContext:aws:scheduler:schedule:arn": "false"
                },
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::<account>:role/service-role/AmazonSageMaker*",
                        "arn:aws:iam::<account>:role/<role_name>"
                    ]
                }
            }
        },
        {
            "Sid": "SecretsKms",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account>:root"
            },
            "Action": [
                "kms:Decrypt",
                "kms:Encrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "secretsmanager.*.amazonaws.com"
                },
                "Null": {
                    "kms:EncryptionContext:SecretARN": "false"
                },
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::<account>:role/service-role/AmazonSageMaker*",
                        "arn:aws:iam::<account>:role/<role_name>"
                    ]
                }
            }
        },
        {
            "Sid": "SageMakerKms",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account>:root"
            },
            "Action": [
                "kms:Decrypt",
                "kms:Encrypt",
                "kms:GenerateDataKey",
                "kms:GenerateDataKeyWithoutPlaintext",
                "kms:ReEncryptTo",
                "kms:ReEncryptFrom"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "sagemaker.*.amazonaws.com"
                },
                "Null": {
                    "kms:EncryptionContextKeys": "false"
                },
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::<account>:role/service-role/AmazonSageMaker*",
                        "arn:aws:iam::<account>:role/<role_name>"
                    ]
                }
            }
        },
        {
            "Sid": "SageMakerCreateGrant",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account>:root"
            },
            "Action": [
                "kms:CreateGrant"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "sagemaker.*.amazonaws.com"
                },
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::<account>:role/service-role/AmazonSageMaker*",
                        "arn:aws:iam::<account>:role/<role_name>"
                    ]
                }
            }
        },
        {
            "Sid": "DataZoneCreateGrant",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account>:root"
            },
            "Action": [
                "kms:CreateGrant"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "datazone.*.amazonaws.com"
                },
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::<account>:role/service-role/AmazonSageMaker*",
                        "arn:aws:iam::<account>:role/<role_name>"
                    ]
                },
                "ForAllValues:StringEquals": {
                    "kms:GrantOperations": [
                        "Encrypt",
                        "Decrypt",
                        "ReEncryptFrom",
                        "ReEncryptTo",
                        "GenerateDataKeyWithoutPlaintext",
                        "GenerateDataKey",
                        "DescribeKey",
                        "RetireGrant",
                        "CreateGrant"
                    ]
                }
            }
        },
        {
            "Sid": "GlueKms",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account>:root"
            },
            "Action": [
                "kms:Decrypt",
                "kms:Encrypt",
                "kms:GenerateDataKey",
                "kms:GenerateDataKeyWithoutPlaintext"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "glue.*.amazonaws.com"
                },
                "Null": {
                    "kms:EncryptionContextKeys": "false"
                },
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::<account>:role/service-role/AmazonSageMaker*",
                        "arn:aws:iam::<account>:role/<role_name>"
                    ]
                }
            }
        },
        {
            "Sid": "BedrockKms",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account>:root"
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "bedrock.*.amazonaws.com"
                },
                "Null": {
                    "kms:EncryptionContextKeys": "false"
                },
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::<account>:role/service-role/AmazonSageMaker*",
                        "arn:aws:iam::<account>:role/<role_name>"
                    ]
                }
            }
        },
        {
            "Sid": "WorkflowsCreateGrant",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account>:root"
            },
            "Action": [
                "kms:CreateGrant"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "airflow-serverless.*.amazonaws.com"
                },
                "ForAnyValue:StringEquals": {
                    "kms:EncryptionContextKeys": "aws:airflow-serverless:workflow-arn"
                },
                "ForAllValues:StringEquals": {
                    "kms:GrantOperations": [
                        "Decrypt",
                        "Encrypt",
                        "GenerateDataKey",
                        "GenerateDataKeyWithoutPlaintext",
                        "RetireGrant"
                    ]
                },
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::<account>:role/service-role/AmazonSageMaker*",
                        "arn:aws:iam::<account>:role/<role_name>"
                    ]
                }
            }
        },
        {
            "Sid": "WorkflowsKms",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account>:root"
            },
            "Action": [
                "kms:Decrypt",
                "kms:Encrypt",
                "kms:GenerateDataKey",
                "kms:GenerateDataKeyWithoutPlaintext"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "kms:EncryptionContextKeys": "aws:airflow-serverless:workflow-arn"
                },
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::<account>:role/service-role/AmazonSageMaker*",
                        "arn:aws:iam::<account>:role/<role_name>"
                    ]
                }
            }
        }
    ]
}

```

5. Replace the resource ARN with your actual KMS key ARN.
6. Complete the domain setup process with your encryption configuration.

###### Warning

Encryption settings cannot be modified after domain creation. Choose your encryption
approach carefully based on your long-term security requirements.
