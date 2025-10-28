# Amazon Neptune Engine Updates 2018-07-24

**Version:** 1.0.1.0.200236.0

Amazon Neptune 1.0.1.0.200236.0 is generally available. All new Neptune DB clusters, including
those restored from snapshots, will be created in Neptune 1.0.1.0.200236.0 after the engine update
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

Neptune DB clusters will automatically be upgraded to engine release 1.0.1.0.200236.0 during
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

- Updated the SPARQL serialization for the `xsd:string` datatype.
  xsd:string is no longer included in JSON serialization, which is now consistent
  with other output formats.
- Fixed handling of `xsd:double`/`xsd:float` infinity.
  `-INF`, `NaN`, and `INF` values are now
  properly recognized and handled in all SPARQL data loader formats, SPARQL 1.1
  UPDATE, and SPARQL 1.1 Query.
- Fixed an issue where a Gremlin query with empty string values fail
  unexpectedly.
- Fixed an issue where Gremlin `aggregate()` and `cap()`
  on an empty graph fails unexpectedly.
- Fixed an issue where incorrect error responses are returned for Gremlin when
  the cardinality specification is invalid, e.g.
  `.property(set,id,'10')` and
  `.property(single,id,'10')`.
- Fixed an issue where invalid Gremlin syntax was returned as an
  InternalFailureException.
- Fixed the spelling in `TimeLimitExceeededException` to
  `TimeLimitExceededException`, in error messages.
- Changed the SPARQL and GREMLIN endpoints respond in a consistent way when
  no script is supplied.
- Clarified error messages for too many concurrent requests.
