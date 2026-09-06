

# Data protection in Amazon Cognito
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Amazon Cognito (Amazon Cognito). As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. This content includes the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq).

For data protection purposes, we recommend that you protect AWS account credentials and set up individual user accounts with AWS Identity and Access Management (IAM). That way each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources.
+ Set up API and user activity logging with AWS CloudTrail.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing personal data that is stored in Amazon S3.

We strongly recommend that you never put sensitive identifying information, such as your customers' account numbers, into free-form fields such as a **Name** field. This includes when you work with Amazon Cognito or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into Amazon Cognito or other services might get picked up for inclusion in diagnostic logs. When you provide a URL to an external server, don't include credentials information in the URL to validate your request to that server.

## Data encryption
<a name="data-encryption"></a>

Data encryption typically falls into two categories: encryption at rest and encryption in transit.

### Encryption at rest
<a name="data-encryption-at-rest"></a>

Data within Amazon Cognito user pools and identity pools is encrypted at rest in accordance with industry standards. 
+ Amazon Cognito encrypts customer data in identity pools with [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk). You can't change this behavior.
+ *By default*, Amazon Cognito also encrypts customer data in user pools with AWS owned keys. You can also configure your user pools to instead encrypt your customers' information with [customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk).

**AWS owned key**  
Amazon Cognito encrypts the data in your user pool or identity pool with an AWS owned KMS key. Keys of this type aren't visible in AWS KMS.

**Customer managed key**  
Amazon Cognito encrypts the data in your user pool with a customer managed key. You own the administration of customer managed key policies, rotation, and scheduled deletion.  
Encryption with customer managed keys might not be available in some user pools. Newly-created user pools always have this form of encryption available to them.

**Things to know about user pool encryption with customer managed keys**

1. All customer data in user pools is encrypted at rest, even if you take no action to configure encryption settings.

1. Amazon Cognito supports only symmetric KMS keys in the same AWS Region as your user pool for user pool encryption at rest. You can't configure user pool encryption at rest with [asymmetric keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html). You can configure encryption at rest with single-Region keys and with [multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) that are in the same Region as your user pool.

1. You can configure user pool encryption only with a KMS key ARN, not an alias.

**PII encryption**  
Amazon Cognito supports the confidentiality, integrity, and availability of personally identifiable information (PII) in user attribute searches with [searchable encryption](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/searchable-encryption.html). These Hash-based Message Authentication Code (HMAC) functions, performance-optimized for user pool datasets, map between the plaintext and encrypted values of user attributes. Amazon Cognito calculates HMAC values with the KMS key that encrypts your user pool. This protection applies to the following attributes:
+ `sub`
+ `email`
+ `phone_number`
+ `given_name`
+ `family_name`
+ `name`
+ `username`
+ `preferred_username`
+ `cognito:user_status`

The following procedures configure encryption at rest in your user pool. For more information about KMS key policies that delegate access to AWS services like Amazon Cognito, see [Permissions for Amazon Cognito in key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-services.html).

------
#### [ Set customer managed key policy ]

To use a customer managed key, your key must trust an Amazon Cognito service principal to perform encryption and decryption operations on the key. Configure the [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) of your KMS key as shown in the following example. The IAM principal that writes this policy must have write access to your KMS key, with `kms:PutKeyPolicy` permission.

```
{
    "Id": "cognito-cmk-policy",
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Allow Amazon Cognito service access",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "cognito-idp.amazonaws.com",
                    "identitystore.amazonaws.com"
                ]
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKeyWithoutPlainText"
            ],
            "Resource": "*",
            "Condition": {
                "ArnEquals": {
                    "aws:SourceArn": [
                        "arn:{{aws}}:cognito-idp:{{us-east-1}}:{{111122223333}}:userpool/{{us-east-1_EXAMPLE}}"
                    ]
                },
                "StringEquals": {
                    "aws:SourceAccount": [
                        "{{111122223333}}"
                    ]
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:cognito-idp:userpool-arn": "arn:{{aws}}:cognito-idp:{{us-east-1}}:{{111122223333}}:userpool/{{us-east-1_EXAMPLE}}"
                }
            }
        },
        {
            "Sid": "Allow Amazon Cognito service DescribeKey access",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "cognito-idp.amazonaws.com",
                    "identitystore.amazonaws.com"
                ]
            },
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": "*",
            "Condition": {
                "ArnEquals": {
                    "aws:SourceArn": [
                        "arn:{{aws}}:cognito-idp:{{us-east-1}}:{{111122223333}}:userpool/{{us-east-1_EXAMPLE}}"
                    ]
                },
                "StringEquals": {
                    "aws:SourceAccount": [
                        "{{111122223333}}"
                    ]
                }
            }
        },
        {
            "Sid": "Allow access through Amazon Cognito for all principals in account that are authorized to use Amazon Cognito",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": [
                        "cognito-idp.{{us-east-1}}.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Sid": "Allow access through Amazon Cognito for all principals in account that are authorized to use Amazon Cognito",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKeyWithoutPlainText"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": [
                        "cognito-idp.{{us-east-1}}.amazonaws.com"
                    ]
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:cognito-idp:userpool-arn": "arn:{{aws}}:cognito-idp:{{us-east-1}}:{{111122223333}}:userpool/{{us-east-1_EXAMPLE}}"
                }
            }
        },
        {
            "Sid": "Allow administrators to manage the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:{{aws}}:iam::{{111122223333}}:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        }
    ]
}
```

------
#### [ Set customer managed key policy with permissions for encryption of exported logs ]

Apply this policy to your KMS key when you have [log export](exporting-quotas-and-usage.md) configured. This policy permits Amazon Cognito to encrypt logs as it exports them, and the intermediate service to decrypt them before writing them to your CloudWatch Logs log group. Configure the [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) of your KMS key as shown in the following example. The IAM principal that writes this policy must have write access to your KMS key, with `kms:PutKeyPolicy` permission.

```
{
    "Id": "cognito-cmk-policy",
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Allow Amazon Cognito service access",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "cognito-idp.amazonaws.com",
                    "identitystore.amazonaws.com"
                ]
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKeyWithoutPlainText"
            ],
            "Resource": "*",
            "Condition": {
                "ArnEquals": {
                    "aws:SourceArn": [
                        "arn:{{aws}}:cognito-idp:{{us-east-1}}:{{111122223333}}:userpool/{{us-east-1_EXAMPLE}}"
                    ]
                },
                "StringEquals": {
                    "aws:SourceAccount": [
                        "{{111122223333}}"
                    ]
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:cognito-idp:userpool-arn": "arn:{{aws}}:cognito-idp:{{us-east-1}}:{{111122223333}}:userpool/{{us-east-1_EXAMPLE}}"
                }
            }
        },
        {
            "Sid": "Allow Amazon Cognito service DescribeKey access",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "cognito-idp.amazonaws.com",
                    "identitystore.amazonaws.com"
                ]
            },
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": "*",
            "Condition": {
                "ArnEquals": {
                    "aws:SourceArn": [
                        "arn:{{aws}}:cognito-idp:{{us-east-1}}:{{111122223333}}:userpool/{{us-east-1_EXAMPLE}}"
                    ]
                },
                "StringEquals": {
                    "aws:SourceAccount": [
                        "{{111122223333}}"
                    ]
                }
            }
        },
        {
            "Sid": "Allow access through Amazon Cognito for all principals in account that are authorized to use Amazon Cognito",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": [
                "kms:DescribeKey"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": [
                        "cognito-idp.{{us-east-1}}.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Sid": "Allow access through Amazon Cognito for all principals in account that are authorized to use Amazon Cognito",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKeyWithoutPlainText"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": [
                        "cognito-idp.{{us-east-1}}.amazonaws.com"
                    ]
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:cognito-idp:userpool-arn": "arn:{{aws}}:cognito-idp:{{us-east-1}}:{{111122223333}}:userpool/{{us-east-1_EXAMPLE}}"
                }
            }
        },
        {
            "Sid": "Allow Amazon Cognito service log delivery access",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "cognito-idp.amazonaws.com"
                ]
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Encrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:EncryptionContext:SourceArn": "arn:{{aws}}:logs:{{us-east-1}}:{{111122223333}}:*"
                }
            }
        },
        {
            "Sid": "Allow IngestionHub service log delivery access",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "delivery.logs.amazonaws.com"
                ]
            },
            "Action": [
                "kms:GenerateDataKey",
                "kms:Decrypt"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:EncryptionContext:SourceArn": "arn:{{aws}}:logs:{{us-east-1}}:{{111122223333}}:*"
                }
            }
        },
        {
            "Sid": "Allow administrators to manage the key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:{{aws}}:iam::{{111122223333}}:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        }
    ]
}
```

------
#### [ Configure encryption at rest in the console ]

**To configure encryption at rest in a user pool**

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home). You might be prompted for your AWS credentials.

1. Choose **User Pools**.

1. Choose an existing user pool from the list, or [create a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-as-user-directory.html).

1. Choose the **Settings** menu and navigate to the **User pool security** tab. Locate **Encryption at rest** and select **Edit**.

1. Under **Key type**, select either **AWS owned key** or **Customer managed key**.

   1. If you selected **AWS owned key**, no additional configuration is required.

   1. If you selected **Customer managed key**, enter the ARN of a KMS key into **Customer managed key ARN**. You can also choose **Create an AWS KMS key** and open a new window in the AWS KMS console to create a new KMS key.

1. Choose **Save changes**.

------
#### [ Configure encryption at rest with the API ]

Set your key configuration in a [CreateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.html#CognitoUserPools-CreateUserPool-request-KeyConfiguration) or [UpdateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.html#CognitoUserPools-UpdateUserPool-request-KeyConfiguration) API request. The following partial example request body sets a user pool to use the provided customer managed key. For a complete example request, see [Examples](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.html#API_CreateUserPool_Examples).

```
"KeyConfiguration": { 
   "KeyType": "CUSTOMER_MANAGED_KEY",
   "KmsKeyArn": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{a1b2c3d4-5678-90ab-cdef-EXAMPLE22222}}"
},
```

The following partial example request body sets a user pool to use an AWS owned key.

```
"KeyConfiguration": { 
   "KeyType": "AWS_OWNED_KEY"
},
```

If your [DescribeUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPool.html) response doesn't include a `KeyConfiguration` parameter, your user pool is configured to encrypt data at rest with an AWS owned key.

------

## Encryption in transit
<a name="data-encryption-in-transit"></a>

As a managed service, Amazon Cognito is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access Amazon Cognito through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Amazon Cognito user pools and identity pools have IAM-authenticated, unauthenticated, and token-authorized API operations. Some are *control plane*-type operations for administrative operations like configuring a user pool domain, and others are *data plane*-type operations for authentication. For more information, see [List of API operations grouped by authorization model](authentication-flows-public-server-side.md#user-pool-apis-auth-unauth). All classes of Amazon Cognito API operations share a namespace—`cognito-idp` for user pools, `cognito-identity` for identity pools—and service endpoints. [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) require encryption in transit with a [minimum TLS version of 1.2](https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/).

Amazon Cognito user pools host [managed login](cognito-user-pools-managed-login.md) and the classic hosted UI on web domains that are served from service-owned Amazon CloudFront distributions. Amazon Cognito manages the settings for encryption in transit on those distributions. For more information about the encryption settings for managed login, see [TLS version](cognito-user-pools-managed-login.md#managed-login-things-to-know-TLSversion) in the managed login chapter.