# Monitoring Self-Managed Databases

CloudWatch Database Insights supports monitoring self-managed databases, so you can bring databases that you
run yourself into the same console you use for your Amazon RDS and Amazon Aurora databases. You install
the CloudWatch agent on the database host, and within minutes the database appears in the Database Insights
fleet view with live performance data, including database load (measured as average active
sessions), wait event analysis, and query-level statistics.

Database Insights currently supports PostgreSQL for self-managed databases. The database can run on an
Amazon EC2 instance.

By monitoring self-managed databases alongside your Amazon RDS and Amazon Aurora databases, you can
use a single tool across heterogeneous fleets of managed and self-managed databases, apply
consistent diagnostics, and troubleshoot performance issues from a single console.

Self-managed databases do not use the Standard mode and Advanced mode of Database Insights. Database Insights
retains 15 months of the metrics collected for your self-managed databases. Logs collected by
the agent are stored in CloudWatch Logs and follow the retention setting on the log group they are
delivered to.

Standard pricing for CloudWatch OpenTelemetry metrics and CloudWatch Logs applies. For more
information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

For information about setting up monitoring for a self-managed database, see the following
topics.

###### Topics

- [Monitoring Self-Managed PostgreSQL](Database-Insights-Self-Managed-PostgreSQL.md "Database-Insights-Self-Managed-PostgreSQL.md")
