# Impact of central configuration on cross-Region aggregation

Central configuration is an opt-in feature in AWS Security Hub CSPM that you can use if you integrate with AWS Organizations.
If you use central configuration, the delegated administrator account can configure the Security Hub CSPM service, standards, and controls for accounts and organizational units (OU) in the
organization. To configure accounts and OUs, the delegated administrator creates Security Hub CSPM configuration policies. Configuration policies can be used to define whether
Security Hub CSPM is enabled or disabled, and which standards and controls are enabled. The delegated administrator associates configuration policies with specific accounts, OUs, or the
root (the entire organization).

The delegated administrator can create and manage configuration policies for the organization only from the home Region. In addition, configuration policies take effect in the home Region and all linked Regions. You
can't create a configuration policy that applies only in some linked Regions and not others.
For information about cross-Region aggregation, see [Cross-Region aggregation](finding-aggregation.md "finding-aggregation.md").

To use central configuration, you
must designate a home Region. Optionally, you can choose one or more Regions as linked Regions. You can also choose to designate a
home Region without any linked Regions.

Changing your cross-Region aggregation settings can impact
your configuration policies. When you add a linked Region, your configuration policies take effect in that Region. If the Region is an
[opt-in Region](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md"), the Region must be enabled in order for your configuration policies to take effect there.
Conversely, when you remove a linked Region, configuration policies no longer take effect in that Region. In that Region, accounts maintain the
settings they had when the linked Region was removed. You can change those settings, but must do so separately in each
account and Region.

If you
remove or change the home Region, your configuration policies and policy associations are deleted. You can no longer
use central configuration or create configuration policies in any Region. Accounts maintain
the settings they had before the home Region was changed or removed. You can change those settings at any time, but since
you no longer use central configuration, settings must be modified separately in each account and Region. You can use central configuration
and create configuration policies again if you designate a new home Region.

For more information about central configuration, see [Understanding central configuration in Security Hub CSPM](central-configuration-intro.md "central-configuration-intro.md").
