# IAM role

Whether you use the AWS Management Console or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API, you must provide an IAM role that allows Amazon Q Business to access your Amazon S3 bucket.

If you use the AWS CLI or an AWS SDK, you must create an AWS Identity and Access Management (IAM) policy
before you create an Amazon Q Business resource. When you call the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") operation, you provide the Amazon Resource Name (ARN) role with
the policy attached.

If you use the AWS Management Console, you can create a new IAM role in the Amazon Q console or use an existing IAM role while creating your data
source.

###### Note

To learn how to create an IAM role, see [Create a
role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

Cross-account Amazon S3 buckets are supported with Amazon Q Business. However, your bucket must be located in the same AWS Region as your Amazon Q Business index, and your index must have permissions to access the bucket containing your documents.

When you use an Amazon S3 bucket as a data source, you must provide a role that has
permissions to:

- Access your Amazon S3 bucket.
- Permission to access the [`BatchPutDocument`](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") and [`BatchDeleteDocument`](../api-reference/API_BatchDeleteDocument.md "../api-reference/API_BatchDeleteDocument.md") API operations in order to ingest
  documents.
- Permission to access the Principal Store APIs needed to ingest access control and
  identity information from documents.
  Cross-account Amazon S3 buckets are supported. To configure cross-account Amazon S3 bucket access, follow these steps:

###### Configuring Cross-Account Amazon S3 Permissions

1. **Data Source Inline Policy** - Navigate to the IAM console, select the Role used for the data source, and click on "Create inline policy." Use the following JSON policy:

```
{
"Version": "2012-10-17",		 	 	 ,
"Statement": [
  {
    "Sid": "AllowsAmazonQToGetObjectfromS3",
    "Action": [
      "s3:GetObject"
    ],
    "Resource": [
      "arn:aws:s3:::<Bucket Name Here>/*"
    ],
    "Effect": "Allow",
    "Condition": {
      "StringEquals": {
        "aws:ResourceAccount": "<Cross Account AWS Account ID Here>"
      }
    }
  },
  {
    "Sid": "AllowsAmazonQToListS3Buckets",
    "Action": [
      "s3:ListBucket"
    ],
    "Resource": [
      "arn:aws:s3:::<Bucket Name Here>"
    ],
    "Effect": "Allow",
    "Condition": {
      "StringEquals": {
        "aws:ResourceAccount": "<Cross Account AWS Account ID Here>"
      }
    }
  },
  {
    "Sid": "AllowsAmazonQToIngestDocuments",
    "Effect": "Allow",
    "Action": [
      "qbusiness:BatchPutDocument",
      "qbusiness:BatchDeleteDocument"
    ],
    "Resource": "<Amazon Q Business Index ARN Here>"
  },
  {
    "Sid": "AllowsAmazonQToCallPrincipalMappingAPIs",
    "Effect": "Allow",
    "Action": [
      "qbusiness:PutGroup",
      "qbusiness:CreateUser",
      "qbusiness:DeleteGroup",
      "qbusiness:UpdateUser",
      "qbusiness:ListGroups"
    ],
    "Resource": [
      "<Amazon Q Business Application ARN Here>",
      "<Amazon Q Business Index ARN Here>",
      "<Amazon Q Business Index ARN Here>/data-source/*"
    ]
  }
]
}
```

2. **Amazon S3 Bucket Policy** - Attach the following policy to the Amazon S3 bucket policy:

```
{
"Version": "2012-10-17",		 	 	 ,
"Statement": [
  {
    "Effect": "Allow",
    "Principal": {
      "AWS": "$amazonq-s3-connector-role-arn"
    },
    "Action": [
      "s3:GetObject"
    ],
    "Resource": [
      "arn:aws:s3:::$bucket-in-other-account/*"
    ]
  },
  {
    "Effect": "Allow",
    "Principal": {
      "AWS": "$amazonq-s3-connector-role-arn"
    },
    "Action": "s3:ListBucket",
    "Resource": "arn:aws:s3:::$bucket-in-other-account"
  }
]
}
```

**To allow Amazon Q to use an Amazon S3 bucket as a data
source, use the following role policy:**

```
{
  "Version": "2012-10-17",		 	 	 ,
  "Statement": [
    {
      "Sid": "AllowsAmazonQToGetObjectfromS3",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::{{input_bucket_name}}/*"
      ],
      "Effect": "Allow",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "{{account_id}}"
        }
      }
    },
    {
      "Sid": "AllowsAmazonQToListS3Buckets",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::{{input_bucket_name}}"
      ],
      "Effect": "Allow",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "{{account_id}}"
        }
      }
    },
    {
      "Sid": "AllowsAmazonQToIngestDocuments",
      "Effect": "Allow",
      "Action": [
        "qbusiness:BatchPutDocument",
        "qbusiness:BatchDeleteDocument"
      ],
      "Resource": "arn:aws:qbusiness:{{region}}:{{source_account}}:application/{{application_id}}/index/{{index_id}}"
    },
    {
      "Sid": "AllowsAmazonQToCallPrincipalMappingAPIs",
      "Effect": "Allow",
      "Action": [
        "qbusiness:PutGroup",
        "qbusiness:CreateUser",
        "qbusiness:DeleteGroup",
        "qbusiness:UpdateUser",
        "qbusiness:ListGroups"
      ],
      "Resource": [
        "arn:aws:qbusiness:{{region}}:{{account_id}}:application/{{application_id}}",
        "arn:aws:qbusiness:{{region}}:{{account_id}}:application/{{application_id}}/index/{{index_id}}",
        "arn:aws:qbusiness:{{region}}:{{account_id}}:application/{{application_id}}/index/{{index_id}}/data-source/*"
      ]
    },
    {
      "Sid": "AllowsAmazonQToPassCustomerRole",
      "Effect": "Allow",
      "Action": [
        "iam:PassRole"
      ],
      "Resource": [
        "arn:aws:iam::{{account_id}}:role/QBusiness-DataSource-*"
      ],
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "qbusiness.amazonaws.com"
        }
      }
    }
  ]
}
```

**If the documents in the Amazon S3 bucket are encrypted, you
must provide the following permissions to use the AWS KMS key to decrypt the
documents:**

```
{
      "Sid": "AllowsAmazonQToDecryptSecret",
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt"
      ],
      "Resource": [
        "arn:aws:kms:{{region}}:{{account_id}}:key/[[key_id]]"
      ],
      "Condition": {
        "StringLike": {
          "kms:ViaService": [
            "secretsmanager.*.amazonaws.com"
          ]
        }
      }
    }
```

**If you are using an Amazon VPC, you must add the following VPC
access permissions to your policy:**

```
{
  "Version": "2012-10-17",		 	 	 ,
  "Statement": [
    {
      "Sid": "AllowsAmazonQToGetObjectfromS3",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::{{input_bucket_name}}/*"
      ],
      "Effect": "Allow",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "{{account_id}}"
        }
      }
    },
    {
      "Sid": "AllowsAmazonQToListS3Buckets",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::{{input_bucket_name}}"
      ],
      "Effect": "Allow",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "{{account_id}}"
        }
      }
    },
    {
      "Sid": "AllowsAmazonQToIngestDocuments",
      "Effect": "Allow",
      "Action": [
        "qbusiness:BatchPutDocument",
        "qbusiness:BatchDeleteDocument"
      ],
      "Resource": "arn:aws:qbusiness:{{region}}:{{source_account}}:application/{{application_id}}/index/{{index_id}}"
    },
    {
      "Sid": "AllowsAmazonQToCallPrincipalMappingAPIs",
      "Effect": "Allow",
      "Action": [
        "qbusiness:PutGroup",
        "qbusiness:CreateUser",
        "qbusiness:DeleteGroup",
        "qbusiness:UpdateUser",
        "qbusiness:ListGroups"
      ],
      "Resource": [
        "arn:aws:qbusiness:{{region}}:{{account_id}}:application/{{application_id}}",
        "arn:aws:qbusiness:{{region}}:{{account_id}}:application/{{application_id}}/index/{{index_id}}",
        "arn:aws:qbusiness:{{region}}:{{account_id}}:application/{{application_id}}/index/{{index_id}}/data-source/*"
      ]
    },
    {
      "Sid": "AllowsAmazonQToCreateAndDeleteENI",
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:DeleteNetworkInterface"
      ],
      "Resource": [
        "arn:aws:ec2:{{region}}:{{account_id}}:subnet/[[subnet_ids]]",
        "arn:aws:ec2:{{region}}:{{account_id}}:security-group/[[security_group]]"
      ]
    },
    {
      "Sid": "AllowsAmazonQToCreateDeleteENI",
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:DeleteNetworkInterface"
      ],
      "Resource": "arn:aws:ec2:{{region}}:{{account_id}}:network-interface/*",
      "Condition": {
        "StringLike": {
          "aws:RequestTag/AMAZON_Q": "qbusiness_{{account_id}}_{{application_id}}_*"
        },
        "ForAllValues:StringEquals": {
          "aws:TagKeys": [
            "AMAZON_Q"
          ]
        }
      }
    },
    {
      "Sid": "AllowsAmazonQToCreateTags",
      "Effect": "Allow",
      "Action": [
        "ec2:CreateTags"
      ],
      "Resource": "arn:aws:ec2:{{region}}:{{account_id}}:network-interface/*",
      "Condition": {
        "StringEquals": {
          "ec2:CreateAction": "CreateNetworkInterface"
        }
      }
    },
    {
      "Sid": "AllowsAmazonQToCreateNetworkInterfacePermission",
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterfacePermission"
      ],
      "Resource": "arn:aws:ec2:{{region}}:{{account_id}}:network-interface/*",
      "Condition": {
        "StringLike": {
          "aws:ResourceTag/AMAZON_Q": "qbusiness_{{account_id}}_{{application_id}}_*"
        }
      }
    },
    {
      "Sid": "AllowsAmazonQToConnectToVPC",
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeAvailabilityZones",
        "ec2:DescribeNetworkInterfaceAttribute",
        "ec2:DescribeVpcs",
        "ec2:DescribeRegions",
        "ec2:DescribeNetworkInterfacePermissions",
        "ec2:DescribeSubnets"
      ],
      "Resource": "*"
    }
  ]
}
```

**To allow Amazon Q to assume a role, use the following trust
policy:**

```
{
  "Version": "2012-10-17",		 	 	 ,
  "Statement": [
    {
      "Sid": "AllowsAmazonQToAssumeRoleForServicePrincipal",
      "Effect": "Allow",
      "Principal": {
        "Service": "qbusiness.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{source_account}}"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:qbusiness:{{region}}:{{source_account}}:application/{{application_id}}"
        }
      }
    }
  ]
}
```
