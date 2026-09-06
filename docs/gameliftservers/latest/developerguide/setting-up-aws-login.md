# Set up an AWS user account

###### Tip

Use these topics to get help with these tasks:

- Get a new AWS account for use with Amazon GameLift Servers.
- Create a user or group with permissions to work with Amazon GameLift Servers resources.
- Set up security credentials (you need these to use the AWS CLI tools and the Amazon GameLift Servers plugins for Unreal and Unity)
-

As with all AWS services, you need an AWS account to use the Amazon GameLift Servers service and tools.
An AWS account serves two primary functions: (1) it gives you a container for all the
AWS resources that you create with the account; and (2) it lets you manage security for
your AWS resources, including setting up user authentication and controlling user access
permissions. There's no cost for creating an AWS account.

###### Explore Amazon GameLift Servers with or without an AWS account

You **don't** need an AWS account to:

- Discover AWS tools for building, running, and growing game experiences at
  [AWS for Games](https://aws.amazon.com/gametech/ "https://aws.amazon.com/gametech/"). Read the [Blog](https://aws.amazon.com/blogs/gametech/ "https://aws.amazon.com/blogs/gametech/") and browse the [Solutions for Games
  library](https://aws.amazon.com/solutions/games "https://aws.amazon.com/solutions/games").
- Learn more about Amazon GameLift Servers in the [product overview, FAQs,
  and resources](https://aws.amazon.com/gamelift/ "https://aws.amazon.com/gamelift/"). **Ask AWS** to find
  answers to your product questions. (Try this one: "Looking for low-cost options to
  host my multiplayer game".)
- For a deeper dive, find out what makes Amazon GameLift Servers work in the [technical documentation](../../../gamelift.md "../../../gamelift.md"), including developer
  guides for hosting and matchmaking, and the service API reference guide.
- Check out information on [Amazon GameLift Servers pricing](https://aws.amazon.com/gamelift/servers/pricing/ "https://aws.amazon.com/gamelift/servers/pricing/") and cost optimization techniques.
  Try the [Pricing Calculator](https://calculator.aws/#/createCalculator/GameLift "https://calculator.aws/#/createCalculator/GameLift") to see how hosting costs are calculated based on peak concurrent player usage (CCU).
- Get downloads and see code repositories for Amazon GameLift Servers SDKs, plugins, and toolkits. See
  [Amazon GameLift Servers Getting started](https://aws.amazon.com/gamelift/servers/getting-started/ "https://aws.amazon.com/gamelift/servers/getting-started/"). (You need an AWS account to use them.)
  You **do** need an AWS account to:

- Follow onboarding workflows with the Amazon GameLift Servers plugins for Unreal and Unity, or use
  the game server wrapper.
- Create and manage AWS resources using the AWS Management Console.
- Create and manage AWS resources using the AWS Command Line Interface.
- Use Amazon Q with the In the Amazon GameLift Servers technical documentation to find answers, guidance, and recommendations.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Set user permissions for Amazon GameLift Servers](#getting-started-create-iam-user "#getting-started-create-iam-user")
- [Set up programmatic access for users](#getting-started-iam-user-access-keys "#getting-started-iam-user-access-keys")
- [Set up programmatic access for your game](#getting-started-iam-player-user "#getting-started-iam-player-user")
- [IAM permission examples for Amazon GameLift Servers](gamelift-iam-policy-examples.md "gamelift-iam-policy-examples.md")
- [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md "setting-up-role.md")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Set user permissions for Amazon GameLift Servers

Create additional users or extend access permissions to existing users as needed for
your Amazon GameLift Servers resources. As a best practice ( [Security best practices in
IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")), apply least-privilege permissions for all users. For guidance on
permissions syntax, see [IAM permission examples for Amazon GameLift Servers](gamelift-iam-policy-examples.md "gamelift-iam-policy-examples.md").

Use the following instructions to set user permissions based on how you manage the users
in your AWS account.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:

  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

When working with IAM users, as a best practice always attach permissions to roles or
user groups, not individual users.

## Set up programmatic access for users

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                                  | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM                                                          | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Login for AWS local development](../../../cli/latest/userguide/cli-configure-sign-in.md "../../../cli/latest/userguide/cli-configure-sign-in.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs, see [Login for AWS local development](../../../sdkref/latest/guide/access-login.md "../../../sdkref/latest/guide/access-login.md") in the<br>_AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                                                             |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

If you use access keys, see [Best
practices for managing AWS access keys](../../../accounts/latest/reference/credentials-access-keys-best-practices.md "../../../accounts/latest/reference/credentials-access-keys-best-practices.md").

## Set up programmatic access for your game

Most games use backend services to communicate with Amazon GameLift Servers using the AWS SDKs. Use a
backend service (acting for a game client) to request game sessions, place players into
games, and other tasks. These services need programmatic access and security credentials
to authenticate calls to the service API for Amazon GameLift Servers.

For Amazon GameLift Servers, you manage this access by creating a player user in AWS Identity and Access Management (IAM).
Manage player user permissions through one of the following options:

- Create an IAM role with player user permissions and allow the player user to
  assume the role when needed. The backend service must include code to assume
  this role before making requests to Amazon GameLift Servers. In accordance with security best
  practices, roles provide limited, temporary access. You can use roles for
  workloads running on AWS resources ([IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md"))
  or outside of AWS ([IAM
  Roles Anywhere](../../../IAM/latest/UserGuide/id_roles_common-scenarios_non-aws.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_non-aws.md")).
- Create an IAM user group with player user permissions and add your player
  user to the group. This option gives your player user long-term credentials,
  which the backend service must store and use when communicating with
  Amazon GameLift Servers.

For permissions policy syntax, see [Player user permission examples](gamelift-iam-policy-examples.md#iam-policy-admin-game-dev-example "gamelift-iam-policy-examples.md#iam-policy-admin-game-dev-example").

For more information on managing permissions for use by a workload, see [IAM
Identities: Temporary credentials in IAM](../../../IAM/latest/UserGuide/id.md#id_temp-creds "../../../IAM/latest/UserGuide/id.md#id_temp-creds").
