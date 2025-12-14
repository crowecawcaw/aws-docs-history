**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Resource sharing for Network Firewall and DNS Firewall policies

To manage Firewall Manager Network Firewall and DNS Firewall policies, you must enable resource sharing with AWS Organizations in
AWS Resource Access Manager. This allows Firewall Manager to deploy protections across your accounts when you create these policy types.

To enable resource sharing, follow the instructions at
[Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS Resource Access Manager User Guide_.

###### Problems with resource sharing

You might encounter problems with resource sharing, either when you use AWS RAM to enable it, or
when you're working on Firewall Manager policies that require it.

Examples of these problems include the following:

- When you follow the instructions to enable sharing, in the AWS RAM console, the choice
  **Enable sharing with AWS Organizations** is grayed out and not
  available for selection.
- When you work in Firewall Manager on a policy that requires resource sharing, the policy is marked as
  non-compliant and you see messages indicating that resource sharing or AWS RAM
  isn't enabled.
  If you encounter problems with resource sharing, use the following procedure to try to enable it.

###### Try again to enable resource sharing

- Try again to enable sharing using one of the following options:
  - (Option) Through the AWS RAM console, follow the instructions at [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS Resource Access Manager
    User Guide_.
  - (Option) Using the AWS RAM API, call `EnableSharingWithAwsOrganization`. See the
    documentation at [EnableSharingWithAwsOrganization](../../../ram/latest/APIReference/API_EnableSharingWithAwsOrganization.md "../../../ram/latest/APIReference/API_EnableSharingWithAwsOrganization.md").
