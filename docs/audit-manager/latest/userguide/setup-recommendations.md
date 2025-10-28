# Enabling the recommended features and

AWS services for AWS Audit Manager

Now that you have enabled AWS Audit Manager, it's time to set up the recommended features and
integrations to get the most out of the service.

## Key points

For an optimal experience in Audit Manager, we recommend that you set up the following
features and enable the following AWS services.

###### Tasks

- [Set up recommended Audit Manager
  features](#setup-recommendations-features "#setup-recommendations-features")
- [Set up recommended integrations
  with other AWS services](#setup-recommendations-services "#setup-recommendations-services")
  - [Enable and set up AWS Config](#config-recommendations "#config-recommendations")
  - [Enable and set up AWS Security Hub](#securityhub-recommendations "#securityhub-recommendations")
  - [Enable and set up AWS Organizations](#enabling-orgs "#enabling-orgs")

## Set up recommended Audit Manager

features

After you enable Audit Manager, we recommend that you enable the evidence finder feature.

**[Evidence finder](evidence-finder.md "evidence-finder.md")** provides a powerful way to
search for evidence in Audit Manager. Instead of browsing deeply nested evidence folders to
find what you're looking for, you can use evidence finder to quickly query your
evidence. If you use evidence finder as a delegated administrator, you can search
for evidence across all member accounts in your organization.

Using a combination of filters and groupings, you can progressively narrow the
scope of your search query. For example, if you want a high-level view of your
system health, perform a broad search and filter by assessment, date range, and
resource compliance. If your goal is to remediate a specific resource, you can
perform a narrow search to target evidence for a specific control or resource ID.
After you define your filters, you can group and then preview the matching search
results before creating an assessment report.

## Set up recommended integrations

with other AWS services

For an optimal experience in Audit Manager, we strongly recommend that you enable the
following AWS services:

- **AWS Organizations** – You can use Organizations to run
  Audit Manager assessments over multiple accounts and consolidate evidence into a
  delegated administrator account.
- **AWS Security Hub** and **AWS Config** – Audit Manager relies on these AWS services as
  data sources for evidence collection. When you enable AWS Config and Security Hub,
  Audit Manager can operate with its full functionality, collecting comprehensive
  evidence and accurately reporting the results of compliance checks directly
  from these services.

###### Important

If you don’t enable and configure AWS Config and Security Hub, you won’t be able to
collect the intended evidence for many controls in your Audit Manager assessments. As a
result, you risk incomplete or failed evidence collection for certain controls.
More specifically:

- If Audit Manager attempts to use AWS Config as a control data source, but the
  required AWS Config rules aren’t enabled, no evidence will be collected for
  those controls.
- Similarly, if Audit Manager attempts to use Security Hub as a control data source, but
  the required standards aren’t enabled in Security Hub, no evidence will be
  collected for those controls.
  To mitigate these risks and ensure comprehensive evidence collection, follow
  the steps on this page to enable and configure AWS Config and Security Hub before you create
  your Audit Manager assessments.

Many controls in Audit Manager require AWS Config as a data source type. To support these
controls, you must enable AWS Config on all accounts in each AWS Region where
Audit Manager is enabled.

Audit Manager doesn’t manage AWS Config for you. You can follow these steps to enable AWS Config
and configure its settings.

###### Important

Enabling AWS Config is an optional recommendation. However, if you do enable
AWS Config, the following settings are required. If Audit Manager tries to collect
evidence for controls that use AWS Config as a data source type, and AWS Config is
not set up as described below, no evidence is collected for those
controls.

**Tasks to integrate AWS Config with Audit Manager**

- [Step 1: Enable AWS Config](#enabling-config "#enabling-config")
- [Step 2: Configure your AWS Config settings for use
  with Audit Manager](#set-up-config "#set-up-config")

#### Step 1: Enable AWS Config

You can enable AWS Config using the AWS Config console or API. For instructions, see
[Getting started
with AWS Config](../../../config/latest/developerguide/getting-started.md "../../../config/latest/developerguide/getting-started.md") in the _AWS Config Developer
Guide_.

#### Step 2: Configure your AWS Config settings for use

with Audit Manager

After you enable AWS Config, make sure that you also [enable AWS Config rules](../../../config/latest/developerguide/setting-up-aws-config-rules-with-console.md "../../../config/latest/developerguide/setting-up-aws-config-rules-with-console.md") or [deploy
a conformance pack](../../../config/latest/developerguide/conformance-pack-console.md "../../../config/latest/developerguide/conformance-pack-console.md") for the compliance standard that's related to
your audit. This step ensures that Audit Manager can import findings for the AWS Config
rules that you enabled.

After you enable an AWS Config rule, we recommend that you review the parameters
of that rule. You should then validate those parameters against the
requirements of your chosen compliance framework. If needed, you can [update a rule’s parameters in AWS Config](../../../config/latest/developerguide/evaluate-config_manage-rules.md "../../../config/latest/developerguide/evaluate-config_manage-rules.md") to ensure that it aligns
with framework requirements. This will help to ensure that your assessments
collect the correct compliance check evidence for a given framework.

For example, suppose that you’re creating an assessment for CIS v1.2.0.
This framework has a control named [1.4 – Ensure access keys are rotated every 90 days or less](../../../securityhub/latest/userguide/securityhub-cis-controls.md#securityhub-cis-controls-1.4 "../../../securityhub/latest/userguide/securityhub-cis-controls.md#securityhub-cis-controls-1.4"). In
AWS Config, the [access-keys-rotated](../../../config/latest/developerguide/access-keys-rotated.md "../../../config/latest/developerguide/access-keys-rotated.md") rule has a `maxAccessKeyAge`
parameter with a default value of 90 days. As a result, the rule aligns with
the control requirements. If you aren’t using the default value, ensure that
the value you’re using is equal to or greater than the 90 day requirement
from CIS v1.2.0.

You can find the default parameter details for each managed rule in the
[AWS Config
documentation](../../../config/latest/developerguide/managed-rules-by-aws-config.md "../../../config/latest/developerguide/managed-rules-by-aws-config.md"). For instructions on how to configure a rule, see
[Working with AWS Config Managed Rules](../../../config/latest/developerguide/managing-aws-managed-rules.md "../../../config/latest/developerguide/managing-aws-managed-rules.md").

Many controls in Audit Manager require Security Hub as a data source type. To support
these controls, you must enable Security Hub on all accounts in each Region where
Audit Manager is enabled.

Audit Manager doesn’t manage Security Hub for you. You can follow these steps to enable Security Hub
and configure its settings.

###### Important

Enabling Security Hub is an optional recommendation. However, if you do
enable Security Hub, the following settings are required. If Audit Manager tries to
collect evidence for controls that use Security Hub as a data source type, and
Security Hub is not set up as described below, no evidence is collected for
those controls.

**Tasks to integrate AWS Security Hub with Audit Manager**

- [Step 1: Enable AWS Security Hub](#enabling-securityhub "#enabling-securityhub")
- [Step 2: Configure your Security Hub settings
  for use with Audit Manager](#set-up-securityhub "#set-up-securityhub")
- [Step 3: Configure the Organizations settings
  for your organization](#set-up-securityhub-orgs "#set-up-securityhub-orgs")

#### Step 1: Enable AWS Security Hub

You can enable Security Hub using either the console or the API. For
instructions, see [Setting up
AWS Security Hub](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md") in the _AWS Security Hub User
Guide_.

#### Step 2: Configure your Security Hub settings

for use with Audit Manager

After you enable Security Hub, make sure that you also do the following:

- [Enable AWS Config and configure resource recording](../../../securityhub/latest/userguide/securityhub-prereq-config.md "../../../securityhub/latest/userguide/securityhub-prereq-config.md")
  – Security Hub uses service-linked AWS Config rules to perform most of its
  security checks for controls. To support these controls, AWS Config must
  be enabled and configured to record resources that are required for
  the controls that you have enabled in each enabled standard.
- [Enable all security standards](../../../securityhub/latest/userguide/securityhub-standards-enable-disable.md#securityhub-standard-enable-console "../../../securityhub/latest/userguide/securityhub-standards-enable-disable.md#securityhub-standard-enable-console") – This step
  ensures that Audit Manager can import findings for all supported compliance
  standards.
- [Turn on the consolidated control findings setting in
  Security Hub](../../../securityhub/latest/userguide/controls-findings-create-update.md#turn-on-consolidated-control-findings "../../../securityhub/latest/userguide/controls-findings-create-update.md#turn-on-consolidated-control-findings") - This setting is turned _on_ by default if you enable Security Hub on or after
  February 23, 2023.

###### Note

When you enable consolidated findings, Security Hub produces a single
finding for each security check (even when the same check is
used across multiple standards). Each Security Hub finding is collected
as one unique resource assessment in Audit Manager. As a result,
consolidated findings results in a decrease of the total unique
resource assessments that Audit Manager performs for Security Hub findings. For
this reason, using consolidated findings can often result in a
reduction in your Audit Manager usages costs. For more information about
using Security Hub as a data source type, see [AWS Security Hub controls supported by AWS Audit Manager](control-data-sources-ash.md "control-data-sources-ash.md"). For more
information about Audit Manager pricing, see [AWS Audit Manager
Pricing](https://aws.amazon.com/audit-manager/pricing/ "https://aws.amazon.com/audit-manager/pricing/").

#### Step 3: Configure the Organizations settings

for your organization

If you use AWS Organizations and you want to collect Security Hub evidence from your
member accounts, you must also perform the following steps in Security Hub.

###### To set up your organization's Security Hub settings

1. Sign in to the AWS Management Console and open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. Using your AWS Organizations management account, designate an account as
   the delegated administrator for Security Hub. For more information, see
   [Designating a Security Hub administrator account](../../../securityhub/latest/userguide/designate-orgs-admin-account.md#designate-admin-console "../../../securityhub/latest/userguide/designate-orgs-admin-account.md#designate-admin-console") in the
   _AWS Security Hub User Guide_.

###### Note

Make sure that the delegated administrator account that you
designate in Security Hub is the same one that you use in Audit Manager. 3. Using your Organizations delegated administrator account, go to
**Settings, Accounts**, select all accounts,
and then add them as members by selecting
**Auto-enroll**. For more information, see
[Enabling member accounts from your organization](../../../securityhub/latest/userguide/orgs-accounts-enable.md "../../../securityhub/latest/userguide/orgs-accounts-enable.md") in the
_AWS Security Hub User Guide_. 4. Enable AWS Config for every member account of the organization. For
more information, see [Enabling member accounts from your organization](../../../securityhub/latest/userguide/orgs-accounts-enable.md "../../../securityhub/latest/userguide/orgs-accounts-enable.md") in the
_AWS Security Hub User Guide_. 5. Enable the PCI DSS security standard for every member account of
the organization. The AWS CIS Foundations Benchmark standard and
the AWS Foundational Best Practices standard are already enabled
by default. For more information, see [Enabling a security standard](../../../securityhub/latest/userguide/securityhub-standards-enable-disable.md#securityhub-standard-enable-console "../../../securityhub/latest/userguide/securityhub-standards-enable-disable.md#securityhub-standard-enable-console") in the _AWS Security Hub User Guide_.

Audit Manager supports multiple accounts via integration with AWS Organizations. Audit Manager can
run assessments over multiple accounts and consolidate evidence into a
delegated administrator account. The delegated administrator has permissions
to create and manage Audit Manager resources with the organization as the zone of
trust. Only the management account can designate a delegated administrator.

###### Important

Enabling AWS Organizations is an optional recommendation. However, if you do
enable AWS Organizations, the following settings are required.

**Tasks to integrate AWS Organizations with Audit Manager**

- [Step 1: Create or join an
  organization](#enabling-orgs-create "#enabling-orgs-create")
- [Step 2: Enable all
  features in your organization](#enabling-orgs-enable-all-features "#enabling-orgs-enable-all-features")
- [Step 3: Specify a delegated
  administrator for Audit Manager](#enabling-orgs-designate "#enabling-orgs-designate")

#### Step 1: Create or join an

organization

If your AWS account isn't part of an organization, you can create or
join an organization. For instructions, see [Creating and
managing an organization](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md") in the _AWS Organizations User
Guide_.

#### Step 2: Enable all

features in your organization

Next, you must enable all features in your organization. For instructions,
see [Enabling all features in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md") in the _AWS Organizations User Guide_.

#### Step 3: Specify a delegated

administrator for Audit Manager

We recommend that you enable Audit Manager using an Organizations management account, and
then specify a delegated administrator. After that, you can use the
delegated administrator account to log in and run assessments. As a best
practice, we recommend that you only create assessments using the delegated
administrator account instead of the management account.

To add or change a delegated administrator after you enable Audit Manager, see
[Adding a delegated administrator](add-delegated-admin.md "add-delegated-admin.md") and [Changing a delegated administrator](change-delegated-admin.md "change-delegated-admin.md").

## Next steps

Now that you have set up Audit Manager with the recommended settings, you're ready to get
started with using the service.

- To get started with your first assessment, see [Tutorial for Audit Owners: Creating an
  assessment](tutorial-for-audit-owners.md "tutorial-for-audit-owners.md").
- To update your settings in the future, see [Reviewing and configuring your AWS Audit Manager settings](console-settings.md "console-settings.md").
