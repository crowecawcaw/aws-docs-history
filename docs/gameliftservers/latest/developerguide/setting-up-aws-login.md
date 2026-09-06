

# Set up an AWS user account
<a name="setting-up-aws-login"></a>

**Tip**  
Use these topics to get help with these tasks:   
Get a new AWS account for use with Amazon GameLift Servers.
Create a user or group with permissions to work with Amazon GameLift Servers resources.
Set up security credentials (you need these to use the AWS CLI tools and the Amazon GameLift Servers plugins for Unreal and Unity)


As with all AWS services, you need an AWS account to use the Amazon GameLift Servers service and tools. An AWS account serves two primary functions: (1) it gives you a container for all the AWS resources that you create with the account; and (2) it lets you manage security for your AWS resources, including setting up user authentication and controlling user access permissions. There's no cost for creating an AWS account. 

**Explore Amazon GameLift Servers with or without an AWS account**  
You **don't** need an AWS account to:
+ Discover AWS tools for building, running, and growing game experiences at [AWS for Games](https://aws.amazon.com/gametech/). Read the [Blog](https://aws.amazon.com/blogs/gametech/) and browse the [Solutions for Games library](https://aws.amazon.com/solutions/games).
+ Learn more about Amazon GameLift Servers in the [product overview, FAQs, and resources](https://aws.amazon.com/gamelift/). **Ask AWS** to find answers to your product questions. (Try this one: "Looking for low-cost options to host my multiplayer game".)
+ For a deeper dive, find out what makes Amazon GameLift Servers work in the [technical documentation](https://docs.aws.amazon.com/gamelift/), including developer guides for hosting and matchmaking, and the service API reference guide.
+ Check out information on [Amazon GameLift Servers pricing](https://aws.amazon.com/gamelift/servers/pricing/) and cost optimization techniques. Try the [Pricing Calculator](https://calculator.aws/#/createCalculator/GameLift) to see how hosting costs are calculated based on peak concurrent player usage (CCU). 
+ Get downloads and see code repositories for Amazon GameLift Servers SDKs, plugins, and toolkits. See [Amazon GameLift Servers Getting started](https://aws.amazon.com/gamelift/servers/getting-started/). (You need an AWS account to use them.)

You **do** need an AWS account to: 
+ Follow onboarding workflows with the Amazon GameLift Servers plugins for Unreal and Unity, or use the game server wrapper.
+ Create and manage AWS resources using the AWS Management Console. 
+ Create and manage AWS resources using the AWS Command Line Interface.
+ Use Amazon Q with the In the Amazon GameLift Servers technical documentation to find answers, guidance, and recommendations. 

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Set user permissions for Amazon GameLift Servers](#getting-started-create-iam-user)
+ [Set up programmatic access for users](#getting-started-iam-user-access-keys)
+ [Set up programmatic access for your game](#getting-started-iam-player-user)
+ [IAM permission examples for Amazon GameLift Servers](gamelift-iam-policy-examples.md)
+ [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Set user permissions for Amazon GameLift Servers
<a name="getting-started-create-iam-user"></a>

Create additional users or extend access permissions to existing users as needed for your Amazon GameLift Servers resources. As a best practice ([ Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)), apply least-privilege permissions for all users. For guidance on permissions syntax, see [IAM permission examples for Amazon GameLift Servers](gamelift-iam-policy-examples.md).

Use the following instructions to set user permissions based on how you manage the users in your AWS account. 

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

When working with IAM users, as a best practice always attach permissions to roles or user groups, not individual users.

## Set up programmatic access for users
<a name="getting-started-iam-user-access-keys"></a>

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.



| Which user needs programmatic access? | To | By | 
| --- | --- | --- | 
| IAM | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Login for AWS local development](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs, see [Login for AWS local development](https://docs.aws.amazon.com/sdkref/latest/guide/access-login.html) in the *AWS SDKs and Tools Reference Guide*.  | 
| Workforce identity<br />(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*.  | 
| IAM | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions in [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the IAM User Guide. | 
| IAM | (Not recommended)Use long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Authenticating using IAM user credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs and tools, see [Authenticate using long-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html) in the *AWS SDKs and Tools Reference Guide*. <br />+  For AWS APIs, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*.  | 

If you use access keys, see [Best practices for managing AWS access keys](https://docs.aws.amazon.com/accounts/latest/reference/credentials-access-keys-best-practices.html).

## Set up programmatic access for your game
<a name="getting-started-iam-player-user"></a>

Most games use backend services to communicate with Amazon GameLift Servers using the AWS SDKs. Use a backend service (acting for a game client) to request game sessions, place players into games, and other tasks. These services need programmatic access and security credentials to authenticate calls to the service API for Amazon GameLift Servers. 

For Amazon GameLift Servers, you manage this access by creating a player user in AWS Identity and Access Management (IAM). Manage player user permissions through one of the following options:
+ Create an IAM role with player user permissions and allow the player user to assume the role when needed. The backend service must include code to assume this role before making requests to Amazon GameLift Servers. In accordance with security best practices, roles provide limited, temporary access. You can use roles for workloads running on AWS resources ([IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)) or outside of AWS ([IAM Roles Anywhere](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_non-aws.html)).
+ Create an IAM user group with player user permissions and add your player user to the group. This option gives your player user long-term credentials, which the backend service must store and use when communicating with Amazon GameLift Servers.

For permissions policy syntax, see [Player user permission examples](gamelift-iam-policy-examples.md#iam-policy-admin-game-dev-example). 

For more information on managing permissions for use by a workload, see [IAM Identities: Temporary credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html#id_temp-creds).