# IAM access roles for Amazon Kendra

When you create an index, data source, or an FAQ, Amazon Kendra needs access to the
AWS resources required to create the Amazon Kendra resource. You must
create a AWS Identity and Access Management (IAM) policy before you create the Amazon Kendra resource. When you call the operation, you provide the Amazon Resource Name (ARN)
of the role with the policy attached. For example, if you are calling the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md") API to add documents from an Amazon S3 bucket, you provide
Amazon Kendra with a role with a policy that has access to the bucket.

You can create a new IAM role in the Amazon Kendra console or choose an
IAM existing role to use. The console displays roles that have the string
"kendra" or "Kendra" in the role name.

The following topics provide details for the required policies. If you create IAM roles using the Amazon Kendra console these policies are created for
you.

###### Topics

- [IAM roles for indexes](#iam-roles-index "#iam-roles-index")
- [IAM roles for the BatchPutDocument
  API](#iam-roles-batch "#iam-roles-batch")
- [IAM roles for data sources](#iam-roles-ds "#iam-roles-ds")
- [Virtual private cloud (VPC) IAM role](#iam-roles-vpc "#iam-roles-vpc")
- [IAM roles for frequently asked questions
  (FAQs)](#iam-roles-ds-faq "#iam-roles-ds-faq")
- [IAM roles for query
  suggestions](#iam-roles-query-suggestions "#iam-roles-query-suggestions")
- [IAM roles for principal mapping
  of users and groups](#iam-roles-principal-mapping "#iam-roles-principal-mapping")
- [IAM roles for AWS IAM Identity Center](#iam-roles-aws-sso "#iam-roles-aws-sso")
- [IAM roles for Amazon Kendra experiences](#iam-roles-amazon-kendra-experiences "#iam-roles-amazon-kendra-experiences")
- [IAM roles for Custom
  Document Enrichment](#iam-roles-custom-document-enrichment "#iam-roles-custom-document-enrichment")

## IAM roles for indexes

When you create an index, you must provide an IAM role with permission to
write to an Amazon CloudWatch. You must also provide a trust policy that allows Amazon Kendra to assume the role. The following are the policies that must be provided.

A role policy to allow Amazon Kendra to access a CloudWatch log.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "cloudwatch:PutMetricData",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/Kendra"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "logs:DescribeLogGroups",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "logs:CreateLogGroup",
 "Resource": "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/kendra/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/kendra/*:log-stream:*"
 }
 ]
}`

```

A role policy to allow Amazon Kendra to access AWS Secrets Manager. If you are
using user context with Secrets Manager as a key location, you can use the following
policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "cloudwatch:PutMetricData",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/Kendra"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "logs:DescribeLogGroups",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "logs:CreateLogGroup",
 "Resource": "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/kendra/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/kendra/*:log-stream:*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.`us-east-1`.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

## IAM roles for the BatchPutDocument

API

###### Warning

Amazon Kendra doesn't use a bucket policy that grants permissions to an Amazon Kendra principal to interact with an S3 bucket. Instead, it uses IAM
roles. Make sure that Amazon Kendra isn't included as a trusted member in your bucket
policy to avoid any data security issues in accidentally granting permissions to arbitrary
principals. However, you can add a bucket policy to use an Amazon S3 bucket across
different accounts. For more information, see [Policies to use
Amazon S3 across accounts](iam-roles.md#iam-roles-ds-s3-cross-accounts "iam-roles.md#iam-roles-ds-s3-cross-accounts"). For information about IAM
roles for S3 data sources, see [IAM
roles](iam-roles.md#iam-roles-ds-s3 "iam-roles.md#iam-roles-ds-s3").

When you use the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md") API to
index documents in an Amazon S3 bucket, you must provide Amazon Kendra with an
IAM role with access to the bucket. You must also provide a trust policy that
allows Amazon Kendra to assume the role. If the documents in the bucket are encrypted,
you must provide permission to use the AWS KMS customer master key (CMK) to decrypt
the documents.

A required role policy to allow Amazon Kendra to access an Amazon S3
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`/*"
 ]
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

It is recommended that you include `aws:sourceAccount` and
`aws:sourceArn` in the trust policy. This limits permissions and securely
checks if `aws:sourceAccount` and `aws:sourceArn` are the same as
provided in the IAM role policy for the `sts:AssumeRole` action.
This prevents unauthorized entities from accessing your IAM roles and their
permissions. For more information, see the AWS Identity and Access Management guide on the [confused deputy
problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

An optional role policy to allow Amazon Kendra to use an AWS KMS
customer master key (CMK) to decrypt documents in an Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ]
 }
 ]
}`

```

## IAM roles for data sources

When you use the [CreateDataSource](../APIReference/API_CreateDataSource.md "../APIReference/API_CreateDataSource.md") API, you
must give Amazon Kendra an IAM role that has permission to access the
resources. The specific permissions required depend on the data source.

When you use Adobe Experience Manager, you provide a role with the following
policies.

- Permission to access your AWS Secrets Manager secret to authenticate your Adobe
  Experience Manager.
- Permission to call the required public APIs for the Adobe Experience Manager
  connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect an Adobe Experience Manager data source to Amazon Kendra
through Amazon VPC. If you are using a Amazon VPC, you need to add
[additional permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:111122223333:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:111122223333:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.us-east-1.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:PutPrincipalMapping",
 "kendra:DeletePrincipalMapping",
 "kendra:ListGroupsOlderThanOrderingId",
 "kendra:DescribePrincipalMapping"
 ],
 "Resource": [
 "arn:aws:kendra:us-east-1:111122223333:index/`index-id`",
 "arn:aws:kendra:us-east-1:111122223333:index/`index-id`/data-source/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:us-east-1:111122223333:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Alfresco, you provide a role with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Alfresco.
- Permission to call the required public APIs for the Alfresco connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect an Alfresco data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.us-east-1.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:PutPrincipalMapping",
 "kendra:DeletePrincipalMapping",
 "kendra:ListGroupsOlderThanOrderingId",
 "kendra:DescribePrincipalMapping"
 ],
 "Resource": [
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`",
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`/data-source/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Aurora (MySQL), you provide a role with the following
policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Aurora (MySQL).
- Permission to call the required public APIs for the Aurora (MySQL)
  connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect an Aurora (MySQL) data source to Amazon Kendra
through Amazon VPC. If you are using a Amazon VPC, you need to add
[additional permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Aurora (PostgreSQL), you provide a role with the following
policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Aurora (PostgreSQL).
- Permission to call the required public APIs for the Aurora
  (PostgreSQL) connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect an Aurora (PostgreSQL) data source to Amazon Kendra
through Amazon VPC. If you are using a Amazon VPC, you need to add
[additional permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Amazon FSx, you provide a role with the following
policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Amazon FSx file system.
- Permission to access Amazon Virtual Private Cloud (VPC) where your Amazon FSx
  file system resides.
- Permission to get the domain name of your Active Directory for your Amazon FSx file system.
- Permission to call the required public APIs for the Amazon FSx
  connector.
- Permission to call the `BatchPutDocument` and
  `BatchDeleteDocument` APIs to update the index.

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a database as a data source, you provide Amazon Kendra with a role
that has the permissions necessary for connecting to the . These include:

- Permission to access the AWS Secrets Manager secret that contains the user name
  and password for the site. For more information about the contents of the secret, see
  [data
  sources](datasource-.md "datasource-.md").
- Permission to use the AWS KMS customer master key (CMK) to decrypt the
  user name and password secret stored by Secrets Manager.
- Permission to use the `BatchPutDocument` and
  `BatchDeleteDocument` operations to update the index.
- Permission to access the Amazon S3 bucket that contains the SSL
  certificate used to communicate with the site.

###### Note

You can connect database data sources to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

There are two optional policies that you might use with a data source.

If you have encrypted the Amazon S3 bucket that contains the SSL certificate
used to communicate with the , provide a policy to give Amazon Kendra access to the
key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ]
 }
 ]
}`

```

If you are using a VPC, provide a policy that gives Amazon Kendra access to the
required resources. See [IAM roles for data
sources, VPC](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for the required policy.

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a Amazon RDS (Microsoft SQL Server) data source connector, you
provide a role with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Amazon RDS (Microsoft SQL Server) data source instance.
- Permission to call the required public APIs for the Amazon RDS (Microsoft
  SQL Server) data source connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect an Amazon RDS (Microsoft SQL Server) data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need
to add [additional permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a Amazon RDS (MySQL) data source connector, you provide a role
with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Amazon RDS (MySQL) data source instance.
- Permission to call the required public APIs for the Amazon RDS (MySQL)
  data source connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect an Amazon RDS (MySQL) data source to Amazon Kendra
through Amazon VPC. If you are using a Amazon VPC, you need to add
[additional permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a Amazon RDS Oracle data source connector, you provide a role
with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Amazon RDS (Oracle) data source instance.
- Permission to call the required public APIs for the Amazon RDS (Oracle)
  data source connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect an Amazon RDS Oracle data source to Amazon Kendra
through Amazon VPC. If you are using a Amazon VPC, you need to add
[additional permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a Amazon RDS (PostgreSQL) data source connector, you provide a
role with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Amazon RDS (PostgreSQL) data source instance.
- Permission to call the required public APIs for the Amazon RDS
  (PostgreSQL) data source connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect an Amazon RDS (PostgreSQL) data source to Amazon Kendra
through Amazon VPC. If you are using a Amazon VPC, you need to add
[additional permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

###### Warning

Amazon Kendra doesn't use a bucket policy that grants permissions to an Amazon Kendra principal to interact with an S3 bucket. Instead, it uses IAM roles. Make sure that Amazon Kendra isn't included as a trusted member in your
bucket policy to avoid any data security issues in accidentally granting permissions to
arbitrary principals. However, you can add a bucket policy to use an Amazon S3
bucket across different accounts. For more information, see [Policies to use Amazon S3
across accounts](#iam-roles-ds-s3-cross-accounts "#iam-roles-ds-s3-cross-accounts") (scroll down).

When you use an Amazon S3 bucket as a data source, you supply a role that has
permission to access the bucket, and to use the `BatchPutDocument` and
`BatchDeleteDocument` operations. If the documents in the Amazon S3
bucket are encrypted, you must provide permission to use the AWS KMS customer
master key (CMK) to decrypt the documents.

The following role policies must allow Amazon Kendra to assume a role. Scroll
further down to view a trust policy to assume a role.

A required role policy to allow Amazon Kendra to use an Amazon S3 bucket
as a data source.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`/*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`"
 ],
 "Effect": "Allow"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": [
 "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 ]
 }
 ]
}`

```

An optional role policy to allow Amazon Kendra to use an AWS KMS
customer master key (CMK) to decrypt documents in an Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ]
 }
 ]
}`

```

An optional role policy to allow Amazon Kendra to access an Amazon S3
bucket, while using a Amazon VPC, and without activating AWS KMS or
sharing AWS KMS permissions.

An optional role policy to allow Amazon Kendra to access an Amazon S3
bucket while using a Amazon VPC, and with AWS KMS permissions
activated.

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

#### Policies to use Amazon S3

across accounts

If your Amazon S3 bucket is in a different account to the account you use
for your Amazon Kendra index, you can create policies to use it across
accounts.

A role policy to use your Amazon S3 bucket as your data source when the
bucket is in a different account to your Amazon Kendra index. Note that
`s3:PutObject` and `s3:PutObjectAcl` are optional, and you use
this if you want to include a [configuration file for your access control
list](s3-acl.md "s3-acl.md").

A bucket policy to allow the Amazon S3 data source role to access the
Amazon S3 bucket across accounts. Note that `s3:PutObject` and
`s3:PutObjectAcl` are optional, and you use this if you want to include a
[configuration file for
your access control list](s3-acl.md "s3-acl.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "$`kendra-s3-connector-role-arn`"
 },
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": [
 "arn:aws:s3:::$`bucket-in-other-account`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "$`kendra-s3-connector-role-arn`"
 },
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::$`bucket-in-other-account`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Amazon Kendra Web Crawler, you provide a role with the following
policies:

- Permission to access the AWS Secrets Manager secret that contains the
  credentials to connect to websites or a web proxy server backed by basic
  authentication. For more information about the contents of the secret, see [Using a web
  crawler data source](data-source-web-crawler.md "data-source-web-crawler.md").
- Permission to use the AWS KMS customer master key (CMK) to decrypt the
  user name and password secret stored by Secrets Manager.
- Permission to use the `BatchPutDocument` and
  `BatchDeleteDocument` operations to update the index.
- If you use an Amazon S3 bucket to store your list of seed URLs or
  sitemaps, include permission to access the Amazon S3 bucket.

###### Note

You can connect an Amazon Kendra Web Crawler data source to Amazon Kendra
through Amazon VPC. If you are using a Amazon VPC, you need to add
[additional permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

If you store your seed URLs or sitemaps in an Amazon S3 bucket, you must add
this permission to the role.

```
,
{"Effect": "Allow",
     "Action": [
         "s3:GetObject"
      ],
      "Resource": [
         "arn:aws:s3:::`bucket-name`/*"
      ]
}
```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Box, you provide a role with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Slack.
- Permission to call the required public APIs for the Box connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect a Box data source to Amazon Kendra through Amazon VPC.
If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.us-east-1.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:PutPrincipalMapping",
 "kendra:DeletePrincipalMapping",
 "kendra:ListGroupsOlderThanOrderingId",
 "kendra:DescribePrincipalMapping"
 ],
 "Resource": [
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`",
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`/data-source/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a Confluence server as a data source, you provide a role with the
following policies:

- Permission to access the AWS Secrets Manager secret that contains the
  credentials necessary to connect to Confluence. For more information about the
  contents of the secret, see [Confluence data
  sources](data-source-confluence.md "data-source-confluence.md").
- Permission to use the AWS KMS customer master key (CMK) to decrypt
  the user name and password secret stored by Secrets Manager.
- Permission to use the `BatchPutDocument` and
  `BatchDeleteDocument` operations to update the index.

###### Note

You can connect a Confluence data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 }
 ]
}`

```

If you are using a VPC, provide a policy that gives Amazon Kendra access to
the required resources. See [IAM roles for data
sources, VPC](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for the required policy.

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

For a Confluence connector v2.0 data source, you provide a role with the following
policies.

- Permission to access the AWS Secrets Manager secret that contains the
  authentication credentials for Confluence. For more information about the contents
  of the secret, see [Confluence data
  sources](data-source-confluence.md "data-source-confluence.md").
- Permission to use the AWS KMS customer master key (CMK) to decrypt
  the user name and password secret stored by AWS Secrets Manager.
- Permission to use the `BatchPutDocument` and
  `BatchDeleteDocument` operations to update the index.
  You must also attach a trust policy that allows Amazon Kendra to assume the
  role.

###### Note

You can connect a Confluence data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

A role policy to allow Amazon Kendra to connect to Confluence.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:PutPrincipalMapping",
 "kendra:DeletePrincipalMapping",
 "kendra:ListGroupsOlderThanOrderingId",
 "kendra:DescribePrincipalMapping"
 ],
 "Resource": [
 "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`",
 "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`/data-source/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Dropbox, you provide a role with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Dropbox.
- Permission to call the required public APIs for the Dropbox connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect a Dropbox data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:111122223333:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:111122223333:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.us-east-1.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:PutPrincipalMapping",
 "kendra:DeletePrincipalMapping",
 "kendra:ListGroupsOlderThanOrderingId",
 "kendra:DescribePrincipalMapping"
 ],
 "Resource": [
 "arn:aws:kendra:us-east-1:111122223333:index/`index-id`",
 "arn:aws:kendra:us-east-1:111122223333:index/`index-id`/data-source/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:us-east-1:111122223333:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Drupal, you provide a role with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Drupal.
- Permission to call the required public APIs for the Drupal connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect a Drupal data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:111122223333:secret:`secret_id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:111122223333:key/`key_id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.*.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:PutPrincipalMapping",
 "kendra:DeletePrincipalMapping",
 "kendra:ListGroupsOlderThanOrderingId",
 "kendra:DescribePrincipalMapping"
 ],
 "Resource": [
 "arn:aws:kendra:us-east-1:111122223333:index/`index_id`",
 "arn:aws:kendra:us-east-1:111122223333:index/`index_id`/data-source/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:us-east-1:111122223333:index/`index_id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use GitHub, you provide a role with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  GitHub.
- Permission to call the required public APIs for the GitHub connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect a GitHub data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.us-east-1.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:PutPrincipalMapping",
 "kendra:DeletePrincipalMapping",
 "kendra:ListGroupsOlderThanOrderingId",
 "kendra:DescribePrincipalMapping"
 ],
 "Resource": [
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`",
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`/data-source/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Gmail, you provide a role with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Gmail.
- Permission to call the required public APIs for the Gmailconnector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect a Gmail data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.us-east-1.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:PutPrincipalMapping",
 "kendra:DeletePrincipalMapping",
 "kendra:ListGroupsOlderThanOrderingId",
 "kendra:DescribePrincipalMapping"
 ],
 "Resource": [
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`",
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`/data-source/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a Google Workspace Drive data source, you provide Amazon Kendra with
a role that has the permissions necessary for connecting to the site. These include:

- Permission to get and decrypt the AWS Secrets Manager secret that contains the
  client account email, admin account email, and private key necessary to connect to the
  Google Drive site. For more information about the contents of the secret, see [Google
  Drive data sources](data-source-google-drive.md "data-source-google-drive.md").
- Permission to use the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md")
  and [BatchDeleteDocument](../APIReference/API_BatchDeleteDocument.md "../APIReference/API_BatchDeleteDocument.md") APIs.

###### Note

You can connect a Google Drive data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

The following IAM policy provides the necessary permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use an IBM DB2 data source connector, you provide a role with the following
policies.

- Permission to access your AWS Secrets Manager secret to authenticate your IBM
  DB2 data source instance.
- Permission to call the required public APIs for the IBM DB2 data source
  connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect an IBM DB2 data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Jira, you provide a role with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Jira.
- Permission to call the required public APIs for the Jira connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect a Jira data source to Amazon Kendra through Amazon VPC.
If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.us-east-1.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:PutPrincipalMapping",
 "kendra:DeletePrincipalMapping",
 "kendra:ListGroupsOlderThanOrderingId",
 "kendra:DescribePrincipalMapping"
 ],
 "Resource": [
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`",
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`/data-source/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a Microsoft Exchange data source, you provide Amazon Kendra with a
role that has the permissions necessary for connecting to the site. These include:

- Permission to get and decrypt the AWS Secrets Manager secret that contains the
  application ID and secret key necessary to connect to the Microsoft Exchange site. For
  more information about the contents of the secret, see [Microsoft Exchange data
  sources](data-source-exchange.md "data-source-exchange.md").
- Permission to use the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md")
  and [BatchDeleteDocument](../APIReference/API_BatchDeleteDocument.md "../APIReference/API_BatchDeleteDocument.md") APIs.

###### Note

You can connect a Microsoft Exchange data source to Amazon Kendra through
Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

The following IAM policy provides the necessary permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 }
 ]
}`

```

If you are storing the list of users to index in an Amazon S3 bucket, you must
also provide permission to use the S3 `GetObject` operation. The following
IAM policy provides the necessary permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`/*"
 ],
 "Effect": "Allow"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-ids`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.`us-east-1`.amazonaws.com",
 "s3.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a Microsoft OneDrive data source, you provide Amazon Kendra with a
role that has the permissions necessary for connecting to the site. These include:

- Permission to get and decrypt the AWS Secrets Manager secret that contains the
  application ID and secret key necessary to connect to the OneDrive site. For more
  information about the contents of the secret, see [Microsoft OneDrive data
  sources](data-source-onedrive.md "data-source-onedrive.md").
- Permission to use the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md")
  and [BatchDeleteDocument](../APIReference/API_BatchDeleteDocument.md "../APIReference/API_BatchDeleteDocument.md") APIs.

###### Note

You can connect a Microsoft OneDrive data source to Amazon Kendra through
Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

The following IAM policy provides the necessary permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 }
 ]
}`

```

If you are storing the list of users to index in an Amazon S3 bucket, you must
also provide permission to use the S3 `GetObject` operation. The following
IAM policy provides the necessary permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`/*"
 ],
 "Effect": "Allow"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-ids`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.`us-east-1`.amazonaws.com",
 "s3.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

For a Microsoft SharePoint connector v1.0 data source, you provide a role with the
following policies.

- Permission to access the AWS Secrets Manager secret that contains the user
  name and password for the SharePoint site. For more information about the contents
  of the secret, see [Microsoft SharePoint data
  sources](data-source-sharepoint.md "data-source-sharepoint.md").
- Permission to use the AWS KMS customer master key (CMK) to decrypt
  the user name and password secret stored by AWS Secrets Manager.
- Permission to use the `BatchPutDocument` and
  `BatchDeleteDocument` operations to update the index.
- Permission to access the Amazon S3 bucket that contains the SSL
  certificate used to communicate with the SharePoint site.
  You must also attach a trust policy that allows Amazon Kendra to assume the
  role.

###### Note

You can connect a Microsoft SharePoint data source to Amazon Kendra through
Amazon VPC. If you are using a Amazon VPC, you need to add [additional permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": [
 "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "kendra.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`/*"
 ]
 }
 ]
}`

```

If you have encrypted the Amazon S3 bucket that contains the SSL
certificate used to communicate with the SharePoint site, provide a policy to give
Amazon Kendra access to the key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ]
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

For a Microsoft SharePoint connector v2.0 data source, you provide a role with the
following policies.

- Permission to access the AWS Secrets Manager secret that contains the
  authentication credentials for the SharePoint site. For more information about the
  contents of the secret, see [Microsoft SharePoint data
  sources](data-source-sharepoint.md "data-source-sharepoint.md").
- Permission to use the AWS KMS customer master key (CMK) to decrypt
  the user name and password secret stored by AWS Secrets Manager.
- Permission to use the `BatchPutDocument` and
  `BatchDeleteDocument` operations to update the index.
- Permission to access the Amazon S3 bucket that contains the SSL
  certificate used to communicate with the SharePoint site.
  You must also attach a trust policy that allows Amazon Kendra to assume the
  role.

###### Note

You can connect a Microsoft SharePoint data source to Amazon Kendra through
Amazon VPC. If you are using a Amazon VPC, you need to add [additional permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

If you have encrypted the Amazon S3 bucket that contains the SSL
certificate used to communicate with the SharePoint site, provide a policy to give
Amazon Kendra access to the key.

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Microsoft SQL Server, you provide a role with the following
policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Microsoft SQL Server instance.
- Permission to call the required public APIs for the Microsoft SQL Server
  connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect a Microsoft SQL Server data source to Amazon Kendra through
Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a Microsoft Teams data source, you provide Amazon Kendra with a role
that has the permissions necessary for connecting to the site. These include:

- Permission to get and decrypt the AWS Secrets Manager secret that contains the
  client ID and client secret necessary to connect to Microsoft Teams. For more
  information about the contents of the secret, see [Microsoft Teams data
  sources](data-source-teams.md "data-source-teams.md").

###### Note

You can connect a Microsoft Teams data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

The following IAM policy provides the necessary permissions:

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a Microsoft Yammer data source, you provide Amazon Kendra with a
role that has the permissions necessary for connecting to the site. These include:

- Permission to get and decrypt the AWS Secrets Manager secret that contains the
  application ID and secret key necessary to connect to the Microsoft Yammer site. For
  more information about the contents of the secret, see [Microsoft Yammer data
  sources](data-source-yammer.md "data-source-yammer.md").
- Permission to use the [BatchPutDocument](../APIReference/API_BatchPutDocument.md "../APIReference/API_BatchPutDocument.md")
  and [BatchDeleteDocument](../APIReference/API_BatchDeleteDocument.md "../APIReference/API_BatchDeleteDocument.md") APIs.

###### Note

You can connect a Microsoft Yammer data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

The following IAM policy provides the necessary permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 }
 ]
}`

```

If you are storing the list of users to index in an Amazon S3 bucket, you must
also provide permission to use the S3 `GetObject` operation. The following
IAM policy provides the necessary permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`/*"
 ],
 "Effect": "Allow"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-ids`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.`us-east-1`.amazonaws.com",
 "s3.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a My SQL data source connector, you provide a role with the following
policies.

- Permission to access your AWS Secrets Manager secret to authenticate your My
  SQL data source instance.
- Permission to call the required public APIs for the My SQL data source
  connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect a MySQL data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a Oracle data source connector, you provide a role with the following
policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Oracle data source instance.
- Permission to call the required public APIs for the Oracle data source
  connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect a Oracle data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a PostgreSQL data source connector, you provide a role with the following
policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  PostgreSQL data source instance.
- Permission to call the required public APIs for the PostgreSQL data source
  connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect a PostgreSQL data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Quip, you provide a role with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Quip.
- Permission to call the required public APIs for the Quip connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect a Quip data source to Amazon Kendra through Amazon VPC.
If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.us-east-1.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:PutPrincipalMapping",
 "kendra:DeletePrincipalMapping",
 "kendra:ListGroupsOlderThanOrderingId",
 "kendra:DescribePrincipalMapping"
 ],
 "Resource": [
 "arn:aws:kendra:us-east-1:`123456789012`:index/`your-index-id`",
 "arn:aws:kendra:us-east-1:`123456789012`:index/`your-index-id`/data-source/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a Salesforce as a data source, you provide a role with the following
policies:

- Permission to access the AWS Secrets Manager secret that contains the user name
  and password for the Salesforce site. For more information about the contents of the
  secret, see [Salesforce data
  sources](data-source-salesforce.md "data-source-salesforce.md").
- Permission to use the AWS KMS customer master key (CMK) to decrypt the
  user name and password secret stored by Secrets Manager.
- Permission to use the `BatchPutDocument` and
  `BatchDeleteDocument` operations to update the index.

###### Note

You can connect a Salesforce data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use a ServiceNow as a data source, you provide a role with the following
policies:

- Permission to access the Secrets Manager secret that contains the user name and
  password for the ServiceNow site. For more information about the contents of the
  secret, see [ServiceNow data
  sources](data-source-servicenow.md "data-source-servicenow.md").
- Permission to use the AWS KMS customer master key (CMK) to decrypt the
  user name and password secret stored by Secrets Manager.
- Permission to use the `BatchPutDocument` and
  `BatchDeleteDocument` operations to update the index.

###### Note

You can connect a ServiceNow data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Slack, you provide a role with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Slack.
- Permission to call the required public APIs for the Slack connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect a Slack data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.us-east-1.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:PutPrincipalMapping",
 "kendra:DeletePrincipalMapping",
 "kendra:ListGroupsOlderThanOrderingId",
 "kendra:DescribePrincipalMapping"
 ],
 "Resource": [
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`",
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`/data-source/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

When you use Zendesk, you provide a role with the following policies.

- Permission to access your AWS Secrets Manager secret to authenticate your
  Zendesk Suite.
- Permission to call the required public APIs for the Zendesk connector.
- Permission to call the `BatchPutDocument`,
  `BatchDeleteDocument`, `PutPrincipalMapping`,
  `DeletePrincipalMapping`, `DescribePrincipalMapping`, and
  `ListGroupsOlderThanOrderingId` APIs.

###### Note

You can connect a Zendesk data source to Amazon Kendra through Amazon VPC. If you are using a Amazon VPC, you need to add [additional
permissions](iam-roles.md#iam-roles-vpc "iam-roles.md#iam-roles-vpc").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:`123456789012`:secret:`secret-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.us-east-1.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:PutPrincipalMapping",
 "kendra:DeletePrincipalMapping",
 "kendra:ListGroupsOlderThanOrderingId",
 "kendra:DescribePrincipalMapping"
 ],
 "Resource": [
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`",
 "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`/data-source/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kendra:BatchPutDocument",
 "kendra:BatchDeleteDocument"
 ],
 "Resource": "arn:aws:kendra:us-east-1:`123456789012`:index/`index-id`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

## Virtual private cloud (VPC) IAM role

If you use a virtual private cloud (VPC) to connect to your data source, you must provide
the following additional permissions.

```
{
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:DeleteNetworkInterface"
      ],
      "Resource": [
        "arn:aws:ec2:{{`region`}}:{{`account_id`}}:subnet/[[`subnet_ids`]]",
        "arn:aws:ec2:{{`region`}}:{{`account_id`}}:security-group/[[`security_group`]]"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:DeleteNetworkInterface"
      ],
      "Resource": "arn:aws:ec2:{{`region`}}:{{`account_id`}}:network-interface/*",
      "Condition": {
        "StringLike": {
          "aws:RequestTag/AWS_KENDRA": "kendra_{{`account_id`}}_{{`index_id`}}_*"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateTags"
      ],
      "Resource": "arn:aws:ec2:{{`region`}}:{{`account_id`}}:network-interface/*",
      "Condition": {
        "StringEquals": {
          "ec2:CreateAction": "CreateNetworkInterface"
        }
      }
    },

{
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterfacePermission"
      ],
      "Resource": "arn:aws:ec2:{{`region`}}:{{`account_id`}}:network-interface/*",
      "Condition": {
        "StringLike": {
          "aws:ResourceTag/AWS_KENDRA": "kendra_{{`account_id`}}_{{`index_id`}}_*"
        }
      }
    },
    {
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
}
```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

## IAM roles for frequently asked questions

(FAQs)

When you use the [CreateFaq](../APIReference/API_CreateFaq.md "../APIReference/API_CreateFaq.md") API to load questions
and answers into an index, you must provide Amazon Kendra with an IAM role
with access to the Amazon S3 bucket that contains the source files. If the source
files are encrypted, you must provide permission to use the AWS KMS customer master
key (CMK) to decrypt the files.

A required role policy to allow Amazon Kendra to access an Amazon S3
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`/*"
 ]
 }
 ]
}`

```

An optional role policy to allow Amazon Kendra to use an AWS KMS
customer master key (CMK) to decrypt files in an Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "kendra.`us-east-1`.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

## IAM roles for query

suggestions

When you use an Amazon S3 file as a query suggestions block list, you supply a
role that has permission to access the Amazon S3 file and the Amazon S3
bucket. If the block list text file (the Amazon S3 file) in the Amazon S3
bucket is encrypted, you must provide permission to use the AWS KMS customer master
key (CMK) to decrypt the documents.

A required role policy to allow Amazon Kendra to use the Amazon S3 file
as your query suggestions block list.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {"Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`/*"
 ]
 }
 ]
}`

```

An optional role policy to allow Amazon Kendra to use an AWS KMS
customer master key (CMK) to decrypt documents in an Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ]
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

## IAM roles for principal mapping

of users and groups

When you use the [PutPrincipalMapping](../APIReference/API_PutPrincipalMapping.md "../APIReference/API_PutPrincipalMapping.md")
API to map users to their groups for filtering search results by user context, you need to
provide a list of users or sub groups that belong to a group. If your list is more than 1000
users or sub groups for a group, you need to supply a role that has permission to access the
Amazon S3 file of your list and the Amazon S3 bucket. If the text file (the
Amazon S3 file) of the list in the Amazon S3 bucket is encrypted, you must
provide permission to use the AWS KMS customer master key (CMK) to decrypt the
documents.

A required role policy to allow Amazon Kendra to use the Amazon S3 file
as your list of users and sub groups that belong to a group.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {"Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`/*"
 ]
 }
 ]
}`

```

An optional role policy to allow Amazon Kendra to use an AWS KMS
customer master key (CMK) to decrypt documents in an Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ]
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

It is recommended that you include `aws:sourceAccount` and
`aws:sourceArn` in the trust policy. This limits permissions and securely
checks if `aws:sourceAccount` and `aws:sourceArn` are the same as
provided in the IAM role policy for the `sts:AssumeRole` action.
This prevents unauthorized entities from accessing your IAM roles and their
permissions. For more information, see the AWS Identity and Access Management guide on the [confused deputy
problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

## IAM roles for AWS IAM Identity Center

When you use the [UserGroupResolutionConfiguration](../APIReference/API_UserGroupResolutionConfiguration.md "../APIReference/API_UserGroupResolutionConfiguration.md") object to fetch access levels of groups and users
from an AWS IAM Identity Center identity source, you need to supply a role that has permission
to access IAM Identity Center.

A required role policy to allow Amazon Kendra to access IAM Identity Center.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sso-directory:SearchUsers",
 "sso-directory:ListGroupsForUser",
 "sso-directory:DescribeGroups",
 "sso:ListDirectoryAssociations"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "iamPassRole",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "kendra.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

## IAM roles for Amazon Kendra experiences

When you use the [CreateExperience](../APIReference/API_CreateExperience.md "../APIReference/API_CreateExperience.md") or
[UpdateExperience](../APIReference/API_UpdateExperience.md "../APIReference/API_UpdateExperience.md") APIs to create or update a search application, you must supply a
role that has permission to access the necessary operations and IAM Identity Center.

A required role policy to allow Amazon Kendra to access `Query`
operations, `QuerySuggestions` operations, `SubmitFeedback`
operations, and IAM Identity Center that stores your user and group information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowsKendraSearchAppToCallKendraApi",
 "Effect": "Allow",
 "Action": [
 "kendra:GetQuerySuggestions",
 "kendra:Query",
 "kendra:DescribeIndex",
 "kendra:ListFaqs",
 "kendra:DescribeDataSource",
 "kendra:ListDataSources",
 "kendra:DescribeFaq",
 "kendra:SubmitFeedback"
 ],
 "Resource": [
 "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`"
 ]
 },
 {
 "Sid": "AllowKendraSearchAppToDescribeDataSourcesAndFaq",
 "Effect": "Allow",
 "Action": [
 "kendra:DescribeDataSource",
 "kendra:DescribeFaq"
 ],
 "Resource": [
 "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`/data-source/`data-source-id`",
 "arn:aws:kendra:`us-east-1`:`123456789012`:index/`index-id`/faq/`faq-id`"
 ]
 },
 {
 "Sid": "AllowKendraSearchAppToCallSSODescribeUsersAndGroups",
 "Effect": "Allow",
 "Action": [
 "sso-directory:ListGroupsForUser",
 "sso-directory:SearchGroups",
 "sso-directory:SearchUsers",
 "sso-directory:DescribeUser",
 "sso-directory:DescribeGroup",
 "sso-directory:DescribeGroups",
 "sso-directory:DescribeUsers",
 "sso:ListDirectoryAssociations"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "kendra.`us-east-1`.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

It is recommended that you include `aws:sourceAccount` and
`aws:sourceArn` in the trust policy. This limits permissions and securely
checks if `aws:sourceAccount` and `aws:sourceArn` are the same as
provided in the IAM role policy for the `sts:AssumeRole` action.
This prevents unauthorized entities from accessing your IAM roles and their
permissions. For more information, see the AWS Identity and Access Management guide on the [confused deputy
problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

## IAM roles for Custom

Document Enrichment

When you use the [CustomDocumentEnrichmentConfiguration](../APIReference/API_CustomDocumentEnrichmentConfiguration.md "../APIReference/API_CustomDocumentEnrichmentConfiguration.md") object to apply advanced alterations of your
document metadata and content, you must supply a role that has the required permissions to run
`PreExtractionHookConfiguration` and/or
`PostExtractionHookConfiguration`. You configure a Lambda function for
`PreExtractionHookConfiguration` and/or
`PostExtractionHookConfiguration` to apply advanced alterations of your document
metadata and content during the ingestion process. If you choose to activate Server Side
Encryption for your Amazon S3 bucket, you must provide permission to use the AWS KMS customer master key (CMK) to encrypt and decrypt the objects stored in your
Amazon S3 bucket.

A required role policy to allow Amazon Kendra to run
`PreExtractionHookConfiguration` and
`PostExtractionHookConfiguration` with encryption for your Amazon S3
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`/*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`"
 ],
 "Effect": "Allow"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:`us-east-1`:`123456789012`:function:`lambda-function`"
 }
 ]
}`

```

An optional role policy to allow Amazon Kendra to run
`PreExtractionHookConfiguration` and
`PostExtractionHookConfiguration` without encryption for your Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`/*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`"
 ],
 "Effect": "Allow"
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:`us-east-1`:`123456789012`:function:`lambda-function`"
 }
 ]
}`

```

A trust policy to allow Amazon Kendra to assume a role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"kendra.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

It is recommended that you include `aws:sourceAccount` and
`aws:sourceArn` in the trust policy. This limits permissions and securely
checks if `aws:sourceAccount` and `aws:sourceArn` are the same as
provided in the IAM role policy for the `sts:AssumeRole` action.
This prevents unauthorized entities from accessing your IAM roles and their
permissions. For more information, see the AWS Identity and Access Management guide on the [confused deputy
problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").
