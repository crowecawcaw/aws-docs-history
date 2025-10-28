# Understanding local configuration in Security Hub CSPM

Local configuration is the default way that an AWS organization is configured in Security Hub CSPM. If you don't opt in to and enable
central configuration, your organization uses local configuration by default.

Under local configuration, the delegated Security Hub CSPM administrator account has limited control over configuration settings.
The only settings that the delegated administrator can enforce are automatically enabling
Security Hub CSPM and default security standards in new organization accounts. These settings apply only in the Region in which you designated
the delegated administrator account. The default security standards
are AWS Foundational Security Best Practices (FSBP) and Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0. Local configuration settings don't apply to
existing organization accounts or to Regions other than the one in which the delegated administrator account was designated.

Aside from enabling Security Hub CSPM and default standards in new organization accounts in a single Region, you must configure other Security Hub CSPM settings, including
standards and controls, separately in each Region and account. Because this can be a duplicative process, we recommend using central configuration
for a multi-account environment if one or more of the following applies to you:

- You want different configuration settings for various parts of your organization (for example, different
  enabled standards or controls for different teams).
- You operate in multiple Regions and want to reduce the time and complexity of configuring the service
  across these Regions.
- You want new accounts to use specific configuration settings when they join the organization.
- You want organization accounts to inherit specific configuration settings from a parent account or root.
  For information about central configuration, see [Understanding central configuration in Security Hub CSPM](central-configuration-intro.md "central-configuration-intro.md").
