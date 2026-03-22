# Configuring IAM permissions for RDS for Oracle integration with Amazon EFS

By default, Amazon EFS integration feature doesn't use an IAM role: the
`USE_IAM_ROLE` option setting is `FALSE`. To integrate RDS for Oracle
with Amazon EFS and an IAM role, your DB instance must have IAM permissions to access an Amazon EFS file
system.

###### Topics

- [Step 1: Create an IAM role for your DB instance and attach your policy](#oracle-efs-integration.iam.role "#oracle-efs-integration.iam.role")
- [Step 2: Create a file system policy for your Amazon EFS file system](#oracle-efs-integration.iam.policy "#oracle-efs-integration.iam.policy")
- [Step 3: Associate your IAM role with your RDS for Oracle DB instance](#oracle-efs-integration.iam.instance "#oracle-efs-integration.iam.instance")

## Step 1: Create an IAM role for your DB instance and attach your policy

In this step, you create a role for your RDS for Oracle DB instance to allow Amazon RDS to access
your EFS file system.

###### To create an IAM role to allow Amazon RDS access to an EFS file system

1. Open the [IAM Management Console](https://console.aws.amazon.com/iam/home?#home "https://console.aws.amazon.com/iam/home?#home").
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.
4. For **AWS service**, choose **RDS**.
5. For **Select your use case**, choose **RDS – Add Role to Database**.
6. Choose **Next**.
7. Don't add any permissions policies. Choose
   **Next**.
8. Set **Role name** to a name for your IAM role, for example `rds-efs-integration-role`. You can
   also add an optional **Description** value.
9. Choose **Create role**.
   To limit the service's permissions to a specific resource, we recommend using the
   [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition
   context keys in resource-based trust relationships. This is the most effective way
   to protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

You might use both global condition context keys and have the
`aws:SourceArn` value contain the account ID. In this case, the
`aws:SourceAccount` value and the account in the
`aws:SourceArn` value must use the same account ID when used in the
same statement.

- Use `aws:SourceArn` if you want cross-service access for a
  single resource.
- Use `aws:SourceAccount` if you want to allow any resource in
  that account to be associated with the cross-service use.
  In the trust relationship, make sure to use the `aws:SourceArn` global
  condition context key with the full Amazon Resource Name (ARN) of the resources
  accessing the role.

The following AWS CLI command creates the role named
`rds-efs-integration-role` for this
purpose.

###### Example

For Linux, macOS, or Unix:

```
aws iam create-role \
   --role-name `rds-efs-integration-role` \
   --assume-role-policy-document '{
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
            "Service": "rds.amazonaws.com"
          },
         "Action": "sts:AssumeRole",
         "Condition": {
             "StringEquals": {
                 "aws:SourceAccount": `my_account_ID`,
                 "aws:SourceArn": "arn:aws:rds:`Region`:`my_account_ID`:db:`dbname`"
             }
         }
       }
     ]
   }'
```

For Windows:

```
aws iam create-role ^
   --role-name `rds-efs-integration-role` ^
   --assume-role-policy-document '{
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
            "Service": "rds.amazonaws.com"
          },
         "Action": "sts:AssumeRole",
         "Condition": {
             "StringEquals": {
                 "aws:SourceAccount": `my_account_ID`,
                 "aws:SourceArn": "arn:aws:rds:`Region`:`my_account_ID`:db:`dbname`"
             }
         }
       }
     ]
   }'
```

For more information, see [Creating a role to delegate permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.

## Step 2: Create a file system policy for your Amazon EFS file system

In this step, you create a file system policy for your EFS file system.

###### To create or edit an EFS file system policy

1. Open the [EFS Management
   Console](https://console.aws.amazon.com/efs/home?#home "https://console.aws.amazon.com/efs/home?#home").
2. Choose **File Systems**.
3. On the **File systems** page, choose the file system that you
   want to edit or create a file system policy for. The details page for that file
   system is displayed.
4. Choose the **File system policy** tab.

If the policy is empty, then the default EFS file system policy is in use. For
more information, see [Default EFS file system policy](../../../efs/latest/ug/iam-access-control-nfs-efs.md#default-filesystempolicy "../../../efs/latest/ug/iam-access-control-nfs-efs.md#default-filesystempolicy") in the _Amazon Elastic File System User
Guide_. 5. Choose **Edit**. The **File system policy** page
appears. 6. In **Policy editor**, enter a policy such as the following, and
then choose **Save**.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "ExamplePolicy01",
 "Statement": [
 {
 "Sid": "ExampleStatement01",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:role/rds-efs-integration-role"
 },
 "Action": [
 "elasticfilesystem:ClientMount",
 "elasticfilesystem:ClientWrite",
 "elasticfilesystem:ClientRootAccess"
 ],
 "Resource": "arn:aws:elasticfilesystem:`us-east-1`:`123456789012`:file-system/`fs-1234567890abcdef0`"
 }
 ]
}`

```

## Step 3: Associate your IAM role with your RDS for Oracle DB instance

In this step, you associate your IAM role with your DB instance. Be aware of the
following requirements:

- You must have access to an IAM role with the required Amazon EFS permissions policy attached to it.
- You can associate only one IAM role with your RDS for Oracle DB instance at a
  time.
- The status of your instance must be **Available**.

For more information, see [Identity and access management for Amazon EFS](../../../efs/latest/ug/auth-and-access-control.md "../../../efs/latest/ug/auth-and-access-control.md") in the
_Amazon Elastic File System User Guide_.

###### To associate your IAM role with your RDS for Oracle DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases**.
3. If your database instance is unavailable, choose **Actions** and then **Start**. When the
   instance status shows **Started**, go to the next step.
4. Choose the Oracle DB instance name to display its details.
5. On the **Connectivity & security** tab, scroll down to the **Manage IAM roles**
   section at the bottom of the page.
6. Choose the role to add in the **Add IAM roles to this instance** section.
7. For **Feature**, choose **EFS_INTEGRATION**.
8. Choose **Add role**.
   The following AWS CLI command adds the role to an Oracle DB instance named
   `mydbinstance`.

###### Example

For Linux, macOS, or Unix:

```
aws rds add-role-to-db-instance \
   --db-instance-identifier `mydbinstance` \
   --feature-name EFS_INTEGRATION \
   --role-arn `your-role-arn`
```

For Windows:

```
aws rds add-role-to-db-instance ^
   --db-instance-identifier `mydbinstance` ^
   --feature-name EFS_INTEGRATION ^
   --role-arn `your-role-arn`
```

Replace `your-role-arn` with the role ARN
that you noted in a previous step. `EFS_INTEGRATION` must be specified
for the `--feature-name` option.
