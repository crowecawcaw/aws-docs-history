# Report server databases

When your DB instance is associated with the SSRS option, two new databases are created on your DB instance:

- `rdsadmin_ReportServer`
- `rdsadmin_ReportServerTempDB`
  These databases act as the ReportServer and ReportServerTempDB databases.
  SSRS and PBIRS store their data in the ReportServer database and cache their data in the ReportServerTempDB database.
  For more information, see [Report Server Database](https://learn.microsoft.com/en-us/sql/reporting-services/report-server/report-server-database-ssrs-native-mode?view=sql-server-ver15 "https://learn.microsoft.com/en-us/sql/reporting-services/report-server/report-server-database-ssrs-native-mode?view=sql-server-ver15")
  in the Microsoft documentation.

RDS owns and manages these databases, so database operations on them such as ALTER and DROP aren't permitted.
Access isn't permitted on the `rdsadmin_ReportServerTempDB` database. However,
you can perform read operations on the `rdsadmin_ReportServer`database.
