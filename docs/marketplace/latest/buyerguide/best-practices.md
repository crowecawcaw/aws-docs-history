# Best practices

## Create a default experience

It is recommended to configure a default governing experience to govern your entire
organization. This experience should be associated with your organization root as the
audience and curated with products that you approve for all your users. This ensures that
any organizational unit (OU) or account that does not have a directly associated
experience will automatically fall under the governance of this default experience.

## Register a delegated administrator

The management account administrator can register a trusted member account to act as a
delegated administrator for Private Marketplace. This reduces the operational burden on management
account administrator by allowing the delegated administrator account to create and manage
Private Marketplace experiences in your organization. It also minimizes the need to use the management
account for security reasons.

## Leverage organizational units

When you build your organization hierarchy, structure your OUs to align with your
procurement needs. With this, you can apply specific procurement controls by creating and
associating experiences with OUs. This reduces the maintenance overhead allowing you to
seamlessly reuse your structure from AWS Organizations. When you make updates to the hierarchy in
AWS Organizations, the changes are automatically synchronized and the governance is updated in
Private Marketplace.

## Customize governance of individual accounts

If you have individual accounts with specific procurement needs that do not align with
the overarching organization or OU experience, you can create and customize an experience
and associate it with the individual account. This provides flexibility and allows you to
tailor governance based on specific account requirements.

## Audit experiences regularly

Conduct regular audits of experiences, their associated audiences, and the list of
approved products to prevent outdated products from lingering in the approved list.
Periodic reviews help maintain the relevance and security of the Private Marketplace setup.

## Monitor all administration actions

Track all Private Marketplace management actions through the **Change sets** page.
You can also use AWS CloudTrail. For more information, see [Viewing changes](view-changes.md "view-changes.md").

## Manage your approved product list

Ensure that all AWS Marketplace products currently in use across your organization are included
in your Private Marketplace experiences. Though Private Marketplace does not disrupt existing subscriptions, any changes
to the subscription or new subscriptions will be allowed only if the product is approved
in the user's experience. It's also recommended to have a plan in place to discontinue use
of unapproved products before turning on Private Marketplace governance.

## Archive experiences that you no longer need

If you create multiple experiences for testing, it is recommended to archive them.
This ensures a streamlined list of experiences that allows better oversight.

## Integrate with AWS Organizations

If you have been using Private Marketplace without Organizations integration or using it to govern individual
accounts that are not in Organizations, you will not be able to use the new features launched since
February 16, 2024. To use the latest features, an administrator in the management account
of your AWS Organizations must create an integration for Private Marketplace. This is a prerequisite to use the
AWS Marketplace console for managing Private Marketplace. The website for managing Private Marketplace will be deprecated on
November 15, 2025. The integration is also required to use the features for organizational
unit (OU) support and user request notifications discussed in the following What’s New posts:

- [AWS Marketplace now supports managing Private Marketplace catalogs for organizational units](https://aws.amazon.com/about-aws/whats-new/2024/02/aws-marketplace-private-marketplace-catalogs-organizational-units/ "https://aws.amazon.com/about-aws/whats-new/2024/02/aws-marketplace-private-marketplace-catalogs-organizational-units/")
- [AWS Marketplace now supports notifications for Private Marketplace](https://aws.amazon.com/about-aws/whats-new/2024/10/aws-marketplace-notifications-private-marketplace/ "https://aws.amazon.com/about-aws/whats-new/2024/10/aws-marketplace-notifications-private-marketplace/")
