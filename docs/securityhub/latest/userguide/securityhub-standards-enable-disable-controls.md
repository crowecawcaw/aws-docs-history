# Enabling controls in

Security Hub CSPM

In AWS Security Hub CSPM, a control is a safeguard within a security standard that helps an organization protect the confidentiality,
integrity, and availability of its information. Each Security Hub CSPM control is related to a specific AWS resource. When you enable a control,
Security Hub CSPM begins to run security checks for the control and generates findings for it. Security Hub CSPM also considers all enabled controls when calculating security scores.

You can choose to enable a control across all of the security standards that it applies to.
Alternatively, you can configure the enablement status
differently in different standards. We recommend the former option, in which
the enablement status of a control is aligned across all of your enabled standards. For instructions on enabling
a control across all standards that it applies it, see [Enabling a control across standards](enable-controls-overview.md "enable-controls-overview.md"). For instructions on enabling
a control in specific standards, see [Enabling a control in a specific standard](controls-configure.md "controls-configure.md").

If you enable cross-Region aggregation and sign in to an aggregation Region, the Security Hub CSPM console shows controls
that are available in at least one linked Region.
If a control is available in a linked Region but not in the aggregation Region, you can't
enable or disable that control from the aggregation Region.

You can enable and disable controls in each Region by using the Security Hub CSPM console, Security Hub CSPM API, or AWS CLI.

The instructions for enabling and disabling controls vary based on whether or not you use [central configuration](central-configuration-intro.md "central-configuration-intro.md"). This topic describes the differences.
Central configuration is available to users who integrate Security Hub CSPM and AWS Organizations. We recommend using central configuration to
simplify the process of enabling and disabling controls in multi-account, multi-Region environments. If you use central configuration,
you can enable a control across multiple accounts and Regions through the use of configuration policies. If you don't use
central configuration, you must enable a control separately in each Region and account.
