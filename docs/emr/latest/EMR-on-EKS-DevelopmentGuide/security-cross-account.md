# Set up cross-account access for Amazon EMR on EKS

You can set up cross-account access for Amazon EMR on EKS. Cross-account access enables users from
one AWS account to run Amazon EMR on EKS jobs and access the underlying data that belongs to another
AWS account.

## Prerequisites

To set up cross-account access for Amazon EMR on EKS, you’ll complete tasks while signed in to
the following AWS accounts:

- `AccountA` ‐ An AWS account where you have created an Amazon EMR on EKS virtual
  cluster by registering Amazon EMR with a namespace on an EKS cluster.
- `AccountB` ‐ An AWS account that contains an Amazon S3 bucket or a DynamoDB table
  that you want your Amazon EMR on EKS jobs to access.

You must have the following ready in your AWS accounts before setting up
cross-account access:

- An Amazon EMR on EKS virtual cluster in `AccountA` where you want to run jobs.
- A job execution role in `AccountA` that has the required permissions to run jobs in
  the virtual cluster. For more information, see [Create a job execution role](creating-job-execution-role.md "creating-job-execution-role.md") and [Using job execution roles with Amazon EMR on EKS](iam-execution-role.md "iam-execution-role.md").

## How to access a cross-account Amazon S3 bucket or DynamoDB

table

To set up cross-account access for Amazon EMR on EKS, complete the following steps.

1. Create an Amazon S3 bucket, `cross-account-bucket`, in `AccountB`. For more
   information, see [Creating a bucket](../../../AmazonS3/latest/gsg/CreatingABucket.md "../../../AmazonS3/latest/gsg/CreatingABucket.md"). If
   you want to have cross-account access to DynamoDB, you can also create a DynamoDB
   table in `AccountB`. For more information, see [Creating a DynamoDB table](../../../amazondynamodb/latest/developerguide/getting-started-step-1.md "../../../amazondynamodb/latest/developerguide/getting-started-step-1.md").
2. Create a `Cross-Account-Role-B` IAM role in `AccountB` that can access
   the `cross-account-bucket`.
   1. Sign in to the IAM console.
   2. Choose **Roles** and create a new role: `Cross-Account-Role-B`.
      For more information about how to create IAM roles, see [Creating IAM roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") in the IAM user Guide.
   3. Create an IAM policy that specifies the permissions for `Cross-Account-Role-B` to
      access the `cross-account-bucket` S3 bucket, as the following
      policy statement demonstrates. Then attach the IAM policy to
      `Cross-Account-Role-B`. For more information, see [Creating a
      New Policy](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the IAM user Guide.

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
    "arn:aws:s3:::cross-account-bucket",
    "arn:aws:s3:::cross-account-bucket/*"
    ],
    "Sid": "AllowS3"
    }
    ]
   }`

   ```

   If DynamoDB access is required, create an IAM policy that specifies
   permissions to access the cross-account DynamoDB table. Then attach the IAM
   policy to `Cross-Account-Role-B`. For more information, see
   [Create a DynamoDB table](../../../IAM/latest/UserGuide/reference_policies_examples_dynamodb_specific-table.md "../../../IAM/latest/UserGuide/reference_policies_examples_dynamodb_specific-table.md") in the IAM user guide.

   Following is a policy to access a DynamoDB table,
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
    "arn:aws:dynamodb:us-east-1:*:table/CrossAccountTable"
    ],
    "Sid": "AllowDYNAMODB"
    }
    ]
   }`

   ```

3. Edit the trust relationship for the `Cross-Account-Role-B` role.
   1. To configure the trust relationship for the role, choose the **Trust
      Relationships** tab in the IAM console for the role created
      in Step 2: `Cross-Account-Role-B`.
   2. Select **Edit Trust Relationship**.
   3. Add the following policy document, which allows `Job-Execution-Role-A` in
      `AccountA` to assume this
      `Cross-Account-Role-B` role.

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
    "arn:aws:iam::*:role/Job-Execution-Role-A"
    ],
    "Sid": "AllowSTSAssumerole"
    }
    ]
   }`

   ```

4. Grant `Job-Execution-Role-A` in `AccountA` with -
   STS
   Assume role permission to assume
   `Cross-Account-Role-B`.
   1. In the IAM console for AWS account `AccountA`, select `Job-Execution-Role-A`.
   2. Add the following policy statement to the `Job-Execution-Role-A` to allow the
      `AssumeRole` action on the `Cross-Account-Role-B`
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
    "arn:aws:iam::*:role/Cross-Account-Role-B"
    ],
    "Sid": "AllowSTSAssumerole"
    }
    ]
   }`

   ```

5. For Amazon S3 access, set the following `spark-submit` parameters (`spark
conf`) while submitting the job to Amazon EMR on EKS.

###### Note

By default, EMRFS uses the job execution role to access the S3 bucket from the job. But when
`customAWSCredentialsProvider` is set to
`AssumeRoleAWSCredentialsProvider`, EMRFS uses the
corresponding role that you specify with
`ASSUME_ROLE_CREDENTIALS_ROLE_ARN` instead of the
`Job-Execution-Role-A` for Amazon S3 access.

    * `--conf spark.hadoop.fs.s3.customAWSCredentialsProvider=com.amazonaws.emr.AssumeRoleAWSCredentialsProvider`
    * `--conf
     spark.kubernetes.driverEnv.ASSUME_ROLE_CREDENTIALS_ROLE_ARN=arn:aws:iam::`AccountB`:role/Cross-Account-Role-B
     \`
    * `--conf
     spark.executorEnv.ASSUME_ROLE_CREDENTIALS_ROLE_ARN=arn:aws:iam::`AccountB`:role/Cross-Account-Role-B
     \`

###### Note

You must set `ASSUME_ROLE_CREDENTIALS_ROLE_ARN` for both executor and driver
`env`
in the job spark configuration.

For DynamoDB cross-account access, you must set `--conf
 spark.dynamodb.customAWSCredentialsProvider=com.amazonaws.emr.AssumeRoleAWSCredentialsProvider`. 6. Run the Amazon EMR on EKS job with cross-account access, as the following example demonstrates.

```
aws emr-containers start-job-run \
--virtual-cluster-id 123456 \
--name myjob \
--execution-role-arn execution-role-arn \
--release-label emr-6.2.0-latest \
--job-driver '{"sparkSubmitJobDriver": {"entryPoint": "entryPoint_location", "entryPointArguments": ["arguments_list"], "sparkSubmitParameters": "--class <main_class> --conf spark.executor.instances=2 --conf spark.executor.memory=2G --conf spark.executor.cores=2 --conf spark.driver.cores=1 --conf spark.hadoop.fs.s3.customAWSCredentialsProvider=com.amazonaws.emr.AssumeRoleAWSCredentialsProvider --conf spark.kubernetes.driverEnv.ASSUME_ROLE_CREDENTIALS_ROLE_ARN=arn:aws:iam::`AccountB`:role/Cross-Account-Role-B --conf spark.executorEnv.ASSUME_ROLE_CREDENTIALS_ROLE_ARN=arn:aws:iam::`AccountB`:role/Cross-Account-Role-B"}} ' \
--configuration-overrides '{"applicationConfiguration": [{"classification": "spark-defaults", "properties": {"spark.driver.memory": "2G"}}], "monitoringConfiguration": {"cloudWatchMonitoringConfiguration": {"logGroupName": "log_group_name", "logStreamNamePrefix": "log_stream_prefix"}, "persistentAppUI":"ENABLED",  "s3MonitoringConfiguration": {"logUri": "s3://my_s3_log_location" }}}'

```
