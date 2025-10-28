# Filtering and sorting control findings

Selecting a control from the **Controls** page of the AWS Security Hub CSPM console or
from the details page of a standard takes you to the control details page.

The control details page shows the title and description of the control, the overall control status,
and a breakdown of security checks for the control in the last 24 hours.

Use the **Filter by** options next to the control checks list to quickly
focus on findings with a specific [workflow status](findings-workflow-status.md "findings-workflow-status.md") or
[compliance status](controls-overall-status.md#controls-overall-status-compliance-status "controls-overall-status.md#controls-overall-status-compliance-status").

In addition to the **Filter by** options, you can use the **Add filter** box
to filter the checks list by other fields, such as AWS account ID or resource ID.

By default, findings with a compliance status of **PASSED** are listed first. You can
change the default sorting by choosing a different option in the column headers.

From the control details page, you can choose **Download** to download the current page of control findings to a .csv file.

If you filter the finding list, then the download only includes the controls that
match the filter. If you select specific findings from the list, then the download only includes the
selected findings.

For more information about filtering findings, see [Filtering findings in Security Hub CSPM](securityhub-findings-manage.md "securityhub-findings-manage.md").
