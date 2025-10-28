# AppStream 2.0 Applications Reports

For each day that users launch at least one application during their streaming sessions,
AppStream 2.0 exports an applications report to your Amazon S3 bucket. The report, named
**daily-app-report-[YYYY]-[MM]-[DD].csv**, is stored
in a nested folder structure in your Amazon S3 account, using the following folder path:

[bucket\_name]/applications/schedule=DAILY/year=[YYYY]/month=[MM]/day=[DD]/

This nesting structure facilitates partitioning if you choose to query your reports by using Amazon Athena. Athena is a serverless, interactive query service that you can use to analyze data stored in your S3 buckets using standard SQL. For more information, see [Create Custom Reports and Analyze AppStream 2.0 Usage Data](configure-custom-reports-analyze-usage-data.md "configure-custom-reports-analyze-usage-data.md").

Each application launch is described in a single record in an applications report.
For example, if a user launches five separate applications during a session, five
separate records appear in the relevant applications report. An application is recorded
as launched if any of the following events occurs:

- The application is launched directly when the session begins, because the application ID is embedded in either the streaming URL or the relay state.
- A user chooses the application from the application catalog when launching a new streaming session.
- A user chooses the application from the application catalog list during a streaming session.
  The applications report doesn’t include applications that are launched in other ways.
  For example, if you provide users with access to Windows Explorer, PowerShell, or the Windows desktop **Start** menu, and
  users use those tools to launch applications directly, or if another program or script
  launches an application, those application launches are not included in the applications
  report.

Applications reports are generated daily according to UTC time within 24 hours of the close of the day that is the subject of the report. If a session spans more than one day, applications launched during the session are reflected in the applications report corresponding to the day in which the session ends. For information about the data included in applications reports, see [Applications Report Fields](usage-reports-fields-applications-reports.md "usage-reports-fields-applications-reports.md").
