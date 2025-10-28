# Connecting to your DB cluster using IAM authentication with the AWS drivers

The AWS suite of drivers has been designed to provide support for faster
switchover and failover times, and authentication with AWS Secrets Manager, AWS Identity and Access Management (IAM),
and Federated Identity. The AWS drivers rely on monitoring DB cluster
status and being aware of the cluster topology to determine the new writer.
This approach reduces switchover and failover times to single-digit seconds,
compared to tens of seconds for open-source drivers.

For more information on the AWS drivers, see the
corresponding language driver for your [Aurora MySQL](Aurora.md#Aurora.Connecting.JDBCDriverMySQL "Aurora.md#Aurora.Connecting.JDBCDriverMySQL") or [Aurora PostgreSQL](Aurora.md#Aurora.Connecting.AuroraPostgreSQL.Utilities "Aurora.md#Aurora.Connecting.AuroraPostgreSQL.Utilities")
DB cluster.
