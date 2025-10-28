On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Understanding dashboard metrics

The dashboard page in the CodeGuru Security console shows high-level metrics about findings generated
by all scans in an account. The dashboard page visually shows key insights about security issues
in your application that you can use to drive business decisions related to the security of your
code. Use the dashboard as a vulnerability-tracking tool for your applications by monitoring
metrics to track the security of your code over time.

To see metrics for your account, go to the **Dashboard** page in
the [CodeGuru Security
console](https://console.aws.amazon.com/codeguru/security/dashboard/ "https://console.aws.amazon.com/codeguru/security/dashboard/"). There are two sections, a findings overview and a vulnerability fix overview.
The findings overview includes metrics about open and critical findings, finding severity,
vulnerabilities, and more. The vulnerability resolution overview section provides metrics related
to closed findings.

To get account metrics with the AWS CLI or AWS SDKs, call
[`GetMetricsSummary`](../security-api/API_GetMetricsSummary.md "../security-api/API_GetMetricsSummary.md") or
[`ListFindingsMetrics`](../security-api/API_ListFindingsMetrics.md "../security-api/API_ListFindingsMetrics.md").

This section explains the metrics in the dashboard and how to interpret them.

###### Topics

- [Findings overview metrics](findings-overview.md "findings-overview.md")
- [Vulnerability fix overview metrics](vulnerability-resolution-overview.md "vulnerability-resolution-overview.md")
