

# Adaptive autovacuum enhancements in PostgreSQL version 18
<a name="Appendix.PostgreSQL.CommonDBATasks.Autovacuum.AdaptivePG18"></a>

Starting with RDS for PostgreSQL version 18, Amazon RDS enhances the adaptive autovacuum mechanism to dynamically scale `autovacuum_max_workers` when your DB instance approaches transaction ID wraparound. In earlier PostgreSQL versions, `autovacuum_max_workers` required a restart to change. PostgreSQL 18 makes `autovacuum_max_workers` a dynamic parameter, allowing Amazon RDS to adjust it without a restart.

PostgreSQL 18 also introduces a new parameter, `autovacuum_worker_slots`, which reserves backend process slots for autovacuum workers at server startup. This parameter sets the upper limit on how many autovacuum workers can ever run concurrently – `autovacuum_max_workers` cannot exceed this value. Unlike `autovacuum_max_workers`, `autovacuum_worker_slots` requires a restart to change. For more information, see [`autovacuum_worker_slots`](https://www.postgresql.org/docs/devel/runtime-config-vacuum.html#GUC-AUTOVACUUM-WORKER-SLOTS) in the PostgreSQL documentation.

## How adaptive autovacuum scales workers
<a name="Appendix.PostgreSQL.CommonDBATasks.Autovacuum.AdaptivePG18.ScalingWorkers"></a>

When the [`MaximumUsedTransactionIDs`](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html) CloudWatch metric exceeds 1 billion on a PostgreSQL 18 instance, Amazon RDS increases `autovacuum_max_workers` up to the `autovacuum_worker_slots` value using the following formula, which is also the default formula for the `autovacuum_worker_slots` parameter:

```
LEAST(GREATEST({DBInstanceClassMemory/32185783296}, 16), 32)
```

For small and medium instances (up to 512 GiB of memory), adaptive autovacuum scales to 16 workers. For larger instances, the number of workers scales proportionally with memory up to the maximum of 32. For example, a [db.m5.4xlarge](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.Summary.html) instance (64 GiB) has a default `autovacuum_max_workers` of 3. When `MaximumUsedTransactionIDs` exceeds 1 billion, Amazon RDS scales it to 16 workers.

Amazon RDS never decreases a value that you have already configured. If your configured `autovacuum_max_workers` is already higher than the calculated value, Amazon RDS does not change it.

Each autovacuum worker uses memory up to the `autovacuum_work_mem` setting. When adaptive autovacuum increases the number of workers, the total memory consumed by autovacuum increases proportionally. For example, if `autovacuum_work_mem` is set to 1 GB and adaptive autovacuum scales from 3 to 16 workers, the maximum memory used by autovacuum workers increases from 3 GB to 16 GB.

**Warning**  
Make sure that the combination of worker processes and memory equals the total memory that you want to allocate to autovacuum.

## Monitoring adaptive autovacuum changes
<a name="Appendix.PostgreSQL.CommonDBATasks.Autovacuum.AdaptivePG18.Monitoring"></a>

When Amazon RDS modifies `autovacuum_max_workers` or any other autovacuum parameter, it generates an event for the affected DB instance. You can view these events in the AWS Management Console or through the Amazon RDS API. For more information about RDS events, see [Amazon RDS event categories and event messages](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Messages.html). To receive notifications when these events occur, see [Subscribing to Amazon RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html).

To view the current in-memory autovacuum settings, connect to your DB instance and run the following command:

```
SHOW autovacuum_max_workers;
```

The parameter group values are not changed. Amazon RDS modifies these parameters only in memory on the DB instance. When `MaximumUsedTransactionIDs` drops below the threshold, Amazon RDS resets the parameters to the values in your parameter group and generates another event.