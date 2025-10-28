# Allow CodeBuild to interact with other AWS

services

If you follow the steps in [Getting started using the
console](getting-started-overview.md#getting-started "getting-started-overview.md#getting-started") to access AWS CodeBuild for the first time, you
most likely do not need the information in this topic. However, as you continue using
CodeBuild, you might want to do things such as allow CodeBuild to interact with
other AWS services.

To allow CodeBuild to interact with dependent AWS services on your behalf, you need an
AWS CodeBuild service role. You can create a CodeBuild service role by using the CodeBuild or
AWS CodePipeline consoles. For information, see:

- [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console")
- [Create a pipeline that uses CodeBuild (CodePipeline
  console)](how-to-create-pipeline-console.md "how-to-create-pipeline-console.md")
- [Add a CodeBuild build action to a pipeline (CodePipeline
  console)](how-to-create-pipeline-add.md "how-to-create-pipeline-add.md")
- [Change a build project's settings
  (console)](change-project.md#change-project-console "change-project.md#change-project-console")
  If you do not plan to use these consoles, this section describes how to create a CodeBuild
  service role with the IAM console or the AWS CLI.

###### Important

CodeBuild uses the service role for all operations that are performed on your behalf.
If the role includes permissions that the user shouldn't have, you can
unintentionally escalate a user's permissions. Ensure that the role grants [least
privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege").

The service role described on this page contains a policy that grants the minimum
permissions required to use CodeBuild. You may need to add additional permissions,
depending on your use case.

###### To create a CodeBuild service role

(console)

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

You should have already signed in to the console by using one of the
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
    iam:AddRoleToInstanceProfile
    iam:AttachRolePolicy
    iam:CreateInstanceProfile
    iam:CreatePolicy
    iam:CreateRole
    iam:GetRole
    iam:ListAttachedRolePolicies
    iam:ListPolicies
    iam:ListRoles
    iam:PassRole
    iam:PutRolePolicy
    iam:UpdateAssumeRolePolicy
    ```

    For more information, see [Overview of IAM
     Policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the *user Guide*.

2. In the navigation pane, choose **Policies**.
3. Choose **Create Policy**.
4. On the **Create Policy** page, choose
   **JSON**.
5. For the JSON policy, enter the following, and then choose **Review
   Policy**:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CloudWatchLogsPolicy",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CodeCommitPolicy",
 "Effect": "Allow",
 "Action": [
 "codecommit:GitPull"
 ],
 "Resource": "*"
 },
 {
 "Sid": "S3GetObjectPolicy",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": "*"
 },
 {
 "Sid": "S3PutObjectPolicy",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ECRPullPolicy",
 "Effect": "Allow",
 "Action": [
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ECRAuthPolicy",
 "Effect": "Allow",
 "Action": [
 "ecr:GetAuthorizationToken"
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

This policy contains statements that allow access to a potentially large
number of AWS resources. To restrict AWS CodeBuild to access specific AWS
resources, change the value of the `Resource` array. For more
information, see the security documentation for the AWS service. 6. On the **Review Policy** page, for **Policy
Name**, enter a name for the policy (for example,
`CodeBuildServiceRolePolicy`), and then choose
**Create policy**.

###### Note

If you use a different name, be sure to use it throughout this
procedure. 7. In the navigation pane, choose **Roles**. 8. Choose **Create role**. 9. On the **Create role** page, with **AWS
Service** already selected, choose **CodeBuild**,
and then choose **Next:Permissions**. 10. On the **Attach permissions policies** page, select
**CodeBuildServiceRolePolicy**, and then choose
**Next: Review**. 11. On the **Create role and review** page, for **Role
name**, enter a name for the role (for example,
`CodeBuildServiceRole`), and then choose
**Create role**.

###### To create a CodeBuild service role

(AWS CLI)

1. Make sure you have configured the AWS CLI with the AWS access key and AWS
   secret access key that correspond to one of the IAM entities, as described in
   the previous procedure. For more information, see [Getting Set Up with the
   AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md") in the _AWS Command Line Interface User Guide_.
2. In an empty directory on the local workstation or instance where the AWS CLI is
   installed, create two files named `create-role.json` and
   `put-role-policy.json`. If you choose different file
   names, be sure to use them throughout this procedure.

`create-role.json`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "codebuild.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

###### Note

We recommend that you use the `aws:SourceAccount` and
`aws:SourceArn` condition keys to protect yourself against
[the confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"). For example, you can edit the
previous trust policy with the following condition blocks. The
`aws:SourceAccount` is the owner of the CodeBuild project and the
`aws:SourceArn` is the CodeBuild project ARN.

If you would like to restrict your service role to an AWS account,
`create-role.json` might look similar to this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "codebuild.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": [
 "`111122223333`"
 ]
 }
 }
 }
 ]
}`

```

If you would like to restrict your service role to a specific CodeBuild project,
`create-role.json` might look similar to this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "codebuild.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:codebuild:us-east-1:`111122223333`:project/MyProject"
 }
 }
 }
 ]
}`

```

###### Note

If you don't know or haven't decided on a name for your CodeBuild project and
want a trust policy restriction on a particular ARN pattern, you can replace
that portion of the ARN with a wildcard (\*). After you create your project,
you can then update the trust policy.

`put-role-policy.json`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CloudWatchLogsPolicy",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CodeCommitPolicy",
 "Effect": "Allow",
 "Action": [
 "codecommit:GitPull"
 ],
 "Resource": "*"
 },
 {
 "Sid": "S3GetObjectPolicy",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": "*"
 },
 {
 "Sid": "S3PutObjectPolicy",
 "Effect": "Allow",
 "Action": [
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

This policy contains statements that allow access to a potentially large
number of AWS resources. To restrict AWS CodeBuild to access specific AWS
resources, change the value of the `Resource` array. For more
information, see the security documentation for the AWS service. 3. Switch to the directory where you saved the preceding files, and then run the
following two commands, one at a time, in this order. You can use different
values for `CodeBuildServiceRole` and
`CodeBuildServiceRolePolicy`, but be sure to use them
here.

```
aws iam create-role --role-name CodeBuildServiceRole --assume-role-policy-document file://create-role.json
```

```
aws iam put-role-policy --role-name CodeBuildServiceRole --policy-name CodeBuildServiceRolePolicy --policy-document file://put-role-policy.json
```
