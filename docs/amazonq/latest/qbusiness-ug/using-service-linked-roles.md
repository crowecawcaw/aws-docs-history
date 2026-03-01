# Using service-linked roles for Amazon Q Business

Amazon Q Business uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that
is linked directly to Amazon Q Business. Service-linked roles are predefined by
Amazon Q Business and include all the permissions that the service requires to
call other AWS services on your behalf.

A service-linked role makes setting up Amazon Q Business easier because you don’t
have to manually add the necessary permissions. Amazon Q Business defines the
permissions of its service-linked roles, and unless defined otherwise, only Amazon Q Business can assume its roles. The defined permissions include the trust policy
and the permissions policy, and that permissions policy cannot be attached to any other
IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your Amazon Q Business resources because you can't inadvertently remove
permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for Amazon Q Business

Amazon Q Business uses one service-linked role named
`AWSServiceRoleForQBusiness` that performs certain actions in your
account. Examples of these actions include allowing CloudWatch to publish metrics and logs to
your AWS account.

### QBusinessServiceRolePolicy permissions details

The `QBusinessServiceRolePolicy` allows Amazon Q Business to
complete the following administrative actions on the user's behalf on all applicable
AWS resources:

- `logs` – Allows Amazon Q Business to describe,
  create and write to CloudWatch log streams
- `cloudwatch` – Allows Amazon Q Business to publish
  metric data points to CloudWatch under the AWS/QBusiness namespace

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessPutMetricDataPermission",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "AWS/QBusiness"
 }
 }
 },
 {
 "Sid": "QBusinessCreateLogGroupPermission",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/qbusiness/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "QBusinessDescribeLogGroupsPermission",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "QBusinessLogStreamPermission",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/qbusiness/*:log-stream:*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

Any updates to this policy are described in [Amazon Q Business updates to AWS managed
policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. For more information, see
[Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the IAM User Guide.

## Creating a service-linked role for Amazon Q Business

You don't need to manually create a service-linked role. When you [create an
Amazon Q Business application](../business-use-dg/create-app.md "../business-use-dg/create-app.md") in the AWS Management Console, the AWS CLI, or the
AWS API, Amazon Q Business creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you create a new
application, Amazon Q Business creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role. In the IAM CLI
or the IAM API, create a service-linked role with the
`qbusiness.amazonaws.com` service name. For more information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the IAM User Guide.
If you delete this service-linked role, you can use this same process to create the role
again.

You can also choose to create an Amazon Q Business application with a service
role instead of a service-linked role. However, using a service-linked role is
recommended.

## For Amazon Q Business applications created before April 2024

If your Amazon Q Business application was created before April 2024, it uses a
[service role](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") instead of a [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md").

To migrate your existing application from a service role to a service-linked role,
create a service-linked role with the `qbusiness.amazonaws.com` service name.
Then, if you use the console, select to use the newly created service-linked role when
you [update your application](../business-use-dg/supported-app-actions.md#update-app "../business-use-dg/supported-app-actions.md#update-app"). If you use the API, provide
the ARN of the service-linked role as the `roleArn` parameter when you use
the [UpdateApplication](../api-reference/API_UpdateApplication.md "../api-reference/API_UpdateApplication.md") API action.

For more information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the IAM User
Guide.

## Editing a service-linked role for Amazon Q Business

Amazon Q Business does not allow you to edit service-linked roles. After you
create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role
using IAM. For more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Changing between a service-role and a service-linked role for Amazon Q Business

You can choose to update the service-linked role you are using when you update an
application.

For an application using a service role, you can update the role to a service-linked
role.

For an application already using a service-linked role, you can update the role to a
service role.

You can also choose to continue using a service role, or update an existing service
role with a new one.

###### Note

Using a service-linked role is recommended.

For more information on how to update your application, see [Updating an application](../business-use-dg/supported-app-actions.md#update-app "../business-use-dg/supported-app-actions.md#update-app").

## Deleting a service-linked role for Amazon Q Business

You can manually delete your `AWSServiceRoleForQBusiness` role. If you no
longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is
not actively monitored or maintained. However, you must delete your application before
you can manually delete the service-linked role associated with it.

###### Note

If the Amazon Q Business service is using the role when you try to delete
the resources, then the deletion might fail. If that happens, wait for a few minutes
and try the operation again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the IAM CLI, or the IAM API to delete the
`AWSServiceRoleForQBusiness` service-linked role. For more information,
see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported regions for Amazon Q Business service-linked roles

Amazon Q Business supports using service-linked roles in all of the regions
where the service is available. For more information, see [Amazon Q Business
endpoints and quotas](../../../general/latest/gr/amazonq.md "../../../general/latest/gr/amazonq.md").
