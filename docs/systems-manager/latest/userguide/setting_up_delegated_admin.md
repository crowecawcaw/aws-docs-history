AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Creating an AWS Organizations delegated administrator

for Systems Manager

###### Change Manager availability change

AWS Systems Manager Change Manager will no longer be open to new customers
starting November 7, 2025. If you would like to use Change Manager, sign up prior to that
date. Existing customers can continue to use the service as normal. For more
information, see [AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

When you set up an organization in AWS Organizations, you assign a management account to perform all
administrative tasks for all AWS services. The management account user can assign a
_delegated administrator account_ only for Systems Manager to perform
administrative tasks for Change Manager, Explorer, and OpsCenter. AWS Organizations is an account
management service that you can use to create an organization and assign AWS accounts to
manage these accounts centrally. For information about AWS Organizations, see [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") in the _AWS Organizations User Guide_.

Change Manager, Explorer, and OpsCenter, tools in AWS Systems Manager, work with AWS Organizations to perform tasks
on all member accounts of your organization. You can assign only one delegated administrator
for all Systems Manager tools. The delegated administrator account must be a member of the organization to which it's
assigned.

###### Topics

- [Using a delegated
  administrator with Change Manager](#setting_up_delegated_administrator_change_manager "#setting_up_delegated_administrator_change_manager")
- [Using a delegated
  administrator with Explorer](#setting_up_delegated_administrator_explorer "#setting_up_delegated_administrator_explorer")
- [Using a delegated
  administrator with OpsCenter](#setting_up_delegated_administrator_opscenter "#setting_up_delegated_administrator_opscenter")
- [Using a delegated
  administrator with Quick Setup](#setting_up_delegated_administrator_quick_setup "#setting_up_delegated_administrator_quick_setup")

## Using a delegated

administrator with Change Manager

Change Manager is an enterprise change management framework for requesting, approving,
implementing, and reporting on operational changes to your application configuration and
infrastructure.

If you use Change Manager across an organization, assign a delegated administrator account to manage change
templates, approvals, and reporting for all member accounts. Using Quick Setup, you can set
up Change Manager to use with an organization and select the delegated administrator account. If you use
Change Manager with a single AWS account, the delegated administrator account isn't required.

By default, Change Manager displays all change-related tasks in the delegated administrator account. For
instructions on configuring a delegated administrator while setting up Change Manager for an
organization, see [Setting up Change Manager for an
organization (management account)](change-manager-organization-setup.md "change-manager-organization-setup.md").

###### Important

If you use Change Manager across an organization, we recommend always making changes from the
delegated administrator account. Although you can make changes from other accounts in the organization,
those changes won't be reported in or viewable from the delegated administrator account.

## Using a delegated

administrator with Explorer

Explorer is a customizable operations dashboard that reports aggregated view of
operations data (OpsData) for your AWS accounts, across AWS Regions.

You can configure a delegated administrator account for Systems Manager to aggregate Explorer data from
multiple Regions and accounts by using resource data sync with AWS Organizations. A delegated
administrator can search, filter, and aggregate Explorer data using the AWS Management Console, the
AWS Command Line Interface (AWS CLI), or AWS Tools for Windows PowerShell.

When you use a delegated administrator account for Explorer, you limit the number of administrators
who can create or delete multi-account and Region resource data syncs to an individual
AWS account.

You can synchronize operations data across all AWS accounts in your organization by
using Explorer. For information on how to assign a delegated administrator from
Explorer, see [Configuring a delegated
administrator for Explorer](Explorer-setup-delegated-administrator.md "Explorer-setup-delegated-administrator.md").

## Using a delegated

administrator with OpsCenter

OpsCenter provides a central location where operations engineers and IT professionals
can manage operational work items (OpsItems) related to AWS resources. If you want to use
OpsCenter to manage OpsItems centrally across accounts, you must set up the organization in
AWS Organizations.

Using Quick Setup for OpsCenter, you can assign a delegated administrator account and configure OpsCenter
to manage OpsItems centrally. For more information, see [(Optional) Configure
OpsCenter to manage OpsItems across accounts by using Quick Setup](OpsCenter-quick-setup-cross-account.md "OpsCenter-quick-setup-cross-account.md").

## Using a delegated

administrator with Quick Setup

Quick Setup is a tool in Systems Manager that helps you to quickly configure frequently used AWS
services and features with recommended best practices. You can configure a delegated
administrator account for Quick Setup to help you deploy and manage configurations across
accounts and Regions using AWS Organizations. A delegated administrator for Quick Setup can create,
update, view, and delete configuration manager resources in your organization. Systems Manager
registers a delegated administrator for Quick Setup as part of the setup process for the
integrated console experience. For more information, see [Setting up Systems Manager unified console
for an organization](systems-manager-setting-up-organizations.md "systems-manager-setting-up-organizations.md").
