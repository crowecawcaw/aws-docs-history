# AWS managed policies for AWS App Studio

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy: AppStudioServiceRolePolicy

You can't attach `AppStudioServiceRolePolicy` to your IAM entities. This policy is attached to a
service-linked role that allows App Studio to perform actions on your behalf. For more
information, see [Service-linked roles for App Studio](appstudio-service-linked-roles.md "appstudio-service-linked-roles.md").

This policy grants permissions that allow the service-linked role to manage AWS resources.

### Permissions details

This policy includes permissions to do the following:

- `logs` - Create CloudWatch log groups and log streams. Also gives permission to create log events in those log groups and streams.
- `secretsmanager` - Create, read, update, and delete managed secrets that are managed by App Studio.
- `sso` - Retrieve application instances.
- `sso-directory` - Retrieve information about users and retrieve the list of members in groups.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AppStudioResourcePermissionsForCloudWatch",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/appstudio/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "AppStudioResourcePermissionsForSecretsManager",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:CreateSecret",
 "secretsmanager:DeleteSecret",
 "secretsmanager:DescribeSecret",
 "secretsmanager:GetSecretValue",
 "secretsmanager:PutSecretValue",
 "secretsmanager:UpdateSecret",
 "secretsmanager:TagResource"
 ],
 "Resource": "arn:aws:secretsmanager:*:*:secret:appstudio-*",
 "Condition": {
 "ForAllValues:StringEquals": {
 "aws:TagKeys": [
 "IsAppStudioSecret"
 ]
 },
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}",
 "aws:ResourceTag/IsAppStudioSecret": "true"
 }
 }
 },
 {
 "Sid": "AppStudioResourcePermissionsForManagedSecrets",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:DeleteSecret",
 "secretsmanager:DescribeSecret",
 "secretsmanager:GetSecretValue",
 "secretsmanager:PutSecretValue",
 "secretsmanager:UpdateSecret"
 ],
 "Resource": "arn:aws:secretsmanager:*:*:secret:appstudio!*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}",
 "secretsmanager:ResourceTag/aws:secretsmanager:owningService": "appstudio"
 }
 }
 },
 {
 "Sid": "AppStudioResourceWritePermissionsForManagedSecrets",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:CreateSecret"
 ],
 "Resource": "arn:aws:secretsmanager:*:*:secret:appstudio!*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "AppStudioResourcePermissionsForSSO",
 "Effect": "Allow",
 "Action": [
 "sso:GetManagedApplicationInstance",
 "sso-directory:DescribeUsers",
 "sso-directory:ListMembersInGroup"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

## App Studio updates to AWS managed policies

View details about updates to AWS managed policies for App Studio since this service
began tracking these changes.

| Change                                                                                                                                                                  | Description                                                                                              | Date           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------- |
| [AppStudioServiceRolePolicy](#security-iam-awsmanpol-appstudioservicerolepolicy "#security-iam-awsmanpol-appstudioservicerolepolicy") –<br>Update to an existing policy | App Studio added new permissions to allow managing of App Studio managed secrets in AWS Secrets Manager. | March 14, 2025 |
| App Studio started tracking changes                                                                                                                                     | App Studio started tracking changes for its AWS managed policies.                                        | June 28, 2024  |
