

# Connecting to your DB instance using IAM authentication with the AWS drivers
<a name="IAMDBAuth.Connecting.Drivers"></a>

The AWS suite of drivers has been designed to provide support for faster switchover and failover times, and authentication with AWS Secrets Manager, AWS Identity and Access Management (IAM), and Federated Identity. The AWS drivers rely on monitoring DB instance status and being aware of the instance topology to determine the new writer. This approach reduces switchover and failover times to single-digit seconds, compared to tens of seconds for open-source drivers.

For more information on the AWS drivers, see the corresponding language driver for your [RDS for MariaDB](MariaDB.Connecting.Drivers.md#MariaDB.Connecting.JDBCDriver), [RDS for MySQL](MySQL.Connecting.Drivers.md#MySQL.Connecting.JDBCDriver), or [RDS for PostgreSQL](PostgreSQL.Connecting.JDBCDriver.md) DB instance.

**Note**  
The only features supported for RDS for MariaDB are authentication with AWS Secrets Manager, AWS Identity and Access Management (IAM), and Federated Identity.