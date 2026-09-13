

# Create a service role for managed Amazon Bedrock Knowledge Bases
<a name="kb-managed-permissions"></a>

To use a custom role for a managed knowledge base instead of the one Amazon Bedrock automatically creates, create an IAM role and attach the following permissions by following the steps at [Creating a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html). Include only the necessary permissions for your own security.

**Note**  
A policy cannot be shared between multiple roles when the service role is used.
+ Trust relationship
+ Access to the Amazon Bedrock base models
+ Access to the data source for where you store your data
+ (If you configure a multimodal storage destination) Access to your multimodal storage bucket

**Topics**
+ [Trust relationship](#kb-managed-permissions-trust)
+ [Permissions to access Amazon Bedrock models](#kb-managed-permissions-access-models)
+ [Permissions for your multimodal storage destination](#kb-managed-permissions-multimodal-storage)
+ [Permissions to access your data sources](#kb-managed-permissions-access-ds)

## Trust relationship
<a name="kb-managed-permissions-trust"></a>

The following policy allows Amazon Bedrock to assume this role and create and manage knowledge bases. You can restrict the scope of the permission by using one or more global condition context keys. For more information, see [AWS global condition context keys.](IAM/latest/UserGuide/reference_policies_condition-keys.html) Set the `aws:SourceAccount` value to your account ID. Use the `ArnEquals` or `ArnLike` condition to restrict the scope to specific knowledge bases.

**Note**  
As a best practice for security purposes, replace the {{\*}} with specific knowledge base IDs after you have created them.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "bedrock.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                },
                "ArnLike": {
                    "AWS:SourceArn": "arn:aws:bedrock:{{us-east-1}}:{{123456789012}}:knowledge-base/{{*}}"
                }
            }
        }
    ]
}
```

------

## Permissions to access Amazon Bedrock models
<a name="kb-managed-permissions-access-models"></a>

Attach the following policy to provide permissions for the role to use Amazon Bedrock models to embed your source data.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:ListFoundationModels",
                "bedrock:ListCustomModels"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel"
            ],
            "Resource": [
                "arn:aws:bedrock:{{us-east-1}}::foundation-model/amazon.titan-embed-text-v1",
                "arn:aws:bedrock:{{us-east-1}}::foundation-model/cohere.embed-english-v3",
                "arn:aws:bedrock:{{us-east-1}}::foundation-model/cohere.embed-multilingual-v3"
            ]
        }
    ]
}
```

------

If you use the TwelveLabs Marengo Embed 3.0 embedding model, the knowledge base invokes the model both synchronously and asynchronously, so the role needs permissions for both. Attach the following statements, replacing {{${Region}}} and {{${AccountId}}} with the AWS Region and account ID for your knowledge base, and {{${InferenceProfileId}}} with the ID of the inference profile that you use. The `foundation-model` ARN uses `*` for the Region instead of a specific Region. This is required because a cross-region inference profile can route the model invocation to the underlying foundation model in any of its member AWS Regions.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "BedrockInvokeModelStatement",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel"
            ],
            "Resource": [
                "arn:aws:bedrock:*::foundation-model/twelvelabs.marengo-embed-3-0-v1:0",
                "arn:aws:bedrock:{{${Region}}}:{{${AccountId}}}:inference-profile/{{${InferenceProfileId}}}",
                "arn:aws:bedrock:{{${Region}}}:{{${AccountId}}}:async-invoke/*"
            ]
        },
        {
            "Sid": "BedrockGetAsyncInvokeStatement",
            "Effect": "Allow",
            "Action": [
                "bedrock:GetAsyncInvoke"
            ],
            "Resource": [
                "arn:aws:bedrock:{{${Region}}}:{{${AccountId}}}:async-invoke/*"
            ]
        }
    ]
}
```

**Note**  
The preceding policy includes an [inference profile](inference-profiles-support.md) ARN because in some AWS Regions you must specify an inference profile for the TwelveLabs Marengo Embed 3.0 model when you create the knowledge base. In those Regions, the knowledge base uses both the inference profile and the on-demand model, so the role needs access to both. If you don't use an inference profile, you can omit the inference profile ARN from the `Resource` list.  
To determine whether the Region that you use requires an inference profile, see [Native multimodal processing](kb-managed-native-multimodal.md).

## Permissions for your multimodal storage destination
<a name="kb-managed-permissions-multimodal-storage"></a>

The multimodal storage destination is the Amazon S3 bucket that is used for processing and ingesting multimodal content into your knowledge base. Amazon Bedrock Knowledge Bases creates an `aws/` prefix folder within your bucket for easy access.

Attach the following policy to provide permissions for the role to read, write, and delete this content. Replace {{amzn-s3-demo-bucket}} with the name of your multimodal storage bucket.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "S3MultimodalStorageListStatement",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
            ]
        },
        {
            "Sid": "S3MultimodalStorageObjectStatement",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
            ]
        }
    ]
}
```

## Permissions to access your data sources
<a name="kb-managed-permissions-access-ds"></a>

Select from the following data sources to attach the necessary permissions for the role.

**Topics**
+ [Permissions to access your Amazon S3 data source](#kb-managed-permissions-access-s3)
+ [Permissions to access your Confluence data source](#kb-managed-permissions-access-confluence)
+ [Permissions to access your Microsoft SharePoint data source](#kb-managed-permissions-access-sharepoint)
+ [Permissions to access your Web Crawler data source](#kb-managed-permissions-access-webcrawler)
+ [Permissions to access your Microsoft OneDrive data source](#kb-managed-permissions-access-onedrive)
+ [Permissions to access your Google Drive data source](#kb-managed-permissions-access-googledrive)

### Permissions to access your Amazon S3 data source
<a name="kb-managed-permissions-access-s3"></a>

If your data source is Amazon S3, attach the following policy to provide permissions for the role to access the S3 bucket that you will connect to as your data source.

If you encrypted the data source with a AWS KMS key, attach permissions to decrypt the key to the role by following the steps at [Permissions to decrypt your AWS KMS key for your data sources in Amazon S3](encryption-kb.md#encryption-kb-ds).

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "S3ListBucketStatement",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "{{123456789012}}"
                }
            }
        },
        {
            "Sid": "S3GetObjectStatement",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "{{123456789012}}"
                }
            }
        }
    ]
}
```

------

### Permissions to access your Confluence data source
<a name="kb-managed-permissions-access-confluence"></a>

Attach the following policy to provide permissions for the role to access Confluence.

**Note**  
`secretsmanager:PutSecretValue` is only necessary if you use OAuth 2.0 authentication with a refresh token.  
Confluence OAuth2.0 **access** token has a default expiry time of 60 minutes. If this token expires while your data source is syncing (sync job), Amazon Bedrock will use the provided **refresh** token to regenerate this token. This regeneration refreshes both the access and refresh tokens. To keep the tokens updated from the current sync job to the next sync job, Amazon Bedrock requires write/put permissions for your secret credentials.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "secretsmanager:GetSecretValue"
        ],
        "Resource": [
            "arn:aws:secretsmanager:{{${Region}}}:{{${AccountId}}}:secret:{{${SecretId}}}"
        ]
    }]
}
```

### Permissions to access your Microsoft SharePoint data source
<a name="kb-managed-permissions-access-sharepoint"></a>

Attach the following policy to provide permissions for the role to access Microsoft SharePoint.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "secretsmanager:GetSecretValue"
        ],
        "Resource": [
            "arn:aws:secretsmanager:{{${Region}}}:{{${AccountId}}}:secret:{{${SecretId}}}"
        ]
    }]
}
```

**Note**  
If you use certificate-based authentication (X.509) and store your certificate in an Amazon S3 bucket, you must also grant `s3:GetObject` permission to the service role for the bucket and key where the certificate file (.pfx or .pem) is stored. The following example shows the additional policy statement required:  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "s3:GetObject"
        ],
        "Resource": [
            "arn:aws:s3:::{{${CertificateBucketName}}}/{{${CertificateKeyPath}}}"
        ]
    }]
}
```

### Permissions to access your Web Crawler data source
<a name="kb-managed-permissions-access-webcrawler"></a>

Attach the following policy to provide permissions for the role to access websites through the Web Crawler. If your website requires authentication, include permissions to access the AWS Secrets Manager secret that stores your credentials.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "secretsmanager:GetSecretValue"
        ],
        "Resource": [
            "arn:aws:secretsmanager:{{${Region}}}:{{${AccountId}}}:secret:{{${SecretId}}}"
        ]
    }]
}
```

### Permissions to access your Microsoft OneDrive data source
<a name="kb-managed-permissions-access-onedrive"></a>

Attach the following policy to provide permissions for the role to access Microsoft OneDrive.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "secretsmanager:GetSecretValue"
        ],
        "Resource": [
            "arn:aws:secretsmanager:{{${Region}}}:{{${AccountId}}}:secret:{{${SecretId}}}"
        ]
    }]
}
```

### Permissions to access your Google Drive data source
<a name="kb-managed-permissions-access-googledrive"></a>

Attach the following policy to provide permissions for the role to access Google Drive.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "secretsmanager:GetSecretValue"
        ],
        "Resource": [
            "arn:aws:secretsmanager:{{${Region}}}:{{${AccountId}}}:secret:{{${SecretId}}}"
        ]
    }]
}
```