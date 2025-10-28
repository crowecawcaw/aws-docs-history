# IAM role for Amazon Q Business Web Crawler connector

To connect Web Crawler to Amazon Q Business, you must give Amazon Q an IAM role that has the following permissions.

**If you're crawling a public website with no
authentication:**

- Permission to access the `BatchPutDocument` and
  `BatchDeleteDocument` operations to ingest documents.
- Permission to access the [User Store](connector-principal-store.md "connector-principal-store.md") operations to ingest access control
  information from documents.

```
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
                "arn:aws:qbusiness:{{region}}:{{account_id}}:application/{{application_id}}",
                "arn:aws:qbusiness:{{region}}:{{account_id}}:application/{{application_id}}/index/{{index_id}}",
                "arn:aws:qbusiness:{{region}}:{{account_id}}:application/{{application_id}}/index/{{index_id}}/data-source/*"
            ]
        }
```

**If you're crawling a website which uses
authentication:**

- Permission to access the AWS Secrets Manager secret that contains the
  credentials to connect to websites or a web proxy server backed by basic
  authentication.

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

**If your Secrets Manager secret is decrypted, add permissions
for a AWS KMS key to decrypt the username and password secret stored by Secrets
Manager:**

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

**If your Amazon Q data source connector needs access
to an object stored in an Amazon S3 bucket—like seed URLs or
sitemaps— you must add the following permissions to your IAM
role:**

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

**If you are using an Amazon VPC, you need to add the
following VPC access permissions to your policy:**

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

**To allow Amazon Q to assume a role, you must also use
the following trust policy:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowsAmazonQServicePrincipal",
 "Effect": "Allow",
 "Principal": {
 "Service": "qbusiness.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 }
 }
 }
 ]
}`

```

For more information on Amazon Q data source connector IAM
roles, see [IAM
roles for Amazon Q data source connectors](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").
