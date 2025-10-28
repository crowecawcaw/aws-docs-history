# Understanding central configuration in Security Hub CSPM

Central configuration is an AWS Security Hub CSPM feature that helps you set up and manage Security Hub CSPM across
multiple AWS accounts and AWS Regions. To use central configuration, you must first
integrate Security Hub CSPM and AWS Organizations. You can integrate the services by creating an organization and
designating a delegated Security Hub CSPM administrator account for the organization.

From the delegated Security Hub CSPM administrator account, you can enable Security Hub CSPM for your
organization’s accounts and organizational units (OUs) across Regions. You can also enable,
configure, and disable individual security standards and security controls for accounts and
OUs across Regions. You can configure these settings in just a few steps from one primary
Region, referred to as the _home Region_.

When you use central configuration, the delegated administrator can choose which accounts and OUs to configure. If the delegated administrator designates a member account or OU as _self-managed_, the member can configure its own
settings separately in each Region. If the delegated administrator designates a member account or OU as _centrally managed_, only the delegated administrator can configure the member account or OU
across Regions. You can designate all accounts and OUs in your organization as centrally managed, all self-managed, or a combination of both.

To configure centrally managed accounts, the delegated administrator uses Security Hub CSPM
configuration policies. Configuration policies let the delegated administrator specify
whether Security Hub CSPM is enabled or disabled, and which standards and controls are enabled or
disabled. They can also be used to customize parameters for certain controls.

Configuration policies take effect in the home Region and all linked Regions. The delegated administrator specifies the organization's home Region and linked Regions before starting to use central configuration. Specifying
linked Regions is optional. The delegated administrator can create a single configuration policy for the whole organization, or create multiple configuration policies to configure variable settings for different accounts and
OUs.

###### Tip

If you don't use central configuration, you must largely configure Security Hub CSPM separately in each account and Region. This is called
_local configuration_. Under local configuration, the delegated administrator can automatically enable
Security Hub CSPM and a limited set of security standards in new organization accounts in the current Region. Local configuration doesn't apply to
existing organization accounts or to Regions other than the current Region. Local configuration also doesn't support the use of configuration policies.

This section provides an overview of central configuration.

## Benefits of using central configuration

Benefits of central configuration include the following:

**Simplify configuration of the Security Hub CSPM service and capabilities**
When you use central configuration, Security Hub CSPM guides you through the process of configuring security best practices for your organization.
It also deploys the resulting configuration policies to specified accounts and OUs automatically. If you have existing Security Hub CSPM settings, such as automatically
enabling new security controls, you can use those as a starting point for your configuration policies. In addition, the **Configuration** page on the
Security Hub CSPM console displays a real-time summary of your configuration policies and which accounts and OUs use each policy.

**Configure across accounts and Regions**
You can use central configuration to configure Security Hub CSPM across multiple accounts and Regions.
This helps ensure that each part of your organization maintains a consistent configuration and adequate security coverage.

**Accommodate different configurations in different accounts and OUs**
With central configuration, you can choose to configure your organization's accounts and OUs
in different ways. For example, your test accounts and production accounts might require different configurations. You can also
create a configuration policy that covers new accounts when they join the organization.

**Prevent configuration drift**
Configuration drift occurs when a user makes a change to a service or feature that conflicts
with the delegated administrator's selections. Central configuration prevents this drift. When you designate an account or OU as centrally managed, it's configurable only
by the delegated administrator for the organization. If you prefer a specific account or OU to configure its own settings, you can designate it
as self-managed.

## When to use central configuration?

Central configuration is most beneficial for AWS environments that include multiple Security Hub CSPM accounts. It's designed to
help you centrally manage Security Hub CSPM for multiple accounts.

You can use central configuration to configure the Security Hub CSPM service, security standards, and security controls. You can
also use it to customize parameters of certain controls. For more information about security standards, see [Understanding security standards in Security Hub CSPM](standards-view-manage.md "standards-view-manage.md").
For more information about security controls, see [Understanding security controls in Security Hub CSPM](controls-view-manage.md "controls-view-manage.md").

## Central configuration terms and

concepts

Understanding the following key terms and concepts can help you use Security Hub CSPM central configuration.

**Central configuration**

A Security Hub CSPM feature that helps the delegated Security Hub CSPM administrator account for an organization configure the Security Hub CSPM service, security standards, and security controls
across multiple accounts and Regions. To configure these settings, the delegated administrator creates and manages Security Hub CSPM configuration policies for centrally managed accounts in their organization. Self-managed accounts can configure their own settings separately in each Region.
To use central configuration, you must integrate Security Hub CSPM and AWS Organizations.

**Home Region**

The AWS Region from which the delegated administrator centrally configures Security Hub CSPM, by creating and managing
configuration policies. Configuration policies take effect in the home Region and all linked Regions.

The home Region also serves as the Security Hub CSPM aggregation Region, receiving findings, insights, and other data from linked Regions.

Regions that AWS introduced on or after March 20, 2019 are known as opt-in Regions. An opt-in Region can't be the home Region, but it
can be a linked Region. For a list of opt-in Regions, see [Considerations before enabling and disabling Regions](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations")
in the _AWS Account Management Reference Guide_.

**Linked Region**

An AWS Region that is configurable from the home Region. Configuration policies are created
by the delegated administrator in the home Region. The policies take effect in the home Region and all linked Regions. Specifying
linked Regions is optional.

A linked Region also sends findings, insights, and other data to the home Region.

Regions that AWS introduced on or after March 20, 2019 are known as opt-in Regions. You must enable
such a Region for an account before a configuration policy can be applied to it. The Organizations management account
can enable opt-in Regions for a member account. For more information,
see [Specify which AWS Regions your account can use](../../../accounts/latest/reference/manage-acct-regions.md#rande-manage-enable "../../../accounts/latest/reference/manage-acct-regions.md#rande-manage-enable") in the _AWS Account Management Reference Guide_.

**Target**

An AWS account, organizational unit (OU), or the organization root.

**Security Hub CSPM configuration policy**

A collection of Security Hub CSPM settings that the delegated administrator can configure for centrally managed targets. This includes:

- Whether to enable or disable Security Hub CSPM.
- Whether to enable one or more [security standards](standards-reference.md "standards-reference.md").
- Which [security controls](securityhub-controls-reference.md "securityhub-controls-reference.md") to enable across the enabled standards. The delegated administrator can do this by providing a list of
  specific controls that should be enabled, and Security Hub CSPM disables all other controls (including new controls when they are released). Alternatively, the delegated administrator
  can provide a list of specific controls that should be disabled, and Security Hub CSPM enables all other controls (including new controls when they
  are released).
- Optionally, [customize parameters](custom-control-parameters.md "custom-control-parameters.md")
  for select enabled controls across the enabled standards.

A configuration policy takes effect in the home Region and all linked Regions after it's associated with
at least one account, organizational unit (OU), or the root.

On the Security Hub CSPM console, the delegated administrator can choose the Security Hub CSPM recommended configuration policy
or create custom configuration policies. With the Security Hub CSPM API and AWS CLI, the delegated administrator can only
create custom configuration policies. The delegated administrator can create a maximum of 20 custom configuration policies.

In the recommended configuration policy, Security Hub CSPM, the
AWS Foundational Security Best Practices (FSBP) standard, and
all existing and new FSBP controls are enabled. Controls that accept parameters use the default values. The recommended configuration policy applies to the entire organization.

To apply different settings to the organization, or apply different configuration policies to different accounts and OUs, create
a custom configuration policy.

**Local configuration**

The default configuration type for an organization, after integrating Security Hub CSPM and AWS Organizations. With local configuration, the delegated administrator can choose to automatically enable Security Hub CSPM and
[default security standards](securityhub-auto-enabled-standards.md "securityhub-auto-enabled-standards.md") in _new_ organization accounts in the current Region. If the delegated administrator automatically enables default standards,
all controls that are part of these standards are also automatically enabled with default parameters for new organization accounts. These settings don't apply to existing
accounts, so configuration drift is possible after an account joins the organization. Disabling specific controls that are part of the default standards, and configuring additional standards and controls,
must be done separately in each account and Region.

Local configuration doesn't support the use of configuration policies. To use configuration policies, you must switch to central configuration.

**Manual account management**

If you don't integrate Security Hub CSPM with AWS Organizations or you have a standalone account, you must specify settings for each account
separately in each Region. Manual account management doesn't support the use of configuration policies.

**Central configuration APIs**

Security Hub CSPM operations that only the Security Hub CSPM delegated Security Hub CSPM administrator can use in the home
Region to manage configuration policies for centrally managed accounts. The operations
include:

- `CreateConfigurationPolicy`
- `DeleteConfigurationPolicy`
- `GetConfigurationPolicy`
- `ListConfigurationPolicies`
- `UpdateConfigurationPolicy`
- `StartConfigurationPolicyAssociation`
- `StartConfigurationPolicyDisassociation`
- `GetConfigurationPolicyAssociation`
- `BatchGetConfigurationPolicyAssociations`
- `ListConfigurationPolicyAssociations`

**Account-specific APIs**

Security Hub CSPM operations that can be used to enable or disable Security Hub CSPM, standards, and controls on an account-by-account basis. These operations
are used in each individual Region.

Self-managed accounts can use account-specific operations to configure their own
settings. Centrally managed
accounts can't use the following account-specific operations in the home Region and linked Regions. In those Regions, only the
delegated administrator can configure centrally managed accounts through central configuration operations and configuration policies.

- `BatchDisableStandards`
- `BatchEnableStandards`
- `BatchUpdateStandardsControlAssociations`
- `DisableSecurityHub`
- `EnableSecurityHub`
- `UpdateStandardsControl`

To check account status, the owner of a centrally managed account _can_ use any `Get` or
`Describe` operations of the Security Hub CSPM API.

If you use local configuration or manual account management, instead of central configuration, these
account-specific operations can be used.

Self-managed accounts can also use `*Invitations` and `*Members` operations.
However, we recommend that self-managed accounts don't use these operations. Policy associations can fail if a member account
has its own members that are part of a different organization than the delegated administrator's.

**Organizational unit (OU)**

In AWS Organizations and Security Hub CSPM, a container for a group of AWS accounts. An organizational unit (OU) also can contain other OUs, enabling you to create a
hierarchy that resembles an upside-down tree, with a parent OU at the top and branches of OUs that reach down, ending in accounts
that are the leaves of the tree. An OU can have exactly one parent, and each organization account can be a member of exactly one OU.

You can manage OUs in AWS Organizations or AWS Control Tower. For more
information, see [Managing
organizational units](../../../organizations/latest/userguide/orgs_manage_ous.md "../../../organizations/latest/userguide/orgs_manage_ous.md") in the
_AWS Organizations User Guide_ or [Govern
organizations and accounts with AWS Control Tower](../../../controltower/latest/userguide/existing-orgs.md "../../../controltower/latest/userguide/existing-orgs.md") in the
_AWS Control Tower User Guide_.

The delegated administrator can associate configuration policies with specific accounts or OUs, or with the root to cover all accounts and OUs in an
organization.

**Centrally managed**

A target that only the delegated administrator can configure across Regions by using configuration policies.

The delegated administrator account specifies whether a target is
centrally managed. The delegated administrator can also change a target's status
from centrally managed to self-managed, or the other way around.

**Self-managed**

A target that manages its own Security Hub CSPM settings. A self-managed target
uses account-specific operations to configure Security Hub CSPM for itself separately in each Region.
This is in contrast to centrally managed targets, which are configurable only by the
delegated administrator across Regions through configuration policies.

The delegated administrator account specifies whether a target is
self-managed. The delegated administrator can apply self-managed behavior to a target. Alternatively, an account or
OU can inherit self-managed behavior from a parent.

The delegated administrator account can itself be
a self-managed account.The delegated administrator account can change a target's status
from self-managed to centrally managed, or the other way around.

**Configuration policy association**

A link between a configuration policy and an account, organizational unit (OU), or root. When a policy association
exists, the account, OU, or root uses the settings defined by the configuration policy. An association exists in either of these cases:

- When the delegated administrator directly applies a configuration policy to an account, OU, or root
- When an account or OU inherits a configuration policy from a parent OU or the root

An association exists until a different configuration is applied or inherited.

**Applied configuration policy**

A type of configuration policy association in which the delegated administrator directly applies a configuration policy to
target accounts, OUs, or the root. Targets are configured in the way that the
configuration policy defines, and only the delegated administrator can change their configuration. If applied to root, the configuration policy affects all
accounts and OUs in the organization that don't use a different configuration through application or inheritance from the closest parent.

The delegated administrator can also apply a self-managed configuration to specific accounts, OUs, or the root.

**Inherited configuration policy**

A type of configuration policy association in which an account or OU adopts the configuration of the closest parent OU or the root.
If a configuration policy isn't directly applied to an account or OU, it inherits the configuration of the closest parent.
All elements of a policy are inherited. In other words, an account or OU can't choose to selectively inherit only parts of a policy.
If the closest parent is self-managed, the child account or OU inherits the self-managed behavior of the parent.

Inheritance can't override an applied configuration. That is, if a configuration policy or self-managed configuration
is directly applied to an account or OU, it uses that configuration and doesn't inherit the configuration of the parent.

**Root**

In AWS Organizations and Security Hub CSPM, the top-level parent node in an organization.
If the delegated administrator applies a configuration policy to root, the policy
is associated with all accounts and OUs in the organization unless they use a
different policy, through application or inheritance, or are designated as self-managed. If the administrator designates the root as self-managed,
all accounts and OUs in the organization are self-managed unless they use a configuration policy through application or inheritance.
If the root is self-managed and no configuration policies currently
exist, all new accounts in the organization retain their current settings.

New accounts that join an organization fall under the root until they are assigned to a specific OU. If a
new account isn't assigned to an OU, it inherits the root configuration unless the delegated administrator designates it as a
self-managed account.
