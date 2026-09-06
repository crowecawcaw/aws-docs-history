

# Managing users in Deadline Cloud
<a name="managing-users"></a>

AWS Deadline Cloud uses AWS IAM Identity Center to manage users and groups. IAM Identity Center is a cloud-based single sign-on service that can be integrated with your enterprise single-sign on (SSO) provider. With integration, users can sign in with their company account.

Deadline Cloud enables IAM Identity Center by default, and signing in to the Deadline Cloud monitor requires it. You can also use Deadline Cloud without IAM Identity Center by calling the API or CLI with IAM credentials; see [How permissions work in Deadline Cloud](permissions-overview.md). An organization owner for your AWS Organizations is responsible for managing the users and groups that have access to your Deadline Cloud monitor. For more information, see [What is AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).

Where you create and manage users depends on your IAM Identity Center identity source: with the default IAM Identity Center directory, you create users in the Deadline Cloud console, and with an external identity provider such as Okta or Microsoft Entra ID, you create them in that system. For more information, see [Understanding your identity source](understanding-identity-source.md).

To bring a new artist, team, or vendor onto your farm, start with [Onboard users to your farm](onboarding.md).

**Topics**
+ [How permissions work in Deadline Cloud](permissions-overview.md)
+ [Onboard users to your farm](onboarding.md)
+ [Understanding your identity source](understanding-identity-source.md)
+ [Create and manage users with IAM Identity Center directory](manage-monitor-users_users.md)
+ [Manage users with an external identity provider](manage-users-external-idp.md)
+ [Restricting which users can access the monitor](restrict-user-management-visibility.md)
+ [Assign permissions to users and groups](assign-permissions-procedure.md)