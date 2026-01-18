# Full load PostgreSQL database migration

The full load migration phase populates the target database with a copy of the source data. This chapter describes the following native methods to help you choose the one that best matches your migration scenario.

- pg_dump and pg_restore
- Publisher and Subscriber
- pglogical
  We recommend that you begin by reviewing the following table to understand the tools suitable for your use case.

| Method                   | Supported versions         | Support of metadata migration | Suitable database sizes | Performance |
| ------------------------ | -------------------------- | ----------------------------- | ----------------------- | ----------- |
| pg_dump and pg_restore   | All versions of PostgreSQL | Yes                           | 100 GB or less          | Medium      |
| Publisher and Subscriber | PostgreSQL 10.0 and higher | No                            | Any size                | High        |
| pglogical                | PostgreSQL 9.4 and higher  | Yes                           | Any size                | High        |

The suitable database sizes provided in the preceding table are the AWS DMS recommendations. These recommendations are based on customer migration experiences and aren’t the limitation of the native tools.

###### Topics

- [Preparing for Ongoing Replication](chap-manageddatabases.md "chap-manageddatabases.md")
- [PostgreSQL pg_dump and pg_restore utility](chap-manageddatabases.md "chap-manageddatabases.md")
- [PostgreSQL publisher and subscriber model](chap-manageddatabases.md "chap-manageddatabases.md")
- [PostgreSQL pglogical extension](chap-manageddatabases.md "chap-manageddatabases.md")
