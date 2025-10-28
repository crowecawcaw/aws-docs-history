# Monitoring active-active clusters

Monitoring active-active clusters in Amazon RDS for MySQL is crucial for tracking
performance, replication integrity, and node synchronization. You can monitor your
active-active cluster by connecting to a DB instance in the cluster, and running the
following SQL command:

```
SELECT * FROM performance_schema.replication_group_members;
```

Your output should show `ONLINE` for the `MEMBER_STATE` of each DB instance, as in the
following sample output:

````
+---------------------------+--------------------------------------+----------------+-------------+--------------+-------------+----------------+----------------------------+
| CHANNEL_NAME              | MEMBER_ID                            | MEMBER_HOST    | MEMBER_PORT | MEMBER_STATE | MEMBER_ROLE | MEMBER_VERSION | MEMBER_COMMUNICATION_STACK | +---------------------------+--------------------------------------+----------------+-------------+--------------+-------------+----------------+----------------------------+
| group_replication_applier | 9854d4a2-5d7f-11ee-b8ec-0ec88c43c251 | ip-10-15-3-137 |        3306 | ONLINE       | PRIMARY     | 8.0.35         | MySQL                      |
| group_replication_applier | 9e2e9c28-5d7f-11ee-8039-0e5d58f05fef | ip-10-15-3-225 |        3306 | ONLINE       | PRIMARY     | 8.0.35         | MySQL                      |
| group_replication_applier | a6ba332d-5d7f-11ee-a025-0a5c6971197d | ip-10-15-1-83  |        3306 | ONLINE       | PRIMARY     | 8.0.35         | MySQL                      | +---------------------------+--------------------------------------+----------------+-------------+--------------+-------------+----------------+----------------------------+ 3 rows in set (0.00 sec) ``` For information about the possible `MEMBER_STATE` values, see [Group Replication Server States](https://dev.mysql.com/doc/refman/8.0/en/group-replication-server-states.html "https://dev.mysql.com/doc/refman/8.0/en/group-replication-server-states.html") in the MySQL documentation.
````
