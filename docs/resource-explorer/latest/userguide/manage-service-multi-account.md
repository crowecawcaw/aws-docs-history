# Turning on multi-account search

With multi-account search, you can search for resources across accounts with active
indexes in your AWS Organizations or organizational unit (OU).

###### Topics

- [Prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Enable multi-account search](#enable-multi-account-search "#enable-multi-account-search")
- [Multi-account Quick Setup](#getting-started-quick-setup "#getting-started-quick-setup")
- [Effect of account actions on Resource Explorer
  multi-account search](manage-service-account-actions.md "manage-service-account-actions.md")

## Prerequisites

To turn on multi-account search for your organization, complete the following:

- For [opt-in
  Regions](opt-in-region-considerations.md "opt-in-region-considerations.md"), verify your management account is also opted-in where you
  are turning on multi-account search.
- [Create an administrative user.](getting-started-setting-up-prereqs.md#create-an-admin "getting-started-setting-up-prereqs.md#create-an-admin")
- [Create a
  service-linked role in the administrator account](security_iam_service-linked-roles.md "security_iam_service-linked-roles.md") with `aws iam
create-service-linked-role --aws-service-name
resource-explorer-2.amazonaws.com`.
- [Enable
  trusted access in AWS Organizations](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md"). This allows full integration with Resource Explorer
  to list resources across all accounts in your organization.
- Assign a delegated administrator (_recommended_). For more
  information, see [Delegated administrator for AWS services that work with
  Organizations](../../../organizations/latest/userguide/orgs_integrate_delegated_admin.md "../../../organizations/latest/userguide/orgs_integrate_delegated_admin.md") in the _AWS Organizations User
  Guide_.
  - Resource Explorer supports only 1 delegated administrator who performs similar
    actions to the management account.
  - Removing or changing the delegated administrator for your organization
    results in the removal of all multi-account views created in their
    account.

## Enable multi-account search

To search and discover resources across your organization's accounts, you must
complete the following steps:

1. [Activate AWS Resource Explorer
   in one or more accounts in your AWS Organizations.](getting-started-setting-up.md "getting-started-setting-up.md")
2. [Register one Region to
   contain the aggregator index.](manage-aggregator-region.md "manage-aggregator-region.md")
3. [Choose
   a Region in which to create an aggregator index. This Region must be
   consistent across your AWS Organizations.](configure-views.md "configure-views.md")
4. [Create a Resource Explorer view that's scoped to your AWS Organizations or organizational unit.
   Create this view in the aggregator Region from the preceding
   step.](configure-views-create.md "configure-views-create.md")
5. [Share the view with accounts across your organization.](configure-views-share.md "configure-views-share.md")

## Multi-account Quick Setup

Enable Resource Explorer across multiple accounts in your organization with the Quick
Setup.

###### Note

This process does not deploy any resources in the management account. If you are
using the management account and you want indexes in the account, you must manually
add them with the Resource Explorer onboarding flow.

1. Navigate to [Quick Setup](https://console.aws.amazon.com/systems-manager/quick-setup/create-configuration?configurationType=AWSQuickSetupType-ResourceExplorer "https://console.aws.amazon.com/systems-manager/quick-setup/create-configuration?configurationType=AWSQuickSetupType-ResourceExplorer") for Resource Explorer in the Systems Manager console.
2. Choose your **Aggregator index Region**. This allows you to
   search for resources located in all Regions in the selected target accounts. If
   any of the selected target accounts already have an aggregator index configured
   in another Region, the existing aggregator index will be automatically replaced
   with this new Region.
3. Choose your account **Targets**. You can enable Resource Explorer for
   your entire organization or for specific organizational units (OUs).

###### Note

You can deploy to a maximum of 50,000 AWS CloudFormation stacks at a time. If you
have a large organization that spans multiple Regions, you
should deploy at the OU level in smaller batches. 4. Read through the summary of acknowledgements before you choose
**Create**.
