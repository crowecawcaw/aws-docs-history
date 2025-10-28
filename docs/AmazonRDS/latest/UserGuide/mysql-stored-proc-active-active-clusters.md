# Managing active-active clusters

The following stored procedures set up and manage RDS for MySQL active-active clusters. For more information, see [Configuring active-active clusters for RDS for MySQL](mysql-active-active-clusters.md "mysql-active-active-clusters.md").

These stored procedures are only available with RDS for MySQL DB instances running the
following versions:

- All MySQL 8.4 versions
- MySQL 8.0.35 and higher minor versions

###### Topics

- [mysql.rds_group_replication_advance_gtid](#mysql_rds_group_replication_advance_gtid "#mysql_rds_group_replication_advance_gtid")
- [mysql.rds_group_replication_create_user](#mysql_rds_group_replication_create_user "#mysql_rds_group_replication_create_user")
- [mysql.rds_group_replication_set_recovery_channel](#mysql_rds_group_replication_set_recovery_channel "#mysql_rds_group_replication_set_recovery_channel")
- [mysql.rds_group_replication_start](#mysql_rds_group_replication_start "#mysql_rds_group_replication_start")
- [mysql.rds_group_replication_stop](#mysql_rds_group_replication_stop "#mysql_rds_group_replication_stop")

## mysql.rds_group_replication_advance_gtid

Creates placeholder GTIDs on the current DB instance.

### Syntax

```
CALL mysql.rds_group_replication_advance_gtid(
`begin_id`
, `end_id`
, `server_uuid`
);
```

### Parameters

`begin_id`

The start transaction ID to be created.

`end_id`

The end transaction ID to be created.

`begin_id`

The `group_replication_group_name` for the transaction to be created. The
`group_replication_group_name` is specified as a UUID in the DB parameter
group associated with the DB instance.

### Usage notes

In an active-active cluster, for a DB instance to join a group, all GTID transactions executed on the new DB instance must
exist on the other members in the cluster. In unusual cases, a new DB instance might have more transactions when transactions are
executed before joining the instance to group. In this case, you can't remove any existing transactions, but you can use this
procedure to create the corresponding placeholder GTIDs on the othe DB instances in the group. Before doing so, verify that
the transactions _don't affect the replicated data_.

When you call this procedure, GTID transactions of `server_uuid:begin_id-end_id` are created with empty content.
To avoid replication issues, don't use this procedure under any other conditions.

###### Important

Avoid calling this procedure when the active-active cluster is functioning normally. Don't call this procedure unless
you understand the possible consequences of the transactions you are creating. Calling this procedure might result in
inconsistent data.

### Example

The following example creates placeholder GTIDs on current DB instance.:

```
CALL mysql.rds_group_replication_advance_gtid(`5`, `6`, '`11111111-2222-3333-4444-555555555555`');
```

## mysql.rds_group_replication_create_user

Creates the replication user `rdsgrprepladmin` for group replication on the DB instance.

### Syntax

```
CALL mysql.rds_group_replication_create_user(
`replication_user_password`
);
```

### Parameters

`replication_user_password`

The password of the replication user `rdsgrprepladmin`.

### Usage notes

- The password of the replication user `rdsgrprepladmin` must be the same on all of the DB instances in
  an active-active cluster.
- The `rdsgrprepladmin` user name is reserved for group replication connections. No other user, including the master user, can
  have this user name.

### Example

The following example creates the replication user `rdsgrprepladmin` for group replication on the DB instance:

```
CALL mysql.rds_group_replication_create_user('`password`');
```

## mysql.rds_group_replication_set_recovery_channel

Sets the `group_replication_recovery` channel for an active-active cluster. The procedure uses the
reserved `rdsgrprepladmin` user to configure the channel.

### Syntax

```
CALL mysql.rds_group_replication_set_recovery_channel(
`replication_user_password`);
```

### Parameters

`replication_user_password`

The password of the replication user `rdsgrprepladmin`.

### Usage notes

The password of the replication user `rdsgrprepladmin` must be the same on all of the DB instances in
an active-active cluster. A call to the `mysql.rds_group_replication_create_user` specifies
the password.

### Example

The following example sets the `group_replication_recovery` channel for an active-active cluster:

```
CALL mysql.rds_group_replication_set_recovery_channel('`password`');
```

## mysql.rds_group_replication_start

Starts group replication on the current DB instance.

### Syntax

```
CALL mysql.rds_group_replication_start(
`bootstrap`
);
```

### Parameters

`bootstrap`

A value that specifies whether to initialize a new group or join an existing group.
`1` initializes a new group with the current DB instance. `0` joins the
current DB instance to an existing group by connecting to the endpoints defined in
`group_replication_group_seeds` parameter in the of DB parameter group associated
with the DB instance.

### Example

The following example initializes a new group with the current DB instance:

```
CALL mysql.rds_group_replication_start(`1`);
```

## mysql.rds_group_replication_stop

Stops group replication on the current DB instance.

### Syntax

```
CALL mysql.rds_group_replication_stop();
```

### Usage notes

When you stop replication on a DB instance, it doesn't affect any other DB instance in the
active-active cluster.
