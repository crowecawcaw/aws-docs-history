On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Findings overview metrics

Use the **Findings overview** section of the dashboard to
monitor metrics related to open findings in your account. The findings overview metrics are
refreshed whenever a scan is run and are calculated based on all open findings.

## Open and critical findings

The **Open and critical findings** panel displays the total number of open
findings and the total number of open critical findings across your account. The percentage next
to the absolute number indicates the change in the metric from the previous week.

You can choose the number of findings to be redirected to the findings page and view your
open findings.

Monitor the number of open and critical findings in your account periodically to track the
security posture of your code.

## Severity distribution

The **Severity distribution** panel is a graphical representation of the
distribution of the severity of all open findings. The severity of a finding can be one of five
categories: Critical, High, Medium, Low, and Informational. For information on how severity is
calculated and how severity levels are defined, see [Finding severity](finding-severity.md "finding-severity.md").

Check the severity distribution of your findings to monitor how severe the vulnerabilities
in your code are.

## Vulnerability assessment

The **Vulnerability assessment** panel displays the top four
vulnerabilities that are found across all open findings. This metric is calculated on a weekly
basis.

Use the vulnerability assessment metric to monitor the most common security issues in your
code, if they are being remediated, and if certain vulnerabilities become more or less
common.

## Scans with most findings and most critical findings

The **Scans with most findings** panel lists the top three
scans that have generated the most findings and how many open findings each scan has. You can
choose **View all scans** to see a list of all scans in your
account.

The **Scans with most critical findings** panel lists the top
three scans that have generated the most critical findings and how many open critical findings
each scan has. You can choose **View all critical findings** to see
a list of all open critical findings in your account.

Use these metrics to track which code scans have the most open findings to target the areas
of your application that are most unsecure.
