# How to change the partitioner in Amazon Keyspaces

You can change the partitioner by using the AWS Management Console or Cassandra Query Language
(CQL).

AWS Management Console

###### To change the partitioner using the Amazon Keyspaces console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose
   **Configuration**.
3. On the **Configuration** page, go to
   **Edit partitioner**.
4. Select the partitioner compatible with your version of Cassandra. The partitioner change takes approximately 10 minutes to apply.

###### Note

After the configuration change is complete, you have to disconnect and reconnect to Amazon Keyspaces for requests to use the new partitioner.

Cassandra Query Language (CQL)

1. To see which partitioner is configured for the account, you can use the following query.

```
SELECT partitioner from system.local;
```

If the partitioner hasn't been changed, the query has the following output.

```
`partitioner
--------------------------------------------
com.amazonaws.cassandra.DefaultPartitioner`
```

2. To update the partitioner to the `Murmur3` partitioner, you can use the following
   statement.

```
UPDATE system.local set partitioner='org.apache.cassandra.dht.Murmur3Partitioner' where key='local';
```

3. Note that this configuration change takes approximately 10 minutes to complete. To confirm that the partitioner has been set,
   you can run the `SELECT` query again. Note that due to eventual read consistency,
   the response might not reflect the results of the recently completed partitioner change yet. If you repeat the `SELECT`
   operation again after a short time, the response should return the latest data.

```
SELECT partitioner from system.local;
```

###### Note

You have to disconnect and reconnect to Amazon Keyspaces so that requests use the new partitioner.
