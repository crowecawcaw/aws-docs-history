# On-Demand DB instances for Amazon RDS

Amazon RDS on-demand DB instances are billed based on the class of the DB instance (for example, db.t3.small or db.m5.large). For Amazon RDS
pricing information, see the [Amazon RDS product page](https://aws.amazon.com/rds/pricing "https://aws.amazon.com/rds/pricing").

Billing starts for a DB instance as soon as the DB instance is available. Pricing is
listed on a per-hour basis, but bills are calculated down to the second and show times in
decimal form. Amazon RDS usage is billed in one-second increments, with a minimum of 10 minutes.
In the case of billable configuration change, such as scaling compute or storage capacity,
you're charged a 10-minute minimum. Billing continues until the DB instance terminates,
which occurs when you delete the DB instance or if the DB instance fails.

If you no longer want to be charged for your DB instance, you must stop or delete it to avoid being
billed for additional DB instance hours. For more information about the DB
instance states for which you are billed, see [Viewing Amazon RDSDB instance status](accessing-monitoring.md#Overview.DBInstance.Status "accessing-monitoring.md#Overview.DBInstance.Status").

## Stopped DB instances

While your DB instance is stopped, you're charged for provisioned storage,
including Provisioned IOPS. You are also charged for backup storage, including storage
for manual snapshots and automated backups within your specified retention window. You
aren't charged for DB instance hours.

## Multi-AZ DB instances

A Multi-AZ setup enhances data durability and availability by automatically
provisioning and maintaining a synchronous standby replica in a different Availability
Zone. Due to the additional resources and increased availability, Multi-AZ deployments
are priced higher than Single-AZ deployments, and can cost approximately twice as much
due to the additional standby instance and associated resources.

Consider the following important details about Multi-AZ pricing:

- **Compute costs**: Billed per DB instance-hour
  for both the primary and standby instances.
- **Storage costs**: Charged per GB-month for the
  storage provisioned for both the primary and standby instances.
- **Data transfer costs**: Replication between the
  primary and standby instances is included in the cost, but other data transfer
  charges might apply based on your usage.

To accurately estimate your monthly costs based on your specific use case and
AWS Region, you can use the AWS Pricing Calculator. This tool lets you to input your configuration
details and provides a comprehensive cost breakdown.

###### Note

Pricing is subject to change. See the [Amazon RDS Pricing page](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/") for
the most up-to-date information.
