AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# (Optional) Setting up OpsCenter

to centrally manage OpsItems across accounts

You can use Systems Manager OpsCenter to centrally manage OpsItems across multiple
AWS accounts in a selected AWS Region. This feature is available after you set
up your organization in AWS Organizations. AWS Organizations is an account management service that
enables you to consolidate multiple AWS accounts into an organization that you
create and centrally manage. AWS Organizations includes account management and consolidated
billing capabilities that enable you to better meet the budgetary, security, and
compliance needs of your business. For more information, see [What is AWS Organizations?](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") in the _AWS Organizations User Guide_

Users who belong to the AWS Organizations management account can set up a delegated
administrator account for Systems Manager. In the context of OpsCenter, delegated
administrators can create, edit, and view OpsItems in member accounts. The delegated
administrator can also use Systems Manager Automation runbooks to bulk resolve OpsItems or
remediate issues with AWS resources that are generating OpsItems.

###### Note

You can assign only one account as the delegated administrator for Systems Manager. For
more information, see [Creating an AWS Organizations delegated administrator
for Systems Manager](setting_up_delegated_admin.md "setting_up_delegated_admin.md").

Systems Manager offers the following methods for setting up OpsCenter to centrally manage
OpsItems across multiple AWS accounts.

- **Quick Setup**: Quick Setup, a tool in
  Systems Manager, simplifies set up and configuration tasks for Systems Manager tools. For more
  information, see [AWS Systems Manager Quick Setup](systems-manager-quick-setup.md "systems-manager-quick-setup.md").

Quick Setup for OpsCenter helps you complete the following tasks for
managing OpsItems across accounts:

    + Registering an account as the delegated administrator (if the
     delegated administrator hasn't already been designated)
    + Creating required AWS Identity and Access Management (IAM) policies and roles
    + Specifying an AWS Organizations organization or organizational units (OUs)
     where a delegated administrator can manage OpsItems across
     accounts

For more information, see [(Optional) Configure
OpsCenter to manage OpsItems across accounts by using Quick Setup](OpsCenter-quick-setup-cross-account.md "OpsCenter-quick-setup-cross-account.md").

###### Note

Quick Setup isn't available in all AWS Regions where Systems Manager is
currently available. If Quick Setup isn't available in a Region where
you want to use it to configure OpsCenter to centrally manage OpsItems
across multiple accounts, then you must use the manual method. To view a
list of AWS Regions where Quick Setup is available, see [Availability of Quick Setup in
AWS Regions](systems-manager-quick-setup.md#quick-setup-getting-started-regions "systems-manager-quick-setup.md#quick-setup-getting-started-regions").

- **Manual set up**: If Quick Setup isn't
  available in the Region where you want to configure OpsCenter to centrally
  manage OpsItems across accounts, then you can use the manual procedure to do
  so. For more information, see [(Optional)
  Manually set up OpsCenter to centrally manage OpsItems across accounts](OpsCenter-getting-started-multiple-accounts.md "OpsCenter-getting-started-multiple-accounts.md").
