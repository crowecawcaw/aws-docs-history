# Viewing Private Marketplace settings

To use all features in Private Marketplace, an administrator in the management account of your AWS Organizations must create an integration for Private Marketplace. This is a prerequisite to use the AWS Marketplace console for managing Private Marketplace. The integration is also required to use the organizational unit (OU) support and user request notification features discussed in the following What’s New posts:

- [AWS Marketplace now supports managing Private Marketplace catalogs for organizational units](https://aws.amazon.com/about-aws/whats-new/2024/02/aws-marketplace-private-marketplace-catalogs-organizational-units/ "https://aws.amazon.com/about-aws/whats-new/2024/02/aws-marketplace-private-marketplace-catalogs-organizational-units/")
- [AWS Marketplace now supports notifications for Private Marketplace](https://aws.amazon.com/about-aws/whats-new/2024/10/aws-marketplace-notifications-private-marketplace/ "https://aws.amazon.com/about-aws/whats-new/2024/10/aws-marketplace-notifications-private-marketplace/")

###### To view integration status

###### Note

You must use the management account of your organization with a role or user that has the `AWSPrivateMarketplaceAdminFullAccess` managed policy. Attempting to view the integration status from a non-management account or with insufficient permissions will result in a "Status cannot be determined" message.

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
2. In the navigation pane, choose **Settings**.
3. Check the values for **Service-linked role** and **Trusted access**:
   - If they show **Successfully created**, your organization has created an integration for Private Marketplace.
   - If they show **Not created**, your organization has not created an integration for Private Marketplace.
