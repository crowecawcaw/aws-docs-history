# Delegated administration

When you enable account access manager, AWS creates it in the management account in AWS Organizations because
account access manager manages IAM role assignments for an entire AWS Organization. You can choose to delegate
administration of account access manager to a member account in AWS Organizations.

If you choose to register a member account as a delegated administrator for account access manager,
users in this account can perform most account access manager administrative tasks. The following table indicates
whether an account access manager administrative task can be performed by users in an organization management
account, a delegated administration member account, or another member account. IAM role
management is excluded from the list of administrative tasks because it takes place outside of
account access manager.

| Account access manager administrative tasks                          | Management account | Delegated administrator account | Member account |
| -------------------------------------------------------------------- | ------------------ | ------------------------------- | -------------- |
| Manage IAM role assignments\*                                        | Yes                | Yes                             | No             |
| Enable account access manager                                        | Yes                | No                              | No             |
| Delete account access manager                                        | Yes                | No                              | No             |
| Enable or disable user access in the management account              | Yes                | No                              | No             |
| Enable or disable user access in a member account                    | Yes                | Yes                             | No             |
| Register or deregister a member account as a delegated administrator | Yes                | No                              | No             |

\*Refer to the best practices for delegated administration regarding user and group
assignments to the management account.

## Register a member account

To configure delegated administration, you must first register a member account in your
organization as a delegated administrator. Users in that member account who have sufficient
permissions will have administrative access to account access manager.

Account access manager supports registering only one member account as a delegated administrator at a
time. You can only register a member account while signed in with credentials from the
management account.

Use the following procedure to register a member account in your AWS organization as a
delegated administrator.

###### To register a member account

1. Sign in to the AWS Management Console using the credentials of your management account in AWS Organizations.
   Management account credentials are required to run the [RegisterDelegatedAdministrator](../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md") API.
2. Select the Region where account access manager was enabled and then open the AWS Identity and Access Management console.
3. Choose **Account access manager**, and then choose the
   **Settings** tab.
4. In the **Delegated administrator** section, choose
   **Register**.
5. On the **Register delegated administrator** page, select
   the AWS account you want to register, and then choose **Register**.

## Deregister a member account

You can only deregister a member account while signed in with credentials from the
management account.

Use the following procedure to deregister a member account in your AWS organization
that had previously been designated as a delegated administrator.

###### Important

When you deregister an account, you remove the ability for all admin users to manage
account access manager from that account. They can no longer administer AWS account access from this
account.

This operation does not affect permissions or assignments configured in account access manager. Your
end users continue to access their AWS accounts from the account access portal.

###### To deregister a member account

1. Sign in to the AWS Management Console using the credentials of your management account in AWS Organizations.
   Management account credentials are required to run the [DeregisterDelegatedAdministrator](../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md") API.
2. Select the Region where account access manager was enabled, and then open the AWS Identity and Access Management console.
3. Choose **Account access manager**, and then choose the
   **Settings** tab.
4. In the **Delegated administrator** section, choose
   **Deregister account**.
5. In the **Deregister delegated administrator** dialog box,
   review the security implications, and then confirm that you understand.
6. Choose **Deregister**.

## View the registered delegated administrator account

Use the following procedure to find which member account in your AWS Organizations has been
configured as the delegated administrator for account access manager.

###### To view your registered member account

1. Sign in to the AWS Management Console using the credentials of your management account in
   AWS Organizations.
2. Select the Region where account access manager was enabled and then open the AWS Identity and Access Management console.
3. Choose **Account access manager**, and then choose the
   **Settings** tab.
4. In the **Delegated administrator** section, you can view
   the current delegated administrator account details.
