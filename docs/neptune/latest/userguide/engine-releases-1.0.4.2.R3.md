

# Amazon Neptune Engine Version 1.0.4.2.R3 (2021-06-28)
<a name="engine-releases-1.0.4.2.R3"></a>

As of 2021-06-28, engine version 1.0.4.2.R3 is being generally deployed. Please note that it takes several days for a new release to become available in every region.

## Known issues in this engine release
<a name="engine-releases-1.0.4.2.R3-known-issues"></a>

**Issue:**

A SPARQL bug that fails to honor media type in an `Accept` header if there are spaces present.

For example, a query with ` -H "Accept: text/csv; q=1.0, */*; q=0.1" ` returns JSON output rather than CSV output.

**Workaround:**

If you remove the spaces in the `Accept` clause in the header, the engine returns output in the correct requested format. In other words, instead of ` -H "Accept: text/csv; q=1.0, */*; q=0.1" `, use:

```
  -H "Accept: text/csv;q=1.0,*/*;q=0.1"
```

## Defects Fixed in This Engine Release
<a name="engine-releases-1.0.4.2.R3-defects"></a>
+ Fixed a bug in clearing the lookup cache on replicas after a fast reset.

## Query-Language Versions Supported in This Release
<a name="engine-releases-1.0.4.2.R3-query-versions"></a>

Before upgrading a DB cluster to version 1.0.4.2.R3, make sure that your project is compatible with these query-language versions:
+ *Gremlin version:* `3.4.10`
+ *SPARQL version:* `1.1`

## Upgrade Paths to Engine Release 1.0.4.2.R3
<a name="engine-releases-1.0.4.2.R3-upgrade-paths"></a>

This patch release is optional unless your DB cluster is using one or more `R5d` instances. If your cluster has `R5d` instances, it will automatically be upgraded in the next maintenance window. Otherwise, it will not automatically be upgraded to this patch release.

You can upgrade release `1.0.4.2.R2` to this `1.0.4.2.R3` release manually using the AWS CLI [apply-pending-maintenance-action](https://docs.aws.amazon.com/cli/latest/reference/neptune/apply-pending-maintenance-action.html) command (the [ApplyPendingMaintenanceAction](api-other-apis.md#ApplyPendingMaintenanceAction) API).