# Account coverage in Security Hub

Security Hub allows you to enable multiple capabilities across Regions and organization accounts through policies and configurations.
Some of these capabilities are from services outside of Security Hub, including Amazon Inspector, Amazon GuardDuty, AWS Security Hub CSPM, and Amazon Macie.
You can use the **Account coverage** page to track which accounts and Regions are covered by these capabilities.

## Account coverage page

The account coverage page provides visibility into security capability enablement across your AWS accounts.
This view helps you identify gaps in your security coverage and track capability adoption across your organization.

###### To access the Security Hub **Account coverage** page

1. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. From the navigation pane, under **Settings** choose **Account coverage**.

### Overview section

The **Overview** section displays aggregated security coverage metrics across all monitored accounts.
This high-level visualization shows the percentage of accounts with each security capability enabled, offering a comprehensive view of your security posture.
You can select each percentage of covered capability to filter the coverage finding results to display findings related to coverage for that capability.

The percentages in the Overview section are determined using the following calculation:

`(Count of number of accounts and regions the capability is enabled in)`/`((Total number of accounts Security Hub is enabled in)`\*`(Number of regions the capability is available in))`

### Accounts tab

The **Accounts** tab enables account-specific coverage analysis through filtering by account functionality.
Each security capability displays a coverage percentage that, when selected, reveals a detailed breakdown of individual features and their coverage percentage within that capability.
When you select these percentages, the system filters the coverage finding results to display those that indicate the coverage for that capability and for the account in that row.

The percentages in the Accounts tab are determined using the following calculation:

`(Count of number of regions the capability is enabled in)`/`(Number of regions the capability is available in)`

There are several cases where the coverage percentage might show as 0%:

- Security Hub is not enabled in the account and therefore no coverage findings are being ingested.
- Security Hub is waiting for coverage findings to be generated.

### Coverage findings tab

The **Coverage findings** tab displays informational findings generated when security capability checks detect disabled features in an account.
These findings help identify areas where security coverage can be enhanced.
Each coverage finding provides information on the title of the coverage finding, the account and region of the finding, and the current status of the finding.
Each finding also has a configure link that takes you to the individual service where the configuration for that capability can to be managed, or to the Security Hub configurations page where you can update your current configurations for security services.

For more information about coverage findings, see [Coverage findings in Security Hub](coverage-findings.md "coverage-findings.md").

## Security coverage widget

Account coverage can also be viewed via the **Security coverage widget** in the Security Hub summary dashboard.
More details about the widget can be found at [Security coverage widget](dashboard-v2.md#security-hub-v2-dashboard-coverage-widget "dashboard-v2.md#security-hub-v2-dashboard-coverage-widget") documentation.
