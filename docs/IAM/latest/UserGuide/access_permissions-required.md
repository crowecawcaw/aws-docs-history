# Permissions required to access IAM

resources

_Resources_ are objects within a service. IAM resources
include groups, users, roles, and policies. If you are signed in with AWS account root user credentials,
you have no restrictions on administering IAM credentials or IAM resources. However,
IAM users must explicitly be given permissions to administer credentials or IAM resources.
You can do this by attaching an identity-based policy to the user.

###### Note

Throughout the AWS documentation, when we refer to an IAM policy without mentioning
any of the specific categories, we mean an identity-based, customer managed policy. For
details about policy categories, see [Policies and permissions in AWS Identity and Access Management](access_policies.md "access_policies.md").

## Permissions for administering IAM

identities

The permissions that are required to administer IAM groups, users, roles, and
credentials usually correspond to the API actions for the task. For example, in order to
create IAM users, you must have the `iam:CreateUser` permission that has the
corresponding API command: [`CreateUser`](../APIReference/API_CreateUser.md "../APIReference/API_CreateUser.md"). To allow an IAM user to create other IAM users, you
could attach an IAM policy like the following one to that user:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "iam:CreateUser",
 "Resource": "*"
 }
}`

```

In a policy, the value of the `Resource` element depends on the action and what
resources the action can affect. In the preceding example, the policy allows a user to create
any user (`*` is a wildcard that matches all strings). In contrast, a policy that
allows users to change only their own access keys (API actions [`CreateAccessKey`](../APIReference/API_CreateAccessKey.md "../APIReference/API_CreateAccessKey.md") and [`UpdateAccessKey`](../APIReference/API_UpdateAccessKey.md "../APIReference/API_UpdateAccessKey.md")) typically
has a `Resource` element. In this case the ARN includes a variable
(`${aws:username}`) that resolves to the current user's name, as in the following
example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListUsersForConsole",
 "Effect": "Allow",
 "Action": "iam:ListUsers",
 "Resource": "arn:aws:iam::*:*"
 },
 {
 "Sid": "ViewAndUpdateAccessKeys",
 "Effect": "Allow",
 "Action": [
 "iam:UpdateAccessKey",
 "iam:CreateAccessKey",
 "iam:ListAccessKeys"
 ],
 "Resource": "arn:aws:iam::*:user/${aws:username}"
 }
 ]
}`

```

In the previous example, `${aws:username}` is a variable that resolves to the
user name of the current user. For more information about policy variables, see [IAM policy elements: Variables and tags](reference_policies_variables.md "reference_policies_variables.md").

Using a wildcard character (`*`) in the action name often makes it easier to
grant permissions for all the actions related to a specific task. For example, to allow users
to perform any IAM action, you can use `iam:*` for the action. To allow users to
perform any action related just to access keys, you can use `iam:*AccessKey*` in
the `Action` element of a policy statement. This gives the user permission to
perform the [`CreateAccessKey`](../APIReference/API_CreateAccessKey.md "../APIReference/API_CreateAccessKey.md"), [`DeleteAccessKey`](../APIReference/API_DeleteAccessKey.md "../APIReference/API_DeleteAccessKey.md"), [`GetAccessKeyLastUsed`](../APIReference/API_GetAccessKeyLastUsed.md "../APIReference/API_GetAccessKeyLastUsed.md"),
[`ListAccessKeys`](../APIReference/API_ListAccessKeys.md "../APIReference/API_ListAccessKeys.md"), and
[`UpdateAccessKey`](../APIReference/API_UpdateAccessKey.md "../APIReference/API_UpdateAccessKey.md")
actions. (If an action is added to IAM in the future that has "AccessKey" in the name, using
`iam:*AccessKey*` for the `Action` element will also give the user
permission to that new action.) The following example shows a policy that allows users to
perform all actions pertaining to their own access keys (replace
`account-id` with your AWS account ID):

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "iam:*AccessKey*",
 "Resource": "arn:aws:iam::`111122223333`:user/${aws:username}"
 }
}`

```

Some tasks, such as deleting a group, involve multiple actions: You must first remove
users from the group, then detach or delete the group's policies, and then actually delete the
group. If you want a user to be able to delete a group, you must be sure to give the user
permissions to perform all of the related actions.

## Permissions for working in the

AWS Management Console

The preceding examples show policies that allow a user to perform the actions with the
[AWS CLI](http://aws.amazon.com/cli/ "http://aws.amazon.com/cli/") or the [AWS SDKs](http://aws.amazon.com/tools/ "http://aws.amazon.com/tools/").

As users work with the console, the console issues requests to IAM to list groups,
users, roles, and policies, and to get the policies associated with a group, user, or role.
The console also issues requests to get AWS account information and information about the
principal. The principal is the user making requests in the console.

In general, to perform an action, you must have only the matching action included in a
policy. To create a user, you need permission to call the `CreateUser` action.
Often, when you use the console to perform an action, you must have permissions to display,
list, get, or otherwise view resources in the console. This is necessary so that you can
navigate through the console to make the specified action. For example, if user Jorge wants to
use the console to change his own access keys, he goes to the IAM console and chooses
**Users**. This action causes the console to make a [`ListUsers`](../APIReference/API_ListUsers.md "../APIReference/API_ListUsers.md") request. If Jorge
doesn't have permission for the `iam:ListUsers` action, the console is denied
access when it tries to list users. As a result, Jorge can't get to his own name and to his
own access keys, even if he has permissions for the [`CreateAccessKey`](../APIReference/API_CreateAccessKey.md "../APIReference/API_CreateAccessKey.md") and [`UpdateAccessKey`](../APIReference/API_UpdateAccessKey.md "../APIReference/API_UpdateAccessKey.md")
actions.

If you want to give users permissions to administer groups, users, roles, policies, and
credentials with the AWS Management Console, you need to include permissions for the actions that the
console performs. For some examples of policies that you can use to grant a user for these
permissions, see [Example policies for
administering IAM resources](id_credentials_delegate-permissions_examples.md "id_credentials_delegate-permissions_examples.md").

## Grant permissions across AWS

accounts

You can directly grant IAM users in your own account access to your resources. If users
from another account need access to your resources, you can create an IAM role, which is
an entity that includes permissions but that isn't associated with a specific user. Users from
other accounts can then use the role and access resources according to the permissions you've
assigned to the role. For more information, see [Access for an IAM user in another
AWS account that you own](id_roles_common-scenarios_aws-accounts.md "id_roles_common-scenarios_aws-accounts.md").

###### Note

Some services support resource-based policies as described in [Identity-based policies and
resource-based policies](access_policies_identity-vs-resource.md "access_policies_identity-vs-resource.md") (such as Amazon S3, Amazon SNS, and Amazon SQS). For those services, an alternative to using roles is to attach a policy to the resource (bucket, topic, or queue)
that you want to share. The resource-based policy can specify the AWS account that has
permissions to access the resource.

## Permissions for one service to access

another

Many AWS services access other AWS services. For example, several AWS
services—including Amazon EMR, Elastic Load Balancing, and Amazon EC2 Auto Scaling—manage Amazon EC2 instances.
Other AWS services make use of Amazon S3 buckets, Amazon SNS topics, Amazon SQS queues, and so on.

The scenario for managing permissions in these cases varies by service. Here are some
examples of how permissions are handled for different services:

- In Amazon EC2 Auto Scaling, users must have permission to use Auto Scaling, but don't need to be explicitly
  granted permission to manage Amazon EC2 instances.
- In AWS Data Pipeline, an IAM role determines what a pipeline can do; users need permission to
  assume the role. (For details, see [Granting
  Permissions to Pipelines with IAM](../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md "../../../datapipeline/latest/DeveloperGuide/dp-iam-roles.md") in the
  _AWS Data Pipeline Developer Guide_.)

For details about how to configure permissions properly so that an AWS service is able
to accomplish the tasks you intend, refer to the documentation for the service you are
calling. To learn how to create a role for a service, see [Create a role to delegate permissions to an
AWS service](id_roles_create_for-service.md "id_roles_create_for-service.md").

###### Configuring a service with an IAM role to work on your behalf

When you want to configure an AWS service to work on your behalf, you typically
provide the ARN for an IAM role that defines what the service is allowed to do. AWS
checks to ensure that you have permissions to pass a role to a service. For more
information, see [Grant a user permissions to pass a role to an AWS
service](id_roles_use_passrole.md "id_roles_use_passrole.md").

## Required actions

Actions are the things that you can do to a resource, such as viewing, creating, editing,
and deleting that resource. Actions are defined by each AWS service.

To allow someone to perform an action, you must include the necessary actions in a policy
that applies to the calling identity or the affected resource. In general, to provide the
permission required to perform an action, you must include that action in your policy. For
example, to create a user, you need add the CreateUser action to your policy.

In some cases, an action might require that you include additional related actions in your
policy. For example, to provide permission for someone to create a directory in AWS Directory Service
using the `ds:CreateDirectory` operation, you must include the following actions in
their policy:

- `ds:CreateDirectory`
- `ec2:DescribeSubnets`
- `ec2:DescribeVpcs`
- `ec2:CreateSecurityGroup`
- `ec2:CreateNetworkInterface`
- `ec2:DescribeNetworkInterfaces`
- `ec2:AuthorizeSecurityGroupIngress`
- `ec2:AuthorizeSecurityGroupEgress`

When you create or edit a policy using the visual editor, you receive warnings and prompts
to help you choose all of the required actions for your policy.

For more information about the permissions required to create a directory in AWS Directory Service,
see [Example 2: Allow a User to Create a Directory](../../../directoryservice/latest/admin-guide/IAM_Auth_Access_IdentityBased.md#IAMPolicyExamples_DS_create_directory "../../../directoryservice/latest/admin-guide/IAM_Auth_Access_IdentityBased.md#IAMPolicyExamples_DS_create_directory").
