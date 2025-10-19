# Deregister a member
 account

You can only deregister a member account while signed in with credentials from the
 management account.

Use the following procedure to remove administrative access from IAM Identity Center by
 deregistering a member account in your AWS organization that had previously been
 designated as a delegated administrator.

###### Important

When you deregister an account, you effectively remove the ability for all
 admin users to manage IAM Identity Center from that account. As a result, they can no longer
 administer IAM Identity Center identities, access management, authentication, or application
 access from this account. This operation will not affect any permissions or
 assignments configured in IAM Identity Center and therefore will have no impact on your end
 users as they will continue to have access to their apps and AWS accounts from
 within the AWS access portal.

###### To deregister a member account

1. Sign in to the AWS Management Console using the credentials of your management account
 in AWS Organizations. Management account credentials are required to run the [DeregisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.html "https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.html") API.
2. Select the Region where IAM Identity Center is enabled, and then open the [IAM Identity Center
 console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
3. Choose **Settings**, and then select the
 **Management** tab.
4. In the **Delegated administrator** section, choose
 **Deregister account**.
5. In the **Deregister account** dialog box, review the
 security implications, and then enter the name of the member account to
 confirm that you understand.
6. Choose **Deregister account**.
