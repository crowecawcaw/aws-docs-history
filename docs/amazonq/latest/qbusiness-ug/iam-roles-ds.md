# IAM role for Amazon Q Business data source connectors

You can use either the Amazon Q Business console or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API operation to connect your data source.
However, you must first provide Amazon Q Business with an IAM role that
has permissions to access the data source resources.

If you use the console, you can either create an IAM role when you connect
your data source to Amazon Q Business or use an existing role. If you use the
`CreateDataSource` API operation, you must provide the Amazon Resource Name
(ARN) of an existing IAM role.

The specific permissions required depend on the data source. At a minimum, your IAM role must include the following:

- Permission to access the [`BatchPutDocument`](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") and [`BatchDeleteDocument`](../api-reference/API_BatchDeleteDocument.md "../api-reference/API_BatchDeleteDocument.md") API operations in
  order to ingest documents.
- Permission to access the User Store APIs needed to ingest access control and
  identity information from documents.

###### Topics

- [IAM role for Amazon Q Business data source connectors](#iam-roles-ds-general "#iam-roles-ds-general")
- [IAM role for Amazon S3 data sources](#create-s3-datasource-iam-role "#create-s3-datasource-iam-role")

## IAM role for Amazon Q Business data source connectors

When you use an Amazon Q Business data source, you require the following
permissions, depending on your use case.

**To allow Amazon Q Business to connect to your data source,
use the following least-permissions role policy:**

###### Note

This policy assumes your data source doesn't use any authentication.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowsAmazonQToIngestDocuments",
 "Effect": "Allow",
 "Action": [
 "qbusiness:BatchPutDocument",
 "qbusiness:BatchDeleteDocument"
 ],
 "Resource": [
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`",
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/index/`index-id`"
 ]
 },
 {
 "Sid": "AllowsAmazonQToIngestPrincipalMapping",
 "Effect": "Allow",
 "Action": [
 "qbusiness:PutGroup",
 "qbusiness:CreateUser",
 "qbusiness:DeleteGroup",
 "qbusiness:UpdateUser",
 "qbusiness:ListGroups"
 ],
 "Resource": [
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`",
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/index/`index-id`",
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/index/`index-id`/data-source/*"
 ]
 }
 ]
}`

```

**To allow Amazon Q Business to assume a role, you must also
use the following trust policy:**

JSON

```
`{
 "Version":"2012-10-17",
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
 "aws:SourceAccount": "111122223333"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 }
 }
 }
 ]
}`

```

**If your data source uses authentication, you must add the
following policy to your IAM role to allow Amazon Q Business to
access your AWS Secrets Manager secret:**

```
{
            "Sid": "AllowsAmazonQToGetSecret",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": [
                "arn:aws:secretsmanager:{{region}}:{{account_id}}:secret:[[secret_id]]"
            ]
        }
```

**If you are using an Amazon VPC, you must add the following
VPC access permissions to your policy:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowsAmazonQToCreateAndDeleteNI",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:us-east-1:111122223333:subnet/[[subnet_ids]]",
 "arn:aws:ec2:us-east-1:111122223333:security-group/[[security_group]]"
 ]
 },
 {
 "Sid": "AllowsAmazonQToCreateAndDeleteNIForSpecificTag",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface"
 ],
 "Resource": "arn:aws:ec2:us-east-1:111122223333:network-interface/*",
 "Condition": {
 "StringLike": {
 "aws:RequestTag/AMAZON_Q": "qbusiness_111122223333_`application-id`_*"
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
 "Resource": "arn:aws:ec2:us-east-1:111122223333:network-interface/*",
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
 "Resource": "arn:aws:ec2:us-east-1:111122223333:network-interface/*",
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/AMAZON_Q": "qbusiness_111122223333_`application-id`_*"
 }
 }
 },
 {
 "Sid": "AllowsAmazonQToDescribeResourcesForVPC",
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
}`

```

**If your Secrets Manager secret is encrypted, you must add
permissions for AWS KMS key to decrypt the username and password secret
stored by Secrets Manager:**

```
{
    "Effect": "Allow",
    "Action": [
        "kms:Decrypt"
    ],
    "Resource": [
        "arn:aws:kms:your-region:your-account-id:key/key-id"
    ],
    "Condition": {
        "StringLike": {
            "kms:ViaService": [
                "s3.*.amazonaws.com"
            ]
        }
    }

}
```

**If your Amazon Q Business data source connector needs access
to an object stored in an Amazon S3 bucket (such as an SSL certificate), you
must add the following permissions to your IAM role:**

###### Note

Check that the file path to the object in your Amazon S3 bucket is of the
following format:
`s3://BucketName/FolderName/FileName.extension`.

```
{
            "Sid": "AllowsAmazonQToGetS3Objects",
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
        }
```

## IAM role for Amazon S3 data sources

If you use the AWS CLI or an AWS SDK, you must create an AWS Identity and Access Management (IAM) policy
before you create an Amazon Q Business resource. When you call the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") operation, you provide the Amazon Resource Name (ARN) role with the
policy attached.

If you use the AWS Management Console, you can create a new IAM role in the Amazon Q console or use an existing IAM role while creating your data
source.

###### Note

To learn how to create an IAM role, see [Create a
role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

When you use an Amazon S3 bucket as a data source, you must provide a role that has
permissions to:

- Access your Amazon S3 bucket.
- Permission to access the [`BatchPutDocument`](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") and [`BatchDeleteDocument`](../api-reference/API_BatchDeleteDocument.md "../api-reference/API_BatchDeleteDocument.md") API operations in order to ingest
  documents.
- Access the Principal Store APIs needed to ingest access control and identity information
  from documents.

**To allow Amazon Q to use an Amazon S3 bucket as a
data source, use the following role policy:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowsAmazonQToGetObjectfromS3",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ],
 "Effect": "Allow",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "111122223333"
 }
 }
 },
 {
 "Sid": "AllowsAmazonQToListS3Buckets",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket"
 ],
 "Effect": "Allow",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "111122223333"
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
 "Resource": [
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`",
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/index/`index-id`"
 ]
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
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`",
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/index/`index-id`",
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/index/`index-id`/data-source/*"
 ]
 }
 ]
}`

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

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowsAmazonQToGetObjectfromS3",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ],
 "Effect": "Allow",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "111122223333"
 }
 }
 },
 {
 "Sid": "AllowsAmazonQToListS3Buckets",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket"
 ],
 "Effect": "Allow",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "111122223333"
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
 "Resource": [
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`",
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/index/`index-id`"
 ]
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
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`",
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/index/`index-id`",
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/index/`index-id`/data-source/*"
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
 "arn:aws:ec2:us-east-1:111122223333:subnet/[[subnet_ids]]",
 "arn:aws:ec2:us-east-1:111122223333:security-group/[[security_group]]"
 ]
 },
 {
 "Sid": "AllowsAmazonQToCreateDeleteENI",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface"
 ],
 "Resource": "arn:aws:ec2:us-east-1:111122223333:network-interface/*",
 "Condition": {
 "StringLike": {
 "aws:RequestTag/AMAZON_Q": "qbusiness_111122223333_`application-id`_*"
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
 "Resource": "arn:aws:ec2:us-east-1:111122223333:network-interface/*",
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
 "Resource": "arn:aws:ec2:us-east-1:111122223333:network-interface/*",
 "Condition": {
 "StringLike": {
 "aws:ResourceTag/AMAZON_Q": "qbusiness_111122223333_`application-id`_*"
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
}`

```

**To allow Amazon Q to assume a role, use the following trust
policy:**

JSON

```
`{
 "Version":"2012-10-17",
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
 "aws:SourceAccount": "111122223333"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 }
 }
 }
 ]
}`

```
