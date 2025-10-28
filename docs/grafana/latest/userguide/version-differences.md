# Differences between Grafana versions

When [creating a Grafana workspace](AMG-create-workspace.md "AMG-create-workspace.md"), you
must choose a Grafana version to create. You can choose between versions compatible with
Grafana versions 8, 9, and 10. Each of these has added functionality from the previous
version. The following topics describe the changes in versions 9 and 10, including
changes in version 10 that might break functionality that you use in version 9.

###### Note

You can read version-specific documentation for using your Grafana workspace in
the [Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md"), [Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md"), and [Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md") topics.

For detailed notes by version, and more information from Grafana Labs, see [What's new in
Grafana](https://grafana.com/docs/grafana/latest/whatsnew/ "https://grafana.com/docs/grafana/latest/whatsnew/") in the _Grafana Labs documentation_.

## Grafana version 10

The following features were added in Grafana version 10.

- **Correlations** – Correlations define
  how data in one data source is used to query data in another data source,
  and allow the Explore visualization to easily run queries related to the
  shown data. For more details, see [Correlations in Grafana version 10](v10-correlations.md "v10-correlations.md").
- **Subfolders** – When organizing your
  dashboards, you can now use subfolders to create a nested hierarchy. For
  more details, see [Creating dashboard
  folders](v10-dash-managing-dashboards.md#v10-dash-create-dashboard-folder "v10-dash-managing-dashboards.md#v10-dash-create-dashboard-folder").
- **Alerts** – Grafana alerting now
  supports silencing alerts. Additionally, Grafana alerting no longer sends
  notifications 3 times.
- **Alerting upgrade preview** – Before
  upgrading from classic dashboard alerts to Grafana alerts, you can see what
  your alerts will look like, and even make changes that are applied when
  migrating. For more details, see [Migrating classic dashboard alerts to Grafana
  alerting](v10-alerting-use-grafana-alerts.md "v10-alerting-use-grafana-alerts.md"). Grafana Labs has
  announced that Grafana version 11 and beyond will no longer support classic
  dashboard alerts.
- **Support bundles** – Support bundles
  provide a simple way to collect information about your Grafana workspace to
  share with product support. You can quickly create a support bundle
  containing data about migrations, plugins, settings, and more. For more
  details, see [Gather information for support](support-bundles.md "support-bundles.md").
- **New visualizations** – Three new
  visualizations are available. [XY
  Chart](v10-panels-xychart.md "v10-panels-xychart.md"), [Datagrid](v10-panels-datagrid.md "v10-panels-datagrid.md"), and
  [Trend panel](v10-panels-trend.md "v10-panels-trend.md") are all available
  for workspaces compatible with version 10. Version 9 workspaces can also use
  XY Charts.
- **PagerDuty** – The Enterprise plugins
  now include a plugin for PagerDuty.
- **Transformations redesign** – The
  transformations tab has an improved user experience and visual design.
  Transformations are categorized, and each transformation type has an
  illustration to help you choose the right one.
- **Prometheus metric encyclopedia** –
  The metrics dropdown for Prometheus metrics in the Prometheus query builder
  has been replaced with a paginated and searchable metric
  _encyclopedia_.
- **API key UI discontinued** – [Service accounts](service-accounts.md "service-accounts.md") are the recommended
  way to authenticate calls to the Grafana HTTP APIs. As part of Grafana Labs
  work toward discontinuing API keys, you can no longer create API keys
  through the workspace user interface. You can only create API keys through
  the AWS APIs.

For more information about the discontinuation of API keys by Grafana
Labs, see [APIKeys: Sunsetting of API keys](https://github.com/grafana/grafana/issues/53567 "https://github.com/grafana/grafana/issues/53567") in the Grafana GitHub issues
list.

**Breaking changes**

The Grafana version 10.4 release includes changes from Grafana versions 9.5
through 10.4. Grafana versions 10.0 and 10.3 had some changes that might break
functionality in some cases. When updating to a new version, it is recommended to
test in a non-production environment before updating your production
workspaces.

The following changes might affect some users updating to Grafana version 10.

- **Angular discontinued** – Plugins
  that use Angular will no longer be supported in future releases of Grafana.
  In version 10, panels that use angular will show a banner stating that they
  use a discontinued feature, to give a notice that they won't work in future
  versions.
- **Alias in CloudWatch removed** – Alias
  patterns in the CloudWatch query editor were replaced by Label (dynamic
  labels).

Open any dashboard that uses the Alias field, and save it. Alias is
migrated to Label automatically.

- **Older plugins need to be upgraded**
  – The plugins for Athena and Amazon Redshift data source must be updated in
  Grafana v10 workspaces. The Athena data source plugin must be version 2.9.3
  or newer; the Amazon Redshift data source plugin must be version 1.8.3 or newer.

For information on installing or upgrading plugins, see [Find plugins with the plugin catalog](grafana-plugins.md#plugin-catalog "grafana-plugins.md#plugin-catalog").

- **DoiT BigQuery plugin no longer supported**
  – The DoiT BigQuery data source plugin is no longer supported. Use
  the official Grafana Labs BigQuery data source plugin instead.
- **Transformation changes** – Grafana
  version 10 has made a few bug fix changes to field names and keys. For full
  details, see [Transformation breaking changes](https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v10-3/#transformations "https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v10-3/#transformations") in the Grafana Labs
  documentation.
- **Data source permissions APIs** – The
  endpoints for accessing data source permissions have changed. For full
  details, see [Data source permissions changes](https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v10-3/#data-source-permissions "https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v10-3/#data-source-permissions") in the Grafana Labs
  documentation.

For more details on breaking changes, and changes that affect plugin developers,
see the following topics in the _Grafana Labs
documentation_:

- [Breaking changes in Grafana v10.0](https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v10-0/ "https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v10-0/")
- [Breaking changes in Grafana v10.3](https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v10-3/ "https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v10-3/")

## Grafana version 9

The following features were added in Grafana v9.

- **Alerting**: Grafana-managed alert rules now
  supports group names.
- **Explore**: Create a dashboard from within
  Explore view.
- **Prometheus queries**: A new query builder
  for Prometheus queries (using PromQL) makes writing queries easier.
- **Loki queries**: A new query builder for
  Loki queries (using LogQL) makes writing queries easier.
- **API tokens / Service accounts**: Service
  accounts simplify machine access in Grafana, helping you to manage API
  tokens.
- **Plugin management**: You can enable plugin
  management to install, remove, or update community plugins in your
  workspace. This gives you access to more data sources and visualizations,
  and gives you control over the version of each plugin that you use.
- **Trace to metrics**: Configure a tracing
  data source to add links to metrics with queries and tags.
- **Canvas panel**: A new panel visualization
  with static and dynamic elements to create data-driven, custom panels with
  images and overlain text.
- **Reorganized interface**: Updated UI with
  easier navigation in the Grafana console.
- **CloudWatch**: The Amazon CloudWatch data source can now
  monitor metrics across AWS accounts and across AWS Regions.
- **Logs**: The interface for log details has
  been improved.
- **General**: Bug fixes and minor improvements
  throughout.

**Breaking changes**

The Grafana version 9.4 release includes a range of new features and improvements,
building upon previous versions. This version had some changes that might break
functionality in some cases. When updating to a new version, we recommend you test
in a non-production environment before updating your production workspaces.

The following changes might affect some users updating to Grafana version 9.4. For
a detailed list of these changes, see the [Grafana 9.4 changelog](https://github.com/grafana/grafana/blob/release-9.4.17/CHANGELOG.md "https://github.com/grafana/grafana/blob/release-9.4.17/CHANGELOG.md") on _GitHub_.

- **API discontinued** – The
  `/api/tsdb/query` API has been removed.

**Action required:** Use
`/api/ds/query` instead. See [Query a data source](https://grafana.com/docs/grafana/latest/http_api/data_source/#query-a-data-source "https://grafana.com/docs/grafana/latest/http_api/data_source/#query-a-data-source") in the _Grafana public
documentation_ and Issue [#49916](https://github.com/grafana/grafana/issues/49916 "https://github.com/grafana/grafana/issues/49916")
on _GitHub_.

- **API endpoint changes** – Several
  alerting API endpoints now require data source UID instead of numeric
  ID.

**Affected endpoints:**
`api/v1/rule/test`, `api/prometheus/`,
`api/ruler/`, `api/alertmanager/`

**Action required:** Update API calls to use
data source UID as path parameter. See Issues [#48070](https://github.com/grafana/grafana/issues/48070 "https://github.com/grafana/grafana/issues/48070"), [#48052](https://github.com/grafana/grafana/issues/48052 "https://github.com/grafana/grafana/issues/48052"), [#48046](https://github.com/grafana/grafana/issues/48046 "https://github.com/grafana/grafana/issues/48046"), and [#47978](https://github.com/grafana/grafana/issues/47978 "https://github.com/grafana/grafana/issues/47978")
on _GitHub_.

- **Azure Monitor queries removed** –
  Application Insights and Insight Analytics queries are no longer
  supported.

Deprecated in Grafana 8.0, removed in 9.0. Deprecated queries will not
execute.

**Action required:** See [Azure Monitor data source](https://grafana.com/docs/grafana/latest/datasources/azuremonitor/deprecated-application-insights/ "https://grafana.com/docs/grafana/latest/datasources/azuremonitor/deprecated-application-insights/") in the _Grafana public
documentation_ for migration guidance.

- **Browser access mode removed** –
  Browser access mode is no longer available for InfluxDB and Prometheus data
  sources.

**Action required:** Switch to server access
mode in your data source configuration. InfluxDB: Deprecated in 8.0.0,
removed in 9.2.0. See Issue [#53529](https://github.com/grafana/grafana/issues/53529 "https://github.com/grafana/grafana/issues/53529")
on _GitHub_. Prometheus: Deprecated in 7.4.0, removed in
9.2.0. See Issue [#50162](https://github.com/grafana/grafana/issues/50162 "https://github.com/grafana/grafana/issues/50162")
on _GitHub_.

- **Dashboard settings access restricted**
  – You can no longer open dashboard settings while editing
  panels.

Dashboard settings are locked when panel edit mode is active. Close panel
edit mode before accessing dashboard settings. See Issue [#54746](https://github.com/grafana/grafana/issues/54746 "https://github.com/grafana/grafana/issues/54746")
on _GitHub_.

- **Data source password encryption** –
  Unencrypted passwords are no longer supported.

**Action required:** Use
`secureJsonData.password` and
`secureJsonData.basicAuthPassword`. Previously discontinued
in v8.1.0. See Issue [#49987](https://github.com/grafana/grafana/issues/49987 "https://github.com/grafana/grafana/issues/49987")
on _GitHub_.

- **Default data source behavior** –
  Default data source selection no longer affects existing panels.

Default data source only applies to new panels. Changing the default won't
update existing dashboards. Previously saved panels retain their data source
configuration. See Issue [#45132](https://github.com/grafana/grafana/issues/45132 "https://github.com/grafana/grafana/issues/45132")
on _GitHub_.

- **Elasticsearch interval property changed**
  – Query interval specification updated for Elasticsearch 7.x.

Changed from `interval` to `fixed_interval`
property. Provides consistency with Elasticsearch 8.x. Most queries won't
show visible changes. See Issue [#50297](https://github.com/grafana/grafana/issues/50297 "https://github.com/grafana/grafana/issues/50297")
on _GitHub_.

- **Elasticsearch Raw document mode
  discontinued** – Display mode changes in Elasticsearch
  data source.

**Action required:** Use **Raw
Data** mode instead. See Issue [#62236](https://github.com/grafana/grafana/issues/62236 "https://github.com/grafana/grafana/issues/62236")
on _GitHub_.

- **Elasticsearch version support** –
  Older Elasticsearch versions are no longer supported.

**Action required:** Upgrade Elasticsearch to
version 7.10.0 or later. Versions below 7.10.0 are past end-of-life. See
Issue [#48715](https://github.com/grafana/grafana/issues/48715 "https://github.com/grafana/grafana/issues/48715") on _GitHub_.

- **Explore URL format discontinued** –
  Compact Explore URLs will be removed in a future release.

**Action required:** Update hard coded links
to use standard URL format. Compact URLs:
`&left=["now-1h","now"...]`. Standard URLs:
`&left={"datasource":"test"...}`. See Issue [#50873](https://github.com/grafana/grafana/issues/50873 "https://github.com/grafana/grafana/issues/50873")
on _GitHub_.

- **GitHub OAuth display changes** –
  GitHub name and login display updated.

GitHub name appears as Grafana name. GitHub login appears as Grafana
login. Improves user identification clarity. See Issue [#45438](https://github.com/grafana/grafana/issues/45438 "https://github.com/grafana/grafana/issues/45438")
on _GitHub_.

- **Heatmap panel implementation updated**
  – Heatmap panels use a new implementation starting in 9.1.0.

Significantly improved rendering performance. Buckets are placed on
reasonable borders (1m, 5m, 30s). Round cells are no longer
supported.

**Action required:** Test your heatmap panels
after upgrade. Disable new implementation by setting
`useLegacyHeatmapPanel` feature flag to true if needed. Add
`?__feature.useLegacyHeatmapPanel=true` to dashboard URLs for
testing. See Issue [#50229](https://github.com/grafana/grafana/issues/50229 "https://github.com/grafana/grafana/issues/50229")
on _GitHub_.

- **InfluxDB backend migration** –
  InfluxDB data parsing behavior has changed.

The InfluxDB backend migration feature toggle
(`influxdbBackendMigration`) is reintroduced due to backend
processing issues. By default, InfluxDB data is parsed in the frontend. If
you upgraded to 9.4.4 and added transformations on InfluxDB data, those
panels will fail to render.

**Action required:** Remove affected panels
and recreate them, or edit the `time` field as `Time`
in `panel.json` or `dashboard.json`. See Issue [#64842](https://github.com/grafana/grafana/issues/64842 "https://github.com/grafana/grafana/issues/64842")
on _GitHub_.

- **Log message format updated** – Log
  message structure has changed.

`lvl` is now `level`. `eror` and
`dbug` are now `error` and `debug`.
Increased timestamp precision. Opt-out available with `oldlog`
feature toggle (temporary). See Issue [#47584](https://github.com/grafana/grafana/issues/47584 "https://github.com/grafana/grafana/issues/47584")
on _GitHub_.

- **Loki data format optimization** –
  Loki logs data uses a more efficient dataframe format.

Single dataframe with **labels** column instead of
separate dataframes. Explore and logs panels work without changes. Other
panels or transforms may need adjustment.

**Action required:** Replace **labels
to fields** transformation with **extract
fields** transformation. See Issue [#47153](https://github.com/grafana/grafana/issues/47153 "https://github.com/grafana/grafana/issues/47153")
on _GitHub_.

- **NaN value handling** – Consistent
  `NaN` representation across Prometheus and Loki data
  sources.

`NaN` values remain as `NaN` instead of converting
to `null`. Change should be mostly invisible to users. Affects
both dashboard and alerting paths. See Issues [#49475](https://github.com/grafana/grafana/issues/49475 "https://github.com/grafana/grafana/issues/49475")
and [#45389](https://github.com/grafana/grafana/issues/45389 "https://github.com/grafana/grafana/issues/45389") on _GitHub_.

- **Password reset links invalidated** –
  Existing password reset links won't work after upgrade.

Password reset links sent before upgrade are invalid. Users must request
new password reset links. Links expire after 2 hours. See Issue [#42334](https://github.com/grafana/grafana/issues/42334 "https://github.com/grafana/grafana/issues/42334")
on _GitHub_.

- **Reserved label prefix** – Labels
  starting with `grafana_` are reserved.

Manually configured labels beginning with `grafana_` may be
overwritten. Current reserved labels: `grafana_folder` (Title of
the folder containing the alert). See Issue [#50262](https://github.com/grafana/grafana/issues/50262 "https://github.com/grafana/grafana/issues/50262") on _GitHub_.

- **Transformation improvements** –
  **Rename by regex** transformation now supports global
  patterns.

Global patterns use the format `/<stringToReplace>/g`.
Some transformations may behave differently. Wrap match strings in forward
slashes for previous behavior: `(.*)` becomes
`/(.*)/`. See Issue [#48179](https://github.com/grafana/grafana/issues/48179 "https://github.com/grafana/grafana/issues/48179") on _GitHub_.
