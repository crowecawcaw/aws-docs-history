# Limitations of Multi-AZ DB clusters for Amazon RDS

A Multi-AZ DB cluster has a writer DB instance and two reader DB instances in three separate Availability Zones.
Multi-AZ DB clusters provide high availability, increased capacity for read workloads, and lower latency
when compared to Multi-AZ deployments. For more information about Multi-AZ DB clusters, see [Multi-AZ DB cluster deployments for Amazon RDS](multi-az-db-clusters-concepts.md "multi-az-db-clusters-concepts.md").

The following limitations apply to Multi-AZ DB clusters.

- Multi-AZ DB clusters don't support the following features:
  - IPv6 connections (dual-stack mode)
  - Cross-Region automated backups
  - Kerberos authentication
  - Modifying the port. As an alternative, you can restore a Multi-AZ DB cluster to a point in time and
    specify a different port.
  - Option groups
  - Point-in-time-recovery (PITR) for deleted clusters
  - Storage autoscaling by setting the maximum allocated storage. As an alternative, you can
    scale storage manually.
  - Stopping and starting the Multi-AZ DB cluster
  - Copying a snapshot of a Multi-AZ DB cluster
  - Encrypting an unencrypted Multi-AZ DB cluster

- RDS for MySQL Multi-AZ DB clusters support only the following system stored procedures:
  - `mysql.rds_rotate_general_log`
  - `mysql.rds_rotate_slow_log`
  - `mysql.rds_show_configuration`
  - `mysql.rds_set_external_master_with_auto_position`
  - `mysql.rds_set_configuration`

- RDS for PostgreSQL Multi-AZ DB clusters don't support the following extensions: `aws_s3` and
  `pg_transport`.
- RDS for PostgreSQL Multi-AZ DB clusters don't support using a custom DNS server for outbound network
  access.
