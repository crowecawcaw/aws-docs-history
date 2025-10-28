# Metrics, dashboards, and reports in Amazon Connect

In Amazon Connect, data about contacts are captured in contact records. This data can
include the amount of time a contact spends in each state: customer on hold, customer in
queue, agent interaction time.

The basis for most historical and real-time metrics in Amazon Connect is the data in
the contact record. When you create metrics reports, the values displayed for **most** (not all) metrics in the report are calculated using the
data in the contact records.

Contact records are available within your instance for 24 months from the time when the
associated contact was initiated. You can also stream contact records to Amazon Kinesis to retain the data longer, and perform advanced analysis on it.

###### Tip

For detailed information about the activity of agents in your contact center, use
[Amazon Connect agent event streams](agent-event-streams.md "agent-event-streams.md").

###### Contents

- [Metric definitions](metrics-definitions.md "metrics-definitions.md")
- [Assign
  permissions](dashboard-required-permissions.md "dashboard-required-permissions.md")
- [Dashboards](dashboards.md "dashboards.md")
- [Real-time metrics
  reports](real-time-metrics-reports.md "real-time-metrics-reports.md")
- [Historical metrics
  reports](historical-metrics.md "historical-metrics.md")
- [Login/Logout reports for agents in Amazon Connect](login-logout-reports.md "login-logout-reports.md")
- [Agent event streams](agent-event-streams.md "agent-event-streams.md")
- [Contacts, contact chains,
  and contact attributes](contacts-contact-chains-attributes.md "contacts-contact-chains-attributes.md")
- [Contact events](contact-events.md "contact-events.md")
- [Contact records data model](ctr-data-model.md "ctr-data-model.md")
- [Use contact segment
  attributes](use-contact-segment-attributes.md "use-contact-segment-attributes.md")
- [Apply hierarchy-based access
  control](dashboard-access-control.md "dashboard-access-control.md")
- [Identify conferences and
  transfers](identify-conferences-transfers.md "identify-conferences-transfers.md")
- [View a contact record in the Amazon Connect admin website](sample-ctr.md "sample-ctr.md")
- [Agent status in the Contact Control Panel
  (CCP)](metrics-agent-status.md "metrics-agent-status.md")
- [About contact states](about-contact-states.md "about-contact-states.md")
- [About queued
  callbacks](about-queued-callbacks.md "about-queued-callbacks.md")
- [Save custom reports](save-reports.md "save-reports.md")
- [Share saved reports](share-reports.md "share-reports.md")
- [View a shared report](view-a-shared-report.md "view-a-shared-report.md")
- [Make a report read-only](readonly-reports.md "readonly-reports.md")
- [Publish reports](publish-reports.md "publish-reports.md")
- [Manage saved reports
  (admin)](manage-saved-reports-admin.md "manage-saved-reports-admin.md")
- [Monitor CloudWatch metrics](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Logging service API
  calls](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
- [EventBridge events emitted by Amazon Connect](connect-eventbridge-events.md "connect-eventbridge-events.md")
- [Analytics data lake](data-lake.md "data-lake.md")
