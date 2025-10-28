# Private marketplaces for administrators

To create and manage a private marketplace, you must be signed into the management account
or the delegated administrator account for private marketplace. You must also have the AWS Identity and Access Management
(IAM) permissions in the AWSPrivateMarketplaceAdminFullAccess IAM policy. For
more information about applying this policy to users, groups, and roles, see [Creating a private marketplace administrator](it-administrator.md "it-administrator.md").

###### Note

If you're a current private marketplace customer without the AWS Organizations integration for
private marketplace, you can create and manage a private marketplace from any account in your
organization that has the AWSPrivateMarketplaceAdminFullAccess IAM
policy.

This section includes tasks that you can complete as a private marketplace administrator
through the AWS Marketplace website. You can also manage private marketplaces using the AWS Marketplace Catalog API. For
more information, see [Working with a private
marketplace](../../../marketplace-catalog/latest/api-reference/private-marketplace.md "../../../marketplace-catalog/latest/api-reference/private-marketplace.md") in the _AWS Marketplace Catalog API Reference_.

## Getting started with private

marketplace

To get started with private marketplace, ensure you're signed into your AWS management
account, navigate to [Private
Marketplace](https://aws.amazon.com/marketplace/pmp/getstarted "https://aws.amazon.com/marketplace/pmp/getstarted"), and then enable the following prerequisites:

- **Trusted access** – You must enable trusted
  access for AWS Organizations, which allows the management account of an organization to provide or
  revoke access for their AWS Organizations data for an AWS service. Enabling trusted access is
  critical for private marketplace to integrate with AWS Organizations and designate private
  marketplace as a trusted service in your organization.
- **Service-linked role** – You must enable the
  private marketplace service-linked role, which resides in the management account and
  includes all the permissions that private marketplace requires to describe AWS Organizations and
  update private marketplace resources on your behalf. For more information on the
  service-linked role, see [Using roles to configure Private Marketplace in AWS Marketplace](using-service-linked-roles-private-marketplace.md "using-service-linked-roles-private-marketplace.md").

###### Note

Current private marketplace customers can enable settings for your private marketplace
by navigating to the **Private Marketplace** administrator's page and
choosing **Settings**. By enabling trusted access for AWS Organizations and creating
a service-linked role, you can utilize features, such as associating OUs to private
marketplace experiences and registering a delegated administrator. When enabled, only the
management account and delegated administrator account can create and manage marketplace
experiences, with existing resources transferred to the management account and shared only
with the delegated administrator. Disabling trusted access will remove private marketplace
governance for your organization. There are no account groups displayed in your private
marketplace. To view your organization’s governance at different levels, use the
**Organization structure** page. For questions or support, [contact us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").
