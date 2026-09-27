

# Troubleshooting OpenSearch Dashboards
<a name="dashboards-troubleshooting"></a>

This section describes known issues that can cause OpenSearch Dashboards to become unavailable, fail to load, or behave unexpectedly. Each issue includes the actions you can take to resolve it yourself. Dashboards runs on the hot data nodes in your domain and stores its state (index patterns, visualizations, and dashboards) in the OpenSearch Dashboards index. As a result, most Dashboards availability issues trace back to cluster health, storage, an OpenSearch Dashboards index migration, a cluster or Dashboards setting, resource limits, or the domain's service software version.

Each issue is organized as **Symptom** (what you see and how to confirm it), **Root cause**, **How to mitigate** (self-service steps), and **Suggested action** (how to prevent it from recurring).

**Note**  
Many known Dashboards issues are already resolved in a newer service software release. Before you troubleshoot further, open the Amazon OpenSearch Service console (the AWS console for the service, not the OpenSearch Dashboards UI), check the **Notifications** panel, and install the latest available service software update. Several sections below list this as the recommended action. If a configuration change or upgrade is already in progress, wait for it to finish before you install an update.

## Dashboards is stuck at "server is not ready yet" (HTTP 503 not ready error)
<a name="dashboards-troubleshooting-not-ready"></a>

Symptom  
Dashboards displays `OpenSearch Dashboards server is not ready yet` (an HTTP 503 not ready error) and doesn't finish loading. Dashboards shows this page whenever it hasn't finished starting up. A brief version is normal during a restart, upgrade, or blue/green deployment and clears on its own. Treat it as a problem when it persists. To narrow down the cause, check the domain's **Cluster health** and whether a configuration change or upgrade is in progress:  
+ If a change or upgrade is in progress, the message is usually transient; wait for the domain to return to **Active**.
+ If cluster health is red, Dashboards can't start because it depends on the cluster; resolve the cluster issue first (see [Related cluster and access issues](#dashboards-troubleshooting-related)).
+ If the message persists while cluster health is green, the OpenSearch Dashboards index migration is most likely blocked (described below).

Root cause  
Dashboards reports "server is not ready yet" until all of its core services finish initializing, which is why a transient version of the message is expected during startup and blue/green deployments. When it persists with a green cluster, the most common cause is that the migration of the OpenSearch Dashboards index is blocked: on startup, Dashboards migrates its saved objects into a new index behind an alias, and if that migration can't complete, Dashboards never becomes ready. Common triggers for a blocked migration:  
+ After an upgrade, a blocked migration can happen for these reasons:
  + An OpenSearch Dashboards index left over from a previous version prevents the new alias from being created.
  + An upgrade from an older engine version whose Dashboards didn't use an alias conflicts with an existing index.
  + Documents written by a newer (self-managed) Dashboards instance can't be automatically migrated to the target version.
  + The `rest.action.multi.allow_explicit_index` advanced cluster option is set to `false`, which blocks the bulk requests that the migration uses. Unlike the other causes in this list, you can correct this one yourself. For more information, see [Dashboards fails to load or start because explicit indexes are disabled](#dashboards-troubleshooting-allow-explicit-index).
+ Without an upgrade, a blocked migration can happen for these reasons:
  + A corrupted OpenSearch Dashboards index created by a UI request or a restore blocks the alias.
  + Two or more versioned OpenSearch Dashboards indexes point at the same alias. This can also surface as an `Internal Server Error` (HTTP 500) even when cluster health is green.
  + Per-user or per-tenant indexes were created without an alias on domains that use fine-grained access control or Amazon Cognito authentication.
  + A saved-object mapping change can't be applied because of a broken document.

How to mitigate  

1. If a configuration change or version upgrade is in progress, wait for the domain to return to **Active**. The message is often transient and clears on its own. A normal change or upgrade completes within a few hours. If Dashboards is still unavailable more than 4 hours after the domain returns to **Active**, treat it as a persistent problem. Continue with the following steps. (You can't start a service software update while the domain is still processing a change.)

1. If cluster health is red or yellow, resolve the cluster issue first (see [Related cluster and access issues](#dashboards-troubleshooting-related)). Dashboards can't start on an unhealthy cluster.

1. Check whether the `rest.action.multi.allow_explicit_index` advanced cluster option is set to `false`. If it is, that alone prevents Dashboards from starting. Set it back to `true` as described in [Dashboards fails to load or start because explicit indexes are disabled](#dashboards-troubleshooting-allow-explicit-index), then skip the remaining steps.

   You can usually make this change yourself without a Support case. The exception is a domain that is stuck part-way through a version upgrade. You can't change advanced options while an upgrade is in progress, so the request is rejected. In that case, contact [AWS Support](https://aws.amazon.com/premiumsupport/) to clear the upgrade first.

1. If the message persists while cluster health is green, gather some read-only diagnostics that help AWS Support resolve the issue faster, then contact [AWS Support](https://aws.amazon.com/premiumsupport/) to repair the OpenSearch Dashboards index. Include the output of the following commands in your case:

   ```
   GET _cat/aliases/.kibana*?v
   GET _cat/indices/.kibana*?v
   ```

   Repairing the blocked migration is the fix for an already-stuck domain. Installing a software update does not, by itself, unblock a domain that is already stuck. Don't delete the OpenSearch Dashboards index yourself. Deleting it permanently removes all saved visualizations, dashboards, and index patterns that aren't backed up in a snapshot. If a repair requires deleting an index that contains data, AWS Support requests your permission first. For a production domain that has been unavailable for more than an hour with no configuration change in progress, open your Support case with a severity of **Production system impaired** or higher.

1. To prevent recurrence, keep the domain on the latest service software update; current releases fix the common causes of migration failure. Install the update after the domain returns to **Active**.

1. Take a manual snapshot before every version upgrade so that you can restore saved objects if a migration fails. For more information about taking snapshots, see [Creating index snapshots in Amazon OpenSearch Service](managedomains-snapshots.md).

Suggested action  
Keep your domain on a current service software version and take a snapshot before each upgrade. If you rely on Dashboards for production monitoring, consider the centralized [Using OpenSearch UI in Amazon OpenSearch Service](application.md), which is not tied to a single domain's per-domain OpenSearch Dashboards index migration.

## Dashboards fails to load or start because explicit indexes are disabled
<a name="dashboards-troubleshooting-allow-explicit-index"></a>

Symptom  
Dashboards is unavailable or unusable, in one of three ways.  
On older engine versions, Dashboards loads and displays a message that names the option:  

```
Kibana must be able to specify the index within Elasticsearch multi-requests (rest.action.multi.allow_explicit_index=true).
```
On current versions there is no such message. If a saved-object migration is pending, Dashboards reports `OpenSearch Dashboards server is not ready yet` and never finishes starting. This looks the same as any other blocked migration (see [Dashboards is stuck at "server is not ready yet" (HTTP 503 not ready error)](#dashboards-troubleshooting-not-ready)).  
If no migration is pending, Dashboards starts and reports that it is healthy, but it can't read its saved objects. The page loads, and index patterns, saved searches, visualizations, and dashboards are missing or fail to load. Your browser's developer console shows HTTP 400 responses from requests to `api/saved_objects/_bulk_get`. Your saved objects have not been lost. Dashboards can't read them while this option is `false`.  
Because none of these messages names the option, check its value directly before you assume another cause. You can see the current value in the console under **Advanced cluster settings**, or with the AWS CLI:  

```
aws opensearch describe-domain-config \
  --domain-name {{my-domain}} \
  --query "DomainConfig.AdvancedOptions"
```

Root cause  
The `rest.action.multi.allow_explicit_index` advanced cluster option is set to `false`. Dashboards needs the bulk, mget, and msearch APIs with index names in the request body. It needs them both to load data and to migrate its own saved objects, so this option prevents it from working:  
+ Dashboards can't read its own saved objects, because it retrieves them with mget and msearch. This happens as soon as the option is set, whether or not a migration is pending, and it happens even when Dashboards reports that it is healthy.
+ Dashboards can fail to start entirely. Whenever the saved-object format changes (for example, after an engine version upgrade), Dashboards migrates the OpenSearch Dashboards index into a new index on startup. This migration uses the bulk API with the index named in the request body. It fails while this option is `false`, and Dashboards doesn't recover on its own.
+ An engine version upgrade can stop before it finishes, because the upgrade verifies that Dashboards is healthy before it completes.

How to mitigate  
Set `rest.action.multi.allow_explicit_index` back to `true` in the domain's advanced options. This is a management-plane change you make with your own AWS credentials, either in the console (open the domain, choose **Edit**, and update **Advanced cluster settings**) or with the AWS Command Line Interface (AWS CLI):  

```
aws opensearch update-domain-config \
  --domain-name {{my-domain}} \
  --advanced-options rest.action.multi.allow_explicit_index=true
```
Changing an advanced option triggers a blue/green deployment, so the change takes a few minutes to apply. For more information about advanced cluster settings, see [Advanced cluster settings](createupdatedomains.md#createdomain-configure-advanced-options).  
You can't change advanced options while a configuration change or version upgrade is in progress. If an upgrade has already stalled because Dashboards can't start, this request is rejected. You can't apply the fix yourself in this case—contact [AWS Support](https://aws.amazon.com/premiumsupport/). To avoid this, set the option to `true` before you start an upgrade.
If the domain was already upgraded while this option was `false`, Dashboards might have left behind one or more unused OpenSearch Dashboards indexes from the failed migration attempts. Setting the option back to `true` doesn't always clear them. If Dashboards still reports `OpenSearch Dashboards server is not ready yet` after the change is applied, contact [AWS Support](https://aws.amazon.com/premiumsupport/) to repair the OpenSearch Dashboards index. Don't delete it yourself—it holds your index patterns, visualizations, and dashboards.

Suggested action  
Don't set `rest.action.multi.allow_explicit_index` to `false` unless both of the following are true:  
+ You intend to restrict index access through resource-based policies.
+ You don't need Dashboards on the domain.
Leaving it at the default (`true`) keeps Dashboards operational. If you do need to restrict subresource access this way, see [Advanced options and API considerations](ac.md#ac-advanced) for the tradeoff and for a per-user alternative that keeps Dashboards working. Before any engine version upgrade, confirm this option is `true`. An upgrade started while it is `false` can leave both Dashboards and the upgrade stuck.

## Dashboards runs out of memory
<a name="dashboards-troubleshooting-oom"></a>

Symptom  
Dashboards restarts, crashes, or becomes unresponsive under load, especially when opening large dashboards or loading many saved objects.

Root cause  
The Dashboards process exhausted its available memory, often from loading too many saved objects or rendering heavy dashboards.

How to mitigate  

1. Install the latest service software update. Current releases size the Dashboards heap dynamically and remove the older fixed-size limit.

1. If you increased `savedObjects:listingLimit` (default `1000`) in **Advanced Settings**, reduce it. Large values, such as `10000`, have caused out-of-memory errors.

1. Reduce dashboard complexity, the number of panels, and the auto-refresh frequency.

1. If memory usage is chronically high, scale to an instance type with more memory. For more information about sizing domains, see [Sizing Amazon OpenSearch Service domains](sizing-domains.md).

Suggested action  
To catch this before Dashboards runs out of memory, watch the `OpenSearchDashboardsHeapUtilization` CloudWatch metric; if it consistently exceeds 80%, scale to a larger instance type. Right-size your instance type for your Dashboards usage, keep dashboards lean, and avoid raising `savedObjects:listingLimit` beyond what you need.

## Requests fail because of payload size
<a name="dashboards-troubleshooting-payload"></a>

Symptom  
Certain Dashboards pages fail to load because the request payload exceeds the Dashboards payload limit (`server.maxPayloadBytes`, which defaults to 1 MB / 1,048,576 bytes).

Root cause  
Index patterns that match a very large number of indexes or fields produce requests larger than the payload limit.

How to mitigate  

1. Reduce the request size rather than raising the limit:
   + Reduce the number of indexes in your index patterns.
   + Reduce the number of fields.
   + Reduce field-name length.

1. Contact [AWS Support](https://aws.amazon.com/premiumsupport/) to request the supported, account-level option that persists an increased `server.maxPayloadBytes` value so that it survives blue/green deployments and node replacements. This option is available on all supported Amazon OpenSearch Service versions.
Don't try to raise this limit by editing the Dashboards configuration on nodes yourself. Node-level changes aren't persistent. Any blue/green deployment or node replacement removes them. Use the account-level option through AWS Support instead.

Suggested action  
Keep index patterns scoped to the indexes and fields you actually use so requests stay within the payload limit.

## Dashboards is unavailable during a version upgrade
<a name="dashboards-troubleshooting-upgrade-downtime"></a>

Symptom  
Dashboards is unavailable for most of the duration of an engine version-upgrade blue/green deployment. This is expected behavior, not a fault, and it resolves itself when the upgrade completes.

Root cause  
Dashboards stays offline for most of a version upgrade to avoid version-check race conditions between the old and new environments.

How to mitigate  
Wait for the upgrade to complete; Dashboards becomes available again automatically. Treat version upgrades as a planned Dashboards maintenance window and schedule them outside business-critical hours. For more information about configuration changes, see [Making configuration changes in Amazon OpenSearch Service](managedomains-configuration-changes.md).

Suggested action  
Schedule upgrades during low-traffic windows. If you need Dashboards availability that isn't tied to a single domain's upgrade window, consider the centralized [Using OpenSearch UI in Amazon OpenSearch Service](application.md).

## An engine version upgrade fails the pre-upgrade check with an incompatible index
<a name="dashboards-troubleshooting-upgrade-incompatible-index"></a>

Symptom  
You start an engine version upgrade (or run the upgrade eligibility check) and it fails at the pre-upgrade check, before any upgrade begins. The validation notification lists one or more incompatible indexes, and can name the OpenSearch Dashboards index specifically. This typically happens when you upgrade to OpenSearch 3.x while the domain still has indexes created in OpenSearch 1.3, Elasticsearch 7.10, or earlier, including the OpenSearch Dashboards index. (Upgrades from OpenSearch 1.3 or 2.x must go to OpenSearch 2.19 first, then to OpenSearch 3.x.)

Root cause  
OpenSearch can read indexes only from the immediately preceding major version, so OpenSearch 3.x doesn't support indexes created in OpenSearch 1.3, Elasticsearch 7.10, or earlier. The pre-upgrade check blocks the upgrade and lists these indexes on purpose, so you don't lose any data. You must reindex or remove older indexes before a major version upgrade; the service doesn't reindex them automatically. The OpenSearch Dashboards index follows the same rule.

How to mitigate  

1. Run the upgrade eligibility check to see the full list of incompatible indexes (the same list is in the failed-upgrade notification). For more information about upgrading domains, see [Upgrading Amazon OpenSearch Service domains](version-migration.md).

1. Take a manual snapshot before making changes. For more information about taking snapshots, see [Creating index snapshots in Amazon OpenSearch Service](managedomains-snapshots.md).

1. For each incompatible data index, reindex it into a new index (created on the current version), then delete the old one. For UltraWarm or cold indexes, move them to hot storage first, reindex, then move them back.

   ```
   POST _reindex
   { "source": { "index": "my-old-index" }, "dest": { "index": "my-new-index" } }
   ```

1. For the OpenSearch Dashboards index, back up first because it holds your index patterns, visualizations, and dashboards: in Dashboards, go to **Dashboards Management**, **Saved Objects**, and export them. Then delete the incompatible index. A new, compatible index is created automatically after the upgrade; re-import your saved objects afterward. If you'd rather not delete it, contact [AWS Support](https://aws.amazon.com/premiumsupport/).

1. Delete any incompatible index you no longer need instead of reindexing it.

1. Re-run the eligibility check, and re-trigger the upgrade after it passes.

Suggested action  
Reindex or retire old indexes so they don't span more than one major version; indexes left across several upgrades will eventually block one. Take a manual snapshot before every upgrade, and export your OpenSearch Dashboards saved objects periodically as a backup.

## Dashboards doesn't load properly, shows a blank page, or generates blank reports
<a name="dashboards-troubleshooting-blank-page"></a>

Symptom  
A single user or browser sees a blank page, blank reports, or a red banner that reads `OpenSearch Dashboards did not load properly. Check the server output for more information.`, while other users are unaffected. Confirm by reproducing in a private (incognito) window or a different browser.

Root cause  
A stale browser cache causes this issue, especially after a service software update or when you use the Reporting feature.

How to mitigate  

1. Clear your browser cache and cookies, then reload the page. Try a private (incognito) window and a supported, up-to-date browser.

1. Disable ad blockers or browser extensions for the Dashboards URL.

1. If the banner persists for all users (not just one browser), install the latest service software update, then contact [AWS Support](https://aws.amazon.com/premiumsupport/) if the issue continues.

Suggested action  
Clear your browser cache after a service software update, and use a supported, up-to-date browser.

## Unsupported configurations
<a name="dashboards-troubleshooting-unsupported-configs"></a>

Avoid these configurations, which are common sources of Dashboards problems:
+ **Dashboards isn't supported on domains where `rest.action.multi.allow_explicit_index` is set to `false`.** Dashboards requires the bulk, mget, and msearch APIs with index names in the request body, so this option is not compatible with running Dashboards. Setting the option back to `true` is the only way to restore Dashboards. No configuration keeps both. AWS Support can help you repair the OpenSearch Dashboards index after you re-enable the option, but can't make Dashboards work while it stays disabled. Decide per domain which one you need. For more information, see [Dashboards fails to load or start because explicit indexes are disabled](#dashboards-troubleshooting-allow-explicit-index).
+ **Reverse proxies (for example, nginx) in front of Dashboards are supported only for access control**, as described in [Using a proxy to access OpenSearch Service from Dashboards](dashboards.md#dashboards-proxy). If you run Dashboards through third-party proxy software and hit an unexpected error, reproduce the issue without the proxy before you contact AWS Support.
+ **Manual edits to node configuration files aren't persistent.** Any blue/green deployment or node replacement reverts them. Use supported settings and options instead of node-level edits. You can't use SSH to access nodes or directly modify configuration files.

## Related cluster and access issues
<a name="dashboards-troubleshooting-related"></a>

Because Dashboards depends on a healthy cluster and on your domain's access configuration, the following troubleshooting topics frequently apply when Dashboards is unavailable. For all of these, see [Troubleshooting Amazon OpenSearch Service](handling-errors.md).
+ **Can't access OpenSearch Dashboards**: access policy and Amazon Cognito authentication, including the `User: anonymous is not authorized to perform: es:ESHttpGet` error and VPC-access request timeouts.
+ **Red cluster status** and **Yellow cluster status**: unassigned shards prevent Dashboards from reading or writing its OpenSearch Dashboards index.
+ **ClusterBlockException**: low storage space or high JVM memory pressure blocks writes, including writes to the OpenSearch Dashboards index.
+ **JVM OutOfMemoryError** and **Request throttling**: cluster overload surfaces as Dashboards errors and `429 Too Many Requests` responses.