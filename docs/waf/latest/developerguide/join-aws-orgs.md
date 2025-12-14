**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Joining and configuring AWS Organizations for using Firewall Manager

To use Firewall Manager, your account must be a member of the organization in the
AWS Organizations service where you want to use your Firewall Manager policies.

###### Note

For information about Organizations, see [AWS Organizations User Guide](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

###### To establish the required AWS Organizations membership and configuration

1. Choose an account to use as the Firewall Manager administrator for the organization in Organizations.
2. If your chosen account isn't already a member of the organization, have it join. Follow the guidance at [Inviting an AWS account to join your organization](../../../organizations/latest/userguide/orgs_manage_accounts_invites.md "../../../organizations/latest/userguide/orgs_manage_accounts_invites.md").
3. AWS Organizations has two available feature sets: _consolidated billing
   features_ and _all features_. To use Firewall Manager, your organization
   must be enabled for all features. If your organization is configured only for consolidated
   billing, follow the guidance at
   [Enabling All Features in Your Organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md").
