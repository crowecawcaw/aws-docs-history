# Amazon EBS fast snapshot restore volume creation credits

The number of volumes that receive the full performance benefit of fast snapshot
restore is determined by the volume creation credits for the snapshot. There is one
credit bucket per snapshot per Availability Zone. Each volume that you create from a
snapshot with fast snapshot restore enabled consumes one credit from the credit bucket.
You must have at least one credit in the bucket to create an initialized volume from
the snapshot. If you create a volume but there is less than one credit in the bucket,
the volume is created without benefit of fast snapshot restore.

When you enable fast snapshot restore for a snapshot that is shared with you, you
get a separate credit bucket for the shared snapshot in your account. If you create
volumes from the shared snapshot, the credits are consumed from your credit bucket;
they are not consumed from the snapshot owner's credit bucket.

The credit bucket size and the refill rate are based on the size of the snapshot
(which is also the size of the source volume), not the size of the snapshot data. For
example, if you create a snapshot from a 200 GiB volume that has 150 GiB of data, and
enable it for fast snapshot restore, the credit bucket size and the refill rate are
based on 200 GiB.

When you enable fast snapshot restore for a snapshot, the credit bucket starts
with zero credits, and it gets filled at a set rate until it reaches its maximum
credit capacity. Also, as you consume credits, the credit bucket is refilled over
time until it reaches its maximum credit capacity.

The fill rate for a credit bucket is calculated as follows:

```
MIN (10, (1024 ÷ `snapshot_size_gib`))
```

And the size of the credit bucket is calculated as follows:

```
MAX (1, MIN (10, (1024 ÷ `snapshot_size_gib`)))
```

**For example**, if you enable fast snapshot restore
for a snapshot with a size of `128 GiB`, the fill rate is `0.1333`
credits per minute.

```
MIN (10, (1024 ÷ `128`))
 = MIN (10, 8)
 = 8 credits per hour
 = 0.1333 credits per minute
```

And the maximum size of the credit bucket is `8` credits.

```
MAX (1, MIN (10, (1024 ÷ `128`)))
 = MAX (1, MIN (10, 8))
 = MAX (1, 8)
 = 8 credits
```

In this example, when you enable fast snapshot restore, the credit bucket starts
with zero credits. After 8 minutes, the credit bucket has enough credits to create
one initialized volume (`0.1333 credits × 8 minutes = 1.066 credits`).
When the credit bucket is full, you can create 8 initialized volumes simultaneously
(8 credits). When the bucket is below its maximum capacity, it refills with
`0.1333` credits per minute.

You can use CloudWatch metrics to monitor the size of your credit buckets and
the number of credits available in each bucket. For more information, see [Metrics for fast snapshot restore](using_cloudwatch_ebs.md#fast-snapshot-restore-metrics "using_cloudwatch_ebs.md#fast-snapshot-restore-metrics").

After you create a volume from a snapshot with fast snapshot restore enabled,
you can describe the volume using [describe-volumes](../../../cli/latest/reference/ec2/describe-volumes.md "../../../cli/latest/reference/ec2/describe-volumes.md") and check the `fastRestored` field in the
output to determine whether the volume was created as an initialized volume using
fast snapshot restore.
