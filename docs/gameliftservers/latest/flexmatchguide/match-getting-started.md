# Getting started with FlexMatch

Use the resources in this section to help you get started with buildiing a matchmaking
system with FlexMatch.

###### Topics

- [Set up an AWS account for FlexMatch](#match-setting-up "#match-setting-up")
- [Roadmap: Create a standalone matchmaking solution with FlexMatch](match-tasks-safm.md "match-tasks-safm.md")
- [Roadmap: Add matchmaking to a Amazon GameLift Servers hosting solution](match-tasks.md "match-tasks.md")

## Set up an AWS account for FlexMatch

Amazon GameLift Servers FlexMatch is an AWS service, and you must have an AWS account to use this service.
Creating an AWS account is free. For more information on what you can do with an AWS
account, see [Getting Started with
AWS](https://aws.amazon.com/getting-started/ "https://aws.amazon.com/getting-started/").

If you are using FlexMatch with other Amazon GameLift Servers solutions, see the following topics:

- [Setting up access for Amazon GameLift Servers hosting](../../../gamelift/latest/developerguide/setting-up-intro.md "../../../gamelift/latest/developerguide/setting-up-intro.md")
- [Setting up access for hosting with Amazon GameLift Servers FleetIQ](../../../gamelift/latest/fleetiqguide/gsg-iam-permissions.md "../../../gamelift/latest/fleetiqguide/gsg-iam-permissions.md")

###### To set up your account for Amazon GameLift Servers

1. **Get an account.** Open [Amazon Web Services](https://aws.amazon.com/ "https://aws.amazon.com/") and choose **Sign In to the
   Console**. Follow the prompts to either create a new account or sign in
   to an existing one.
2. **Set up an administrative user group.** Open the
   AWS Identity and Access Management (IAM) service console and follow the steps to create or update users or
   user groups. IAM manages access to your AWS services and resources. Everyone who
   accesses your FlexMatch resources, using the Amazon GameLift Servers console or by calling Amazon GameLift Servers APIs,
   must be given explicit access. For detailed instructions on using the console (or
   the AWS CLI or other tools) to set up user groups, see [Creating IAM Users](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md").
3. **Attach a permissions policy to your user or user group.** Access to AWS services and resources are managed by attaching an [IAM policy](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") to a user or user
   group. Permissions policies specify a set of AWS services and actions a user has
   to have access to.

For Amazon GameLift Servers, you must create a custom permissions policy and attach it to each user
or user group. A policy is a JSON document. Use the example below to create your
policy.

The following example illustrates an inline permissions policy with administrative
permissions for all Amazon GameLift Servers resources and actions. You can choose to limit access by
specifying only FlexMatch-specific items.

JSON

```
`{
"Version":"2012-10-17",
"Statement":
 {
 "Effect": "Allow",
 "Action": "gamelift:*",
 "Resource": "*"
 }
}`

```
