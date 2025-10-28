# Amazon Neptune Engine Updates 2019-05-01

**Version:** 1.0.1.0.200296.0

Amazon Neptune 1.0.1.0.200296.0 is generally available. All new Neptune DB clusters, including
those restored from snapshots, will be created in Neptune 1.0.1.0.200296.0 after the engine update
is complete for that Region.

Existing clusters can be upgraded to this release immediately using the DB cluster operations
on the console or by using the SDK. You can use the following CLI command to upgrade a DB cluster
to this release immediately:

```
aws neptune apply-pending-maintenance-action \
    --apply-action system-update \
    --opt-in-type immediate \
    --resource-identifier arn:aws:rds:`<region>`:`<account number>`:`<resourcetype>`:`<name>`
```

Neptune DB clusters will automatically be upgraded to engine release 1.0.1.0.200296.0 during
system maintenance windows. The timing of when updates are applied depends on the Region and
maintenance window setting for the DB cluster, as well as on the type of update.

###### Note

The instance maintenance window does not apply to engine updates.

Updates are applied to all instances in a DB cluster simultaneously. An update requires
a database restart on all instances in a DB cluster, so you will experience downtime ranging
from 20–30 seconds to several minutes, after which you can resume using your DB cluster
or clusters. You can view or change your maintenance window settings on the [Neptune console](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").

If you have any questions or concerns, the AWS Support team is available on the community forums and through
[AWS Premium Support](http://aws.amazon.com/support "http://aws.amazon.com/support").

## Improvements

- Added the new `explain` feature to Neptune SPARQL queries to help you visualize
  the query plan and take steps to optimize it if necessary. For information, see [SPARQL explain](sparql-explain.md "sparql-explain.md").
- Improved SPARQL performance and reporting in various ways.
- Improved Gremlin performance and behavior in various ways.
- Improved the timing-out of long-running `drop( )` queries.
- Improved the performance of `otherV( )` queries.
- Added two fields to the information returned when you query the
  Neptune health status of a DB cluster or instance, namely the engine version number
  and the cluster or instance start time. See [Instance Status](access-graph-status.md "access-graph-status.md").
- The Neptune loader `Get-Status` API now returns a `startTime` field
  that records when a load job started.
- The loader command now takes an optional `parallelism` parameter
  that lets you restrict the number of threads the loader uses.
