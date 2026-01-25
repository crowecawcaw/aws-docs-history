# SQL Server Audit

In Amazon RDS, you can audit Microsoft SQL Server databases by using the built-in SQL Server
auditing mechanism. You can create audits and audit specifications in the same way that you
create them for on-premises database servers.

RDS uploads the completed audit logs to your S3 bucket, using the IAM role that you
provide. If you enable retention, RDS keeps your audit logs on your DB instance for the
configured period of time.

For more information, see [SQL Server Audit (database engine)](https://docs.microsoft.com/sql/relational-databases/security/auditing/sql-server-audit-database-engine "https://docs.microsoft.com/sql/relational-databases/security/auditing/sql-server-audit-database-engine") in the Microsoft SQL Server documentation.

## SQL Server Audit with Database Activity Streams

You can use Database Activity Streams for RDS to integrate SQL Server Audit events with
database activity monitoring tools from Imperva, McAfee, and IBM. For more information about
auditing with Database Activity Streams for RDS SQL Server, see
[Auditing in Microsoft SQL Server](DBActivityStreams.md#DBActivityStreams.Overview.SQLServer-auditing "DBActivityStreams.md#DBActivityStreams.Overview.SQLServer-auditing")

###### Topics

- [Support for SQL Server Audit](#Appendix.SQLServer.Options.Audit.Support "#Appendix.SQLServer.Options.Audit.Support")
- [Adding SQL Server Audit to the DB instance options](Appendix.SQLServer.Options.Audit.md "Appendix.SQLServer.Options.Audit.md")
- [Using SQL Server Audit](Appendix.SQLServer.Options.Audit.md "Appendix.SQLServer.Options.Audit.md")
- [Viewing audit logs](Appendix.SQLServer.Options.Audit.md "Appendix.SQLServer.Options.Audit.md")
- [Using SQL Server Audit with Multi-AZ instances](#Appendix.SQLServer.Options.Audit.Multi-AZ "#Appendix.SQLServer.Options.Audit.Multi-AZ")
- [Configuring an S3 bucket](Appendix.SQLServer.Options.Audit.md "Appendix.SQLServer.Options.Audit.md")
- [Manually creating an IAM role for SQL Server Audit](Appendix.SQLServer.Options.Audit.md "Appendix.SQLServer.Options.Audit.md")

## Support for SQL Server Audit

In Amazon RDS, starting with SQL Server 2016, all editions of SQL Server support server-level
audits, and the Enterprise edition also supports database-level audits. Starting
with SQL Server 2016 (13.x) SP1, all editions support both server-level and
database-level audits. For more information, see [SQL Server Audit (database engine)](https://docs.microsoft.com/sql/relational-databases/security/auditing/sql-server-audit-database-engine "https://docs.microsoft.com/sql/relational-databases/security/auditing/sql-server-audit-database-engine") in the SQL Server
documentation.

RDS supports configuring the following option settings for SQL Server Audit.

| Option setting       | Valid values                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `IAM_ROLE_ARN`       | A valid Amazon Resource Name (ARN) in the format<br>`arn:aws:iam::*`account-id`*:role/*`role-name`*`.                | The ARN of the IAM role that grants access to the S3 bucket where you want to store<br>your audit logs. For more information, see<br>[Amazon Resource Names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-iam "../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-iam") in the _AWS General Reference._ |
| `S3_BUCKET_ARN`      | A valid ARN in the format `arn:aws:s3:::`amzn-s3-demo-bucket`` or<br>`arn:aws:s3:::`amzn-s3-demo-bucket`/key-prefix` | The ARN for the S3 bucket where you want to store your audit<br>logs.                                                                                                                                                                                                                                                                            |
| `ENABLE_COMPRESSION` | `true` or `false`                                                                                                    | Controls audit log compression. By default, compression is enabled (set<br>to `true`).                                                                                                                                                                                                                                                           |
| `RETENTION_TIME`     | `0` to `840`                                                                                                         | The retention time (in hours) that SQL Server audit records are kept on<br>your RDS instance. By default, retention is disabled.                                                                                                                                                                                                                 |

## Using SQL Server Audit with Multi-AZ instances

For Multi-AZ instances, the process for sending audit log files to Amazon S3 is similar to the
process for Single-AZ instances. However, there are some important differences:

- Database audit specification objects are replicated to all nodes.
- Server audits and server audit specifications aren't replicated to secondary
  nodes. Instead, you have to create or modify them manually.

To capture server audits or a server audit specification from both nodes:

1. Create a server audit or a server audit specification on the primary node.
2. Fail over to the secondary node and create a server audit or a server audit
   specification with the same name and GUID on the secondary node. Use the
   `AUDIT_GUID` parameter to specify the GUID.
