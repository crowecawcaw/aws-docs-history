# Getting started with notebooks in AWS Glue Studio

When you start a notebook through AWS Glue Studio, all the configuration steps are done for you so that you can explore your data
and start developing your job script after only a few seconds.

The following sections describe how to create a role and grant the appropriate permissions to use notebooks in AWS Glue Studio
for ETL jobs.

For more information on actions defined by AWS Glue, see
[Actions defined by AWS Glue](../../../service-authorization/latest/reference/list_awsglue.md "../../../service-authorization/latest/reference/list_awsglue.md") .

###### Topics

- [Granting permissions for the IAM role](#studio-notebook-permissions "#studio-notebook-permissions")

## Granting permissions for the IAM role

Setting up AWS Glue Studio is a pre-requisite to using notebooks.

To use notebooks in AWS Glue, your role requires the following:

- A trust relationship with AWS Glue for the `sts:AssumeRole` action and, if you want tagging then
  `sts:TagSession`.
- An IAM policy containing all the permissions for notebooks, AWS Glue, and interactive sessions.
- An IAM policy for a pass role since the role needs to be able to pass itself from the notebook to interactive sessions.

For example, when you create a new role, you can add a standard AWS managed policy like `AWSGlueConsoleFullAccessRole`
to the role, and then add a new policy for the notebook operations and another for the IAM PassRole policy.

### Actions needed for a trust relationship with AWS Glue

When starting a notebook session, you must add the `sts:AssumeRole` to the trust relationship of the role that is
passed to the notebook. If your session includes tags, you must also pass the `sts:TagSession` action. Without these
actions, the notebook session cannot start.

For example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "glue.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

### Policies containing IAM permissions for notebooks

The following sample policy describes the required AWS IAM permissions for notebooks. If you are creating a new role,
create a policy that contains the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:StartNotebook",
 "glue:TerminateNotebook",
 "glue:GlueNotebookRefreshCredentials",
 "glue:DeregisterDataPreview",
 "glue:GetNotebookInstanceStatus",
 "glue:GlueNotebookAuthorize"
 ],
 "Resource": "*"
 }
 ]
}`

```

You can use the following IAM policies to allow access to specific resources:

- _AwsGlueSessionUserRestrictedNotebookServiceRole_: Provides full access to all AWS Glue resources
  except for sessions. Allows users to create and use only the notebook sessions that are associated with the user. This policy also
  includes other permissions needed by AWS Glue to manage AWS Glue resources in other AWS services.
- _AwsGlueSessionUserRestrictedNotebookPolicy_: Provides permissions that allows users to create and use only the
  notebook sessions that are associated with the user. This policy also includes permissions to explicitly allow users to pass a
  restricted AWS Glue session role.

### IAM policy to pass a role

When you create a notebook with a role, that role is then passed to interactive sessions so that the same
role can be used in both places. As such, the `iam:PassRole` permission needs to be part of the role's policy.

Create a new policy for your role using the following example. Replace the account number with your own and the role name.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::`111122223333`:role/`<role_name`>"
 }
 ]
}`

```
