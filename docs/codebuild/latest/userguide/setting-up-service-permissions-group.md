# Allow users to interact with

CodeBuild

If you follow the steps in [Getting started using the
console](getting-started-overview.md#getting-started "getting-started-overview.md#getting-started") to access AWS CodeBuild for the first time, you most
likely do not need the information in this topic. However, as you continue using CodeBuild, you
might want to do things such as give other users and groups in your organization the ability to
interact with CodeBuild.

To allow an IAM user or group to interact with AWS CodeBuild, you must give them access
permissions to CodeBuild. This section describes how to do this with the IAM console or
the AWS CLI.

If you will access CodeBuild with your AWS root account (not recommended) or an
administrator user in your AWS account, then you do not need to follow these
instructions.

For information about AWS root accounts and administrator users, see [The AWS account root user](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md") and [Creating Your First
AWS account root user and Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the _user Guide_.

###### To add CodeBuild access

permissions to an IAM group or user (console)

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

You should have already signed in to the AWS Management Console by using one of the
following:

    * Your AWS root account. This is not recommended. For more
     information, see [The
     AWS account root user](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md") in the *user
     Guide*.
    * An administrator user in your AWS account. For more information, see
     [Creating Your First AWS account root user and Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the
     *user Guide*.
    * An user in your AWS account with permission to perform the following
     minimum set of actions:



    ```
    iam:AttachGroupPolicy
    iam:AttachUserPolicy
    iam:CreatePolicy
    iam:ListAttachedGroupPolicies
    iam:ListAttachedUserPolicies
    iam:ListGroups
    iam:ListPolicies
    iam:ListUsers
    ```

    For more information, see [Overview of IAM
     Policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the *user Guide*.

2. In the navigation pane, choose **Policies**.
3. To add a custom set of AWS CodeBuild access permissions to an IAM group or IAM
   user, skip ahead to step 4 in this procedure.

To add a default set of CodeBuild access permissions to an IAM group or IAM
user, choose **Policy Type**, **AWS
Managed**, and then do the following:

    * To add full access permissions to CodeBuild, select the box named
     **AWSCodeBuildAdminAccess**, choose
     **Policy Actions**, and then choose
     **Attach**. Select the box next to the target IAM
     group or user, and then choose **Attach Policy**.
     Repeat this for the policies named
     **AmazonS3ReadOnlyAccess** and
     **IAMFullAccess**.
    * To add access permissions to CodeBuild for everything except build project
     administration, select the box named
     **AWSCodeBuildDeveloperAccess**, choose
     **Policy Actions**, and then choose
     **Attach**. Select the box next to the target IAM
     group or user, and then choose **Attach Policy**.
     Repeat this for the policy named
     **AmazonS3ReadOnlyAccess**.
    * To add read-only access permissions to CodeBuild, select the boxes named
     **AWSCodeBuildReadOnlyAccess**. Select the box next
     to the target IAM group or user, and then choose **Attach
     Policy**. Repeat this for the policy named
     **AmazonS3ReadOnlyAccess**.

You have now added a default set of CodeBuild access permissions to an IAM group
or user. Skip the rest of the steps in this procedure. 4. Choose **Create Policy**. 5. On the **Create Policy** page, next to **Create Your
Own Policy**, choose **Select**. 6. On the **Review Policy** page, for **Policy
Name**, enter a name for the policy (for example,
`CodeBuildAccessPolicy`). If you use a different
name, be sure to use it throughout this procedure. 7. For **Policy Document**, enter the following, and then choose
**Create Policy**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CodeBuildAccessPolicy",
 "Effect": "Allow",
 "Action": [
 "codebuild:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CodeBuildRolePolicy",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/`role-name`"
 },
 {
 "Sid": "CloudWatchLogsAccessPolicy",
 "Effect": "Allow",
 "Action": [
 "logs:FilterLogEvents",
 "logs:GetLogEvents"
 ],
 "Resource": "*"
 },
 {
 "Sid": "S3AccessPolicy",
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:GetObject",
 "s3:List*",
 "s3:PutObject"
 ],
 "Resource": "*"
 },
 {
 "Sid": "S3BucketIdentity",
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketAcl",
 "s3:GetBucketLocation"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

This policy allows access to all CodeBuild actions and to a potentially large
number of AWS resources. To restrict permissions to specific CodeBuild
actions, change the value of `codebuild:*` in the CodeBuild policy
statement. For more information, see [Identity and access
management](auth-and-access-control.md "auth-and-access-control.md"). To restrict access to
specific AWS resources, change the value of the `Resource`
object. For more information, see [Identity and access
management](auth-and-access-control.md "auth-and-access-control.md"). 8. In the navigation pane, choose **Groups** or
**Users**. 9. In the list of groups or users, choose the name of the IAM group or IAM
user to which you want to add CodeBuild access permissions. 10. For a group, on the group settings page, on the
**Permissions** tab, expand **Managed
Policies**, and then choose **Attach
Policy**.

For a user, on the user settings page, on the **Permissions**
tab, choose **Add permissions**. 11. For a group, on the **Attach Policy** page, select
**CodeBuildAccessPolicy**, and then choose
**Attach Policy**.

For a user, on the **Add permissions** page, choose
**Attach existing policies directly**. Select
**CodeBuildAccessPolicy**, choose **Next:
Review**, and then choose **Add
permissions**.

###### To add CodeBuild access

permissions to an IAM group or user (AWS CLI)

1. Make sure you have configured the AWS CLI with the AWS access key and AWS
   secret access key that correspond to one of the IAM entities, as described in
   the previous procedure. For more information, see [Getting Set Up with the
   AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md") in the _AWS Command Line Interface User Guide_.
2. To add a custom set of AWS CodeBuild access permissions to an IAM group or IAM
   user, skip to step 3 in this procedure.

To add a default set of CodeBuild access permissions to an IAM group or IAM
user, do the following:

Run one of the following commands, depending on whether you want to add
permissions to an IAM group or user:

```
aws iam attach-group-policy --group-name `group-name` --policy-arn `policy-arn`

aws iam attach-user-policy --user-name `user-name` --policy-arn `policy-arn`
```

You must run the command three times, replacing
`group-name` or
`user-name` with the IAM group name or user name,
and replacing `policy-arn` once for each of the
following policy Amazon Resource Names (ARNs):

    * To add full access permissions to CodeBuild, use the following policy
     ARNs:




    	+ `arn:aws:iam::aws:policy/AWSCodeBuildAdminAccess`
    	+ `arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess`
    	+ `arn:aws:iam::aws:policy/IAMFullAccess`
    * To add access permissions to CodeBuild for everything except build project
     administration, use the following policy ARNs:




    	+ `arn:aws:iam::aws:policy/AWSCodeBuildDeveloperAccess`
    	+ `arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess`
    * To add read-only access permissions to CodeBuild, use the following policy
     ARNs:




    	+ `arn:aws:iam::aws:policy/AWSCodeBuildReadOnlyAccess`
    	+ `arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess`

You have now added a default set of CodeBuild access permissions to an IAM group
or user. Skip the rest of the steps in this procedure. 3. In an empty directory on the local workstation or instance where the AWS CLI is
installed, create a file named `put-group-policy.json` or
`put-user-policy.json`. If you use a different file name,
be sure to use it throughout this procedure.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CodeBuildAccessPolicy",
 "Effect": "Allow",
 "Action": [
 "codebuild:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CodeBuildRolePolicy",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/`role-name`"
 },
 {
 "Sid": "CloudWatchLogsAccessPolicy",
 "Effect": "Allow",
 "Action": [
 "logs:FilterLogEvents",
 "logs:GetLogEvents"
 ],
 "Resource": "*"
 },
 {
 "Sid": "S3AccessPolicy",
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:GetObject",
 "s3:List*",
 "s3:PutObject"
 ],
 "Resource": "*"
 },
 {
 "Sid": "S3BucketIdentity",
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketAcl",
 "s3:GetBucketLocation"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

This policy allows access to all CodeBuild actions and to a potentially large
number of AWS resources. To restrict permissions to specific CodeBuild
actions, change the value of `codebuild:*` in the CodeBuild policy
statement. For more information, see [Identity and access
management](auth-and-access-control.md "auth-and-access-control.md"). To restrict access to
specific AWS resources, change the value of the related
`Resource` object. For more information, see [Identity and access
management](auth-and-access-control.md "auth-and-access-control.md") or the specific AWS
service's security documentation. 4. Switch to the directory where you saved the file, and then run one of the
following commands. You can use different values for
`CodeBuildGroupAccessPolicy` and
`CodeBuildUserAccessPolicy`. If you use different values,
be sure to use them here.

For an IAM group:

```
aws iam put-group-policy --group-name `group-name` --policy-name CodeBuildGroupAccessPolicy --policy-document file://put-group-policy.json
```

For an user:

```
aws iam put-user-policy --user-name `user-name` --policy-name CodeBuildUserAccessPolicy --policy-document file://put-user-policy.json
```

In the preceding commands, replace `group-name` or
`user-name` with the name of the target IAM group
or user.
