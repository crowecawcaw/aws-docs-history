

# Amazon Neptune Engine Version 1.0.2.2.R2 (2020-04-02)
<a name="engine-releases-1.0.2.2.R2"></a>

As of 2020-04-02, engine version 1.0.2.2.R2 is being generally deployed. Please note that it takes several days for a new release to become available in every region.

## Improvements in This Engine Release
<a name="engine-releases-1.0.2.2.R2-improvements"></a>
+ You can now queue up to 64 bulk-load jobs, rather than having to wait for one to finish before initiating the next one. You can also make execution of a queued load request contingent on the successful completion of one or more previously queued load jobs using the `dependencies` parameter of the `load` command. See [Neptune Loader Command](load-api-reference-load.md).
+ Full-text-search output can now be sorted (see [Full-text search parameters](full-text-search-parameters.md)).
+ There is now a DB cluster parameter for invoking Neptune streams, and the feature has been moved out of Lab Mode. See [Enabling Neptune Streams](streams-using-enabling.md).

## Defects Fixed in This Engine Release
<a name="engine-releases-1.0.2.2.R2-defects"></a>
+ Fixed a stochastic failure in server startup which delayed instance creation.
+ Fixed an optimizer issue where `BIND` statements in the query made the optimizer start out with unselective patterns in join-order planning.

## Query-Language Versions Supported in This Release
<a name="engine-releases-1.0.2.2.R2-query-versions"></a>

Before upgrading a DB cluster to version 1.0.2.2.R2, make sure that your project is compatible with these query-language versions:
+ *Gremlin version:* `3.4.3`
+ *SPARQL version:* `1.1`

## Upgrade Paths to Engine Release 1.0.2.2.R2
<a name="engine-releases-1.0.2.2.R2-upgrade-paths"></a>

Your cluster will be upgraded to this patch release automatically during your next maintenance window if you are running engine version `1.0.2.2`.

You can manually upgrade any previous Neptune engine release to this release.

## Upgrading to This Release
<a name="engine-releases-1.0.2.2.R2-upgrading"></a>

Amazon Neptune 1.0.2.2.R2 is now generally available.

If a DB cluster is running an engine version from which there is an upgrade path to this release, it is eligible to be upgraded now. You can upgrade any eligible cluster using the DB cluster operations on the console or by using the SDK. The following CLI command will upgrade an eligible cluster immediately:

For Linux, OS X, or Unix:

```
1. aws neptune modify-db-cluster \
2.     --db-cluster-identifier {{(your-neptune-cluster)}} \
3.     --engine-version 1.0.2.2 \
4.     --apply-immediately
```

For Windows:

```
1. aws neptune modify-db-cluster ^
2.     --db-cluster-identifier {{(your-neptune-cluster)}} ^
3.     --engine-version 1.0.2.2 ^
4.     --apply-immediately
```

Updates are applied to all instances in a DB cluster simultaneously. An update requires a database restart on those instances, so you will experience downtime ranging from 20–30 seconds to several minutes, after which you can resume using the DB cluster.

### Always test before you upgrade
<a name="engine-1.0.2.2.R2-test-before-upgrading"></a>

When a new major or minor Neptune engine version is released, always test your Neptune applications on it first before upgrading to it. Even a minor upgrade could introduce new features or behavior that would affect your code.

Start by comparing the release notes pages from your current version to those of the targeted version to see if there will be changes in query language versions or other breaking changes.

The best way to test a new version before upgrading your production DB cluster is to clone your production cluster so that the clone is running the new engine version. You can then run queries on the clone without affecting the production DB cluster.

### Always create a manual snapshot before you upgrade
<a name="engine-1.0.2.2.R2-snapshot-before-upgrading"></a>

Before performing an upgrade, we strongly recommend that you always create a manual snapshot of your DB cluster. Having an automatic snapshot only offers short-term protection, whereas a manual snapshot remains available until you explicitly delete it.

In certain cases Neptune creates a manual snapshot for you as a part of the upgrade process, but you should not rely on this, and should create your own manual snapshot in any case.

When you are certain that you won't need to revert your DB cluster to its pre-upgrade state, you can explicitly delete the manual snapshot that you created yourself, as well as the manual snapshot that Neptune might have created. If Neptune creates a manual snapshot, it will have a name that begins with `preupgrade`, followed by the name of your DB cluster, the source engine version, the target engine version, and the date.

**Note**  
If you are trying to upgrade while [a pending action is in process](manage-console-maintaining), you may encounter an error such as the following:  

```
   We're sorry, your request to modify DB cluster (cluster identifier) has failed.
   Cannot modify engine version because instance (instance identifier) is
   running on an old configuration. Apply any pending maintenance actions on the instance before
   proceeding with the upgrade.
```
If you encounter this error, wait for the pending action to finish, or trigger a maintenance window immediately to let the previous upgrade complete.

For more information about upgrading your engine version, see [Maintaining your Amazon Neptune DB Cluster](cluster-maintenance.md). If you have any questions or concerns, the AWS Support team is available on the community forums and through [AWS Premium Support](http://aws.amazon.com/support).