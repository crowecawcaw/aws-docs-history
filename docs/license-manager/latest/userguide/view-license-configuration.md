# View self-managed licenses in License Manager

You can view your self-managed licenses through the License Manager console to monitor usage, compliance, and distribution across your AWS environment.

## View licenses in a single account

To view self-managed licenses within your current account:

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the left navigation pane, choose `Self-managed licenses`.
3. Review the list of licenses, their status, and current usage.
4. Choose a license name to view detailed information including associated resources and compliance status.

## View aggregated licenses (For Organization Administrator or Delegated Administrator)

Organization Administrators and Delegated Administrators can view self-managed licenses across all AWS accounts in their organization from a centralized location. This provides organization-wide visibility and management capabilities for license compliance.

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. Ensure you are signed in as an Organization Administrator or Delegated Administrator.
3. In the left navigation pane, choose `Self-managed licenses`.
4. Choose the `Organization license configuration` tab to view the aggregated license view.
5. Review the aggregated view of all self-managed licenses across your organization's accounts.

This aggregated view enables centralized license governance and helps ensure compliance across your entire AWS organization.

###### To view aggregated licenses using the command line

- [list-license-configurations-for-organization](../../../cli/latest/reference/license-manager/list-license-configurations-for-organization.md "../../../cli/latest/reference/license-manager/list-license-configurations-for-organization.md") (AWS CLI)
