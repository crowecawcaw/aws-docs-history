

# Differences between Grafana versions
<a name="version-differences"></a>

When [creating a Grafana workspace](AMG-create-workspace.md), you must choose a Grafana version to create. You can choose between versions compatible with Grafana versions 8, 9, 10, and 12. Each of these has added functionality from the previous version. The following topics describe the changes in versions 9, 10, and 12, including changes that might break functionality that you use in previous versions.

**Note**  
You can read version-specific documentation for using your Grafana workspace in the [Working in Grafana version 12](using-grafana-v12.md), [Working in Grafana version 10](using-grafana-v10.md), [Working in Grafana version 9](using-grafana-v9.md), and [Working in Grafana version 8](using-grafana-v8.md) topics.

For detailed notes by version, and more information from Grafana Labs, see [What's new in Grafana](https://grafana.com/docs/grafana/latest/whatsnew/) in the *Grafana Labs documentation*.

## Grafana version 12
<a name="version-diff-v12"></a>

The following features were added in Grafana version 12.

**Drilldown apps**
+ **Metrics Drilldown** – A queryless, point-and-click experience for exploring Prometheus metric data. See [Metrics Drilldown](v12-drilldown-metrics.md).
+ **Logs Drilldown** – A queryless experience for browsing Loki logs with volume and text patterns. See [Logs Drilldown](v12-drilldown-logs.md).
+ **Traces Drilldown** – A queryless experience for exploring distributed Tempo traces. See [Traces Drilldown](v12-drilldown-traces.md).
+ **Profiles Drilldown** – A queryless experience for browsing Pyroscope profiling data. See [Profiles Drilldown](v12-drilldown-profiles.md).

**Dashboards and visualizations**
+ **Scenes-powered dashboards** – The dashboard rendering engine has been rebuilt using the Scenes framework, providing improved performance, better template variable support, and more flexible layouts.
+ **New table visualization** – The table panel has been completely rebuilt for improved performance and new capabilities, including CSS cell styling, tooltip generation from table fields, an improved footer, a new Actions cell type for interactive buttons, and auto-formatted cell values in Cell Inspect.
+ **Canvas visualization improvements** – Canvas panels now support one-click data links and actions, dynamic connection directions, the ability to disable tooltips, and pan and zoom improvements, giving you more control over interactive data-driven layouts.
+ **Visualization actions** – You can now add interactive actions to visualizations that trigger API calls or navigate to URLs, with support for custom variables, one-click data links, and a new Actions cell type for table visualizations.
+ **Colored table rows with conditional formatting** – Table visualizations now support row-level conditional formatting, allowing you to color entire rows based on data values.
+ **Stat visualization percent change** – Stat panels now display percent change with configurable color mode options, making it easier to see trends at a glance.
+ **Legend support in bar gauge** – Bar gauge visualizations now support legends, improving readability when displaying multiple series.
+ **State timeline pagination** – State timeline visualizations now support pagination, making it easier to navigate large datasets.
+ **Redesigned dashboard filters** – Dashboard list filters have been redesigned for a more intuitive browsing experience.
+ **Switch variable type** – A new Switch variable type lets you quickly toggle between values in queries, simplifying dashboard interactions.
+ **Static options for query variables** – Query variables now support static options, giving you more control over variable values without requiring a data source query.
+ **Enhanced ad hoc filters** – Ad hoc filters now provide improved support across data sources, making it easier to dynamically filter dashboard data.
+ **Better time region control with Cron syntax** – Annotations now support Cron syntax for time regions, providing more precise control over time-based annotations.
+ **Improved geomap performance** – Geomap visualizations now render significantly faster with improved performance optimizations.
+ **Navigation bookmarks** – You can now bookmark frequently used pages in the navigation menu for quick access.
+ **Set threshold colors from query** – The Config from query transformation now supports setting threshold colors dynamically based on query results.
+ **Enhanced custom currency format** – A new custom currency format option lets you display exact financial values with precise decimal control.
+ **Server-configurable quick time ranges** – Administrators can now configure the quick time range options available in dashboard time pickers.
+ **Announcement banner** – Administrators can now display announcement banners to communicate important information to workspace users.

**Transformations**
+ **Substring matcher in Filter by value** – The Filter by value transformation now includes a substring matcher, making it easier to filter data based on partial text matches.
+ **Trendline transformation** – A new Trendline transformation lets you spot patterns in your data by adding trend lines and moving averages to visualizations.
+ **Binary transformation for all number fields** – You can now apply the same binary transformation to all number fields in a table at once, reducing repetitive configuration.
+ **New regex option for Extract fields** – The Extract fields transformation now supports regular expressions, providing more powerful field extraction from text data.
+ **Transformation updates** – Multiple transformation improvements have been added, including new modes and usability enhancements across the transformation pipeline.
+ **Dashboard variables in all transformations** – Dashboard variables are now supported in all transformation types, expanding the flexibility of data processing pipelines.

**Alerting**
+ **Keep Last State for Grafana Managed Alerting** – Alert rules can now be configured to keep their last state when a query returns no data or an error, preventing unnecessary alert state changes.
+ **Alert detail view redesign** – The alert rule detail view has been redesigned with a clearer layout and more actionable information.
+ **Alerting template selector** – A new template selector in the alerting UI makes it easier to choose and apply notification templates.
+ **Improved paused alert visibility** – Paused alert rules are now more clearly indicated in the UI, making it easier to identify which rules are not actively evaluating.
+ **Only available for Grafana-managed alerts: rule-specific silences** – You can now create silences that apply to specific alert rules with granular permissions, providing more targeted alert suppression.
+ **Recording rules for Grafana-managed alerts** – Recording rules are now available for Grafana-managed alerts, allowing you to precompute frequently used queries for better performance. This replaces the deprecated recorded queries feature. See [Configure recording rules](v12-alerting-configure-recordingrules.md).
+ **Alert rule version history** – Alert rules now maintain a version history, allowing you to track changes and revert to previous configurations.
+ **Grafana-managed alert rule "Recovering" state** – Alert rules now support a "Recovering" state that indicates when an alert condition is no longer firing but has not yet returned to normal.
+ **Alert rule improvements** – Grafana-managed alert rules include multiple usability improvements, including updated list pages, active time intervals, the ability to import rules from Prometheus YAML, and a redesigned settings page.

**Explore and logs**
+ **New logs visualization** – A new logs visualization panel provides improved log rendering with a new field selector component for customizing which fields are displayed.
+ **JSON Log Line Viewer** – The Logs Drilldown app now includes a JSON viewer for structured log lines, making it easier to inspect JSON-formatted log data.
+ **Forward direction search for Loki** – Loki queries in Explore now support forward direction search, allowing you to search logs from oldest to newest.
+ **Correlations in Explore** – You can now add correlations to external URLs directly from Explore, enabling seamless navigation between data sources and external systems. See [Correlations in Grafana version 12](v12-correlations.md).

**Data sources**
+ **Amazon Managed Service for Prometheus data source migration** – Starting with this release, Sigv4 authentication support in the Core Prometheus plugin has been deprecated. When you upgrade to Grafana version 12, all Amazon Managed Service for Prometheus data sources that were previously using the Core Prometheus plugin are automatically migrated to the Amazon Managed Service for Prometheus plugin. Any dashboards using these data sources are automatically updated to reflect this change.
+ **Amazon CloudWatch Logs Insights with PPL and SQL** – You can now query Amazon CloudWatch Logs Insights using PPL (Piped Processing Language) and SQL syntax in addition to the standard query language.
+ **Amazon CloudWatch Metric Insights cross-account support** – Amazon CloudWatch Metric Insights now supports cross-account observability, allowing you to query metrics across multiple AWS accounts.
+ **Amazon CloudWatch Logs Anomaly Detection and Pattern Analysis** – The Amazon CloudWatch data source now supports log anomaly detection and pattern analysis for identifying unusual patterns in your log data.
+ **OpenSearch PPL and Sample Queries** – The OpenSearch data source now supports PPL language and sample queries for easier query building.
+ **MSSQL Windows Active Directory authentication** – The Microsoft SQL Server data source now supports Windows Active Directory (Kerberos) authentication.
+ **Removal of old Tempo and Loki Search** – The legacy Tempo Search and Loki Search interfaces have been removed in favor of the TraceQL-powered search experience.
+ **BigQuery Service Account Impersonation** – The BigQuery data source now supports service account impersonation for more flexible authentication.
+ **Google Sheets template variables** – The Google Sheets data source now supports template variables for dynamic data queries.
+ **Time series macro support for SQL data sources** – The visual query builder for SQL data sources now supports time series macros, simplifying time-based queries.
+ **Unity Catalog support in Databricks** – The Grafana Databricks plugin now supports Unity Catalog for unified data governance.
+ **Honeycomb raw query support** – The Honeycomb data source now supports raw queries for advanced query capabilities.
+ **GitHub App authentication** – The GitHub data source now supports GitHub App authentication as an alternative to personal access tokens.

**Authentication and security**
+ **API keys migrated to service accounts** – API keys have been fully deprecated and automatically migrated to service accounts, providing improved security and management capabilities. See [Using service accounts](v12-authenticating-grafana-apis.md#v12-service-accounts).
+ **OAuth and SAML session handling improvements** – Session handling for OAuth and SAML authentication providers has been improved for better reliability and security.
+ **Entra Workload Identity support** – Grafana now supports Microsoft Entra Workload Identity for authentication in Azure environments.
+ **OAuth2 for Alertmanager and Mimir** – You can now configure OAuth2 authentication in HTTP settings for vanilla Alertmanager and Mimir data sources.

**Accessibility**
+ **GeoMap keyboard support** – GeoMap visualizations now support keyboard navigation for improved accessibility.
+ **Panel shortcut keyboard support** – Dashboard panels now support keyboard shortcuts for common actions.
+ **Heading and reduced motion improvements** – Heading structure has been improved for screen readers, and reduced motion support has been added for users who prefer minimal animation.

**Breaking changes**

**Important**  
**Legacy alerting is entirely removed** – Legacy alerting is completely removed in Amazon Managed Grafana v12, and workspaces with legacy alerting settings will fail to start. You must migrate from legacy alerting to Grafana Alerting before upgrading to v12. See [Migrating classic dashboard alerts to Grafana alerting](v10-alerting-use-grafana-alerts.md) and [Classic dashboard alerts](old-alerts-overview.md).

**Important**  
**AngularJS support is removed** – AngularJS support is completely removed in Amazon Managed Grafana v12, so Angular-based plugins will not load and dashboards using them will display errors. You must migrate all Angular-based plugins to React alternatives before upgrading. See [Find plugins with the plugin catalog](grafana-plugins.md#plugin-catalog) for managing plugins in your workspace.

**Important**  
**API keys are removed** – API keys are fully removed in Amazon Managed Grafana v12 in favor of service accounts, and existing API keys will no longer function. You must create service accounts to replace all API keys and update automation to use service account tokens before upgrading. See [Using service accounts](v12-authenticating-grafana-apis.md#v12-service-accounts).

**Important**  
**Alert rule evaluation result limit** – The number of query evaluation results per alert rule is now limited to 500. If the condition query of an alert rule produces more results than this limit, the evaluation results in an error. To receive alerts when this error occurs, configure `Alert state if execution error or timeout` to `Error` under the alert rule's settings. See [State and health of alerting rules](v12-alerting-explore-state.md).

**Important**  
**Annotations limited to 3 million** – The number of annotations is now limited to 3 million per workspace. If more than 3 million annotations are created, the oldest annotations will be deleted first.
+ **Input data source is removed** – The Input data source plugin has been completely removed, so you must migrate affected dashboards to the TestData data source before upgrading. See [TestData Documentation](https://grafana.com/docs/grafana/latest/datasources/testdata/) in the *Grafana Labs documentation*.
+ **Query filtering behavior changes** – The "Disable query" button is now "Hide response/Show response" and hidden queries' responses are no longer returned to panels, so review your query configurations and update panels if data is missing after upgrading. See [Query Filtering Changes](https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v11-0/#data-sources-query-filtering-changes) in the *Grafana Labs documentation*.
+ **Data source UIDs must follow stricter format** – Data source UIDs must now use only alphanumeric characters, hyphens, and underscores, so you should update any non-compliant UIDs and their dashboard references before upgrading. See [Stricter Data Source UID Format](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v12-0/#enforcing-stricter-data-source-uid-format) in the *Grafana Labs documentation*.
+ **Panel view URLs changed for repeated panels** – The URL format for viewing individual repeated panels has changed and old URLs will return "Panel not found" errors, so update any bookmarks or automation by opening panels in view mode to get the new URLs. See [Panel View URL Changes](https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v11-0/#changes-to-how-the-panel-view-url-is-generated-for-repeated-panels) in the *Grafana Labs documentation*.
+ **Folders with forward slashes require escaped matchers** – The introduction of subfolders can break alert rules tied to folders containing forward slashes, so update notification policies with escaped matchers (for example, `grafana_folder=MyFolder\/sub-folder`) or rename folders to remove forward slashes before upgrading. See [Creating dashboard folders](v12-dash-managing-dashboards.md#v12-dash-create-dashboard-folder) and [Configure notification policies](v12-alerting-configure-notification-policies.md).
+ **Alert template $value variable behavior changes** – The `$value` variable in alert notification templates now returns the query value when querying a single data source, so review alert templates that use `$value` and update formatting if needed. See [Templating labels and annotations](v12-alerting-overview-labels-templating.md).
+ **Alert rule access permissions relaxed** – Permission requirements for accessing alert rules have been relaxed. See [Using permissions](Grafana-permissions.md) and [What's new in Grafana v11.1](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v11-1/#removes-requirement-of-datasourcesquery-permission-for-reading-rules) in the *Grafana Labs documentation*.
+ **Recording rules enabled by default** – Recording rules are now enabled by default in Grafana Alerting. See [Configure recording rules](v12-alerting-configure-recordingrules.md).
+ **Internal Alertmanager config POST endpoint removed** – The POST endpoint for the internal Grafana Alertmanager config has been removed, so you must update API integrations to use the new provisioning endpoints (for example, `POST /api/v1/provisioning/alert-rules`) before upgrading.
+ **Viewer and Editor permissions expanded** – Viewers can now read and write annotations and Editors can create and delete annotations. See [Using permissions](Grafana-permissions.md).
+ **Creator permissions changed** – The permissions granted to the creator of a resource (such as a dashboard or folder) have changed, so review your access control settings after upgrading. See [Change to creator permissions](https://grafana.com/whats-new/2025-10-16-change-to-creator-permissions/) in the *Grafana Labs documentation*.
+ **API key associated permissions removed** – Permissions previously associated with API keys have been removed as part of the full migration to service accounts. See [Removal of API key associated permissions](https://grafana.com/whats-new/2025-10-03-removal-of-api-key-associated-permissions/) in the *Grafana Labs documentation*.
+ **SNS contact point migration** – SNS contact points are automatically migrated to a newer SNS notifier. This migration does not require any manual action. However, the contact point settings schema for SNS has changed. See [Create notification channel](v12-Grafana-API-AlertingNotificationChannels.md#v12-Grafana-API-AlertNotificationChannels-Create) for an example of the updated request format.
+ **Alert rule evaluation result limit** – The number of query evaluation results per alert rule is now limited to 500. If the condition query of an alert rule produces more results than this limit, the evaluation results in an error. To receive alerts when this error occurs, Configure `Alert state if execution error or timeout` to `Error` under the alert rule's settings.
+ **SigV4 authentication removed from Core Prometheus plugin** – SigV4 authentication support in the Core Prometheus plugin has been removed. When you upgrade to Grafana version 12, all Amazon Managed Service for Prometheus data sources that were previously using the Core Prometheus plugin are automatically migrated to the Amazon Managed Service for Prometheus plugin. Any dashboards using these data sources are automatically updated to reflect this change. See [Connect to an Amazon Managed Service for Prometheus data source](amazon-prometheus-data-source.md).
+ **OpsGenie contact point removed** – The OpsGenie contact point is removed in Grafana version 12.

Amazon Managed Grafana v12 includes features from open source Grafana v11.0 through v12.4. For AWS-specific features, see the Amazon Managed Grafana User Guide. For detailed information about what's new, see [What's new in Grafana](https://grafana.com/docs/grafana/latest/whatsnew/) for v11.x and v12.x in the *Grafana Labs documentation*. Versions 11.x and 12.x include changes that might break functionality, so test in a non-production environment before updating production workspaces.

For more details on breaking changes, see the following topics in the *Grafana Labs documentation*:

**Grafana 12**
+ [What's new in Grafana v12.4](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v12-4/)
+ [What's new in Grafana v12.3](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v12-3/)
+ [What's new in Grafana v12.2](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v12-2/)
+ [What's new in Grafana v12.1](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v12-1/)
+ [What's new in Grafana v12.0](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v12-0/)

**Grafana 11**
+ [What's new in Grafana v11.6](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v11-6/)
+ [What's new in Grafana v11.5](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v11-5/)
+ [What's new in Grafana v11.4](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v11-4/)
+ [What's new in Grafana v11.3](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v11-3/)
+ [What's new in Grafana v11.2](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v11-2/)
+ [What's new in Grafana v11.1](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v11-1/)
+ [What's new in Grafana v11.0](https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v11-0/)

## Grafana version 10
<a name="version-diff-v10"></a>

The following features were added in Grafana version 10.
+ **Correlations** – Correlations define how data in one data source is used to query data in another data source, and allow the Explore visualization to easily run queries related to the shown data. For more details, see [Correlations in Grafana version 10](v10-correlations.md).
+ **Subfolders** – When organizing your dashboards, you can now use subfolders to create a nested hierarchy. For more details, see [Creating dashboard folders](v10-dash-managing-dashboards.md#v10-dash-create-dashboard-folder).
+ **Alerts** – Grafana alerting now supports silencing alerts. Additionally, Grafana alerting no longer sends notifications 3 times.
+ **Alerting upgrade preview** – Before upgrading from classic dashboard alerts to Grafana alerts, you can see what your alerts will look like, and even make changes that are applied when migrating. For more details, see [Migrating classic dashboard alerts to Grafana alerting](v10-alerting-use-grafana-alerts.md). Grafana Labs has announced that Grafana version 11 and beyond will no longer support classic dashboard alerts.
+ **Support bundles** – Support bundles provide a simple way to collect information about your Grafana workspace to share with product support. You can quickly create a support bundle containing data about migrations, plugins, settings, and more. For more details, see [Gather information for support](support-bundles.md).
+ **New visualizations** – Three new visualizations are available. [XY Chart](v10-panels-xychart.md), [Datagrid](v10-panels-datagrid.md), and [Trend panel](v10-panels-trend.md) are all available for workspaces compatible with version 10. Version 9 workspaces can also use XY Charts.
+ **PagerDuty** – The Enterprise plugins now include a plugin for PagerDuty.
+ **Transformations redesign** – The transformations tab has an improved user experience and visual design. Transformations are categorized, and each transformation type has an illustration to help you choose the right one.
+ **Prometheus metric encyclopedia** – The metrics dropdown for Prometheus metrics in the Prometheus query builder has been replaced with a paginated and searchable metric *encyclopedia*.
+ **API key UI discontinued** – [Service accounts](v12-authenticating-grafana-apis.md#v12-service-accounts) are the recommended way to authenticate calls to the Grafana HTTP APIs. As part of Grafana Labs work toward discontinuing API keys, you can no longer create API keys through the workspace user interface. You can only create API keys through the AWS APIs.

  For more information about the discontinuation of API keys by Grafana Labs, see [APIKeys: Sunsetting of API keys](https://github.com/grafana/grafana/issues/53567) in the Grafana GitHub issues list.

**Breaking changes**

The Grafana version 10.4 release includes changes from Grafana versions 9.5 through 10.4. Grafana versions 10.0 and 10.3 had some changes that might break functionality in some cases. When updating to a new version, it is recommended to test in a non-production environment before updating your production workspaces.

The following changes might affect some users updating to Grafana version 10.
+ **Angular discontinued** – Plugins that use Angular will no longer be supported in future releases of Grafana. In version 10, panels that use angular will show a banner stating that they use a discontinued feature, to give a notice that they won't work in future versions.
+ **Alias in CloudWatch removed** – Alias patterns in the CloudWatch query editor were replaced by Label (dynamic labels).

  Open any dashboard that uses the Alias field, and save it. Alias is migrated to Label automatically.
+ **Older plugins need to be upgraded** – The plugins for Athena and Amazon Redshift data source must be updated in Grafana v10 workspaces. The Athena data source plugin must be version 2.9.3 or newer; the Amazon Redshift data source plugin must be version 1.8.3 or newer.

  For information on installing or upgrading plugins, see [Find plugins with the plugin catalog](grafana-plugins.md#plugin-catalog).
+ **DoiT BigQuery plugin no longer supported** – The DoiT BigQuery data source plugin is no longer supported. Use the official Grafana Labs BigQuery data source plugin instead.
+ **Transformation changes** – Grafana version 10 has made a few bug fix changes to field names and keys. For full details, see [Transformation breaking changes](https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v10-3/#transformations) in the Grafana Labs documentation.
+ **Data source permissions APIs** – The endpoints for accessing data source permissions have changed. For full details, see [Data source permissions changes](https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v10-3/#data-source-permissions) in the Grafana Labs documentation.

For more details on breaking changes, see the following topics in the *Grafana Labs documentation*:
+ [Breaking changes in Grafana v10.0](https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v10-0/)
+ [Breaking changes in Grafana v10.3](https://grafana.com/docs/grafana/latest/breaking-changes/breaking-changes-v10-3/)

## Grafana version 9
<a name="version-diff-v9"></a>

The following features were added in Grafana v9.
+ **Alerting**: Grafana-managed alert rules now supports group names.
+ **Explore**: Create a dashboard from within Explore view.
+ **Prometheus queries**: A new query builder for Prometheus queries (using PromQL) makes writing queries easier.
+ **Loki queries**: A new query builder for Loki queries (using LogQL) makes writing queries easier.
+ **API tokens / Service accounts**: Service accounts simplify machine access in Grafana, helping you to manage API tokens.
+ **Plugin management**: You can enable plugin management to install, remove, or update community plugins in your workspace. This gives you access to more data sources and visualizations, and gives you control over the version of each plugin that you use.
+ **Trace to metrics**: Configure a tracing data source to add links to metrics with queries and tags.
+ **Canvas panel**: A new panel visualization with static and dynamic elements to create data-driven, custom panels with images and overlain text.
+ **Reorganized interface**: Updated UI with easier navigation in the Grafana console.
+ **CloudWatch**: The Amazon CloudWatch data source can now monitor metrics across AWS accounts and across AWS Regions.
+ **Logs**: The interface for log details has been improved.
+ **General**: Bug fixes and minor improvements throughout.

**Breaking changes**

The Grafana version 9.4 release includes a range of new features and improvements, building upon previous versions. This version had some changes that might break functionality in some cases. When updating to a new version, we recommend you test in a non-production environment before updating your production workspaces.

The following changes might affect some users updating to Grafana version 9.4. For a detailed list of these changes, see the [Grafana 9.4 changelog](https://github.com/grafana/grafana/blob/release-9.4.17/CHANGELOG.md) on *GitHub*.
+ **API discontinued** – The `/api/tsdb/query` API has been removed.

  **Action required:** Use `/api/ds/query` instead. See [Query a data source](https://grafana.com/docs/grafana/latest/http_api/data_source/#query-a-data-source) in the *Grafana public documentation* and Issue [\#49916](https://github.com/grafana/grafana/issues/49916) on *GitHub*.
+ **API endpoint changes** – Several alerting API endpoints now require data source UID instead of numeric ID.

  **Affected endpoints:** `api/v1/rule/test`, `api/prometheus/`, `api/ruler/`, `api/alertmanager/`

  **Action required:** Update API calls to use data source UID as path parameter. See Issues [\#48070](https://github.com/grafana/grafana/issues/48070), [\#48052](https://github.com/grafana/grafana/issues/48052), [\#48046](https://github.com/grafana/grafana/issues/48046), and [\#47978](https://github.com/grafana/grafana/issues/47978) on *GitHub*.
+ **Azure Monitor queries removed** – Application Insights and Insight Analytics queries are no longer supported.

  Deprecated in Grafana 8.0, removed in 9.0. Deprecated queries will not execute.

  **Action required:** See [Azure Monitor data source](https://grafana.com/docs/grafana/latest/datasources/azuremonitor/deprecated-application-insights/) in the *Grafana public documentation* for migration guidance.
+ **Browser access mode removed** – Browser access mode is no longer available for InfluxDB and Prometheus data sources.

  **Action required:** Switch to server access mode in your data source configuration. InfluxDB: Deprecated in 8.0.0, removed in 9.2.0. See Issue [\#53529](https://github.com/grafana/grafana/issues/53529) on *GitHub*. Prometheus: Deprecated in 7.4.0, removed in 9.2.0. See Issue [\#50162](https://github.com/grafana/grafana/issues/50162) on *GitHub*.
+ **Dashboard settings access restricted** – You can no longer open dashboard settings while editing panels.

  Dashboard settings are locked when panel edit mode is active. Close panel edit mode before accessing dashboard settings. See Issue [\#54746](https://github.com/grafana/grafana/issues/54746) on *GitHub*.
+ **Data source password encryption** – Unencrypted passwords are no longer supported.

  **Action required:** Use `secureJsonData.password` and `secureJsonData.basicAuthPassword`. Previously discontinued in v8.1.0. See Issue [\#49987](https://github.com/grafana/grafana/issues/49987) on *GitHub*.
+ **Default data source behavior** – Default data source selection no longer affects existing panels.

  Default data source only applies to new panels. Changing the default won't update existing dashboards. Previously saved panels retain their data source configuration. See Issue [\#45132](https://github.com/grafana/grafana/issues/45132) on *GitHub*.
+ **Elasticsearch interval property changed** – Query interval specification updated for Elasticsearch 7.x.

  Changed from `interval` to `fixed_interval` property. Provides consistency with Elasticsearch 8.x. Most queries won't show visible changes. See Issue [\#50297](https://github.com/grafana/grafana/issues/50297) on *GitHub*.
+ **Elasticsearch Raw document mode discontinued** – Display mode changes in Elasticsearch data source.

  **Action required:** Use **Raw Data** mode instead. See Issue [\#62236](https://github.com/grafana/grafana/issues/62236) on *GitHub*.
+ **Elasticsearch version support** – Older Elasticsearch versions are no longer supported.

  **Action required:** Upgrade Elasticsearch to version 7.10.0 or later. Versions below 7.10.0 are past end-of-life. See Issue [\#48715](https://github.com/grafana/grafana/issues/48715) on *GitHub*.
+ **Explore URL format discontinued** – Compact Explore URLs will be removed in a future release.

  **Action required:** Update hard coded links to use standard URL format. Compact URLs: `&left=["now-1h","now"...]`. Standard URLs: `&left={"datasource":"test"...}`. See Issue [\#50873](https://github.com/grafana/grafana/issues/50873) on *GitHub*.
+ **GitHub OAuth display changes** – GitHub name and login display updated.

  GitHub name appears as Grafana name. GitHub login appears as Grafana login. Improves user identification clarity. See Issue [\#45438](https://github.com/grafana/grafana/issues/45438) on *GitHub*.
+ **Heatmap panel implementation updated** – Heatmap panels use a new implementation starting in 9.1.0.

  Significantly improved rendering performance. Buckets are placed on reasonable borders (1m, 5m, 30s). Round cells are no longer supported.

  **Action required:** Test your heatmap panels after upgrade. Disable new implementation by setting `useLegacyHeatmapPanel` feature flag to true if needed. Add `?__feature.useLegacyHeatmapPanel=true` to dashboard URLs for testing. See Issue [\#50229](https://github.com/grafana/grafana/issues/50229) on *GitHub*.
+ **InfluxDB backend migration** – InfluxDB data parsing behavior has changed.

  The InfluxDB backend migration feature toggle (`influxdbBackendMigration`) is reintroduced due to backend processing issues. By default, InfluxDB data is parsed in the frontend. If you upgraded to 9.4.4 and added transformations on InfluxDB data, those panels will fail to render.

  **Action required:** Remove affected panels and recreate them, or edit the `time` field as `Time` in `panel.json` or `dashboard.json`. See Issue [\#64842](https://github.com/grafana/grafana/issues/64842) on *GitHub*.
+ **Log message format updated** – Log message structure has changed.

  `lvl` is now `level`. `eror` and `dbug` are now `error` and `debug`. Increased timestamp precision. Opt-out available with `oldlog` feature toggle (temporary). See Issue [\#47584](https://github.com/grafana/grafana/issues/47584) on *GitHub*.
+ **Loki data format optimization** – Loki logs data uses a more efficient dataframe format.

  Single dataframe with **labels** column instead of separate dataframes. Explore and logs panels work without changes. Other panels or transforms may need adjustment.

  **Action required:** Replace **labels to fields** transformation with **extract fields** transformation. See Issue [\#47153](https://github.com/grafana/grafana/issues/47153) on *GitHub*.
+ **NaN value handling** – Consistent `NaN` representation across Prometheus and Loki data sources.

  `NaN` values remain as `NaN` instead of converting to `null`. Change should be mostly invisible to users. Affects both dashboard and alerting paths. See Issues [\#49475](https://github.com/grafana/grafana/issues/49475) and [\#45389](https://github.com/grafana/grafana/issues/45389) on *GitHub*.
+ **Password reset links invalidated** – Existing password reset links won't work after upgrade.

  Password reset links sent before upgrade are invalid. Users must request new password reset links. Links expire after 2 hours. See Issue [\#42334](https://github.com/grafana/grafana/issues/42334) on *GitHub*.
+ **Reserved label prefix** – Labels starting with `grafana_` are reserved.

  Manually configured labels beginning with `grafana_` may be overwritten. Current reserved labels: `grafana_folder` (Title of the folder containing the alert). See Issue [\#50262 ](https://github.com/grafana/grafana/issues/50262) on *GitHub*.
+ **Transformation improvements** – **Rename by regex** transformation now supports global patterns.

  Global patterns use the format `/<stringToReplace>/g`. Some transformations may behave differently. Wrap match strings in forward slashes for previous behavior: `(.*)` becomes `/(.*)/`. See Issue [\#48179 ](https://github.com/grafana/grafana/issues/48179) on *GitHub*.