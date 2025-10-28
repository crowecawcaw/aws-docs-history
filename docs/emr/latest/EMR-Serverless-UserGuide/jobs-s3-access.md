# Accessing S3 data in another AWS account from

EMR Serverless

You can run Amazon EMR Serverless jobs from one AWS account and configure them to access
data in Amazon S3 buckets that belong to another AWS account. This page describes how to
configure cross-account access to S3 from EMR Serverless.

Jobs that run on EMR Serverless can use an S3 bucket policy or an assumed role to access
data in Amazon S3 from a different AWS account.

## Prerequisites

To set up cross-account access for Amazon EMR Serverless, complete tasks while
signed in to two AWS accounts:

- `AccountA` – This is the AWS
  account where you have created an Amazon EMR Serverless application. Before you set up
  cross-account access, have the following ready in this account:
  - An Amazon EMR Serverless application where you want to run jobs.
  - A job execution role that has the required permissions to run jobs in the
    application. For more information, refer to [Job runtime roles for Amazon EMR Serverless](security-iam-runtime-role.md "security-iam-runtime-role.md").

- `AccountB` – This is the AWS
  account that contains the S3 bucket that you want your Amazon EMR Serverless jobs to
  access.

## Use an S3 bucket policy to access

cross-account S3 data

To access the S3 bucket in account B from account A,
attach the following policy to the S3 bucket in account B.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ExamplePermissions1",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::my-bucket-name"
 ]
 },
 {
 "Sid": "ExamplePermissions2",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::my-bucket-name/*"
 ]
 }
 ]
}`

```

For more information about S3 cross-account access with S3 bucket policies, refer to [Example
2: Bucket owner granting cross-account bucket permissions](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md") in the _Amazon Simple Storage Service User Guide_.

## Use an assumed role to access

cross-account S3 data

Another way to set up cross-account access for Amazon EMR Serverless is with the
`AssumeRole` action from the AWS Security Token Service (AWS STS). AWS STS is a global web service
that lets you request temporary, limited-privilege credentials for users. You can make API
calls to EMR Serverless and Amazon S3 with the temporary security credentials that you create
with `AssumeRole`.

The following steps illustrate how to use an assumed role to access cross-account S3
data from EMR Serverless:

1. Create an Amazon S3 bucket, `cross-account-bucket`, in
   `AccountB`. For more information, refer to [Creating a bucket](../../../AmazonS3/latest/gsg/CreatingABucket.md "../../../AmazonS3/latest/gsg/CreatingABucket.md") in the
   _Amazon Simple Storage Service User Guide_. If you want to have cross-account access to
   DynamoDB, also create a DynamoDB table in `AccountB`. For more information,
   refer to [Creating a
   DynamoDB table](../../../amazondynamodb/latest/developerguide/getting-started-step-1.md "../../../amazondynamodb/latest/developerguide/getting-started-step-1.md") in the _Amazon DynamoDB Developer Guide_.
2. Create a `Cross-Account-Role-B` IAM role in `AccountB` that
   can access the `cross-account-bucket`.
   1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   2. Choose **Roles** and create a new role:
      `Cross-Account-Role-B`. For more information about how to create IAM
      roles, refer to [Creating IAM roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") in
      the IAM User Guide.
   3. Create an IAM policy that specifies the permissions for
      `Cross-Account-Role-B` to access the
      `cross-account-bucket` S3 bucket, as the following policy
      statement demonstrates. Then attach the IAM policy to
      `Cross-Account-Role-B`. For more information, refer to [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:*"
 ],
 "Resource": [
 "arn:aws:s3:::`cross-account-bucket`",
 "arn:aws:s3:::`cross-account-bucket`/*"
 ],
 "Sid": "AllowS3"
 }
 ]
}`

```

If you require DynamoDB access, create an IAM policy that specifies permissions to
access the cross-account DynamoDB table. Then attach the IAM policy to
`Cross-Account-Role-B`. For more information, refer to [Amazon DynamoDB: Allows access to a specific table](../../../IAM/latest/UserGuide/reference_policies_examples_dynamodb_specific-table.md "../../../IAM/latest/UserGuide/reference_policies_examples_dynamodb_specific-table.md") in the _IAM User Guide_.

The following is a policy to allow access to the DynamoDB table
`CrossAccountTable`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:*"
 ],
 "Resource": [
 "arn:aws:dynamodb:*:123456789012:table/CrossAccountTable"
 ],
 "Sid": "AllowDYNAMODB"
 }
 ]
}`

```

3. Edit the trust relationship for the `Cross-Account-Role-B` role.
   1. To configure the trust relationship for the role, choose the **Trust
      Relationships** tab in the IAM console for the role
      `Cross-Account-Role-B` that you created in Step 2.
   2. Select **Edit Trust Relationship**.
   3. Add the following policy document. This allows `Job-Execution-Role-A`
      in `AccountA` to assume the `Cross-Account-Role-B`
      role.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "sts:AssumeRole"
    ],
    "Resource": "arn:aws:iam::123456789012:role/Job-Execution-Role-A",
    "Sid": "AllowSTSAssumerole"
    }
    ]
   }`

   ```

4. Grant `Job-Execution-Role-A` in `AccountA` the AWS STS
   `AssumeRole` permission to assume `Cross-Account-Role-B`.
   1. In the IAM console for AWS account `AccountA`, select
      `Job-Execution-Role-A`.
   2. Add the following policy statement to the `Job-Execution-Role-A` to
      allow the `AssumeRole` action on the `Cross-Account-Role-B`
      role.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "sts:AssumeRole"
    ],
    "Resource": [
    "arn:aws:iam::123456789012:role/Cross-Account-Role-B"
    ],
    "Sid": "AllowSTSAssumerole"
    }
    ]
   }`

   ```

## Assumed role examples

Use a single assumed role to access all S3 resources in an account, or with Amazon EMR
6.11 and higher, configure multiple IAM roles to assume when you access different
cross-account S3 buckets.

###### Topics

- [Access S3 resources with one
  assumed role](#jobs-s3-access-how-to-assumed-role-single "#jobs-s3-access-how-to-assumed-role-single")
- [Access S3 resources with
  multiple assumed roles](#jobs-s3-access-how-to-assumed-role-multiple "#jobs-s3-access-how-to-assumed-role-multiple")

### Access S3 resources with one

assumed role

###### Note

When you configure a job to use a single assumed role, all S3 resources throughout
the job use that role, including the `entryPoint` script.

If you want to use a single assumed role to access all S3 resources in account B,
specify the following configurations:

1. Specify EMRFS configuration `fs.s3.customAWSCredentialsProvider` to
   `com.amazonaws.emr.AssumeRoleAWSCredentialsProvider`.
2. For Spark, use
   `spark.emr-serverless.driverEnv.ASSUME_ROLE_CREDENTIALS_ROLE_ARN` and
   `spark.executorEnv.ASSUME_ROLE_CREDENTIALS_ROLE_ARN` to specify the
   environment variables on driver and executors.
3. For Hive, use
   `hive.emr-serverless.launch.env.ASSUME_ROLE_CREDENTIALS_ROLE_ARN`,
   `tez.am.emr-serverless.launch.env.ASSUME_ROLE_CREDENTIALS_ROLE_ARN`, and
   `tez.task.emr-serverless.launch.env.ASSUME_ROLE_CREDENTIALS_ROLE_ARN` to
   specify the environment variables on Hive driver, Tez application primary, and Tez task
   containers.

The following examples demonstrate how to use an assumed role to start an EMR Serverless job
run with cross-account access.

Spark
The following example shows how to use an assumed role to start an
EMR Serverless Spark job run with cross-account access to S3.

```
aws emr-serverless start-job-run \
    --application-id application-id \
    --execution-role-arn job-role-arn \
    --job-driver '{
        "sparkSubmit": {
            "entryPoint": "`entrypoint_location`",
            "entryPointArguments": [":`argument_1`:", ":`argument_2`:"],
            "sparkSubmitParameters": "--conf spark.executor.cores=4 --conf spark.executor.memory=20g --conf spark.driver.cores=4 --conf spark.driver.memory=8g --conf spark.executor.instances=1"
        }
    }' \
     --configuration-overrides '{
        "applicationConfiguration": [{
            "classification": "spark-defaults",
            "properties": {
                "spark.hadoop.fs.s3.customAWSCredentialsProvider": "com.amazonaws.emr.AssumeRoleAWSCredentialsProvider",
                "spark.emr-serverless.driverEnv.ASSUME_ROLE_CREDENTIALS_ROLE_ARN": "arn:aws:iam::`AccountB`:role/Cross-Account-Role-B",
                "spark.executorEnv.ASSUME_ROLE_CREDENTIALS_ROLE_ARN": "arn:aws:iam::`AccountB`:role/Cross-Account-Role-B"
            }
        }]
    }'
```

Hive
The following example shows how to use an assumed role to start an
EMR Serverless Hive job run with cross-account access to S3.

```
aws emr-serverless start-job-run \
    --application-id application-id \
    --execution-role-arn job-role-arn \
    --job-driver '{
        "hive": {
            "query": "`query_location`",
            "parameters": "`hive_parameters`"
        }
    }' \
    --configuration-overrides '{
        "applicationConfiguration": [{
            "classification": "hive-site",
            "properties": {
                "fs.s3.customAWSCredentialsProvider": "com.amazonaws.emr.serverless.credentialsprovider.AssumeRoleAWSCredentialsProvider",
                "hive.emr-serverless.launch.env.ASSUME_ROLE_CREDENTIALS_ROLE_ARN": "arn:aws:iam::`AccountB`:role/Cross-Account-Role-B",
                "tez.am.emr-serverless.launch.env.ASSUME_ROLE_CREDENTIALS_ROLE_ARN": "arn:aws:iam::`AccountB`:role/Cross-Account-Role-B",
                "tez.task.emr-serverless.launch.env.ASSUME_ROLE_CREDENTIALS_ROLE_ARN": "arn:aws:iam::`AccountB`:role/Cross-Account-Role-B"
            }
        }]
    }'
```

### Access S3 resources with

multiple assumed roles

With EMR Serverless releases 6.11.0 and higher, configure multiple IAM
roles to assume when you access different cross-account buckets. If you want to access
different S3 resources with different assumed roles in account B, use following
configurations when you start the job run:

1. Specify EMRFS configuration `fs.s3.customAWSCredentialsProvider` to
   `com.amazonaws.emr.serverless.credentialsprovider.BucketLevelAssumeRoleCredentialsProvider`.
2. Specify EMRFS configuration `fs.s3.bucketLevelAssumeRoleMapping` to
   define the mapping from S3 bucket name to the IAM role in account B to assume. The
   value should be in format of `bucket1->role1;bucket2->role2`.

For example, use
`arn:aws:iam::`AccountB`:role/Cross-Account-Role-B-1`
to access bucket `bucket1`, and use
`arn:aws:iam::`AccountB`:role/Cross-Account-Role-B-2`
to access bucket `bucket2`. The following examples demonstrate how to start an
EMR Serverless job run with cross-account access through multiple assumed roles.

Spark
The following example shows how to use multiple assumed roles to create an
EMR Serverless Spark job run.

```
aws emr-serverless start-job-run \
    --application-id application-id \
    --execution-role-arn job-role-arn \
    --job-driver '{
        "sparkSubmit": {
            "entryPoint": "`entrypoint_location`",
            "entryPointArguments": [":`argument_1`:", ":`argument_2`:"],
            "sparkSubmitParameters": "--conf spark.executor.cores=4 --conf spark.executor.memory=20g --conf spark.driver.cores=4 --conf spark.driver.memory=8g --conf spark.executor.instances=1"
        }
    }' \
     --configuration-overrides '{
        "applicationConfiguration": [{
            "classification": "spark-defaults",
            "properties": {
                "spark.hadoop.fs.s3.customAWSCredentialsProvider": "com.amazonaws.emr.serverless.credentialsprovider.BucketLevelAssumeRoleCredentialsProvider",
                "spark.hadoop.fs.s3.bucketLevelAssumeRoleMapping": "bucket1->arn:aws:iam::`AccountB`:role/Cross-Account-Role-B-1;bucket2->arn:aws:iam::`AccountB`:role/Cross-Account-Role-B-2"
            }
        }]
    }'
```

Hive
The following examples demonstrate how to use multiple assumed roles to create an
EMR Serverless Hive job run.

```
aws emr-serverless start-job-run \
    --application-id application-id \
    --execution-role-arn job-role-arn \
    --job-driver '{
        "hive": {
            "query": "`query_location`",
            "parameters": "`hive_parameters`"
        }
    }' \
    --configuration-overrides '{
        "applicationConfiguration": [{
            "classification": "hive-site",
            "properties": {
                "fs.s3.customAWSCredentialsProvider": "com.amazonaws.emr.serverless.credentialsprovider.AssumeRoleAWSCredentialsProvider",
                "fs.s3.bucketLevelAssumeRoleMapping": "bucket1->arn:aws:iam::`AccountB`:role/Cross-Account-Role-B-1;bucket2->arn:aws:iam::`AccountB`:role/Cross-Account-Role-B-2"
            }
        }]
    }'
```
