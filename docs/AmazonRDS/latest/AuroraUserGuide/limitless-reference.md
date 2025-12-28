# DB cluster parameters in Aurora PostgreSQL Limitless Database

You can use the following DB cluster parameters to configure Aurora PostgreSQL Limitless Database.

**rds_aurora.limitless_adaptive_fetch_size**

Enhances batch prefetching. When set to `true`, this parameter allows a self-adjusting (adaptive) fetch size for
prefetching. When set to `false`, the fetch size is constant.

**rds_aurora.limitless_auto_scale_options**

Sets the options available for adding routers or splitting shards in a DB shard group. The value can be `add_router`,
`split_shard`, or both.

For more information, see [Adding a router to a DB shard group](limitless-add-router.md "limitless-add-router.md") and [Splitting a shard in a DB shard group](limitless-shard-split.md "limitless-shard-split.md").

**rds_aurora.limitless_distributed_deadlock_timeout**

The amount of time to wait on a lock before checking whether there is a distributed deadlock condition, in milliseconds. The default
is `1000` (1 second).

For more information, see [Distributed deadlocks in Aurora PostgreSQL Limitless Database](limitless-query.md "limitless-query.md").

**rds_aurora.limitless_enable_auto_scale**

Enables the adding of routers and splitting of shards in a DB shard group.

For more information, see [Adding a router to a DB shard group](limitless-add-router.md "limitless-add-router.md") and [Splitting a shard in a DB shard group](limitless-shard-split.md "limitless-shard-split.md").

**rds_aurora.limitless_finalize_split_shard_mode**

Determines how system-initiated shard splits are finalized. For more information, see [Splitting a shard in a DB shard group](limitless-shard-split.md "limitless-shard-split.md").

**rds_aurora.limitless_maximum_adaptive_fetch_size**

Sets the upper limit for the adaptive fetch size. The range is `1`–`INT_MAX`. The default is
`1000`.
