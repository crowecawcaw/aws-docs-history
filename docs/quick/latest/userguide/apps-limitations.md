

# Limitations of apps in Quick
<a name="apps-limitations"></a>

The following limitations apply to apps in Amazon Quick in its current release.

## Regional availability
<a name="apps-regional-availability"></a>

Apps in Amazon Quick is available in a subset of the AWS Regions that Amazon Quick supports: US East (N. Virginia), US West (Oregon), Europe (Ireland), and Asia Pacific (Sydney). Support for additional Regions is being added.

## Limits
<a name="apps-limits-platform"></a>


**Limits**  

| Resource | Limit | 
| --- | --- | 
| Dashboard visuals per app | 8 | 
| Visual minimum size | 100 × 100 pixels | 
| Storage value size | 350 KB per item | 
| Storage key length | 255 characters | 
| Table name length | 255 characters | 

## Building experience
<a name="apps-limits-building"></a>
+ **Content policy violations** — Prompts occasionally trigger security guardrails as false positives. When this happens, the agent cannot process further prompts in the current session. Close the editor and wait 15 to 20 minutes for the session to time out, then reopen the app.
+ **Agent memory in long conversations** — The agent's accuracy decreases as the conversation grows longer. For complex applications, consider building in phases.
+ **No image upload from agent chat** — You cannot upload screenshots or reference images to the agent.
+ **No investigation-only mode** — The agent executes code changes with every instruction. To have the agent investigate without making changes, explicitly say "Investigate but do not write code yet."
+ **Network sensitivity** — The editor uses a WebSocket for real-time streaming. Unstable connections can cause prompts to fail silently.

## Live data (Quick datasets)
<a name="apps-limits-live-data"></a>

When an app queries datasets directly for live data, the following limitations apply in the current release. For how to use live data, see [Connecting to Quick datasets in apps in Quick](connecting-datasets-apps.md).

### Data and datasets
<a name="apps-limits-live-data-data"></a>
+ **Datasets only** — Topics, dashboards, and analyses cannot be a live data source. You can still embed individual dashboard visuals separately.
+ **Single-table datasets only** — Multi-table (data model) datasets, composite or child datasets, and datasets that join across sources or engines are not supported.
+ **Supported engines** — SPICE, plus Direct Query on Redshift, Athena, Aurora PostgreSQL, PostgreSQL, Databricks, and S3 Tables. Import other engines into SPICE first.
+ **Same account and Region** — Cross-account and cross-Region datasets cannot be reached.

### Sharing and access
<a name="apps-limits-live-data-sharing"></a>
+ **Sharing an app does not share its data** — Grant each app user read access to every dataset the app uses, or share the folder that holds them.
+ **App user roles** — Only Admin, Author, Admin Pro, Author Pro, and Reader Pro roles can view live data (Reader Pro only where enabled). Standard Reader and Restricted Reader cannot.
+ **No public apps** — An app that uses live datasets cannot be made public.
+ **One-time consent** — Each app user approves a prompt per dataset the first time they open the app.

### What to expect at scale
<a name="apps-limits-live-data-scale"></a>
+ **Large datasets** — A visual shows up to 50,000 rows of data. If a visual tries to load more than that, it shows only the first 50,000 rows. A total calculated from the raw rows can therefore be inaccurate. Ask the agent to summarize the data, for example, totals by category, instead of listing every row.
+ **Many visuals on one page** — A page with many live visuals loads a little at a time rather than all at once. Keep the number of live visuals on a page reasonable, and ask the agent to combine related charts so they share data where possible.

### Dataset changes are not tracked
<a name="apps-limits-live-data-changes"></a>

A published app refers to its columns by exact name and type as of build time. Renaming or retyping a column, or replacing or deleting a dataset, breaks the visuals that use it, with no warning. Reopen the app, have the agent update the visuals, and republish.

## Sharing and access
<a name="apps-limits-sharing"></a>
+ **Subscription requirement** — Only users with Author, Professional, Author Pro, Enterprise, or Admin Pro subscriptions can view apps.
+ **External access** — Users must have a Amazon Quick account to view an app, unless the app is published publicly. Public access is available on Free and Plus accounts only. Public apps cannot use connectors, embedded visuals, embedded chat, or spaces.

## Portability
<a name="apps-limits-portability"></a>
+ **No code export** — You cannot download the source code of an app.
+ **Duplication** — You can duplicate an app to create a copy.

## Integration limitations
<a name="apps-limits-integrations"></a>
+ **No direct Quick Flows integration** — Use a space as an intermediary.
+ **No standalone agent embedding** — You can create a new agent instance backed by a space.
+ **No integration removal** — You cannot remove a registered integration from an app through the settings UI.

## Sandbox restrictions
<a name="apps-limits-sandbox"></a>

For detailed information about sandbox restrictions, see [Sandbox restrictions](security-sandbox-apps.md#apps-sandbox-restrictions). Key restrictions include:
+ **No direct link navigation** — Users must use Cmd\+Click or Ctrl\+Click.
+ **No external images** — CSP blocks loading images from external URLs.
+ **No built-in app analytics** — As a workaround, you can ask the agent to implement a view counter using shared app storage.