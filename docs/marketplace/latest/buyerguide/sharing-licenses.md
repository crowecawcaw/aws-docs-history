# Sharing your licenses

Only AMI, container, machine learning, data products and Oracle Database@AWS
subscriptions have licenses that can be shared.

Subscriptions in AWS Marketplace have an **Access level** shown in the product
details:

- Products with an **Agreement** level have a license that you
  can use and share with other accounts in your organization.
- Products with an **Entitlement** level are licenses that have
  been shared with your account—you can use these products, but you can't
  share them.
  AWS Marketplace supports grants, which share the use of a license directly with AWS Organizations, an
  AWS account, or an organizational unit using AWS License Manager. The grant activation process
  now includes additional options to replace grants that are activated for the same
  product sourced from AWS Marketplace. For more information, see [Granted
  licenses](../../../license-manager/latest/userguide/granted-licenses.md "../../../license-manager/latest/userguide/granted-licenses.md") in the _AWS License Manager User Guide_.

###### Note

For products that are restricted to specific AWS Regions, an account you share
your license with can only activate the license if the account is within an allowed
Region.

## Prerequisites for license sharing

Before you can share licenses in AWS Marketplace you must set up license sharing for your
organization. Complete the following tasks to set up license sharing for your
organization:

- Give AWS Marketplace permission to manage licenses on your behalf so that it can
  create the associated license grants when you purchase or share your
  licenses. For more information, see [Service-linked role to share entitlements for AWS Marketplace](buyer-using-service-linked-roles-license-manager.md "buyer-using-service-linked-roles-license-manager.md").
- Set up AWS License Manager for first use. For more information, see [Getting
  started with AWS License Manager](../../../license-manager/latest/userguide/getting-started.md "../../../license-manager/latest/userguide/getting-started.md") in the _AWS License Manager User
  Guide_.
