# Working with high availability features for RDS Custom for Oracle

RDS Custom for Oracle provides built-in high availability through Multi-AZ deployments. Alternatively, you can use Oracle Data Guard as a customer-managed option based on your use cases.

## Multi-AZ deployments

(fully-managed)

With Multi-AZ deployments for RDS Custom for Oracle, Amazon RDS automatically provisions and
maintains a synchronous standby replica in a different Availability Zone (AZ). The
primary DB instance is synchronously replicated across AZs to a standby replica for data
redundancy. Multi-AZ deployment is supported in both the Enterprise Edition and the
Standard Edition 2. See [Managing a Multi-AZ deployment for RDS Custom for Oracle](custom-oracle-multiaz.md "custom-oracle-multiaz.md") for details.

## Oracle Data Guard

(customer-managed)

Alternatively, you can achieve high availability by manually configuring Oracle
Data Guard to replicate data between RDS Custom for Oracle DB instances. The primary DB instance
automatically synchronizes data to the standby instances. Oracle Data Guard is supported
only in the Enterprise Edition.

You can configure your high availability environment in the following ways:

- Configure standby instances in different AZs to be resilient to AZ
  failures.
- Place your standby databases in mounted or read-only mode. Read-only mode
  requires an Oracle Active Data Guard license.
- Fail over or switch over from the primary database to a standby database with no data loss.
- Migrate data by configuring high availability for your on-premises
  instance, and then failing over or switching over to the RDS Custom for Oracle standby
  database.

To learn how to configure Oracle Data Guard for high availability, see the AWS blog [Build high availability for RDS Custom for Oracle using read replicas](https://aws.amazon.com/blogs/database/build-high-availability-for-amazon-rds-custom-for-oracle-using-read-replicas/ "https://aws.amazon.com/blogs/database/build-high-availability-for-amazon-rds-custom-for-oracle-using-read-replicas/"). You can perform the following tasks:

- Use a virtual private network (VPN) tunnel to encrypt data in transit for
  your high availability instances. Encryption in transit isn't configured
  automatically by RDS Custom for Oracle.
- Configure Oracle Fast-Failover Observer (FSFO) to monitor your high availability instances.
- Allow the observer to perform automatic failover when necessary conditions are met.
