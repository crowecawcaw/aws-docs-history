# Amazon Neptune Engine Updates 2018-11-19

**Version:** 1.0.1.0.200264.0

Amazon Neptune 1.0.1.0.200264.0 is generally available. All new Neptune DB clusters, including
those restored from snapshots, will be created in Neptune 1.0.1.0.200264.0 after the engine update
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

Neptune DB clusters will automatically be upgraded to engine release 1.0.1.0.200264.0 during
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

- Added support for [Gremlin query hints](gremlin-query-hints.md "gremlin-query-hints.md").
- Improved error messages for IAM authentication. For more information, see
  [IAM Authentication Errors](errors-engine-codes.md#errors-iam-auth "errors-engine-codes.md#errors-iam-auth").
- Improved SPARQL query performance with a high number of predicates.
- Improved SPARQL property path performance.
- Improved Gremlin performance for conditional mutations, such as the
  `fold().coalesce(unfold(), …)` pattern, when used with
  `addV()`, `addE()`, and `property()`
  steps.
- Improved Gremlin performance for `by()` and `sack()`
  modulations.
- Improved Gremlin performance for `group()` and
  `groupCount()` steps.
- Improved Gremlin performance for `store()`,
  `sideEffect()`, and `cap().unfold()` steps.
- Improved support for Gremlin single cardinality properties constraints.
  - Improved enforcement of single cardinality for edge properties and
    vertex properties marked as single cardinality properties.
  - Introduced an error if additional property values are specified for an
    existing edge property during Neptune Load jobs.
