# Consolidated billing process

AWS Organizations provides consolidated billing so that you can track the combined costs of all
the member accounts in your organization. The following steps provide an overview of the
process for creating an organization and viewing your consolidated bill.

1. Open the [AWS Organizations console](https://console.aws.amazon.com/organizations/ "https://console.aws.amazon.com/organizations/") or the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing/ "https://console.aws.amazon.com/billing/"). If you open the
   AWS Billing and Cost Management console, choose **Consolidated Billing**, and then
   choose **Get started**. You are redirected to the AWS Organizations
   console.
2. Choose **Create organization** on the AWS Organizations
   console.
3. Create an organization from the account that you want to be the
   management account of your new organization. For details, see [Creating an Organization](../../../organizations/latest/userguide/orgs_manage_create.md "../../../organizations/latest/userguide/orgs_manage_create.md").
   The management account is responsible for paying the charges of all the member
   accounts.
4. (Optional) Create accounts that are automatically member to the organization.
   For details, see [Creating an AWS account in Your Organization](../../../organizations/latest/userguide/orgs_manage_accounts_create.md "../../../organizations/latest/userguide/orgs_manage_accounts_create.md").
5. (Optional) Invite existing accounts to join your organization. For details,
   see [Inviting an
   AWS account to Join Your Organization](../../../organizations/latest/userguide/orgs_manage_accounts_invites.md "../../../organizations/latest/userguide/orgs_manage_accounts_invites.md").
6. Each month AWS charges your management account for all the member accounts in
   a consolidated bill.
   The management account is billed for all charges of the member accounts. However,
   unless the organization is changed to support all features in the organization (not
   consolidated billing features only) and member accounts are explicitly restricted by
   policies, each member account is otherwise independent from the other member accounts.
   For example, the owner of a member account can sign up for AWS services, access
   resources, and use AWS Premium Support unless the management account restricts those
   actions. Each account owner continues to use their own sign-in credentials, with account
   permissions assigned independently of other accounts in the organization.

###### Securing the consolidated billing management account

The owner of the management account in an organization should secure the account by
using [AWS Multi-Factor Authentication](https://aws.amazon.com/mfa/ "https://aws.amazon.com/mfa/")
and a strong password that has a minimum of eight characters with both uppercase and
lowercase letters, at least one digit, and at least one special character. You can
change your password on the [AWS
Security Credentials](https://aws.amazon.com/security-credentials "https://aws.amazon.com/security-credentials") page.

###### Note

You can use billing transfer to maintain root access to your management account while transferring billing to another management account outside your AWS Organizations. For more information, see [Transfer billing management to external accounts](orgs_transfer_billing.md "orgs_transfer_billing.md").
