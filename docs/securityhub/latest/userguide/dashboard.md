#

Working with the dashboard in Security Hub CSPM

On the Security Hub CSPM console, the **Summary** dashboard shows a summary of your
risks, attack sequences, and security coverage. This dashboard helps you identify risks and
attack sequences based on severity and account coverage for different security capabilities.
Each time you open the dashboard, it refreshes automatically. Note, however, that security
scores and control statuses refresh every 24 hours.

You can customize the **Summary** dashboard by adding and removing
different security widgets from it. You can also specify filter criteria to retrieve and
display particular types of data. If you customize the dashboard, Security Hub saves your
customization settings. If other users of your account customize the dashboard, their
changes are saved independently from your customization settings.

If you configured cross-Region aggregation in Security Hub CSPM, the **Summary**
dashboard shows your aggregated data. If your account is the delegated administrator account
for an organization, the data includes findings for your account and your member accounts.
If your account is a member account or a standalone account, the data includes findings only
for your account.

###### Topics

- [Available widgets for the Summary dashboard](#available-widgets "#available-widgets")
- [Filtering the
  dashboard](filters-dashboard.md "filters-dashboard.md")
- [Customizing the
  dashboard](customize-dashboard.md "customize-dashboard.md")

## Available widgets for the Summary dashboard

The **Summary** dashboard includes widgets that reflect the modern cloud security threat
landscape, guided by the security operations and experiences of AWS customers. Some widgets are shown by default while
others are not. You can customize your view of the dashboard by adding or removing widgets.

To add a widget, choose **Add widget** at the top of the dashboard.
You can then browse the list of available widgets or enter the title of a widget in the
search bar. When you find the widget to add, drag it to the location where you want it
to appear on the dashboard. For more information, see [Customizing the
dashboard](customize-dashboard.md "customize-dashboard.md").

### Widgets shown by default

By default, the **Summary** dashboard includes the following
widgets.

**Top threat sequences**

Displays the highest severity threat sequences. Threat sequence findings, known as _attack sequence findings_ in
Amazon GuardDuty, correlate multiple events to identify potential threats to your AWS environment. Threat sequences may
include in-progress or recent attack behaviors (within a 24-hour time window) in your environment, which may in turn
lead to further compromise. You must have GuardDuty and GuardDuty S3 Protection enabled to receive threat sequence findings in Security Hub CSPM.

**Top risks**

Displays a summary of the top risks in your environment. The top of the widget shows you the count of risks at
each severity level. You can choose a severity level to go to the
**Risks** page with risks filtered to the selected severity level. Risks that have the most
occurrences in your environment appear first.
This widget helps
you prioritize which risks to mitigate.

**Security coverage**

Summarizes the extent of your security coverage, based on coverage control findings. Coverage
controls check whether a specific AWS service and its capabilities are enabled (for example, [[Macie.1] Amazon Macie should be enabled](macie-controls.md#macie-1 "macie-controls.md#macie-1")).
This widget helps you ensure that
you have `PASSED` findings for coverage controls. The Security Hub CSPM console provides
links from this widget to help you enable missing security capabilities. We recommend using central configuration to enable
missing security capabilities across multiple AWS accounts and AWS Regions. For more information, see [Understanding central configuration in Security Hub CSPM](central-configuration-intro.md "central-configuration-intro.md").

**Security standards**

Displays your most recent summary security score and the security score for each
Security Hub CSPM standard. Security scores, which range from 0–100 percent, represent
the proportion of passed controls relative to all of your enabled controls. For more
information about these scores, see [Method of calculating security scores](standards-security-score.md#standard-security-score-calculation "standards-security-score.md#standard-security-score-calculation"). This widget helps
you understand your overall security posture.

**Assets with the most findings**

Provides an overview of the resources, accounts, and applications that have the most
findings. The list is sorted in descending order by the number of findings. In the widget, each tab
shows the top six items in that category, grouped by severity and
resource type. If you choose a number in the **Total findings** column,
Security Hub CSPM opens a page that shows the findings for the asset. This widget helps you quickly identify
which of your core assets have potential security threats.

**Findings by Region**

Shows the total number of findings, grouped by severity, in each
AWS Region in which Security Hub CSPM is enabled. This widget helps you identify security issues that potentially affect
particular Regions. If you open the dashboard in your aggregation Region, this widget helps you monitor potential
security issues in each linked Region.

**Most common threat types**

Provides a breakdown of the 10 most common types of threats in your AWS environment. This
includes threats such as escalation of privileges, use of exposed
credentials, or communication with malicious IP addresses.

To view this data, [Amazon GuardDuty](../../../guardduty/latest/ug/securityhub-integration.md "../../../guardduty/latest/ug/securityhub-integration.md") must be enabled. If it is, choose a threat type in this widget to
open the GuardDuty console and review findings related to this threat. This widget helps you evaluate potential threats
in the context of other security issues.

**Software vulnerabilities with exploits**

Provides a summary of software vulnerabilities that exist in your AWS environment and have known exploits. You
can also review a breakdown of vulnerabilities that do and don't have fixes available.

To view this data, [Amazon Inspector](../../../inspector/latest/user/securityhub-integration.md "../../../inspector/latest/user/securityhub-integration.md") must be enabled. If it is, choose a
statistic in this widget to open the Amazon Inspector console and review more details about the vulnerability. This widget helps you
evaluate software vulnerabilities in the context of other security issues.

**New findings over time**

Shows trends in the number of new daily findings during the past 90 days. You
can break down the data by severity or by provider for additional
context. This widget helps you understand if finding volume spiked or
dropped at specific times during the past 90 days.

**Resources with the most findings**

Provides a summary of the resources that have generated the most findings, broken down by the following
resource types: Amazon Simple Storage Service (Amazon S3) buckets, Amazon Elastic Compute Cloud (Amazon EC2) instances, and AWS Lambda functions.

In the widget, each tab focuses on one of the preceding
resource types, listing the 10 resource instances that generated the most
findings. To review the findings for a specific resource, choose the resource instance.
This widget helps you triage security findings that are associated with common AWS resources.

### Widgets hidden by default

The following widgets are also available for the **Summary**
dashboard, but they are hidden by default.

**AMIs with the most findings**

Provides a list of the 10 Amazon Machine Images (AMIs) that have generated
the most findings. This data is available only if Amazon EC2 is enabled for
your account. It helps you identify which AMIs pose potential security
risks.

**IAM principals with the most findings**

Provides a list of the 10 AWS Identity and Access Management (IAM) users that have generated the most findings. This widget helps you perform administrative and
billing tasks. It shows you which users contribute to Security Hub CSPM usage the most.

**Accounts with the most findings (by severity)**

Shows a graph of the 10 accounts that have generated the most findings, grouped by severity. This
widget helps you determine which accounts to focus analysis and remediation efforts on.

**Accounts with the most findings (by resource type)**

Shows a graph of the 10 accounts that have generated the most findings, grouped by resource type.
This widget helps you determine which accounts and resource types to prioritize for analysis and remediation.

**Insights**

Lists five [Security Hub CSPM managed insights](securityhub-managed-insights.md "securityhub-managed-insights.md") and the
number of findings that they generated. Insights identify a specific security area that
requires attention.

**Latest findings from AWS integrations**

Shows the number of findings that you received in Security Hub CSPM from
[integrated AWS services](securityhub-internal-providers.md "securityhub-internal-providers.md"). It also shows when you most recently
received findings from each integrated service. This widget provides consolidated findings data from multiple AWS services.
To drill down, choose an integrated service. Security Hub CSPM then opens the console for that service.
