# Creating a parallel query DB cluster in Aurora MySQL

To create an Aurora MySQL cluster with parallel query, add new instances to it, or
perform other administrative operations, you use the same AWS Management Console and AWS CLI techniques that
you do with other Aurora MySQL clusters. You can create a new cluster to work with parallel
query. You can also create a DB cluster to work with parallel query by restoring from a
snapshot of a MySQL-compatible Aurora DB cluster. If you aren't familiar with the process for
creating a new Aurora MySQL cluster, you can find background information and prerequisites in
[Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

When you choose an Aurora MySQL engine version, we recommend that you choose the latest one available. Currently, all available Aurora MySQL versions
support parallel query. You have more flexibility to turn parallel query on and off, or use parallel query with existing clusters, if you use the latest
versions.

Whether you create a new cluster or restore from a snapshot, you use the same techniques to add new DB
instances that you do with other Aurora MySQL clusters.

You can create a parallel query cluster using the Amazon RDS console or the AWS CLI.

###### Contents

- [Creating a parallel query cluster using the console](aurora-mysql-parallel-query-creating-cluster.md#aurora-mysql-parallel-query-creating-cluster-console "aurora-mysql-parallel-query-creating-cluster.md#aurora-mysql-parallel-query-creating-cluster-console")
- [Creating a parallel query cluster using the CLI](aurora-mysql-parallel-query-creating-cluster.md#aurora-mysql-parallel-query-creating-cluster-cli "aurora-mysql-parallel-query-creating-cluster.md#aurora-mysql-parallel-query-creating-cluster-cli")

## Creating a parallel query cluster using the console

You can create a new parallel query cluster with the console as described following.

###### To create a parallel query cluster with the AWS Management Console

1. Follow the general AWS Management Console procedure in [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").
2. For **Engine type**, choose Aurora MySQL.
3. For **Additional configuration**, choose a parameter group that you created for **DB cluster
   parameter group**. Using such a custom parameter group is required for Aurora MySQL 2.09 and higher. In
   your DB cluster parameter group, specify the parameter settings `aurora_parallel_query=ON` and
   `aurora_disable_hash_join=OFF`. Doing so turns on parallel query for the cluster, and turns on the
   hash join optimization that works in combination with parallel query.

###### To verify that a new cluster can use parallel query

1. Create a cluster using the preceding technique.
2. (For Aurora MySQL version 2 or 3) Check that the `aurora_parallel_query` configuration setting is true.

```
`mysql>` select @@aurora_parallel_query;
`+-------------------------+
| @@aurora_parallel_query |
+-------------------------+
| 1 |
+-------------------------+`

```

3. (For Aurora MySQL version 2) Check that the `aurora_disable_hash_join` setting is false.

```
`mysql>` select @@aurora_disable_hash_join;
`+----------------------------+
| @@aurora_disable_hash_join |
+----------------------------+
| 0 |
+----------------------------+`

```

4. With some large tables and data-intensive queries, check the query plans to confirm that some of your
   queries are using the parallel query optimization. To do so, follow the procedure in
   [Verifying which statements use parallel query for Aurora MySQL](aurora-mysql-parallel-query-verifying.md "aurora-mysql-parallel-query-verifying.md").

## Creating a parallel query cluster using the CLI

You can create a new parallel query cluster with the CLI as described following.

###### To create a parallel query cluster with the AWS CLI

1. (Optional) Check which Aurora MySQL versions are compatible with parallel query clusters.
   To do so, use the `describe-db-engine-versions` command and check the
   value of the `SupportsParallelQuery` field. For an example, see
   [Checking Aurora MySQL version compatibility for parallel query](aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-checking-compatibility "aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-checking-compatibility").
2. (Optional) Create a custom DB cluster parameter group with the settings `aurora_parallel_query=ON` and
   `aurora_disable_hash_join=OFF`. Use commands such as the following.

```
aws rds create-db-cluster-parameter-group --db-parameter-group-family aurora-mysql8.0 --db-cluster-parameter-group-name pq-enabled-80-compatible
aws rds modify-db-cluster-parameter-group --db-cluster-parameter-group-name pq-enabled-80-compatible \
  --parameters ParameterName=aurora_parallel_query,ParameterValue=ON,ApplyMethod=pending-reboot
aws rds modify-db-cluster-parameter-group --db-cluster-parameter-group-name pq-enabled-80-compatible \
  --parameters ParameterName=aurora_disable_hash_join,ParameterValue=OFF,ApplyMethod=pending-reboot
```

If you perform this step, specify the option
`--db-cluster-parameter-group-name `my_cluster_parameter_group`` in the subsequent`create-db-cluster` statement. Substitute the name of your own parameter group.
If you omit this step, you create the parameter group and associate it with the cluster later, as described in
[Turning parallel query on and
off in Aurora MySQL](aurora-mysql-parallel-query-enabling.md "aurora-mysql-parallel-query-enabling.md"). 3. Follow the general AWS CLI procedure in [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md"). 4. Specify the following set of options:

    * For the `--engine` option, use `aurora-mysql`. These values produce parallel query clusters that
     are compatible with MySQL 5.7 or 8.0.
    * For the `--db-cluster-parameter-group-name` option, specify the name of a DB cluster parameter group
     that you created and specified the parameter value `aurora_parallel_query=ON`. If you omit this option,
     you can create the cluster with a default parameter group and later modify it to use such a custom parameter group.
    * For the `--engine-version` option, use an Aurora MySQL version that's compatible with parallel query. Use the procedure from
     [Optimizing parallel query in Aurora MySQL](aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-planning "aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-planning") to get a list of versions if
     necessary.


    The following code example shows how. Substitute your own value for each of
     the environment variables such as `$CLUSTER_ID`. This example also specifies the `--manage-master-user-password` option to generate the master user password and manage it in Secrets Manager.
     For more information, see [Password management with
     Amazon Aurora
     and AWS Secrets Manager](rds-secrets-manager.md "rds-secrets-manager.md").
     Alternatively, you can use the `--master-password` option to specify and manage the password yourself.




    ```
    aws rds create-db-cluster --db-cluster-identifier `$CLUSTER_ID` \
      **--engine aurora-mysql --engine-version 8.0.mysql\_aurora.3.04.1** \
      --master-username `$MASTER_USER_ID` --manage-master-user-password \
      --db-cluster-parameter-group-name `$CUSTOM_CLUSTER_PARAM_GROUP`

    aws rds create-db-instance --db-instance-identifier `${INSTANCE_ID}-1` \
      --engine `same_value_as_in_create_cluster_command` \
      --db-cluster-identifier `$CLUSTER_ID` --db-instance-class `$INSTANCE_CLASS`

    ```

5. Verify that a cluster you created or restored has the parallel query feature available.

Check that the `aurora_parallel_query` configuration setting exists. If this setting has the value 1, parallel
query is ready for you to use. If this setting has the value 0, set it to 1 before you can use parallel query.
Either way, the cluster is capable of performing parallel queries.

```
`mysql>` select @@aurora_parallel_query;
`+------------------------+
| @@aurora_parallel_query|
+------------------------+
| 1 |
+------------------------+`

```

###### To restore a snapshot to a parallel query cluster with the AWS CLI

1. Check which Aurora MySQL versions are compatible with parallel query clusters. To do so, use the `describe-db-engine-versions`
   command and check the value of the `SupportsParallelQuery` field. For an example, see [Checking Aurora MySQL version compatibility for parallel query](aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-checking-compatibility "aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-checking-compatibility"). Decide which
   version to use for the restored cluster.
2. Locate an Aurora MySQL-compatible cluster snapshot.
3. Follow the general AWS CLI procedure in [Restoring from a DB cluster snapshot](aurora-restore-snapshot.md "aurora-restore-snapshot.md").

```
aws rds restore-db-cluster-from-snapshot \
  --db-cluster-identifier `mynewdbcluster` \
  --snapshot-identifier `mydbclustersnapshot` \
  --engine aurora-mysql
```

4. Verify that a cluster you created or restored has the parallel query feature available. Use the same
   verification procedure as in
   Creating a parallel query cluster using the CLI.
