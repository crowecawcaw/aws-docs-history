# Controlling access to Cost Explorer

You can manage access to your Cost Explorer in the following ways:

- Using the management account, you can enable Cost Explorer as a root user, automatically
  enabling all member accounts.
- After member accounts are enabled, you can change Cost Explorer settings from within the
  management account. You can control the information that can be accessed in
  Cost Explorer. This includes costs, refunds or credits, discounts, and Reserved
  Instance (RI) recommendations.
- After you enable Cost Explorer at the management account level, you can manage user IAM
  policies. For example, you can grant users full access or deny users access to
  Cost Explorer.
  This topic provides information about how to control access in Cost Explorer.

For information about managing access to Billing and Cost Management pages, see [Overview of managing access permissions](control-access-billing.md "control-access-billing.md").

To reference Cost Explorer IAM policies, see [Using identity-based policies (IAM policies) for AWS Cost Management](billing-permissions-ref.md "billing-permissions-ref.md").

For more information about consolidated
billing, see [Consolidated billing for AWS Organizations](../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md "../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md").

###### Topics

- [Granting Cost Explorer access](#grant-ce-access "#grant-ce-access")
- [Controlling access using Cost Explorer
  preferences](#ce-controlling-access "#ce-controlling-access")
- [Managing Cost Explorer access for users](#ce-iam-users "#ce-iam-users")

## Granting Cost Explorer access

If you're signed into the management account with your root account credentials, you can
enable Cost Explorer access. Your root account credentials are through the Billing and Cost Management
console. Enabling Cost Explorer at the management account level enables Cost Explorer
for all of your organization accounts. All accounts in the organization are granted
access, and you can't grant or deny access individually.

## Controlling access using Cost Explorer

preferences

A management account can grant access to Cost Explorer for all or none of the member
accounts. Access isn’t customizable for each individual member account.

The management account in AWS Organizations has full access to all Billing and Cost Management information for costs
incurred by both the management account and member accounts. Member accounts only have
access to their own cost and usage data in Cost Explorer.

By default, the management account in AWS Organizations sees all costs at the chargeable rate.
If an organization is onboarded to Billing Conductor, the management account also sees costs at the
proforma rate. The Cost Explorer view for member accounts depends on the configuration
in Billing Conductor.

The owner of a management account can do the following:

- View all costs in Cost Explorer.
- Grant all member accounts the permission to see the costs for their own member
  account, refunds, credits, and RI recommendations.

Member account owners can't see costs, refunds, and RI recommendations for other
accounts in the Organizations. For more information about consolidated billing, see [Consolidated
billing for AWS Organizations](../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md "../../../awsaccountbilling/latest/aboutv2/consolidated-billing.md").

If you're an AWS account owner and not using consolidated billing, you have full
access to all Billing and Cost Management information including Cost Explorer.

If you're onboarded to Billing Conductor, the Cost Explorer view for member accounts depends on
whether a member account is part of a billing group.

If a member account is part of a billing group:

- The member account sees all costs at the proforma rate.
- Cost Explorer preferences, such as **Linked Account
  Access**, **Linked Account Refunds and Credits**,
  **Linked Account Discounts**, **Hourly and Resource
  Level Data**, and **Split cost allocation data**
  are not applicable to the member account.

If a member account is not part of a billing group:

- The member account see costs at the chargeable rate.
- Cost Explorer preferences apply to the member account.

For more information about Billing Conductor, see the [Billing Conductor User
Guide](../../../billingconductor/latest/userguide/what-is-billingconductor.md "../../../billingconductor/latest/userguide/what-is-billingconductor.md").

### Organizations account status use cases

An account’s status within an organization determines what cost and usage data are
visible in the following ways:

- A standalone account joins an organization. After this, the account can no
  longer access cost and usage data from when the account was a standalone
  account.
- A member account leaves an organization to become a standalone account.
  After this, the account can no longer access cost and usage data from when
  the account was a member of their previous organization. The account can
  only access the data that's generated as a standalone account.
- A member account leaves organization A to join organization B. After this,
  the account can no longer access cost and usage data from organization A.
  The account can access only the data that's generated as a member of
  organization B.
- An account rejoins an organization that it previously belonged to. After
  this, the account regains access to its historical cost and usage
  data.

### Controlling member accounts’ access

using Cost Explorer preferences

You can grant or restrict the access to all member accounts in your Organizations. When you
enable your account at the management account level, all member accounts are granted
access to their cost and usage data by default.

###### To control member account access to

Cost Explorer data

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Management Preferences**.
3. On the **Preferences** page, under **Member account
   permissions** in the **General** tab, select
   or clear **Linked account access**.
4. Choose **Save preferences**.

## Managing Cost Explorer access for users

After you enable Cost Explorer at the management account level, you can use IAM to manage
access to your billing data for individual users. This way, you can grant or revoke
access on an individual level for each account, rather than granting access to all
member accounts.

A user must be granted explicit permissions to view pages in the Billing and Cost Management console. With the
appropriate permissions, the user can view costs for the AWS account that the user
belongs to. For the policy that grants the necessary permissions to a user, see [Overview of managing access permissions](control-access-billing.md "control-access-billing.md").
