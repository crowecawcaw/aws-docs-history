# Prerequisites for managing Amazon Redshift namespaces in the AWS Glue Data Catalog

1. Create a data lake administrator - Create an IAM role that is authorized to accept
   the namespace invitation, and creates the AWS Glue Data Catalog objects (catalogs, databases,
   tables/views), and grant Lake Formation permissions to other users.

For step-by-step instructions on creating a data lake administrator, see [Create a data lake administrator](initial-lf-config.md#create-data-lake-admin "initial-lf-config.md#create-data-lake-admin"). 2. Update data lake administrator permissions.

In addition to data lake administrator permissions, the data lake administrator
requires the following permissions to accept an Amazon Redshift namespace invitation in Lake Formation, create
or update the Data Catalog resources, and enable data lake access:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "glue-enable-datalake-access",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "redshift:AssociateDataShareConsumer",
 "redshift:DescribeDataSharesForConsumer",
 "redshift:DescribeDataShares",
 "redshift-serverless:CreateNamespace",
 "redshift-serverless:CreateWorkgroup",
 "redshift-serverless:DeleteNamespace",
 "redshift-serverless:DeleteWorkgroup",
 "ec2:DescribeAccountAttributes",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeAvailabilityZones",
 "s3:createBucket",
 "s3:deleteBucket",
 "s3:putBucketPolicy",
 "s3:putEncryptionConfiguration",
 "s3:putLifecycleConfiguration",
 "s3:putBucketVersioning",
 "iam:CreateRole"
 ],
 "Resource": "*"
 },
 {
 "Action": [
 "iam:PassRole"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/`data transfer role name`",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": [
 "glue.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

3. If the IAM role used for creating federated catalogs is not a data lake administrator, you need to grant the role the `Create catalog` permission.

###### To create catalog creators

    1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
    2. Choose **Administrative roles and tasks** under **Administration**.
    3. Choose **Grant.**
    4. On the **Grant permissions** screen, choose an IAM user or role.
    5. Select **Create catalog** permission.
    6. Optionally, you can also grant grantable **Create catalog** permission. Grantable permission allows the catalog creator to
     grant the `Create catalog` permission to other principals.
    7. Choose **Grant**.

AWS CLI example for granting permissions to create a federated catalog.

```
aws lakeformation grant-permissions \
--cli-input-json \
'{
    "Principal": {
     "DataLakePrincipalIdentifier":"arn:aws:iam::123456789012:role/Admin"
    },
    "Resource": {
        "Catalog": {
        }
    },
    "Permissions": [
        "CREATE_CATALOG",
        "DESCRIBE"
    ]
}'

```

4. Create a read only administrator role to discover the Amazon Redshift federated catalogs in the
   Data Catalog from Amazon Redshift Query Editor v2.

To query the Amazon Redshift tables in the federated catalog from Amazon Redshift Query Editor v2, ensure that
the Read only administrator role policy contains the ARN for the Amazon Redshift service-linked
role-`AWSServiceRoleForRedshift`.

```
 aws lakeformation put-data-lake-settings
        --region us-east-1 \
        --data-lake-settings \
 '{
   "DataLakeAdmins": [{"DataLakePrincipalIdentifier":"arn:aws:iam::123456789012:role/Admin"}],
   "ReadOnlyAdmins":[{"DataLakePrincipalIdentifier":"arn:aws:iam::123456789012:role/aws-service-role/redshift.amazonaws.com/AWSServiceRoleForRedshift"}],
   "CreateDatabaseDefaultPermissions":[],
   "CreateTableDefaultPermissions":[],
   "Parameters":{"CROSS_ACCOUNT_VERSION":"4","SET_CONTEXT":"TRUE"}
  }'

```

5. Create a data transfer role that Amazon Redshift can assume on your behalf to transfer data to and from the Amazon S3 bucket.

When you enable data lake access for Apache Iceberg compatible query engines
such as Athena, Amazon EMR on Amazon EC2 to access the Amazon Redshift resources in the Data Catalog, you need to
create an IAM role with the required permissions to perform data transfer to and from
the Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "glue-enable-datalake-access",
 "Statement": [{
 "Sid": "DataTransferRolePolicy",
 "Effect": "Allow",
 "Action": [ "glue:GetCatalog",
 "glue:GetDatabase",
 "kms:GenerateDataKey",
 "kms:Decrypt"],
 "Resource": "*"
 }
 ]
}`

```

6. Add the following trust policy to the data transfer role for AWS Glue and Amazon Redshift services to assume the role to transfer data to and from the Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "redshift.amazonaws.com",
 "glue.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }]
}`

```

7. Add the following key policy to the AWS KMS key if you're using a customer managed key to encrypt the data in the Amazon Redshift cluster/namespace.
   Replace the account number with a valid AWS account number, and specify data transfer role name.
   By default, the data in the Amazon Redshift cluster is encrypted using an KMS key.
   Lake Formation provides an option to create your custom KMS key for encryption.
   If you're using a customer managed key, you must add specific key policies to the key.

For more information about managing the permissions of a customer managed key,
see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk").

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "auto-redshift-3",
 "Statement": [{
 "Sid": "RedshiftAllowAccessPolicy",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:CreateGrant",
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:CallerAccount": "`111122223333`",
 "kms:ViaService": "redshift.us-east-1.amazonaws.com"
 }
 }
 },
 {
 "Sid": "RedshiftServerlessAllowAccessPolicy",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:CreateGrant",
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:CallerAccount": "`111122223333`",
 "kms:ViaService": "redshift-serverless.us-east-1.amazonaws.com"
 }
 }
 },
 {
 "Sid": "DirectMetadataAccess",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "kms:Describe*",
 "kms:Get*",
 "kms:List*",
 "kms:RevokeGrant"
 ],
 "Resource": "*"
 },
 {
 "Sid": "GenerateDataKeyDecryptDataTransferRole",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`data-transfer-role-name`"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "`s3.us-east-1.amazonaws.com`"
 }
 }
 }
 ]
}`

```
