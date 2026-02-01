# User pool case sensitivity

Amazon Cognito user pools that you create in the AWS Management Console are case insensitive by
default. When a user pool is case insensitive, *user@example.com* and *User@example.com* refer
to the same user. When usernames in a user pool are case insensitive, the
`preferred_username` and `email` attributes also are case
insensitive.

Case insensitivity applies not only to attribute inputs, but outputs too. Mixed-case
attribute values in case-insensitive user pools are flattened to lowercase in user pool text
output. Examples of user pool text output are [userInfo](userinfo-endpoint.md "userinfo-endpoint.md") responses, user query responses like the output of [GetUser](../../../cognito-user-identity-pools/latest/APIReference/API_GetUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetUser.md"), and input events to [Lambda triggers](cognito-user-pools-working-with-lambda-triggers.md "cognito-user-pools-working-with-lambda-triggers.md").

To account for user pool case sensitivity settings, identify users in your app code based
on an alternative user attribute. Because the case of a username, preferred username, or email
address attribute can vary in different user profiles, refer instead to the `sub`
attribute. You can also create an immutable custom attribute in your user pool, and assign
your own unique identifier value to the attribute in each new user profile. When you first
create a user, you can write a value to the immutable custom attribute that you
created.

###### Note

Regardless of the case sensitivity settings of your user pool, Amazon Cognito requires that a
federated user from a SAML or OIDC identity provider (IdP) pass a unique and case-sensitive
`NameId` or `sub` claim. For more information about unique
identifier case sensitivity and SAML IdPs, see [Implement
SP-initated SAML sign-in](cognito-user-pools-SAML-session-initiation.md#cognito-user-pools-saml-idp-authentication "cognito-user-pools-SAML-session-initiation.md#cognito-user-pools-saml-idp-authentication").

Creating a case-sensitive user pool

If you create resources with the AWS Command Line Interface (AWS CLI) and API operations such as [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md"), you must set the
Boolean `CaseSensitive` parameter to `false`. This setting creates
a case-insensitive user pool. If you do not specify a value, `CaseSensitive`
defaults to `true`. User pools that you create in the Amazon Cognito console are not
case-sensitive. To produce a case-sensitive user pool, you must use the
`CreateUserPool` operation. Before February 12, 2020, user pools defaulted
to case sensitive regardless of platform.

In the **Sign-in** menu of the AWS Management Console
and in the `UsernameConfiguration` property of [DescribeUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UserPoolType.md#CognitoUserPools-Type-UserPoolType-UsernameConfiguration "../../../cognito-user-identity-pools/latest/APIReference/API_UserPoolType.md#CognitoUserPools-Type-UserPoolType-UsernameConfiguration"), you can review the case sensitivity
settings for each user pool in your account.

Migrating to a new user pool

Because of potential conflicts between user profiles, you can't change an Amazon Cognito user
pool from case-sensitive to case-insensitive. Instead, migrate your users to a new user
pool. You must build migration code to resolve case-related conflicts. This code must
either return a unique new user or reject the sign-in attempt when it detects a
conflict. In a new case-insensitive user pool, assign a [Migrate user Lambda trigger](user-pool-lambda-migrate-user.md "user-pool-lambda-migrate-user.md"). The AWS Lambda function can create users in the new case-insensitive user pool. When
the user fails sign-in with the case-insensitive user pool, the Lambda function finds and
duplicates the user from the case-sensitive user pool. You can also activate a migrate
user Lambda trigger on [ForgotPassword](../../../cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_ForgotPassword.md") events. Amazon Cognito passes user information and event metadata from
the sign-in or password-recovery action to your Lambda function. You can use event data
to manage conflicts between usernames and email addresses when your function creates the
new user in your case-insensitive user pool. These conflicts are between usernames and
email addresses that would be unique in a case-sensitive user pool, but identical in a
case-insensitive user pool.

For more information about how to use a migrate user Lambda trigger between Amazon Cognito user pools,
see [Migrating Users to
Amazon Cognito user pools](https://aws.amazon.com/blogs/mobile/migrating-users-to-amazon-cognito-user-pools/ "https://aws.amazon.com/blogs/mobile/migrating-users-to-amazon-cognito-user-pools/") in the AWS blog.
