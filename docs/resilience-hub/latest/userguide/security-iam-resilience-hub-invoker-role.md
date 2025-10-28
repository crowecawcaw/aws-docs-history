# Invoker

role

The AWS Resilience Hub invoker role is an AWS Identity and Access Management (IAM) role that AWS Resilience Hub
assumes to access AWS services and resources. For example, you might
create an invoker role that has permission to access your CFN template and
the resource it creates. This page provides information on how to create,
view, and manage an application invoker role.

When you create an application, you provide an invoker role. AWS Resilience Hub
assumes this role to access your resources when you import resources or
start an assessment. For AWS Resilience Hub to properly assume your invoker role, the
role's trust policy must specify the AWS Resilience Hub service principal (**resiliencehub.amazonaws.com**) as a trusted
service.

To view the application's invoker role, choose
**Applications** from the navigation pane, and then
choose **Update permissions** from
**Actions** menu in the
**Application** page.

You can add or remove permissions from an application invoker role at any
time, or configure your application to use a different role for accessing
application resources.

**Topics**

- [Creating an invoker role in the IAM console](#security-iam-resilience-hub-create-invoker-role "#security-iam-resilience-hub-create-invoker-role")
- [Managing roles with the IAM API](#security-iam-resilience-hub-manage-roles-with-IAM-API "#security-iam-resilience-hub-manage-roles-with-IAM-API")
- [Defining trust policy using JSON file](#security-iam-resilience-define-policy "#security-iam-resilience-define-policy")

## Creating an invoker role in the IAM console

To enable AWS Resilience Hub to access AWS services and resources, you must
create an invoker role in the primary account using the IAM console.
For more information about creating roles using IAM console, see
[Creating a role for an AWS service (console)](../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console "../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console").

###### To create an invoker role in the primary account using IAM

console

1. Open the IAM console at
   `https://console.aws.amazon.com/iam/`.
2. From the navigation pane, choose **Roles**
   and then choose **Create role**.
3. Select **Custom Trust Policy**, copy the
   following policy in the **Custom trust policy**
   window, and then choose **Next**.

###### Note

If your resources are in different accounts, you have to
create a role in each of those accounts, and use the
secondary account trust policy for the other
accounts.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "resiliencehub.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

4. In the **Permissions policies** section of
   **Add permissions** page, enter
   `AWSResilienceHubAsssessmentExecutionPolicy` in
   the **Filter policies by property or policy name and
   press enter** box.
5. Select the policy and choose **Next**.
6. In **Role details** section, enter a unique
   role name (such as `AWSResilienceHubAssessmentRole`)
   in the **Role name** box.

This field accepts only alphanumeric and
'`+=,.@-_/`' characters. 7. (Optional) Enter a description about the role in the
**Description** box. 8. Choose **Create Role**.

To edit the use cases and permissions, in step 6, choose
**Edit** button that is located to the
right of **Step 1: Select trusted entities** or
**Step 2: Add permissions**
sections.

After creating the invoker role and the resource role (if applicable),
you can configure your application to use these roles.

###### Note

You must have an `iam:passRole` permission in your
current IAM user/role to the invoker role when creating or updating
the application. However, you do not need this permission to run an
assessment.

## Managing roles with the IAM API

A role's trust policy gives the specified principal's permission to
assume the role. To create the roles using AWS Command Line Interface (AWS CLI), use the
`create-role` command. While using this command, you can
specify the trust policy inline. The following example shows how to
grant the AWS Resilience Hub service the principal permission to assume your
role.

###### Note

The requirement to escape quotes (`' '`) in the JSON
string may vary based on your shell version.

**Sample
`create-role`**

```
aws iam create-role --role-name AWSResilienceHubAssessmentRole --assume-role-policy-document '{
  "Version": "2012-10-17",		 	 	 "Statement":
  [
    {
      "Effect": "Allow",
      "Principal": {"Service": "resiliencehub.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }
  ]
}'
```

## Defining trust policy using JSON file

You can define the trust policy for the role using a separate JSON
file and then run the `create-role` command. In the following
example, **`trust-policy.json`**
is a file that contains the trust policy in the current directory. This
policy is attached to a role by running **`create-role`** command. The output of the
`**create-role**`
command is shown in the **Sample Output**.
To add permissions to the role, use the **attach-policy-to-role** command and you can start by
adding the `AWSResilienceHubAsssessmentExecutionPolicy`
managed policy. For more information about this managed policy, see
[AWSResilienceHubAsssessmentExecutionPolicy](security-iam-awsmanpol.md#security_iam_aws-assessment-policy "security-iam-awsmanpol.md#security_iam_aws-assessment-policy").

**Sample
`trust-policy.json`**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Principal": {
 "Service": "resiliencehub.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }]
}`

```

**Sample
`create-role`**

`aws iam create-role --role-name AWSResilienceHubAssessmentRole
 --assume-role-policy-document file://trust-policy.json`

**Sample Output**

**Sample
`attach-policy-to-role`**

`aws iam attach-role-policy --role-name
 AWSResilienceHubAssessmentRole --policy-arn
 arn:aws:iam::aws:policy/AWSResilienceHubAsssessmentExecutionPolicy`
