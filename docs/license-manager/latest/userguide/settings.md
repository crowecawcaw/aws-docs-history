# Settings in License Manager

The **Settings** section of the AWS License Manager console displays settings for the
current account. You must configure settings to enable associated functionality.

Managed licenses
The following settings are configurable for managed licenses:

- Distribution of managed entitlements and self-managed licenses to your organization
- Cross-account resource discovery
- Amazon SNS notification
- License asset discovery and ruleset configuration for License asset groups

For organizations using License asset groups, additional settings are available for cross-region discovery and organization-wide license management across multiple AWS regions and accounts.

For more information, see [Managed license settings in License Manager](settings-managed-licenses.md "settings-managed-licenses.md").

Linux subscriptions
The following settings are configurable for Linux subscriptions:

- Discovery and aggregation of Commercial Linux license subscription data
- Red Hat Subscription Manager (RHSM) discovery for Linux subscriptions

For more information, see [Linux subscription settings in
License Manager](settings-linux-subscriptions.md "settings-linux-subscriptions.md").

User-based subscriptions
The following settings are configurable for user-based subscriptions:

- AWS Managed Microsoft AD
- Virtual Private Cloud (VPC)

For more information, see [User-based subscription settings in
License Manager](settings-user-based-subscriptions.md "settings-user-based-subscriptions.md").

Delegated administration
This tab is displayed if your account has administrative access for your
organization. As an administrator, you can register a delegated administrator
from the AWS CLI or AWS Management Console. For more information, see [Delegated administrator settings in License Manager](delegated-administrator.md "delegated-administrator.md").

###### Settings topics

- [Edit License Manager settings](settings.md#settings-edit "settings.md#settings-edit")
- [Managed license settings in License Manager](settings-managed-licenses.md "settings-managed-licenses.md")
  - [License asset discovery and ruleset settings](settings-managed-licenses.md#settings-license-asset-groups "settings-managed-licenses.md#settings-license-asset-groups")
  - [Account details](settings-managed-licenses.md#settings-account-details "settings-managed-licenses.md#settings-account-details")
  - [Cross-account resource discovery](settings-managed-licenses.md#settings-resource-discovery "settings-managed-licenses.md#settings-resource-discovery")
  - [Simple Notification Service (SNS)](settings-managed-licenses.md#settings-sns "settings-managed-licenses.md#settings-sns")

- [Linux subscription settings in
  License Manager](settings-linux-subscriptions.md "settings-linux-subscriptions.md")
  - [Linux subscriptions settings](settings-linux-subscriptions.md#linux-subscriptions-general-settings "settings-linux-subscriptions.md#linux-subscriptions-general-settings")
  - [Red Hat Subscription Manager discovery](settings-linux-subscriptions.md#linux-subscriptions-rhsm-settings "settings-linux-subscriptions.md#linux-subscriptions-rhsm-settings")

- [User-based subscription settings in
  License Manager](settings-user-based-subscriptions.md "settings-user-based-subscriptions.md")
  - [AWS Managed Microsoft AD](settings-user-based-subscriptions.md#settings-managed-ad "settings-user-based-subscriptions.md#settings-managed-ad")
  - [Virtual private cloud](settings-user-based-subscriptions.md#settings-vpc "settings-user-based-subscriptions.md#settings-vpc")

- [Delegated administrator settings in License Manager](delegated-administrator.md "delegated-administrator.md")
  - [Regions supported for
    delegated License Manager administrators](delegated-administrator.md#delegated-administrator-supported-regions "delegated-administrator.md#delegated-administrator-supported-regions")
  - [Register a delegated License Manager
    administrator](delegated-administrator.md#register-delegated-admin "delegated-administrator.md#register-delegated-admin")
  - [Deregister a delegated License Manager
    administrator](delegated-administrator.md#deregister-delegated-admin "delegated-administrator.md#deregister-delegated-admin")

## Edit License Manager settings

To edit your License Manager settings, follow these steps:

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, choose **Settings**.
3. Choose the tab containing the settings to configure. For example, choose
   **Managed licenses** to configure **Account details**.
4. After you've configured your settings, choose **Save**, or
   choose **Cancel** to back out.
