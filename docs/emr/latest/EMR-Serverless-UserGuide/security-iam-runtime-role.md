# Job runtime roles for Amazon EMR Serverless

You can specify IAM role permissions that a EMR Serverless job run can assume when
calling other services on your behalf. This includes access to Amazon S3 for any data sources,
targets, as well as other AWS resources like Amazon Redshift clusters and DynamoDB tables. To learn more
about how to create a role, refer to [Create a job runtime role](getting-started.md#gs-runtime-role "getting-started.md#gs-runtime-role").

**Sample runtime policies**

You can attach a runtime policy, such as the following, to a job runtime role. The
following job runtime policy allows:

- Read access to Amazon S3 buckets with EMR samples.
- Full access to S3 buckets.
- Create and read access to AWS Glue Data Catalog.
  To add access to other AWS resources like DynamoDB, you’ll need to include permissions for
  them in the policy when creating the runtime role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadAccessForEMRSamples",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::*.elasticmapreduce",
 "arn:aws:s3:::*.elasticmapreduce/*"
 ]
 },
 {
 "Sid": "FullAccessToS3Bucket",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Sid": "GlueCreateAndReadDataCatalog",
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabase",
 "glue:CreateDatabase",
 "glue:GetDataBases",
 "glue:CreateTable",
 "glue:GetTable",
 "glue:UpdateTable",
 "glue:DeleteTable",
 "glue:GetTables",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:CreatePartition",
 "glue:BatchCreatePartition",
 "glue:GetUserDefinedFunctions"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

**Pass role privileges**

You can attach IAM permissions policies to the a user’s role to allow the user to
pass only approved roles. This allows administrators to control which users can pass specific
job runtime roles to EMR Serverless jobs. To learn more about setting permissions, refer to [Granting a user
permissions to pass a role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md").

The following is an example policy that allows passing a job runtime role to the
EMR Serverless service principal.

```
{
     "Effect": "Allow",
     "Action": "iam:PassRole",
     "Resource": "arn:aws:iam::1234567890:role/JobRuntimeRoleForEMRServerless",
        "Condition": {
                "StringLike": {
                    "iam:PassedToService": "emr-serverless.amazonaws.com"
                }
            }
}
```

## Managed permission policies associated with runtime roles

When you submit job runs to EMR serverless through the EMR Studio console, there is a step where you choose a **Runtime role** to associate with
your application. There are underlying managed
policies associated with each selection in the console that are important to be aware of. The three selections are the following:

1. **All buckets** – When you choose this, it specifies
   the [AmazonS3FullAccess](../../../aws-managed-policy/latest/reference/AmazonS3FullAccess.md "../../../aws-managed-policy/latest/reference/AmazonS3FullAccess.md") AWS managed policy, which
   provides full access to all buckets.
2. **Specific buckets** – This specifies the Amazon resource name (ARN) identifier of each bucket
   that you choose. There isn't an underlying managed policy included.
3. **None** – No managed-policy permissions are included.

We suggest adding specific buckets. If you choose all buckets, keep in mind that it sets full access
for all buckets.
