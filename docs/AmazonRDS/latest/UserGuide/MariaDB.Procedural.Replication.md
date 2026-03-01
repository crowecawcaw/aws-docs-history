# Configuring GTID-based replication with an external source instance

You can set up replication based on global transaction identifiers (GTIDs) from an
external MariaDB instance of version 10.0.24 or higher into an RDS for MariaDB DB instance.
Follow these guidelines when you set up an external source instance and a replica on
Amazon RDS:

- Monitor failover events for the RDS for MariaDB DB instance that is your replica. If a
  failover occurs, then the DB instance that is your replica might be recreated on
  a new host with a different network address. For information on how to monitor
  failover events, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").
- Maintain the binary logs (binlogs) on your source instance until you have verified that they
  have been applied to the replica. This maintenance ensures that you can restore
  your source instance in the event of a failure.
- Turn on automated backups on your MariaDB DB instance on Amazon RDS. Turning on automated backups
  ensures that you can restore your replica to a particular point in time if you
  need to resynchronize your source instance and replica. For information on
  backups and Point-In-Time Restore, see [Backing up, restoring, and exporting data](CHAP_CommonTasks.md "CHAP_CommonTasks.md").

###### Note

The permissions required to start replication on a MariaDB DB instance
are restricted and not available to your Amazon RDS master user. Because of this, you
must use the Amazon RDS [mysql.rds_set_external_master_gtid](mysql_rds_set_external_master_gtid.md "mysql_rds_set_external_master_gtid.md") and [mysql.rds_start_replication](mysql-stored-proc-replicating.md#mysql_rds_start_replication "mysql-stored-proc-replicating.md#mysql_rds_start_replication") commands to set up replication
between your live database and your RDS for MariaDB database.

To start replication between an external source instance
and a MariaDB DB instance on Amazon RDS,
use the following procedure.

###### To start replication

1. Make the source MariaDB instance read-only:

```
mysql> FLUSH TABLES WITH READ LOCK;
mysql> SET GLOBAL read_only = ON;
```

2. Get the current GTID of the external MariaDB instance. You can do this by
   using `mysql` or the query editor of your choice to run `SELECT
@@gtid_current_pos;`.

The GTID is formatted as
`<domain-id>-<server-id>-<sequence-id>`. A
typical GTID looks something like `0-1234510749-1728`. For
more information about GTIDs and their component parts, see [Global
transaction ID](http://mariadb.com/kb/en/mariadb/global-transaction-id/ "http://mariadb.com/kb/en/mariadb/global-transaction-id/") in the MariaDB documentation. 3. Copy the database from the external MariaDB instance to the MariaDB DB
instance using `mysqldump`. For very large databases, you might want
to use the procedure in [Importing data to an Amazon RDS for MariaDB DB instance with reduced downtime](mariadb-importing-data-reduced-downtime.md "mariadb-importing-data-reduced-downtime.md").

For Linux, macOS, or Unix:

```
mysqldump \
    --databases `database_name` \
    --single-transaction \
    --compress \
    --order-by-primary \
    -u `local_user` \
    -p`local_password` | mysql \
        --host=hostname \
        --port=3306 \
        -u `RDS_user_name` \
        -p`RDS_password`
```

For Windows:

```
mysqldump ^
    --databases `database_name` ^
    --single-transaction ^
    --compress ^
    --order-by-primary \
    -u `local_user` \
    -p`local_password` | mysql ^
        --host=hostname ^
        --port=3306 ^
        -u `RDS_user_name` ^
        -p`RDS_password`
```

###### Note

Make sure that there isn't a space between the `-p` option and the entered password.

Specify a password other than the prompt shown here as a security best practice.

Use the `--host`, `--user (-u)`, `--port`
and `-p` options in the `mysql` command to specify the
host name, user name, port, and password to connect to your MariaDB DB
instance. The host name is the DNS name from the MariaDB DB instance
endpoint, for example `myinstance.123456789012.us-east-1.rds.amazonaws.com`. You can
find the endpoint value in the instance details in the Amazon RDS Management Console. 4. Make the source MariaDB instance writeable again.

```
mysql> SET GLOBAL read_only = OFF;
mysql> UNLOCK TABLES;
```

5. In the Amazon RDS Management Console, add the IP address of the server
   that hosts the external MariaDB database to the VPC security group for the
   MariaDB DB instance. For more information on modifying a VPC
   security group, go to [Security groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the _Amazon Virtual Private Cloud User Guide_.

The IP address can change when the following conditions are met:

    * You are using a public IP address for communication between the external source instance and the DB instance.
    * The external source instance was stopped and restarted.

If these conditions are met, verify the IP address before adding it.

You might also need to configure your local network to permit connections
from the IP address of your MariaDB DB instance, so that it can
communicate with your external MariaDB instance. To find the IP address of the
MariaDB DB instance, use the `host` command.

```
host `db_instance_endpoint`
```

The host name is the DNS name from the MariaDB DB instance endpoint. 6. Using the client of your choice, connect to the external MariaDB instance
and create a MariaDB user to be used for replication. This account is used
solely for replication and must be restricted to your domain to improve
security. The following is an example.

```
CREATE USER '`repl_user`'@'`mydomain.com`' IDENTIFIED BY '`password`';
```

###### Note

Specify a password other than the prompt shown here as a security best practice. 7. For the external MariaDB instance, grant `REPLICATION CLIENT`
and `REPLICATION SLAVE` privileges to your replication user. For
example, to grant the `REPLICATION CLIENT` and `REPLICATION
 SLAVE` privileges on all databases for the '`repl_user`'
user for your domain, issue the following command.

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO '`repl_user`'@'`mydomain.com`';
```

8. Make the MariaDB DB instance the replica. Connect to the MariaDB DB instance
   as the master user and identify the external MariaDB database as the replication
   source instance by using the [mysql.rds_set_external_master_gtid](mysql_rds_set_external_master_gtid.md "mysql_rds_set_external_master_gtid.md") command. Use the GTID
   that you determined in Step 2. The following is an example.

```
CALL mysql.rds_set_external_master_gtid ('`mymasterserver.mydomain.com`', 3306, '`repl_user`', '`password`', '`GTID`', `1`);
```

###### Note

Specify a password other than the prompt shown here as a security best
practice. 9. On the MariaDB DB instance, issue the [mysql.rds_start_replication](mysql-stored-proc-replicating.md#mysql_rds_start_replication "mysql-stored-proc-replicating.md#mysql_rds_start_replication") command to start replication.

```
CALL mysql.rds_start_replication;
```
