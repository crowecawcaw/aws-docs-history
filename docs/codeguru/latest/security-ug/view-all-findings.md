On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# View all findings

You can view a list of all findings in your account on the **Findings** page in the [CodeGuru Security console](https://console.aws.amazon.com/codeguru/security/Findings "https://console.aws.amazon.com/codeguru/security/Findings"), or use the AWS CLI
and AWS SDKs.

###### Topics

- [View findings in the console](#view-findings-console "#view-findings-console")
- [View findings with the AWS CLI or AWS SDKs](#view-findings-cli-sdk "#view-findings-cli-sdk")

## View findings in the console

The **Overview** panel summarizes the security posture of your
code based on open critical findings and provides the number of open critical findings in your
account, if any. The **Closed findings** panel lists how many
findings you have addressed across all scans. The **Findings
summary** panel indicates how many findings of each severity level are open across all
scans. For information about the severity of findings, see [Severity definitions](finding-severity.md#severity-definitions "finding-severity.md#severity-definitions").

The **Findings** section lists all findings in your account,
including the name of the vulnerability, the name of the scan that generated the finding, the
severity of the finding, the age of the finding, the time the finding was detected, and the
status of the finding.

You can customize what findings are listed on the Findings page using the dropdown menus
next to the search bar. Findings are grouped by severity. By default, findings with critical
severity are shown. You can choose the **All severities** dropdown
menu to change which finding severity you want to view. Choose the **Open
status** dropdown to change the status of findings you want to view.

To customize the view of the Findings table, choose the gear icon on the upper right side
of the table. In the **Preferences** window that appears, you can
select page size, display settings, and which columns you want to see.

## View findings with the AWS CLI or AWS SDKs

To view a list of findings in your account with the AWS CLI or AWS SDKs, use the [`ListFindings`](../security-api/API_ListFindings.md "../security-api/API_ListFindings.md") or [`BatchGetFindings`](../security-api/API_BatchGetFindings.md "../security-api/API_BatchGetFindings.md") operations. For more information, see the
[Amazon CodeGuru Security API Reference](../security-api.md "../security-api.md").
