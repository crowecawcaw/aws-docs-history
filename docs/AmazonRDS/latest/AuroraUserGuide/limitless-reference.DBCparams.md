

# DB cluster parameters in Aurora PostgreSQL Limitless Database
<a name="limitless-reference.DBCparams"></a>

You can use the following DB cluster parameters to configure Aurora PostgreSQL Limitless Database.

**rds\_aurora.limitless\_adaptive\_fetch\_size**  
Enhances batch prefetching. When set to `true`, this parameter allows a self-adjusting (adaptive) fetch size for prefetching. When set to `false`, the fetch size is constant.

**rds\_aurora.limitless\_auto\_scale\_options**  
Sets the options available for adding routers or splitting shards in a DB shard group. The value can be `add_router`, `split_shard`, or both.  
For more information, see [Adding a router to a DB shard group](limitless-add-router.md) and [Splitting a shard in a DB shard group](limitless-shard-split.md).

**rds\_aurora.limitless\_distributed\_deadlock\_timeout**  
The amount of time to wait on a lock before checking whether there is a distributed deadlock condition, in milliseconds. The default is `1000` (1 second).  
For more information, see [Distributed deadlocks in Aurora PostgreSQL Limitless Database](limitless-query.deadlocks.md).

**rds\_aurora.limitless\_enable\_auto\_scale**  
Enables the adding of routers and splitting of shards in a DB shard group.  
For more information, see [Adding a router to a DB shard group](limitless-add-router.md) and [Splitting a shard in a DB shard group](limitless-shard-split.md).

**rds\_aurora.limitless\_finalize\_split\_shard\_mode**  
Determines how system-initiated shard splits are finalized. For more information, see [Splitting a shard in a DB shard group](limitless-shard-split.md).

**rds\_aurora.limitless\_maximum\_adaptive\_fetch\_size**  
Sets the upper limit for the adaptive fetch size. The range is `1`–`INT_MAX`. The default is `1000`.