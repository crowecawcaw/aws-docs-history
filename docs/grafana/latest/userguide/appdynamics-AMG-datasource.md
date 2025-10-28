# Connect to an AppDynamics data

source

The AppDynamics data source for Amazon Managed Grafana enables you to query metrics from
AppDynamics using its Metrics API and visualize them in Grafana dashboards.

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

## Note on the Data source

configuration

Use Server (proxy) access (to avoid CORS and users looking up your password)
and basic authentication. Remember that the username should be
"user@account", (that is, your.name@customer1 or
my_user@saas_account_name).

Configure the password using the following steps:

1. Navigate to [https://accounts.appdynamics.com/subscriptions](https://accounts.appdynamics.com/subscriptions "https://accounts.appdynamics.com/subscriptions")
2. Choose the link in the **Name** column on the row
   for your subscription.
3. Navigate to the **License details** by choosing the
   tab at top of the page.
4. The Access Key field has a **Show** button. Choose
   the **Show** button to show the Access Key.
5. Copy the Access Key into the Password field in the Basic Auth Details
   on config page in Grafana.

Set up a user and role for Amazon Managed Grafana using the following steps.

1. In AppDynamics, navigate to Settings, Administration.
2. Select the **Roles** tab, and choose the
   "+" button to create a new role; for
   example, `grafana_readonly.`
3. In the **Account** tab of the Create
   Role section, add the permission `View Business Flow`.
4. In the **Applications** tab, check the
   **View** box to allow Grafana to view application
   data.
5. In the **Databases** tab, check the
   **View** box to allow Grafana to view database
   data.
6. In the **Analytics** tab, check the
   **Can view data from all Applications** box to
   allow Grafana to view application analytics data.
7. In the **Users** tab of the
   Administration page, create a new user; for
   example, `grafana`. Assign the new user (or a Group to
   which the user belongs) to the role you just created; for
   example, `grafana_readonly`.

## Templating

The supported template queries for now are:

1. `Applications` (All Applications)
2. `AppName.BusinessTransactions` (All BTs for the Application
   Name)
3. `AppName.Tiers` (All Tiers for the Application Name)
4. `AppName.Nodes` (All Nodes for the Application Name)
5. `AppName.TierName.BusinessTransactions` (All BTs for a
   specific Tier)
6. `AppName.TierName.Nodes` (All Nodes for a specific Tier)
7. `AppName.Path.<Any Metric Path>` (Any metric Path can
   be specified)

## Legend keys

The default for the legend key can be quite long but this formatting can be
customized.

The legend key can be prefixed with the application name by choosing the
`App on legend` option. For example: `MyApp - Overall
 Application Performance|Average Response Time (ms)`.

If the query is for a singlestat or other panel where you cannot see the
legend key, then choose the Show Metadata option to see what the legend key
(also called an alias) for the query is.

The Legend dropdown list has three options: `Full Path`,
`Segments` and `Custom`.

### Legend option – full

path

The legend key is the full metric path; for example, `Overall
 Application Performance|Average Response Time (ms)`.

### Legend option –

segments

The metric name is made up of segments. You can choose which segments to
show.

For example, with a metric name:

`Errors|mywebsite|Error|Errors per Minute`

entering the following `2,4` in the Segments field returns
`mywebsite|Errors per minute`.

The indexing starts with 1 so `1` returns `Errors`.

### Legend option –

custom

Create a custom legend by combining text with the following aliasing
patterns to be able to mix in metric metadata.

- `{{app}}` returns the Application name
- `{{1}}` returns a segment from the metric path.

For example, the metric: `Overall Application
 Performance|Average Response Time (ms)` has two segments.
`{{1}}` returns the first segment, `{{2}}`
returns the second segment.

Examples of legend key patterns and the legend keys that are generated:

- `custom legend key` => `custom legend key`
- `App: {{app}} MetricPart2: {{2}}` => `App: myApp
MetricPart2: Average Response Time (ms)`
