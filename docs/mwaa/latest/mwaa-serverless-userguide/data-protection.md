# Data protection in Amazon MWAA Serverless

The [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") applies
to data protection in Amazon MWAA Serverless for Apache Airflow Serverless.
As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud.
ou are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible
for the security configuration and management tasks for the AWS services that you use. For more information about data privacy,
see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq "https://aws.amazon.com/compliance/data-privacy-faq").
For information about data protection in Europe, see the
[AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the AWS Security Blog.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with
AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary
to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with CloudTrail. For information about using CloudTrail trails to
  capture AWS activities, see
  [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in the CloudTrail User Guide.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing sensitive data that is stored in Amazon S3.

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses,
into tags or free-form text fields such as a **Name** field. This includes when you work with
Amazon MWAA Serverless or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form
text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly
recommend that you do not include credentials information in the URL to validate your request to that server.

## Data encryption

The following topics describe how Amazon MWAA Serverless protects your data at rest, and in transit. Use this information to learn how
Amazon MWAA Serverless integrates with AWS KMS to encrypt data at rest, and how data is encrypted using Transport Layer Security (TLS) protocol
in transit.

### Encryption at rest

Amazon MWAA Serverless by default encrypts data at rest and uses the KMS key you provide while creating the workflow.
If you do not provide a key, Amazon MWAA Serverless encrypts this data using service keys. If you choose to use a
customer-managed KMS key, it must be in the same account as the other AWS resources and services you are using with your
workflow.

To use a customer-managed KMS key, you must attach the required policy statement for CloudWatch access to your
key policy and make the call to API using the KMS policy. Amazon MWAA Serverless attaches two grant to your
customer-managed KMS key to encrypt data at rest.

###### Note

You pay for the storage and use of AWS-owned and customer-managed KMS keys on Amazon MWAA Serverless.
For more information, refer to [AWS KMS Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

### Encryption artifacts

You specify the encryption artifacts used for at rest encryption by providing a
[customer-managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk")
when you create your Amazon MWAA Serverless workflow. Amazon MWAA Serverless adds the
[grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") needed to your specified key.

**CloudWatch Logs**: If you to use a customer-managed KMS key, you must add a key policy to your key to allow
CloudWatch Logs to use your key. If you do not provide a customer-managed KMS key, CloudWatch Logs are encrypted
using Server Side Encryption with service owned key.

## Encryption in transit

Data in transit is data that may be intercepted as it travels the network.

Transport Layer Security (TLS) encrypts the Amazon MWAA Serverless objects in transit between your Amazon MWAA Serverless workflow components and other AWS
services that integrate with Amazon MWAA Serverless, such as Amazon S3. For more information about Amazon S3 encryption, refer to
[Protecting data using encryption](../../../AmazonS3/latest/dev/UsingEncryption.md "../../../AmazonS3/latest/dev/UsingEncryption.md").

## Key management

You can configure AWS KMS to automatically rotate your KMS keys. This rotates your keys once a year while saving old keys
indefinitely so that your data can still be decrypted. For more information, refer to
[Rotate AWS KMS keys](../../../AmazonS3/latest/dev/UsingEncryption.md "../../../AmazonS3/latest/dev/UsingEncryption.md").

### Using customer-managed keys for encryption

You can optionally provide a [Customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") for data encryption on your workflow. You must create the customer managed KMS key in
the same Region as your Amazon MWAA Serverless workflow instance and your Amazon S3 bucket where you store resources for your workflows.

#### Key support

| AWS KMS feature                                                                                                                                                           | Supported |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| An<br>[AWS KMS<br>key ID or ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md").                          | Yes       |
| An<br>[AWS KMS key alias](../../../kms/latest/developerguide/kms-alias.md "../../../kms/latest/developerguide/kms-alias.md").                                             | No        |
| An<br>[AWS KMS<br>multi-region key](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md"). | No        |

#### Using Grants for Encryption

There are two resource-based access control mechanisms supported by AWS KMS for customer managed KMS key: a
[key policy](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") and
[grant](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md").

A key policy is used when the permission is mostly static and used in synchronous service mode. A grant is used when
more dynamic and granular permissions are required, such as when a service needs to define different access permissions
for itself or other accounts.

When you create an Amazon MWAA Serverless workflow and specify a customer managed KMS key, Amazon MWAA Serverless attaches the grant to
your customer managed KMS key.

Amazon MWAA Serverless creates, and attaches, additional grants to a specified KMS key on your behalf. This includes policies to
retire a grant if you delete your workflow, to use your customer managed KMS key for Client-Side Encryption (CSE),
and for execution role that needs to access secrets protected by your customer managed key in Secrets Manager.

#### Grants

Amazon MWAA Serverless adds the following
[resource based policy](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") grants on your behalf to a customer managed KMS key. These policies allow the grantee and the principal
(Amazon MWAA Serverless) to perform actions defined in the policy.

##### Grant 1: Create data plane resources

JSON

```

{
	"GranteePrincipal": "airflow-serverless.us-east-1.amazonaws.com",
	"RetiringPrincipal": "airflow-serverless.us-east-1.amazonaws.com",
	"IssuingAccount": "AWS Internal",
	"Operations": [
		"Decrypt",
		"Encrypt",
		"GenerateDataKey",
		"RetireGrant"
	],
	"Constraints": {
		"EncryptionContextSubset": {
			"aws:airflow-serverless:workflow-arn": "arn:aws:airflow-serverless:eu-west-1:`111122223333`:workflow/`workflow_name`"
		}
    }
}

```

##### Grant 2: For workflow execution

JSON

```

{
	"GranteePrincipal": "airflow-serverless.us-east-1.amazonaws.com",
	"RetiringPrincipal": "airflow-serverless.us-east-1.amazonaws.com",
	"IssuingAccount": "AWS Internal",
	"Operations": [
		"Decrypt",
		"Encrypt",
		"GenerateDataKey",
		"RetireGrant"
		],
	"Constraints": {
		"EncryptionContextSubset": {
			"aws:airflow-serverless:workflow-arn": "arn:aws:airflow-serverless:eu-west-1:`111122223333`:workflow/`workflow_name`"
			}
		}
}
```

##### Sample polices

**Execution role**: To provide permissions to the Execution role permission for KMS keys,
attach following add-on policies to the execution role.

Note that you can not use kms:viaService in the execution role since the execution role credentials are directly
used to make encrypt/decrypt calls while execution of the workflow.

JSON

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
        "Effect": "Allow",
        "Action": [
            "kms:Decrypt",
            "kms:GenerateDataKey"
        ],
        "Resource": "arn:aws:kms:eu-west-1:`111122223333`:key/`keyId`",
        "Condition": {
            "ArnLike": {
                "kms:EncryptionContext:aws:airflow-serverless:workflow-arn": "arn:aws:airflow-serverless:us-east-1:*:*"
            }
        }
    }
  ]
}

```

Trust relationship for the workflow execution role:

JSON

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "airflow-serverless.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

```

Add KMS resource policy for [CloudWatch logs](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md")

JSON

```

{
    "Version":"2012-10-17",
    "Id": "`key-default-1`",
    "Statement": [
        {
            "Sid": "Enable IAM User Permissions",
            "Effect": "Allow",
            "Principal": {
            "AWS": "arn:aws:iam::`111122223333`:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "logs.us-east-1.amazonaws.com"
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:Describe*"
            ],
            "Resource": "*",
            "Condition": {
                "ArnEquals": {
                    "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:us-east-1:`111122223333`:log-group:`log-group-name`"
                },
                {
                }
            }
        }
    ]
}

```

##### Attaching key policies to a customer-managed key

If the customer managed KMS key you used for your Amazon MWAA Serverless workflow is not already configured to
work with CloudWatch, you must update the key policy to allow for encrypted CloudWatch Logs. For more information,
refer to the [Encrypt log data in CloudWatch using AWS KMS](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md").

The following example represents a key policy for CloudWatch Logs. Substitute the sample values provided for the region.

JSON

```

{
    "Effect": "Allow",
    "Principal": {
        "Service": "logs.us-east-1.amazonaws.com"
    },
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:Describe*"
    ],
    "Resource": "*",
    "Condition": {
        "ArnEquals": {
           "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:us-east-1:`111122223333`:log-group:`log-group-name`"
        }

    }
}

```

You could add a condition on kms:viaService to scope down the usage by adding the following statement to the key policy.

JSON

```

{
            "Sid": "Enable Encrypt Decrypt with Context",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`111122223333`:`caller and execution role`"
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:GenerateDataKey",
                "kms:CreateGrant"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "airflow-serverless.us-east-1.amazonaws.com"
                }
            }
}

```

#### API Policies

This section applies only if you are using a customer-managed KMS key.
Use the following add-on policies on the role that is calling these APIs when using a customer-managed KMS key.

**CreateWorkflow API:**

JSON

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "airflow-serverless:CreateWorkflow",
            "Resource": "*"
        }
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey",
                "kms:CreateGrant"
            ],
            "Resource": "arn:aws:kms:us-east-1:`111122223333`:key/`keyId`",
            "Condition": {
                "ArnLike": {
                    "kms:EncryptionContext:aws:airflow-serverless:workflow-arn": "arn:aws:airflow-serverless:us-east-1:*:*"
                },
                "StringEquals": {
                    "kms:ViaService": "airflow-serverless.us-east-1.amazonaws.com"
                }
            }
        }
    ]
}

```

**GetWorkflow** and **GetWorkflowRun**

Note: only permission needed is `kms:Decrypt`. You can scope down to `kms:viaService`

JSON

```


{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "airflow-serverless:GetWorkflow",
                "airflow-serverless:GetWorkflowRun"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:us-east-1:`111122223333`:key/`key_id`",
            "Condition": {
                "ArnLike": {
                    "kms:EncryptionContext:aws:airflow-serverless:workflow-arn": "arn:aws:airflow-serverless:us-east-1:*:*"
                },
                "StringEquals": {
                    "kms:ViaService": "airflow-serverless.us-east-1.amazonaws.com"
                }
            }
        }
    ]
}

```

**StartWorkflowRun**

JSON

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "airflow-serverless:StartWorkflowRun",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "arn:aws:kms:us-east-1:`111122223333`:key/`key_id`",
      "Condition": {
        "ArnLike": {
          "kms:EncryptionContext:aws:airflow-serverless:workflow-arn": "arn:aws:airflow-serverless:us-east-1:*:*"
        },
        "StringEquals": {
            "kms:ViaService": "airflow-serverless.us-east-1.amazonaws.com"
        }
      }
    }
  ]
}

```
