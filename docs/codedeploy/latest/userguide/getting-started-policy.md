# Step 3: Limit the CodeDeploy user's permissions

For security reasons, we recommend that you limit the permissions of the administrative
user that you created in [Step 1: Setting up](getting-started-setting-up.md "getting-started-setting-up.md") to just those required to create and manage
deployments in CodeDeploy.

Use the following series of procedures to limit the CodeDeploy administrative user's
permissions.

###### Before you begin

- Make sure you have created a CodeDeploy administrative user in IAM Identity Center following
  the instructions in [Step 1: Setting up](getting-started-setting-up.md "getting-started-setting-up.md").

###### To create a permission set

You'll assign this permission set to the CodeDeploy administrative user later.

1. Sign in to the AWS Management Console and open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. In the navigation pane, choose **Permission sets**, and then choose
   **Create permission set**.
3. Choose **Custom permission set**.
4. Choose **Next**.
5. Choose **Inline policy**.
6. Remove the sample code.
7. Add the following policy code:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CodeDeployAccessPolicy",
 "Effect": "Allow",
 "Action": [
 "autoscaling:*",
 "codedeploy:*",
 "ec2:*",
 "lambda:*",
 "ecs:*",
 "elasticloadbalancing:*",
 "iam:AddRoleToInstanceProfile",
 "iam:AttachRolePolicy",
 "iam:CreateInstanceProfile",
 "iam:CreateRole",
 "iam:DeleteInstanceProfile",
 "iam:DeleteRole",
 "iam:DeleteRolePolicy",
 "iam:GetInstanceProfile",
 "iam:GetRole",
 "iam:GetRolePolicy",
 "iam:ListInstanceProfilesForRole",
 "iam:ListRolePolicies",
 "iam:ListRoles",
 "iam:PutRolePolicy",
 "iam:RemoveRoleFromInstanceProfile",
 "s3:*",
 "ssm:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CodeDeployRolePolicy",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "`arn:aws:iam::`111122223333`:role/CodeDeployServiceRole`"
 }
 ]
}`

```

In this policy, replace
`arn:aws:iam::account-ID:role/CodeDeployServiceRole` with the
ARN value of the CodeDeploy service role that you created in [Step 2: Create a service role for
CodeDeploy](getting-started-create-service-role.md "getting-started-create-service-role.md"). You can find the ARN value in the
details page of the service role in the IAM console.

The preceding policy lets you deploy an application to an
AWS Lambda compute platform, an EC2/On-Premises compute platform, and an
Amazon ECS compute platform.

You can use the CloudFormation templates provided in this documentation to launch Amazon EC2
instances that are compatible with CodeDeploy. To use CloudFormation templates to create applications,
deployment groups, or deployment configurations, you must provide access to CloudFormation—and
AWS services and actions that CloudFormation depends on—by adding the
`cloudformation:*` permission to the CodeDeploy administrative user's permission
policy, like this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

8. Choose **Next**.
9. In **Permission set name**, enter:

```
`CodeDeployUserPermissionSet`
```

10. Choose **Next**.
11. On the **Review and create** page, review the information and choose
    **Create**.

###### To assign the permission set to the CodeDeploy administrative user

1. In the navigation pane, choose **AWS accounts**, and then select
   the check box next to the AWS account that you're currently signed in to.
2. Choose the **Assign users or groups** button.
3. Choose the **Users** tab.
4. Select the check box next to the CodeDeploy administrative user.
5. Choose **Next**.
6. Select the check box next to `CodeDeployUserPermissionSet`.
7. Choose **Next**.
8. Review the information and choose **Submit**.

You have now assigned the CodeDeploy administrative user and
`CodeDeployUserPermissionSet` to your AWS account, binding them together.

###### To sign out and sign back in as the CodeDeploy administrative user

1. Before you sign out, make sure you have the AWS access portal URL and the username
   and one-time password for the CodeDeploy adminstrative user.

###### Note

If you do not have this information, go to the CodeDeploy adminstrative user details page
in IAM Identity Center, choose **Reset password**, **Generate a one-time
password [...]**, and **Reset password** again to display
the information on the screen. 2. Sign out of AWS. 3. Paste the AWS access portal URL into your browser's address bar. 4. Sign in as the CodeDeploy adminstrative user.

An **AWS account** box appears on the screen. 5. Choose **AWS account**, and then choose the name of the
AWS account to which you assigned the CodeDeploy adminstrative user and permission
set. 6. Next to the `CodeDeployUserPermissionSet`, choose **Management
console**.

The AWS Management Console appears. You are now signed in as the CodeDeploy adminstrative user with the
limited permissions. You can now perform CodeDeploy-related operations, and
_only_ CodeDeploy-related operations, as this user.
