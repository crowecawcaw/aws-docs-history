# Using pgAudit to log database activity

Financial institutions, government agencies, and many industries need to keep
_audit logs_ to meet regulatory requirements. By using the PostgreSQL Audit
extension (pgAudit) with your RDS for PostgreSQL DB instance, you can
capture the detailed records that are typically needed by auditors or to meet regulatory
requirements. For example, you can set up the pgAudit extension to track changes made to
specific databases and tables, to record the user who made the change, and many other
details.

The pgAudit extension builds on the functionality of the native PostgreSQL
logging infrastructure by extending the log messages with more detail. In other words, you use the same
approach to view your audit log as you do to view any log messages. For more information about PostgreSQL logging,
see [RDS for PostgreSQL database log files](USER_LogAccess.Concepts.md "USER_LogAccess.Concepts.md").

The pgAudit extension redacts sensitive data such as cleartext passwords from the logs.
If your RDS for PostgreSQL
DB instance is configured to log data manipulation language (DML) statements as detailed in
[Turning on query
logging for your RDS for PostgreSQL DB instance](USER_LogAccess.Concepts.PostgreSQL.md "USER_LogAccess.Concepts.PostgreSQL.md"),
you can avoid the cleartext password issue by using the PostgreSQL Audit extension.

You can configure auditing on your database instances with a great degree of specificity. You can audit
all databases and all users. Or, you can choose to audit only certain databases, users, and other objects.
You can also explicitly exclude certain users and databases from being audited. For more information, see
[Excluding users or databases from audit logging](Appendix.PostgreSQL.CommonDBATasks.pgaudit.md "Appendix.PostgreSQL.CommonDBATasks.pgaudit.md").

Given the amount of detail that can be captured, we recommend that if you do use pgAudit, you monitor
your storage consumption.

The pgAudit extension is supported on all available
RDS for PostgreSQL versions. For a list of pgAudit versions supported by available
RDS for PostgreSQL versions, see [Extension
versions for Amazon RDS for PostgreSQL](../PostgreSQLReleaseNotes/postgresql-extensions.md "../PostgreSQLReleaseNotes/postgresql-extensions.md") in the _Amazon RDS for PostgreSQL Release Notes._

###### Topics

- [Setting up the pgAudit extension](Appendix.PostgreSQL.CommonDBATasks.pgaudit.md "Appendix.PostgreSQL.CommonDBATasks.pgaudit.md")
- [Auditing database objects](Appendix.PostgreSQL.CommonDBATasks.pgaudit.md "Appendix.PostgreSQL.CommonDBATasks.pgaudit.md")
- [Excluding users or databases from audit logging](Appendix.PostgreSQL.CommonDBATasks.pgaudit.md "Appendix.PostgreSQL.CommonDBATasks.pgaudit.md")
- [Reference for the pgAudit
  extension](Appendix.PostgreSQL.CommonDBATasks.pgaudit.md "Appendix.PostgreSQL.CommonDBATasks.pgaudit.md")
