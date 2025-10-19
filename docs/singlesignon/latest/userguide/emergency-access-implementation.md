# Summary of emergency access configuration

To configure emergency access, you must complete the following tasks:


1. [Create an emergency operations account in your organization in
 AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html"). This account will become your emergency operations account.
2. Connect your IdP to the emergency operations account by using [SAML 2.0-based federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html").
3. In the emergency operations account, [create a role for third-party identity provider federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html"). Also, create an
 emergency operations role in each of your workload accounts, with your required
 permissions.
4. [Delegate access to your workload accounts for the IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html") that you created
 in the emergency operations account. To authorize access to your
 emergency
 operations account, create an emergency operations group in your IdP,
 with no members.
5. Enable the emergency operations group in your IdP to use the emergency operations role by
 creating a rule in your IdP that [enables SAML 2.0 federated access to the AWS Management Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html").
During normal operations, no one has access to the emergency operations account
 because the emergency operations group in your IdP has no members. In the event of an IAM Identity Center
 disruption, use your IdP to add trusted users to the emergency operations group in your IdP.
 These users can then sign in to your IdP, navigate to the AWS Management Console, and assume the
 emergency operations role in the emergency operations account. From there, these users can
 [switch roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html") to the emergency access role in your workload accounts where they
 need to perform operations work.
