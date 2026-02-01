# Amazon Neptune Engine Version 1.0.4.0 (2020-10-12)

As of 2020-10-12, engine version 1.0.4.0 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

## Subsequent Patch Releases for This Release

- [Release: 1.0.4.0.R2 (2021-02-24)](engine-releases-1.0.4.0.md "engine-releases-1.0.4.0.md")

## New Features in This Engine Release

- Added frame-level compression for Gremlin.

## Improvements in This Engine Release

- Amazon Neptune now requires the use of the Secure Sockets Layer (SSL) with the TLSv1.2
  protocol for all connections to Neptune in all regions, using these strong cipher
  suites:

      + `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`
      + `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
      + `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`
      + `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`
      + `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`
      + `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`

  This is true for both REST and WebSocket connections to Neptune, and means that
  you must use HTTPS rather than HTTP when connecting to Neptune in all regions.

Because client connections using HTTP or TLS 1.1 will no longer be supported
anywhere, please make sure that your clients and code have been updated to use
TLS 1.2 and HTTPS before upgrading to this engine release.

###### Important

**Having to use SSL/TLS for all connections to
Neptune can be a breaking change.** It affects your
connections with the Gremlin console, the Gremlin driver, Gremlin Python, .NET,
nodeJs, REST APIs, and also load-balancer connections. If you have been using HTTP
for any or all of these, you must now update the relevant client and drivers and
change your code to use HTTPS or your connections will fail.

A bug in this release has allowed HTTP connections and/or outdated TLS connections
to continue to work for customers who previously set a DB cluster parameter to prevent
enforcement of HTTPS connections. That bug was fixed in patch releases [1.0.4.0.R2](engine-releases-1.0.4.0.md "engine-releases-1.0.4.0.md") and [1.0.4.1.R2](engine-releases-1.0.4.1.md "engine-releases-1.0.4.1.md"), but the fix has caused unexpected
connection failures when the patches are automatically installed.

For this reason, both patches have been reverted, and can only be installed manually,
to give you a chance to update your setup for TLS 1.2.

- Upgraded TinkerPop to version 3.4.8. This is a backwards compatible
  upgrade. See the [TinkerPop
  change log](https://github.com/apache/tinkerpop/blob/master/CHANGELOG.asciidoc#tinkerpop-348-release-date-august-3-2020 "https://github.com/apache/tinkerpop/blob/master/CHANGELOG.asciidoc#tinkerpop-348-release-date-august-3-2020") for what's new.
- Improved performance for the Gremlin `properties()` step.
- Added details about `BindOp` and `MultiplexerOp`
  in explain and profile reports.
- Added data prefetch to improve performance when there are cache misses.
- Added a new `allowEmptyStrings` setting in the bulk loader's
  `parserConfiguration` parameter that allows empty strings to be
  treated as valid property values in CSV loads (see [Neptune Loader Request Parameters](load-api-reference-load.md#load-api-reference-load-parameters "load-api-reference-load.md#load-api-reference-load-parameters")).
- The loader now allows an escaped semicolon in multivalue CSV columns.

## Defects Fixed in This Engine Release

- Fixed a potential Gremlin memory leak related to the `both()` step.
- Fixed a bug where request metrics were missing because an endpoint ending
  in '/' was not being handled correctly.
- Fix a bug that caused replicas to fall behind and restart under heavy
  load when the DFE engine is enabled in lab mode.
- Fixed a bug that prevented the correct error message from being reported
  when a bulk load failed because of an out-of-memory condition.
- Fixed a SPARQL bug where the character encoding was placed in the
  Content-Encoding header in SPARQL query responses. Now `charset` is placed
  in the Content-Type header instead, enabling HTTP clients to recognize the character
  set being used automatically.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.0.4.0, make sure that your project is compatible
with these query-language versions:

- _Gremlin version:_ `3.4.8`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.0.4.0

You can manually upgrade any previous Neptune engine release to this release.

You will not automatically upgrade to this release.

## Upgrading to This Release

Amazon Neptune 1.0.4.0 is now generally available.

If a DB cluster is running an engine version from which there is an upgrade path
to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster
using the DB cluster operations on the console or by using the SDK. The following CLI
command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
aws neptune modify-db-cluster \
    --db-cluster-identifier `(your-neptune-cluster)` \
    --engine-version 1.0.4.0 \
    --apply-immediately
```

For Windows:

```
aws neptune modify-db-cluster ^
    --db-cluster-identifier `(your-neptune-cluster)` ^
    --engine-version 1.0.4.0 ^
    --apply-immediately
```

Updates are applied to all instances in a DB cluster simultaneously. An update requires
a database restart on those instances, so you will experience downtime ranging
from 20–30 seconds to several minutes, after which you can resume using the DB cluster.

### Always test before you upgrade

When a new major or minor Neptune engine version is released, always test your
Neptune applications on it first before upgrading to it. Even a minor upgrade could
introduce new features or behavior that would affect your code.

Start by comparing the release notes pages from your current version to those
of the targeted version to see if there will be changes in query language versions
or other breaking changes.

The best way to test a new version before upgrading your production DB cluster is
to clone your production cluster so that the clone is running the new engine version.
You can then run queries on the clone without affecting the production DB cluster.

### Always create a manual snapshot before you upgrade

Before performing an upgrade, we strongly recommend that you always create
a manual snapshot of your DB cluster. Having an automatic snapshot only offers
short-term protection, whereas a manual snapshot remains available until you
explicitly delete it.

In certain cases Neptune creates a manual snapshot for you as a part of the
upgrade process, but you should not rely on this, and should create your own manual
snapshot in any case.

When you are certain that you won't need to revert your DB cluster to its
pre-upgrade state, you can explicitly delete the manual snapshot that you created
yourself, as well as the manual snapshot that Neptune might have created. If Neptune
creates a manual snapshot, it will have a name that begins with `preupgrade`,
followed by the name of your DB cluster, the source engine version, the target engine
version, and the date.

###### Note

If you are trying to upgrade while [a
pending action is in process](manage-console-maintaining.md "manage-console-maintaining.md"), you may encounter an error such as the
following:

```
   **We're sorry, your request to modify DB cluster (cluster identifier) has failed.**
   Cannot modify engine version because instance (instance identifier) is
   running on an old configuration. Apply any pending maintenance actions on the instance before
   proceeding with the upgrade.
```

If you encounter this error, wait for the pending action to finish, or trigger
a maintenance window immediately to let the previous upgrade complete.

For more information about upgrading your engine version, see [Maintaining your Amazon Neptune DB Cluster](cluster-maintenance.md "cluster-maintenance.md"). If you have any questions or concerns, the AWS Support
team is available on the community forums and through [AWS Premium Support](http://aws.amazon.com/support "http://aws.amazon.com/support").
