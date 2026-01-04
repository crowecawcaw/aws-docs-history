# Scaling reads for your MySQL database with Amazon Aurora

You can use Amazon Aurora with your MySQL DB instance to take advantage of the read scaling capabilities of Amazon Aurora and
expand the read workload for your MySQL DB instance. To use Aurora to scale reads for your MySQL DB instance, create an
Amazon Aurora MySQL DB cluster and make it a read replica of your MySQL DB instance. This applies to an RDS for MySQL DB instance,
or a MySQL database running external to Amazon RDS.

For information on creating an Amazon Aurora DB cluster, see [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

When you set up replication between your MySQL DB instance and your Amazon Aurora DB cluster, be sure to follow these
guidelines:

- Use the Amazon Aurora DB cluster endpoint address when you reference your Amazon Aurora MySQL DB cluster. If a failover
  occurs, then the Aurora Replica that is promoted to the primary instance for the Aurora MySQL DB cluster continues to
  use the DB cluster endpoint address.
- Maintain the binlogs on your writer instance until you have verified that they have been applied to the Aurora
  Replica. This maintenance ensures that you can restore your writer instance in the event of a failure.

###### Important

When using self-managed replication, you're responsible for monitoring and resolving any replication issues that
may occur. For more information, see [Diagnosing and resolving lag
between read replicas](CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL.ReplicaLag "CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL.ReplicaLag").

###### Note

The permissions required to start replication on an Aurora MySQL DB cluster are
restricted and not available to your Amazon RDS master user. Therefore, you must use
the [mysql.rds_set_external_master (Aurora MySQL version 2)](mysql-stored-proc-replicating.md#mysql_rds_set_external_master "mysql-stored-proc-replicating.md#mysql_rds_set_external_master") or [mysql.rds_set_external_source (Aurora MySQL version 3)](mysql-stored-proc-replicating.md#mysql_rds_set_external_source "mysql-stored-proc-replicating.md#mysql_rds_set_external_source") and [mysql.rds_start_replication](mysql-stored-proc-replicating.md#mysql_rds_start_replication "mysql-stored-proc-replicating.md#mysql_rds_start_replication") procedures to set up
replication between your Aurora MySQL DB cluster and your MySQL DB
instance.

## Start replication between an external source instance

and an Aurora MySQL DB cluster

1. Make the source MySQL DB instance read-only:

```
`mysql>` FLUSH TABLES WITH READ LOCK;
`mysql>` SET GLOBAL read_only = ON;

```

2. Run the `SHOW MASTER STATUS` command on the source MySQL
   DB instance to determine the binlog location. You receive output similar
   to the following example:

```
File                        Position
------------------------------------
 mysql-bin-changelog.000031      107
------------------------------------

```

3. Copy the database from the external MySQL DB instance to the
   Amazon Aurora MySQL DB cluster using `mysqldump`. For very large
   databases, you might want to use the procedure in [Importing data to an Amazon RDS for MySQL database with reduced
   downtime](../UserGuide/mysql-importing-data-reduced-downtime.md "../UserGuide/mysql-importing-data-reduced-downtime.md") in the _Amazon Relational Database Service User
   Guide_.

For Linux, macOS, or Unix:

```
mysqldump \
    --databases <database_name> \
    --single-transaction \
    --compress \
    --order-by-primary \
    -u `local_user` \
    -p `local_password` | mysql \
        --host aurora_cluster_endpoint_address \
        --port 3306 \
        -u `RDS_user_name` \
        -p `RDS_password`
```

For Windows:

```
mysqldump ^
    --databases <database_name> ^
    --single-transaction ^
    --compress ^
    --order-by-primary ^
    -u `local_user` ^
    -p `local_password` | mysql ^
        --host aurora_cluster_endpoint_address ^
        --port 3306 ^
        -u `RDS_user_name` ^
        -p `RDS_password`
```

###### Note

Make sure that there is not a space between the `-p`
option and the entered password.

Use the `--host`, `--user (-u)`,
`--port` and `-p` options in the
`mysql` command to specify the hostname, user name, port,
and password to connect to your Aurora DB cluster. The host name is the
DNS name from the Amazon Aurora DB cluster endpoint, for example,
`mydbcluster.cluster-123456789012.us-east-1.rds.amazonaws.com`.
You can find the endpoint value in the cluster details in the Amazon RDS
Management Console. 4. Make the source MySQL DB instance writeable again:

```
`mysql>` SET GLOBAL read_only = OFF;
`mysql>` UNLOCK TABLES;

```

For more information on making backups for use with replication, see
[Backing up a source or replica by making it read
only](http://dev.mysql.com/doc/refman/8.0/en/replication-solutions-backups-read-only.html "http://dev.mysql.com/doc/refman/8.0/en/replication-solutions-backups-read-only.html") in the MySQL documentation. 5. In the Amazon RDS Management Console, add the IP address of the server that
hosts the source MySQL database to the VPC security group for the
Amazon Aurora DB cluster. For more information on modifying a VPC security
group, see [Security
groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the _Amazon Virtual Private Cloud User
Guide_.

You might also need to configure your local network to permit
connections from the IP address of your Amazon Aurora DB cluster, so that it
can communicate with your source MySQL instance. To find the IP address
of the Amazon Aurora DB cluster, use the `host` command.

```
host `aurora_endpoint_address`
```

The host name is the DNS name from the Amazon Aurora DB cluster
endpoint. 6. Using the client of your choice, connect to the external MySQL
instance and create a MySQL user to be used for replication. This
account is used solely for replication and must be restricted to your
domain to improve security. The following is an example.

```
CREATE USER '`repl_user`'@'`example.com`' IDENTIFIED BY '`password`';
```

7. For the external MySQL instance, grant `REPLICATION CLIENT`
   and `REPLICATION SLAVE` privileges to your replication user.
   For example, to grant the `REPLICATION CLIENT` and
   `REPLICATION SLAVE` privileges on all databases for the
   '`repl_user`' user for your domain, issue the following
   command.

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO '`repl_user`'@'`example.com`'
    IDENTIFIED BY '`password`';
```

8. Take a manual snapshot of the Aurora MySQL DB cluster to be the read
   replica before setting up replication. If you need to reestablish
   replication with the DB cluster as a read replica, you can restore the
   Aurora MySQL DB cluster from this snapshot instead of having to import the
   data from your MySQL DB instance into a new Aurora MySQL DB
   cluster.
9. Make the Amazon Aurora DB cluster the replica. Connect to the Amazon Aurora DB
   cluster as the master user and identify the source MySQL database as the
   replication source by using the [mysql.rds_set_external_master (Aurora MySQL version 2)](mysql-stored-proc-replicating.md#mysql_rds_set_external_master "mysql-stored-proc-replicating.md#mysql_rds_set_external_master") or [mysql.rds_set_external_source (Aurora MySQL version 3)](mysql-stored-proc-replicating.md#mysql_rds_set_external_source "mysql-stored-proc-replicating.md#mysql_rds_set_external_source") and [mysql.rds_start_replication](mysql-stored-proc-replicating.md#mysql_rds_start_replication "mysql-stored-proc-replicating.md#mysql_rds_start_replication") procedures.

Use the binlog file name and position that you determined in Step 2.
The following is an example.

```
For Aurora MySQL version 2:
CALL mysql.rds_set_external_master ('mymasterserver.example.com', 3306,
    'repl_user', 'password', 'mysql-bin-changelog.000031', 107, 0);

For Aurora MySQL version 3:
CALL mysql.rds_set_external_source ('mymasterserver.example.com', 3306,
    'repl_user', 'password', 'mysql-bin-changelog.000031', 107, 0);

```

10. On the Amazon Aurora DB cluster, call the [mysql.rds_start_replication](mysql-stored-proc-replicating.md#mysql_rds_start_replication "mysql-stored-proc-replicating.md#mysql_rds_start_replication") procedure to start
    replication.

```
CALL mysql.rds_start_replication;
```

After you have established replication between your source MySQL DB instance and your Amazon Aurora DB cluster, you can
add Aurora Replicas to your Amazon Aurora DB cluster. You can then connect to the Aurora Replicas to read scale your data. For
information on creating an Aurora Replica, see [Adding Aurora Replicas to a DB cluster](aurora-replicas-adding.md "aurora-replicas-adding.md").
