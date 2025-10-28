# Register a member account

To configure delegated administration, you must first register a member account in
your organization as a delegated administrator. Users in that member account who
have sufficient permissions will have administrative access to IAM Identity Center. After a member
account is successfully registered for delegated administration, it is referred to as
the _delegated administrator account_. To learn more about tasks
that the delegated administrator account can perform, see [AWS account types](manage-your-accounts.md#account-types "manage-your-accounts.md#account-types").

IAM Identity Center supports registering only one member account as a delegated administrator at
a time. You can only register a member account while signed in with credentials from
the management account.

Use the following procedure to grant administrative access to IAM Identity Center by registering
a specific member account in your AWS organization as a delegated
administrator.

###### Important

This operation delegates IAM Identity Center administrative access to admin users in this
member account. All users who have sufficient permissions to this delegated
administrator account can perform all IAM Identity Center administrative tasks from the
account, except for:

- Enabling IAM Identity Center
- Deleting IAM Identity Center configurations
- Managing permission sets provisioned in the management account
- Registering or deregistering other member accounts as delegated
  administrators
- Enabling or disabling user access in the management account
  The delegated administrator can edit group membership.

###### To register a member account

1. Sign in to the AWS Management Console using the credentials of your management account
   in AWS Organizations. Management account credentials are required to run the [RegisterDelegatedAdministrator](../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md") API.
2. Select the Region where IAM Identity Center is enabled, and then open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
3. Choose **Settings**, and then select the
   **Management** tab.
4. In the **Delegated administrator** section, choose
   **Register account**.
5. On the **Register delegated administrator** page, select
   the AWS account you want to register, and then choose **Register
   account**.
