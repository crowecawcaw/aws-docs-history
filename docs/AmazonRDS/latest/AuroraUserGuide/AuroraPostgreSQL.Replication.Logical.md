# Setting up logical replication for your Aurora PostgreSQL DB cluster

Setting up logical replication requires `rds_superuser` privileges. Your
Aurora PostgreSQL DB cluster must be configured to use a custom DB cluster parameter group
so that you can set the necessary parameters as detailed in the procedure following. For
more information, see [DB cluster parameter groups for Amazon Aurora DB clusters](USER_WorkingWithDBClusterParamGroups.md "USER_WorkingWithDBClusterParamGroups.md").

###### To set up PostgreSQL logical replication for an Aurora PostgreSQL DB cluster

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose your Aurora PostgreSQL DB cluster.
3. Open the **Configuration** tab. Among the Instance details,
   find the **Parameter group** link with **DB cluster
   parameter group** for **Type**.
4. Choose the link to open the custom parameters associated with your
   Aurora PostgreSQL DB cluster.
5. In the **Parameters** search field, type `rds` to
   find the `rds.logical_replication` parameter. The default value for
   this parameter is `0`, meaning that it's turned off by default.
6. Choose **Edit parameters** to access the property values, and
   then choose `1` from the selector to turn on the feature. Depending
   on your expected usage, you might also need to change the settings for the
   following parameters. However, in many cases, the default values are sufficient.
   - `max_replication_slots` – Set this parameter to a
     value that's at least equal to your planned total number of logical
     replication publications and subscriptions. If you are using AWS DMS, this
     parameter should equal at least your planned change data capture tasks
     from the cluster, plus logical replication publications and
     subscriptions.
   - `max_wal_senders` and
     `max_logical_replication_workers` – Set these
     parameters to a value that's at least equal to the number of
     logical replication slots that you intend to be active, or the number of
     active AWS DMS tasks for change data capture. Leaving a logical
     replication slot inactive prevents the vacuum from removing obsolete
     tuples from tables, so we recommend that you monitor replication slots
     and remove inactive slots as needed.
   - `max_worker_processes` – Set this parameter to a
     value that's at least equal to the total of the
     `max_logical_replication_workers`,
     `autovacuum_max_workers`, and
     `max_parallel_workers` values. On small DB instance
     classes, background worker processes can affect application workloads,
     so monitor the performance of your database if you set
     `max_worker_processes` higher than the default value.
     (The default value is the result of
     `GREATEST(${DBInstanceVCPU*2},8}`, which means that, by
     default, this is either 8 or twice the CPU equivalent of the DB instance
     class, whichever is greater).

###### Note

You can modify parameter values in a customer-created DB parameter group.
you can't change the parameter values in a default DB parameter
group. 7. Choose **Save changes**. 8. Reboot the writer instance of your Aurora PostgreSQL DB cluster so that your
changes takes effect. In the Amazon RDS console, choose the primary DB instance of
the cluster and choose **Reboot** from the
**Actions** menu. 9. When the instance is available, you can verify that logical replication is
turned on, as follows.

    1. Use `psql` to connect to the writer instance of your
     Aurora PostgreSQL DB cluster.



    ```
    psql --host=`your-db-cluster-instance-1`.`aws-region`.rds.amazonaws.com --port=5432 --username=`postgres` --password --dbname=`labdb`
    ```
    2. Verify that logical replication has been enabled by using the
     following command.



    ```
    `labdb=>` `SHOW rds.logical_replication;`
     `rds.logical_replication
    -------------------------
     on
    (1 row)`
    ```
    3. Verify that the `wal_level` is set to `logical`.



    ```
    `labdb=>` `SHOW wal_level;`
     `wal_level
    -----------
     logical
    (1 row)`
    ```

For an example of using logical replication to keep a database table synchronized with
changes from a source Aurora PostgreSQL DB cluster, see [Example: Using logical replication with Aurora PostgreSQL DB clusters](AuroraPostgreSQL.Replication.Logical.md "AuroraPostgreSQL.Replication.Logical.md").
