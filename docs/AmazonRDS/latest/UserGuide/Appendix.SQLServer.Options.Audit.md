

# SQL Server Audit
<a name="Appendix.SQLServer.Options.Audit"></a>

In Amazon RDS, you can audit Microsoft SQL Server databases by using the built-in SQL Server auditing mechanism. You can create audits and audit specifications in the same way that you create them for on-premises database servers. 

RDS uploads the completed audit logs to your S3 bucket, using the IAM role that you provide. If you enable retention, RDS keeps your audit logs on your DB instance for the configured period of time. Additionally, you may also choose to forward them to CloudWatch (log streams) or to both destinations simultaneously.

For more information, see [SQL Server Audit (database engine)](https://docs.microsoft.com/sql/relational-databases/security/auditing/sql-server-audit-database-engine) in the Microsoft SQL Server documentation.

## SQL Server Audit with Database Activity Streams
<a name="Appendix.SQLServer.DAS.Audit"></a>

You can use Database Activity Streams for RDS to integrate SQL Server Audit events with database activity monitoring tools from Imperva, McAfee, and IBM. For more information about auditing with Database Activity Streams for RDS SQL Server, see [Auditing in Microsoft SQL Server](DBActivityStreams.md#DBActivityStreams.Overview.SQLServer-auditing) 

**Topics**
+ [SQL Server Audit with Database Activity Streams](#Appendix.SQLServer.DAS.Audit)
+ [Support for SQL Server Audit](#Appendix.SQLServer.Options.Audit.Support)
+ [Adding SQL Server Audit to the DB instance options](Appendix.SQLServer.Options.Audit.Adding.md)
+ [Using SQL Server Audit](Appendix.SQLServer.Options.Audit.CreateAuditsAndSpecifications.md)
+ [Viewing audit logs](Appendix.SQLServer.Options.Audit.AuditRecords.md)
+ [Using SQL Server Audit with Multi-AZ instances](#Appendix.SQLServer.Options.Audit.Multi-AZ)
+ [Configuring an S3 bucket](Appendix.SQLServer.Options.Audit.S3bucket.md)
+ [Configuring CloudWatch Log Stream](Appendix.SQLServer.Options.Audit.CloudWatch.md)
+ [Manually creating an IAM role for SQL Server Audit](Appendix.SQLServer.Options.Audit.IAM.md)

## Support for SQL Server Audit
<a name="Appendix.SQLServer.Options.Audit.Support"></a>

In Amazon RDS, starting with SQL Server 2016, all editions of SQL Server support server-level audits, and the Enterprise edition also supports database-level audits. Starting with SQL Server 2016 (13.x) SP1, all editions support both server-level and database-level audits. For more information, see [SQL Server Audit (database engine)](https://docs.microsoft.com/sql/relational-databases/security/auditing/sql-server-audit-database-engine) in the SQL Server documentation.

RDS supports configuring the following option settings for SQL Server Audit. 


| Option setting | Valid values | Description | 
| --- | --- | --- | 
| IAM\_ROLE\_ARN | A valid Amazon Resource Name (ARN) in the format arn:aws:iam::account-id:role/role-name. | The ARN of the IAM role that grants access to the S3 bucket where you want to store your audit logs. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam) in the AWS General Reference. | 
| S3\_BUCKET\_ARN | A valid ARN in the format arn:aws:s3:::{{amzn-s3-demo-bucket}} or arn:aws:s3:::{{amzn-s3-demo-bucket}}/key-prefix | The ARN for the S3 bucket where you want to store your audit logs. | 
| ENABLE\_COMPRESSION | true or false | Controls audit log compression. By default, compression is enabled (set to true). | 
| RETENTION\_TIME | 0 to 840 | The retention time (in hours) that SQL Server audit records are kept on your RDS instance. By default, retention is disabled. | 

## Using SQL Server Audit with Multi-AZ instances
<a name="Appendix.SQLServer.Options.Audit.Multi-AZ"></a>

For Multi-AZ instances, the process for sending audit log files to Amazon S3 is similar to the process for Single-AZ instances. However, there are some important differences: 
+ Database audit specification objects are replicated to all nodes.
+ Server audits and server audit specifications aren't replicated to secondary nodes. Instead, you have to create or modify them manually.

To capture server audits or a server audit specification from both nodes:

1. Create a server audit or a server audit specification on the primary node.

1. Fail over to the secondary node and create a server audit or a server audit specification with the same name and GUID on the secondary node. Use the `AUDIT_GUID` parameter to specify the GUID.