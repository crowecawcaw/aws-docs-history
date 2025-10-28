# Adding groups to a user pool

Support for groups in Amazon Cognito user pools enables you to create and manage groups, add users to
groups, and remove users from groups. Use groups to create collections of users to manage their
permissions or to represent different types of users. You can assign an AWS Identity and Access Management (IAM) role
to a group to define the permissions for members of a group.

You can use groups to create a collection of users in a user pool, which is often done to
set the permissions for those users. For example, you can create separate groups for users who
are readers, contributors, and editors of your website and app. Using the IAM role associated
with a group, you can also set different permissions for those different groups so that only
contributors can put content into Amazon S3 and only editors can publish content through an API in
Amazon API Gateway.

Amazon Cognito creates a user group for each OIDC, SAMl, and social [identity provider](cognito-user-pools-identity-federation.md#cognito-user-pools-identity-federation-how-it-works "cognito-user-pools-identity-federation.md#cognito-user-pools-identity-federation-how-it-works") (IdP)
that you add to your user pool. The name of the group is in the format `[user pool ID]_[IdP
 name]`, for example `us-east-1_EXAMPLE_MYSSO` or
`us-east-1_EXAMPLE_Google`. Each unique automatically-generated IdP user profile is
automatically added to this group. [Linked users](cognito-user-pools-identity-federation-consolidate-users.md "cognito-user-pools-identity-federation-consolidate-users.md") aren't
automatically added to this group, but you can add their profiles to the group in a separate
process.

You can create and manage groups in a user pool from the AWS Management Console, the APIs, and the CLI.
As a developer (using AWS credentials), you can create, read, update, delete, and list the
groups for a user pool. You can also add users and remove users from groups.

There is no additional cost for using groups within a user pool. See [Amazon Cognito Pricing](https://aws.amazon.com/cognito/pricing/ "https://aws.amazon.com/cognito/pricing/") for more information.

## Assigning IAM roles to groups

You can use groups to control permissions to your resources using an IAM role. IAM
roles include trust policies and permission policies. The role [trust](role-trust-and-permissions.md "role-trust-and-permissions.md") policy specifies who can use the role. The [permissions](iam-roles.md#access-policies "iam-roles.md#access-policies") policies specify the actions and resources that your group members can
access. When you create an IAM role, set up the role trust policy to allow your group's
users to assume the role. In the role permissions policies, specify the permissions that you
want your group to have.

When you create a group in Amazon Cognito, you specify an IAM role by providing the role’s
[ARN](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns"). When group members sign in using Amazon Cognito, they can receive temporary
credentials from the identity pools. Their permissions are determined by the associated IAM
role.

Individual users can be in multiple groups. As a developer, you have the following options
for automatically choosing the IAM role when a user is in multiple groups:

- You can assign precedence values to each group. The group with the better (lower)
  precedence will be chosen and its associated IAM role will be applied.
- Your app can also choose from among the available roles when requesting AWS
  credentials for a user through an identity pool, by specifying a role ARN in the [GetCredentialsForIdentity](../../../cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.md "../../../cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.md")
  `CustomRoleARN` parameter. The specified IAM role must match a role that is
  available to the user.

## Assigning precedence values to

groups

A user can belong to more than one group. In the user's access and ID tokens, the
`cognito:groups` claim contains the list of all the groups a user belongs to. The
`cognito:roles` claim contains the list of roles corresponding to the
groups.

Because a user can belong to more than one group, each group can be assigned a precedence.
This is a non-negative number that specifies the precedence of this group relative to the
other groups that a user belongs to in the user pool. Zero is the top precedence value. Groups
with lower precedence values take precedence over groups with higher or null precedence
values. If a user belongs to two or more groups, the group with the lowest precedence value
will have its IAM role applied to the `cognito:preferred_role` claim in the
user's ID token.

Two groups can have the same precedence value. If this happens, neither group takes
precedence over the other. If two groups with the same precedence value have the same role
ARN, that role is used in the `cognito:preferred_role` claim in ID tokens for users
in each group. If the two groups have different role ARNs, the
`cognito:preferred_role` claim is not set in users' ID tokens.

## Using groups to

control permission with Amazon API Gateway

You can use groups in a user pool to control permission with Amazon API Gateway. The groups that a
user is a member of are included in both the ID token and access token from a user pool in the
`cognito:groups` claim. You can submit ID or access tokens with requests to
Amazon API Gateway and use an Amazon Cognito user pool authorizer for a REST API. For more information, see
[Control access to a REST API using Amazon Cognito user pools as authorizer](../../../apigateway/latest/developerguide/apigateway-integrate-with-cognito.md "../../../apigateway/latest/developerguide/apigateway-integrate-with-cognito.md") in the
[API Gateway Developer Guide](../../../apigateway/latest/developerguide.md "../../../apigateway/latest/developerguide.md").

You can also authorize access to an Amazon API Gateway HTTP API with a custom JWT authorizer. For
more information, see [Controlling access to HTTP APIs with JWT authorizers](../../../apigateway/latest/developerguide/http-api-jwt-authorizer.md "../../../apigateway/latest/developerguide/http-api-jwt-authorizer.md") in the [API Gateway Developer Guide](../../../apigateway/latest/developerguide.md "../../../apigateway/latest/developerguide.md").

## Limitations on groups

User groups are subject to the following limitations:

- The number of groups you can create is limited by the [Amazon Cognito
  service quotas](quotas.md "quotas.md").
- Groups cannot be nested.
- You cannot search for users in a group.
- You cannot search for groups by name, but you can list groups.

## Creating a new group in the

AWS Management Console

Use the following procedure to create a new group.

###### To create a new group

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). If
   prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **Groups** menu, and then choose **Create a
   group**.
5. On the **Create a group** page, in **Group name**,
   enter a friendly name for your new group.
6. You can optionally provide additional information about this group using any of the
   following fields:
   - **Description** - Enter details about what this new group will be
     used for.
   - **Precedence** - Amazon Cognito evaluates and applies all group
     permissions for a given user based on which groups that they belong to has a lower
     precedence value. The group with the lower precedence will be chosen and its
     associated IAM role will be applied. For more information, see [Assigning precedence values to
     groups](#assigning-precedence-values-to-groups "#assigning-precedence-values-to-groups").
   - **IAM role** - You can assign an IAM role to your group when
     you need to control permissions to your resources. If you are integrating a user pool
     with an identity pool, the **IAM role** setting determines which
     role is assigned in the user's ID token if the identity pool is configured to choose
     the role from the token. For more information, see [Assigning IAM roles to groups](#assigning-iam-roles-to-groups "#assigning-iam-roles-to-groups").
   - **Add users to this group** - Add existing users as members of
     this group after it is created.

7. Choose **Create** to confirm.
