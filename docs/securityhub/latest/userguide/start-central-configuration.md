# Enabling central configuration in Security Hub CSPM

The delegated AWS Security Hub CSPM administrator account can use central configuration to configure Security Hub CSPM, standards, and controls
for multiple accounts and organizational units (OUs) across AWS Regions.

For background information about the benefits of central configuration and how it works, see [Understanding central configuration in Security Hub CSPM](central-configuration-intro.md "central-configuration-intro.md").

This section explains prerequisites for central configuration and how to begin using it.

## Prerequisites for central configuration

Before you can start using central configuration, you must integrate Security Hub CSPM with AWS Organizations and designate a home Region. If you use the Security Hub CSPM console, these
prerequisites are included in the opt-in workflow for central configuration.

### Integrate with Organizations

You must integrate Security Hub CSPM and Organizations to use central configuration.

To integrate these services, you begin by creating an organization in Organizations. From the Organizations management account, you
then designate a Security Hub CSPM delegated administrator account. For instructions, see [Integrating Security Hub CSPM with AWS Organizations](designate-orgs-admin-account.md "designate-orgs-admin-account.md").

Ensure that you designate your delegated administrator in your **intended home Region**. When you start using central configuration, the same delegated
administrator is automatically set in all linked Regions as well. The Organizations management account
_cannot_ be set as the delegated administrator account.

###### Important

When you use central configuration, you can't use the Security Hub CSPM console or Security Hub CSPM APIs
to change or remove the delegated administrator account. If the Organizations management account uses AWS Organizations APIs to change or remove
the Security Hub CSPM delegated administrator, Security Hub CSPM automatically stops central configuration. Your configuration policies are also
disassociated and deleted. Member accounts retain the configuration that they had before the delegated administrator was changed or removed.

### Designate a home Region

You must designate a home Region to use central configuration. The home Region is the Region from which the
delegated administrator configures the organization.

###### Note

The home Region cannot be a Region that AWS has designated as an opt-in Region. An opt-in Region is disabled by
default. For a list of opt-in Regions, see [Considerations before enabling and disabling Regions](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations") in the
_AWS Account Management Reference Guide_.

Optionally, you can specify one or more linked Regions that are configurable from the home
Region.

The delegated administrator can create and manage configuration policies only from the home
Region. Configuration policies take effect in the home Region and all linked Regions. You can't create a
configuration policy that applies only to a subset of these Regions, and not others. The exception to this is
controls that involve global resources. If you use central configuration, Security Hub CSPM automatically disables
controls that involve global resources in all Regions except the home Region.
For more information, see [Controls that use global resources](controls-to-disable.md#controls-to-disable-global-resources "controls-to-disable.md#controls-to-disable-global-resources").

The home Region is also your Security Hub CSPM aggregation Region that receives findings, insights, and other data from linked Regions.

If you have already set an aggregation Region for cross-Region aggregation, then that's your default home Region for
central configuration. You can change the home Region before you start to use central configuration by deleting your current finding aggregator and creating a
new one in your desired home Region. A finding aggregator is a Security Hub CSPM resource that specifies the home Region and linked Regions.

To designate a home Region, see [the steps for setting an aggregation Region](finding-aggregation-enable.md "finding-aggregation-enable.md").
If you already have a home Region, you can invoke the [GetFindingAggregator](../../1.0/APIReference/API_GetFindingAggregator.md "../../1.0/APIReference/API_GetFindingAggregator.md") API to see details about it, including which Regions currently are linked to it.

## Instructions for enabling central configuration

Choose your preferred method, and follow the steps to enable central configuration for your organization.

Security Hub CSPM console

###### To enable central configuration (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. On the navigation pane, choose **Settings** and **Configuration**.
   Then, choose **Start central configuration**.

If you're onboarding to Security Hub CSPM, choose **Go to Security Hub CSPM**. 3. On the
**Designate delegated administrator** page, select your delegated administrator account or enter its account ID. If applicable, we
recommend choosing the same delegated administrator that you have set for other AWS
security and compliance services. Choose **Set delegated administrator**. 4. On the **Centralize organization** page, in the **Regions** section, select your
home Region. You must be signed in to the home Region
to proceed. If you've already set an aggregation Region for cross-Region aggregation, it's displayed as the home Region. To change the
home Region, choose **Edit Region settings**. You can then select your preferred home Region and return to this workflow. 5. Select at least one Region to link to the home Region. Optionally, choose whether you want to
automatically link future supported Regions to the home Region. The Regions you select here will be configurable from the home
Region by the delegated administrator. Configuration policies take effect in your home Region and all linked Regions. 6. Choose **Confirm and continue**. 7. You can now use central configuration. Continue following the console prompts to create your first configuration policy. If you're not ready to create a configuration policy yet,
choose **I'm not ready to configure yet**. You can create a policy later by choosing **Settings**
and **Configuration** in the navigation pane. For instructions on
creating a configuration policy, see [Creating and associating configuration policies](create-associate-policy.md "create-associate-policy.md").

Security Hub CSPM API

###### To enable central configuration (API)

1. Using the credentials of the delegated administrator account, invoke the [UpdateOrganizationConfiguration](../../1.0/APIReference/API_UpdateOrganizationConfiguration.md "../../1.0/APIReference/API_UpdateOrganizationConfiguration.md")
   API from the home Region.
2. Set the `AutoEnable` field to `false`.
3. Set the
   `ConfigurationType` field in the `OrganizationConfiguration` object to
   `CENTRAL`. This action has the following
   impact:
   - Designates the calling account as the Security Hub CSPM delegated administrator in all linked Regions.
   - Enables Security Hub CSPM in the delegated administrator account in all linked Regions.
   - Designates the calling account as the Security Hub CSPM delegated administrator for new and existing
     accounts that use Security Hub CSPM and belong to the
     organization. This occurs in the home Region and all linked Regions.
     The calling account is set as the delegated administrator for new organization accounts only if they
     are associated with a configuration policy that has Security Hub CSPM enabled. The calling account is set as the delegated administrator for existing organization accounts only if they already have Security Hub CSPM enabled.
   - Sets [AutoEnable](../../1.0/APIReference/API_UpdateOrganizationConfiguration.md#securityhub-UpdateOrganizationConfiguration-request-AutoEnable "../../1.0/APIReference/API_UpdateOrganizationConfiguration.md#securityhub-UpdateOrganizationConfiguration-request-AutoEnable") to
     `false` in all linked Regions, and sets [AutoEnableStandards](../../1.0/APIReference/API_UpdateOrganizationConfiguration.md#securityhub-UpdateOrganizationConfiguration-request-AutoEnableStandards "../../1.0/APIReference/API_UpdateOrganizationConfiguration.md#securityhub-UpdateOrganizationConfiguration-request-AutoEnableStandards") to
     `NONE` in the home Region and all linked Regions. These parameters aren't relevant in the home and linked Regions when you use central configuration, but you can
     automatically enable Security Hub CSPM and default security standards in
     organization accounts through the use of
     configuration policies.

4. You can now use central configuration. The delegated administrator can create configuration policies to configure Security Hub CSPM in your organization. For
   instructions on creating a configuration policy, see [Creating and associating configuration policies](create-associate-policy.md "create-associate-policy.md").

**Example API request:**

```
{
    "AutoEnable": false,
    "OrganizationConfiguration": {
        "ConfigurationType": "CENTRAL"
    }
}

```

AWS CLI

###### To enable central configuration (AWS CLI)

1. Using the credentials of the delegated administrator account, run the [update-organization-configuration](../../../cli/latest/reference/securityhub/update-organization-configuration.md "../../../cli/latest/reference/securityhub/update-organization-configuration.md") command from the
   home Region.
2. Include the `no-auto-enable` parameter.
3. Set the
   `ConfigurationType` field in the `organization-configuration` object to
   `CENTRAL`. This action has the following impact:
   - Designates the calling account as the Security Hub CSPM delegated administrator in all linked Regions.
   - Enables Security Hub CSPM in the delegated administrator account in all linked Regions.
   - Designates the calling account as the Security Hub CSPM delegated administrator for new and existing
     accounts that use Security Hub CSPM and belong to the
     organization. This occurs in the home Region and all linked Regions. The calling account is set as the delegated administrator for new organization accounts only if they are associated with a configuration policy that has Security Hub enabled.
     The calling account is set as the delegated administrator for existing organization accounts only if they already have Security Hub CSPM enabled.
   - Sets the auto-enablement option to [no-auto-enable](../../../cli/latest/reference/securityhub/update-organization-configuration.md#options "../../../cli/latest/reference/securityhub/update-organization-configuration.md#options") in all linked Regions, and sets
     [auto-enable-standards](../../../cli/latest/reference/securityhub/update-organization-configuration.md#options "../../../cli/latest/reference/securityhub/update-organization-configuration.md#options") to `NONE` in the home Region and all linked Regions.
     These parameters aren't relevant in the home and linked Regions when you use central configuration, but you can
     automatically enable Security Hub CSPM and default security standards in organization accounts through the use of
     configuration policies.

4. You can now use central configuration. The delegated administrator can create configuration policies to configure Security Hub CSPM in your organization. For
   instructions on creating a configuration policy, see [Creating and associating configuration policies](create-associate-policy.md "create-associate-policy.md").

**Example command:**

```
aws securityhub --region us-east-1 update-organization-configuration \
--no-auto-enable \
--organization-configuration '{"ConfigurationType": "`CENTRAL`"}'

```
