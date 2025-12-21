# Enabling

GTID-based replication for new read replicas for RDS for MySQL

When GTID-based replication is enabled for an RDS for MySQL DB instance, GTID-based
replication is configured automatically for read replicas of the DB instance.

###### To enable GTID-based replication for new read replicas

1.  Make sure that the parameter group associated with the DB instance has the
    following parameter settings:

        * `gtid_mode` – `ON` or `ON_PERMISSIVE`
        * `enforce_gtid_consistency` – `ON`

    For more information about setting configuration parameters using parameter groups, see
    [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

2.  If you changed the parameter group of the DB instance, reboot the DB
    instance. For more information on how to do so, see [Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md").
3.  Create one or more read replicas of the DB instance. For more information on
    how to do so, see [Creating a read replica](USER_ReadRepl.md "USER_ReadRepl.md").
    Amazon RDS attempts to establish GTID-based replication between the MySQL DB instance and
    the read replicas using the `MASTER_AUTO_POSITION`. If the attempt fails,
    Amazon RDS uses log file positions for replication with the read replicas. For more
    information about the `MASTER_AUTO_POSITION`, see [GTID auto-positioning](https://dev.mysql.com/doc/refman/5.7/en/replication-gtids-auto-positioning.html "https://dev.mysql.com/doc/refman/5.7/en/replication-gtids-auto-positioning.html") in the MySQL documentation.
