# Creating a scan configuration

Before you create a scan configuration, you must [create an integration with Amazon Inspector](code-security-assessments-create-integration.md "code-security-assessments-create-integration.md").
The first time you create an integration, you're prompted to create a default scan configuration.
This topic describes how to create a general scan configuration.
The difference between a default scan configuration and a general scan configuration is that a default scan configuration is automatically attached to new projects.
You can skip creating a default scan configuration.

Code Security only supports a maximum of 500 general scan configurations.
Code security only supports 1 default scan configuration per account and per organization.
A scan configuration only can be associated with a maximum of 100,000 projects.

A project can be associated with a maximum of 4 scan configurations total.
This includes a default scan configuration if a default scan configuration was created.
Scan configurations for an organization cannot be tagged.

If the delegated administrator for an organization creates a scan configuration, the scan configuration is created at the organization level and applied to all member accounts in the organization.
The same occurs if the delegated administrator creates a default scan configuration.

When you create a scan configuration, you choose the scan frequency, scan analysis, and repositories to be scanned.
The scan frequency can be change based and periodic or customized.
Change-based and periodic scanning gives you the option to enable periodic scanning.
If you enable periodic scanning, you set the scan frequency to the day of the week or month when a scan occurs.
Customized scanning gives you the option to enable scanning when code is changed and periodic scanning.
If you enable scanning when code is changed, you specify the scan trigger to include in merge and pull requests.

Scans can be skipped if a commit ID hasn't changed in a set amount of time.
For periodic scanning, scans are skipped if a commit ID hasn't changed between scans in 1 week.
For on-demand scans, scans are skipped if a commit ID hasn't changed between scans in 24 hours.

###### Note

If a scan configuration only has triggers for merge requests and pull requests, only the top 25 critical or high findings are presented and only in the source code management platform.
None will be visible in Amazon Inspector.

###### To create a general scan configuration

1. Sign in using your credentials.
   Open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. From the navigation pane, choose **Code Security**.
3. Choose **Configurations**, and then choose **Create scan configuration**.
4. Under **Scan details**, do the following:
   1. For **Configuration name**, enter a name for the scan configuration.

5. Under **Scan frequency**, specify how often code is scanned by choosing **Change-based and periodic scanning** or **Customized scanning types and triggers**.
   1. (Option 1) If you choose **Change based and periodic scanning**, choose **Enable periodic scanning** or **Disable periodic scanning**.
      1. .
         If you choose **Enable periodic scanning**, set the scan frequency by choosing the week and day you want code to be scanned.

   2. (Option 2) If you choose **Customized scanning**, decide whether to enable scanning when code is changed and periodic scanning.
      1. Choose **Enable scanning when code is changed** or **Disable scanning when code is changed**.
         If you choose **Enable scanning when code is changed**, specify when scans are triggered from the dropdown.
      2. Choose **Enable periodic scanning** or **Disable periodic scanning**.
         If you choose **Enable periodic scanning**, set the scan frequency by choosing the week and day you want code to be scanned.
         You can also scan on event-based triggers.
         These events include when a pull request is open against the default branch and when a commit is pushed to the default branch.

6. Under **Scan analysis**, decide whether to configure a complete scanning analysis or customized scanning analysis:
   1. (Option 1) If you choose **Complete scanning analysis**, you apply all of the following scan analyses:
      - _Static Application Security Testing_ – Analyzes source code for vulnerabilities.
      - _IaC scanning_ – Analyzes scripts and code that configure and provision infrastructure.
      - _Static software composition analysis_ – Examines open source packages in applications.

   2. (Option 2) If you choose **Customized scanning analysis**, you must choose at least one type of the previously mentioned scan analysis types from the dropdown menu:

7. (Optional) For **Tags**, create a key-value pair to apply to your project.
   You can create up to 50 tags.
8. Choose **Next**.
9. Under **Repository selection**, choose **All repositories** or **Specific repositories**.
   1. (Option 1) If you choose **All repositories**, scanning is enabled for any of your existing repositories.
   2. (Option 2) If you choose **Specific repositories**, scanning is enabled only for the repositories that you specify.

10. Choose **Next**.
11. Review your choices, and then choose **Create scan configuration**.

###### Note

General scan configurations are applied to all existing code repositories only.
They will not be applied to new code repositories.
