# Historical metrics reports in Amazon Connect

Historical metrics reports include data about past, completed activity and performance
in your contact center. Amazon Connect includes built-in historical reports that you
can start using right away. You can also build your own custom reports.

When creating and analyzing your historical metrics reports, keep in mind that there
are two categories of metrics:

**Contact record-driven metrics**

These metrics are based on formed contact record records. For a given
interval, contact records whose disconnect date falls in the interval are
selected to calculate metrics. For example, if a contact starts at 05:23 and
ends at 06:15, this contact contributes 52 minutes of metrics for the
06:00-06:30 interval.

Example contact record-driven metrics are **Service
level**, **Agent interaction time**, and
**After contact work time**.

**Agent activity-driven metrics**

These metrics are based on agent activities, like agent status changes,
agent conversation changes. The metrics reflect on the actual time the
activity happens. For example, if agent handles a contact from 05:23 to
06:15, the **Agent on contact time** has 7 minutes for the
05:00-05:30 interval, 30 minutes for the 05:30-06:00 interval, and 15
minutes for the 06:00-06:30 interval.

For example, an agent activity-driven metric is **Non-Productive
Time**.

You can customize the report settings to get the view of the data that is most
meaningful for your organization. You can change the time frame for the report, which
metrics are included in the report, and how data is grouped in the report. After you
have customized a report, you can save it for future reference. You can generate a
report using a recurring schedule that you define.

###### Contents

- [Apply tag-based access
  control](hm-tag-based-access-control.md "hm-tag-based-access-control.md")
- [Create a custom historical
  metrics report in Amazon Connect](create-historical-metrics-report.md "create-historical-metrics-report.md")
- [Report
  limits](historical-reporting-limits.md "historical-reporting-limits.md")
- [Schedule a historical metrics
  report in Amazon Connect](schedule-historical-metrics-report.md "schedule-historical-metrics-report.md")
- [Update a historical metrics
  report](update-historical-metrics-report.md "update-historical-metrics-report.md")
- [Download a historical metrics
  report in Amazon Connect](download-historical-metrics-report.md "download-historical-metrics-report.md")
- [Show agent queues in a Queues
  table](show-agent-queues.md "show-agent-queues.md")
- [How many contacts
  in queue on a specific date](contacts-in-queue-on-specific-date.md "contacts-in-queue-on-specific-date.md")
- [Agent activity audit report in
  Amazon Connect](agent-activity-audit-report.md "agent-activity-audit-report.md")
