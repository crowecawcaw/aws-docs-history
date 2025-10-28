# Creating a DB cluster that uses Aurora PostgreSQL Limitless Database

You create a new Aurora DB cluster using the Limitless Database version of Aurora PostgreSQL, and add a DB shard group to the cluster. When adding a DB shard
group, you specify the maximum compute capacity for the entire DB shard group (sum of the capacities for all routers and shards) in Aurora capacity units
(ACUs). Each ACU is a combination of approximately 2 gibibytes (GiB) of memory, corresponding CPU, and networking. Scaling increases or decreases
capacity for your DB shard group, depending on your application workload, similar to how [Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md") works.

###### Topics

- [Correlating DB shard group maximum capacity with the number of routers and shards created](#limitless-capacity-mapping "#limitless-capacity-mapping")
- [Creating your DB cluster](limitless-create-cluster.md "limitless-create-cluster.md")

## Correlating DB shard group maximum capacity with the number of routers and shards created

The initial number of routers and shards in a DB shard group is determined by the maximum capacity that you set when you create the DB shard
group. The higher the maximum capacity, the greater the number of routers and shards that are created in the DB shard group.

Each node (shard or router) has its own current capacity value, also measured in ACUs.

- Limitless Database scales a node up to a higher capacity when its current capacity is too low to handle the load. However, nodes won't scale up
  when the total capacity is at the maximum.
- Limitless Database scales the node down to a lower capacity when its current capacity is higher than needed. However, nodes won't scale down
  when the total capacity is at the minimum.

The following table shows the correlation between the DB shard group maximum capacity in Aurora capacity units (ACUs) and the number of nodes
(routers and shards) created.

###### Note

These values are subject to change.

If you set the compute redundancy to a nonzero value, the total number of shards will be doubled or tripled. This will incur extra costs.

The nodes in compute standbys are scaled up and down to the same capacity as the writer. You don't set the capacity range separately for the standbys.

| Total nodes | Routers | Shards | Default minimum capacity (ACUs) | Maximum capacity range (ACUs) |
| ----------- | ------- | ------ | ------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4           | 2       | 2      | 16                              | 16–400                        |
| 5           | 2       | 3      | 20                              | 401–500                       |
| 6           | 2       | 4      | 24                              | 501–600                       |
| 7           | 3       | 4      | 28                              | 601–700                       |
| 8           | 3       | 5      | 32                              | 701–800                       |
| 9           | 3       | 6      | 36                              | 801–900                       |
| 10          | 4       | 6      | 40                              | 901–1000                      |
| 11          | 4       | 7      | 44                              | 1001–1100                     |
| 12          | 4       | 8      | 48                              | 1101–1200                     |
| 13          | 5       | 8      | 52                              | 1201–1300                     |
| 14          | 5       | 9      | 56                              | 1301–1400                     |
| 15          | 5       | 10     | 60                              | 1401–1500                     |
| 16          | 6       | 10     | 64                              | 1501–1600                     |
| 17          | 6       | 11     | 68                              | 1601–1700                     |
| 18          | 6       | 12     | 72                              | 1701–1800                     |
| 19          | 7       | 12     | 76                              | 1801–1900                     |
| 20          | 7       | 13     | 80                              | 1901–2000                     |
| 21          | 7       | 14     | 84                              | 2001–2100                     |
| 22          | 8       | 14     | 88                              | 2101–2200                     |
| 23          | 8       | 15     | 92                              | 2201–2300                     |
| 24          | 8       | 16     | 96                              | 2301–6144                     | Maximum capacity–based dynamic configuration for the DB shard group is available only during creation. The number of routers and shards remains the same when the maximum capacity is modified. For more information, see [Changing the capacity of a DB shard group](limitless-capacity.md "limitless-capacity.md"). You can use SQL commands to add shards and routers to a DB shard group. For more information, see the following: <br>• [Splitting a shard in a DB shard group](limitless-shard-split.md "limitless-shard-split.md") <br>• [Adding a router to a DB shard group](limitless-add-router.md "limitless-add-router.md") ###### Note You can't delete shards or routers. |
