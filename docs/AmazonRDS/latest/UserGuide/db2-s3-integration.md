# Integrating an Amazon RDS for Db2 DB instance with

Amazon S3

You can transfer files between your Amazon RDS for Db2 DB instance and an Amazon Simple Storage Service (Amazon S3) bucket
with Amazon RDS stored procedures. For more information, see [Amazon RDS for Db2 stored procedure reference](db2-stored-procedures.md "db2-stored-procedures.md").

###### Note

Your DB instance and your Amazon S3 bucket must be in the same AWS Region.

For RDS for Db2 to integrate with Amazon S3, your DB instance must have access to an Amazon S3 bucket
where your RDS for Db2 resides. If you don't currently have an S3 bucket, [create a bucket](../../../AmazonS3/latest/userguide/creating-bucket-overview.md "../../../AmazonS3/latest/userguide/creating-bucket-overview.md").

###### Topics

- [Step 1: Create an IAM policy](#db2-creating-iam-policy "#db2-creating-iam-policy")
- [Step 2: Create an IAM role and attach your
  IAM policy](#db2-creating-iam-role "#db2-creating-iam-role")
- [Step 3: Add your IAM role to your RDS for Db2 DB
  instance](#db2-adding-iam-role "#db2-adding-iam-role")

## Step 1: Create an IAM policy

In this step, you create an AWS Identity and Access Management (IAM) policy with the permissions required to
transfer files from your Amazon S3 bucket to your RDS DB instance. This step assumes that you have
already created an S3 bucket. For more information, see [Creating a
bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.

Before you create the policy, note the following pieces of information:

- The Amazon Resource Name (ARN) for your bucket
- The ARN for your AWS Key Management Service (AWS KMS) key, if your bucket uses
  SSE-KMS or SSE-S3 encryption.

The IAM policy that you create should contain the following information. Replace
`{amzn-s3-demo-bucket}` with the name of your S3
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowS3BucketAccess",
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt",
 "s3:PutObject",
 "s3:GetObject",
 "s3:AbortMultipartUpload",
 "s3:ListBucket",
 "s3:GetObjectVersion",
 "s3:ListMultipartUploadParts",
 "s3:GetBucketAcl",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::${amzn-s3-demo-bucket}/*",
 "arn:aws:s3:::${amzn-s3-demo-bucket}"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

You can create an IAM policy by using the AWS Management Console or the AWS Command Line Interface (AWS CLI).

###### To create an IAM policy to allow Amazon RDS to access your Amazon S3

bucket

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**, and then choose
   **JSON**.
4. Add actions by service. To transfer files from an Amazon S3 bucket to
   Amazon RDS, you must select bucket permissions and object permissions.
5. Expand **Resources**. You must specify your bucket
   and object resources.
6. Choose **Next**.
7. For **Policy name**, enter a name for this policy.
8. (Optional) For **Description**, enter a description
   for this policy.
9. Choose **Create policy**.

###### To create an IAM policy to allow Amazon RDS to access your Amazon S3

bucket

1. Create a JSON file that contains the following JSON policy document.
   Replace `{amzn-s3-demo-bucket}` with the name
   of your S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowS3BucketAccess",
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt",
 "s3:PutObject",
 "s3:GetObject",
 "s3:AbortMultipartUpload",
 "s3:ListBucket",
 "s3:GetObjectVersion",
 "s3:ListMultipartUploadParts",
 "s3:GetBucketAcl",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::${amzn-s3-demo-bucket}/*",
 "arn:aws:s3:::${amzn-s3-demo-bucket}"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

2. Run the [create-policy](../../../cli/latest/reference/iam/create-policy.md "../../../cli/latest/reference/iam/create-policy.md") command. In the following
   example, replace `iam_policy_name` and
   `iam_policy_file_name` with a name for your
   IAM policy and the name of the JSON file you created in Step 1.

For Linux, macOS, or Unix:

```
aws iam create-policy \
    --policy-name `iam_policy_name` \
    --policy-document '{
      "Version": "2012-10-17"		 	 	 		 	 	 		 	 	 ,
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "kms:GenerateDataKey",
            "kms:Decrypt",
            "s3:PutObject",
            "s3:GetObject",
            "s3:AbortMultipartUpload",
            "s3:ListBucket",
            "s3:DeleteObject",
            "s3:GetObjectVersion",
            "s3:ListMultipartUploadParts"
          ],
          "Resource": [
            "arn:aws:s3:::`s3_bucket_name`/*",
            "arn:aws:s3:::`s3_bucket_name`"
          ]
        }
      ]
    }'
```

For Windows:

```
aws iam create-policy ^
    --policy-name `iam_policy_name` ^
    --policy-document '{
      "Version": "2012-10-17"		 	 	 		 	 	 		 	 	 ,
      "Statement": [
        {
          "Effect": "Allow",
            "Action": [
              "s3:PutObject",
              "s3:GetObject",
              "s3:AbortMultipartUpload",
              "s3:ListBucket",
              "s3:DeleteObject",
              "s3:GetObjectVersion",
              "s3:ListMultipartUploadParts"
            ],
            "Resource": [
              "arn:aws:s3:::`s3_bucket_name`/*",
              "arn:aws:s3:::`s3_bucket_name`"
            ]
        }
      ]
    }'
```

3. After the policy is created, note the ARN of the policy. You need the
   ARN for [Step 2: Create an IAM role and attach your
   IAM policy](#db2-creating-iam-role "#db2-creating-iam-role").

For information about creating an IAM policy, see [Creating IAM
policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the IAM User Guide.

## Step 2: Create an IAM role and attach your

IAM policy

This step assumes that you have created the IAM policy in [Step 1: Create an IAM policy](#db2-creating-iam-policy "#db2-creating-iam-policy"). In this
step, you create a IAM role for your RDS for Db2 DB instance and then attach your IAM
policy to the role.

You can create an IAM role for your DB instance by using the AWS Management Console or the AWS CLI.

###### To create an IAM role and attach your IAM policy to it

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.
4. For **Trusted entity type**, select
   **AWS service**.
5. For **Service or use case**, select
   **RDS**, and then select **RDS** **–** **Add Role to
   Database**.
6. Choose **Next**.
7. For **Permissions policies**, search for and select
   the name of the IAM policy that you created.
8. Choose **Next**.
9. For **Role name**, enter a role name.
10. (Optional) For **Description**, enter a description
    for the new role.
11. Choose **Create role**.

###### To create an IAM role and attach your IAM policy to it

1. Create a JSON file that contains the following JSON policy
   document:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "rds.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

2. Run the [create-role](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") command. In the following
   example, replace `iam_role_name` and
   `iam_assume_role_policy_file_name` with a
   name for your IAM role and the name of the JSON file that you created
   in Step 1.

For Linux, macOS, or Unix:

```
aws iam create-role \
    --role-name `iam_role_name` \
    --assume-role-policy-document '{
      "Version": "2012-10-17"		 	 	 		 	 	 		 	 	 ,
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Service": "rds.amazonaws.com"
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }'
```

For Windows:

```
aws iam create-role ^
    --role-name `iam_role_name` ^
    --assume-role-policy-document '{
      "Version": "2012-10-17"		 	 	 		 	 	 		 	 	 ,
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Service": "rds.amazonaws.com"
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }'
```

3. After the role is created, note the ARN of the role. You need the ARN
   for [Step 3: Add your IAM role to your RDS for Db2 DB
   instance](#db2-adding-iam-role "#db2-adding-iam-role").
4. Run the [attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md") command. In the
   following example, replace `iam_policy_arn`
   with the ARN of the IAM policy that you created in [Step 1: Create an IAM policy](#db2-creating-iam-policy "#db2-creating-iam-policy"). Replace
   `iam_role_name` with the name of the IAM
   role that you just created.

For Linux, macOS, or Unix:

```
aws iam attach-role-policy \
   --policy-arn `iam_policy_arn` \
   --role-name `iam_role_name`
```

For Windows:

```
aws iam attach-role-policy ^
   --policy-arn `iam_policy_arn` ^
   --role-name `iam_role_name`
```

For more information, see [Creating a role to delegate
permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.

## Step 3: Add your IAM role to your RDS for Db2 DB

instance

In this step, you add your IAM role to your RDS for Db2 DB instance. Note the following
requirements:

- You must have access to an IAM role with the required Amazon S3 permissions
  policy attached to it.
- You can only associate one IAM role with your RDS for Db2 DB instance at a
  time.
- Your RDS for Db2 DB instance must be in the **Available**
  state.

You can add an IAM role to your DB instance by using the AWS Management Console or the AWS CLI.

###### To add an IAM role to your RDS for Db2 DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose your RDS for Db2 DB instance name.
4. On the **Connectivity & security** tab, scroll
   down to the **Manage IAM roles** section at the
   bottom of the page.
5. For **Add IAM roles to this instance**, choose the
   role that you created in [Step 2: Create an IAM role and attach your
   IAM policy](#db2-creating-iam-role "#db2-creating-iam-role").
6. For **Feature**, choose
   **S3_INTEGRATION**.
7. Choose **Add role**.

![The S3_INTEGRATION feature added to the IAM role for a DB instance.](images/db2-s3-integration-role.png)
To add an IAM role to your RDS for Db2 DB instance, run the [add-role-to-db-instance](../../../cli/latest/reference/rds/add-role-to-db-instance.md "../../../cli/latest/reference/rds/add-role-to-db-instance.md") command. In the
following example, replace `region`,
`db_instance_name`, and
`iam_role_arn` with the name of the AWS Region
where your DB instance exists, the name of your DB instance, and the ARN of the
IAM role that you created in [Step 2: Create an IAM role and attach your
IAM policy](#db2-creating-iam-role "#db2-creating-iam-role").

For Linux, macOS, or Unix:

```
aws rds add-role-to-db-instance \
    --region $`region` \
    --db-instance-identifier $`db_instance_name` \
    --feature-name S3_INTEGRATION \
    --role-arn $`iam_role_arn` \
```

For Windows:

```
aws rds add-role-to-db-instance ^
    --region $`region` \
    --db-instance-identifier `db_instance_name` ^
    --feature-name S3_INTEGRATION ^
    --role-arn `iam_role_arn` ^
```

To confirm that the role was successfully added to your RDS for Db2 DB instance,
run the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") command. In the following
example, replace `db_instance_name` with the name of
your DB instance.

For Linux, macOS, or Unix:

```
aws rds describe-db-instances \
    --filters "Name=db-instance-id,Values=`db_instance_name`" \
    --query 'DBInstances[].AssociatedRoles'
```

For Windows:

```
aws rds describe-db-instances ^
    --filters "Name=db-instance-id,Values=`db_instance_name`" ^
    --query 'DBInstances[].AssociatedRoles'
```

This command produces output similar to the following example:

```
[
    [
        {
            "RoleArn": "arn:aws:iam::0123456789012:role/rds-db2-s3-role",
            "FeatureName": "S3_INTEGRATION",
            "Status": "ACTIVE"
        }
    ]
]
```
