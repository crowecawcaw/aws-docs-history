# Amazon Neptune Engine Version 1.0.4.2.R3 (2021-06-28)

As of 2021-06-28, engine version 1.0.4.2.R3 is being generally deployed. Please note
that it takes several days for a new release to become available in every region.

## Known issues in this engine release

**Issue:**

A SPARQL bug that fails to honor media type in an `Accept` header if
there are spaces present.

For example, a query with `-H "Accept: text/csv; q=1.0, */*; q=0.1"`
returns JSON output rather than CSV output.

**Workaround:**

If you remove the spaces in the `Accept` clause in the header, the engine
returns output in the correct requested format. In other words, instead of
`-H "Accept: text/csv; q=1.0, */*; q=0.1"` , use:

```
  -H "Accept: text/csv;q=1.0,*/*;q=0.1"
```

## Defects Fixed in This Engine Release

- Fixed a bug in clearing the lookup cache on replicas after a fast reset.

## Query-Language Versions Supported in This Release

Before upgrading a DB cluster to version 1.0.4.2.R3, make sure that your project is compatible
with these query-language versions:

- _Gremlin version:_ `3.4.10`
- _SPARQL version:_ `1.1`

## Upgrade Paths to Engine Release 1.0.4.2.R3

This patch release is optional unless your DB cluster is using one or more `R5d`
instances. If your cluster has `R5d` instances, it will automatically be upgraded
in the next maintenance window. Otherwise, it will not automatically be upgraded to this
patch release.

You can upgrade release `1.0.4.2.R2` to this `1.0.4.2.R3` release
manually using the AWS CLI [apply-pending-maintenance-action](../../../cli/latest/reference/neptune/apply-pending-maintenance-action.md "../../../cli/latest/reference/neptune/apply-pending-maintenance-action.md")
command (the [ApplyPendingMaintenanceAction](api-other-apis.md#ApplyPendingMaintenanceAction "api-other-apis.md#ApplyPendingMaintenanceAction") API).
