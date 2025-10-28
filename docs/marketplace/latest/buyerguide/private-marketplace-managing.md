# Managing a private marketplace

You can manage your private marketplace from the **Private Marketplace**
administrator's page under **Settings** in the left pane. The management
account administrator and delegated administrators can use this page to view private
marketplace details, including the default private marketplace and number of live
experiences.

Management account administrators can also use this page to manage the following
settings.

## Delegated administrators

The management account administrator can delegate private marketplace administrative
permissions to a designated member account known as delegated administrator. To register an
account as a delegated administrator for the private marketplace, the management account
administrator must ensure trusted access and the service-linked role are enabled, choose
**Register a new administrator**, provide the 12-digit AWS
account number, and choose **Submit**.

Management accounts and delegated administrator accounts can perform private marketplace
administrative tasks, such as creating experiences, updating branding settings, associating or
disassociating audiences, adding or removing products, and approving or declining pending
requests.

## Trusted access and service-linked role

The management account administrator can enable the following features for your private
marketplace.

###### Note

Current private marketplace customers can enable settings for your private marketplace
by navigating to the **Private Marketplace** administrator's page and
choosing **Settings**. By enabling trusted access for AWS Organizations and
creating a service-linked role, you can utilize features, such as associating OUs to
private marketplace experiences and registering a delegated administrator. When enabled,
only the management account and delegated administrator account can create and manage
marketplace experiences, with existing resources transferred to the management account and
shared only with the delegated administrator. Disabling trusted access will remove private
marketplace governance for your organization. There are no account groups displayed in
your private marketplace. To view your organization’s governance at different levels, use
the **Organization structure** page. For questions or support, [contact us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

- **Trusted access** – You must enable trusted
  access for AWS Organizations, which allows the management account of an organization to provide
  or revoke access for their AWS Organizations data for an AWS service. Enabling trusted access
  is critical for private marketplace to integrate with AWS Organizations and designate private
  marketplace as a trusted service in your organization.
- **Service-linked role** – You must enable the
  private marketplace service-linked role, which resides in the management account and
  includes all the permissions that private marketplace requires to describe AWS Organizations and
  update private marketplace resources on your behalf. For more information on the
  service-linked role, see [Using roles to configure Private Marketplace in AWS Marketplace](using-service-linked-roles-private-marketplace.md "using-service-linked-roles-private-marketplace.md").
