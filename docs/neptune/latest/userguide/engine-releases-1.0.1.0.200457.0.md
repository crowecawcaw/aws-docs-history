# Amazon Neptune Engine Updates 2019-09-19

## IMPORTANT: THIS ENGINE VERSION IS NOW DEPRECATED

No new instances using this engine version will be created, beginning 2021-04-27.

**Version:** 1.0.1.0.200457.0

Amazon Neptune 1.0.1.0.200457.0 is generally available. All new Neptune DB clusters, including
those restored from snapshots, will be created in Neptune 1.0.1.0.200457.0 after the engine update
is complete for that Region.

Existing clusters can be upgraded to this release immediately using the DB cluster operations
on the console or by using the SDK. You can use the following CLI command to upgrade a DB cluster:

```
aws neptune apply-pending-maintenance-action \
    --apply-action system-update \
    --opt-in-type immediate \
    --resource-identifier arn:aws:rds:`<region>`:`<account number>`:`<resourcetype>`:`<name>`
```

Updates are applied to all instances in a DB cluster simultaneously. An update requires
a database restart on all instances in a DB cluster, so you will experience downtime ranging
from 20–30 seconds to several minutes, after which you can resume using your DB cluster
or clusters. You can view or change your maintenance window settings on the [Neptune console](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").

If you have any questions or concerns, the AWS Support team is available on the
community forums and through [AWS Premium
Support](http://aws.amazon.com/support "http://aws.amazon.com/support").

## Defects Fixed in This Engine Release

- Fixed a Gremlin correctness issue introduced in the previous engine release
  (1.0.1.0.200369.0) by removing the performance improvement to conjunctive predicate handling
  that caused it.
- Fixed a SPARQL bug that caused queries with `DISTINCT` and a single
  pattern wrapped into `OPTIONAL` to generate an `InternalServerError`.
