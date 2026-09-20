

# Metrics, dashboards, and insights in Connect Customer
<a name="amazon-connect-metrics"></a>

In Connect Customer, data about contacts are captured in contact records. This data can include the amount of time a contact spends in each state: customer on hold, customer in queue, agent interaction time. 

The basis for most historical and real-time metrics in Connect Customer is the data in the contact record. When you create metrics reports, the values displayed for **most** (not all) metrics in the report are calculated using the data in the contact records. 

Contact records are available within your instance for 24 months from the time when the associated contact was initiated. You can also stream contact records to Amazon Kinesis to retain the data longer, and perform advanced analysis on it.

**Tip**  
For detailed information about the activity of agents in your contact center, use [Connect Customer agent event streams](agent-event-streams.md).

**Topics**
+ [Metric definitions in Connect Customer](metrics-definitions.md)
+ [Custom metric primitives](metric-primitive-definitions.md)
+ [Assign permissions to view dashboards and reports in Connect Customer](dashboard-required-permissions.md)
+ [Dashboards in Connect Customer for getting contact center performance data](dashboards.md)
+ [Manager assist in Connect Customer](manager-assist.md)
+ [Real-time metrics reports in Connect Customer](real-time-metrics-reports.md)
+ [Historical metrics reports in Connect Customer](historical-metrics.md)
+ [Login/Logout reports for agents in Connect Customer](login-logout-reports.md)
+ [Connect Customer agent event streams](agent-event-streams.md)
+ [Contacts, contact chains, and contact attributes](contacts-contact-chains-attributes.md)
+ [Connect Customer contact events](contact-events.md)
+ [Data model for Connect Customer contact records](ctr-data-model.md)
+ [Use contact segment attributes](use-contact-segment-attributes.md)
+ [Use predefined attributes in dashboards](use-predefined-attributes-dashboards.md)
+ [Change the "Agent activity" status in a metrics report in the Contact Control Panel (CCP)](rtm-change-agent-activity-state.md)
+ [Apply hierarchy-based access control to dashboards and reports in Connect Customer](dashboard-access-control.md)
+ [Apply tag-based access controls to dashboards and reports in Connect Customer](dashboard-tag-based-access-control.md)
+ [Identify conferences and transfers by using Connect Customer contact records](identify-conferences-transfers.md)
+ [View a contact record in the Connect Customer admin website](sample-ctr.md)
+ [Agent status in the Contact Control Panel (CCP)](metrics-agent-status.md)
+ [About contact states in Connect Customer](about-contact-states.md)
+ [Queued callbacks in real-time metrics in Connect Customer](about-queued-callbacks.md)
+ [Save custom reports in Connect Customer](save-reports.md)
+ [Share saved reports in Connect Customer](share-reports.md)
+ [View a shared report in Connect Customer](view-a-shared-report.md)
+ [Make a report in Connect Customer read-only](readonly-reports.md)
+ [Publish reports in Connect Customer](publish-reports.md)
+ [Manage saved reports as an admin in Connect Customer](manage-saved-reports-admin.md)
+ [Monitoring your Connect Customer instance using CloudWatch](monitoring-cloudwatch.md)
+ [Log Connect Customer API calls with AWS CloudTrail](logging-using-cloudtrail.md)
+ [EventBridge events emitted by Connect Customer](connect-eventbridge-events.md)