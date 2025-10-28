# Policies for tag-based access control

You can use conditions in your identity-based policy to control access to applications and
job runs based on tags.

The following examples demonstrate different scenarios and ways to use condition operators
with EMR Serverless condition keys. These IAM policy statements are intended for
demonstration purposes only and should not be used in production environments. There are
multiple ways to combine policy statements to grant and deny permissions according to your
requirements. For more information about planning and testing IAM policies, refer to the [IAM user Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

###### Important

Explicitly denying permission for tagging actions is an important consideration. This
prevents users from tagging a resource and thereby granting themselves permissions that you
did not intend to grant. If tagging actions for a resource are not denied, a user can modify
tags and circumvent the intention of the tag-based policies. For an example of a policy that
denies tagging actions, refer to [Deny access to add and remove tags](#security-iam-TBAC-deny "#security-iam-TBAC-deny").

The examples below demonstrate identity-based permissions policies that are used to
control the actions that are allowed with EMR Serverless applications.

## Allow actions only on resources with specific tag

values

In the following policy example, the `StringEquals` condition operator tries
to match `dev` with the value for the tag department. If the tag department
hasn't been added to the application, or doesn't contain the value `dev`, the
policy doesn't apply, and the actions aren't allowed by this policy. If no other policy
statements allow the actions, the user can only work with applications that have this tag
with this value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "emr-serverless:GetApplication"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/department": "dev"
 }
 },
 "Sid": "AllowEMRSERVERLESSGetapplication"
 }
 ]
}`

```

You can also specify multiple tag values using a condition operator. For example, to
allow actions on applications where the `department` tag contains the value
`dev` or `test`, replace the condition block in the
earlier example with the following.

```
"Condition": {
        "StringEquals": {
          "emr-serverless:ResourceTag/department": ["dev", "test"]
        }
      }
```

## Require tagging when a resource is

created

In the example below, the tag needs to be applied when creating the application.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "emr-serverless:CreateApplication"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": "us-east-1"
 }
 },
 "Sid": "AllowEMRSERVERLESSCreateapplication"
 }
 ]
}`

```

The following policy statement allows a user to create an application only if the
application has a `department` tag, which can contain any value.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "emr-serverless:CreateApplication"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": ["us-east-1", "us-west-2"]
 }
 },
 "Sid": "AllowEMRSERVERLESSCreateapplication"
 }
 ]
}`

```

## Deny access to add and remove tags

This policy prevents a user from adding or removing tags on EMR Serverless applications
with a `department` tag whose value is not `dev`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "emr-serverless:TagResource",
 "emr-serverless:UntagResource"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringNotEquals": {
 "aws:PrincipalTag/department": "dev"
 }
 },
 "Sid": "AllowEMRSERVERLESSTagresource"
 }
 ]
}`

```
