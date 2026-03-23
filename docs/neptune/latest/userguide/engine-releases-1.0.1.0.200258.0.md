# Amazon Neptune Engine Updates 2018-11-08

**Version:** 1.0.1.0.200258.0

Amazon Neptune 1.0.1.0.200258.0 is generally available. All new Neptune DB clusters, including
those restored from snapshots, will be created in Neptune 1.0.1.0.200258.0 after the engine update
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

Neptune DB clusters will automatically be upgraded to engine release 1.0.1.0.200258.0 during
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

- Added support for [SPARQL query hints](sparql-query-hints.md "sparql-query-hints.md").
- Improved performance for SPARQL FILTER (NOT) Exists queries.
- Improved performance for SPARQL DESCRIBE queries.
- Improved performance for the repeat until pattern in Gremlin.
- Improved performance for adding edges in Gremlin.
- Fixed an issue where SPARQL Update DELETE queries could fail in some
  cases.
- Fixed an issue for handling timeouts with the Gremlin WebSocket
  server.
