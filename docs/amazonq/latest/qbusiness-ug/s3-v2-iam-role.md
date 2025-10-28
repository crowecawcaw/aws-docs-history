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
