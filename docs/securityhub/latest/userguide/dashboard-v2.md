# Working in the Summary dashboard in Security Hub

###### Note

Security Hub is in preview release and is subject to change.

The **Summary** dashboard in the Security Hub console shows an overview of your exposures, resources, threats, and security coverage across multiple security widgets.
Data automatically refreshes every time you open the **Summary** dashboard.

You can customize this page by adding and removing different security widgets and setting filter criteria to retrieve specific data in each widget.
Customizations are saved for future use.
If your account is the delegated administrator account for an organization, customizations are saved independently from customizations in member accounts.

If your account is the delegated administrator account for an organization, data includes findings for your account and member accounts.
If your account is a member account or a standalone account, data only includes findings for your account.
If you configure cross-Region aggregation in Security Hub, the **Summary** dashboard shows findings in your aggregation.

###### Note

We recommend that you do not include confidential, sensitive, or personally identifiable information (PII) in saved filters, custom widgets, or other related free-form text fields.

##

Exposure summary widget

This widget shows all of your exposures by severity.
An exposure is based on an analysis of findings and traits from Security Hub and other AWS security services, such as Amazon Inspector.
You can review the frequency of each exposure in your environment.
Exposures with greater severity appear first.
The list of exposures in this widget is limited to the eight highest exposures with the greatest number of critical findings.
If two or more exposures have an equal number of critical findings, the list automatically groups those findings behind more recent critical findings.

##

Resource summary widget

This widget shows all of your resources by type and includes the number of findings associated with them.
Resources are prioritized by exposures and attack sequences.

##

Security coverage widget

This widget shows an overview of your security coverage and is based on coverage findings for supported AWS security services.
It displays which coverage checks **Covered**, **Not covered**, or are **Not available**.
**Covered** indicates the coverage check passed.
**Not covered** indicates the coverage check failed.
**Not available** indicates the coverage check is unable to be completed.
This can be caused by a deleted resource or a failing server.

Percentages for coverage checks point to the number of checks that passed and failed.
For example, one coverage check passes, and one coverage check fails.
This indicates 50% of your checks passed, and 50% of your checks failed.
In some cases, percentages are rounded to the nearest whole number.

Unlike AWS security services such as GuardDuty, Amazon Inspector, and Macie, Security Hub CSPM publishes one coverage finding per account, which is `PASS`/`FAIL` depending on the enabled standards, such as `PASS` if at least 1 standard is enabled.
Coverage percentages for Security Hub CSPM are the number of Security Hub CSPM coverage findings that passed to the total number of Security Hub CSPM coverage findings.

###### Note

We recommend that you do not include confidential, sensitive, or personally identifiable information (PII) in saved filters, custom widgets, or other related free-form text fields.

##

Threat summary widget

This widget shows all of your threats by severity.
A threat refers to malicious activity or suspicious activity that can potentially compromise the security of your environment.
You can review the frequency of each threat in your environment.
Threats with greater severity appear first.
The list of threats in this widget is limited to the eight threats with the highest severity.
If two or more threats are of equal severity, the list automatically groups those findings behind more recent findings.

###### Note

You must enable GuardDuty to receive threat data in this widget.
For more information, see [Getting started with Amazon GuardDuty](../../../guardduty/latest/ug/guardduty_settingup.md "../../../guardduty/latest/ug/guardduty_settingup.md").
