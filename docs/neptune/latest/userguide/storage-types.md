# Choosing storage types for Amazon Neptune

Neptune offers two types of storage with a different pricing model:

- **Standard storage**   –  
  Standard storage provides cost-effective database storage for applications
  with moderate to low I/O usage.
- **I/O–Optimized storage**   –  
  With I/O–Optimized storage, available from engine version 1.3.0.0, you pay only for the storage
  and instances you are using. The storage costs are higher than for standard storage, and also the instance
  costs are higher than for standard instances. You pay nothing for the I/O that you use. If your I/O usage is
  high, provisioned IOPs storage can reduce costs significantly.

I/O–Optimized storage is designed to meet the needs of I/O–intensive graph
workloads at a predictable cost. You can only switch
between I/O–Optimized and Standard storage types once per 30 days.

For pricing information about I/O–Optimized storage, see the [Neptune pricing page](https://aws.amazon.com/neptune/pricing/ "https://aws.amazon.com/neptune/pricing/").
The following section describes how to set up I/O–Optimized storage for a
Neptune DB cluster.

## Choosing I/O–Optimized storage for a Neptune DB cluster

By default, Neptune DB clusters use standard storage.You can enable I/O–Optimized storage on a DB cluster
at the time you create it, like this:

Here is an example of how you can enable I/O–Optimized storage when you create a
cluster using the AWS CLI:

```
aws neptune create-db-cluster \
  --db-cluster-identifier `(an ID for the cluster)` \
  --engine neptune \
  --engine-version `(the Neptune engine version)` \
  --storage-type iopt1
```

Then, any instance you create automatically has I/O–Optimized storage enabled:

```
aws neptune create-db-instance \
  --db-cluster-identifier `(the ID of the new cluster)` \
  --db-instance-identifier `(an ID for the new instance)` \
  --engine neptune \
  --db-instance-class `db.r5.large`
```

You can also modify an existing DB cluster to enable I/O–Optimized storage on it,
like this:

```
aws neptune modify-db-cluster \
  --db-cluster-identifier `(the ID of a cluster without I/O–Optimized storage)` \
  --storage-type iopt1 \
  --apply-immediately
```

You can restore a backup snapshot to a DB cluster with I/O–Optimized storage enabled:

```
aws neptune restore-db-cluster-from-snapshot \
  --db-cluster-identifier `(an ID for the restored cluster)` \
  --snapshot-identifier `(the ID of the snapshot to restore from)` \
  --engine neptune \
  --engine-version `(the Neptune engine version)` \
  --storage-type iopt1
```

You can determine whether a cluster is using I/O–Optimized storage using
any `describe-` call. If the I/O–Optimized storage is enabled, the call
returns a storage-type field set to `iop1`.
