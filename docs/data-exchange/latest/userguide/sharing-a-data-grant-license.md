# Sharing an AWS Data Exchange data grant license in an

organization

When you accept a data grant, you receive a license that allows you to share the underlying data set under the following conditions:

- The data grant sender allows you to share the underlying data set.
- Your AWS account belongs to an organization. For more information about AWS Organizations, see the [AWS Organizations
  User Guide](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

###### Note

You can only share access with accounts in your organization.

The following topics explain how to share licenses across accounts.

###### Topics

- [Prerequisites for license sharing](#data-grant-prerequisites-license-sharing "#data-grant-prerequisites-license-sharing")
- [Viewing your licenses](data-grant-viewing-licenses.md "data-grant-viewing-licenses.md")
- [Sharing your licenses](data-grant-sharing-license.md "data-grant-sharing-license.md")

## Prerequisites for license sharing

Before you can share licenses, you must complete the following setup tasks:

- In the AWS Data Exchange console, use the **Data Grant settings** page to enable integration with AWS Organizations.
- Give AWS Data Exchange permission to read information about accounts in your organization and manage licenses on your behalf so that
  it can create the associated license grants when you share your licenses. For more information, see
  [Using service-linked roles for
  AWS Data Exchange](using-service-linked-roles-adx.md "using-service-linked-roles-adx.md"), in this guide.
