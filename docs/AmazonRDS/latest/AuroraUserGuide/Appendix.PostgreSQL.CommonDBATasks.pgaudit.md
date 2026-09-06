

# Using pgAudit to log database activity
<a name="Appendix.PostgreSQL.CommonDBATasks.pgaudit"></a>

Financial institutions, government agencies, and many industries need to keep *audit logs* to meet regulatory requirements. By using the PostgreSQL Audit extension (pgAudit) with your Aurora PostgreSQL DB cluster, you can capture the detailed records that are typically needed by auditors or to meet regulatory requirements. For example, you can set up the pgAudit extension to track changes made to specific databases and tables, to record the user who made the change, and many other details.

The pgAudit extension builds on the functionality of the native PostgreSQL logging infrastructure by extending the log messages with more detail. In other words, you use the same approach to view your audit log as you do to view any log messages. For more information about PostgreSQL logging, see [Aurora PostgreSQL database log files](USER_LogAccess.Concepts.PostgreSQL.md). 

The pgAudit extension redacts sensitive data such as cleartext passwords from the logs. If your Aurora PostgreSQL DB cluster is configured to log data manipulation language (DML) statements as detailed in [Turning on query logging for your Aurora PostgreSQL DB cluster ](USER_LogAccess.Concepts.PostgreSQL.Query_Logging.md), you can avoid the cleartext password issue by using the PostgreSQL Audit extension. 

You can configure auditing on your database instances with a great degree of specificity. You can audit all databases and all users. Or, you can choose to audit only certain databases, users, and other objects. You can also explicitly exclude certain users and databases from being audited. For more information, see [Excluding users or databases from audit logging](Appendix.PostgreSQL.CommonDBATasks.pgaudit.exclude-user-db.md). 

Given the amount of detail that can be captured, we recommend that if you do use pgAudit, you monitor your storage consumption. 

The pgAudit extension is supported on all available Aurora PostgreSQL versions. For a list of pgAudit versions supported by Aurora PostgreSQL version, see [Extension versions for Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Extensions.html) in the *Release Notes for Aurora PostgreSQL*. 

**Topics**
+ [Setting up the pgAudit extension](Appendix.PostgreSQL.CommonDBATasks.pgaudit.basic-setup.md)
+ [Auditing database objects](Appendix.PostgreSQL.CommonDBATasks.pgaudit.auditing.md)
+ [Excluding users or databases from audit logging](Appendix.PostgreSQL.CommonDBATasks.pgaudit.exclude-user-db.md)
+ [Reference for the pgAudit extension](Appendix.PostgreSQL.CommonDBATasks.pgaudit.reference.md)