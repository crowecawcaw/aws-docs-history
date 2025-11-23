# Identity-based policy examples

for Amazon GameLift Servers

By default, users and roles don't have permission to create or modify Amazon GameLift Servers
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon GameLift Servers, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon GameLift Servers](../../../service-authorization/latest/reference/list_amazongamelift.md "../../../service-authorization/latest/reference/list_amazongamelift.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the
  Amazon GameLift Servers console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow
  users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Allow player
  access for game sessions](#security_iam_id-based-policy-examples-player-access "#security_iam_id-based-policy-examples-player-access")
- [Allow
  access to one Amazon GameLift Servers queue](#security_iam_id-based-policy-examples-access-one-bucket "#security_iam_id-based-policy-examples-access-one-bucket")
- [View
  Amazon GameLift Servers fleets based on tags](#security_iam_id-based-policy-examples-view-fleet-tags "#security_iam_id-based-policy-examples-view-fleet-tags")
- [Access a
  game build file in Amazon S3](#security_iam_id-based-policy-examples-access-storage-loc "#security_iam_id-based-policy-examples-access-storage-loc")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon GameLift Servers resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Using the

Amazon GameLift Servers console

To access the Amazon GameLift Servers console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Amazon GameLift Servers
resources in your AWS account. If you create an identity-based policy that is more
restrictive than the minimum required permissions, the console won't function as
intended for entities (users or roles) with that policy.

To ensure that those entities can still use the Amazon GameLift Servers console, add
permissions to users and groups with the syntax in the following examples and in
[Administration permission examples](gamelift-iam-policy-examples.md#iam-policy-simple-example "gamelift-iam-policy-examples.md#iam-policy-simple-example"). For more information, see [Set user permissions for Amazon GameLift Servers](setting-up-aws-login.md#getting-started-create-iam-user "setting-up-aws-login.md#getting-started-create-iam-user").

Users that work with Amazon GameLift Servers through AWS CLI or AWS API operations don't
require minimum console permissions. Instead, you can limit access to only the
operations the user needs to perform. For example, a player user, acting on behalf
of game clients, requires access to request game sessions, place players into games,
and other tasks.

For information about the permissions required to use all Amazon GameLift Servers console
features, see permissions syntax for administrators in [Administration permission examples](gamelift-iam-policy-examples.md#iam-policy-simple-example "gamelift-iam-policy-examples.md#iam-policy-simple-example").

## Allow

users to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Allow player

access for game sessions

To place players into game sessions, game clients and backend services need
permissions. For policy examples for these scenarios, see [Player user permission examples](gamelift-iam-policy-examples.md#iam-policy-admin-game-dev-example "gamelift-iam-policy-examples.md#iam-policy-admin-game-dev-example").

## Allow

access to one Amazon GameLift Servers queue

The following example provides a user with access to a specific Amazon GameLift Servers
queues.

This policy grants the user permissions to add, update, and delete queue
destinations with the following actions:
`gamelift:UpdateGameSessionQueue`,
`gamelift:DeleteGameSessionQueue`, and
`gamelift:DescribeGameSessionQueues`. As shown, this policy uses the
`Resource` element to limit access to a single queue:
`gamesessionqueue/examplequeue123`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"ViewSpecificQueueInfo",
 "Effect":"Allow",
 "Action":[
 "gamelift:DescribeGameSessionQueues"
 ],
 "Resource":"arn:aws:gamelift:us-east-1:555555555555:gamesessionqueue/examplequeue123"
 },
 {
 "Sid":"ManageSpecificQueue",
 "Effect":"Allow",
 "Action":[
 "gamelift:UpdateGameSessionQueue",
 "gamelift:DeleteGameSessionQueue"
 ],
 "Resource":"arn:aws:gamelift:us-east-1:111122223333:gamesessionqueue/examplequeue123"
 }
 ]
}`

```

## View

Amazon GameLift Servers fleets based on tags

You can use conditions in your identity-based policy to control access to
Amazon GameLift Servers resources based on tags. This example shows how you can create a policy
that allows viewing a fleet if the `Owner` tag matches the user's user
name. This policy also grants the permissions necessary to complete this operation
in the console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListFleetsInConsole",
 "Effect": "Allow",
 "Action": "gamelift:ListFleets",
 "Resource": "*"
 },
 {
 "Sid": "ViewFleetIfOwner",
 "Effect": "Allow",
 "Action": "gamelift:DescribeFleetAttributes",
 "Resource": "arn:aws:gamelift:*:*:fleet/*",
 "Condition": {
 "StringEquals": {"aws:ResourceAccount": "${aws:username}"}
 }
 }
 ]
}`

```

## Access a

game build file in Amazon S3

After you integrate your game server with Amazon GameLift Servers, upload the build files to Amazon S3.
For Amazon GameLift Servers to access the build files, use the following policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": "arn:aws:s3:::`bucket-name`/`object-name`"
 }
 ]
}`

```

For more information about uploading Amazon GameLift Servers game files, see [Create a game server build for Amazon GameLift Servers](gamelift-build-cli-uploading.md "gamelift-build-cli-uploading.md").
