

# Viewing discovered issues
<a name="cv-viewing-issues"></a>

You can review issues for an environment on the **Issues** tab in the AWS Continuum console. Use search and the severity filter to find an issue, then choose its title to review the available details.

**To find and review an issue**

1. Open the AWS Continuum console at [https://console.aws.amazon.com/continuum/](https://console.aws.amazon.com/continuum/).

1. In the navigation pane, choose **Environments**.

1. Choose the name of your environment.

1. Choose the **Issues** tab to view the list of issues.

1. (Optional) To search for an issue, enter text in **Find issues**.

1. (Optional) For **Severity**, select **Critical**, **High**, **Medium**, or **Low**. Select **All severities** to remove the severity filter.

1. Choose the issue title to open its details.

Search, sorting, and counts include only issues that the console has loaded. When **Load more** appears, choose it to include additional issues. Use the page controls to move through the loaded results.

If the table shows **No matching issues**, choose **Clear filters** to remove your search and severity filter. To retrieve updated results, choose the refresh icon labeled **Refresh issues**.

If no issues appear after you clear filters, a scan or its results might still be processing. Check the **Scans** tab for progress, then refresh the issues list.

The available details depend on the issue's processing results. You might see the following:
+ **Issue details**
+ **Severity** and **Processing status**
+ **Synopsis** and **Risk assessment**
+ Validation evidence in **Proof**
+ **Remediation summary** and **Patch details**
+ **Contributing findings**

When **Proof** appears, review the evidence shown there, such as **Source analysis**. The proof type depends on the issue. A unit test or executable proof might not be available.

For more information about available patches, see [Viewing generated patches](cv-viewing-patches.md).