# Understanding authentication sessions in IAM Identity Center

When a user signs in to the [AWS access portal](using-the-portal.md "using-the-portal.md"), IAM Identity Center creates an authentication session that
represents the user’s verified identity.

Once authenticated, the user can access all their assigned AWS accounts, [AWS managed applications](awsapps.md "awsapps.md"), and [customer managed applications](customermanagedapps.md "customermanagedapps.md") that administrators
have granted them permission to use, without additional sign ins.

## Types of authentication sessions

### User interactive sessions

After a user signs in to the AWS access portal, IAM Identity Center creates a user interactive
session. This session represents the user's authenticated state within IAM Identity Center and
serves as the foundation for creating other session types. User interactive
sessions can last for the duration configured in IAM Identity Center, which can
be up to 90 days.

User interactive sessions are the primary authentication mechanism. They end
when the user signs out or when an administrator ends their session. The
duration of these sessions should be carefully configured based on your
organization's security requirements.

For information about configuring user interactive session duration, see [Configure the session duration in IAM Identity Center](configure-user-session.md "configure-user-session.md").

### Application sessions

Application sessions are the authenticated connections between users and AWS
managed applications (such as Amazon Q Developer or Amazon Quick Suite) that IAM Identity Center establishes through
single sign-on.

By default, application sessions have a one hour lifetime, but they're
automatically refreshed as long as the underlying user interactive session remains
valid. This refresh mechanism provides a seamless experience for users while
maintaining security controls. When a user interactive session ends, either through
user sign-out or administrator action, the application sessions will end at their
next refresh attempt, typically within 30 minutes.

### User background sessions

User background sessions are extended-duration sessions designed for
applications that need to run processes for hours or days without interruption.
Currently, this session type applies primarily to [Amazon SageMaker Studio](../../../sagemaker/latest/dg/studio-updated.md "../../../sagemaker/latest/dg/studio-updated.md"), where
data scientists might run machine learning training jobs that take many hours to
complete.

For information about configuring user background session duration,
see [User background sessions](user-background-sessions.md "user-background-sessions.md").

### Amazon Q Developer sessions

You can extend Amazon Q Developer sessions to allow developers using Amazon Q Developer in
IDEs to maintain authentication for up to 90 days. This feature reduces login
interruptions while you work on code.

These sessions are independent of other session types and don't affect user interactive sessions or other
AWS managed applications. Depending on when you enabled IAM Identity Center, this feature might be enabled by default.

For information about configuring extended Amazon Q Developer sessions, see [Extended sessions for Amazon Q Developer](90-day-extended-session-duration.md "90-day-extended-session-duration.md").

### IAM Identity Center-created IAM role sessions

IAM Identity Center creates a different type of session when users access the AWS Management Console or AWS CLI. In these cases, IAM Identity Center
uses the sign-in session to obtain an IAM session by assuming an IAM role specified in the user's permission set.

###### Important

Unlike application sessions, IAM role sessions operate independently once
established. They persist for the duration configured in the permission set,
which can be up to 12 hours, regardless of the status of the original sign-in
session. This behavior ensures that long-running CLI operations or console
sessions aren't unexpectedly ended.

## Ways to end user sessions in IAM Identity Center

### User-initiated

When a user signs out of the AWS access portal, the sign-in session ends, preventing the user from accessing any new resources.

Existing application sessions, however, don't end instantly. Instead, they
will end within approximately 30 minutes, when they attempt their next refresh
and find the sign-in session is no longer valid. Existing IAM role sessions
continue until they expire based on the permission set configuration, which
could be up to 12 hours later.

### Administrator-initiated

Anyone with IAM Identity Center administrative permissions in your organization, typically IT administrators or
security teams, can [end a user's session](end-active-sessions.md "end-active-sessions.md"). This action works the same way as if users signed out
themselves, allowing administrators to require users to sign in again when needed. This capability
is useful when security policies change or when suspicious activity is detected.

When an IAM Identity Center administrator [deletes a user](deleteusers.md "deleteusers.md") or
[disables a user’s access](disableuser.md "disableuser.md"), the user loses access to the
AWS access portal and is prevented from signing back in to start a new application or IAM role session.
The user will lose access to existing application sessions within 30 minutes. Any existing IAM
role sessions will continue based on the session duration configured in the IAM Identity Center permission set.
The maximum session duration can be 12 hours.

## What happens to user access when you end a session

This reference provides detailed information about how IAM Identity Center sessions behave when
administrative actions are taken. The tables in this section show the duration and
effects of user management actions and permission changes on access to the AWS access portal,
applications, and AWS account sessions.

### User management

This table summarizes how user management changes affect access to AWS resources,
application sessions, and AWS account sessions.

| Action                 | User loses IAM Identity Center access    | User can't create new application sessions | User can't access existing application sessions | User loses access to existing AWS account sessions                                                                  |
| ---------------------- | ---------------------------------------- | ------------------------------------------ | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| User's access disabled | Effective immediately                    | Effective immediately                      | Within 30 minutes                               | Within 12 hours or less. Duration depends on IAM role session<br>expiry duration configured for the permission set. |
| User deleted           | Effective immediately                    | Effective immediately                      | Within 30 minutes                               | Within 12 hours or less. Duration depends on IAM role session<br>expiry duration configured for the permission set. |
| User session revoked   | User must sign in again to regain access | Effective immediately                      | Within 30 minutes                               | Within 12 hours or less. Duration depends on IAM role session<br>expiry duration configured for the permission set. |
| User signs out         | User must sign in again to regain access | Effective immediately                      | Within 30 minutes                               | Within 12 hours or less. Duration depends on IAM role session<br>expiry duration configured for the permission set. |

### Group membership

This table summarizes how changes to user permissions and group memberships affect access to AWS resources, application sessions,
and AWS account sessions.

| Action                                                                     | User loses IAM Identity Center access                   | User can't create new application sessions | User can't access existing application sessions | User loses access to existing AWS account sessions                                                                  |
| -------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Application or AWS account access removed from user                        | No<br>• User can continue accessing IAM Identity Center | Effective immediately                      | Within 1 hour                                   | Within 12 hours or less. Duration depends on IAM role session<br>expiry duration configured for the permission set. |
| User removed from group that had an assigned application or<br>AWS account | No<br>• User can continue accessing IAM Identity Center | Within 1 hour                              | Within 2 hours                                  | Within 12 hours or less. Duration depends on IAM role session<br>expiry duration configured for the permission set. |
| Application or AWS account access removed from group                       | No<br>• User can continue accessing IAM Identity Center | Effective immediately                      | Within 1 hour                                   | Within 12 hours or less. Duration depends on IAM role session<br>expiry duration configured for the permission set. |

###### Note

The AWS access portal and AWS CLI will reflect updated user permissions within 1 hour after you add or remove a user from that group.

###### Understanding timing differences

- Effective immediately – Actions that require immediate re-authentication.
- Within 30 minutes - 2 hours – Application sessions need time to check with IAM Identity Center and discover any changes.
- Within 12 hours or less – IAM role sessions operate independently and only end when their configured duration expires.

## Single logout

IAM Identity Center doesn't support SAML Single Logout (a protocol that automatically signs users
out of all connected applications when they sign out of one) initiated by an identity
provider that acts as your [identity
source](manage-your-identity-source.md "manage-your-identity-source.md"). Additionally, it doesn't send SAML Single Logout to [SAML 2.0 applications](customermanagedapps-saml2-oauth2.md "customermanagedapps-saml2-oauth2.md") that use
IAM Identity Center as an identity provider.

## Best practices for session management

Effective session management requires thoughtful configuration and monitoring.
Organizations should configure session durations appropriate to their security
requirements, generally using shorter durations for sensitive applications and
environments.

Implementing processes to end sessions when users change roles or leave the
organization is essential for maintaining security boundaries. Regular review of
active sessions should be incorporated into security monitoring practices to detect
anomalous behavior that might indicate security issues, such as unusual access
patterns, unexpected login times or locations, or access to resources outside normal
job functions.
